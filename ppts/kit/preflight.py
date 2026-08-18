"""Check a lesson .yaml before building it.

    python -m kit.preflight python
    python -m kit.preflight python/programacion-orientada-a-objetos/es/w04.es.yaml

`build` reports a code card that does not fit only after it has written the file,
and `lint` reports it only as a box that ends too low. Both are late. The caps
below are the same arithmetic `deck._code_card` does, run against the source, so
a lesson gets rejected before it becomes a deck.

The type in a code card shrinks to fit and stops at the 18 pt projection floor,
which turns the card into two hard caps: the longest line and the number of rows.
A blank line counts as half a row because it carries no code. Solving for 18 pt:

    widest <= (card_w - 0.95) * 72 / (0.6 * 18)
    rows   <= room / (CODE_LINE_STEP / T.code) / 18

The three card widths in the kit are 10.40 in for `code` and `code_output`,
9.60 in for `quiz`, and 8.60 in for each side of `compare`.
"""
from __future__ import annotations

import argparse
import glob
import os
import re
import sys

import yaml

from . import tokens as K
from .deck import fit_size, line_h, wrap_lines

# (widest line in characters, rows) per layout, at the 18 pt floor
CAPS = {'code': (63, 13.9), 'quiz': (57, 12.4), 'compare': (51, 8.0)}
OUTPUT_LINES, OUTPUT_CHARS = 10, 36

# Row titles that get a fixed-height box, so a second line lands on the text
# below it instead of pushing it down. lint cannot see this: the slide stays
# inside the safe area, the two runs just overlap. (layout, list key, box width)
ONE_LINE_TITLES = [('takeaways', 'items', 8.0), ('pitfalls', 'items', 8.3)]

# concept.panel puts its title at y + 0.79 and its note at y + 1.40, so the
# title owns 0.61 in and a second line lands on the note. Same failure as above,
# one level deeper in the mapping. (layout, key chain, box width, type size)
ONE_LINE_NESTED = [('concept', ('panel', 'title'), 9.44, K.T.value)]

# deck.diagram, measured off the method. The card is a fixed height, so unlike a
# card that grows, both of its text rows have a hard ceiling and neither one
# pushes the other down. It cannot join ONE_LINE_TITLES because the box width
# depends on how many blocks the slide has.
DIAGRAM_GAP = 1.25
DIAGRAM_CARD_Y, DIAGRAM_CARD_H = 2.65, 2.48
DIAGRAM_TITLE_Y, DIAGRAM_DESC_Y = 3.49, 4.02

# The description row has 1.11 in of card under it and a line is 0.38 in, so it
# holds 2.94 lines. Truncating that to two rejects a third line whose last
# descender lands 0.02 in below the card edge, which is not something anyone can
# see: the sixteen COM102 diagrams this check first flagged all render correctly.
# The tolerance buys back that rounding and nothing more. A fourth line clears the
# card by 0.40 in and is still caught.
DIAGRAM_SLACK = 0.05

# a plain scalar carrying ": " ends the key early and YAML stops with
# "mapping values are not allowed here", pointing at a column, not a cause
PLAIN_SCALAR = re.compile(r'^(\s*)(?:- )?([a-z_]+):\s(?!["\'|>])(.+)$')

# The mirror of the one above: a value that opens with a quote. YAML reads it as
# a quoted scalar and then trips over whatever follows the closing quote, and it
# blames the enclosing mapping rather than this line. Written as prose it looks
# innocent: 'A' is a char and "A" is a string.
QUOTED_SCALAR = re.compile(r'^\s*(?:- )?[a-z_]+:\s(["\']).*$')


def _code(problems, n, layout, key, source, caps):
    lines = source.rstrip('\n').split('\n')
    widest = max((len(ln) for ln in lines), default=0)
    rows = sum(0.5 if not ln.strip() else 1.0 for ln in lines)
    if widest > caps[0]:
        longest = max(lines, key=len).strip()
        problems.append(f'slide {n:02d} {layout}.{key}: {widest} chars, cap {caps[0]} '
                        f'-> {longest[:56]}')
    if rows > caps[1]:
        problems.append(f'slide {n:02d} {layout}.{key}: {rows:g} rows, cap {caps[1]:g}')


