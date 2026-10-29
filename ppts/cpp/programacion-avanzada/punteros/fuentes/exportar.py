from pathlib import Path
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from pypdf import PdfReader
import shutil, json, hashlib
r=Path(__file__).resolve().parents[1]
images=sorted((r/'es').glob('*.png'))
assert len(images)==2
pdf=r/'Punteros en CPP - Infografía visual - Learning Hub.pdf'
c=canvas.Canvas(str(pdf),pagesize=letter,pageCompression=1)
c.setTitle('Punteros en C++: dirección, contenido y cadenas | Learning Hub')
c.setAuthor('David Escobar-Castillejos')
c.setSubject('Infografía en dos láminas: &, *, char*, C-strings y getMatricula().')
for img in images:
 c.drawImage(str(img),0,0,width=612,height=792,preserveAspectRatio=True,anchor='c')
 c.showPage()
c.save()
pages=PdfReader(pdf).pages
assert len(pages)==2
assert all([float(v) for v in p.mediabox]==[0.,0.,612.,792.] for p in pages)
export=Path('/Users/davidowa/Downloads/Learning Hub - CPP - Punteros')
export.mkdir(exist_ok=True)
for p in [pdf,*images]:shutil.copy2(p,export/p.name)
manifest={'pdf':str(pdf),'paginas':len(pages),'tamano_pt':[612,792],'generador':'ImageGen integrado','imagenes':[{'archivo':p.name,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in images],'pdf_sha256':hashlib.sha256(pdf.read_bytes()).hexdigest()}
(r/'fuentes/exportacion.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2))
print(pdf)
