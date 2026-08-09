"""Draw hand-sketched diagrams, in the deck palette, as SVG and PNG.

An image model cannot be trusted with the text inside a picture, and a figure
whose label reads "ZeroDivisionErrar" is worse than no figure. So the technical
diagrams are drawn rather than generated: exact labels, exact palette, free,
reproducible, and diffable in git.

The sketchy look comes from perturbing every stroke with a seeded noise function
and drawing it twice, the way roughjs does. Same seed, same drawing, every run.

Everything reduces to two primitives, a stroked polyline and an even-odd filled
contour set, so the same recording emits SVG and rasterises with Pillow. Labels
are converted to outlines, which means no font has to be installed to view them.
"""
from __future__ import annotations

import functools
import math
import os

from fontTools.pens.recordingPen import DecomposingRecordingPen
from fontTools.pens.transformPen import TransformPen
from fontTools.ttLib import TTFont
from PIL import Image, ImageChops, ImageDraw

# palette, kept in sync with tokens.PYTHON
INK, BLUE, YELLOW, PAPER = '#0B1B3A', '#3776AB', '#FFD43B', '#F7F8FA'
BLUE_WASH, YELLOW_WASH, MUTED = '#DCE8F2', '#FFF3C4', '#5B6B84'
WOOD, WOOD_WASH = '#8A6A00', '#EADCB4'   # the one warm pair, for wood

FONTS = os.path.join(os.environ.get('WINDIR', r'C:\Windows'), 'Fonts')
HAND_FILE = os.path.join(FONTS, 'Inkfree.ttf')     # Ink Free ships with Windows
MONO_FILE = os.path.join(FONTS, 'consola.ttf')

CURVE_STEPS = 12


def _rgb(h: str) -> tuple[int, int, int]:
    h = h.lstrip('#')
    return int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16)


def _quad(p0, p1, p2, steps=CURVE_STEPS):
    out = []
    for i in range(steps + 1):
        t = i / steps
        u = 1 - t
        out.append((u * u * p0[0] + 2 * u * t * p1[0] + t * t * p2[0],
                    u * u * p0[1] + 2 * u * t * p1[1] + t * t * p2[1]))
    return out


def _cubic(p0, p1, p2, p3, steps=CURVE_STEPS):
    out = []
    for i in range(steps + 1):
        t = i / steps
        u = 1 - t
        out.append((u**3 * p0[0] + 3 * u * u * t * p1[0] + 3 * u * t * t * p2[0] + t**3 * p3[0],
                    u**3 * p0[1] + 3 * u * u * t * p1[1] + 3 * u * t * t * p2[1] + t**3 * p3[1]))
    return out


@functools.lru_cache(maxsize=8)
def _font(path: str):
    f = TTFont(path, fontNumber=0, lazy=True)
    return f.getGlyphSet(), f.getBestCmap(), f['head'].unitsPerEm


def glyph_contours(s: str, x: float, y: float, size: float, font_path: str,
                   anchor: str = 'middle') -> tuple[list[list[tuple]], float]:
    """Text as closed contours, ready to fill with the even-odd rule."""
    glyphs, cmap, upem = _font(font_path)
    scale = size / upem
    names, widths = [], []
    for ch in s:
        name = cmap.get(ord(ch)) or cmap.get(ord('?')) or '.notdef'
        names.append(name)
        widths.append(glyphs[name].width * scale)
    total = sum(widths)
    cursor = {'start': x, 'middle': x - total / 2, 'end': x - total}[anchor]

    contours: list[list[tuple]] = []
    for name, w in zip(names, widths):
        # decomposing, so accented glyphs (í, ó, ñ) resolve their components
        rec = DecomposingRecordingPen(glyphs)
        glyphs[name].draw(TransformPen(rec, (scale, 0, 0, -scale, cursor, y)))
        cur: list[tuple] = []
        start: tuple = ()      # every contour opens with moveTo, which sets it
        for op, args in rec.value:
            if op == 'moveTo':
                if len(cur) > 2:
                    contours.append(cur)
                start = args[0]
                cur = [start]
            elif op == 'lineTo':
                cur.append(args[0])
            elif op == 'qCurveTo':
                pts = list(args)
                on = pts[-1]          # None here means an implied point
                ctrl = pts[:-1]
                # TrueType allows implied on-curve points between two controls
                prev = cur[-1]
                for i, c in enumerate(ctrl):
                    nxt: tuple
                    if i == len(ctrl) - 1:
                        nxt = on if on is not None else start
                    else:
                        nxt = ((c[0] + ctrl[i + 1][0]) / 2,
                               (c[1] + ctrl[i + 1][1]) / 2)
                    cur.extend(_quad(prev, c, nxt, 8)[1:])
                    prev = nxt
            elif op == 'curveTo':
                pts = list(args)
                cur.extend(_cubic(cur[-1], pts[0], pts[1], pts[2], 8)[1:])
            elif op == 'closePath':
                if len(cur) > 2:
                    contours.append(cur)
                cur = []
        if len(cur) > 2:
            contours.append(cur)
        cursor += w
    return contours, total


