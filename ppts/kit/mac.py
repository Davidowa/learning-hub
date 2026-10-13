"""Generate reproducible Excel for Mac lessons, then use the normal kit checks.

From ppts: python -m kit.mac && python -m kit.preflight mac
The original lessons remain the source of subject matter and assessment.
"""
from pathlib import Path
from copy import deepcopy
import argparse
import yaml

class LessonDumper(yaml.SafeDumper):
    pass

def represent_text(dumper, value):
    return dumper.represent_scalar('tag:yaml.org,2002:str', value, style='|' if '\n' in value else None)

LessonDumper.add_representer(str, represent_text)

COURSES=('office/manejo-y-analisis-de-la-informacion','vba/analisis-y-procesamiento-de-la-informacion')
CAPTIONS={
'format-cells-dialog':('Format Cells on the Number tab. Categories appear on the left.','Format Cells en Number. Las categorías aparecen a la izquierda.'),
'format-cells-font':('Font controls the font, style, size and effects.','Font controla fuente, estilo, tamaño y efectos.'),
'format-cells-fill':('Fill provides background and pattern controls.','Fill contiene controles de fondo y patrón.'),
'data-validation-dialog':('Settings, Input Message and Error Alert appear across the top.','Settings, Input Message y Error Alert aparecen arriba.'),
'subtotal-dialog':('Region defines the groups. Sum is the function. Revenue receives the subtotal.','Region define los grupos. Sum es la función. Revenue recibe el subtotal.'),
'advanced-filter':('Choose in-place filtering or copying to another location.','Elige filtrar en el mismo lugar o copiar a otra ubicación.'),
'new-formatting-rule':('Style determines the settings. This capture shows a color scale.','Style determina las opciones. Esta captura muestra una escala de color.'),
'cf-rules-manager':('Manage Rules lists rules, order and ranges. The plus button adds a rule.','Manage Rules muestra reglas, orden y rangos. El botón de suma agrega una regla.'),
'page-setup-dialog':('Page Setup has four tabs: Page, Margins, Header/Footer and Sheet.','Page Setup tiene cuatro pestañas: Page, Margins, Header/Footer y Sheet.'),
'goal-seek-dialog':('Goal Seek asks for the formula cell, target value and changing cell.','Goal Seek pide la celda con fórmula, el valor objetivo y la celda que cambia.'),
'scenario-manager':('The plus button creates the first scenario.','El botón de suma crea el primer escenario.'),
'excel-developer-tab':('Developer includes Visual Basic, Macros and Record Macro.','Developer incluye Visual Basic, Macros y Record Macro.'),
'record-macro-dialog':('Record Macro asks for name, storage, shortcut and description.','Record Macro pide nombre, ubicación, atajo y descripción.'),
'macro-dialog':('The Macro dialog includes the macro list and Step, Edit and Run buttons.','Macro contiene la lista de macros y los botones Step, Edit y Run.'),
'vbe-editor':('Project Explorer, Properties and Module1 are visible. FormatHeader formats header cells.','Se ven Project Explorer, Properties y Module1. FormatHeader da formato al encabezado.')}

FIGURE_TITLES={
'format-cells-dialog':('The Number tab and its categories','Number y sus categorías'),
'format-cells-font':('Six tabs in Format Cells','Seis pestañas en Format Cells'),
'format-cells-fill':('Background and pattern controls','Controles de fondo y patrón'),
'data-validation-dialog':('Three tabs in Data Validation','Tres pestañas en Data Validation'),
'subtotal-dialog':('Grouping and subtotal settings','Opciones de agrupación y subtotal'),
'advanced-filter':('Three ranges and two destinations','Tres rangos y dos destinos'),
'new-formatting-rule':('Style and color scale settings','Style y opciones de escala de color'),
'cf-rules-manager':('Rules, formats and ranges','Reglas, formatos y rangos'),
'page-setup-dialog':('Four tabs in Page Setup','Cuatro pestañas en Page Setup'),
'goal-seek-dialog':('Three fields in Goal Seek','Tres campos en Goal Seek'),
'scenario-manager':('Scenario Manager before adding a scenario','Scenario Manager antes de agregar un escenario'),
'excel-developer-tab':('The Developer ribbon on Mac','La cinta Developer en Mac'),
'record-macro-dialog':('Naming and storing a recorded macro','Nombre y ubicación de una macro grabada'),
'macro-dialog':('The Macro dialog on Mac','El cuadro Macro en Mac'),
'vbe-editor':('The VBA editor for Mac','El editor VBA para Mac')}


