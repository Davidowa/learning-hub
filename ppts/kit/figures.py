"""The course figures, drawn with kit.doodle.

Each entry is one diagram: a drawing function, the thing it explains, where it
gets reused, and which lessons place it. `--catalogue` turns that into markdown,
so the documentation cannot drift from the drawings.

    python -m kit.figures --list
    python -m kit.figures slicing --lang es
    python -m kit.figures --all
    python -m kit.figures --catalogue          # rewrites ppts/IMAGES.md in UTF-8

Output goes to ppts/img/<lang>/<id>.{svg,png}, outside any one subject, because
most of these explain a language feature rather than a lesson.
"""
from __future__ import annotations

import argparse
import os

from .doodle import BLUE, BLUE_WASH, INK, MUTED, PAPER, YELLOW, YELLOW_WASH, Pen

W, H = 1680, 720           # 21:9, the shape the figure layout expects
WS, HS = 1440, 810         # 16:9, for the squarer diagrams

T = {  # every label the figures use, so a new language is one dict away
    'es': dict(
        index='índice', negative='negativo', not_in='el 3 no entra',
        function='función', local='local', dies='lo local muere cuando la función termina',
        same='el = copia la referencia, no el contenido',
        list_='lista', tuple_='tupla', set_='conjunto', dict_='diccionario',
        ordered='ordenada', immutable='inmutable', unique='sin repetidos', bykey='por llave',
        caught='cada except atrapa su tipo', clean='sin excepción',
        klass='clase', object_='objeto', objects='objetos',
        blueprint='el molde', instances='cada objeto con su propio estado',
        shared='se comparte', own='propio de cada objeto',
        in_body='en el cuerpo de la clase', in_init='dentro de __init__',
        four_lists='cuatro listas', one_object='un objeto',
        drift='borra uno y las listas se desalinean',
        names='nombres', grades='notas', degree='carrera', term='semestre',
        # w04 · access levels
        outside='desde fuera', acc_class='Cuenta', acc_pub='titular',
        acc_prot='_banco', acc_priv='__saldo',
        public='público', protected='protegido', private='privado',
        by_convention='nada lo impide, es un acuerdo', readable='se lee sin problema',
        blocked='AttributeError',
        mangled='los dos guiones bajos renombran el atributo a _Cuenta__saldo',
        # w05 · UML class box
        uml_class='Libro',
        uml_attrs=('- titulo: str', '- autor: str', '- prestado: bool'),
        uml_methods=('+ prestar()', '+ devolver()'),
        uml_code=('class Libro:', 'self.__titulo = titulo', 'def prestar(self):'),
        uml_name='el nombre', uml_state='lo que recuerda', uml_does='lo que sabe hacer',
        uml_legend='- privado · + público',
        # COM103 · the C++ variants. Same drawings, different truth: C++ enforces
        # all three access levels at compile time, where Python enforces one.
        cpp_undeclared='C2065',
        cpp_from_outside='desde fuera', cpp_from_child='desde una clase hija',
        cpp_acc_pub='titular', cpp_acc_prot='banco', cpp_acc_priv='saldo',
        cpp_acc_note='los tres los cobra el compilador, y saltárselos da error C2248',
        cpp_uml_attrs=('- titulo: string', '- autor: string', '- prestado: bool'),
        cpp_uml_code=('class Libro {', 'std::string titulo;', 'void prestar();'),
        vr_by_value='por valor', vr_by_ref='por referencia', vr_copy='se copia',
        vr_sig_value='void duplicar(int n)', vr_sig_ref='void duplicarRef(int& n)',
        vr_caller='original', vr_note_value='cambiar n no toca a original',
        vr_note_ref='n es otro nombre de la misma caja',
        am_name='notas', am_index='índice',
        am_note='el índice 6 no existe y nadie lo revisa: compila, corre y lee memoria ajena',
        ptr_var='x', ptr_ptr='p', ptr_value='42', ptr_addr='0x7ffe4c',
        ptr_holds='p guarda la dirección de x, no su valor',
        ptr_deref='*p llega al 42 · p es la dirección',
        sh_stack='pila', sh_heap='montón',
        sh_auto='int n = 42;', sh_dyn='int* p = new int(42);',
        sh_auto_note='nace y muere con el bloque, sin que escribas nada',
        sh_dyn_note='vive hasta el delete, aunque el bloque haya terminado',
        sh_leak='sin delete, esa memoria queda perdida hasta que el programa termina',
        vt_call='figura->area()', vt_table='tabla virtual',
        vt_rows=('Circulo::area', 'Cuadrado::area', 'Triangulo::area'),
        vt_real='el objeto es un Cuadrado',
        vt_note='la llamada es una sola y el tipo real decide cuál corre',
        # w07 · inheritance depth
        hier_a='Animal', hier_b='Ave', hier_c='Gallina', hier_fly='volar()',
        hier_good='dos niveles: cada hijo lee a su manera',
        hier_bad='tres niveles, y la gallina hereda volar()',
        # w08 · polymorphism
        poly_loop='for animal in animales:', poly_call='animal.hablar()',
        poly_dog='Perro', poly_cat='Gato', poly_woof='¡Guau!', poly_meow='¡Miau!',
        poly_note='una sola línea, y el tipo real elige el método',
        # w09 · recursion
        base_case='caso base = 1', down='baja', up='sube',
        rec_note='cada llamada espera a la de abajo, y el resultado se arma de regreso',
        # w12 · the file lifecycle
        fl_open='open(ruta, "r")', fl_work='f.read()', fl_close='f.close()',
        fl_with='with open(ruta) as f:',
        fl_auto='abre al entrar y cierra al salir del bloque',
        fl_good='con with cierra aunque truene',
        fl_bad='sin with, un error se salta el close',
        fl_note='el archivo abierto retiene el búfer, así que lo escrito puede no llegar al disco',
        # w13 · sequential and random access
        st_data='HOLA MUNDO!!', sequential='lectura secuencial, una posición a la vez',
        st_note='seek mueve el cursor de un salto; tell dice dónde quedó',
        # w14 · the Qt event loop
        el_user='clic del usuario', el_queue='cola de eventos',
        el_dispatch='exec() reparte', el_slot='tu función corre',
        el_back='y vuelve a esperar el siguiente',
        el_note='entre un evento y el siguiente el programa no hace nada, solo espera',
        # w15 · layout managers
        lay_note='el layout decide la posición y el tamaño; tú solo dices en qué orden entran',
        # w16 · database access
        db_prog='tu programa', db_file='pixar.db', db_cursor='cursor',
        db_commit='sin commit, lo escrito no se guarda',
        db_note='el cursor no trae las filas, apunta a ellas y las entrega una por una',
        # w00 · where C++ comes from
        tl=(('1972', 'nace C'), ('1979', 'C con clases'), ('1983', 'se llama C++'),
            ('1998', 'primer ISO'), ('2011', 'el gran salto'), ('2020', 'el del curso')),
        tl_note='cuarenta años del mismo lenguaje, y desde 2011 una versión cada tres',
        # w00 · what a compiled language does before running
        cc_src='hola.cpp', cc_obj='hola.obj', cc_exe='hola.exe',
        cc_write='lo que escribes', cc_mid='código máquina, todavía incompleto',
        cc_out='el programa que corre',
        cc_step1='compilador', cc_step2='enlazador',
        cc_sub1='a código máquina', cc_sub2='suma la biblioteca',
        cc_note='el error de sintaxis aparece aquí, antes de que el programa llegue a correr',
        # w02 (TIA502) · the rest of the flowchart symbols
        fs_sub='proceso predefinido', fs_sub_e='una función que ya escribiste',
        fs_prep='preparación', fs_prep_e='donde arranca un ciclo',
        fs_conn='conector', fs_conn_e='sigue en el círculo con la misma letra',
        fs_off='fuera de página', fs_off_e='sigue en otra hoja',
        fs_db='datos almacenados', fs_db_e='un archivo o una tabla',
        fs_doc='documento', fs_doc_e='una salida hecha para leerse',
        fs_min='entrada manual', fs_min_e='alguien lo teclea · input()',
        fs_disp='despliegue', fs_disp_e='va a la pantalla · print()',
        fs_mop='operación manual', fs_mop_e='la hace una persona',
        fs_call='calcular_bono()', fs_loop='i = 0, i < n', fs_page='pág. 2',
        fs_file='ventas.csv', fs_rep='Reporte', fs_field='sueldo',
        fs_out='total', fs_ok='Autorizar',
        fc_left='se corta aquí', fc_right='y sigue aquí',
        fc_read='LEER datos', fc_valid='¿válidos?', fc_clean='limpiar',
        fc_group='agrupar', fc_write='ESCRIBIR', fc_end='FIN',
        fc_note='el círculo no es un paso, solo dice dónde continúa la línea',
    ),
    'en': dict(
        index='index', negative='negative', not_in='index 3 is excluded',
        function='function', local='local', dies='locals die when the call returns',
        same='= copies the reference, not the contents',
        list_='list', tuple_='tuple', set_='set', dict_='dictionary',
        ordered='ordered', immutable='immutable', unique='no duplicates', bykey='by key',
        caught='each except catches its own type', clean='no exception',
        klass='class', object_='object', objects='objects',
        blueprint='the cutter', instances='each object with its own state',
        shared='shared', own='one per object',
        in_body='in the class body', in_init='inside __init__',
        four_lists='four lists', one_object='one object',
        drift='delete one and the lists go out of step',
        names='names', grades='grades', degree='degree', term='term',
        # w04 · access levels
        outside='from outside', acc_class='Account', acc_pub='holder',
        acc_prot='_bank', acc_priv='__balance',
        public='public', protected='protected', private='private',
        by_convention='nothing stops you, it is an agreement',
        readable='reads just fine', blocked='AttributeError',
        mangled='the two underscores rename the attribute to _Account__balance',
        # w05 · UML class box
        uml_class='Book',
        uml_attrs=('- title: str', '- author: str', '- on_loan: bool'),
        uml_methods=('+ lend()', '+ give_back()'),
        uml_code=('class Book:', 'self.__title = title', 'def lend(self):'),
        uml_name='the name', uml_state='what it remembers', uml_does='what it can do',
        uml_legend='- private · + public',
        # COM103 · the C++ variants. Same drawings, different truth: C++ enforces
        # all three access levels at compile time, where Python enforces one.
        cpp_undeclared='C2065',
        cpp_from_outside='from outside', cpp_from_child='from a derived class',
        cpp_acc_pub='holder', cpp_acc_prot='bank', cpp_acc_priv='balance',
        cpp_acc_note='all three are enforced by the compiler, and breaking one is error C2248',
        cpp_uml_attrs=('- title: string', '- author: string', '- onLoan: bool'),
        cpp_uml_code=('class Book {', 'std::string title;', 'void lend();'),
        vr_by_value='by value', vr_by_ref='by reference', vr_copy='copied',
        vr_sig_value='void twice(int n)', vr_sig_ref='void twiceRef(int& n)',
        vr_caller='original', vr_note_value='changing n does not touch original',
        vr_note_ref='n is another name for the same box',
        am_name='marks', am_index='index',
        am_note='index 6 does not exist and nothing checks: it builds, it runs, it reads memory that is not yours',
        ptr_var='x', ptr_ptr='p', ptr_value='42', ptr_addr='0x7ffe4c',
        ptr_holds='p holds the address of x, not its value',
        ptr_deref='*p reaches the 42 · p is the address',
        sh_stack='stack', sh_heap='heap',
        sh_auto='int n = 42;', sh_dyn='int* p = new int(42);',
        sh_auto_note='born and destroyed with the block, without you writing anything',
        sh_dyn_note='lives until the delete, even after the block has ended',
        sh_leak='with no delete that memory is lost until the program exits',
        vt_call='shape->area()', vt_table='virtual table',
        vt_rows=('Circle::area', 'Square::area', 'Triangle::area'),
        vt_real='the object is a Square',
        vt_note='there is one call site and the real type decides which one runs',
        # w07 · inheritance depth
        hier_a='Animal', hier_b='Bird', hier_c='Chicken', hier_fly='fly()',
        hier_good='two levels: each child reads its own way',
        hier_bad='three levels, and the chicken inherits fly()',
        # w08 · polymorphism
        poly_loop='for animal in animals:', poly_call='animal.talk()',
        poly_dog='Dog', poly_cat='Cat', poly_woof='Woof!', poly_meow='Meow!',
        poly_note='one line, and the real type picks the method',
        # w09 · recursion
        base_case='base case = 1', down='down', up='up',
        rec_note='every call waits on the one below, and the result is built on the way back',
        # w12 · the file lifecycle
        fl_open='open(path, "r")', fl_work='f.read()', fl_close='f.close()',
        fl_with='with open(path) as f:',
        fl_auto='opens on entry and closes on the way out of the block',
        fl_good='with it, the file closes even on a crash',
        fl_bad='without it, an error skips the close',
        fl_note='an open file holds the buffer, so what you wrote may never reach the disk',
        # w13 · sequential and random access
        st_data='HELLO WORLD!', sequential='sequential reading, one position at a time',
        st_note='seek moves the cursor in one jump; tell says where it ended up',
        # w14 · the Qt event loop
        el_user='the user clicks', el_queue='event queue',
        el_dispatch='exec() dispatches', el_slot='your function runs',
        el_back='then back to waiting for the next one',
        el_note='between one event and the next the program does nothing but wait',
        # w15 · layout managers
        lay_note='the layout decides position and size; you only say what order they go in',
        # w16 · database access
        db_prog='your program', db_file='pixar.db', db_cursor='cursor',
        db_commit='without commit, what you wrote is not saved',
        db_note='the cursor does not hold the rows, it points at them and hands them over one by one',
        # w00 · where C++ comes from
        tl=(('1972', 'C is born'), ('1979', 'C with Classes'), ('1983', 'named C++'),
            ('1998', 'first ISO'), ('2011', 'the big leap'), ('2020', 'the course one')),
        tl_note='forty years of one language, and since 2011 a release every three',
        # w00 · what a compiled language does before running
        cc_src='hello.cpp', cc_obj='hello.obj', cc_exe='hello.exe',
        cc_write='what you write', cc_mid='machine code, still incomplete',
        cc_out='the program that runs',
        cc_step1='compiler', cc_step2='linker',
        cc_sub1='to machine code', cc_sub2='adds the library',
        cc_note='the syntax error turns up here, before the program ever gets to run',
        # w02 (TIA502) · the rest of the flowchart symbols
        fs_sub='predefined process', fs_sub_e='a function you already wrote',
        fs_prep='preparation', fs_prep_e='where a loop is set up',
        fs_conn='connector', fs_conn_e='continues at the circle with the same letter',
        fs_off='off-page connector', fs_off_e='continues on another sheet',
        fs_db='stored data', fs_db_e='a file or a table',
        fs_doc='document', fs_doc_e='output made to be read',
        fs_min='manual input', fs_min_e='somebody types it · input()',
        fs_disp='display', fs_disp_e='it goes to the screen · print()',
        fs_mop='manual operation', fs_mop_e='a person does it',
        fs_call='compute_bonus()', fs_loop='i = 0, i < n', fs_page='page 2',
        fs_file='sales.csv', fs_rep='Report', fs_field='salary',
        fs_out='total', fs_ok='Approve',
        fc_left='it stops here', fc_right='and carries on here',
        fc_read='READ data', fc_valid='valid?', fc_clean='clean',
        fc_group='group', fc_write='WRITE', fc_end='END',
        fc_note='the circle is not a step, it only says where the line continues',
    ),
}