class Pen:
    """A seeded sketch pen. Records strokes and fills; emits SVG or PNG."""

    def __init__(self, w: int, h: int, seed: int = 7, roughness: float = 1.0):
        self.w, self.h = w, h
        self._s = (seed & 0x7FFFFFFF) or 7
        self.roughness = roughness
        self.ops: list[tuple] = []

    # deterministic PRNG, so a rebuild does not reshuffle the drawing
    def _rand(self) -> float:
        self._s = (1103515245 * self._s + 12345) & 0x7FFFFFFF
        return self._s / 0x7FFFFFFF

    def _j(self, amount: float = 1.0) -> float:
        return (self._rand() - 0.5) * 2 * amount * self.roughness

    def _stroke(self, points, width, color):
        self.ops.append(('stroke', [(float(a), float(b)) for a, b in points],
                         float(width), color))

    def _fill(self, contours, color):
        self.ops.append(('fill', contours, color))

    # ── strokes
    def line(self, x1, y1, x2, y2, w=2.4, color=INK, passes=2, wobble=1.7):
        for _ in range(passes):
            mx, my = (x1 + x2) / 2, (y1 + y2) / 2
            self._stroke(_quad((x1 + self._j(wobble), y1 + self._j(wobble)),
                               (mx + self._j(wobble * 2), my + self._j(wobble * 2)),
                               (x2 + self._j(wobble), y2 + self._j(wobble))), w, color)
        return self

    def arc(self, cx, cy, r, a0, a1, w=2.4, color=INK, passes=2):
        for _ in range(passes):
            steps = max(5, int(abs(a1 - a0) / 10))
            pts = []
            for i in range(steps + 1):
                a = math.radians(a0 + (a1 - a0) * i / steps)
                pts.append((cx + r * math.cos(a) + self._j(1.1),
                            cy + r * math.sin(a) + self._j(1.1)))
            self._stroke(pts, w, color)
        return self

    def rect(self, x, y, rw, rh, r=12, w=2.4, color=INK, fill=None):
        if fill:
            self._fill([[(x + r, y), (x + rw - r, y), (x + rw, y + r),
                         (x + rw, y + rh - r), (x + rw - r, y + rh), (x + r, y + rh),
                         (x, y + rh - r), (x, y + r)]], fill)
        self.line(x + r, y, x + rw - r, y, w, color)
        self.line(x + rw, y + r, x + rw, y + rh - r, w, color)
        self.line(x + rw - r, y + rh, x + r, y + rh, w, color)
        self.line(x, y + rh - r, x, y + r, w, color)
        for cx, cy, a0 in ((x + rw - r, y + r, -90), (x + rw - r, y + rh - r, 0),
                           (x + r, y + rh - r, 90), (x + r, y + r, 180)):
            self.arc(cx, cy, r, a0, a0 + 90, w, color, passes=1)
        return self

    def ellipse(self, cx, cy, rx, ry, w=2.4, color=INK, fill=None, passes=2):
        if fill:
            self._fill([[(cx + rx * math.cos(2 * math.pi * i / 40),
                          cy + ry * math.sin(2 * math.pi * i / 40)) for i in range(40)]],
                       fill)
        for _ in range(passes):
            pts = [(cx + rx * math.cos(2 * math.pi * i / 28) + self._j(1.4),
                    cy + ry * math.sin(2 * math.pi * i / 28) + self._j(1.4))
                   for i in range(29)]
            self._stroke(pts, w, color)
        return self

    def wave(self, x1, y1, x2, y2, amp=8, w=2.4, color=INK, cycles=None):
        """A softly waving thread.

        The amplitude stays constant along the run and only eases off in the last
        few percent at each end, so the line lands cleanly without tapering to a
        point. A taper plus many cycles reads as a tadpole, not a thread.
        """
        dx, dy = x2 - x1, y2 - y1
        length = math.hypot(dx, dy) or 1
        nx, ny = -dy / length, dx / length
        n = max(24, int(length / 6))
        if cycles is None:
            cycles = 1.0 if length < 300 else 1.5
        pts = []
        for i in range(n + 1):
            t = i / n
            ease = min(1.0, min(t, 1 - t) * 8)     # only the outer eighth eases
            off = math.sin(t * math.pi * 2 * cycles) * amp * ease
            pts.append((x1 + dx * t + nx * off + self._j(0.6),
                        y1 + dy * t + ny * off + self._j(0.6)))
        self._stroke(pts, w, color)
        return self

    def arrow(self, x1, y1, x2, y2, w=2.4, color=INK, head=14, wavy=False):
        (self.wave if wavy else self.line)(x1, y1, x2, y2, **(
            {'w': w, 'color': color} if wavy else {'w': w, 'color': color}))
        a = math.atan2(y2 - y1, x2 - x1)
        for s in (+1, -1):
            b = a + s * math.radians(152)
            self.line(x2, y2, x2 + head * math.cos(b), y2 + head * math.sin(b),
                      w, color, passes=1)
        return self

    def cross(self, cx, cy, r=14, w=3.2, color=INK):
        self.line(cx - r, cy - r, cx + r, cy + r, w, color)
        self.line(cx + r, cy - r, cx - r, cy + r, w, color)
        return self

    def bracket(self, x1, x2, y, depth=14, w=2.4, color=INK):
        self.line(x1, y, x1, y + depth, w, color, passes=1)
        self.line(x1, y + depth, x2, y + depth, w, color)
        self.line(x2, y + depth, x2, y, w, color, passes=1)
        return self

    # ── shapes the course illustrations keep needing
    def poly(self, points, w=2.4, color=INK, fill=None, close=True):
        pts = list(points)
        if fill:
            self._fill([pts], fill)
        seq = pts + [pts[0]] if close else pts
        for a, b in zip(seq, seq[1:]):
            self.line(a[0], a[1], b[0], b[1], w, color, passes=2, wobble=1.3)
        return self

    def triangle(self, cx, cy, r, w=2.4, color=INK, fill=None):
        return self.poly([(cx, cy - r), (cx + r * 0.88, cy + r * 0.6),
                          (cx - r * 0.88, cy + r * 0.6)], w, color, fill)

    def diamond(self, cx, cy, rx, ry, w=2.4, color=INK, fill=None):
        return self.poly([(cx, cy - ry), (cx + rx, cy), (cx, cy + ry), (cx - rx, cy)],
                         w, color, fill)

    def rhomboid(self, cx, cy, rw, rh, skew=0.28, w=2.4, color=INK, fill=None):
        s = rw * skew
        return self.poly([(cx - rw / 2 + s, cy - rh / 2), (cx + rw / 2 + s, cy - rh / 2),
                          (cx + rw / 2 - s, cy + rh / 2), (cx - rw / 2 - s, cy + rh / 2)],
                         w, color, fill)

    def scribble(self, cx, cy, r, loops=26, w=2.2, color=INK):
        """A dense tangle: the drawing of a problem before anyone has sorted it.

        A wandering point with momentum, steered back toward the middle whenever it
        drifts past the radius. Anything periodic here turns into a rosette or a
        spiral, which reads as decoration rather than mess.
        """
        x, y = cx + r * 0.3, cy
        heading = 0.0
        pts = [(x, y)]
        step = r * 0.16
        for _ in range(loops * 13):
            dist = math.hypot(x - cx, y - cy)
            heading += (self._rand() - 0.5) * 1.5
            if dist > r * 0.92:                     # steer home before leaving the disc
                inward = math.atan2(cy - y, cx - x)
                delta = (inward - heading + math.pi) % (2 * math.pi) - math.pi
                heading += delta * 0.55
            x += step * math.cos(heading)
            y += step * 0.86 * math.sin(heading)
            pts.append((x, y))
        self._stroke(pts, w, color)
        return self

    def coil(self, cx, cy, r, w=2.2, color=INK, fill=None):
        """A tidy ball of yarn: the same thread, wound."""
        self.ellipse(cx, cy, r, r * 0.92, w, color, fill=fill, passes=1)
        for a in (-32, 0, 32):
            ar = math.radians(a)
            self.arc(cx + r * 0.1 * math.cos(ar), cy, r * 0.86, -70 + a, 110 + a,
                     w * 0.8, color, passes=1)
        return self

    def sun(self, cx, cy, r, spikes=14, w=2.6, color=INK, fill=None):
        self.ellipse(cx, cy, r, r * 0.92, w, color, fill=fill)
        for i in range(spikes):
            a = 2 * math.pi * i / spikes
            self.line(cx + r * 1.02 * math.cos(a), cy + r * 0.94 * math.sin(a),
                      cx + r * 1.30 * math.cos(a), cy + r * 1.22 * math.sin(a),
                      w * 0.8, color, passes=1)
        return self

    def ladder(self, cx, top, h, w_=90, rungs=7, w=2.6, color=INK, fill=None):
        lean = h * 0.10
        for s in (-1, 1):
            self.line(cx + s * w_ / 2 - lean, top, cx + s * w_ / 2 + lean * 0.4, top + h,
                      w, color)
        for i in range(rungs):
            t = (i + 0.6) / (rungs + 0.4)
            y = top + h * t
            x = cx - lean * (1 - t) + lean * 0.4 * t
            if fill:
                self._fill([[(x - w_ / 2, y - 7), (x + w_ / 2, y - 7),
                             (x + w_ / 2, y + 7), (x - w_ / 2, y + 7)]], fill)
            self.line(x - w_ / 2, y, x + w_ / 2, y, w * 0.85, color, passes=1)
        return self

    def monitor(self, x, y, mw, mh, w=2.6, color=INK, fill=None):
        self.rect(x, y, mw, mh, r=14, w=w, color=color, fill=fill)
        self.line(x + mw * 0.36, y + mh, x + mw * 0.36, y + mh + mh * 0.16, w, color, 1)
        self.line(x + mw * 0.64, y + mh, x + mw * 0.64, y + mh + mh * 0.16, w, color, 1)
        self.line(x + mw * 0.24, y + mh + mh * 0.16, x + mw * 0.76, y + mh + mh * 0.16,
                  w, color)
        return self

    def chip(self, cx, cy, s, w=2.6, color=INK, fill=None, pins=5):
        self.rect(cx - s / 2, cy - s / 2, s, s, r=10, w=w, color=color, fill=fill)
        for i in range(pins):
            t = (i + 1) / (pins + 1)
            self.line(cx - s / 2 - s * 0.13, cy - s / 2 + s * t,
                      cx - s / 2, cy - s / 2 + s * t, w * 0.7, color, 1)
            self.line(cx + s / 2, cy - s / 2 + s * t,
                      cx + s / 2 + s * 0.13, cy - s / 2 + s * t, w * 0.7, color, 1)
            self.line(cx - s / 2 + s * t, cy - s / 2 - s * 0.13,
                      cx - s / 2 + s * t, cy - s / 2, w * 0.7, color, 1)
            self.line(cx - s / 2 + s * t, cy + s / 2,
                      cx - s / 2 + s * t, cy + s / 2 + s * 0.13, w * 0.7, color, 1)
        return self

    def robot(self, cx, top, h, w=2.4, color=INK, fill=None):
        bw = h * 0.62
        self.rect(cx - bw / 2, top + h * 0.30, bw, h * 0.52, r=12, w=w, color=color,
                  fill=fill)
        self.rect(cx - bw * 0.34, top, bw * 0.68, h * 0.26, r=10, w=w, color=color,
                  fill=fill)
        for s in (-1, 1):
            self.ellipse(cx + s * bw * 0.14, top + h * 0.13, h * 0.030, h * 0.030,
                         1.8, color, fill=color, passes=1)
        self.line(cx, top, cx, top - h * 0.12, w * 0.8, color, 1)
        self.ellipse(cx, top - h * 0.16, h * 0.028, h * 0.028, 1.8, color, passes=1)
        for s in (-1, 1):
            self.line(cx + s * bw / 2, top + h * 0.44, cx + s * bw * 0.78,
                      top + h * 0.62, w * 0.8, color, 1)
        self.line(cx - bw * 0.34, top + h * 0.82, cx + bw * 0.34, top + h * 0.82,
                  w * 0.8, color, 1)
        return self

    # ── the duck, the character of the course
    def duck(self, cx, cy, h=180, mood='happy', wing='down', facing='right',
             fill=None, color=INK, hat=None, feet=True):
        """The rubber duck, drawn loose, following the shape of the course logo.

        Body and head are two overlapping circles whose silhouette is stroked as
        one outline: the seam between them is never drawn, which is what stops the
        bird reading as a snowman. ``cy`` is the top of the head.

        ``mood`` is happy, think, confused or wow. ``wing`` is down, tuck, point or
        up. ``hat`` adds a hard hat. ``feet`` can be turned off for a bath duck.
        """
        f = 1 if facing == 'right' else -1
        s = h / 180.0

        R, r = 74 * s, 42 * s                       # body and head radii
        bx, by = cx - f * 16 * s, cy + h - R - 14 * s
        hx, hy = bx + f * 62 * s, by - 62 * s

        # where the two circles cross, so the seam can be left undrawn
        dx, dy = hx - bx, hy - by
        d = math.hypot(dx, dy)
        aa = (R * R - r * r + d * d) / (2 * d)
        hh = math.sqrt(max(0.0, R * R - aa * aa))
        mxp, myp = bx + aa * dx / d, by + aa * dy / d
        px, py = -dy / d * hh, dx / d * hh
        i1, i2 = (mxp + px, myp + py), (mxp - px, myp - py)

        def ang(ox, oy, pt):
            return math.degrees(math.atan2(pt[1] - oy, pt[0] - ox)) % 360

        b1, b2 = ang(bx, by, i1), ang(bx, by, i2)
        n1, n2 = ang(hx, hy, i1), ang(hx, hy, i2)

        def outside(a0, a1, ox, oy, rr, oc, orad):
            """Of the two arcs between a0 and a1, keep the one outside circle ``oc``.

            The midpoint has to be farther from the other centre than the *other*
            circle's radius, not this one's. Comparing against the wrong radius is
            what makes a head disappear.
            """
            for lo, hi in ((a0, a1 if a1 > a0 else a1 + 360),
                           (a1, a0 if a0 > a1 else a0 + 360)):
                mid = math.radians((lo + hi) / 2)
                if math.hypot(ox + rr * math.cos(mid) - oc[0],
                              oy + rr * math.sin(mid) - oc[1]) > orad:
                    return lo, hi
            return a0, a1 if a1 > a0 else a1 + 360

        bl, bh = outside(b1, b2, bx, by, R, (hx, hy), r)
        nl, nh = outside(n1, n2, hx, hy, r, (bx, by), R)

        def arc_pts(ox, oy, rr, a0, a1, squash=1.0):
            n = max(8, int(abs(a1 - a0) / 7))
            return [(ox + rr * math.cos(math.radians(a0 + (a1 - a0) * i / n)),
                     oy + rr * squash * math.sin(math.radians(a0 + (a1 - a0) * i / n)))
                    for i in range(n + 1)]

        body = arc_pts(bx, by, R, bl, bh)
        head = arc_pts(hx, hy, r, nl, nh)
        tail = [(bx - f * R * 1.44, by - R * 0.66), (bx - f * R * 1.05, by - R * 0.86),
                (bx - f * R * 0.82, by - R * 0.30)]

        if fill:
            self._fill([body + head], fill)
            self._fill([tail], fill)
        for pts in (body, head):
            for _ in range(2):
                self._stroke([(qx + self._j(1.4), qy + self._j(1.4)) for qx, qy in pts],
                             2.6, color)
        self.poly(tail, 2.4, color, None)

        # a wide flat beak, upper and lower, the way a bath duck has it
        bx0, by0 = hx + f * r * 0.62, hy + r * 0.10
        # short and wide, rounded at the tip, tucked against the head
        upper = [(bx0, by0 - r * 0.26), (bx0 + f * r * 0.62, by0 - r * 0.30),
                 (bx0 + f * r * 0.90, by0 - r * 0.14),
                 (bx0 + f * r * 0.92, by0 + r * 0.06), (bx0, by0 + r * 0.12)]
        lower = [(bx0 + f * r * 0.10, by0 + r * 0.08),
                 (bx0 + f * r * 0.78, by0 + r * 0.06),
                 (bx0 + f * r * 0.60, by0 + r * 0.28),
                 (bx0 + f * r * 0.14, by0 + r * 0.26)]
        self.poly(upper, 2.2, color, YELLOW_WASH if fill else None)
        self.poly(lower, 1.9, color, None)

        self.ellipse(hx + f * r * 0.18, hy - r * 0.26, 5.6 * s, 6.6 * s,
                     1.6, color, fill=color, passes=1)
        if mood == 'confused':
            self.line(hx + f * r * 0.00, hy - r * 0.70, hx + f * r * 0.46,
                      hy - r * 0.56, 2.0, color, passes=1)
        elif mood == 'wow':
            self.arc(hx + f * r * 0.18, hy - r * 0.58, 9 * s, 200, 340, 2.0, color, 1)

        wx, wy = bx + f * 12 * s, by + 6 * s
        if wing in ('up', 'point'):
            deg = -54 if wing == 'up' else -6
            a = math.radians(deg if f > 0 else 180 - deg)
            ca, sa = math.cos(a), math.sin(a)
            L = (84 if wing == 'up' else 100) * s

            def put(qx, qy):
                return (wx + qx * ca - qy * sa, wy + qx * sa + qy * ca)

            top = [put(L * t, -24 * s * math.sin(math.pi * t) - 6 * s * (1 - t))
                   for t in [i / 16 for i in range(17)]]
            bot = [put(L * t, 22 * s * math.sin(math.pi * t) + 8 * s * (1 - t))
                   for t in [i / 16 for i in range(17)]]
            if fill:
                self._fill([top + bot[::-1]], fill)
            self._stroke(top, 2.4, color)
            self._stroke(bot, 2.4, color)
            for k in (0.42, 0.62):
                self.line(*put(L * k, -6 * s), *put(L * k, 12 * s), 1.6, color, passes=1)
        elif wing == 'tuck':
            self.arc(wx, wy, 34 * s, 150, 30, 2.4, color, passes=2)
        else:
            # the logo wing: a teardrop lying on the flank
            self.ellipse(wx - f * 4 * s, wy + 4 * s, 40 * s, 30 * s, 2.4, color, passes=2)
            self.arc(wx - f * 10 * s, wy - 2 * s, 24 * s, 205, 335, 1.8, color, 1)

        if feet:
            for dd in (-0.30, 0.26):
                fx = bx + f * R * dd
                self.line(fx, by + R * 0.90, fx, by + R * 1.16, 2.2, color, passes=1)
                self.poly([(fx - 15 * s, by + R * 1.16), (fx + 17 * s, by + R * 1.16),
                           (fx + 3 * s, by + R * 1.38)], 2.0, color,
                          YELLOW_WASH if fill else None)

        if hat:
            self.arc(hx, hy - r * 0.58, r * 0.88, 190, 350, 2.6, color, passes=2)
            self.line(hx - r * 1.12, hy - r * 0.56, hx + r * 1.12, hy - r * 0.56,
                      2.6, color)
            self.line(hx, hy - r * 1.42, hx, hy - r * 0.62, 1.8, color, passes=1)
        return self

    # ── the blob person, kept for scenes where a human reads better
    def blob(self, cx, cy, h=170, mood='happy', arms='down', fill=None, color=INK):
        """A marshmallow character: rounded body, dot eyes, small mouth, stick limbs.

        ``cy`` is the top of the head. ``mood`` is happy, think, confused or wow;
        ``arms`` is down, up, point-right, point-left or think.
        """
        bw = h * 0.52                       # body width
        top, bot = cy, cy + h
        # body: a capsule drawn as one wobbly closed outline
        pts = []
        for i in range(41):
            a = math.pi * 2 * i / 40
            # squash the bottom so it reads as standing, not floating
            rx = bw / 2
            ry = h / 2 * (1.0 if math.sin(a) < 0 else 0.92)
            pts.append((cx + rx * math.cos(a), cy + h / 2 + ry * math.sin(a)))
        if fill:
            self._fill([pts], fill)
        for _ in range(2):
            self._stroke([(px + self._j(1.5), py + self._j(1.5)) for px, py in pts],
                         2.6, color)

        # face sits high on the body
        ey = top + h * 0.30
        dx = bw * 0.19
        for s in (-1, 1):
            self.ellipse(cx + s * dx, ey, h * 0.034, h * 0.040, w=1.6,
                         color=color, fill=color, passes=1)
        my = ey + h * 0.13
        if mood in ('happy', 'wow'):
            self.arc(cx, my - h * 0.03, h * 0.06, 20, 160, w=2.2, color=color, passes=1)
        elif mood == 'confused':
            self.arc(cx, my + h * 0.06, h * 0.055, 200, 340, w=2.2, color=color, passes=1)
        else:                                # think, a small flat mouth
            self.line(cx - h * 0.04, my, cx + h * 0.04, my, 2.2, color, passes=1)

        # limbs
        ly = top + h * 0.62
        if arms == 'up' or mood == 'wow':
            for s in (-1, 1):
                self.line(cx + s * bw * 0.46, ly, cx + s * bw * 1.0, ly - h * 0.34,
                          2.2, color, passes=1)
        elif arms in ('point-right', 'point-left'):
            s = 1 if arms == 'point-right' else -1
            self.line(cx + s * bw * 0.46, ly, cx + s * bw * 1.15, ly - h * 0.06,
                      2.2, color, passes=1)
            self.line(cx - s * bw * 0.46, ly, cx - s * bw * 0.72, ly + h * 0.18,
                      2.2, color, passes=1)
        elif arms == 'think':
            # elbow swings clear of the body, hand comes back to the chin
            self.line(cx + bw * 0.46, ly, cx + bw * 0.92, top + h * 0.52,
                      2.2, color, passes=1)
            self.line(cx + bw * 0.92, top + h * 0.52, cx + bw * 0.40, top + h * 0.44,
                      2.2, color, passes=1)
            self.line(cx - bw * 0.46, ly, cx - bw * 0.78, ly + h * 0.16,
                      2.2, color, passes=1)
        else:
            for s in (-1, 1):
                self.line(cx + s * bw * 0.46, ly, cx + s * bw * 0.80, ly + h * 0.20,
                          2.2, color, passes=1)
        for s in (-1, 1):
            self.line(cx + s * bw * 0.22, bot - h * 0.02, cx + s * bw * 0.30,
                      bot + h * 0.16, 2.2, color, passes=1)
        return self

    def bubble(self, cx, cy, w, h, tail=(0, 0), color=INK, fill=None):
        """A speech bubble with a small tail pointing at ``tail``."""
        self.rect(cx - w / 2, cy - h / 2, w, h, r=min(w, h) * 0.28, color=color, fill=fill)
        if tail != (0, 0):
            self.line(cx + (tail[0] - cx) * 0.18, cy + h / 2 * 0.85, tail[0], tail[1],
                      2.2, color, passes=1)
        return self

    def bulb(self, cx, cy, r=26, color=INK, fill=None):
        """The idea lightbulb, for the moment something clicks."""
        self.ellipse(cx, cy, r, r, w=2.4, color=color, fill=fill)
        self.line(cx - r * 0.45, cy + r * 0.95, cx + r * 0.45, cy + r * 0.95, 2.2, color, 1)
        self.line(cx - r * 0.35, cy + r * 1.35, cx + r * 0.35, cy + r * 1.35, 2.2, color, 1)
        for a in (-90, -40, -140, 10, -190):
            ax, ay = math.radians(a), None
            self.line(cx + r * 1.35 * math.cos(ax), cy + r * 1.35 * math.sin(ax),
                      cx + r * 1.85 * math.cos(ax), cy + r * 1.85 * math.sin(ax),
                      1.8, color, 1)
        return self

    # ── text, as outlines
    def text(self, x, y, s, size=28, color=INK, anchor='middle', font=None):
        contours, width = glyph_contours(s, x, y, size, font or HAND_FILE, anchor)
        if contours:
            self._fill(contours, color)
        return width

    def mono(self, x, y, s, size=24, color=INK, anchor='middle'):
        return self.text(x, y, s, size, color, anchor, font=MONO_FILE)

    def width_of(self, s, size=28, font=None) -> float:
        return glyph_contours(s, 0, 0, size, font or HAND_FILE, 'start')[1]

    # ── output
    def to_svg(self, title='') -> str:
        parts = []
        for op in self.ops:
            if op[0] == 'stroke':
                pts, width, color = op[1], op[2], op[3]
                d = 'M' + ' L'.join(f'{px:.1f} {py:.1f}' for px, py in pts)
                parts.append(f'<path d="{d}" fill="none" stroke="{color}" '
                             f'stroke-width="{width}" stroke-linecap="round" '
                             f'stroke-linejoin="round"/>')
            else:
                contours, color = op[1], op[2]
                d = ' '.join('M' + ' L'.join(f'{px:.1f} {py:.1f}' for px, py in c) + ' Z'
                             for c in contours)
                parts.append(f'<path d="{d}" fill="{color}" fill-rule="evenodd"/>')
        body = '\n  '.join(parts)
        t = f'\n  <title>{title}</title>' if title else ''
        return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {self.w} {self.h}" '
                f'width="{self.w}" height="{self.h}" role="img">{t}\n'
                f'  <rect width="{self.w}" height="{self.h}" fill="{PAPER}"/>\n'
                f'  {body}\n</svg>\n')

    def to_image(self, scale=3) -> Image.Image:
        """Rasterise with Pillow, supersampled so the strokes stay smooth."""
        W, H = self.w * scale, self.h * scale
        img = Image.new('RGB', (W, H), _rgb(PAPER))
        draw = ImageDraw.Draw(img)
        for op in self.ops:
            if op[0] == 'stroke':
                pts = [(px * scale, py * scale) for px, py in op[1]]
                draw.line(pts, fill=_rgb(op[3]), width=max(1, round(op[2] * scale)),
                          joint='curve')
            else:
                # even-odd fill: XOR each contour into a mask, then paint through it
                mask = Image.new('1', (W, H), 0)
                for contour in op[1]:
                    layer = Image.new('1', (W, H), 0)
                    ImageDraw.Draw(layer).polygon(
                        [(px * scale, py * scale) for px, py in contour], fill=1)
                    mask = ImageChops.logical_xor(mask, layer)
                img.paste(Image.new('RGB', (W, H), _rgb(op[2])), (0, 0), mask)
        return img.resize((self.w, self.h), Image.Resampling.LANCZOS)

    def save(self, path_no_ext: str, title='', scale=3):
        os.makedirs(os.path.dirname(os.path.abspath(path_no_ext)), exist_ok=True)
        open(path_no_ext + '.svg', 'w', encoding='utf-8').write(self.to_svg(title))
        self.to_image(scale).save(path_no_ext + '.png')
        return path_no_ext + '.png'