def concept(title,lead,es,steps):
    return {'concept':{'eyebrow':'Excel para Mac' if es else 'Excel for Mac','title':title,'lead':lead,
       'panel':{'label':'Ruta' if es else 'Route','title':steps[0],'note':'Usa los nombres visibles del producto.' if es else 'Follow the labels visible in the application.'},
       'steps':[{'text':s} for s in steps]}}


def adapt_text(node):
    if isinstance(node,list):return [adapt_text(x) for x in node]
    if isinstance(node,dict):return {k:adapt_text(v) if k not in ('output',) or not isinstance(v,str) else v for k,v in node.items()}
    if not isinstance(node,str):return node
    for a,b in {'Alt + F11':'Option + F11','Alt+F11':'Option+F11','Alt + F8':'Option + F8','Alt+F8':'Option+F8',
       'Alt and F8':'Option and F8','Alt y F8':'Option y F8','Alt+Enter':'Control+Option+Return',
       'Ctrl+Alt+V':'Command+Control+V','Ctrl + Alt + V':'Command + Control + V',
       'Ctrl+F3':'Insert, Name, Name Manager','Ctrl+E':'Edit, Fill, Flash Fill',
       'Ctrl + Break':'Run, Break', 'Ctrl+Break':'Run, Break',
       'Ctrl+1':'Command+1','Ctrl+Z':'Command+Z','Ctrl+Y':'Command+Y','Ctrl+A':'Command+A',
       'Ctrl+K':'Command+K','Ctrl+X':'Command+X','Ctrl+T':'Command+T','Ctrl+L':'Command+T',
       'Ctrl+P':'Command+P','Ctrl+F':'Command+F','Ctrl+click':'Command+click','Ctrl+clic':'Command+clic',
       'Alt+=':'Formulas, AutoSum','Alt+F1':'Insert, Recommended Charts',
       'File, Options':'Excel, Preferences','Archivo, Opciones de Excel':'Excel, Preferences',
       'Archivo, Opciones':'Excel, Preferences','File, Info':'File, Properties','Archivo, Información':'File, Properties',
       'Options, then Formulas':'Excel Preferences, Calculation','Read-only set in Windows':'Read-only file permissions','Solo lectura en Windows':'Permisos de solo lectura','Opciones, luego Fórmulas':'Excel Preferences, Calculation'}.items():node=node.replace(a,b)
    # Chr uses the host character set; Unicode 160 is NBSP on both platforms.
    node = node.replace('Chr(160)', 'WorksheetFunction.Unichar(160)')
    if '\n' in node:
        lines = []
        for line in node.splitlines():
            for variable in ('celda', 'cell'):
                marker = f'Replace({variable}.Value, WorksheetFunction.Unichar(160), " "))'
                if marker in line:
                    indent = line[:len(line) - len(line.lstrip())]
                    line = line.replace(marker, f'Replace({variable}.Value, _\n{indent}WorksheetFunction.Unichar(160), " "))')
            lines.append(line)
        node = '\n'.join(lines) + ('\n' if node.endswith('\n') else '')
    return node


def worksheet_form(es):
    return concept('Formulario en una hoja' if es else 'A worksheet input form',
       'Usa celdas con nombre para los campos y un botón de formulario para ejecutar la macro. Valida cada entrada antes de guardar.' if es else
       'Use named worksheet cells for the fields and a Form Control button to run the macro. Validate every input before saving.',es,
       ['Insert, Name, Define Name','Developer, Button','ValidateLoan'])


