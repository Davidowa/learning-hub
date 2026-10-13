"""Author the initial course lessons with the established kit layouts."""
from pathlib import Path
import json,re,textwrap
import yaml

ROOT=Path(__file__).resolve().parents[1]
class LessonDumper(yaml.SafeDumper):pass
LessonDumper.add_representer(str,lambda d,v:d.represent_scalar('tag:yaml.org,2002:str',v,style='|' if '\n' in v else None))

def short(value,limit=105):
    value=re.sub(r'`([^`]+)`',r'\1',value).strip()
    if len(value)<=limit:return value
    for sep in ('. ',': ','; ',':',', '):
      head=value.split(sep,1)[0]
      if 15<len(head)<=limit:return head
    return value[:limit].rsplit(' ',1)[0]

def dump(path,doc):
    path.parent.mkdir(parents=True,exist_ok=True);path.write_text(yaml.dump(doc,Dumper=LessonDumper,sort_keys=False,allow_unicode=True,width=1000))

def cover(course,lang,n,topic,subtitle,code):
    es=lang=='es'
    return {'cover':{'kicker':'Universidad Panamericana · 2026',
      'unit':('Encuadre' if n==0 and es else 'Course framing' if n==0 else f"{'Semana' if es else 'Week'} {n:02} · {short(topic,66)}"),
      'title':course,'subtitle':subtitle,'meta':[['Profesor' if es else 'Instructor','David Escobar-Castillejos'],['Track',code],['Sesión' if es else 'Session',f'{n} de 17' if es else f'{n} of 17']]}}

def roadmap(n,lang,mobile=False):
    es=lang=='es';ranges=[(1,3),(4,7),(8,12),(13,17)] if mobile else [(1,4),(5,8),(9,13),(14,17)]
    names=['Fundamentos','Interfaz y estado','Datos y dispositivo','Calidad y entrega'] if mobile and es else ['Foundations','Interface and state','Data and device','Quality and release'] if mobile else ['Modelo y economía','Compra y pago','Operación y medición','Retención y decisión'] if es else ['Model and economics','Shopping and payment','Operations and measurement','Retention and decisions']
    return {'roadmap':{'eyebrow':'Mapa del curso' if es else 'Course map','title':'Ubicación de la sesión' if es else 'Session position',
       'phases':[{'label':f'{a:02}–{b:02}','title':title,'desc':('Concepto, caso y evidencia.' if es else 'Concept, case and evidence.'),'state':'done' if n>b else 'now' if a<=n<=b else 'todo'} for (a,b),title in zip(ranges,names)]}}

def concept(title,lead,lang,notes=''):
    es=lang=='es'
    return {'concept':{'eyebrow':'Concepto' if es else 'Concept','title':short(title,75),'lead':lead,
      'panel':{'label':'Aplicación' if es else 'Application','title':short(title,55),
               'note':'Identifica qué decisión cambia con este concepto.' if es else 'Identify which decision changes with this concept.'},
      'steps':[{'text':'Define el caso y sus restricciones' if es else 'Define the case and its constraints'},
               {'text':'Comprueba la evidencia disponible' if es else 'Check the available evidence'},
               {'text':'Explica la decisión y su límite' if es else 'Explain the decision and its limit'}],'notes':notes}}

def assessment(plan,lang):
    es=lang=='es';rows=[]
    for x in plan['assessment']:rows.append([x['name_'+lang],str(x['weight'])+' %',x['week']])
    return {'table':{'eyebrow':'Evaluación' if es else 'Assessment','title':'Cinco componentes de la calificación' if es else 'Five grading components','headers':['Componente','Peso','Entrega'] if es else ['Component','Weight','Due'],'rows':rows}}