# ────────────────────────────────────────────────────────────── figures
def slicing(t, lang):
    p = Pen(W, H, seed=41)
    word = 'PYTHON'
    n, tw, gap = len(word), 150, 20
    total = n * tw + (n - 1) * gap
    x0, y0, th = (W - total) / 2, 290, 150

    p.mono(W / 2, 120, 'course = "PYTHON"', 42)
    for i, ch in enumerate(word):
        x = x0 + i * (tw + gap)
        p.rect(x, y0, tw, th, r=14, fill=BLUE_WASH if i < 3 else None)
        p.text(x + tw / 2, y0 + 104, ch, 70)
        p.text(x + tw / 2, y0 - 26, str(i), 30, BLUE)
        p.text(x + tw / 2, y0 + th + 48, str(i - n), 30, BLUE)
    p.text(x0 - 34, y0 - 26, t['index'], 26, MUTED, anchor='end')
    p.text(x0 - 34, y0 + th + 48, t['negative'], 26, MUTED, anchor='end')

    p.bracket(x0, x0 + 3 * tw + 2 * gap, y0 + th + 76, depth=24)
    p.mono(x0 + (3 * tw + 2 * gap) / 2, y0 + th + 148, 'course[0:3]', 40)

    cut = x0 + 3 * tw + 2.5 * gap
    p.line(cut, y0 - 6, cut, y0 + th + 6, w=5, color=YELLOW, passes=1, wobble=0.8)
    p.arrow(cut + 300, y0 - 96, cut + 12, y0 - 14)
    p.text(cut + 320, y0 - 104, t['not_in'], 32, anchor='start')
    return p


def _scope(t, error):
    p = Pen(W, H, seed=13)
    p.rect(70, 110, 1180, 520, r=28)
    p.text(110, 172, 'global', 36, BLUE, anchor='start')
    p.rect(200, 240, 720, 330, r=24, fill=BLUE_WASH)
    p.text(240, 300, t['function'], 34, BLUE, anchor='start')
    p.rect(330, 340, 440, 180, r=20, fill=YELLOW_WASH)
    p.text(550, 392, t['local'], 34)
    for cx, name in ((450, 'x'), (650, 'y')):
        p.ellipse(cx, 465, 38, 34)
        p.mono(cx, 475, name, 30)
    p.arrow(1440, 600, 800, 470)
    p.cross(880, 528, r=24)
    p.text(1450, 632, error, 36, anchor='start')
    p.text(W / 2, 690, t['dies'], 30, MUTED)
    return p


