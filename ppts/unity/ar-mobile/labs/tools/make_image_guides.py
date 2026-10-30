"""Build the first two AR guides from their Markdown sources using ReportLab."""
from pathlib import Path
from html import escape
import re
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import cm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Paragraph, Flowable, Spacer, PageBreak

ROOT = Path(__file__).resolve().parents[1]
FONT_DIR = Path('/System/Library/Fonts/Supplemental')
if (FONT_DIR / 'Arial.ttf').exists():
    pdfmetrics.registerFont(TTFont('GuideBody', str(FONT_DIR / 'Arial.ttf')))
    pdfmetrics.registerFont(TTFont('GuideBold', str(FONT_DIR / 'Arial Bold.ttf')))
else:
    pdfmetrics.registerFont(pdfmetrics.Font('GuideBody', 'Helvetica', 'WinAnsiEncoding'))
    pdfmetrics.registerFont(pdfmetrics.Font('GuideBold', 'Helvetica-Bold', 'WinAnsiEncoding'))
NAVY = colors.HexColor('#132A38')
STYLES = {
    'title': ParagraphStyle('title', fontName='GuideBold', fontSize=21, leading=26, textColor=NAVY, spaceAfter=16),
    'heading': ParagraphStyle('heading', fontName='GuideBold', fontSize=13.5, leading=18, textColor=NAVY, spaceBefore=13, spaceAfter=6, keepWithNext=True),
    'body': ParagraphStyle('body', fontName='GuideBody', fontSize=10, leading=13.2, spaceAfter=5.5, splitLongWords=True),
    'step': ParagraphStyle('step', fontName='GuideBody', fontSize=10, leading=13.2, spaceAfter=5.5, leftIndent=19, firstLineIndent=-19),
    'bullet': ParagraphStyle('bullet', fontName='GuideBody', fontSize=10, leading=13.2, spaceAfter=5.5, leftIndent=12, firstLineIndent=-9),
    'code': ParagraphStyle('code', fontName='Courier', fontSize=8.1, leading=10.2, leftIndent=8, rightIndent=4, backColor=colors.HexColor('#F2F5F6'), borderPadding=6, spaceBefore=5, spaceAfter=9),
}

def inline(text):
    text = escape(text)
    text = re.sub(r'`([^`]+)`', r'<font name="Courier" size="9">\1</font>', text)
    return re.sub(r'(https://[^\s<]+)', r'<link href="\1" color="#15526A">\1</link>', text)


