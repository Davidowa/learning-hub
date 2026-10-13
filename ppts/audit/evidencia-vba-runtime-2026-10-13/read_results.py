"""Read native Excel's saved results without recalculating or rewriting the workbook."""
from pathlib import Path
import argparse,json,zipfile,xml.etree.ElementTree as E,collections
ap=argparse.ArgumentParser();ap.add_argument('workbook',type=Path);ap.add_argument('--sheet',default='VBAResultsV2');ap.add_argument('--out',type=Path,required=True);a=ap.parse_args();ns={'m':'http://schemas.openxmlformats.org/spreadsheetml/2006/main','r':'http://schemas.openxmlformats.org/officeDocument/2006/relationships'}
with zipfile.ZipFile(a.workbook)as z:
 strings=[''.join(x.itertext()) for x in E.fromstring(z.read('xl/sharedStrings.xml')).findall('m:si',ns)]
 sheets=E.fromstring(z.read('xl/workbook.xml')).findall('m:sheets/m:sheet',ns);rels={x.attrib['Id']:x.attrib['Target']for x in E.fromstring(z.read('xl/_rels/workbook.xml.rels'))}
 sh=next(s for s in sheets if s.attrib['name']==a.sheet);target=rels[sh.attrib['{'+ns['r']+'}id']];rows=[]
 for r in E.fromstring(z.read('xl/'+target)).findall('m:sheetData/m:row',ns):
  n=r.attrib['r'];cells={}
  for c in r.findall('m:c',ns):
   v=c.find('m:v',ns);val=v.text if v is not None else''
   if c.attrib.get('t')=='s':val=strings[int(val)]
   if c.attrib.get('t')=='b':val='True'if val=='1'else'False'
   cells[c.attrib['r']]=val
  if cells.get('C'+n)in['PASS','FAIL']:rows.append({'id':cells.get('A'+n),'week':cells.get('B'+n),'status':cells.get('C'+n),'actual':cells.get('D'+n),'expected':cells.get('E'+n)})
 result={'workbook':str(a.workbook),'sheet':a.sheet,'native_vba_project':'xl/vbaProject.bin'in z.namelist(),'counts':dict(collections.Counter(r['status']for r in rows)),'results':rows}
 a.out.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n');print(result['counts']);print(json.dumps([r for r in rows if r['status']=='FAIL'],ensure_ascii=False,indent=2))