def _diagram(problems, n, kw):
    """Check a diagram's two fixed-height text rows.

    The title sits at 3.49 and the description at 4.02, so the title owns 0.53 in
    and a second line lands on the description. The description in turn runs to
    the bottom of a card that does not grow, so the line that does not fit breaks
    out of it. On a ``dark: true`` block that stray line comes out in
    ``ON_NAVY_SOFT`` over the paper, where it is close to invisible.

    `lint` sees none of this. Every box stays inside the safe area; they only
    overlap each other.
    """
    blocks = kw.get('blocks') or []
    if not blocks:
        return
    w = (K.CONTENT_W - DIAGRAM_GAP * (len(blocks) - 1)) / len(blocks)
    title_rows = int((DIAGRAM_DESC_Y - DIAGRAM_TITLE_Y) /
                     line_h(K.T.block_title, K.LS.card_title))
    desc_rows = int((DIAGRAM_CARD_Y + DIAGRAM_CARD_H - DIAGRAM_DESC_Y + DIAGRAM_SLACK) /
                    line_h(K.T.label, K.LS.desc))
    for i, b in enumerate(blocks, 1):
        title = b.get('title', '')
        lines = wrap_lines(title, K.SANS, K.T.block_title, w - 0.5, True)
        if lines > title_rows:
            problems.append(f'slide {n:02d} diagram: block {i} title wraps to {lines} '
                            f'lines, cap {title_rows}, and overlaps the text under it '
                            f'-> {title[:48]}')
        desc = b.get('desc', '')
        lines = wrap_lines(desc, K.SANS, K.T.label, w - 0.7)
        if lines > desc_rows:
            problems.append(f'slide {n:02d} diagram: block {i} desc wraps to {lines} '
                            f'lines, cap {desc_rows} with {len(blocks)} blocks, and '
                            f'spills out of the card -> {desc[:48]}')


def _table_height(problems, n, kw):
    headers, rows = kw['headers'], kw['rows'][:7]
    cols = len(headers)
    widths = [K.CONTENT_W * (0.19 if i == 0 else 0.81 / (cols - 1)) for i in range(cols)]
    size = fit_size(kw.get('title', ''), K.SANS, K.T.title, K.TITLE_W, 2, bold=True, floor=30)
    lines = wrap_lines(kw.get('title', ''), K.SANS, size, K.TITLE_W, True)
    dy = max(0.0, (lines - 1) * size * 1.2 * K.LS.title / 72.0)
    y = 2.65 + dy + 0.52 + 0.22
    tall = []
    for r, row in enumerate(rows, 1):
        hs = max(wrap_lines(str(c), K.MONO if i else K.SANS, K.T.body,
                            widths[i] - 0.35) for i, c in enumerate(row))
        y += 0.38 + 0.40 * hs + 0.14
        if hs > 1:
            tall.append(r)
    y -= 0.14                      # the last row has no gap after it
    if y > K.FOOTER_RULE_Y:
        extra = f', rows {tall} wrap' if tall else ''
        problems.append(f'slide {n:02d} table: {len(rows)} rows end at {y:.2f}", '
                        f'footer rule at {K.FOOTER_RULE_Y}"{extra}')


