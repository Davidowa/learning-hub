"""Compile positive examples and verify seven language-rule diagnostics."""
from pathlib import Path
import json,re,subprocess,tempfile
ROOT=Path(__file__).resolve().parents[1]
FLAGS=['clang++','-std=c++20','-Wall','-Wextra','-pedantic','-Werror']
negatives={
 'private':('class A { int dato{}; }; int main(){ A a; return a.dato; }',r'private'),
 'protected-base-reference':('struct A { protected: int dato{}; }; struct B:A { int leer(A& a){return a.dato;} };',r'protected'),
 'override-const':('struct A { virtual double area() const=0; }; struct B:A { double area() override{return 0;} };',r'override|overrid'),
 'const-in-body':('struct A { const int id; A(){id=1;} };',r'const|initializ'),
 'reference-in-body':('struct A { int& ref; A(int& r){ref=r;} };',r'initializ|reference'),
 'abstract-instantiation':('struct A { virtual double area() const=0; }; int main(){A a;}',r'abstract'),
 'ambiguous-diamond':('struct A{}; struct B:A{}; struct C:A{}; struct D:B,C{}; A* base(D* d){return d;}',r'ambiguous'),
}
results=[]
with tempfile.TemporaryDirectory(prefix='learninghub-cpp-') as folder:
 tmp=Path(folder)
 for file in sorted((ROOT/'ejemplos').glob('*.cpp')):
  binary=tmp/file.stem
  compiled=subprocess.run(FLAGS+[str(file),'-o',str(binary)],capture_output=True,text=True)
  if compiled.returncode:raise RuntimeError(file.name+'\n'+compiled.stderr)
  run=subprocess.run([str(binary)],capture_output=True,text=True)
  if run.returncode:raise RuntimeError(file.name+'\n'+run.stderr)
  if file.name.startswith('07'):assert run.stdout=='78.54\n'
  if file.name.startswith('08'):assert run.stdout=='78.54\n24.00\n9.00\n'
  results.append(dict(file=file.name,compiled=True,assertions_passed=True,stdout=run.stdout))
  print('PASS',file.name)
 for name,(source,reason) in negatives.items():
  file=tmp/(name+'.cpp');file.write_text(source)
  run=subprocess.run(FLAGS+['-fsyntax-only',str(file)],capture_output=True,text=True)
  assert run.returncode!=0 and re.search(reason,run.stderr,re.I),(name,run.stderr)
  results.append(dict(case=name,rejected_as_expected=True,diagnostic=reason))
  print('PASS expected rejection:',name)
version=subprocess.run(['clang++','--version'],capture_output=True,text=True,check=True).stdout.splitlines()[0]
(ROOT/'fuentes/validacion-cpp.json').write_text(json.dumps(dict(compiler=version,standard='C++20',positive_examples=8,negative_cases=7,results=results),ensure_ascii=False,indent=2))
print('PASS: 8 complete examples; 7 expected compile failures.')