def generate(out=Path('mac')):
    made=[]
    for course in COURSES:
      for lang in ('en','es'):
        es=lang=='es';vba=course.startswith('vba/')
        for p in sorted(Path(course,lang).glob('*.yaml')):
          d=adapt_text(deepcopy(yaml.safe_load(p.read_text())))
          d['meta']['platform']='macOS';d['meta']['footer']+=' · macOS'
          intro=concept('Esta edición en macOS' if es else 'This edition on macOS',
             'Las capturas muestran Excel para Mac 16.112.3 con interfaz en inglés. Las fórmulas conservan el idioma de la clase. Las teclas F pueden requerir Fn.' if es else
             'The captures show Excel for Mac 16.112.3 with an English interface. Formulas retain the course language. Function keys may require Fn.',es,
             ['Excel for Mac 16.112.3','Command+1','Option+F11' if vba else 'File, Page Setup'])
          intro['concept']['notes']='https://support.microsoft.com/en-us/accessibility/excel/keyboard-shortcuts-in-excel'
          d['slides'].insert(1,intro)
          if vba and p.name.startswith('w05.'):
            start=next(i for i,s in enumerate(d['slides']) if 'divider' in s and s['divider'].get('block')==3)
            stop=next(i for i in range(start,len(d['slides'])) if 'quiz' in d['slides'][i])
            code={'code':{'eyebrow':'VBA','title':'Validación del importe' if es else 'Validating the amount','filename':'ValidateLoan.bas','lang':'vba',
              'source':'Sub ValidateLoan()\n    Dim amount As Variant\n    amount = Range("LoanAmount").Value\n    If Not IsNumeric(amount) Then\n        MsgBox "Enter a numeric amount."\n        Exit Sub\n    End If\n    If CDbl(amount) <= 0 Then\n        MsgBox "Enter a positive amount."\n        Exit Sub\n    End If\n    MsgBox "Amount accepted."\nEnd Sub\n',
              'annotations':[{'label':'IsNumeric','text':'Comprueba antes de convertir.' if es else 'Check before converting.'},
                {'label':'Exit Sub','text':'Detiene la validación si falla.' if es else 'Stop validation on failure.'}]}}
            d['slides'][start:stop]=[{'divider':{'eyebrow':'Bloque 03' if es else 'Block 03','title':'Formulario en hoja' if es else 'Worksheet input form','lede':'Campos visibles y validación en VBA.' if es else 'Visible fields and VBA validation.','block':3}},worksheet_form(es),code]
          adjusted=[]
          for slide in d['slides']:
            layout,k=next(iter(slide.items()));text=str(k)
            if not vba and p.name.startswith('w17.') and layout=='steps' and any(x in text for x in ('PDF/XPS','Publish as PDF','Publicar como PDF')):
              slide=concept('Guardar el libro como PDF' if es else 'Save the workbook as PDF',
                'Abre File, Save As, elige PDF y Workbook para incluir todas las hojas. Abre el PDF y comprueba las páginas antes de entregar.' if es else
                'Open File, Save As, select PDF and Workbook to include every sheet. Open the PDF and check its pages before submission.',es,['File, Save As','File Format, PDF','Workbook'])
            elif not vba and p.name.startswith('w17.') and layout=='quiz':
              k['question']='El PDF contiene una sola hoja. ¿Qué ajuste permite incluir todas?' if es else 'The PDF contains one sheet. Which setting includes them all?'
              k['options']=['Workbook al guardar como PDF','Zoom de 85 %','Color del encabezado','Nombre del archivo'] if es else ['Workbook when saving as PDF','85 percent zoom','Header color','File name']
              k['notes']='Respuesta: A. Workbook incluye todas las hojas; verifica el PDF final.' if es else 'Answer: A. Workbook includes all sheets; inspect the final PDF.'
            elif not vba and p.name.startswith('w17.') and layout=='agenda':
              for item in k.get('cards',[]):
                if 'PDF/XPS' in str(item):item['sub']='File, Save As, PDF, Workbook'
            elif vba and p.name.startswith('w05.') and layout=='takeaways':
              k['items'][0]={'title':'Valida antes de convertir' if es else 'Validate before converting','desc':'Las celdas pueden contener números, texto o errores. Revisa el tipo antes de usar CDbl.' if es else 'Cells can contain numbers, text or errors. Check the type before calling CDbl.'}
            if not vba and p.name.startswith('w05.') and layout=='table' and 'Link to' in text:
              k['rows']=[['Web','Address','URL'],['Este libro' if es else 'This workbook','This Document','Celda o nombre' if es else 'Cell or name'],['Correo' if es else 'Email','Email Address','Dirección y asunto' if es else 'Address and subject']]
              k['headers']=['Destino','Control','Entrada'] if es else ['Destination','Control','Input']
              k['notes']='Insert, Link. Verifica destino y texto al insertar.' if es else 'Insert, Link. Verify the destination and displayed text when inserting.'
            if not vba and p.name.startswith('w17.') and layout=='table' and any(x in text for x in ('Copies','Copias')):
              k['title']='Imprimir en Mac' if es else 'Printing on Mac'
              k['headers']=['Ajuste','Ruta','Comprobación'] if es else ['Setting','Route','Check']
              k['rows']=[['Copias' if es else 'Copies','File, Print','Cantidad' if es else 'Count'],['Hojas' if es else 'Sheets','Show Details','Workbook'],['Página' if es else 'Page','File, Page Setup','Orientación y márgenes' if es else 'Orientation and margins'],['PDF','PDF, Save as PDF','Abre el archivo' if es else 'Open the file']]
            if layout=='figure':
              name=Path(k['image']).stem
              if name not in CAPTIONS or not Path('img/en/mac',name+'.png').is_file():raise ValueError(f'{p}: missing Mac image {name}')
              k['image']='img/en/mac/'+name+'.png';k['caption']=CAPTIONS[name][1 if es else 0]+(' Interfaz en inglés.' if es else '')
              k['alt']=CAPTIONS[name][1 if es else 0]
              k['title']=FIGURE_TITLES[name][1 if es else 0]
              k.pop('side',None)
              if name=='vbe-editor':k['title']='El editor VBA para Mac' if es else 'The VBA editor for Mac'
              if name=='macro-dialog':k['title']='Macros en Excel para Mac' if es else 'Macros in Excel for Mac'
            elif layout not in ('cover','code','code_output','quiz'):
              if layout in ('steps','concept','pitfalls','table','method','tiers','compare') and any(x in text for x in ('Document Inspector','Inspector de documento','Inspect Document','Inspeccionar documento','UnsavedFiles','Unsaved Files')):
                slide=concept('Revisión del libro en Mac' if es else 'Workbook review on Mac',
                  'Revisa propiedades, comentarios y hojas ocultas antes de entregar. Document Inspector corresponde a Windows y no se exige en la práctica de Mac.' if es else
                  'Review properties, comments and hidden sheets before submission. Document Inspector is a Windows feature and is not required in the Mac lab.',es,['File, Properties','Review, Show Comments','Format, Sheet, Unhide'])
              elif layout in ('steps','concept','pitfalls','table','method','tiers','compare') and any(x in text for x in ('Trust Center','Centro de confianza','SECURITY WARNING','Enable Content','Habilitar contenido','Macro Security')):
                slide=concept('Seguridad de macros en Mac' if es else 'Macro security on Mac',
                  'Conserva las advertencias de macros. Habilita código solo en archivos cuyo origen y contenido hayas revisado. Guarda las macros en .xlsm.' if es else
                  'Keep macro warnings enabled. Allow code only in files whose source and contents you have reviewed. Save macros in .xlsm.',es,['Excel, Preferences, Security','Revisa el código' if es else 'Review the code','Guarda como .xlsm' if es else 'Save as .xlsm'])
              elif layout=='steps' and any(x in text for x in ('Customize Ribbon','Personalizar cinta','Personalizar la cinta')):
                for item in k['items']:
                  if any(x in str(item) for x in ('Developer','Programador','Desarrollador')):item['desc']='Excel, Preferences, Ribbon & Toolbar. Activa Developer.' if es else 'Excel, Preferences, Ribbon & Toolbar. Enable Developer.'
              elif layout=='steps' and 'From Text (Legacy)' in text:
                for item in k['items'][:2]:item['desc']='Si aparece From Text (Legacy), úsalo desde Data, Get Data. Si no, importa con From Text/CSV y verifica delimitador y codificación.' if es else 'If From Text (Legacy) is available, use it from Data, Get Data. Otherwise use From Text/CSV and check delimiter and encoding.'
              if vba and p.name.startswith('w05.') and layout in ('lab','homework'):
                k['brief']='Crea un formulario en una hoja con número de empleado, días trabajados, sueldo diario y porcentaje de bono. Una macro debe validar los campos y guardar sus valores en celdas con nombre.' if es else 'Build a worksheet input form with employee number, days worked, daily wage and bonus percentage. A macro must validate the fields and save values in named cells.'
                if layout=='homework':
                  k['meta']=[[a,b.replace('.frm','.bas')] for a,b in k.get('meta',[])]
                if layout=='lab':k['blocks']=[{'label':'Entrega' if es else 'Submission','text':'.xlsm y módulo exportado' if es else '.xlsm and exported module'}, {'label':'Restricción' if es else 'Constraint','text':'Cada campo tiene un nombre definido.' if es else 'Each field has a defined name.'},{'label':'Prueba' if es else 'Test','text':'Rechaza entradas vacías y no numéricas.' if es else 'Reject empty and nonnumeric inputs.'}]
            if layout in ('agenda','objectives','lab','homework','takeaways'):
              def platform_labels(n):
                if isinstance(n,list): return [platform_labels(v) for v in n]
                if isinstance(n,dict): return {key:platform_labels(val) for key,val in n.items()}
                if isinstance(n,str):
                  for a,b in {'Document Inspector':'workbook properties','Inspector de documento':'propiedades del libro','File, Info':'File, Properties','Archivo, Información':'File, Properties','Trust Center':'Security preferences','Centro de confianza':'Security preferences'}.items(): n=n.replace(a,b)
                return n
              slide={layout:platform_labels(k)}
            if vba and p.name.startswith('w13.') and 'WorksheetFunction.Unichar(160)' in str(slide):
              if layout == 'code_output':
                k['output_label'] = 'Con un espacio duro' if es else 'With a hard space'
              k['notes'] = str(k.get('notes', '')) + ('\nEn Excel para Mac 16.112.3, AscW(Chr(160)) dio 8224. Unichar(160) dio 160 y corrigió la limpieza de nombres. Usa Unicode para este espacio duro.' if es else '\nIn Excel for Mac 16.112.3, AscW(Chr(160)) returned 8224. Unichar(160) returned 160 and corrected the name cleaner. Use Unicode for this hard space.')
            current=next(iter(slide.values()));current['notes']=str(current.get('notes',''))+('\nEdición Mac. Interfaz capturada en inglés.' if es else '\nMac edition. Captured interface is English.')
            # Expanded Command labels must still fit the existing table geometry.
            if layout=='table' and not es:
              for row in current.get('rows',[]):
                for i,value in enumerate(row):
                  if isinstance(value,str):row[i]=value.replace('Command+1 over the range','Format Cells').replace('Command+1 over the same cells','Format Cells').replace('Command+1, Number tab, Custom','Format Cells, Custom')
            adjusted.append(slide)
          d['slides']=adjusted;dest=out/course/lang/p.name;dest.parent.mkdir(parents=True,exist_ok=True)
          dest.write_text(yaml.dump(d,Dumper=LessonDumper,sort_keys=False,allow_unicode=True,width=1000));made.append(dest)
    return made


def main():
    a=argparse.ArgumentParser(description=__doc__);a.add_argument('--out',type=Path,default=Path('mac'));args=a.parse_args()
    print(f'{len(generate(args.out))} Mac lessons generated in {args.out}')

if __name__=='__main__':main()