def scope(t, lang):
    return _scope(t, 'NameError')


def scope_cpp(t, lang):
    # Same drawing, one label. Python raises NameError when the program runs;
    # C++ never gets that far, the compiler refuses the name at build time.
    return _scope(t, t['cpp_undeclared'])


def reference_vs_copy(t, lang):
    p = Pen(W, H, seed=97)
    p.line(W / 2, 90, W / 2, 640, w=2.0, color=MUTED)

    def side(cx, code, boxes, tags):
        p.mono(cx, 130, code, 34)
        for (bx, by, label) in boxes:
            p.rect(bx, by, 280, 110, r=16, fill=BLUE_WASH)
            p.mono(bx + 140, by + 68, label, 28)
        for (tx, ty, name, target) in tags:
            p.rect(tx, ty, 190, 66, r=30, fill=YELLOW_WASH)
            p.mono(tx + 95, ty + 43, name, 26)
            p.wave(tx + 190, ty + 33, target[0], target[1], amp=9)

    side(400, 'copia = numeros' if lang == 'es' else 'copy = numbers',
         [(510, 350, '[1, 2, 3, 4]')],
         [(110, 250, 'numeros' if lang == 'es' else 'numbers', (505, 380)),
          (110, 440, 'copia' if lang == 'es' else 'copy', (505, 425))])

    side(1240, 'copia = numeros.copy()' if lang == 'es' else 'copy = numbers.copy()',
         [(1340, 240, '[1, 2, 3]'), (1340, 430, '[1, 2, 3, 4]')],
         [(950, 250, 'numeros' if lang == 'es' else 'numbers', (1335, 285)),
          (950, 440, 'copia' if lang == 'es' else 'copy', (1335, 475))])

    p.text(W / 2, 692, t['same'], 30, MUTED)
    return p


def collections(t, lang):
    p = Pen(W, H, seed=5)
    labels = [(t['list_'], t['ordered'], '[1, 2, 3]'),
              (t['tuple_'], t['immutable'], '(1, 2, 3)'),
              (t['set_'], t['unique'], '{1, 2, 3}'),
              (t['dict_'], t['bykey'], "{'a': 1}")]
    bw, gap = 340, 60
    total = 4 * bw + 3 * gap
    x0, y0 = (W - total) / 2, 190

    for i, (name, prop, syntax) in enumerate(labels):
        x = x0 + i * (bw + gap)
        p.rect(x, y0, bw, 330, r=22, fill=BLUE_WASH if i % 2 == 0 else None)
        p.text(x + bw / 2, y0 + 74, name, 44)
        p.mono(x + bw / 2, y0 + 150, syntax, 30, BLUE)
        p.line(x + 50, y0 + 196, x + bw - 50, y0 + 196, w=1.8, color=MUTED)
        p.text(x + bw / 2, y0 + 256, prop, 30, MUTED)
        if i < 3:
            p.text(x + bw + gap / 2, y0 + 180, '·', 44, MUTED)
    p.text(W / 2, y0 + 430, 'list · tuple · set · dict', 32, MUTED)
    return p


def exceptions(t, lang):
    p = Pen(WS, HS, seed=61)
    p.rect(120, 120, 520, 220, r=22, fill=YELLOW_WASH)
    p.mono(380, 200, 'try:', 40)
    p.mono(380, 268, '10 / age', 32, MUTED)

    for i, (name, y) in enumerate((('ValueError', 470), ('ZeroDivisionError', 640))):
        p.arrow(660, 250 + i * 40, 830, y - 30, wavy=True)
        p.rect(840, y - 78, 470, 110, r=18, fill=BLUE_WASH)
        p.mono(1075, y - 12, f'except {name}', 26 if i else 30)

    p.arrow(400, 350, 400, 690)
    p.rect(180, 690, 440, 96, r=18)
    p.mono(400, 750, 'else:', 34)
    p.text(400, 660, t['clean'], 26, MUTED)
    p.text(1075, 250, t['caught'], 28, MUTED)
    return p


def paradigms(t, lang):
    p = Pen(W, H, seed=23)
    cx, cy = W / 2, H / 2 - 10
    p.ellipse(cx, cy, 190, 120, w=3.0, fill=YELLOW_WASH)
    p.text(cx, cy + 4, 'POO' if lang == 'es' else 'OOP', 58)
    p.text(cx, cy + 60, t['klass'] + ' + ' + t['object_'] if lang == 'es'
           else 'class + object', 26, MUTED)

    spokes = ([('imperativo', -168), ('estructurado', -120), ('funcional', -58),
               ('eventos', 58), ('visual', 120), ('lógico', 168)] if lang == 'es'
              else [('imperative', -168), ('structured', -120), ('functional', -58),
                    ('event-driven', 58), ('visual', 120), ('logic', 168)])
    import math
    for label, deg in spokes:
        a = math.radians(deg)
        ex, ey = cx + 560 * math.cos(a), cy + 250 * math.sin(a)
        p.wave(cx + 200 * math.cos(a), cy + 130 * math.sin(a),
               ex - 70 * math.cos(a), ey - 40 * math.sin(a), amp=7)
        p.ellipse(ex, ey, 26, 24, fill=BLUE_WASH)
        p.text(ex, ey + 62, label, 28, BLUE)
    return p


def parallel_lists(t, lang):
    p = Pen(W, H, seed=77)
    p.line(W / 2, 100, W / 2, 640, w=2.0, color=MUTED)
    p.text(400, 90, t['four_lists'], 38)
    p.text(1280, 90, t['one_object'], 38)

    rows = [t['names'], t['grades'], t['degree'], t['term']]
    for r, name in enumerate(rows):
        y = 180 + r * 96
        p.text(150, y + 42, name, 26, MUTED, anchor='end')
        shift = 60 if r > 0 else 0
        for c in range(3):
            if r == 0 and c == 1:
                p.rect(180 + c * 190, y, 170, 70, r=12)
                p.cross(265 + c * 190, y + 35, r=20, w=3.0)
                continue
            p.rect(180 + c * 190 + shift, y, 170, 70, r=12, fill=BLUE_WASH)

    for c in range(3):
        x = 1000 + c * 220
        if c == 1:
            p.rect(x, 210, 190, 300, r=16)
            p.cross(x + 95, 360, r=28, w=3.4)
            continue
        p.rect(x, 210, 190, 300, r=16, fill=YELLOW_WASH)
        for r in range(4):
            p.line(x + 26, 270 + r * 62, x + 164, 270 + r * 62, w=1.8, color=MUTED)

    p.text(420, 690, t['drift'], 28, MUTED)
    p.text(1280, 690, t['instances'], 28, MUTED)
    return p


def class_object(t, lang):
    p = Pen(W, H, seed=31)
    p.rect(110, 230, 380, 300, r=22)
    p.text(300, 300, t['klass'], 46)
    for dx in (-70, 0, 70):
        p.arc(300 + dx, 430, 46, 200, 340, w=2.2)
    p.line(196, 430, 404, 430, w=2.2)
    p.text(300, 570, t['blueprint'], 28, MUTED)

    p.arrow(520, 380, 640, 380)
    p.rect(660, 250, 340, 260, r=20, fill=YELLOW_WASH)
    p.mono(830, 350, '__init__', 38)
    p.text(830, 430, '(  )', 40, MUTED)
    p.arrow(1030, 380, 1130, 380)

    # three cookies, sized and spaced so the last one clears the right edge
    r, step, first = 66, 160, 1250
    for i in range(3):
        cx = first + i * step
        p.ellipse(cx, 380, r, r - 4, fill=BLUE_WASH if i != 1 else YELLOW_WASH)
        p.text(cx, 392, str(i + 1), 38)
    mid = first + step
    p.text(mid, 540, t['objects'], 34)
    p.text(mid, 596, t['instances'], 26, MUTED)
    return p


def class_vs_instance(t, lang):
    p = Pen(W, H, seed=53)
    p.line(W / 2, 100, W / 2, 640, w=2.0, color=MUTED)
    p.mono(420, 110, t['in_body'], 30)
    p.mono(1260, 110, t['in_init'], 30)

    # shared
    p.rect(280, 180, 280, 130, r=18, fill=YELLOW_WASH)
    p.mono(420, 252, "['X1']", 30)
    for dx, name in ((-160, 'a'), (160, 'b')):
        p.rect(340 + dx, 430, 160, 130, r=18, fill=BLUE_WASH)
        p.mono(420 + dx, 502, name, 34)
        # each cart reaches the shared basket from its own side, no crossing
        p.wave(420 + dx, 430, 420 + dx * 0.38, 316, amp=7)
    p.text(420, 630, t['shared'], 30, MUTED)

    # own
    for dx, name, items in ((-170, 'a', "['X1']"), (170, 'b', '[]')):
        p.rect(1180 + dx, 300, 200, 260, r=18, fill=BLUE_WASH)
        p.mono(1280 + dx, 360, name, 34)
        p.rect(1206 + dx, 400, 148, 110, r=14, fill=YELLOW_WASH)
        p.mono(1280 + dx, 468, items, 26)
    p.text(1280, 630, t['own'], 30, MUTED)
    return p