def _trace_height(problems, n, kw):
    """Check that a trace's rows, and the verdict under them, clear the rule.

    deck.trace stacks rows and then drops the verdict below the last one without
    ever asking whether the stack still fits. Nothing downstream catches it: the
    cells are their own small boxes and stay inside the safe area, and `lint`
    reads anything starting below the rule as footer chrome, so a verdict sitting
    on the footer measures as if it were the footer. The arithmetic below is the
    same walk deck.trace does, run against the source.

    A cell that wraps costs 0.40 in, which is what usually pushes a six-row trace
    over: the trace in COM102 w01.2 fit on every count except that step 5 read
    "while 3 < 3 es falso" and took two lines.
    """
    headers, rows = kw['headers'], kw['rows'][:8]
    w = K.CONTENT_W / len(headers)
    size = fit_size(kw.get('title', ''), K.SANS, K.T.title, K.TITLE_W, 2, bold=True, floor=30)
    lines = wrap_lines(kw.get('title', ''), K.SANS, size, K.TITLE_W, True)
    dy = max(0.0, (lines - 1) * size * 1.2 * K.LS.title / 72.0)
    y = 2.70 + dy + 0.52 + 0.20
    tall = []
    for r, row in enumerate(rows, 1):
        hs = max(wrap_lines(str(c), K.MONO, K.T.sub, w - 0.3) for c in row)
        y += 0.30 + 0.40 * hs + 0.14
        if hs > 1:
            tall.append(r)
    bottom = y + 1.00 if kw.get('verdict') else y - 0.14
    # Same rounding buy-back as DIAGRAM_SLACK, and for the same reason. The
    # verdict's accent bar is the last 0.75 in of the block and the text sits
    # 0.03 in inside it, so a block ending 0.02 in under the rule puts the bar on
    # the rule and nothing else: the four traces this first flagged all render
    # correctly. A block 0.10 in over does show, which is the COM102 w01.2 case,
    # and it is still caught.
    if bottom > K.FOOTER_RULE_Y + 0.05:
        what = 'the verdict ends' if kw.get('verdict') else 'the rows end'
        extra = f', rows {tall} wrap' if tall else ''
        problems.append(f'slide {n:02d} trace: {len(rows)} rows, {what} at {bottom:.2f}", '
                        f'footer rule at {K.FOOTER_RULE_Y}"{extra}')


# YAML 1.1 resolves a bare NULL, yes, no, on, off, true, false or a bare number to a
# non-string. Every one of these is a value the deck renders as text, so the coercion is
# invisible in the source and wrong on the slide -- or fatal: deck._card calls .upper() on
# a label, and a bare `label: NULL` becomes None and crashes the build. preflight used to
# certify such a file clean, because the damage happens inside the parser.
#
# Fields that are legitimately not text, and are therefore exempt.
NON_TEXT = {'week', 'blocks', 'block', 'dark', 'accent', 'cols', 'rows_'}


def _coerced(problems, n, layout, node, trail=''):
    """Report any value YAML turned from text into something else."""
    if isinstance(node, dict):
        for k, v in node.items():
            if k in NON_TEXT:
                continue
            _coerced(problems, n, layout, v, f'{trail}.{k}' if trail else str(k))
    elif isinstance(node, list):
        for i, v in enumerate(node):
            _coerced(problems, n, layout, v, f'{trail}[{i}]')
    elif node is None or isinstance(node, (bool, int, float)):
        got = 'null' if node is None else repr(node)
        problems.append(f'slide {n:02d} {layout}.{trail}: YAML read this as {got}, not text. '
                        f'A bare NULL, yes, no, on, off or number is not a string -- quote it')


