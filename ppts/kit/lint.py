"""Check a built deck for text that spills past the safe area.

Measures every run with the real font metrics, wraps it inside its own box, and
reports anything whose rendered bottom crosses the footer rule or whose right
edge crosses the margin, lands on another text, is struck through by a rule, or
runs out of the card or band it starts in.

    python -m kit.lint out/w03.es.pptx
    python -m kit.lint out
"""
from __future__ import annotations

import argparse
import glob
import os

from pptx import Presentation
from pptx.enum.dml import MSO_FILL
from pptx.enum.shapes import MSO_SHAPE_TYPE
from pptx.enum.text import MSO_ANCHOR, PP_ALIGN

from . import tokens as K
from .deck import line_h, measure, wrap_lines

SAFE_RIGHT = K.M + K.CONTENT_W + 0.10      # 19.06 in
FOOTER_TOP = K.FOOTER_RULE_Y - 0.06        # content must end above the rule
CHROME_TOP = K.SLIDE_H - 0.12              # the footer band itself

# A line box runs a little below the ink of its descenders, so two boxes that
# overlap by less than this are touching on paper, not printing over each other.
GAP = 0.06


def _extent(sh):
    """Where the text of a shape lands: (left, top, right, bottom), in inches.

    The box is not the answer. A one-line label in a wide box only covers its own
    width, and a paragraph only covers the lines it wraps to, whatever height the
    box was given. Code and console lines are skipped: they are stacked at a
    tighter step than their line box on purpose, and are measured on their own below.
    """
    para = sh.text_frame.paragraphs[0]
    runs = para.runs
    if not runs:
        return None
    size = max((r.font.size.pt for r in runs if r.font.size), default=18)
    name = runs[0].font.name or K.SANS
    mult = para.line_spacing if isinstance(para.line_spacing, float) else 1.0
    if name == K.MONO and abs(mult - K.LS.code) < 1e-6:
        return None
    bold = bool(runs[0].font.bold)
    text = ''.join(r.text for r in runs)
    x, y = sh.left / 914400, sh.top / 914400
    w, h = sh.width / 914400, sh.height / 914400
    lines = wrap_lines(text, name, size, w, bold)
    th = 0.028 + lines * line_h(size, mult)
    top = y + (h - th) / 2 if sh.text_frame.vertical_anchor == MSO_ANCHOR.MIDDLE else y
    left, right = x, x + w
    if lines == 1:
        tw = measure(text, name, size, bold) + 0.056
        if para.alignment == PP_ALIGN.RIGHT:
            left = x + w - tw
        elif para.alignment == PP_ALIGN.CENTER:
            left = x + (w - tw) / 2
        right = left + tw
    return left, top, right, top + th, text.strip()[:40]


def _collisions(n, slide) -> list[str]:
    """Text on text, a rule through text, and text leaving the card it sits in.

    None of these cross the safe area, so the checks in ``check`` never see them:
    every box stays inside the slide and they only land on each other. That is
    how a concept lead struck through by its own rule, or a takeaway whose second
    line runs under the separator, passed lint on every deck that had them.
    """
    texts, rules, panels = [], [], []
    for sh in slide.shapes:
        if sh.has_text_frame and sh.text_frame.text.strip():
            e = _extent(sh)
            if e:
                texts.append(e)
            continue
        if sh.shape_type != MSO_SHAPE_TYPE.AUTO_SHAPE or sh.fill.type != MSO_FILL.SOLID:
            continue
        x, y = sh.left / 914400, sh.top / 914400
        w, h = sh.width / 914400, sh.height / 914400
        if h <= 0.02 and w >= 1.0 and y < K.FOOTER_RULE_Y - 0.02:
            rules.append((x, y + h / 2, x + w))
        elif h >= 0.3 and w >= 1.0:
            panels.append((x, y, x + w, y + h))

    problems = []
    for i, a in enumerate(texts):
        for b in texts[i + 1:]:
            down = min(a[3], b[3]) - max(a[1], b[1])
            across = min(a[2], b[2]) - max(a[0], b[0])
            if down > GAP and across > 0.05:
                problems.append(f'{n:02d}  text lands on text: "{a[4]}" / "{b[4]}"')
        for x0, ry, x1 in rules:
            if a[0] < x1 and a[2] > x0 + 0.1 and a[1] + GAP < ry < a[3] - GAP:
                problems.append(f'{n:02d}  rule at {ry:.2f}" runs through "{a[4]}"')
        for px0, py0, px1, py1 in panels:
            inside = px0 - 0.01 <= a[0] < px1 - 0.1 and py0 - 0.01 <= a[1] < py1 - 0.05
            if inside and (a[3] > py1 + GAP or a[2] > px1 + 0.02):
                problems.append(f'{n:02d}  text runs out of its card at {a[3]:.2f}" '
                                f'(card ends {py1:.2f}"): "{a[4]}"')
    return problems