def access_levels(t, lang):
    p = Pen(W, H, seed=101)
    p.rect(70, 270, 290, 150, r=22, fill=BLUE_WASH)
    p.text(215, 332, t['outside'], 34)
    p.mono(215, 386, 'c.???', 28, MUTED)

    p.rect(540, 90, 580, 540, r=26)
    p.text(830, 158, t['acc_class'], 46)
    p.line(580, 192, 1080, 192, w=2.0, color=MUTED)

    rows = ((t['acc_pub'], t['public'], t['readable'], BLUE_WASH, 'plain'),
            (t['acc_prot'], t['protected'], t['by_convention'], None, 'wavy'),
            (t['acc_priv'], t['private'], t['blocked'], YELLOW_WASH, 'blocked'))
    for i, (name, kind, verdict, wash, how) in enumerate(rows):
        y = 236 + i * 126
        p.rect(590, y, 480, 96, r=18, fill=wash)
        p.mono(830, y + 60, name, 34)
        p.arrow(365, 345, 585, y + 48, wavy=(how == 'wavy'))
        if how == 'blocked':
            p.cross(523, 483, r=26)
        p.text(1150, y + 40, kind, 32, BLUE, anchor='start')
        p.text(1150, y + 86, verdict, 26, MUTED, anchor='start')
    p.text(W / 2, 694, t['mangled'], 28, MUTED)
    return p


def uml_class(t, lang):
    p = Pen(W, H, seed=109)
    p.rect(70, 110, 540, 470, r=18, fill=BLUE_WASH)
    p.line(70, 220, 610, 220, w=2.4)
    p.line(70, 408, 610, 408, w=2.4)
    p.text(340, 186, t['uml_class'], 46)
    for i, line in enumerate(t['uml_attrs']):
        p.mono(340, 278 + i * 52, line, 26)
    for i, line in enumerate(t['uml_methods']):
        p.mono(340, 472 + i * 52, line, 26)
    p.text(340, 646, t['uml_legend'], 26, MUTED)

    tags = ((t['uml_name'], 166), (t['uml_state'], 312), (t['uml_does'], 490))
    for (tag, y), code in zip(tags, t['uml_code']):
        p.arrow(622, y, 940, y)
        p.text(781, y - 26, tag, 26, MUTED)
        p.mono(970, y + 12, code, 30, BLUE, anchor='start')
    return p


def array_memory(t, lang):
    # Contiguous cells, the index under each, and one cell past the end that the
    # language will happily let you read.
    p = Pen(W, H, seed=139)
    values = ('78', '85', '91', '64', '73', '88')
    p.mono(240, 246, t['am_name'], 34, BLUE, anchor='start')
    for i, v in enumerate(values):
        x = 240 + i * 170
        p.rect(x, 290, 155, 130, r=14, fill=BLUE_WASH)
        p.mono(x + 78, 372, v, 38)
        p.mono(x + 78, 480, str(i), 30, BLUE)
    x = 240 + len(values) * 170
    p.rect(x, 290, 155, 130, r=14)
    p.cross(x + 78, 355, r=30)
    p.mono(x + 78, 480, str(len(values)), 30, MUTED)
    p.text(W / 2, 560, t['am_index'], 28, MUTED)
    p.text(W / 2, 660, t['am_note'], 28, MUTED)
    return p


def pointer(t, lang):
    # A variable, its address, and the second variable that holds that address.
    p = Pen(W, H, seed=149)
    p.rect(240, 300, 280, 150, r=20, fill=BLUE_WASH)
    p.mono(380, 396, t['ptr_value'], 46)
    p.mono(380, 268, t['ptr_var'], 34, BLUE)
    p.mono(380, 500, t['ptr_addr'], 28, MUTED)

    p.rect(1000, 300, 340, 150, r=20, fill=YELLOW_WASH)
    p.mono(1170, 396, t['ptr_addr'], 38)
    p.mono(1170, 268, t['ptr_ptr'], 34, BLUE)

    p.arrow(990, 375, 530, 375)
    p.text(760, 344, t['ptr_deref'], 26, MUTED)
    p.text(W / 2, 620, t['ptr_holds'], 30, MUTED)
    return p


def stack_vs_heap(t, lang):
    # Automatic storage against dynamic, and where each lifetime ends.
    p = Pen(W, H, seed=151)
    p.line(W / 2, 90, W / 2, 640, w=2.0, color=MUTED)

    p.text(420, 150, t['sh_stack'], 38, BLUE)
    p.mono(420, 208, t['sh_auto'], 26, MUTED)
    for i in range(3):
        y = 270 + i * 96
        fill = BLUE_WASH if i == 1 else None
        p.rect(240, y, 360, 80, r=14, fill=fill)
    p.mono(420, 412, '42', 34)
    p.text(420, 600, t['sh_auto_note'], 26, MUTED)

    p.text(1260, 150, t['sh_heap'], 38, BLUE)
    p.mono(1260, 208, t['sh_dyn'], 26, MUTED)
    p.rect(940, 270, 200, 80, r=14, fill=BLUE_WASH)
    p.mono(1040, 322, 'p', 30)
    p.rect(1330, 380, 220, 110, r=18, fill=YELLOW_WASH)
    p.mono(1440, 452, '42', 40)
    p.arrow(1145, 315, 1325, 410)
    p.text(1260, 600, t['sh_dyn_note'], 26, MUTED)
    p.text(W / 2, 680, t['sh_leak'], 26, MUTED)
    return p


def vtable(t, lang):
    # One call site, the table it goes through, and the row the real type picks.
    p = Pen(W, H, seed=157)
    p.rect(90, 300, 380, 130, r=20, fill=BLUE_WASH)
    p.mono(280, 378, t['vt_call'], 32)

    p.rect(700, 200, 520, 340, r=22)
    p.text(960, 262, t['vt_table'], 32, BLUE)
    p.line(700, 292, 1220, 292, w=2.0, color=MUTED)
    for i, row in enumerate(t['vt_rows']):
        y = 316 + i * 74
        if i == 1:
            p.rect(720, y, 480, 62, r=14, fill=YELLOW_WASH)
        p.mono(960, y + 42, row, 28)

    p.arrow(480, 365, 690, 365)
    # short arrow and a centred label: anchored at the arrow head the text ran
    # off the right edge of the canvas
    p.arrow(1230, 421, 1330, 421)
    p.text(1505, 421, t['vt_real'], 24, MUTED)
    p.text(W / 2, 660, t['vt_note'], 28, MUTED)
    return p


def value_vs_reference(t, lang):
    # The whole of week 5 in one drawing: on the left the parameter is a second
    # box, on the right it is a second name for the first box.
    p = Pen(W, H, seed=137)
    p.line(W / 2, 90, W / 2, 640, w=2.0, color=MUTED)

    def box(cx, value, tag):
        p.rect(cx - 110, 300, 220, 140, r=20, fill=BLUE_WASH)
        p.mono(cx, 390, value, 44)
        p.mono(cx, 268, tag, 30, BLUE)

    p.text(420, 140, t['vr_by_value'], 38, BLUE)
    p.mono(420, 196, t['vr_sig_value'], 26, MUTED)
    box(230, '10', t['vr_caller'])
    box(620, '20', 'n')
    p.arrow(345, 370, 505, 370)
    p.text(425, 342, t['vr_copy'], 26, MUTED)
    p.text(420, 560, t['vr_note_value'], 28, MUTED)

    p.text(1260, 140, t['vr_by_ref'], 38, BLUE)
    p.mono(1260, 196, t['vr_sig_ref'], 26, MUTED)
    p.rect(1150, 300, 220, 140, r=20, fill=YELLOW_WASH)
    p.mono(1260, 390, '20', 44)
    # the two arrows land on separate points of the top edge; aiming both at the
    # centre puts the two heads on top of each other and reads as a scribble
    for tx, tag, landing in ((1060, t['vr_caller'], 1190), (1460, 'n', 1330)):
        p.mono(tx, 236, tag, 30, BLUE)
        p.arrow(tx, 254, landing, 292)
    p.text(1260, 560, t['vr_note_ref'], 28, MUTED)
    return p


