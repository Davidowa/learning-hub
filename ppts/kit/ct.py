"""CT-01 to CT-10 redrawn in the deck palette.

The originals are photographs of a sketchbook, warm and textured, and they belong
to the computational thinking course. These are the same ten ideas drawn with
kit.doodle: navy line work on #F7F8FA, washes only in Python blue and Python
yellow, the same blob character, and labels that are always spelled correctly
because they come from a font rather than a model.

    python -m kit.ct --list
    python -m kit.ct ct-09 --lang es
    python -m kit.ct --all
"""
from __future__ import annotations

import math

from .doodle import (BLUE, BLUE_WASH, INK, MUTED, WOOD, WOOD_WASH, YELLOW,
                     YELLOW_WASH, Pen)

W, H = 1680, 654          # the shape the originals use

L = {
    'es': dict(
        decompose='un problema grande, muchos pequeños',
        patterns='agrupa lo que se repite',
        abstract='quédate con lo esencial',
        algorithm='ALGORITMO',
        steps=['reúne', 'mezcla', 'hornea', 'sirve', 'disfruta'],
        start='Inicio', process='Proceso', io='E/S', decision='Decisión',
        flow='cuatro figuras y ya puedes diagramar',
        pseudo='SI hambre ENTONCES comer', code='if hambre:\n    comer()',
        pseudo_note='del idioma de la persona al del intérprete',
        cpu='CPU', ram='RAM', gpu='GPU',
        cpu_d='dirige', ram_d='recuerda', gpu_d='dibuja muchas cosas a la vez',
        human='el pato', compiler='COMPILADOR', machine='máquina',
        greet='hola()', bits='01001', stepwise='paso a paso, sin ambigüedad',
        high='Python / JS / C#', low='Ensamblador / Código máquina',
        easier='más fácil de leer', closer='más cerca del hardware',
        prog='PROGRAMACIÓN',
        paradigms=['imperativo', 'estructurado', 'declarativo',
                   'POO', 'eventos', 'visual'],
    ),
    'en': dict(
        decompose='one big problem, many small ones',
        patterns='group what repeats',
        abstract='keep only what matters',
        algorithm='ALGORITHM',
        steps=['gather', 'mix', 'bake', 'serve', 'enjoy'],
        start='Start', process='Process', io='I/O', decision='Decision',
        flow='four shapes and you can draw any flow',
        pseudo='IF hungry THEN eat', code='if hungry:\n    eat()',
        pseudo_note='from a human language to the interpreter’s',
        cpu='CPU', ram='RAM', gpu='GPU',
        cpu_d='conducts', ram_d='remembers', gpu_d='draws many things at once',
        human='the duck', compiler='COMPILER', machine='machine',
        greet='hi()', bits='01001', stepwise='step by step, no ambiguity',
        high='Python / JS / C#', low='Assembly / Machine Code',
        easier='easier to read', closer='closer to hardware',
        prog='PROGRAMMING',
        paradigms=['imperative', 'structured', 'declarative',
                   'OOP', 'event-driven', 'visual'],
    ),
}


def ct01(t, lang):
    """Decomposition: a tangle pulled apart into tidy coils."""
    p = Pen(W, H, seed=101)
    p.scribble(370, 330, 195, loops=30)
    p.duck(150, 130, h=175, mood='confused', wing='down', fill=YELLOW_WASH)
    # exits ordered top to bottom like the coils, so no two threads cross
    coils = sorted(((1080, 150), (1340, 240), (1080, 330), (1340, 420), (1080, 510)),
                   key=lambda c: c[1])
    for i, (cx, cy) in enumerate(coils):
        p.coil(cx, cy, 62, fill=YELLOW_WASH if i % 2 else BLUE_WASH)
        p.wave(548, 205 + i * 62, cx - 70, cy, amp=8)
    p.text(W / 2, 620, t['decompose'], 30, MUTED)
    return p


