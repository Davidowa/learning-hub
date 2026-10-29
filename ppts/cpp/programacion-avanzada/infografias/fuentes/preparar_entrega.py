"""Package approved ImageGen artwork as letter PDF pages without changing pixels."""
from pathlib import Path
import csv,json,shutil,hashlib
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from pypdf import PdfReader,PdfWriter

ROOT=Path(__file__).resolve().parents[1]
items=json.loads((ROOT/'fuentes/contenido.json').read_text())
selected={x['n']:x for x in json.loads((ROOT/'fuentes/imagenes-seleccionadas.json').read_text())}
P3=ROOT/'P3';P3.mkdir(exist_ok=True)
combined=PdfWriter();manifest=[]
for item in items:
    n=item['n'];slug=item['slug'];stem=f'{n:02d}-{slug}'
    filename=item['filename']
    if n==4: filename='P3 - 04 - CPP - Modificadores de acceso'
    png=ROOT/'es'/f'{stem}.png'
    source=Path(selected[n]['path'])
    if source.exists():shutil.copy2(source,png)
    if not png.exists():raise FileNotFoundError(png)
    named_png=P3/(filename+'.png');shutil.copy2(png,named_png)
    pdf=P3/(filename+'.pdf')
    c=canvas.Canvas(str(pdf),pagesize=letter,pageCompression=1)
    c.setTitle(item['topic']+' · Learning Hub · C++20 · P3')
    c.setAuthor('David Escobar-Castillejos')
    c.setSubject(item['title'])
    c.drawImage(str(png),0,0,width=letter[0],height=letter[1],preserveAspectRatio=True,anchor='c')
    c.showPage();c.save()
    r=PdfReader(pdf);assert len(r.pages)==1
    assert [float(x) for x in r.pages[0].mediabox]==[0.,0.,612.,792.]
    combined.add_page(r.pages[0]);combined.add_outline_item(f'{n:02d} · '+item['topic'],n-1)
    shutil.copy2(pdf,ROOT/'es'/f'{stem}.pdf')
    manifest.append({'numero':n,'tema':item['topic'],'original':item['original'],'png':named_png.name,'pdf':pdf.name,'sha256_png':hashlib.sha256(named_png.read_bytes()).hexdigest(),'sha256_pdf':hashlib.sha256(pdf.read_bytes()).hexdigest()})
combined.add_metadata({'/Title':'Learning Hub · C++20 · Infografías P3','/Author':'David Escobar-Castillejos','/Subject':'Ocho infografías de clases, acceso, inicialización, herencia y polimorfismo'})
with (P3/'P3 - CPP - Infografías completas - Carta.pdf').open('wb') as f:combined.write(f)
assert len(PdfReader(P3/'P3 - CPP - Infografías completas - Carta.pdf').pages)==8
(ROOT/'fuentes/manifiesto.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2))
with (P3/'Nombres para Blackboard.csv').open('w',newline='',encoding='utf-8-sig') as f:
    writer=csv.writer(f);writer.writerow(['Orden','Tema','Nombre para mostrar','Archivo PDF','Archivo PNG'])
    for row in manifest:writer.writerow([row['numero'],row['tema'],row['pdf'][:-4],row['pdf'],row['png']])
print('8 PDF individuales carta + 8 PNG + 1 PDF con 8 páginas. Todos los PDF tienen MediaBox 612 × 792 pt.')