def access_levels_cpp(t, lang):
    # Not a relabel of access_levels. In Python only the private level is
    # enforced and protected is an agreement, so that drawing has one cross. In
    # C++ the compiler enforces all three, and the difference between protected
    # and private is who is asking, which needs the second column.
    p = Pen(W, H, seed=127)

    p.rect(70, 120, 620, 500, r=26)
    p.text(380, 192, t['acc_class'], 46)
    p.line(70, 228, 690, 228, w=2.0, color=MUTED)

    rows = (('public', t['cpp_acc_pub'], BLUE_WASH, True, True),
            ('protected', t['cpp_acc_prot'], None, False, True),
            ('private', t['cpp_acc_priv'], YELLOW_WASH, False, False))

    p.text(900, 196, t['cpp_from_outside'], 30, BLUE)
    p.text(1330, 196, t['cpp_from_child'], 30, BLUE)
    p.line(1115, 232, 1115, 600, w=1.6, color=MUTED)

    def tick(cx, cy):
        p.line(cx - 22, cy + 2, cx - 6, cy + 20, w=3.2)
        p.line(cx - 6, cy + 20, cx + 24, cy - 20, w=3.2)

    for i, (keyword, member, wash, from_outside, from_child) in enumerate(rows):
        y = 255 + i * 120
        cy = y + 50
        p.rect(110, y, 540, 100, r=18, fill=wash)
        p.mono(150, cy + 12, keyword, 30, BLUE, anchor='start')
        p.mono(430, cy + 12, member, 32, anchor='start')
        for cx, allowed in ((900, from_outside), (1330, from_child)):
            if allowed:
                tick(cx, cy)
            else:
                p.cross(cx, cy, r=22)

    p.text(W / 2, 690, t['cpp_acc_note'], 28, MUTED)
    return p


def uml_class_cpp(t, lang):
    # uml_class wires each compartment to the line of Python it becomes. The
    # notation is language independent; the three code lines are not.
    p = Pen(W, H, seed=131)
    p.rect(70, 110, 540, 470, r=18, fill=BLUE_WASH)
    p.line(70, 220, 610, 220, w=2.4)
    p.line(70, 408, 610, 408, w=2.4)
    p.text(340, 186, t['uml_class'], 46)
    for i, line in enumerate(t['cpp_uml_attrs']):
        p.mono(340, 278 + i * 52, line, 26)
    for i, line in enumerate(t['uml_methods']):
        p.mono(340, 472 + i * 52, line, 26)
    p.text(340, 646, t['uml_legend'], 26, MUTED)

    tags = ((t['uml_name'], 166), (t['uml_state'], 312), (t['uml_does'], 490))
    for (tag, y), code in zip(tags, t['cpp_uml_code']):
        p.arrow(622, y, 940, y)
        p.text(781, y - 26, tag, 26, MUTED)
        p.mono(970, y + 12, code, 30, BLUE, anchor='start')
    return p


def hierarchy(t, lang):
    p = Pen(W, H, seed=113)
    p.line(W / 2, 90, W / 2, 630, w=2.0, color=MUTED)

    p.rect(320, 150, 240, 96, r=18, fill=BLUE_WASH)
    p.mono(440, 210, 'Stream', 34)
    for i, name in enumerate(('FileStream', 'NetworkStream', 'MemoryStream')):
        x = 40 + i * 280
        p.rect(x, 380, 230, 96, r=18, fill=YELLOW_WASH)
        p.mono(x + 115, 438, name, 22)
        p.line(440, 250, x + 115, 376, w=2.2)
    p.text(420, 690, t['hier_good'], 28, MUTED)

    for i, name in enumerate((t['hier_a'], t['hier_b'], t['hier_c'])):
        y = 130 + i * 160
        p.rect(1000, y, 280, 90, r=18, fill=BLUE_WASH if i < 2 else YELLOW_WASH)
        p.text(1140, y + 58, name, 36)
        if i:
            p.arrow(1140, y - 66, 1140, y - 6)
    p.line(1284, 335, 1372, 335, w=2.2)
    p.mono(1442, 346, t['hier_fly'], 28, BLUE)
    p.wave(1442, 374, 1442, 458, amp=7)
    p.cross(1442, 492, r=26)
    p.text(1240, 690, t['hier_bad'], 28, MUTED)
    return p


def polymorphism(t, lang):
    p = Pen(W, H, seed=127)
    p.rect(70, 268, 470, 190, r=20, fill=BLUE_WASH)
    p.mono(305, 348, t['poly_loop'], 26)
    p.mono(305, 414, t['poly_call'], 30)

    call = 'hablar()' if lang == 'es' else 'talk()'
    kinds = ((t['poly_dog'], t['poly_woof']), (t['poly_cat'], t['poly_meow']),
             (t['poly_dog'], t['poly_woof']))
    for i, (name, sound) in enumerate(kinds):
        y = 150 + i * 210
        p.arrow(552, 362, 692, y, wavy=True)
        p.ellipse(820, y, 122, 68, fill=YELLOW_WASH if i == 1 else BLUE_WASH)
        p.mono(820, y + 10, f'{name}.{call}', 21)
        p.arrow(950, y, 1084, y)
        p.bubble(1270, y, 300, 108, fill=PAPER)
        p.text(1270, y + 14, sound, 38)
    p.text(W / 2, 692, t['poly_note'], 28, MUTED)
    return p


def recursion(t, lang):
    p = Pen(W, H, seed=149)
    calls = ('factorial(4)', 'factorial(3)', 'factorial(2)', 'factorial(1)')
    rets = ('4 * 6 = 24', '3 * 2 = 6', '2 * 1 = 2', t['base_case'])
    last = len(calls) - 1
    for i, (call, ret) in enumerate(zip(calls, rets)):
        x, y = 210, 96 + i * 116
        p.rect(x + i * 86, y, 500, 88, r=18,
               fill=YELLOW_WASH if i == last else BLUE_WASH)
        p.mono(x + i * 86 + 250, y + 56, call, 30)
        p.mono(1560, y + 56, ret, 28, INK if i == last else BLUE, anchor='end')
    p.arrow(122, 118, 122, 512)
    p.text(122, 566, t['down'], 28, MUTED)
    p.arrow(1622, 512, 1622, 118)
    p.text(1622, 566, t['up'], 28, MUTED)
    p.text(W / 2, 682, t['rec_note'], 28, MUTED)
    return p


def file_lifecycle(t, lang):
    p = Pen(W, H, seed=151)
    for i, step in enumerate((t['fl_open'], t['fl_work'], t['fl_close'])):
        x = 130 + i * 500
        p.rect(x, 130, 380, 120, r=20, fill=YELLOW_WASH if i == 2 else BLUE_WASH)
        p.mono(x + 190, 202, step, 28)
        if i < 2:
            p.arrow(x + 396, 190, x + 486, 190)
    p.bracket(130, 1510, 286, depth=40)
    p.mono(820, 400, t['fl_with'], 34, BLUE)
    p.text(820, 456, t['fl_auto'], 28, MUTED)

    p.line(130, 520, 1510, 520, w=2.0, color=MUTED)
    p.text(450, 592, t['fl_good'], 30)
    p.text(1150, 592, t['fl_bad'], 30)
    p.cross(1470, 584, r=24)
    p.text(W / 2, 686, t['fl_note'], 26, MUTED)
    return p


def seek_tell(t, lang):
    p = Pen(W, H, seed=157)
    n, cw, x0, y0, ch = 12, 110, 180, 250, 120
    data = t['st_data']
    for i in range(n):
        x = x0 + i * cw
        p.rect(x, y0, cw, ch, r=10, fill=YELLOW_WASH if i == 7 else None)
        p.mono(x + cw / 2, y0 + 80, data[i] if i < len(data) else ' ', 40)
        p.mono(x + cw / 2, y0 - 28, str(i), 24, BLUE)

    start, target = x0 + cw / 2, x0 + 7 * cw + cw / 2
    p.line(start, y0 - 62, start, 168, w=2.4)
    p.line(start, 168, target, 168, w=2.4)
    p.arrow(target, 168, target, y0 - 14)
    p.mono((start + target) / 2, 126, 'f.seek(7)', 32, BLUE)

    for i in range(7):
        xa = x0 + i * cw + cw / 2
        p.arrow(xa + 16, 442, xa + cw - 16, 442, head=11)
    p.mono(600, 508, 'f.read(1)', 30, MUTED)
    p.text(600, 566, t['sequential'], 28, MUTED)

    p.arrow(target, 476, target, 386)
    p.mono(target + 60, 490, 'f.tell() == 7', 28, BLUE, anchor='start')
    p.text(W / 2, 686, t['st_note'], 28, MUTED)
    return p


