"""Turn a lesson YAML file into a .pptx.

    python -m kit.build courses/com102-oop/w03.es.yaml
    python -m kit.build courses/com102-oop            # every lesson in the folder

A lesson file is a ``meta`` block plus a list of slides. Each slide is a single
key naming a Deck method, and its value is that method's arguments::

    - code:
        eyebrow: Python
        title: Una clase mínima
        filename: libro.py
        lang: python
        source: |
          class Libro:
              ...
        annotations:
          - {label: Línea 2, text: El constructor recibe lo indispensable}

Positional-only shorthand works too: ``- quote: {text: …, author: …}``.
"""
from __future__ import annotations

import argparse
import glob
import os
import sys

import yaml

from .deck import Deck

METHODS = ('cover', 'agenda', 'objectives', 'roadmap', 'divider', 'concept',
           'diagram', 'code', 'code_output', 'table', 'steps', 'stat',
           'pitfalls', 'method', 'lab', 'quiz', 'trace', 'compare', 'tiers',
           'quote', 'takeaways', 'homework', 'closing', 'figure')


def build(path: str, outdir: str | None = None) -> str:
    with open(path, encoding='utf-8') as fh:
        doc = yaml.safe_load(fh)
    meta = doc.get('meta', {})
    deck = Deck(footer=meta.get('footer', ''), lang=meta.get('lang', 'es'),
                course=meta.get('course', ''), blocks=meta.get('blocks', 3),
                language=meta.get('language', 'python'))

    print(f'{os.path.basename(path)}')
    for i, entry in enumerate(doc.get('slides', []), 1):
        if not isinstance(entry, dict) or len(entry) != 1:
            raise ValueError(f'{path}: slide {i} must be a single-key mapping')
        (name, kwargs), = entry.items()
        if name not in METHODS:
            raise ValueError(f'{path}: slide {i} — unknown layout {name!r}. '
                             f'Known: {", ".join(METHODS)}')
        getattr(deck, name)(**(kwargs or {}))

    base = os.path.splitext(os.path.basename(path))[0]
    out = os.path.join(outdir or os.path.dirname(os.path.abspath(path)), f'{base}.pptx')
    deck.save(out)
    print(f'  -> {out}  ({len(deck.prs.slides)} slides)')
    return out


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split('\n')[0])
    ap.add_argument('target', help='a lesson .yaml, or a folder of them')
    ap.add_argument('-o', '--outdir', default=None,
                    help='where the .pptx files go (default: next to the lesson)')
    a = ap.parse_args(argv)

    if os.path.isdir(a.target):
        files = sorted(glob.glob(os.path.join(a.target, '**', '*.yaml'), recursive=True))
        if not files:
            sys.exit(f'no .yaml lessons under {a.target}')
    else:
        files = [a.target]
    for f in files:
        build(f, a.outdir)


if __name__ == '__main__':
    main()
