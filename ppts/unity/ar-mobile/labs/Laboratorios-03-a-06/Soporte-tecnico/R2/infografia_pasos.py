from pathlib import Path
import sys,re,json

ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'Infografia'
OUT.mkdir(exist_ok=True)
WORK=Path(__file__).parent/'work'
WORK.mkdir(exist_ok=True)
copy={
 'intro1':'Haz la prueba en una escena vacía de un proyecto aparte. El botón Lanzar escribirá “Botón recibido” en Console.',
 's1':'En Project Settings > Player > Other Settings, pon Active Input Handling en Both para probar OnGUI. Reinicia Unity si lo pide. En Hierarchy, crea un objeto vacío llamado Controlador.',
 's2':'En Project, crea BotonDemo.cs y sustituye su contenido por el código de abajo. El nombre del archivo debe coincidir con el de la clase.',
 's3':'Guarda el archivo y espera a que Unity compile. Arrastra BotonDemo.cs desde Project hasta Controlador en Hierarchy.',
 's4':'Entra en Play y pulsa Lanzar en Game. Abre Console: debe aparecer “Botón recibido”. Si no aparece el botón, revisa que Controlador y su componente estén activos.',
 'explain1':'OnGUI describe el botón al procesar eventos de interfaz. GUI.Button devuelve true cuando se activa; por eso Lanzar() está dentro del if. Unity puede llamar OnGUI varias veces por fotograma.',
 'rect':'Rect indica la posición y el tamaño: x = 30, y = 30, ancho = 180 y alto = 60. El origen está en la esquina superior izquierda.',
 'intro2':'Sal de Play antes de editar. La acción seguirá siendo Lanzar(); ahora el botón será un objeto dentro de un Canvas.',
 's5':'Sustituye el script por esta versión. Se retira OnGUI y se conserva el método público que mostrará el mensaje. El componente sigue en Controlador.',
 's6':'En Hierarchy, abre el menú UI y elige el botón de TextMeshPro. Si Unity pide TMP Essentials, impórtalos. Unity añade Canvas y EventSystem si faltan.',
 's7':'Renombra el botón como Lanzar. Selecciona su hijo Text (TMP) y escribe Lanzar en el campo de texto. La etiqueta y la acción se configuran por separado.',
 's8':'Selecciona el botón. En Button, abre On Click (), pulsa + y arrastra Controlador al campo del objeto. En el menú de función elige BotonDemo > Lanzar ().',
 's9':'Entra en Play, limpia Console y pulsa Lanzar en Game. Debe aparecer “Botón recibido”. Si no aparece, revisa On Click (), Interactable y si una imagen con Raycast Target cubre el botón.',
 'check':'Si no responde, revisa primero On Click (): debe tener Controlador y Lanzar (). Después, confirma que Interactable esté activo y que ninguna imagen transparente cubra el botón con Raycast Target.',
 'input':'Con el nuevo Input System, usa un solo EventSystem con InputSystemUIInputModule y sus acciones asignadas. En AR, el código que coloca objetos también debe excluir los toques sobre la UI.'
}
prose='\n\n'.join(' '.join(list(copy.values())[i:i+2]) for i in range(0,len(copy),2))
(WORK/'infografia-pasos-prosa.md').write_text(prose,encoding='utf-8')
if '--text-only' in sys.argv:sys.exit()

from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.colors import HexColor
from reportlab.platypus import Paragraph
from reportlab.lib.styles import ParagraphStyle

for name,file in [('Sans','arial.ttf'),('Bold','arialbd.ttf'),('Serif','georgia.ttf'),('Mono','consola.ttf')]:
 pdfmetrics.registerFont(TTFont(name,'C:/Windows/Fonts/'+file))
pdfmetrics.registerFontFamily('Sans',normal='Sans',bold='Bold')
W,H=720,1020
navy='#0f172a';blue='#2563eb';muted='#5b6478';border='#dce1ea';paper='#fafbff'
c=canvas.Canvas(str(OUT/'OnGUI-y-Canvas-Learning-Hub.pdf'),pagesize=(W,H))
c.setTitle('Un botón con OnGUI y con Canvas: paso a paso')
c.setAuthor('David Escobar Castillejos')
def rect(x,y,w,h,fill,stroke=None):
 c.setFillColor(HexColor(fill));c.setStrokeColor(HexColor(stroke or fill));c.rect(x,H-y-h,w,h,fill=1,stroke=bool(stroke))
def text(s,x,y,size=16,font='Sans',color=navy):
 c.setFillColor(HexColor(color));c.setFont(font,size);c.drawString(x,H-y-size*.83,s)
def para(s,x,y,w,size=15,color=navy,maxh=None,font='Sans'):
 p=Paragraph(s,ParagraphStyle('body',fontName=font,fontSize=size,leading=size*1.28,textColor=HexColor(color)))
 pw,ph=p.wrap(w,H)
 if maxh:assert ph<=maxh,(s,ph,maxh)
 p.drawOn(c,x,H-y-ph)
 return y+ph
def rule(y):rect(42,y,636,.7,border)
def step(n,title,y):
 text(str(n),42,y,26,'Serif',blue);text(title,78,y+3,19,'Bold')
