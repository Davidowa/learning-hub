from pathlib import Path
import re,shutil,json,hashlib,zipfile
from html import escape
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate,Paragraph,Spacer,Table,TableStyle,Preformatted,KeepTogether
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.colors import HexColor
from reportlab.lib.pagesizes import A4
import pdfplumber

WORK=Path(__file__).parent.resolve()
OUT=Path(__file__).resolve().parents[2]/'Entregas'
ROOT=Path(__file__).resolve().parents[2]
for name,file in [('Sans','arial.ttf'),('Bold','arialbd.ttf'),('Mono','consola.ttf')]:pdfmetrics.registerFont(TTFont(name,'C:/Windows/Fonts/'+file))
pdfmetrics.registerFontFamily('Sans',normal='Sans',bold='Bold',italic='Sans',boldItalic='Bold')
styles={
 'body':ParagraphStyle('body',fontName='Sans',fontSize=10.3,leading=14.2,spaceAfter=8,textColor=HexColor('#15233b')),
 'step':ParagraphStyle('step',fontName='Sans',fontSize=10.3,leading=14.2,spaceAfter=8,leftIndent=17,firstLineIndent=-17,textColor=HexColor('#15233b')),
 'h1':ParagraphStyle('h1',fontName='Bold',fontSize=20,leading=25,spaceAfter=15,textColor=HexColor('#0f172a'),keepWithNext=True),
 'h2':ParagraphStyle('h2',fontName='Bold',fontSize=13,leading=17,spaceBefore=16,spaceAfter=9,textColor=HexColor('#2563eb'),keepWithNext=True),
 'h3':ParagraphStyle('h3',fontName='Bold',fontSize=11,leading=15,spaceBefore=10,spaceAfter=7,textColor=HexColor('#330867'),keepWithNext=True),
 'cell':ParagraphStyle('cell',fontName='Sans',fontSize=9.4,leading=12.3,textColor=HexColor('#15233b')),
 'headcell':ParagraphStyle('headcell',fontName='Bold',fontSize=9.4,leading=12.3,textColor=HexColor('#ffffff')),
 'code':ParagraphStyle('code',fontName='Mono',fontSize=10,leading=12.5,leftIndent=12,spaceBefore=6,spaceAfter=12)
}
def markup(s):
 s=escape(s)
 s=re.sub(r'`([^`]+)`',r'<b>\1</b>',s)
 s=re.sub(r'\*\*([^*]+)\*\*',r'<b>\1</b>',s)
 return s

class GuideDoc(SimpleDocTemplate):
 def afterFlowable(self,f):
  if isinstance(f,Paragraph) and f.style.name=='h2':
   key='section-'+str(getattr(self,'section_n',0));self.section_n=getattr(self,'section_n',0)+1
   self.canv.bookmarkPage(key);self.canv.addOutlineEntry(f.getPlainText(),key,0,False)