def frame(course,code,lang,plan,mobile=False):
    es=lang=='es'
    slides=[cover(course,lang,0,'', 'Modelo, práctica, evidencia y evaluación.' if es else 'Models, practice, evidence and assessment.',code),roadmap(0,lang,mobile),assessment(plan,lang),
      concept('Proyecto del curso' if es else 'Course project','Bitácora es una app ficticia de inspección. Cada sesión incorpora una función verificable.' if es and mobile else 'Bitácora is a fictional inspection app. Each session adds a verifiable capability.' if mobile else 'Molienda es un tostador ficticio. El pedido #1001 permite relacionar catálogo, pago, operación y medición.' if es else 'Molienda is a fictional coffee roaster. Order #1001 connects catalog, payment, operations and measurement.',lang),
      {'steps':{'eyebrow':'Trabajo del curso' if es else 'Course work','title':'Evidencia de cada entrega' if es else 'Evidence for each submission','items':[
        {'label':'01','title':'Resultado' if es else 'Result','desc':'Muestra que se cumplen los criterios del caso.' if es else 'Show that the case acceptance criteria are met.'},
        {'label':'02','title':'Método' if es else 'Method','desc':'Conserva datos, supuestos y pasos reproducibles.' if es else 'Keep data, assumptions and reproducible steps.'},
        {'label':'03','title':'Explicación' if es else 'Explanation','desc':'Defiende una decisión y reconoce su límite.' if es else 'Defend a decision and identify its limit.'}]}},
      concept('Código de Honor y uso de IA' if es else 'Honor code and AI use','Declara la asistencia utilizada y cómo verificaste el resultado. Cada integrante explica el trabajo entregado. Los exámenes usan las reglas indicadas en su enunciado.' if es else 'Disclose assistance and how the result was verified. Each member explains the submitted work. Exams follow the rules specified in their instructions.',lang),
      {'quiz':{'eyebrow':'Diagnóstico' if es else 'Diagnostic','question':'¿Qué permite evaluar una entrega?' if es else 'What makes a submission assessable?','options':['Una herramienta popular' if es else 'A popular tool','Un resultado con evidencia y explicación' if es else 'A result with evidence and explanation','Una presentación sin datos' if es else 'A presentation without data','Un porcentaje sin denominador' if es else 'A percentage without a denominator'],'notes':'Respuesta B. Popularidad y formato no sustituyen evidencia.' if es else 'Answer B. Popularity and formatting do not replace evidence.'}},
      {'closing':{'title':'Inicio del curso' if es else 'Course start','subtitle':'Prepara el caso, el entorno y el registro de evidencia.' if es else 'Prepare the case, environment and evidence record.','meta':[['Instructor','David Escobar-Castillejos'],['Contacto' if es else 'Contact','descobarc@up.edu.mx']]}}]
    return {'meta':{'course':course,'code':code,'lang':lang,'language':'react-native' if mobile and code=='React Native' else 'swift' if mobile else 'commerce','week':0,'footer':course.upper()+' · '+code,'blocks':3},'slides':slides}


def closing(lang,next_topic):
    es=lang=='es';return {'closing':{'title':'Preguntas' if es else 'Questions','subtitle':('Siguiente sesión: ' if es else 'Next session: ')+next_topic,'meta':[['Contacto' if es else 'Contact','descobarc@up.edu.mx'],['Curso' if es else 'Course','learning-hub']]}}


def lab_and_homework(s,lang,case):
    es=lang=='es';lab=s['lab_'+lang];hw=s['homework_'+lang]
    return [
      {'divider':{'eyebrow':'Bloque 03' if es else 'Block 03','title':'Aplicación y evidencia' if es else 'Application and evidence','lede':'El caso termina en una decisión que puedes comprobar.' if es else 'The case ends in a decision that can be checked.','block':3}},
      {'lab':{'eyebrow':'Laboratorio' if es else 'Lab','title':case,'brief':short(lab,360),
          'blocks':[{'label':'Entrega' if es else 'Submission','text':'Resultado y registro de evidencia.' if es else 'Result and evidence record.'},
                    {'label':'Restricción' if es else 'Constraint','text':'Usa solo conceptos de esta sesión y anteriores.' if es else 'Use only this session and earlier concepts.'},
                    {'label':'Comprobación' if es else 'Check','text':'Otra persona debe poder reproducir el resultado.' if es else 'Another person must be able to reproduce the result.'}], 'notes':lab}},
      {'homework':{'eyebrow':'Tarea' if es else 'Homework','title':'Aplicación al proyecto' if es else 'Apply to the project','brief':short(hw,320),
          'meta':[['Entrega' if es else 'Due','Antes de la siguiente sesión' if es else 'Before the next session'],['Formato' if es else 'Format','Evidencia y explicación' if es else 'Evidence and explanation']],
          'rubric':[['Concepto' if es else 'Concept','40 %','Uso correcto y supuestos claros' if es else 'Correct use and clear assumptions'],['Evidencia' if es else 'Evidence','40 %','Resultado reproducible' if es else 'Reproducible result'],['Decisión' if es else 'Decision','20 %','Justificación y límite' if es else 'Rationale and limit']], 'notes':hw}}
    ]


