# CUADERNOS DE COLAB PARA COM102, LAS DIECISIETE SEMANAS QUE FALTAN

El curso de Análisis de Datos, TIA502, ya está terminado: veinte semanas, cuarenta cuadernos,
verificados. El de Programación Orientada a Objetos, COM102, va en dos de diecinueve. Tu encargo
es cerrarlo.

No vas a inventar el formato. Ya existe, está construido y hay cuarenta y cuatro cuadernos hechos
con él. Léelos antes de escribir el primero.

## LO QUE YA EXISTE

    notebooks/kit/nbkit.py          celdas markdown y de código, y el escritor de nbformat
    notebooks/kit/diagram.py        diagramas SVG embebidos, flujo y UML
    notebooks/kit/build.py          los módulos de lecciones se vuelven .ipynb
    notebooks/kit/verify.py         corre un cuaderno desde un directorio vacío
    notebooks/kit/lessons/          un módulo por semana por idioma, treinta y uno hasta hoy
    notebooks/analisis-de-datos/{es,en}/     veinte semanas, terminadas
    notebooks/programacion-orientada-a-objetos/{es,en}/   w01.1 y w01.2, terminadas

    cd notebooks
    python -m kit.build                  reconstruye los cuarenta y cuatro
    python -m kit.build poo_w01_3        solo ese
    python kit/verify.py programacion-orientada-a-objetos/es/w01.3.ipynb

`notebooks/kit/README.md` explica el resto. Los cuadernos de POO no llevan celda de arranque de
datos, porque no leen archivos; los de Análisis sí y por eso importan `bootstrap_cell`.

## QUÉ FALTA, Y DE DÓNDE SALE SU CÓDIGO

Diecisiete semanas, en los dos idiomas. Treinta y cuatro cuadernos.

    w01.3, w01.4, w01.5     repasos 3, 4 y 5 de los módulos de 01 - Basics
    w02 a w13               el curso, con w09 partida entre básicos y el proyecto de Hanoi
    w16, w17                SQLite, y repaso con examen final

Las semanas 14 y 15 no llevan cuaderno. Son PyQt6 y Colab no tiene pantalla. Eso quedó decidido
desde el encargo original y no se reabre.

La tabla de qué módulo alimenta cada semana está en `ppts/HANDOFF.md`, bajo "Where the code comes
from". Respétala: lo que el alumno ve en clase tiene que ser lo que puede clonar.

    4 a 8      02 - POO/6th Module/         Code019 a Code028, y MagicMethods.md
    9          01 - Basics/3rd-4th Module/  y 07 - Activities/Projects/02 - Hanoi Tower/
    10         01 - Basics/4th Module/      Code012, Code016, Code017
    11         01 - Basics/5th Module/Code028.py y 02 - POO/6th Module/Code026.py
    12         03 - Paths and Files/7th Module/  Code029 a Code035
    13         03 - Paths and Files/7th Module/Code34.py
    16         04 - SQLite/8th Module/Code036.py y 05 - GUI/9th Module/Code044.py

Los repasos w01.1 a w01.5 recorren los cinco módulos de `01 - Basics` en orden: datos y texto,
decisiones y ciclos, funciones, colecciones, errores. Los dos primeros ya están escritos.

**Corre cada archivo antes de citarlo.** `Code013.py` tiene un error real en la línea 31: llama a
`this_tuple.extend(...)` y las tuplas no tienen `extend`. El HANDOFF avisa que puede haber más, y
en Análisis aparecieron dos errores de deck que nadie había visto.

## QUÉ ES UN CUADERNO DE ESTE CURSO

No es la diapositiva pegada en celdas. La diapositiva tiene que caber en una pantalla y por eso su
código va recortado; el cuaderno no tiene esa restricción, y ahí está su razón de ser. Por cada
bloque que la diapositiva muestra, el cuaderno da la versión completa, la ejecuta, y añade las
variantes que no cupieron.

Alrededor de cinco veces el código del deck, contando el que ya estaba. No es relleno: cada celda
hace algo distinto. Mira `da_w15_2.py` o `poo_w01_2.py` para calibrar.

La estructura que siguen los cuarenta y cuatro:

1. Celda markdown de portada: curso, semana, tema, y qué va a poder hacer quien lo termine.
   Sale de los objetivos del deck. Cierra con una nota de cómo se usa el cuaderno.
2. Por cada bloque: una celda markdown que explica, y una o varias de código que se ejecutan.
3. Las anotaciones al margen del deck se vuelven comentarios en el código o texto arriba.
4. Los quizzes se vuelven "predice antes de correr": la pregunta con sus opciones en markdown, y
   debajo la celda que da la respuesta al ejecutarse, y después la explicación de por qué.
5. Ejercicios al final, de menos a más, con las soluciones en una celda markdown aparte hasta
   abajo para que no se vean de reojo. Ocho o nueve por cuaderno.

La prosa va con Humanizer. La va a leer un alumno sin nadie al lado, así que tiene que sonar a
alguien explicando y no a documentación generada. Frases con sujeto y verbo, sin relleno, diciendo
por qué importa cada cosa y no solo qué hace. Sin em dashes, nunca. Español mexicano neutro.