def event_loop(t, lang):
    p = Pen(W, H, seed=163)
    p.rect(70, 232, 280, 156, r=20, fill=YELLOW_WASH)
    p.text(210, 322, t['el_user'], 30)
    p.arrow(362, 310, 448, 310)

    stages = (t['el_queue'], t['el_dispatch'], t['el_slot'])
    for i, stage in enumerate(stages):
        x = 460 + i * 400
        p.rect(x, 232, 300, 156, r=20, fill=BLUE_WASH)
        p.text(x + 150, 322, stage, 29)
        if i < 2:
            p.arrow(x + 314, 310, x + 386, 310)

    # the return leg: the loop goes back to waiting, it does not stop
    p.line(1410, 400, 1410, 508, w=2.4)
    p.line(1410, 508, 610, 508, w=2.4)
    p.arrow(610, 508, 610, 400)
    p.text(1030, 566, t['el_back'], 28, MUTED)
    p.text(W / 2, 682, t['el_note'], 28, MUTED)
    return p


def layouts(t, lang):
    p = Pen(W, H, seed=167)
    names = ('QHBoxLayout', 'QVBoxLayout', 'QGridLayout')
    for i, name in enumerate(names):
        x, y = 90 + i * 550, 120
        p.rect(x, y, 400, 400, r=14)
        p.rect(x, y, 400, 52, r=14, fill=BLUE_WASH)
        ix, iy, iw, ih = x + 20, y + 72, 360, 308
        if i == 0:
            for c in range(3):
                p.rect(ix + c * 125, iy, 110, ih, r=10, fill=YELLOW_WASH)
                p.mono(ix + c * 125 + 55, iy + ih / 2 + 10, str(c + 1), 30)
        elif i == 1:
            for r in range(3):
                p.rect(ix, iy + r * 108, iw, 92, r=10, fill=YELLOW_WASH)
                p.mono(ix + iw / 2, iy + r * 108 + 58, str(r + 1), 30)
        else:
            p.rect(ix, iy, 172, 140, r=10, fill=YELLOW_WASH)
            p.mono(ix + 86, iy + 88, '0,0', 26)
            p.rect(ix, iy + 168, 172, 140, r=10, fill=YELLOW_WASH)
            p.mono(ix + 86, iy + 256, '1,0', 26)
            p.rect(ix + 188, iy, 172, 308, r=10, fill=BLUE_WASH)
            p.mono(ix + 274, iy + 164, '0,1', 26)
        p.mono(x + 200, y + 470, name, 28, BLUE)
    p.text(W / 2, 682, t['lay_note'], 28, MUTED)
    return p


def db_access(t, lang):
    p = Pen(W, H, seed=173)
    p.rect(60, 258, 280, 160, r=20, fill=BLUE_WASH)
    p.text(200, 348, t['db_prog'], 30)
    p.arrow(352, 338, 486, 338)
    p.mono(419, 300, 'connect()', 24, BLUE)

    cx, rx = 640, 130
    p.ellipse(cx, 226, rx, 44, fill=YELLOW_WASH)
    p.line(cx - rx, 226, cx - rx, 430, w=2.4)
    p.line(cx + rx, 226, cx + rx, 430, w=2.4)
    p.ellipse(cx, 430, rx, 44, fill=YELLOW_WASH)
    p.mono(cx, 340, t['db_file'], 28)
    p.text(cx, 528, t['db_commit'], 26, MUTED)

    p.arrow(786, 338, 926, 338)
    p.mono(856, 300, 'execute(SQL)', 24, BLUE)
    p.rect(940, 258, 260, 160, r=20, fill=BLUE_WASH)
    p.mono(1070, 348, t['db_cursor'], 30)

    p.arrow(1212, 338, 1332, 338)
    for i, row in enumerate(('(1, Toy Story)', '(2, Up)', '(3, Coco)')):
        p.rect(1350, 250 + i * 62, 270, 52, r=10)
        p.mono(1485, 286 + i * 62, row, 22)
    p.text(W / 2, 682, t['db_note'], 28, MUTED)
    return p


def cpp_timeline(t, lang):
    p = Pen(W, H, seed=181)
    y = 372
    p.line(110, y, 1520, y, w=2.6)
    p.arrow(1520, y, 1576, y)
    for i, (year, label) in enumerate(t['tl']):
        x = 176 + i * 268
        last = i == len(t['tl']) - 1
        p.ellipse(x, y, 19, 19, fill=YELLOW_WASH if last else BLUE_WASH)
        up = i % 2 == 0
        p.line(x, y - 19 if up else y + 19, x, y - 74 if up else y + 74, w=2.0)
        p.mono(x, y - 96 if up else y + 128, year, 34, BLUE)
        p.text(x, y - 146 if up else y + 178, label, 27)
    p.text(W / 2, 682, t['tl_note'], 28, MUTED)
    return p


def compilation(t, lang):
    p = Pen(W, H, seed=191)
    boxes = ((t['cc_src'], t['cc_write']), (t['cc_obj'], t['cc_mid']),
             (t['cc_exe'], t['cc_out']))
    for i, (name, sub) in enumerate(boxes):
        x = 180 + i * 520
        p.rect(x, 226, 280, 150, r=20,
               fill=YELLOW_WASH if i == 2 else BLUE_WASH)
        p.mono(x + 140, 300, name, 30)
        p.text(x + 140, 424, sub, 25, MUTED)
        if i < 2:
            ax = x + 296                     # a 224 px gap, so the label fits in it
            p.arrow(ax + 18, 300, ax + 206, 300)
            p.mono(ax + 112, 258, t[f'cc_step{i + 1}'], 26, BLUE)
            p.text(ax + 112, 348, t[f'cc_sub{i + 1}'], 23, MUTED)
    p.text(W / 2, 626, t['cc_note'], 28, MUTED)
    return p



def flow_symbols(t, lang):
    # The nine symbols the four basic ones leave out. Three rows of three, each
    # drawn at the same size so the shapes are what tells them apart.
    p = Pen(W, H, seed=211)
    cols = (300, 840, 1380)
    rows = (128, 358, 588)
    bw, bh = 300, 74

    def caption(cx, cy, name, meaning):
        p.text(cx, cy + 74, name, 30, BLUE)
        p.text(cx, cy + 116, meaning, 24, MUTED)

    # 1 · predefined process
    cx, cy = cols[0], rows[0]
    p.rect(cx - bw / 2, cy - bh / 2, bw, bh, r=10, fill=BLUE_WASH)
    p.line(cx - bw / 2 + 26, cy - bh / 2, cx - bw / 2 + 26, cy + bh / 2)
    p.line(cx + bw / 2 - 26, cy - bh / 2, cx + bw / 2 - 26, cy + bh / 2)
    p.mono(cx, cy + 10, t['fs_call'], 24)
    caption(cx, cy, t['fs_sub'], t['fs_sub_e'])

    # 2 · preparation, the hexagon
    cx, cy = cols[1], rows[0]
    hx = bw / 2
    p.poly([(cx - hx + 40, cy - bh / 2), (cx + hx - 40, cy - bh / 2), (cx + hx, cy),
            (cx + hx - 40, cy + bh / 2), (cx - hx + 40, cy + bh / 2), (cx - hx, cy)],
           fill=BLUE_WASH)
    p.mono(cx, cy + 10, t['fs_loop'], 24)
    caption(cx, cy, t['fs_prep'], t['fs_prep_e'])

    # 3 · on-page connector
    cx, cy = cols[2], rows[0]
    p.ellipse(cx, cy, 46, 42, w=3.0, fill=YELLOW_WASH)
    p.text(cx, cy + 14, 'A', 40)
    caption(cx, cy, t['fs_conn'], t['fs_conn_e'])

    # 4 · off-page connector
    cx, cy = cols[0], rows[1]
    p.poly([(cx - 110, cy - bh / 2), (cx + 110, cy - bh / 2), (cx + 110, cy + 8),
            (cx, cy + bh / 2 + 16), (cx - 110, cy + 8)], fill=YELLOW_WASH)
    p.mono(cx, cy + 4, t['fs_page'], 24)
    caption(cx, cy, t['fs_off'], t['fs_off_e'])

    # 5 · stored data, the cylinder. Two flat ellipses and two sides, the way
    # db_access draws it, so the shape stays inside its row.
    cx, cy = cols[1], rows[1]
    top, bot = cy - bh / 2 + 6, cy + bh / 2 - 6
    p.ellipse(cx, top, 118, 15, fill=BLUE_WASH)
    p.line(cx - 118, top, cx - 118, bot)
    p.line(cx + 118, top, cx + 118, bot)
    p.ellipse(cx, bot, 118, 15, fill=BLUE_WASH)
    p.mono(cx, cy + 10, t['fs_file'], 24)
    caption(cx, cy, t['fs_db'], t['fs_db_e'])

    # 6 · document
    cx, cy = cols[2], rows[1]
    p.line(cx - 130, top, cx + 130, top)
    p.line(cx - 130, top, cx - 130, bot)
    p.line(cx + 130, top, cx + 130, bot)
    p.wave(cx - 130, bot, cx + 130, bot, amp=11, cycles=1)
    p.mono(cx, cy + 6, t['fs_rep'], 24)
    caption(cx, cy, t['fs_doc'], t['fs_doc_e'])

    # 7 · manual input
    cx, cy = cols[0], rows[2]
    p.poly([(cx - 130, cy - bh / 2 + 20), (cx + 130, cy - bh / 2),
            (cx + 130, cy + bh / 2), (cx - 130, cy + bh / 2)], fill=BLUE_WASH)
    p.mono(cx, cy + 14, t['fs_field'], 24)
    caption(cx, cy, t['fs_min'], t['fs_min_e'])

    # 8 · display
    cx, cy = cols[1], rows[2]
    p.poly([(cx - 90, cy - bh / 2), (cx + 110, cy - bh / 2), (cx + 145, cy),
            (cx + 110, cy + bh / 2), (cx - 90, cy + bh / 2),
            (cx - 128, cy + bh / 4), (cx - 140, cy),
            (cx - 128, cy - bh / 4)], fill=BLUE_WASH)
    p.mono(cx + 6, cy + 10, t['fs_out'], 24)
    caption(cx, cy, t['fs_disp'], t['fs_disp_e'])

    # 9 · manual operation
    cx, cy = cols[2], rows[2]
    p.poly([(cx - 140, cy - bh / 2), (cx + 140, cy - bh / 2),
            (cx + 100, cy + bh / 2), (cx - 100, cy + bh / 2)], fill=BLUE_WASH)
    p.mono(cx, cy + 10, t['fs_ok'], 24)
    caption(cx, cy, t['fs_mop'], t['fs_mop_e'])
    return p