def header(n,title,sub):
 rect(0,0,W,H,paper);rect(0,0,W,4,blue)
 c.drawImage(str(next(p for p in ROOT.parents if (p/'ppts/brand/duck-512.png').is_file())/'ppts/brand/duck-512.png'),42,H-67,27,27,mask='auto')
 text('LEARNING HUB',80,43,12,'Bold',blue)
 text('UNITY 6  /  EJERCICIO PARA CLASE',42,86,11,'Bold',muted)
 text(title,42,112,32,'Serif')
 para(sub,42,162,636,15,muted,maxh=60)
 rule(965);text('David Escobar Castillejos · OnGUI y Canvas (uGUI)',42,980,10,'Sans',muted)
 text(f'{n} / 2',647,978,12,'Bold',blue)
def code(lines,x,y,w,size=13.3,leading=17.2):
 h=len(lines)*leading+35
 rect(x,y,w,h,navy)
 for i,s in enumerate(lines):
  text(f'{i+1:02}',x+12,y+17+i*leading,9.2,'Mono','#8895b0')
  text(s,x+39,y+15+i*leading,size,'Mono','#f3f5fc')
 return y+h

header(1,'Primero, el botón con OnGUI',copy['intro1'])
step(1,'Prepara la entrada y crea Controlador.',230)
para(copy['s1'],78,266,596,14.5,maxh=60)
step(2,'Escribe el botón en C#.',342)
para(copy['s2'],78,378,596,14.5,maxh=42)
code1=['using UnityEngine;','public class BotonDemo : MonoBehaviour','{','    void OnGUI()','    {','        if (GUI.Button(','            new Rect(30, 30, 180, 60),','            "Lanzar"))','        {','            Lanzar();','        }','    }','    public void Lanzar()','    {','        Debug.Log("Botón recibido");','    }','}']
code(code1,42,440,403,12.3,15.1)
text('Si se ve, pero no responde',470,444,14.5,'Bold')
para('Con solo Input System activo, OnGUI no recibe eventos de entrada en ejecución. Both permite probarlo con la entrada anterior.',470,477,206,14,maxh=100)
rect(470,584,206,66,'#ffffff',border)
text('GAME',481,593,9,'Bold',muted)
rect(486,610,116,29,blue)
text('Lanzar',521,617,13,'Bold','#ffffff')
para('El if evita ejecutar Lanzar() en cada llamada de OnGUI. La acción ocurre cuando GUI.Button devuelve true.',470,667,206,13.5,maxh=89)
step(3,'Añade el script a Controlador.',758)
para(copy['s3'],78,794,596,14.5,maxh=40)
step(4,'Pulsa el botón y revisa el resultado.',850)
para(copy['s4'],78,887,596,14.5,maxh=58)
text('Fuente: Unity, Input System 1.11, UI support (§ IMGUI).',42,950,9,'Sans',muted)
c.linkURL('https://docs.unity3d.com/Packages/com.unity.inputsystem@1.11/manual/UISupport.html#immediate-mode-gui',(42,H-962,400,H-948),relative=0)
c.showPage()

header(2,'Ahora, el botón dentro de Canvas',copy['intro2'])
step(5,'Deja en el script solo la acción.',225)
para(copy['s5'],78,262,596,14.5,maxh=40)
code2=['using UnityEngine;','public class BotonDemo : MonoBehaviour','{','    public void Lanzar()','    {','        Debug.Log("Botón recibido");','    }','}']
code(code2,42,315,403,12.3,15.1)
text('Revisa EventSystem',470,325,16,'Bold')
para('Con Input System, usa InputSystemUIInputModule y asigna sus acciones. Debe haber un solo EventSystem activo.',470,357,206,13.5,maxh=100)
step(6,'Crea el botón de la interfaz.',489)
para(copy['s6'],78,525,596,14.5,maxh=60)
step(7,'Escribe la etiqueta del botón.',596)
para(copy['s7'],78,632,596,14.5,maxh=40)
step(8,'Conecta el clic con Lanzar().',688)
para(copy['s8'],78,724,596,14.5,maxh=60)
# Simple Inspector strip: a teaching diagram, not a screenshot.
rect(78,791,596,36,'#eef2fa',border)
text('On Click ()',90,802,11.5,'Bold')
text('Controlador',210,802,12,'Mono')
text('BotonDemo.Lanzar ()',414,802,12,'Mono',blue)
step(9,'Prueba la misma acción.',846)
para(copy['s9'],78,882,596,14.5,maxh=60)
text('En AR, excluye los toques sobre UI antes de colocar objetos en el mundo.',78,945,10.5,'Sans',muted)
c.showPage();c.save()
# Explanatory notes included as a companion text, keeping the two-page diagram readable.
notes='''# OnGUI y Canvas: notas para explicar el ejemplo\n\n'''+copy['explain1']+'\n\n'+copy['check']+'\n\n'+copy['input']+'''\n\nFuentes técnicas: Unity Manual, IMGUI Controls; documentación oficial de uGUI, Button; Input System 1.11, UI Support.\nhttps://docs.unity3d.com/6000.0/Documentation/Manual/GUIScriptingGuide.html\nhttps://docs.unity3d.com/Packages/com.unity.ugui@2.0/manual/script-Button.html\nhttps://docs.unity3d.com/Packages/com.unity.inputsystem@1.11/manual/UISupport.html\n'''
# These notes are working copy; the final deliverable stays two pages.
(WORK/'infografia-pasos-notas.md').write_text(notes,encoding='utf-8')
print(OUT/'OnGUI-y-Canvas-Learning-Hub.pdf')
