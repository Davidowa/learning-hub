import os
os.environ['QT_QPA_PLATFORM']='offscreen'
from pathlib import Path
import yaml,json,tempfile,contextlib,io,csv
from PyQt6.QtWidgets import QApplication,QMainWindow,QWidget,QLineEdit,QVBoxLayout
root=Path.cwd();app=QApplication([]);results=[]
with tempfile.TemporaryDirectory() as tmp:
 os.chdir(tmp)
 for p in (root/'ppts/python').glob('*/*/*.yaml'):
  for s in yaml.safe_load(p.read_text())['slides']:
   if 'code' not in s:continue
   b=s['code'];name=b.get('filename');ns={'productos':['X1','X2'],'products':['X1','X2'],'por_region':{'North':10,'South':20},'by_region':{'North':10,'South':20},'QWidget':QWidget,'QLineEdit':QLineEdit,'QVBoxLayout':QVBoxLayout};ns['self']=QMainWindow()
   if name not in ['medir.py','timing.py','formulario.py','form.py']:continue
   try:
    with contextlib.redirect_stdout(io.StringIO()):exec(b['source'],ns)
    if name in ['guardar.py','saving.py']:
     with open('resumen.csv' if name=='guardar.py' else 'summary.csv') as f:assert list(csv.reader(f))==[['region','amount'],['North','10'],['South','20']]
    elif name in ['medir.py','timing.py']:assert ns.get('segundos',ns.get('seconds'))>=0
    else:
     li=ns['self'].lista if name=='formulario.py' else ns['self'].list;assert li.count()==1
    results.append({'file':str(p.relative_to(root)),'fragment':name,'status':'pass'})
   except Exception as ex:results.append({'file':str(p.relative_to(root)),'fragment':name,'status':'fail','error':repr(ex)})
 os.chdir(root)
Path('/tmp/pyu-new-test-results.json').write_text(json.dumps(results,ensure_ascii=False,indent=2));print(len(results),sum(x['status']=='fail' for x in results));assert all(x['status']=='pass' for x in results)