records=[]
for n in range(3,7):
 label=f'Lab{n:02}';source=ROOT/f'{label}-Base'/'Guia.md';text=source.read_text(encoding='utf-8');lines=text.splitlines();story=[];i=0
 while i<len(lines):
  l=lines[i]
  if not l.strip():i+=1;continue
  if l.startswith('```'):
   buf=[];i+=1
   while i<len(lines) and not lines[i].startswith('```'):buf.append(lines[i]);i+=1
   story.append(KeepTogether([Preformatted('\n'.join(buf),styles['code'])]));i+=1;continue
  if l.startswith('|'):
   rows=[]
   while i<len(lines) and lines[i].startswith('|'):
    row=[x.strip() for x in lines[i].strip('|').split('|')]
    if not all(re.fullmatch(r'[-: ]+',v) for v in row):rows.append(row)
    i+=1
   widths={2:[210,299],3:[180,100,229],4:[115,33,92,269]}[len(rows[0])]
   cells=[[Paragraph(markup(v),styles['headcell' if ri==0 else 'cell']) for v in row] for ri,row in enumerate(rows)]
   t=Table(cells,colWidths=widths,repeatRows=1,hAlign='LEFT',spaceBefore=5,spaceAfter=12)
   t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),HexColor('#193b78')),('ROWBACKGROUNDS',(0,1),(-1,-1),[HexColor('#f0f4fb'),HexColor('#ffffff')]),('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),7),('RIGHTPADDING',(0,0),(-1,-1),7),('TOPPADDING',(0,0),(-1,-1),7),('BOTTOMPADDING',(0,0),(-1,-1),7),('LINEBELOW',(0,0),(-1,0),.5,HexColor('#193b78')),('LINEBELOW',(0,1),(-1,-1),.35,HexColor('#dce1ea'))]))
   # Keep the compact Inspector tables together; split only genuinely long tables.
   if t.wrap(509,10000)[1]<285:story.append(KeepTogether([t]))
   else:story.append(t)
   continue
  if l.startswith('# '):kind='h1';l=l[2:]
  elif l.startswith('## '):kind='h2';l=l[3:]
  elif l.startswith('### '):kind='h3';l=l[4:]
  else:kind='step' if re.match(r'^\d+\. |^- ',l) else 'body'
  story.append(Paragraph(markup(l),styles[kind]));i+=1
 def footer(c,doc):
  c.saveState();c.setStrokeColor(HexColor('#dce1ea'));c.line(43,35,A4[0]-43,35)
  c.setFillColor(HexColor('#2563eb'));c.setFont('Bold',8);c.drawString(43,A4[1]-25,f'LABORATORIO {n:02}  /  GUÍA DE CONSTRUCCIÓN R2')
  c.setFillColor(HexColor('#5b6478'));c.setFont('Sans',8);c.drawString(43,23,'Unity 6000.3.27f1 · Revisión 12/11/2026 · R2');c.drawRightString(A4[0]-43,23,str(doc.page));c.restoreState()
 if n==5:
  endsection=next(j for j,f in enumerate(story) if isinstance(f,Paragraph) and f.style.name=='h2' and f.getPlainText().startswith('13.'))
  story=story[:endsection]+[KeepTogether(story[endsection:])]
 pdf=OUT/f'{label}-Guia.pdf'
 GuideDoc(str(pdf),pagesize=A4,leftMargin=43,rightMargin=43,topMargin=46,bottomMargin=48,title=text.splitlines()[0][2:],author='David Escobar Castillejos').build(story,onFirstPage=footer,onLaterPages=footer)
 with pdfplumber.open(pdf) as doc:
  pages=len(doc.pages)
  for page in doc.pages:
   assert all(0<=ch['x0']<ch['x1']<=page.width+1 and 0<=ch['top']<ch['bottom']<=page.height+1 for ch in page.chars),label
  alltext='\n'.join(p.extract_text() or '' for p in doc.pages)
  assert 'referencias finales' in alltext and 'CONFIGURACION CORRECTA' in alltext
  assert 'LAB_BUILD_SUCCEEDED' in alltext
 for edition in ['Base','Solucion']:
  project=ROOT/f'{label}-{edition}';bak=WORK/'originales'/project.name;bak.mkdir(parents=True,exist_ok=True)
  for name in ['Guia.md','Guia.pdf']:
   if not (bak/name).exists():shutil.copy2(project/name,bak/name)
  (project/'Guia.md').write_text(text,encoding='utf-8');shutil.copy2(pdf,project/'Guia.pdf')
  archive=OUT/f'{label}-Editor-{edition}.zip'
  with zipfile.ZipFile(archive) as z:old={x.filename:(x,z.read(x.filename)) for x in z.infolist()}
  temp=WORK/f'{label}-{edition}-R2.zip'
  with zipfile.ZipFile(temp,'w',zipfile.ZIP_DEFLATED,compresslevel=8) as z:
   for name,(info,data) in old.items():
    rel=name.split('/',1)[1]
    if rel=='Guia.md':data=text.encode('utf-8')
    elif rel=='Guia.pdf':data=pdf.read_bytes()
    z.writestr(info,data)
  with zipfile.ZipFile(temp) as z:
   assert z.testzip() is None
   for name,(info,data) in old.items():
    if name.split('/',1)[1] not in ['Guia.md','Guia.pdf']:assert z.read(name)==data,(label,name)
  shutil.copy2(temp,archive)
  records.append({'file':archive.name,'bytes':archive.stat().st_size,'sha256':hashlib.sha256(archive.read_bytes()).hexdigest(),'revision':'R2; only Guia.md and Guia.pdf changed'})
 print(label,pages,'pages',len(text.split()),'words')
(WORK/'archivos-R2.json').write_text(json.dumps(records,ensure_ascii=False,indent=2),encoding='utf-8')
# Preserve records for the other files while updating hashes of the eight ZIPs.
(OUT/'paquetes-verificados.json').write_text(json.dumps(records,ensure_ascii=False,indent=2),encoding='utf-8')
with zipfile.ZipFile(OUT/'Laboratorios-03-a-06-Materiales-revisados.zip','w',zipfile.ZIP_DEFLATED) as z:
 for glob in ['Lab*-Editor-*.zip','Lab*-Guia.pdf']:
  for p in sorted(OUT.glob(glob)):z.write(p,p.name)
 for name in ['Estado-de-revision.txt']:
  if (OUT/name).exists():z.write(OUT/name,name)
 if (ROOT/'Infografia/OnGUI-y-Canvas-Learning-Hub.pdf').exists():z.write(ROOT/'Infografia/OnGUI-y-Canvas-Learning-Hub.pdf','OnGUI-y-Canvas-Learning-Hub.pdf')
with zipfile.ZipFile(OUT/'Guias-Laboratorios-03-a-06-R2.zip','w',zipfile.ZIP_DEFLATED) as z:
 for p in sorted(OUT.glob('Lab*-Guia.pdf')):z.write(p,p.name)
