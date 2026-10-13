"""Run installed the-writer v4.1 lint on lesson prose, with slide locations.

The installed phrase cache keys temporary lists by id. Holding references during
one lint call prevents reuse of those ids; the original rules and pattern
compiler are unchanged. This does not modify any installed skill file.
"""
from pathlib import Path
import argparse
import importlib.util
import json

import yaml

ROOT = Path(__file__).resolve().parents[3]


def module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    value = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(value)
    return value


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--out', type=Path, required=True)
    args = ap.parse_args()
    writer = module('writer', Path.home() / '.agents/skills/the-writer/scripts/lint.py')
    extractor = module('extractor', ROOT / 'ppts/audit/herramientas/extraer_prosa.py')
    original = writer.phrase_pattern
    references = []

    def stable_pattern(phrases):
        references.append(phrases)
        return original(phrases)

    writer.phrase_pattern = stable_pattern
    report = []
    for source in sorted((ROOT / 'ppts').rglob('*.yaml')):
        if source.parent.name not in ('es', 'en'):
            continue
        data = yaml.safe_load(source.read_text())
        fields = []
        for number, slide in enumerate(data['slides'], 1):
            layout, contents = next(iter(slide.items()))
            prose = []
            extractor.walk(contents, [], prose)
            fields.extend((number, layout, field, text) for field, text in prose)
        text = '\n\n'.join(' '.join(field[3].split()) for field in fields)
        writer._PHRASE_CACHE.clear()
        references.clear()
        result = writer.lint(text, data['meta'].get('lang', 'en'), 'casual', 'essay', True)
        findings = []
        for finding in result['findings']:
            if finding['severity'] != 'HIGH' or finding['rule'] == 'choppy-paragraphs':
                continue
            index = (finding['line'] - 1) // 2
            item = dict(finding, location=fields[index][:3] if 0 <= index < len(fields) else None)
            findings.append(item)
        report.append({'source': str(source.relative_to(ROOT)), 'findings': findings})
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps({'skill': 'the-writer 4.1.0',
                                   'format_exception': 'Fragmented slide rows are not essay paragraphs.',
                                   'lessons': report}, ensure_ascii=False, indent=2) + '\n')
    print(f'{len(report)} lessons; raw HIGH findings: {sum(len(row["findings"]) for row in report)}')


if __name__ == '__main__':
    main()
