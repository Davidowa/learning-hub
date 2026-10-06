"""Compile built decks into PDFs: one per deck, then one per course and language
with a bookmark per session.

    python -m kit.pdf python/programacion-orientada-a-objetos        # both languages
    python -m kit.pdf python/programacion-orientada-a-objetos/es -o ../pdf
    python -m kit.pdf . -o ../pdf --jobs 3                            # everything

Two engines. On Windows with PowerPoint installed, PowerPoint itself exports the
PDF through COM (needs the ``comtypes`` package), which is the renderer the decks
were drawn for. Everywhere else, and on Windows without PowerPoint, LibreOffice
does it: ``soffice`` on the PATH, or LibreOffice in its usual install folder on
macOS and Windows. ``--engine`` forces one. Merging needs ``pypdf``.

Build the decks first (``python -m kit.build``); this module converts the
``.pptx`` that sit next to each ``.yaml``, so a stale deck gives a stale PDF.

The per-deck PDFs go to ``<out>/decks/<course>/<lang>/`` and the merged one to
``<out>/<course-slug>.<lang>.pdf``. Each merged file opens with an outline whose
entries read like the cover: "Semana 03 · Tipos, espacios de nombres y string".
"""
from __future__ import annotations

import argparse
import concurrent.futures as cf
import glob
import os
import pathlib
import shutil
import subprocess
import sys
import tempfile

import yaml
from pypdf import PdfReader, PdfWriter


def _decks(target: str) -> list[str]:
    """Built decks only: a .pptx inside an es/ or en/ folder with its .yaml beside
    it. The template and the instructor's original decks are left out."""
    if os.path.isfile(target):
        return [target]
    found = glob.glob(os.path.join(target, '**', '*.pptx'), recursive=True)
    return sorted((p for p in found
                   if os.path.basename(os.path.dirname(os.path.abspath(p))) in ('es', 'en')
                   and os.path.exists(os.path.splitext(p)[0] + '.yaml')), key=_order)


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


def find_soffice() -> str | None:
    """LibreOffice's command-line binary, on the PATH or where its installer puts it."""
    for name in ('soffice', 'libreoffice'):
        hit = shutil.which(name)
        if hit:
            return hit
    candidates = ['/Applications/LibreOffice.app/Contents/MacOS/soffice']
    for root in (os.environ.get('ProgramFiles'), os.environ.get('ProgramFiles(x86)'),
                 r'C:\Program Files', r'C:\Program Files (x86)'):
        if root:
            candidates.append(os.path.join(root, 'LibreOffice', 'program', 'soffice.exe'))
    return next((c for c in candidates if os.path.exists(c)), None)


def _out_pdf(pptx: str, outdir: str) -> str:
    return os.path.join(outdir, os.path.splitext(os.path.basename(pptx))[0] + '.pdf')


def convert(pptx: str, outdir: str, soffice: str = 'soffice') -> str:
    """One deck to PDF with LibreOffice. Each call gets its own profile so several
    can run at once; a shared profile makes the second instance exit silently."""
    os.makedirs(outdir, exist_ok=True)
    profile = tempfile.mkdtemp(prefix='lo-')
    try:
        subprocess.run([soffice, '--headless',
                        f'-env:UserInstallation={pathlib.Path(profile).as_uri()}',
                        '--convert-to', 'pdf', '--outdir', outdir, pptx],
                       check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
                       timeout=600)
    finally:
        shutil.rmtree(profile, ignore_errors=True)
    pdf = _out_pdf(pptx, outdir)
    if not os.path.exists(pdf):
        raise RuntimeError(f'LibreOffice produced nothing for {pptx}')
    return pdf


def powerpoint_app():
    """PowerPoint through COM, or None when this is not Windows with PowerPoint."""
    if sys.platform != 'win32':
        return None
    try:
        import comtypes.client
        return comtypes.client.CreateObject('PowerPoint.Application')
    except Exception:
        return None


def convert_powerpoint(app, pptx: str, outdir: str) -> str:
    """One deck to PDF with PowerPoint. COM drives a single PowerPoint, so these
    run one after another rather than in parallel."""
    os.makedirs(outdir, exist_ok=True)
    pdf = os.path.abspath(_out_pdf(pptx, outdir))
    # Open(FileName, ReadOnly=msoTrue, Untitled=msoFalse, WithWindow=msoFalse)
    pres = app.Presentations.Open(os.path.abspath(pptx), -1, 0, 0)
    try:
        pres.SaveAs(pdf, 32)            # 32 = ppSaveAsPDF
    finally:
        pres.Close()
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
    ap.add_argument('--jobs', type=int, default=max(1, (os.cpu_count() or 2) - 1),
                    help='parallel LibreOffice conversions (PowerPoint always runs one)')
    ap.add_argument('--engine', choices=('auto', 'powerpoint', 'libreoffice'), default='auto',
                    help='auto: PowerPoint on Windows when installed, LibreOffice otherwise')
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

    app = powerpoint_app() if a.engine in ('auto', 'powerpoint') else None
    if a.engine == 'powerpoint' and app is None:
        sys.exit('PowerPoint is not available through COM. Install comtypes '
                 '(pip install comtypes) on a Windows machine with PowerPoint, '
                 'or use --engine libreoffice.')
    soffice = None if app else find_soffice()
    if app is None and soffice is None:
        sys.exit('No PDF engine found. Install LibreOffice (https://www.libreoffice.org/'
                 'download/, or on macOS: brew install --cask libreoffice) or, on Windows, '
                 'PowerPoint plus the comtypes package.')
    print(f"engine: {'PowerPoint' if app else 'LibreOffice (' + soffice + ')'}")

    done: dict[str, str] = {}
    if app:
        try:
            for n, (d, o) in enumerate(jobs, 1):
                done[d] = convert_powerpoint(app, d, o)
                print(f'[{n}/{len(jobs)}] {os.path.relpath(done[d])}')
        finally:
            app.Quit()
    else:
        with cf.ThreadPoolExecutor(max_workers=a.jobs) as ex:
            futs = {ex.submit(convert, d, o, soffice): d for d, o in jobs}
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