def parsed_quiz(s,lang):
    raw=s['quiz_idea_'+lang].replace('our own traffic',"the business’s traffic");parts=re.split(r'\s([A-D])\)\s',raw)
    if len(parts)<9:raise ValueError('quiz not structured '+str(s['n']))
    question=parts[0];options=[];correct=None
    for i in range(1,9,2):
      text=parts[i+1]
      if '(correct' in text:correct=parts[i]
      text=re.sub(r'\s*\(correct[^)]*\)','',text)
      if i==7:text=re.split(r'\. (?=[A-ZÁÉÍÓÚ])',text,maxsplit=1)[0].rstrip('. ')+'.'
      options.append(text.strip())
    if correct is None:raise ValueError('missing key')
    replacements={
        1:('The channel and the control assigned to its participants','El canal y el control asignado a sus participantes'),
        14:('Disclose charges, obtain consent and enable timely cancellation','Informar cargos, obtener consentimiento y permitir cancelación'),
        17:('Contribution per order and payment method','Contribución por pedido y método de pago')}
    if s['n'] in replacements: options[1]=replacements[s['n']][1 if lang=='es' else 0]
    return {'quiz':{'eyebrow':'Comprobación' if lang=='es' else 'Quick check','question':short(question,180),'options':options,'notes':raw+'\n'+('Respuesta: ' if lang=='es' else 'Answer: ')+correct}}


def split_code(code):
    # Preserve every line. Continuation cards are explicitly labeled fragments.
    lines=code.splitlines(); chunks=[];part=[]
    for line in lines:
      if len(line)>63:raise ValueError('wide code line '+line)
      if len(part)==12:chunks.append('\n'.join(part)+'\n');part=[]
      part.append(line)
    if part:chunks.append('\n'.join(part)+'\n')
    return chunks


def main():
    # Specifications and topic definitions are versioned source, not remote content.
    ecommerce();mobile()