def flow_connector(t, lang):
    # A chart that outgrew its page, cut in two with a lettered circle.
    p = Pen(W, H, seed=233)
    lx, rx = 430, 1230
    p.line(W / 2, 60, W / 2, H - 90, w=2.0, color=MUTED)

    p.text(lx, 74, t['fc_left'], 28, MUTED)
    p.text(rx, 74, t['fc_right'], 28, MUTED)

    p.rhomboid(lx, 160, 300, 74, fill=BLUE_WASH)
    p.mono(lx, 170, t['fc_read'], 26)
    p.arrow(lx, 200, lx, 246)

    p.diamond(lx, 310, 170, 62, fill=YELLOW_WASH)
    p.mono(lx, 320, t['fc_valid'], 26)
    p.arrow(lx, 374, lx, 420)

    p.rect(lx - 150, 420, 300, 74, r=10, fill=BLUE_WASH)
    p.mono(lx, 466, t['fc_clean'], 26)
    p.arrow(lx, 496, lx, 542)

    p.ellipse(lx, 588, 46, 42, w=3.0, fill=YELLOW_WASH)
    p.text(lx, 602, 'A', 40)

    p.ellipse(rx, 160, 46, 42, w=3.0, fill=YELLOW_WASH)
    p.text(rx, 174, 'A', 40)
    p.arrow(rx, 204, rx, 250)

    p.rect(rx - 150, 250, 300, 74, r=10, fill=BLUE_WASH)
    p.mono(rx, 296, t['fc_group'], 26)
    p.arrow(rx, 326, rx, 372)

    p.rhomboid(rx, 410, 300, 74, fill=BLUE_WASH)
    p.mono(rx, 420, t['fc_write'], 26)
    p.arrow(rx, 450, rx, 496)

    p.rect(rx - 110, 496, 220, 70, r=34, fill=YELLOW_WASH)
    p.text(rx, 540, t['fc_end'], 32)

    p.text(W / 2, H - 40, t['fc_note'], 26, MUTED)
    return p


FIGURES = {
    'flow-symbols': dict(
        fn=flow_symbols, size='21:9',
        about='The nine flowchart symbols the basic four leave out, each with what it '
              'means: predefined process, preparation, the two connectors, stored data, '
              'document, manual input, display and manual operation.',
        reuse='The three input and output shapes carry the week 5 distinction between '
              'what a person types, what the machine computes and what reaches the '
              'screen. Relabel the boxes for any example.',
        used_by=['w02']),
    'flow-connector': dict(
        fn=flow_connector, size='21:9',
        about='How a flowchart too long for one page gets cut with a lettered circle, '
              'and picked up again at the matching circle.',
        reuse='Any long process diagram. The point is that the circle is not a step, '
              'which is what students assume the first time they meet it.',
        used_by=['w02']),
    'slicing': dict(
        fn=slicing, size='21:9',
        about='Why course[0:3] returns three characters, with the positive and negative '
              'index rulers lined up on the same tiles.',
        reuse='Strings and lists share the rule, so the one drawing serves the string '
              'slide and the list slide. Change the word in the tiles for any example.',
        used_by=['w01.1']),
    'scope': dict(
        fn=scope, size='21:9',
        about='Local against global, and exactly what raises NameError.',
        reuse='Week 3 reuses it: relabel the jar "self" and the same drawing explains why '
              'an attribute outlives a call and a local does not.',
        used_by=['w01.1']),
    'reference-vs-copy': dict(
        fn=reference_vs_copy, size='21:9',
        about='Aliasing. Two tags on one box against two tags on two boxes.',
        reuse='The single most common surprise in the review quiz, and the same mechanism '
              'as the shared class attribute in week 3.',
        used_by=['w01.1']),
    'collections': dict(
        fn=collections, size='21:9',
        about='The four containers, each captioned with the property that separates it '
              'from the other three.',
        reuse='The table on the same slide carries the syntax; this carries the choice. '
              'Any language with the same four structures.',
        used_by=['w01.1']),
    'exceptions': dict(
        fn=exceptions, size='16:9',
        about='One except per type, and where the else clause sits in the flow.',
        reuse='Week 11 covers exceptions properly and opens with the same drawing.',
        used_by=['w01.1']),
    'paradigms': dict(
        fn=paradigms, size='21:9',
        about='Object orientation as one paradigm among six, rather than the only way to '
              'write a program.',
        reuse='Opens the paradigm session of every language course in the academy, '
              'unchanged.',
        used_by=['w02']),
    'parallel-lists': dict(
        fn=parallel_lists, size='21:9',
        about='The failure that makes objects worth the extra lines: delete one student '
              'and four parallel lists go out of step, while three objects do not.',
        reuse='This is the argument of the whole paradigm session, and it is structural, '
              'so it holds in any language.',
        used_by=['w02']),
    'class-object': dict(
        fn=class_object, size='21:9',
        about='Class, constructor, objects, with the cutter-and-cookies analogy drawn out.',
        reuse='The same analogy is already in docs/02-oop.md, so the drawing and the '
              'written notes reinforce each other.',
        used_by=['w03']),
    'class-vs-instance': dict(
        fn=class_vs_instance, size='21:9',
        about='One list on the class shared by every object, against one list per object.',
        reuse='Show it next to reference-vs-copy: same mechanism, one wearing a class '
              'costume.',
        used_by=['w03']),
    'access-levels': dict(
        fn=access_levels, size='21:9',
        about='What actually happens when outside code reaches for a public, a protected '
              'and a private attribute, and which of the three Python enforces.',
        reuse='Week 6 opens the encapsulation block with it. Any language with three '
              'access levels can use the same drawing by relabelling the three rows.',
        used_by=['w04', 'w06']),
    'array-memory': dict(
        fn=array_memory, size='21:9',
        about='Contiguous cells with the index written under each, and one cell past the '
              'end that nothing stops you reading.',
        reuse='Week 10 opens with it. The same drawing explains why the first index is '
              'zero and why the last one is size minus one, which is the same off-by-one '
              'twice.',
        used_by=['w10']),
    'pointer': dict(
        fn=pointer, size='21:9',
        about='A variable, its address, and the second variable that holds that address.',
        reuse='Week 12. Show it beside value-vs-reference: a reference is another name for '
              'the box, a pointer is a box holding where the first one lives.',
        used_by=['w12']),
    'stack-vs-heap': dict(
        fn=stack_vs_heap, size='21:9',
        about='Automatic storage against dynamic, with the pointer on the stack and the '
              'object it owns on the heap, and where each lifetime ends.',
        reuse='Week 12 needs it for new and delete. It is also the picture behind the leak: '
              'the left box disappears on its own, the right one does not.',
        used_by=['w12']),
    'vtable': dict(
        fn=vtable, size='21:9',
        about='One call site, the table the call goes through, and the row the real type '
              'picks out.',
        reuse='Week 12, once virtual is on the board. Pair it with polymorphism: one '
              'drawing is what the caller sees, this one is what actually happens.',
        used_by=['w12']),
    'value-vs-reference': dict(
        fn=value_vs_reference, size='21:9',
        about='The same argument passed both ways, with the copy drawn on one side and '
              'the second name for one box on the other.',
        reuse='Week 5 turns on this one drawing. It is also the picture to point back at '
              'in week 12, when the pointer arrives and the question becomes which of the '
              'three a parameter should be.',
        used_by=['w05']),
    'scope-cpp': dict(
        fn=scope_cpp, size='21:9',
        about='Local against global, and the error C++ gives for reaching a name that '
              'went out of scope.',
        reuse='The COM103 twin of scope. The nesting is identical; only the label on the '
              'blocked arrow changes, because C++ refuses the name at compile time with '
              'C2065 where Python raises NameError while running.',
        used_by=['w05']),
    'access-levels-cpp': dict(
        fn=access_levels_cpp, size='21:9',
        about='Which of public, protected and private can be reached from outside the '
              'class and from a derived class, with the compiler enforcing all three.',
        reuse='Not a relabel of access-levels. Python enforces one of the three levels '
              'and treats protected as an agreement, so that drawing carries a single '
              'cross. Here the second column is the whole point: protected is the level '
              'a child can reach and an outsider cannot.',
        used_by=['w06', 'w09']),
    'uml-class-cpp': dict(
        fn=uml_class_cpp, size='21:9',
        about='The three compartments of a UML class box, each wired to the line of C++ '
              'it turns into.',
        reuse='The COM103 twin of uml-class. The notation is language independent, the '
              'three code lines beside it are not.',
        used_by=['w06']),
    'uml-class': dict(
        fn=uml_class, size='21:9',
        about='The three compartments of a UML class box, each wired to the line of '
              'Python it turns into.',
        reuse='Week 5 models with it and week 16 reuses it when the model becomes a '
              'table. The notation is language independent, so every course can borrow it.',
        used_by=['w05']),
    'hierarchy': dict(
        fn=hierarchy, size='21:9',
        about='A two-level tree that works beside a four-level chain that produces a '
              'chicken which inherits fly().',
        reuse='The argument for keeping inheritance shallow, and it is structural, so it '
              'holds in any language with classes.',
        used_by=['w07']),
    'polymorphism': dict(
        fn=polymorphism, size='21:9',
        about='One call site sending the same message to three objects and getting three '
              'answers back, chosen by the real type.',
        reuse='Week 8 opens with it. Pair it with hierarchy: one drawing is the tree, the '
              'other is what the tree buys you.',
        used_by=['w08']),
    'recursion': dict(
        fn=recursion, size='21:9',
        about='The call stack of factorial(4): four frames going down to the base case, and '
              'the result assembled on the way back up.',
        reuse='Any recursive example fits by relabelling the four frames. The shape of the '
              'drawing is the shape of the mechanism.',
        used_by=['w09']),
    'file-lifecycle': dict(
        fn=file_lifecycle, size='21:9',
        about='Open, work, close, and the with block that does the first and the last for '
              'you even when the middle raises.',
        reuse='Week 16 reuses it for database connections, which have exactly the same '
              'lifecycle and the same failure mode.',
        used_by=['w12']),
    'seek-tell': dict(
        fn=seek_tell, size='21:9',
        about='One cursor over a file laid out as numbered positions: reading walks it one '
              'step at a time, seek jumps it, tell reports where it stopped.',
        reuse='The difference between sequential and random access, drawn once. Same '
              'drawing works for a text file, a binary file or a database page.',
        used_by=['w13']),
    'event-loop': dict(
        fn=event_loop, size='21:9',
        about='Why a GUI program looks idle: exec() is a loop that waits, dispatches one '
              'event to one function, and goes back to waiting.',
        reuse='Any event-driven toolkit has this shape, so the drawing holds for Qt, for '
              'the web and for a game loop.',
        used_by=['w14']),
    'layouts': dict(
        fn=layouts, size='21:9',
        about='The same three widgets under a horizontal box, a vertical box and a grid, '
              'with the grid cell coordinates written in.',
        reuse='Week 15 builds on it. The three arrangements are the same in Qt, in Tk and '
              'in CSS, only the class names change.',
        used_by=['w15']),
    'db-access': dict(
        fn=db_access, size='21:9',
        about='The path a query takes: connection, execute, cursor, rows, and where commit '
              'has to happen for a write to survive.',
        reuse='Pair it with file-lifecycle: a connection is opened, used and closed exactly '
              'like a file, and forgetting the close costs the same.',
        used_by=['w16']),
    'cpp-timeline': dict(
        fn=cpp_timeline, size='21:9',
        about='Forty years of C++ on one line, from C in 1972 to the standard this '
              'course pins, with the three-year release cadence visible at the right end.',
        reuse='Opens COM103. Relabel the six stops and it serves any language that has a '
              'history worth telling.',
        used_by=['w00']),
    'compilation': dict(
        fn=compilation, size='21:9',
        about='Source, object file, executable, with the compiler and the linker named on '
              'the arrows and the standard library entering at the second one.',
        reuse='The figure that explains what a compiled language is, so it belongs in the '
              'first session of any compiled-language course.',
        used_by=['w00', 'w01']),
}