def ct02(t, lang):
    """Pattern recognition: a heap of mixed shapes sorted into groups."""
    p = Pen(W, H, seed=102)
    heap = [(150, 180, 'tri'), (250, 250, 'sq'), (170, 330, 'ci'), (280, 130, 'ci'),
            (330, 350, 'tri'), (110, 260, 'sq'), (250, 400, 'ci'), (350, 220, 'sq')]
    for x, y, kind in heap:
        if kind == 'tri':
            p.triangle(x, y, 46)
        elif kind == 'sq':
            p.rect(x - 42, y - 42, 84, 84, r=8)
        else:
            p.ellipse(x, y, 44, 44)
    p.duck(690, 200, h=200, mood='happy', wing='point', fill=YELLOW_WASH)
    for row, (kind, fill) in enumerate((('tri', BLUE_WASH), ('sq', YELLOW_WASH),
                                        ('ci', BLUE_WASH))):
        y = 150 + row * 165
        p.wave(880, 300, 1080, y, amp=8)
        for i in range(3):
            x = 1180 + i * 130
            if kind == 'tri':
                p.triangle(x, y, 46, fill=fill)
            elif kind == 'sq':
                p.rect(x - 42, y - 42, 84, 84, r=8, fill=fill)
            else:
                p.ellipse(x, y, 44, 44, fill=fill)
    p.text(W / 2, 624, t['patterns'], 30, MUTED)
    return p


def _mug(p, cx, cy, s, detail, fill=None):
    p.rect(cx - s * 0.55, cy - s * 0.5, s * 1.0, s * 1.0, r=s * 0.16, fill=fill)
    p.arc(cx + s * 0.52, cy, s * 0.30, -80, 80)
    if detail >= 1:
        for i in range(3):
            p.wave(cx - s * 0.3 + i * s * 0.3, cy - s * 0.62,
                   cx - s * 0.3 + i * s * 0.3, cy - s * 0.95, amp=6, w=1.8)
    if detail >= 2:
        # a scene painted on the side, plus a rim and a base band
        p.triangle(cx - s * 0.20, cy + s * 0.06, s * 0.18, w=1.8)
        p.triangle(cx + s * 0.14, cy + s * 0.02, s * 0.13, w=1.8)
        p.ellipse(cx + s * 0.24, cy - s * 0.20, s * 0.07, s * 0.07, w=1.8)
        p.line(cx - s * 0.40, cy + s * 0.26, cx + s * 0.40, cy + s * 0.26, 1.8, INK, 1)
        p.line(cx - s * 0.48, cy - s * 0.36, cx + s * 0.48, cy - s * 0.36, 1.8, INK, 1)
        for i in range(6):
            p.line(cx - s * 0.40 + i * s * 0.16, cy + s * 0.30,
                   cx - s * 0.40 + i * s * 0.16, cy + s * 0.42, 1.6, INK, 1)


def ct03(t, lang):
    """Abstraction: the same mug, stripped to what matters."""
    p = Pen(W, H, seed=103)
    _mug(p, 300, 300, 210, detail=2, fill=BLUE_WASH)
    p.arrow(520, 300, 660, 300)
    _mug(p, 840, 300, 190, detail=1)
    p.arrow(1030, 300, 1170, 300)
    _mug(p, 1350, 300, 165, detail=0)
    p.bulb(660, 150, 24, fill=YELLOW_WASH)
    p.text(W / 2, 620, t['abstract'], 30, MUTED)
    return p


def ct04(t, lang):
    """Algorithm: a numbered recipe."""
    p = Pen(W, H, seed=104)
    p.rect(70, 90, W - 140, 430, r=22)
    p.text(150, 175, t['algorithm'], 52, anchor='start')
    p.line(150, 196, 150 + p.width_of(t['algorithm'], 52), 196, w=2.6)
    for i, label in enumerate(t['steps']):
        x = 220 + i * 300
        p.ellipse(x, 330, 62, 58, fill=YELLOW_WASH if i % 2 else BLUE_WASH)
        p.text(x, 344, str(i + 1), 44)
        p.text(x, 452, label, 30)
        if i < 4:
            p.arrow(x + 82, 330, x + 218, 330)
    p.text(W / 2, 600, t['stepwise'], 30, MUTED)
    return p