def ecommerce():
    plan=json.loads((ROOT/'ecommerce/fundamentos-del-comercio-electronico/teaching-plan.json').read_text())
    base=ROOT/'ecommerce/fundamentos-del-comercio-electronico'
    for lang in ('es','en'):
      es=lang=='es';course=plan['title_'+lang]
      dump(base/lang/f'w01.0.{lang}.yaml',frame(course,'Comercio digital' if es else 'Digital commerce',lang,plan))
      for s in plan['sessions']:
        n=s['n'];core=s['core'];topic=s['title_'+lang]
        slides=[cover(course,lang,n,topic,short(s['subtitle_'+lang],240),'Comercio digital' if es else 'Digital commerce'),
          {'agenda':{'eyebrow':'Agenda','title':'Recorrido de la sesión' if es else 'Session outline','cards':[{'title':c['title_'+lang],'desc':short(c['lead_'+lang],100)} for c in core]+[{'title':'Aplicación' if es else 'Application','desc':'Caso, comprobación y entrega.' if es else 'Case, check and submission.'}]}},
          {'objectives':{'eyebrow':'Objetivos' if es else 'Objectives','title':'Al terminar la sesión el alumno podrá…' if es else 'By the end of the session you will be able to…',
            'items':[{'head':('Explicar ' if es else 'Explain ')+c['title_'+lang].lower(),'sub':short(c['lead_'+lang],140)} for c in core]+[{'head':'Justificar una decisión con evidencia' if es else 'Justify a decision with evidence','sub':'Aplicar el caso y declarar sus supuestos.' if es else 'Apply the case and state its assumptions.'}]}},roadmap(n,lang),
          {'divider':{'eyebrow':'Bloque 01' if es else 'Block 01','title':'Modelo de la sesión' if es else 'Session model','lede':short(s['subtitle_'+lang],220),'block':1}}]
        for c in core:slides.append(concept(c['title_'+lang],c['lead_'+lang],lang))
        slides.append({'divider':{'eyebrow':'Bloque 02' if es else 'Block 02','title':'Caso Molienda' if es else 'The Molienda case','lede':'Datos ficticios para practicar una decisión verificable.' if es else 'Fictional data for practicing a verifiable decision.','block':2}})
        slides.extend(ecommerce_case(n,lang))
        sources={
            5:'{\n  "sku": "CAF-MED-250-GRANO",\n  "size_g": 250,\n  "grind": "whole",\n  "price": 289,\n  "currency": "MXN",\n  "taxes_included": true\n}\n',
            9:'{\n  "event_id": "evt-1001-paid",\n  "type": "order.paid",\n  "order_id": "1001",\n  "amount": 2068,\n  "currency": "MXN"\n}\n',
            12:'{\n  "utm_source": "newsletter",\n  "utm_medium": "email",\n  "utm_campaign": "coffee_october",\n  "landing_path": "/coffee"\n}\n',
            13:'{\n  "event": "purchase",\n  "transaction_id": "1001",\n  "value": 2068,\n  "currency": "MXN"\n}\n'}
        if n in sources:
            slides.append({'code':{'eyebrow':'Caso Molienda' if es else 'Molienda case','title':'Registro estructurado del caso' if es else 'Structured case record','filename':f'case-w{n:02}.json','lang':'json','source':sources[n],
              'annotations':[{'label':'Identidad' if es else 'Identity','text':'Conserva identificadores estables.' if es else 'Keep identifiers stable.'},{'label':'Contrato' if es else 'Contract','text':'Define campos, unidades y responsable.' if es else 'Define fields, units and owner.'}],
              'notes':'Synthetic teaching record. This is a generic contract, not a vendor API implementation.'}})

        slides.append(parsed_quiz(s,lang))
        slides+=lab_and_homework(s,lang,'Molienda · Pedido #1001' if es else 'Molienda · Order #1001')
        slides.append({'takeaways':{'eyebrow':'Resumen' if es else 'Summary','title':'Conceptos que debes conservar' if es else 'Concepts to retain','items':[{'title':c['title_'+lang],'desc':c['lead_'+lang]} for c in core]}})
        next_topic=plan['sessions'][n]['title_'+lang] if n<17 else ('Cierre y retroalimentación' if es else 'Closing feedback')
        if n==17:
            slides=[slide if 'homework' not in slide else {'table':{'eyebrow':'Evaluación final' if es else 'Final assessment','title':'Criterios de la defensa' if es else 'Defense criteria','headers':['Criterio','Evidencia'] if es else ['Criterion','Evidence'],'rows':[['Cálculo' if es else 'Calculation','Resultado reproducible' if es else 'Reproducible result'],['Decisión' if es else 'Decision','Justificación y límite' if es else 'Rationale and limit'],['Transferencia' if es else 'Transfer','Aplicación a un caso nuevo' if es else 'Application to an unfamiliar case']]}} for slide in slides]
        slides.append(closing(lang,next_topic))
        dump(base/lang/f"w{n:02}.{lang}.yaml",{'meta':{'course':course,'code':'E-commerce','lang':lang,'language':'commerce','week':n,'footer':plan['footer_'+lang],'blocks':3},'slides':slides})


ES_LABELS={
'Seller':'Vendedor','Direct relationship':'Relación directa','Platform access rules':'Reglas de acceso de la plataforma','Seller agreement':'Acuerdo del vendedor','Platform or seller':'Plataforma o vendedor',
'Survey interest':'Interés en encuesta','Statement':'Declaración','Clicks':'Clics','Action':'Acción','Refundable deposits':'Depósitos reembolsables','Commitment':'Compromiso',
'Net revenue':'Ingreso neto','Product cost':'Costo de producto','Payment cost':'Costo de pago','Other variable costs':'Otros costos variables','Contribution':'Contribución',
'Roasts':'Tuestes','Sizes per roast':'Tamaños por tueste','Grinds per size':'Molidos por tamaño','SKUs per roast':'SKU por tueste','Total SKUs':'SKU totales',
'Sessions':'Sesiones','Product views':'Vistas de producto','Add to cart':'Agregar al carrito','Begin checkout':'Inicio de checkout','Purchases':'Compras',
'Customer payment':'Pago del cliente','Fee rate':'Comisión porcentual','Fixed fee':'Cargo fijo','Calculated fee':'Comisión calculada','Payout before other adjustments':'Abono antes de otros ajustes',
'Primary metric':'Métrica principal','Purchase conversion':'Conversión de compra','Assignment':'Asignación','Random':'Aleatoria','Guardrail':'Métrica de control','Order contribution':'Contribución del pedido','Stopping rule':'Regla de cierre','Set before launch':'Definida antes de iniciar',
'On hand':'Existencia','Reserved':'Reservado','Safety stock':'Inventario de seguridad','Available':'Disponible','Dimensions':'Dimensiones','Actual weight':'Peso físico','Divisor supplied':'Divisor proporcionado','Dimensional weight':'Peso volumétrico','Billable before rounding':'Peso cobrable sin redondeo',
'Original payment':'Pago original','Confirmed refund':'Reembolso confirmado','Unreconciled balance':'Saldo sin conciliar','Invoice treatment':'Tratamiento fiscal','Review applicable rules':'Revisar reglas aplicables',
'Advertising spend':'Gasto publicitario','Acquired customers':'Clientes adquiridos','Attributed revenue':'Ingreso atribuido','Order record':'Registro de pedido','Event record':'Registro de evento','Repeated event':'Evento repetido','Ignore duplicate':'Ignorar duplicado','Reconciled orders':'Pedidos conciliados',
'Cohort A':'Cohorte A','Cohort B':'Cohorte B','Order delivery':'Entrega del pedido','Address':'Dirección','Delivery purpose':'Finalidad de entrega','Promotional contact':'Contacto promocional','Email':'Correo','Separate purpose':'Finalidad separada','Access control':'Control de acceso','Staff account':'Cuenta de personal','Role permissions':'Permisos por rol',
'Handling time':'Tiempo de atención','Error rate':'Proporción de errores','Decision':'Decisión','Quality guardrail':'Control de calidad','Stop and investigate':'Detener e investigar','Conversion':'Conversión','Orders':'Pedidos','Contribution per order':'Contribución por pedido','Total contribution':'Contribución total'}
ES_LABELS['Roasts']='Tuestes'

