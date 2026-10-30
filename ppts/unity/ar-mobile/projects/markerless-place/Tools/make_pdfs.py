"""Render the markerless placement guide using ReportLab."""
from pathlib import Path
from html import escape
import re
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter,A4
from reportlab.lib.units import cm
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Preformatted
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

ROOT=Path(__file__).resolve().parents[1]
GUIDE=ROOT.parents[1]/'labs/lab04.es.md'
if not GUIDE.exists():
    GUIDE=ROOT/'Guia.es.md'
OUTPUT=GUIDE.with_suffix('.pdf')
FONT_DIR=Path('/System/Library/Fonts/Supplemental')
if (FONT_DIR/'Arial.ttf').exists():
    pdfmetrics.registerFont(TTFont('Body',str(FONT_DIR/'Arial.ttf')))
    pdfmetrics.registerFont(TTFont('BodyBold',str(FONT_DIR/'Arial Bold.ttf')))
else:
    pdfmetrics.registerFont(pdfmetrics.Font('Body','Helvetica','WinAnsiEncoding'))
    pdfmetrics.registerFont(pdfmetrics.Font('BodyBold','Helvetica-Bold','WinAnsiEncoding'))
styles=getSampleStyleSheet()
navy=colors.HexColor('#132A38')
styles.add(ParagraphStyle(name='LabTitle',fontName='BodyBold',fontSize=21,leading=26,textColor=navy,spaceAfter=16))
styles.add(ParagraphStyle(name='LabHeading',fontName='BodyBold',fontSize=13.5,leading=18,textColor=navy,spaceBefore=15,spaceAfter=7,keepWithNext=True))
styles.add(ParagraphStyle(name='LabBody',fontName='Body',fontSize=10,leading=13.6,spaceAfter=6.5,splitLongWords=True))
styles.add(ParagraphStyle(name='LabBullet',parent=styles['LabBody'],leftIndent=12,firstLineIndent=-9))
styles.add(ParagraphStyle(name='LabStep',parent=styles['LabBody'],leftIndent=19,firstLineIndent=-19))

def inline(text):
    text=escape(text)
    text=re.sub(r'`([^`]+)`',r'<font name="Courier" size="9">\1</font>',text)
    # Web references remain selectable and clickable in the PDF.
    text=re.sub(r'(https://[^\s<]+)',r'<link href="\1" color="#15526A">\1</link>',text)
    return text

flow=[]
for block in re.split(r'\n\s*\n',GUIDE.read_text()):
    block=block.strip()
    if not block:continue
    if block.startswith('# '):
        flow.append(Paragraph(inline(block[2:]),styles['LabTitle']))
    elif block.startswith('## '):
        flow.append(Paragraph(inline(block[3:]),styles['LabHeading']))
    elif block.startswith('```'):
        flow.append(Preformatted('\n'.join(block.splitlines()[1:-1]),styles['Code']))
    else:
        lines=block.splitlines()
        if all(line.startswith('- ') for line in lines):
            for line in lines:flow.append(Paragraph('• '+inline(line[2:]),styles['LabBullet']))
        elif re.match(r'^\d+\. ',block):
            for line in lines:flow.append(Paragraph(inline(line),styles['LabStep']))
        else:flow.append(Paragraph(inline(' '.join(lines)),styles['LabBody']))

PAGE_W,PAGE_H=letter

def page_chrome(c,doc):
    c.saveState()
    c.setStrokeColor(colors.HexColor('#C8D2D8'));c.setLineWidth(.5)
    c.line(1.8*cm,PAGE_H-1.35*cm,PAGE_W-1.8*cm,PAGE_H-1.35*cm)
    c.setFont('Body',8);c.setFillColor(navy)
    c.drawString(1.8*cm,PAGE_H-1.1*cm,'Práctica 4 · Colocar figuras sin marcador · Unity 6.3 LTS')
    c.drawString(1.8*cm,1.0*cm,'Proyecto fuente y pruebas en Android')
    c.drawRightString(PAGE_W-1.8*cm,1.0*cm,str(doc.page))
    c.restoreState()

doc=SimpleDocTemplate(str(OUTPUT),pagesize=letter,leftMargin=1.8*cm,rightMargin=1.8*cm,
    topMargin=1.8*cm,bottomMargin=1.7*cm,title='Práctica 4 · Colocar figuras sin marcador',author='LearningHub')
doc.build(flow,onFirstPage=page_chrome,onLaterPages=page_chrome)

print(OUTPUT)
