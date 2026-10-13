"""Check the built lesson set and its exported PDF page counts.

Run with the repository Python 3.14 environment. The original template is not a
lesson and is deliberately excluded. Rendering and editorial review are separate
checks, recorded in the continuation reports.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import sys

import pymupdf
from pptx import Presentation
import yaml

PPTS = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(PPTS))
from kit import highlight, lint, preflight, sizes


def digest(path):
    with path.open('rb') as source:
        return hashlib.file_digest(source, 'sha256').hexdigest()


def code_sources(node, language):
    if isinstance(node, dict):
        language = node.get('lang', language)
        if isinstance(node.get('source'), str):
            yield node['source'], language
        for value in node.values():
            yield from code_sources(value, language)
    elif isinstance(node, list):
        for value in node:
            yield from code_sources(value, language)


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--out', type=Path, required=True)
    ap.add_argument('--previous', type=Path,
                    help='Reuse successful checks only when source, PPTX and PDF hashes all match.')
    args = ap.parse_args()
    args.out = args.out.resolve()
    previous = json.loads(args.previous.read_text()) if args.previous else {}
    failed = {item.get('source') for item in previous.get('issues', [])}
    cached = {row['source']: row for row in previous.get('lessons', [])
              if row['source'] not in failed}
    os.chdir(PPTS)
    report = {'lessons': [], 'issues': [], 'groups': {}, 'code_source_blocks': 0,
              'hash_validated_cached_lessons': 0}
    for source in sorted(Path('.').rglob('*.yaml')):
        if source.parent.name not in ('es', 'en'):
            continue
        data = yaml.safe_load(source.read_text())
        problems, expected = preflight.check(str(source))
        deck = source.with_suffix('.pptx')
        pdf = PPTS.parent / 'pdf' / 'decks' / source.with_suffix('.pdf')
        row = {'source': str(source), 'expected_pages': expected}
        problems = list(problems)
        if not deck.exists() or not pdf.exists():
            problems.append('missing built deck or exported PDF')
        else:
            hashes = {key: digest(path) for key, path in
                      [('source', source), ('pptx', deck), ('pdf', pdf)]}
            prior = cached.get(str(source))
            if prior and hashes == prior.get('sha256'):
                row = dict(prior)
                report['hash_validated_cached_lessons'] += 1
            else:
                actual = len(Presentation(deck).slides)
                row['pptx_pages'] = actual
                problems.extend(lint.check(str(deck)))
                size_counts, _, below = sizes.audit(str(deck))
                row['minimum_font_pt'] = min(size_counts) if size_counts else None
                if below:
                    problems.append(f'{len(below)} text runs below font floor')
                with pymupdf.open(pdf) as document:
                    row['pdf_pages'] = len(document)
                    if expected != actual or expected != len(document):
                        problems.append('source, PPTX and PDF page counts differ')
                    empty = [i + 1 for i, page in enumerate(document) if not page.get_text().strip()]
                    if empty:
                        problems.append(f'PDF pages without text: {empty}')
                row['sha256'] = hashes
        for slide in data['slides']:
            figure = slide.get('figure')
            if figure is not None and deck.exists():
                picture = PPTS / figure['image']
                if picture.exists() and picture.stat().st_mtime > deck.stat().st_mtime:
                    problems.append(f'figure newer than built deck: {picture}')
        for text, language in code_sources(data['slides'], data['meta'].get('language', 'python')):
            report['code_source_blocks'] += 1
            rendered = '\n'.join(''.join(value for value, _ in line)
                                 for line in highlight.highlight(text, language))
            if rendered != text.rstrip('\n'):
                problems.append('highlighted code differs from source')
        group = str(source.parent)
        report['groups'][group] = report['groups'].get(group, 0) + expected
        if problems:
            report['issues'].append({'source': str(source), 'issues': problems})
        report['lessons'].append(row)
    for group, expected in report['groups'].items():
        parts = Path(group).parts
        merged = PPTS.parent / 'pdf' / ('--'.join(parts[:-1]) + '.' + parts[-1] + '.pdf')
        if not merged.exists():
            report['issues'].append({'merged': str(merged), 'issues': ['missing merged PDF']})
        else:
            with pymupdf.open(merged) as document:
                if len(document) != expected:
                    report['issues'].append({'merged': str(merged), 'issues': ['merged page count differs']})
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')
    print(f"{len(report['lessons'])} lessons, {len(report['groups'])} merged PDFs, "
          f"{report['code_source_blocks']} code source blocks, {len(report['issues'])} issues")
    return bool(report['issues'])


if __name__ == '__main__':
    raise SystemExit(main())