class CodeBlock(Flowable):
    def __init__(self, lines):
        super().__init__()
        self.lines = lines
        self.leading = 10.2
        self.padding = 7
        self.spaceBefore = 5
        self.spaceAfter = 9

    def wrap(self, available_width, available_height):
        self.width = available_width
        self.height = self.padding * 2 + len(self.lines) * self.leading
        return self.width, self.height

    def split(self, available_width, available_height):
        count = int((available_height - self.padding * 2) // self.leading)
        if count < 3:
            return []
        if len(self.lines) - count < 3:
            count = len(self.lines) - 3
        if count < 3:
            return []
        return [CodeBlock(self.lines[:count]), CodeBlock(self.lines[count:])]

    def draw(self):
        canvas = self.canv
        canvas.saveState()
        canvas.setFillColor(colors.HexColor('#F2F5F6'))
        canvas.rect(0, 0, self.width, self.height, fill=1, stroke=0)
        canvas.setFillColor(NAVY)
        text = canvas.beginText(self.padding, self.height - self.padding - 8.1)
        text.setFont('Courier', 8.1)
        text.setLeading(self.leading)
        for line in self.lines:
            text.textLine(line)
        canvas.drawText(text)
        canvas.restoreState()


class MarkerSheet(Flowable):
    def __init__(self, number):
        super().__init__()
        self.number = number
        self.width = 17.99 * cm
        self.height = 21.5 * cm

    def draw(self):
        canvas = self.canv
        canvas.setFillColor(NAVY)
        canvas.setFont('GuideBold', 18)
        canvas.drawString(0, 20.5 * cm, 'Marcador para imprimir' if self.number == 5 else 'QR para imprimir')
        canvas.setFont('GuideBody', 10)
        root = ROOT.parent / 'projects'
        if self.number == 5:
            canvas.drawString(0, 19.5 * cm, 'DICT_4X4_50 · ID 23 · Imprime al 100 %, sin ajustar a la hoja.')
            canvas.drawString(0, 18.8 * cm, 'El cuadrado negro debe medir 10 cm por lado. Conserva el margen blanco.')
            image = root / 'aruco-cube/Assets/Resources/Aruco23.png'
            canvas.drawImage(str(image), 4 * cm, 6.5 * cm, width=10 * cm, height=10 * cm, mask='auto')
            canvas.setLineWidth(.7)
            canvas.line(4 * cm, 5.5 * cm, 14 * cm, 5.5 * cm)
            canvas.line(4 * cm, 5.3 * cm, 4 * cm, 5.7 * cm)
            canvas.line(14 * cm, 5.3 * cm, 14 * cm, 5.7 * cm)
            canvas.drawCentredString(9 * cm, 4.9 * cm, '10 cm: verifica esta distancia con una regla')
        else:
            canvas.drawString(0, 19.5 * cm, 'Lee un código y después toca una superficie detectada para colocar la figura.')
            for x, name, label in [(0.5, 'cube', 'AR:CUBO'), (9.5, 'sphere', 'AR:ESFERA')]:
                image = root / ('qr-place/Marcadores/QR-' + name + '.png')
                canvas.drawImage(str(image), x * cm, 9.5 * cm, width=8 * cm, height=8 * cm, mask='auto')
                canvas.setFont('GuideBold', 14)
                canvas.drawCentredString((x + 4) * cm, 8.6 * cm, label)
            canvas.setFont('GuideBody', 10)
            canvas.drawString(0, 6.8 * cm, 'Conserva el margen blanco. El QR selecciona contenido, no fija la pose al papel.')
            canvas.drawString(0, 6.1 * cm, 'Usa Leer otro QR para cambiar de figura. Los objetos anteriores permanecen.')


def build(number):
    # Keep the fifth guide and its references on three text pages.
    for key in ('body', 'step', 'bullet'):
        STYLES[key].leading = 12.2 if number == 5 else 13.2
        STYLES[key].spaceAfter = 4.6 if number == 5 else 5.5
    STYLES['heading'].spaceBefore = 11 if number == 5 else 13
    STYLES['heading'].leading = 17 if number == 5 else 18
    source = ROOT / f'lab{number:02d}.es.md'
    title = source.read_text().splitlines()[0][2:]
    flow = []
    # Extract fenced blocks before paragraph splitting so blank code lines survive.
    for index, segment in enumerate(re.split(r'(```csharp\n[\s\S]*?\n```)', source.read_text())):
        if segment.startswith('```csharp'):
            code = segment.splitlines()[1:-1]
            if max(map(len, code)) > 96:
                raise ValueError('Code line too long for the guide')
            flow.append(CodeBlock(code))
            continue
        for block in re.split(r'\n\s*\n', segment):
            block = block.strip()
            if not block:
                continue
            if block.startswith('# '):
                flow.append(Paragraph(inline(block[2:]), STYLES['title']))
            elif block.startswith('## '):
                flow.append(Paragraph(inline(block[3:]), STYLES['heading']))
            elif all(line.startswith('- ') for line in block.splitlines()):
                for line in block.splitlines():
                    reference = re.match(r'(.+?): (https://\S+)$', line[2:])
                    if reference:
                        label, url = reference.groups()
                        value = '<link href="' + escape(url, quote=True) + '" color="#15526A">' + escape(label) + '</link>'
                    else:
                        value = inline(line[2:])
                    flow.append(Paragraph('• ' + value, STYLES['bullet']))
            elif re.match(r'^\d+\. ', block):
                for line in block.splitlines():
                    flow.append(Paragraph(inline(line), STYLES['step']))
            else:
                flow.append(Paragraph(inline(' '.join(block.splitlines())), STYLES['body']))

    if number in (5, 6):
        flow.extend([PageBreak(), MarkerSheet(number)])

    def chrome(canvas, doc):
        canvas.saveState()
        canvas.setFont('GuideBody', 8)
        canvas.setFillColor(NAVY)
        canvas.drawString(1.8 * cm, letter[1] - 1.1 * cm, f'Práctica {number} · AR · Unity 6.3 LTS')
        canvas.setStrokeColor(colors.HexColor('#C8D2D8'))
        canvas.setLineWidth(.5)
        canvas.line(1.8 * cm, letter[1] - 1.35 * cm, letter[0] - 1.8 * cm, letter[1] - 1.35 * cm)
        canvas.drawString(1.8 * cm, 1.0 * cm, 'Rastreo de imágenes y pruebas en Android' if number <= 2 else 'Proyecto fuente y pruebas en Android')
        canvas.drawRightString(letter[0] - 1.8 * cm, 1.0 * cm, str(doc.page))
        canvas.restoreState()
    output = source.with_suffix('.pdf')
    doc = SimpleDocTemplate(str(output), pagesize=letter, leftMargin=1.8 * cm, rightMargin=1.8 * cm,
        topMargin=1.8 * cm, bottomMargin=1.7 * cm, title=title, author='LearningHub')
    doc.build(flow, onFirstPage=chrome, onLaterPages=chrome)
    print(output)

if __name__ == '__main__':
    build(1)
    build(2)