# the ten computational thinking ideas, redrawn in the deck palette
from . import ct as _ct  # noqa: E402

for _name, (_fn, _about, _reuse) in _ct.SCENES.items():
    FIGURES[_name] = dict(fn=_fn, size='21:9', about=_about, reuse=_reuse,
                          used_by=['ct'])
T.update({k: {**v, **_ct.L[k]} for k, v in T.items()})


def build(name, lang, outdir, overwrite=False):
    spec = FIGURES[name]
    base = os.path.join(outdir, name)
    if os.path.exists(base + '.png') and not overwrite:
        print(f'  skip {name} ({lang})')
        return base + '.png'
    pen = spec['fn'](T[lang], lang)
    path = pen.save(base, title=name)
    print(f'  {name} ({lang})  {spec["size"]}  -> {os.path.relpath(path, outdir)}')
    return path


def catalogue(root):
    lines = [
        '# Figure catalogue', '',
        'Hand-sketched diagrams for the course decks, drawn by `kit/figures.py` on top of',
        '`kit/doodle.py`. They are drawn rather than generated by an image model, because',
        'a diagram whose label reads `ZeroDivisionErrar` is worse than no diagram. Labels',
        'are exact, the palette matches the slides, and the SVG is diffable in git.', '',
        '```bash',
        'python -m kit.figures --all              # both languages, skips what exists',
        'python -m kit.figures slicing --lang en --overwrite',
        '```', '',
        'Each figure lands in `ppts/img/<lang>/` as both `.svg` (the source of truth) and',
        '`.png` (what the deck embeds). They sit outside any one subject folder because',
        'most explain a language feature and get reused across sessions.', '',
        '| Figure | Ratio | Lessons | Files |', '|---|---|---|---|',
    ]
    for name, spec in FIGURES.items():
        have = [lg for lg in ('es', 'en')
                if os.path.exists(os.path.join(root, 'img', lg, f'{name}.png'))]
        lines.append(f'| `{name}` | {spec["size"]} | {", ".join(spec["used_by"])} | '
                     f'{", ".join(have) if have else "not built"} |')
    lines += ['', '---', '']
    for name, spec in FIGURES.items():
        lines += [f'## `{name}`', '',
                  f'![{name}](img/es/{name}.png)', '',
                  f'**Shows.** {spec["about"]}', '',
                  f'**Reuse.** {spec["reuse"]}', '',
                  f'**Ratio** {spec["size"]} · **lessons** {", ".join(spec["used_by"])} · '
                  f'**drawn by** `figures.{spec["fn"].__name__}`', '']
    return '\n'.join(lines)


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split('\n')[0])
    ap.add_argument('figure', nargs='?')
    ap.add_argument('--list', action='store_true')
    ap.add_argument('--all', action='store_true')
    ap.add_argument('--catalogue', action='store_true')
    ap.add_argument('--lang', default=None, choices=('es', 'en'))
    ap.add_argument('--overwrite', action='store_true')
    a = ap.parse_args(argv)

    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    if a.catalogue:
        # The catalogue carries the middle dot the decks use as a separator, and
        # on Windows a shell redirect writes stdout in the console codepage,
        # which turns every one of them into a replacement character. Write the
        # file here in UTF-8 rather than trusting the redirect.
        out = os.path.join(root, 'IMAGES.md')
        with open(out, 'w', encoding='utf-8', newline='\n') as fh:
            fh.write(catalogue(root) + '\n')
        print(f'wrote {os.path.relpath(out, root)}')
        return 0
    if a.list or (not a.figure and not a.all):
        print(f'{"figure":<22}{"ratio":>7}  lessons')
        for name, spec in FIGURES.items():
            print(f'  {name:<20}{spec["size"]:>7}  {", ".join(spec["used_by"])}')
        return 0

    names = list(FIGURES) if a.all else [a.figure]
    langs = [a.lang] if a.lang else ['es', 'en']
    for lang in langs:
        outdir = os.path.join(root, 'img', lang)
        print(f'{lang}:')
        for name in names:
            if name not in FIGURES:
                raise SystemExit(f'unknown figure {name!r}. Known: {", ".join(FIGURES)}')
            build(name, lang, outdir, a.overwrite)
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
