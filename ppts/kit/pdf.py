"""Compile built decks into PDFs: one per deck, then one per course and language
with a bookmark per session.

    python -m kit.pdf python/programacion-orientada-a-objetos        # both languages
    python -m kit.pdf python/programacion-orientada-a-objetos/es -o ../pdf
    python -m kit.pdf . -o ../pdf --jobs 3                            # everything

Needs LibreOffice (``soffice``) on the PATH and ``pypdf``. Build the decks first
(``python -m kit.build``); this module converts the ``.pptx`` that sit next to
each ``.yaml``, so a stale deck gives a stale PDF.

The per-deck PDFs go to ``<out>/decks/<course>/<lang>/`` and the merged one to
``<out>/<course-slug>.<lang>.pdf``. Each merged file opens with an outline whose
entries read like the cover: "Semana 03 · Tipos, espacios de nombres y string".
"""
from __future__ import annotations

import argparse
import concurrent.futures as cf
import glob
import os
import shutil
import subprocess
import sys
import tempfile

import yaml
from pypdf import PdfReader, PdfWriter


def _decks(target: str) -> list[str]:
    if os.path.isfile(target):
        return [target]
    return sorted(glob.glob(os.path.join(target, '**', '*.pptx'), recursive=True),
                  key=_order)


def _order(path: str):
    """w01 < w01.1 < w02 < w10, whatever the string sort says."""
    stem = os.path.basename(path).split('.')
    nums = []
    for part in stem:
        digits = part.lstrip('w')
        if digits.isdigit():
            nums.append(int(digits))
    return (os.path.dirname(path), nums)


def _label(pptx: str) -> str:
    """Outline entry for a deck, read off the cover in the YAML beside it."""
    src = os.path.splitext(pptx)[0] + '.yaml'
    try:
        doc = yaml.safe_load(open(src, encoding='utf-8'))
        cover = next(s['cover'] for s in doc['slides'] if 'cover' in s)
        unit = str(cover.get('unit', '')).strip()
        return unit or os.path.basename(src)
    except Exception:
        return os.path.basename(pptx)


def convert(pptx: str, outdir: str) -> str:
    """One deck to PDF. Each call gets its own LibreOffice profile so several can
    run at once; a shared profile makes the second instance exit silently."""
    os.makedirs(outdir, exist_ok=True)
    profile = tempfile.mkdtemp(prefix='lo-')
    try:
        subprocess.run(['soffice', '--headless', f'-env:UserInstallation=file://{profile}',
                        '--convert-to', 'pdf', '--outdir', outdir, pptx],
                       check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
                       timeout=600)
    finally:
        shutil.rmtree(profile, ignore_errors=True)
    pdf = os.path.join(outdir, os.path.splitext(os.path.basename(pptx))[0] + '.pdf')
    if not os.path.exists(pdf):
        raise RuntimeError(f'LibreOffice produced nothing for {pptx}')
    return pdf


def merge(pdfs: list[tuple[str, str]], out: str, title: str) -> int:
    """Concatenate (label, pdf) pairs with one outline entry per deck."""
    w = PdfWriter()
    w.add_metadata({'/Title': title, '/Author': 'David Escobar-Castillejos'})
    pages = 0
    for label, pdf in pdfs:
        r = PdfReader(pdf)
        start = len(w.pages)
        for p in r.pages:
            w.add_page(p)
        w.add_outline_item(label, start)
        pages += len(r.pages)
    os.makedirs(os.path.dirname(os.path.abspath(out)), exist_ok=True)
    with open(out, 'wb') as fh:
        w.write(fh)
    return pages


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split('\n')[0])
    ap.add_argument('target', help='a course folder, a language folder, or ppts itself')
    ap.add_argument('-o', '--out', default='../pdf', help='where the PDFs go (default ../pdf)')
    ap.add_argument('--jobs', type=int, default=max(1, (os.cpu_count() or 2) - 1))
    a = ap.parse_args(argv)

    decks = _decks(a.target)
    if not decks:
        sys.exit(f'no .pptx under {a.target}; run python -m kit.build first')

    # group by course folder and language folder: .../<course>/<lang>/wNN.<lang>.pptx
    groups: dict[tuple[str, str], list[str]] = {}
    for d in decks:
        lang_dir = os.path.dirname(os.path.abspath(d))
        course_dir = os.path.dirname(lang_dir)
        groups.setdefault((course_dir, os.path.basename(lang_dir)), []).append(d)

    here = os.path.abspath('.')
    jobs = []
    for (course_dir, lang), items in groups.items():
        rel = os.path.relpath(course_dir, here)
        for d in items:
            jobs.append((d, os.path.join(a.out, 'decks', rel, lang)))

    done: dict[str, str] = {}
    with cf.ThreadPoolExecutor(max_workers=a.jobs) as ex:
        futs = {ex.submit(convert, d, o): d for d, o in jobs}
        for n, f in enumerate(cf.as_completed(futs), 1):
            d = futs[f]
            done[d] = f.result()
            print(f'[{n}/{len(jobs)}] {os.path.relpath(done[d])}')

    for (course_dir, lang), items in sorted(groups.items()):
        rel = os.path.relpath(course_dir, here)
        slug = rel.replace(os.sep, '--')
        doc = yaml.safe_load(open(os.path.splitext(items[0])[0] + '.yaml', encoding='utf-8'))
        title = f"{doc.get('meta', {}).get('course', slug)} ({lang})"
        out = os.path.join(a.out, f'{slug}.{lang}.pdf')
        pages = merge([(_label(d), done[d]) for d in items], out, title)
        size = os.path.getsize(out) / 1e6
        print(f'{out}  {len(items)} decks, {pages} pages, {size:.1f} MB')


if __name__ == '__main__':
    main()