def ct05(t, lang):
    """The four flowchart shapes."""
    p = Pen(W, H, seed=105)
    xs = [260, 660, 1050, 1440]
    p.ellipse(xs[0], 260, 130, 62, fill=YELLOW_WASH)
    p.text(xs[0], 274, t['start'], 34)
    p.rect(xs[1] - 130, 200, 260, 120, r=10, fill=BLUE_WASH)
    p.text(xs[1], 274, t['process'], 34)
    p.rhomboid(xs[2], 260, 260, 120, fill=BLUE_WASH)
    p.text(xs[2], 274, t['io'], 34)
    p.diamond(xs[3], 260, 150, 100, fill=YELLOW_WASH)
    p.text(xs[3], 274, t['decision'], 30)
    for a, b in zip(xs, xs[1:]):
        p.arrow(a + 150, 260, b - 155, 260)
    p.text(W / 2, 560, t['flow'], 30, MUTED)
    return p


def ct06(t, lang):
    """Pseudocode on paper becomes code on a screen."""
    p = Pen(W, H, seed=106)
    p.rect(120, 140, 520, 300, r=16, fill=YELLOW_WASH)
    for i in range(6):
        p.line(160, 190 + i * 42, 600, 190 + i * 42, w=1.4, color=MUTED, passes=1)
    p.text(380, 300, t['pseudo'], 34)
    p.arrow(700, 290, 900, 290)
    p.bulb(800, 170, 26, fill=YELLOW_WASH)
    p.monitor(960, 140, 560, 300, fill=BLUE_WASH)
    for i, line in enumerate(t['code'].split('\n')):
        p.mono(1010, 250 + i * 52, line, 36, anchor='start')
    p.text(W / 2, 620, t['pseudo_note'], 30, MUTED)
    return p


def ct07(t, lang):
    """The three pieces of hardware, as characters."""
    p = Pen(W, H, seed=107)
    for i, (name, desc, fill) in enumerate(
            ((t['cpu'], t['cpu_d'], BLUE_WASH), (t['ram'], t['ram_d'], YELLOW_WASH),
             (t['gpu'], t['gpu_d'], BLUE_WASH))):
        cx = 320 + i * 520
        p.chip(cx, 260, 190, fill=fill)
        p.text(cx, 236, name, 44)
        for sgn in (-1, 1):
            p.ellipse(cx + sgn * 30, 282, 7, 8, 1.6, INK, fill=INK, passes=1)
        p.arc(cx, 292, 22, 20, 160, w=2.0, passes=1)
        for s in (-1, 1):
            p.line(cx + s * 100, 300, cx + s * 150, 360, 2.2, INK, 1)
            p.line(cx + s * 40, 360, cx + s * 55, 430, 2.2, INK, 1)
        if i == 2:
            for a in (-150, -120, -60, -30):
                ar = math.radians(a)
                p.line(cx + 95 * math.cos(ar), 260 + 95 * math.sin(ar),
                       cx + 165 * math.cos(ar), 260 + 165 * math.sin(ar), 2.2, INK, 1)
        p.text(cx, 520, desc, 30, MUTED)
    return p


def ct08(t, lang):
    """A human sentence, a compiler, and a machine that only reads bits."""
    p = Pen(W, H, seed=108)
    p.duck(200, 170, h=205, mood='happy', wing='point', fill=YELLOW_WASH)
    p.text(230, 520, t['human'], 32)
    p.bubble(470, 200, 250, 110, tail=(360, 265), fill=YELLOW_WASH)
    p.mono(470, 212, t['greet'], 34)

    p.rect(700, 190, 300, 180, r=18, fill=BLUE_WASH)
    p.text(850, 290, t['compiler'], 30)
    p.arrow(640, 280, 690, 280)
    p.arrow(1010, 280, 1080, 280)

    p.robot(1330, 130, 300, fill=YELLOW_WASH)
    p.text(1330, 500, t['machine'], 32)
    p.bubble(1130, 190, 180, 90, tail=(1230, 250))
    p.mono(1130, 200, t['bits'], 26)
    return p


def ct09(t, lang):
    """The one you liked: high level up the ladder, machine code at the foot."""
    p = Pen(W, H, seed=109)
    p.ladder(840, 190, 380, w_=150, rungs=7, color=WOOD, fill=WOOD_WASH)
    p.duck(770, 105, h=160, mood='happy', wing='down', fill=YELLOW_WASH)
    p.text(880, 62, t['high'], 36)

    # the same bird at the foot of the ladder, in a hard hat
    p.duck(1040, 385, h=155, mood='happy', wing='down', fill=BLUE_WASH, hat=True)
    p.text(1060, 590, t['low'], 32)

    p.arrow(400, 490, 400, 210)
    p.text(370, 340, t['easier'], 32, anchor='end')
    p.arrow(1290, 210, 1290, 490)
    p.text(1320, 340, t['closer'], 32, anchor='start')
    return p