def check(path: str) -> list[str]:
    prs = Presentation(path)
    problems = []
    for n, slide in enumerate(prs.slides, 1):
        problems += _collisions(n, slide)
        # A slide with a footer rule has a footer row, and only that row is chrome.
        # Anything else that starts under the rule is content that fell into it,
        # like a fourth code annotation. Dark slides have no rule, and their meta
        # row sits down there on purpose.
        ruled = any(sh.shape_type == MSO_SHAPE_TYPE.AUTO_SHAPE and not sh.text_frame.text.strip()
                    and abs(sh.top / 914400 - K.FOOTER_RULE_Y) < 0.01 for sh in slide.shapes)
        for sh in slide.shapes:
            x = sh.left / 914400
            y = sh.top / 914400
            w = sh.width / 914400
            right = x + w

            if not sh.has_text_frame or not sh.text_frame.text.strip():
                # Zebra bands and rules bleed past the margin on purpose, so an
                # empty shape is not measured sideways. It still has to respect
                # the footer rule downwards: a code card whose type has bottomed
                # out at the 18 pt floor keeps growing, and the card runs under
                # the rule while its last line of type stops just above it. Every
                # text check therefore passes and the deck reads clean, which is
                # how twenty-seven overflowing cards once shipped.
                #
                # Only a panel is checked. A rule is 0.01 in tall, the progress
                # dashes are 0.05, and a full-bleed background starts at the top
                # edge, so none of them can trip this.
                bottom = y + sh.height / 914400
                if sh.height / 914400 > 0.5 and y > 0.10 and bottom > K.FOOTER_RULE_Y + 0.02:
                    problems.append(f'{n:02d}  panel runs to {bottom:.2f}" and crosses '
                                    f'the footer rule at {K.FOOTER_RULE_Y}"')
                continue

            if right > SAFE_RIGHT + 0.01:
                problems.append(f'{n:02d}  text box runs to {right:.2f}" '
                                f'(margin ends at {SAFE_RIGHT:.2f}")')
            para = sh.text_frame.paragraphs[0]
            runs = para.runs
            if not runs:
                continue
            size = max((r.font.size.pt for r in runs if r.font.size), default=18)
            name = runs[0].font.name or K.SANS
            bold = bool(runs[0].font.bold)
            text = ''.join(r.text for r in runs)
            mult = para.line_spacing if isinstance(para.line_spacing, float) else 1.0
            lines = wrap_lines(text, name, size, w, bold)
            bottom = y + lines * line_h(size, mult)

            chrome = y >= K.FOOTER_Y - 0.05 if ruled else y >= FOOTER_TOP
            limit = CHROME_TOP if chrome else FOOTER_TOP
            if bottom > limit + 0.05:
                snippet = text[:52].replace('\n', ' ')
                problems.append(f'{n:02d}  text ends at {bottom:.2f}" '
                                f'(limit {limit:.2f}"): "{snippet}"')

            # A code line and an output line each get their own box, at the code
            # line spacing. Either one wrapping means the tail is sitting on the
            # slide background, which the checks above never see because the box
            # itself stays inside the safe area.
            #
            # Measure the whole string rather than asking wrap_lines: that helper
            # splits on words, which collapses runs of spaces, so an aligned
            # trailing comment measures short and a line that really overflows
            # comes back as fitting. PowerPoint keeps every space.
            if name == K.MONO and abs(mult - K.LS.code) < 1e-6:
                used = measure(text, name, size)
                if used > w - 0.07:
                    snippet = text.strip()[:48]
                    problems.append(f'{n:02d}  code line overflows its card '
                                    f'({used:.2f}" in {w - 0.07:.2f}", '
                                    f'{len(text)} chars): "{snippet}"')

    return problems


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split('\n')[0])
    ap.add_argument('target', help='a .pptx, or a folder of them')
    a = ap.parse_args(argv)
    files = (sorted(glob.glob(os.path.join(a.target, '**', '*.pptx'), recursive=True))
             if os.path.isdir(a.target) else [a.target])
    total = 0
    for f in files:
        found = check(f)
        total += len(found)
        mark = 'clean' if not found else f'{len(found)} issue(s)'
        print(f'{os.path.basename(f):<20} {mark}')
        for p in found:
            print(f'    {p}')
    print(f'\n{total} issue(s) across {len(files)} deck(s)')
    return 1 if total else 0


if __name__ == '__main__':
    raise SystemExit(main())
