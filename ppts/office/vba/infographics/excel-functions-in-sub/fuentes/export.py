from pathlib import Path
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from pypdf import PdfReader
from PIL import Image
import hashlib,json,shutil
root=Path(__file__).resolve().parents[1]
img=root/'en/excel-functions-inside-a-sub.png'
pdf=root/'Excel Functions Inside a Sub - Learning Hub.pdf'
c=canvas.Canvas(str(pdf),pagesize=letter,pageCompression=1)
c.setTitle('Use Excel functions inside a Sub')
c.setAuthor('David Escobar-Castillejos')
c.setSubject('A complete VBA macro with Sum, Average, Max, and Range.Formula.')
c.drawImage(str(img),0,0,width=612,height=792,preserveAspectRatio=True,anchor='c')
c.showPage();c.save()
r=PdfReader(pdf)
assert len(r.pages)==1
assert [float(v) for v in r.pages[0].mediabox]==[0.,0.,612.,792.]
initial=[10,20,30,40]; changed=[10,20,30,80]
assert [sum(initial),sum(initial)/len(initial),max(initial)]==[100,25,40]
assert [sum(changed),sum(changed)/len(changed),max(changed)]==[140,35,80]
export=Path('/Users/davidowa/Downloads/Learning Hub - Excel Functions in a Sub - EN')
export.mkdir(exist_ok=True)
for p in [pdf,img,root/'ExcelFunctionsInSub.bas',root/'README.en.md',root/'fuentes/content.en.md',root/'fuentes/infographic.prompt.txt']:
 shutil.copy2(p,export/p.name)
manifest={'pdf':pdf.name,'page_size_pt':[612,792],'page_count':1,'png_size':list(Image.open(img).size),'generator':'Built-in ImageGen','pdf_sha256':hashlib.sha256(pdf.read_bytes()).hexdigest(),'png_sha256':hashlib.sha256(img.read_bytes()).hexdigest(),'export_folder':str(export),'vba_runtime_execution':False,'arithmetic_validation':'100,25,40 initially; 140,35,80 after input change and macro rerun'}
(root/'fuentes/export.json').write_text(json.dumps(manifest,indent=2))
print(export)