## LO QUE HACE BUENO A UN CUADERNO DE ESTOS

Tres cosas, y son las que separan los que quedaron bien de los que quedaron correctos.

**Las celdas que fallan a propósito.** Cinco o seis por cuaderno, cada una con un comentario que lo
dice. Van con `try/except` que imprime la excepción, porque un `raise` suelto detiene "Ejecutar
todo" en Colab y la barra de verificación es que el cuaderno corra de principio a fin. Las dos
restricciones se cumplen solo así.

Las mejores no son las que truenan, son las que **no** truenan. `unit_price.sum()` concatena 324
precios en un texto sin lanzar nada. `pago_mensual(0.18, 250000, 36)` devuelve 3,750.00, un pago
mensual perfectamente creíble calculado con el capital en el lugar de la tasa. Busca esas.

**Los números medidos, no afirmados.** Si la prosa dice una cifra, que la celda de al lado la
calcule. En Análisis eso cazó tres errores míos: escribí que noviembre iba arriba y no, dije
doscientos mil cuando eran 273,614, y afirmé "may" cuando la respuesta era "abr". La celda no se
equivoca y la prosa sí.

**Los hilos entre semanas.** El cuaderno dice a dónde va lo que está enseñando. En POO eso importa
más que en Análisis, porque el curso construye hacia las clases: el tipado dinámico de w01.1 es lo
que en la semana 3 explica por qué un atributo rompe un método, y el alias de listas del repaso 4
es lo que en la semana 6 explica por qué dos objetos comparten estado. Cóselos.

## LAS TRAMPAS QUE YA ESTÁN RESUELTAS

No las vuelvas a descubrir.

**`input()` detiene el cuaderno.** Una sola celda con `input` de verdad por cuaderno, marcada, con
un `try/except Exception` que cae a un valor de ejemplo. En Colab abre el cuadro; en verificación
headless lanza `StdinNotImplementedError` y pasa de largo. Todo lo demás usa valores asignados. Ve
`poo_w01_1.py` bloque 4.

**El ciclo infinito cuelga el kernel.** En clase se provoca con Control C a la mano; en cuaderno no
se puede. Va con un tope de seguridad y un `break`, y el tope es parte de la lección. Ve
`poo_w01_2.py` bloque 3.

**Colab no renderiza mermaid en celdas markdown.** Verificado. Si una semana necesita diagrama, usa
`notebooks/kit/diagram.py`, que genera SVG embebido como data URI: sin red, sin código, unos pocos
KB. Ya tiene las trece primitivas de flujo y las de UML, que es lo que POO va a querer para las
semanas 3 a 8. `uml_class_figure` y `uml_relations_figure` están hechas y probadas.

**El deck ya tiene figuras de UML.** `uml-class`, `uml-class-cpp`, `hierarchy` y `access-levels`
viven en `ppts/kit/figures.py`. No dupliques: si la semana ya cita una, el cuaderno puede rehacerla
con `diagram.py` o referirse a ella.

## CÓMO SE VERIFICA

Un cuaderno que no corre de principio a fin no está terminado.

    python kit/verify.py programacion-orientada-a-objetos/es/w01.3.ipynb

Eso lo corre con kernel nuevo en un directorio vacío, como arranca una sesión nueva de Colab, y
reporta cualquier traza. Cero errores no atrapados, o no está listo.

Análisis se verificó además contra pandas 3.0.3 y 2.2.3 porque Colab puede traer cualquiera. POO no
usa pandas, así que con una versión basta, salvo que alguna semana lo importe.

Formato: nbformat 4, metadata de Colab, guardados **sin salidas** y con `execution_count` en
`null`. `nbkit.write` ya lo hace.

## QUÉ NO TOCAR

`ppts/` está terminado y verificado: preflight, build, lint y sizes pasan limpios sobre cuarenta y
dos lecciones. Si crees que un deck tiene un error, repórtalo en tu resumen en lugar de corregirlo.
En Análisis aparecieron dos y así se manejaron.

Ojo con una cosa: `ppts/` no está trackeado por git. Nunca se ha commiteado. No hay respaldo, así
que un cambio ahí no se puede deshacer.

Tampoco toques `docs/en/courses/python-course/`. Es la fuente que los decks citan y que el sitio
de MkDocs publica, y las semanas 14 y 15 de POO dependen de ella porque no llevan cuaderno.

## POR DÓNDE EMPEZAR

`poo_w01_3.py`, el repaso del módulo 3 de `01 - Basics`, que es funciones. Su código fuente es
`Code010` y `Code011`.

Copia la estructura de `poo_w01_2.py`, que es el más parecido en forma. Hazlo completo en los dos
idiomas, verifica los dos, y de ahí sigue en orden: w01.4, w01.5, w02, y así hasta w17.

Cada semana es un módulo nuevo en `notebooks/kit/lessons/`. La convención de nombres es
`poo_wNN.py` para el español y `poo_wNN_en.py` para el inglés cuando el archivo se hace largo, o
los dos en el mismo archivo cuando cabe. Las dos formas están en uso y `kit.build` toma cualquiera.

Reporta al terminar cada semana, no cada bloque.
