"""Render the four guided VR labs as Letter PDFs with the Unity kit palette.

Run with the bundled Python runtime (ReportLab), optionally passing --output-dir.
The Markdown files remain the editable source; no browser or Unity is required.
"""
from pathlib import Path
import argparse
import html
import re

from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, Preformatted,
)

ROOT = Path(__file__).resolve().parent
FONT_DIR = Path('/System/Library/Fonts/Supplemental')
for name, filename in [('Arial', 'Arial.ttf'), ('Arial-Bold', 'Arial Bold.ttf'),
                       ('Georgia-Bold', 'Georgia Bold.ttf')]:
    pdfmetrics.registerFont(TTFont(name, str(FONT_DIR / filename)))
pdfmetrics.registerFontFamily('Arial', normal='Arial', bold='Arial-Bold')

INK = colors.HexColor('#222629')
MUTED = colors.HexColor('#515C66')
RULE = colors.HexColor('#D6DBDF')
ORANGE = colors.HexColor('#B4530A')
FILL = colors.HexColor('#F3F4F5')
STYLES = {
    'body': ParagraphStyle('body', fontName='Arial', fontSize=9.8, leading=13.2,
                           textColor=INK, spaceAfter=6),
    'title': ParagraphStyle('title', fontName='Georgia-Bold', fontSize=24, leading=28,
                            textColor=INK, spaceAfter=12),
    'h2': ParagraphStyle('h2', fontName='Arial-Bold', fontSize=13, leading=17,
                         textColor=ORANGE, spaceBefore=11, spaceAfter=7,
                         keepWithNext=True),
    'meta': ParagraphStyle('meta', fontName='Arial', fontSize=9.4, leading=13,
                           textColor=MUTED, spaceAfter=12),
    'cell': ParagraphStyle('cell', fontName='Arial', fontSize=9.1, leading=12,
                           textColor=INK, alignment=TA_LEFT),
    'head': ParagraphStyle('head', fontName='Arial-Bold', fontSize=9.1, leading=12,
                           textColor=colors.white),
    'list': ParagraphStyle('list', fontName='Arial', fontSize=9.8, leading=13.2,
                           leftIndent=14, firstLineIndent=-14, spaceAfter=6,
                           textColor=INK),
    'code': ParagraphStyle('code', fontName='Courier', fontSize=8.1, leading=10.4,
                           textColor=INK, backColor=FILL, borderPadding=8,
                           spaceBefore=5, spaceAfter=9),
}

NAMES = {
    'VR-C00': 'VR-C00 - Primer montaje XR y torquimetro.pdf',
    'VR-C01': 'VR-C01 - Presencia escala y seguimiento.pdf',
    'VR-C02': 'VR-C02 - Interaccion y retroalimentacion.pdf',
    'VR-C03': 'VR-C03 - Locomocion y orientacion espacial.pdf',
    'VR-C04': 'VR-C04 - Opcional - Cibermareo y comodidad.pdf',
}


def inline(text):
    text = html.escape(text)
    text = re.sub(r'\[([^\]]+)\]\((https?://[^)]+)\)',
                  r'<link href="\2" color="#B4530A"><u>\1</u></link>', text)
    text = re.sub(r'`([^`]+)`', r'<font face="Courier">\1</font>', text)
    return re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', text)


def table(lines, width):
    rows = [[cell.strip() for cell in line.strip().strip('|').split('|')]
            for line in lines]
    rows = [row for row in rows if not all(re.fullmatch(r'[:\- ]+', c) for c in row)]
    count = len(rows[0])
    fractions = {2: [0.29, 0.71], 3: [0.29, 0.13, 0.58], 4: [0.13, 0.14, 0.14, 0.59]}
    if count == 3 and rows[0][1] != 'Puntos':
        fractions[3] = [0.27, 0.35, 0.38]
    data = [[Paragraph(inline(c), STYLES['head' if i == 0 else 'cell'])
             for c in row] for i, row in enumerate(rows)]
    t = Table(data, colWidths=[width*f for f in fractions[count]], repeatRows=1,
              hAlign='LEFT')
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), INK),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, FILL]),
        ('LINEBELOW', (0, 0), (-1, -1), 0.4, RULE),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('LEFTPADDING', (0, 0), (-1, -1), 8),
        ('RIGHTPADDING', (0, 0), (-1, -1), 8),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
    ]))
    return [Spacer(1, 3), t, Spacer(1, 9)]


def render(source, output):
    code = source.name[:6]
    title = source.read_text().splitlines()[0].removeprefix('# ')
    doc = SimpleDocTemplate(str(output), pagesize=letter, leftMargin=46,
        rightMargin=46, topMargin=57, bottomMargin=48,
        title=title, author='David Escobar-Castillejos | Learning Hub')
    story = []
    lines = source.read_text().splitlines()
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        if not line:
            i += 1
            continue
        if line == '::: pagebreak':
            story.append(PageBreak())
        elif line.startswith('```'):
            code_lines = []
            i += 1
            while i < len(lines) and not lines[i].startswith('```'):
                code_lines.append(lines[i]); i += 1
            story.append(Preformatted('\n'.join(code_lines), STYLES['code'],
                                      maxLineLength=95))
        elif line.startswith('|'):
            block = []
            while i < len(lines) and lines[i].strip().startswith('|'):
                block.append(lines[i]); i += 1
            story.extend(table(block, doc.width)); continue
        elif line.startswith('# '):
            story.append(Paragraph(inline(line[2:].split(' | ', 1)[1]), STYLES['title']))
        elif line.startswith('## '):
            story.append(Paragraph(inline(line[3:]), STYLES['h2']))
        elif line.startswith('Unity 6.3'):
            story.append(Paragraph(inline(line), STYLES['meta']))
        elif re.match(r'^\d+\. ', line) or line.startswith('- '):
            story.append(Paragraph(inline(line if not line.startswith('- ') else '• '+line[2:]), STYLES['list']))
        else:
            paragraph = [line]
            while i+1 < len(lines) and lines[i+1].strip() and not lines[i+1].startswith(('#','|',':::','- ','```')) and not re.match(r'^\d+\. ', lines[i+1]):
                i += 1; paragraph.append(lines[i].strip())
            story.append(Paragraph(inline(' '.join(paragraph)), STYLES['body']))
        i += 1

    def page(canvas, doc):
        canvas.saveState()
        canvas.setFillColor(INK)
        canvas.setFont('Arial-Bold', 9)
        canvas.drawString(46, 760, 'LEARNING HUB / REALIDAD VIRTUAL')
        canvas.setFillColor(ORANGE)
        canvas.drawRightString(566, 760, code + (' · OPCIONAL' if code == 'VR-C04' else ''))
        canvas.setStrokeColor(RULE)
        canvas.line(46, 750, 566, 750)
        canvas.line(46, 36, 566, 36)
        canvas.setFillColor(MUTED)
        canvas.setFont('Arial', 8)
        canvas.drawString(46, 24, 'Unity 6.3 LTS · URP · Meta Quest 3S')
        canvas.drawRightString(566, 24, str(doc.page))
        canvas.restoreState()
    doc.build(story, onFirstPage=page, onLaterPages=page)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--output-dir', type=Path, default=ROOT / 'output' / 'pdf')
    parser.add_argument('--lab', choices=NAMES)
    args = parser.parse_args()
    args.output_dir.mkdir(parents=True, exist_ok=True)
    for source in sorted(ROOT.glob('VR-C*.es.md')):
        if args.lab and source.name[:6] != args.lab:
            continue
        output = args.output_dir / NAMES[source.name[:6]]
        render(source, output)
        print(output)
