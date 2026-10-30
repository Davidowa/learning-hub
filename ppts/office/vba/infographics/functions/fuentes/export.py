from pathlib import Path
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from pypdf import PdfReader
from PIL import Image
import shutil, hashlib, json
root=Path(__file__).resolve().parents[1]
images=sorted((root/'en').glob('*.png'))
assert len(images)==2
pdf=root/'VBA Functions and Excel Functions in VBA - Learning Hub.pdf'
c=canvas.Canvas(str(pdf),pagesize=letter,pageCompression=1)
c.setTitle('VBA Functions and Excel Functions in VBA')
c.setAuthor('David Escobar-Castillejos')
c.setSubject('Writing a VBA Function and calling Excel worksheet functions from VBA.')
for p in images:
 c.drawImage(str(p),0,0,width=612,height=792,preserveAspectRatio=True,anchor='c')
 c.showPage()
c.save()
reader=PdfReader(pdf)
assert len(reader.pages)==2
assert all([float(v) for v in page.mediabox]==[0.,0.,612.,792.] for page in reader.pages)
export=Path('/Users/davidowa/Downloads/Learning Hub - VBA Functions - EN')
export.mkdir(exist_ok=True)
for p in [pdf,*images,root/'FunctionsExamples.bas',root/'README.en.md',root/'fuentes/01.en.md',root/'fuentes/02.en.md']:
 shutil.copy2(p,export/p.name)
manifest={'pdf':pdf.name,'pages':2,'page_size_pt':[612,792],'image_generation':'Built-in ImageGen','pdf_sha256':hashlib.sha256(pdf.read_bytes()).hexdigest(),'images':[{'name':p.name,'size':list(Image.open(p).size),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in images],'export_folder':str(export),'vba_executed':False}
(root/'fuentes/export.json').write_text(json.dumps(manifest,indent=2))
print(pdf)
print(export)
