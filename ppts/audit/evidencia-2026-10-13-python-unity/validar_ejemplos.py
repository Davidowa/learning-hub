import os
os.environ['QT_QPA_PLATFORM']='offscreen';os.environ['MPLBACKEND']='Agg'
import yaml,pathlib,tempfile,contextlib,io,json,sqlite3,sys
import pandas as pd,seaborn as sns,matplotlib.pyplot as plt
from PyQt6.QtWidgets import *
root=pathlib.Path.cwd();app=QApplication([]);checks=[]
def run(name,func):
 try:func();checks.append({'check':name,'status':'pass'})
 except Exception as ex:checks.append({'check':name,'status':'fail','error':repr(ex)})
def cow():
 x=pd.DataFrame({'region':['North','South'],'channel':['Online','Online']});before=x.copy();x[x.region=='North']['channel']='Retail';assert x.equals(before);x.loc[x.region=='North','channel']='Retail';assert x.iloc[0].channel=='Retail'
run('pandas3 chained assignment leaves source unchanged, loc updates source',cow)
def shared_cart():
 for l in ['es','en']:
  p=root/f'ppts/python/programacion-orientada-a-objetos/{l}/w03.{l}.yaml';b=yaml.safe_load(p.read_text())['slides'][15]['quiz'];ns={};out=io.StringIO()
  with contextlib.redirect_stdout(out):exec(b['source'],ns)
  assert out.getvalue()=='1\n'
run('POOw03 quiz shared class list both languages',shared_cart)
def counter():
 for l in ['es','en']:
  b=next(s['quiz'] for s in yaml.safe_load((root/f'ppts/python/programacion-orientada-a-objetos/{l}/w04.{l}.yaml').read_text())['slides'] if 'quiz' in s);out=io.StringIO()
  with contextlib.redirect_stdout(out):exec(b['source'],{})
  assert out.getvalue()=='0\n'
run('POOw04 quiz instance shadows class count both languages',counter)
def qt_signals():
 for l in ['es','en']:
  ss=yaml.safe_load((root/f'ppts/python/programacion-orientada-a-objetos/{l}/w14.{l}.yaml').read_text())['slides'];ns={'QMainWindow':QMainWindow,'QPushButton':QPushButton,'QLineEdit':QLineEdit};exec(ss[12]['code']['source'],ns);W=ns['VentanaPrincipal' if l=='es' else 'MainWindow'];w=W();entry=w.caja if l=='es' else w.box;button=w.boton if l=='es' else w.button;out=io.StringIO()
  with contextlib.redirect_stdout(out):
   for text in ['Ana','Luis']:entry.setText(text);button.click()
  assert out.getvalue()==ss[13]['code_output']['output'];w.close()
run('POOw14 real offscreen Qt setText and button clicks produce both displayed output lines',qt_signals)
def qt_quiz():
 for l in ['es','en']:
  ss=yaml.safe_load((root/f'ppts/python/programacion-orientada-a-objetos/{l}/w14.{l}.yaml').read_text())['slides'];b=next(s['quiz'] for s in ss if 'quiz'in s);ns={'QMainWindow':QMainWindow,'QPushButton':QPushButton};exec(b['source'],ns);out=io.StringIO()
  try:
   with contextlib.redirect_stdout(out):ns['Ventana' if l=='es' else 'Window']()
  except TypeError:pass
  else:raise AssertionError('expectedTypeError connect(None)')
  assert out.getvalue()=='clic\n' if l=='es' else out.getvalue()=='click\n'
run('POOw14 quiz calls method at construction then connectNone raises TypeError',qt_quiz)
def sqlite_test():
 for l in ['es','en']:
  tmp=tempfile.mkdtemp();os.chdir(tmp);pathlib.Path('datos' if l=='es' else 'data').mkdir();ss=yaml.safe_load((root/f'ppts/python/programacion-orientada-a-objetos/{l}/w16.{l}.yaml').read_text())['slides'];tab='Peliculas' if l=='es' else 'Movies';col='titulo' if l=='es' else 'title';path=pathlib.Path('datos' if l=='es' else 'data')/'pixar.db';db=sqlite3.connect(path);db.execute(f'CREATE TABLE {tab}(id INTEGER PRIMARY KEY,{col} TEXT NOT NULL)');db.executemany(f'INSERT INTO {tab} VALUES(?,?)',[(1,'Toy Story'),(2,'Up')]);db.commit();db.close();ns={};exec(ss[9]['code']['source'],ns);out=io.StringIO()
  with contextlib.redirect_stdout(out):exec(ss[10]['code_output']['source'],ns)
  assert out.getvalue()==ss[10]['code_output']['output'];db=sqlite3.connect(path);db.execute(f'DELETE FROM {tab}');db.commit();db.close();out=io.StringIO()
  with contextlib.redirect_stdout(out):exec(next(s['quiz']['source'] for s in ss if 'quiz'in s),ns)
  assert out.getvalue()=='(1,)\n';os.chdir(root)
run('POOw16 seeded query output and empty-table quiz commit both languages',sqlite_test)
def demo_new():
 for l in ['es','en']:
  p=root/f'ppts/python/programacion-orientada-a-objetos/{l}/w15.{l}.yaml';ss=yaml.safe_load(p.read_text())['slides'];b=next(s['code'] for s in ss if 'code'in s and s['code']['filename'] in ['formulario.py','form.py']);w=QMainWindow();ns={'self':w,'QWidget':QWidget,'QLineEdit':QLineEdit,'QVBoxLayout':QVBoxLayout};exec(b['source'],ns);li=w.lista if l=='es' else w.list;assert li.count()==1 and li.item(0).text()=='Ana';w.close()
run('POOw15 new QFormLayout and QListWidget fragment real offscreenQt',demo_new)
json.dump(checks,open('/tmp/pyu-target-results.json','w'),ensure_ascii=False,indent=2);print(json.dumps(checks,ensure_ascii=False,indent=2));assert all(x['status']=='pass' for x in checks)