def ecommerce_case(n,lang):
    es=lang=='es';cases={
      1:([['Precio / Price','Seller','Seller'],['Datos / Data','Direct relationship','Platform access rules'],['Entrega / Delivery','Seller agreement','Platform or seller']],['Responsabilidad','Tienda propia','Marketplace'] if es else ['Responsibility','Own store','Marketplace']),
      2:([['Survey interest','200','Statement'],['Clicks','300','Action'],['Refundable deposits','25','Commitment']],['Evidencia','Cantidad','Tipo'] if es else ['Evidence','Count','Type']),
      3:([['Net revenue','1,862.48'],['Product cost','1,140.00'],['Payment cost','76.38'],['Other variable costs','148.00'],['Contribution','498.10']],['Concepto','MXN ilustrativos'] if es else ['Item','Illustrative MXN']),
      4:([['10','750','1,650'],['25','1,875','1,875'],['50','3,750','2,250']],['Pedidos','Marketplace','Tienda propia'] if es else ['Orders','Marketplace','Own store']),
      5:([['Roasts','3'],['Sizes per roast','2'],['Grinds per size','2'],['SKUs per roast','4'],['Total SKUs','12']],['Dato','Cantidad'] if es else ['Item','Count']),
      6:([['Sessions','10,000'],['Product views','4,000'],['Add to cart','600'],['Begin checkout','300'],['Purchases','150']],['Etapa','Entradas'] if es else ['Stage','Entrants']),
      7:([['Customer payment','2,068.00'],['Fee rate','3.5 %'],['Fixed fee','4.00'],['Calculated fee','76.38'],['Payout before other adjustments','1,991.62']],['Dato','Supuesto del caso'] if es else ['Item','Case assumption']),
      8:([['Primary metric','Purchase conversion'],['Assignment','Random'],['Guardrail','Order contribution'],['Stopping rule','Set before launch']],['Decisión','Especificación'] if es else ['Decision','Specification']),
      9:([['On hand','100'],['Reserved','20'],['Safety stock','10'],['Available','70']],['Inventario','Unidades'] if es else ['Inventory','Units']),
      10:([['Dimensions','40 × 30 × 20 cm'],['Actual weight','3 kg'],['Divisor supplied','5,000 cm³/kg'],['Dimensional weight','4.8 kg'],['Billable before rounding','4.8 kg']],['Dato','Valor ilustrativo'] if es else ['Item','Illustrative value']),
      11:([['Original payment','2,068.00'],['Confirmed refund','2,068.00'],['Unreconciled balance','0.00'],['Invoice treatment','Review applicable rules']],['Registro','Resultado'] if es else ['Record','Result']),
      12:([['Advertising spend','10,000'],['Acquired customers','100'],['Attributed revenue','40,000'],['CAC','100'],['ROAS','4']],['Métrica','Valor ilustrativo'] if es else ['Metric','Illustrative value']),
      13:([['Order record','1001','2,068'],['Event record','1001','2,068'],['Repeated event','1001','Ignore duplicate'],['Reconciled orders','1','2,068']],['Registro','ID','Efecto'] if es else ['Record','ID','Effect']),
      14:([['Cohort A','100','40','40 %'],['Cohort B','120','42','35 %']],['Cohorte','Clientes','Repiten','Un mes'] if es else ['Cohort','Customers','Repeat','One month']),
      15:([['Order delivery','Address','Delivery purpose'],['Promotional contact','Email','Separate purpose'],['Access control','Staff account','Role permissions']],['Proceso','Dato','Comprobación'] if es else ['Process','Data','Check']),
      16:([['Handling time','5.0','3.5'],['Error rate','2 %','6 %'],['Decision','Quality guardrail','Stop and investigate']],['Indicador','Antes','Piloto'] if es else ['Indicator','Before','Pilot']),
      17:([['Sessions','10,000','10,000'],['Conversion','1 %','2 %'],['Orders','100','200'],['Contribution per order','100','20'],['Total contribution','10,000','4,000']],['Métrica','Antes','Después'] if es else ['Metric','Before','After'])}
    rows,headers=cases[n]
    if es: rows=[[ES_LABELS.get(cell,cell) for cell in row] for row in rows]
    notes='All numbers are synthetic teaching inputs. No vendor fees or product tax classifications are asserted. '
    if n==3:notes+='The supplied tax assumptions are 0% on two bags at 289 and 16% included in a grinder at 1490. Net revenue = 578 + 1490/1.16. Payment cost = 2068*0.035+4. Other variable costs = 28+90+30. Round the final contribution to 2 decimals.'
    if n==4:notes+='Illustrative fees: marketplace 15% of a 500 order; own store 1500 fixed monthly plus 3% of each 500 order. Equality is at 25 orders. Acquisition costs are omitted from this fee-only comparison.'
    if n==6:notes+='Step losses: 60%, 85%, 50%, 50%. Overall conversion is 150/10000 = 1.5%. The largest relative leak is product view to cart.'
    if n==12:notes+='All amounts use the same net revenue basis. With a 25% contribution ratio before advertising, 40000*0.25 - 10000 = 0. This is the simple break-even model, not a lifetime-value model.'
    return [{'table':{'eyebrow':'Caso ilustrativo' if es else 'Illustrative case','title':'Datos para tomar una decisión' if es else 'Data for a decision','headers':headers,'rows':rows,'notes':notes}},
       {'method':{'eyebrow':'Comprobación' if es else 'Check','title':'La decisión necesita una base explícita' if es else 'The decision needs an explicit basis',
        'statement':'Declara unidad, periodo y supuestos antes de comparar resultados.' if es else 'State the unit, period and assumptions before comparing results.',
        'points':[{'label':'Dato' if es else 'Data','text':'Distingue registros de estimaciones.' if es else 'Distinguish records from estimates.'},{'label':'Cálculo' if es else 'Calculation','text':'Conserva denominadores y unidades.' if es else 'Keep denominators and units.'},{'label':'Decisión' if es else 'Decision','text':'Indica qué acción cambia con la evidencia.' if es else 'State which action changes with the evidence.'}]}}]