def ct10(t, lang):
    """The paradigm map."""
    p = Pen(W, H, seed=110)
    cx, cy = W / 2, H / 2 - 15
    p.sun(cx, cy, 150, spikes=16, fill=YELLOW_WASH)
    p.text(cx, cy + 10, t['prog'], 34)
    ring = [(-158, 'gears'), (-118, 'blocks'), (-40, 'bubble'),
            (40, 'card'), (118, 'bolt'), (158, 'bricks')]
    for (deg, kind), label in zip(ring, t['paradigms']):
        a = math.radians(deg)
        ex, ey = cx + 560 * math.cos(a), cy + 235 * math.sin(a)
        p.wave(cx + 195 * math.cos(a), cy + 175 * math.sin(a),
               ex - 66 * math.cos(a), ey - 34 * math.sin(a), amp=8)
        fill = BLUE_WASH if kind in ('gears', 'bubble', 'bolt') else YELLOW_WASH
        if kind == 'gears':
            p.ellipse(ex, ey, 34, 34, fill=fill)
            for i in range(8):
                b = 2 * math.pi * i / 8
                p.line(ex + 34 * math.cos(b), ey + 34 * math.sin(b),
                       ex + 46 * math.cos(b), ey + 46 * math.sin(b), 2.0, INK, 1)
        elif kind == 'blocks':
            p.rect(ex - 46, ey - 34, 92, 30, r=6, fill=fill)
            p.rect(ex - 46, ey + 4, 92, 30, r=6, fill=fill)
        elif kind == 'bubble':
            p.bubble(ex, ey, 96, 62, tail=(ex - 26, ey + 52), fill=fill)
            p.text(ex, ey + 8, '?', 32)
        elif kind == 'card':
            p.rect(ex - 42, ey - 44, 84, 88, r=8, fill=fill)
            p.ellipse(ex, ey - 16, 15, 15, 1.8)
            p.line(ex - 26, ey + 14, ex + 26, ey + 14, 1.8, INK, 1)
            p.line(ex - 26, ey + 32, ex + 26, ey + 32, 1.8, INK, 1)
        elif kind == 'bolt':
            p.poly([(ex + 6, ey - 46), (ex - 22, ey + 4), (ex - 2, ey + 4),
                    (ex - 10, ey + 48), (ex + 24, ey - 8), (ex + 3, ey - 8)],
                   2.2, INK, fill)
        else:
            for r_ in range(2):
                for c in range(2):
                    p.rect(ex - 44 + c * 46, ey - 32 + r_ * 34, 40, 30, r=5, fill=fill)
        p.text(ex, ey + 96, label, 30, BLUE)
    return p


SCENES = {
    'ct-01': (ct01, 'Decomposition, a tangle pulled apart into tidy coils',
              'Opens any session about breaking a problem down. w02 divider.'),
    'ct-02': (ct02, 'Pattern recognition, a heap of shapes sorted into groups',
              'Also serves "what a class is": grouping before syntax. w03.'),
    'ct-03': (ct03, 'Abstraction, the same mug stripped to what matters',
              'The abstraction principle in w02, and modelling in w03.'),
    'ct-04': (ct04, 'Algorithm, a numbered recipe with no ambiguity',
              'The method slide of w01.1, or any step-by-step.'),
    'ct-05': (ct05, 'The four flowchart shapes',
              'Not used by COM102, kept so the set is complete.'),
    'ct-06': (ct06, 'Pseudocode on paper becoming code on a screen',
              'w01.1, the bridge from a plan to a program.'),
    'ct-07': (ct07, 'CPU, RAM and GPU as characters',
              'Not used by COM102, kept for the hardware session of other courses.'),
    'ct-08': (ct08, 'A human sentence, a compiler, and a machine that reads bits',
              'w02, when the question of what runs where comes up.'),
    'ct-09': (ct09, 'High level up the ladder, machine code at the foot',
              'w02, why Python. The original of this one is the favourite.'),
    'ct-10': (ct10, 'The paradigm map, six ways round one sun',
              'w02, the opening slide of the paradigm block.'),
}