def check(path: str) -> tuple[list[str], int]:
    problems: list[str] = []
    for i, raw in enumerate(open(path, encoding='utf-8'), 1):
        line = raw.rstrip('\n').rstrip()
        q = QUOTED_SCALAR.match(line)
        if q and not line.endswith(q.group(1)):
            problems.append(f'line {i}: opens with {q.group(1)} and does not end with it, '
                            f'so YAML stops at the closing quote -> {line.strip()[:64]}')
        m = PLAIN_SCALAR.match(raw.rstrip('\n'))
        if not m:
            continue
        value = m.group(3)
        if ': ' in value:
            problems.append(f'line {i}: unquoted colon -> {value[:64]}')
        if value.lstrip()[:1] in '@*&%`':
            problems.append(f'line {i}: needs quoting -> {value[:64]}')
        # A bare '#' after whitespace opens a YAML comment, so the rest of the
        # value is dropped without a word. Quote the scalar to keep it.
        if re.search(r'(?:^|\s)#', value):
            kept = re.split(r'(?:^|\s)#', value)[0].strip()
            problems.append(f'line {i}: unquoted # starts a comment and YAML drops the rest '
                            f'of the value, keeping only -> {kept[:56]}')

    try:
        doc = yaml.safe_load(open(path, encoding='utf-8'))
    except yaml.YAMLError as exc:
        mark = getattr(exc, 'problem_mark', None)
        where = f' at line {mark.line + 1}, column {mark.column + 1}' if mark else ''
        problem = getattr(exc, 'problem', None) or str(exc).splitlines()[0]
        problems.append(f'yaml{where}: {problem}')
        return problems, 0

    slides = doc.get('slides', [])
    for n, entry in enumerate(slides, 1):
        (layout, kw), = entry.items()
        kw = kw or {}
        _coerced(problems, n, layout, kw)
        if 'source' in kw:
            _code(problems, n, layout, 'source', kw['source'],
                  CAPS['quiz'] if layout == 'quiz' else CAPS['code'])
        for side in ('before', 'after'):
            block = kw.get(side) or {}
            if 'code' in block:
                _code(problems, n, layout, side, block['code'], CAPS['compare'])
        if 'output' in kw:
            out = kw['output'].rstrip('\n').split('\n')
            if len(out) > OUTPUT_LINES:
                problems.append(f'slide {n:02d} {layout}.output: {len(out)} lines, '
                                f'cap {OUTPUT_LINES}')
            wide = max((len(ln) for ln in out), default=0)
            if wide > OUTPUT_CHARS:
                problems.append(f'slide {n:02d} {layout}.output: {wide} chars, '
                                f'cap {OUTPUT_CHARS}')
        # deck.table caps at seven rows, but seven never fit: the rows are laid out
        # at a fixed height and simply keep going past the footer rule, which lint
        # cannot see because each cell is its own small box inside the safe area.
        if layout == 'table' and kw.get('headers') and kw.get('rows'):
            _table_height(problems, n, kw)
        if layout == 'trace' and kw.get('headers') and kw.get('rows'):
            _trace_height(problems, n, kw)
        if layout == 'diagram':
            _diagram(problems, n, kw)

        headers = kw.get('headers')
        for r, row in enumerate(kw.get('rows', []), 1):
            if headers and len(row) != len(headers):
                problems.append(f'slide {n:02d} {layout}: row {r} has {len(row)} cells '
                                f'and there are {len(headers)} headers. A comma inside '
                                f'a YAML flow list splits the cell; quote it.')
        for r, row in enumerate(kw.get('rubric', []), 1):
            if len(row) != 3:
                problems.append(f'slide {n:02d} {layout}: rubric row {r} has {len(row)} '
                                f'cells, needs 3. Quote any cell with a comma.')
        # cover, homework and closing all take meta as [label, value] pairs, and a
        # comma inside an unquoted cell splits it into three
        for r, row in enumerate(kw.get('meta', []), 1):
            if isinstance(row, list) and len(row) != 2:
                problems.append(f'slide {n:02d} {layout}: meta row {r} has {len(row)} '
                                f'cells, needs 2. Quote any cell with a comma.')
        for name, key, width in ONE_LINE_TITLES:
            if layout != name:
                continue
            for it in kw.get(key, []):
                title = it.get('title', '')
                if wrap_lines(title, K.SANS, K.T.head, width, True) > 1:
                    problems.append(f'slide {n:02d} {layout}: title wraps to two lines '
                                    f'and overlaps the text under it -> {title[:56]}')
        for name, keys, width, size in ONE_LINE_NESTED:
            if layout != name:
                continue
            node = kw
            for step in keys:
                node = (node or {}).get(step)
                if node is None:
                    break
            if isinstance(node, str) and wrap_lines(node, K.SANS, size, width) > 1:
                dotted = '.'.join(keys)
                problems.append(f'slide {n:02d} {layout}.{dotted}: wraps to two lines '
                                f'and overlaps the text under it -> {node[:56]}')
    return problems, len(slides)


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split('\n')[0])
    ap.add_argument('target', help='a lesson .yaml, or a folder of them')
    a = ap.parse_args(argv)
    files = (sorted(glob.glob(os.path.join(a.target, '**', '*.yaml'), recursive=True))
             if os.path.isdir(a.target) else [a.target])
    total = 0
    for f in files:
        problems, n = check(f)
        total += len(problems)
        mark = 'clean' if not problems else f'{len(problems)} issue(s)'
        print(f'{os.path.basename(f):<20} {n:>3} slides  {mark}')
        for p in problems:
            print(f'    {p}')
    print(f'\n{total} issue(s) across {len(files)} lesson(s)')
    return 1 if total else 0


if __name__ == '__main__':
    raise SystemExit(main())