def mobile():
    plan=json.loads((ROOT/'react-native/desarrollo-de-aplicaciones-moviles/plan.json').read_text())
    for track in ('react-native','swift'):
      base=ROOT/track/'desarrollo-de-aplicaciones-moviles';code='React Native' if track=='react-native' else 'SwiftUI'
      for lang in ('es','en'):
        es=lang=='es';course=plan['title_'+lang]
        dump(base/lang/f'w01.0.{lang}.yaml',frame(course,code,lang,plan,True))
        for s in plan['sessions']:
          n=s['n'];topic=s['title_'+lang];topics=s['topics_'+lang];model=s['model_'+lang]
          slides=[cover(course,lang,n,topic,short(model[:1].upper()+model[1:],130),code),
            {'agenda':{'eyebrow':'Agenda','title':'Recorrido de la sesión' if es else 'Session outline','cards':[
              {'title':'Modelo' if es else 'Model','desc':short(model,100)}, {'title':'Implementación' if es else 'Implementation','desc':code},
              {'title':'Comprobación' if es else 'Check','desc':'Estados, casos límite y evidencia.' if es else 'States, boundary cases and evidence.'},
              {'title':'Bitácora','desc':short(s['lab_'+lang],100)}]}},
            {'objectives':{'eyebrow':'Objetivos' if es else 'Objectives','title':'Al terminar la sesión el alumno podrá…' if es else 'By the end of the session you will be able to…',
              'items':[{'head':short(t,105),'sub':'Resultado verificable en el caso Bitácora.' if es else 'A verifiable result in the Bitácora case.'} for t in s['objectives_'+lang]]}},roadmap(n,lang,True),
            {'divider':{'eyebrow':'Bloque 01' if es else 'Block 01','title':'Modelo y contratos' if es else 'Model and contracts','lede':model,'block':1}},concept(topic,model,lang)]
          for i,t in enumerate(topics):
            title=short(t.split(':',1)[0],70)
            slides.append(concept(title,t,lang,'Shared concept in the two tracks. Teaching sequence follows the synthesized practice proposal.'))
          slides.append({'divider':{'eyebrow':'Bloque 02' if es else 'Block 02','title':'Implementación en '+code if es else 'Implementation in '+code,'lede':'La API concreta es una instancia del modelo.' if es else 'The concrete API is an instance of the model.','block':2}})
          for i,c in enumerate(s['codes'][track]):
            chunks=split_code(c['source'])
            for j,chunk in enumerate(chunks):
              ext={'tsx':'tsx','ts':'ts','swift':'swift','json':'json','xml':'plist','yaml':'maestro','kotlin':'kt'}.get(c['lang'],c['lang'])
              slides.append({'code':{'eyebrow':code,'title':('Ejemplo' if es else 'Example')+f' {i+1}'+(f' · {j+1}/{len(chunks)}' if len(chunks)>1 else ''),
                'filename':f"w{n:02}-sample-{i+1}.{ext}",'lang':c['lang'],'source':chunk,
                'annotations':[{'label':'Contexto' if es else 'Context','text':'Fragmento del archivo de ejemplo. Conserva los tipos e imports de su contexto.' if es else 'Fragment of the sample file. Keep the types and imports supplied by its context.'},
                   {'label':'Comprobación' if es else 'Check','text':'Explica entradas, estado y resultado esperado.' if es else 'Explain inputs, state and the expected result.'}],
                'notes':'Sample source: '+code+' realization from the course synthesis. Continuation cards form one sample in order. This is a teaching excerpt, not a complete app. See the full source sample under labs/samples/.\n'+('https://reactnative.dev/docs/getting-started' if track=='react-native' else 'https://developer.apple.com/documentation/swiftui')}})
            sample=base/'labs/samples'/f'w{n:02}-sample-{i+1}.{ext}';sample.parent.mkdir(parents=True,exist_ok=True);sample.write_text(c['source'])
          q=s['quiz']
          # Rotate the answer position identically in both language editions.
          shift=(n-1)%4
          options=q['options_'+lang][shift:]+q['options_'+lang][:shift]
          answer='ABCD'[(1-shift)%4]
          slides.append({'quiz':{'eyebrow':'Comprobación' if es else 'Quick check','question':q['question_'+lang],
            'options':options,'notes':('Respuesta ' if es else 'Answer ')+answer+'. '+model}})
          slides+=lab_and_homework(s,lang,'Bitácora · '+f'v0.{n}')
          if n==17:
            slides=[slide for slide in slides if 'homework' not in slide]
          slides.append({'takeaways':{'eyebrow':'Resumen' if es else 'Summary','title':'Modelo, implementación y evidencia' if es else 'Model, implementation and evidence','items':[
            {'title':'Modelo' if es else 'Model','desc':short(model,220)},
            {'title':'Implementación' if es else 'Implementation','desc':short(s['objectives_'+lang][1],200)},
            {'title':'Evidencia' if es else 'Evidence','desc':'El resultado y su comprobación deben poder reproducirse.' if es else 'The result and its check must be reproducible.'}]}})
          slides.append(closing(lang,plan['sessions'][n]['title_'+lang] if n<17 else 'Cierre' if es else 'Closing feedback'))
          dump(base/lang/f'w{n:02}.{lang}.yaml',{'meta':{'course':course,'code':code,'lang':lang,'language':track,'week':n,'footer':course.upper()+' · '+code,'blocks':3},'slides':slides})

if __name__=='__main__':main()
