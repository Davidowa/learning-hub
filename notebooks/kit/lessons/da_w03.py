"""notebooks/analisis-de-datos/{es,en}/w03.ipynb

Source deck: ppts/python/analisis-de-datos/{es,en}/w03.*.yaml
Salaries are the first five rows of 06 - Advanced/data/employees.csv.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from nbkit import md, code, write, REPO
from diagram import structures_figure

OUT = REPO / "notebooks" / "analisis-de-datos"

es = [

md("""
# Análisis de Datos · Semana 3
## Paradigmas e introducción a la programación

**TIA502 · Facultad de Empresariales · Profesor David Escobar-Castillejos**

Esta es la primera sesión con computadora, y cierra el bloque de pensamiento computacional. La
parte de paradigmas se corre rápido: lo que hace falta no es la taxonomía completa, sino saber
que vas a escribir estructurado y por qué eso alcanza para todo el curso.

Lo que vale la sesión entera es el primer programa. Que corra hoy, aquí, y que imprima algo.

Al terminar este cuaderno vas a poder:

1. Explicar qué es un paradigma y por qué el estructurado alcanza para este curso.
2. Nombrar las tres estructuras básicas y decir por qué con esas tres basta.
3. Distinguir compilar de interpretar, y decir qué hace Python con tu archivo.
4. Leer la estructura de un programa: importaciones, instrucciones, comentarios y orden.
5. Reconocer un error de sintaxis, ubicar la línea y corregirlo sin adivinar.

### Cómo se usa este cuaderno

Ejecuta las celdas en orden con **Shift + Enter**. El bloque 3 rompe el programa a propósito
seis veces para que veas cada error una vez en condiciones tranquilas. Todas esas celdas llevan
un comentario que lo dice.
"""),

md("""
---
# Bloque 1 · Formas de programar

Un paradigma es una manera de organizar la solución. Hay varias porque ningún problema se
parece a todos los demás.

| Paradigma | Cómo organiza la solución | Dónde se ve |
|---|---|---|
| Estructurado | Pasos en orden, con decisiones y ciclos | El de este curso, y el de casi todo análisis de datos |
| Orientado a objetos | Datos y comportamiento juntos en clases | Sistemas grandes, aplicaciones de escritorio |
| Funcional | Funciones que transforman datos sin cambiarlos | Procesamiento de datos, hojas de cálculo |
| Declarativo | Se declara qué se quiere, no cómo obtenerlo | SQL, y las fórmulas de Excel |

Ninguno es el correcto. Cada uno organiza la solución de otra forma, y unos encajan mejor que
otros según el problema.

Dos cosas de esa tabla te van a sorprender. **Las fórmulas de Excel son declarativas**: escribes
`=SUMA(A1:A10)` sin decir cómo recorrer las diez celdas. Y **una hoja de cálculo también es
funcional**, porque una fórmula transforma datos sin modificar los originales. Ya trabajaste en
dos paradigmas sin saber cómo se llamaban.

## Programación estructurada

Es la forma que vas a usar todo el semestre, y consiste en una idea sencilla: **todo programa se
puede escribir con tres estructuras.**

| Estructura | Qué hace |
|---|---|
| Secuencia | Una instrucción tras otra |
| Selección | Un camino u otro según una condición |
| Repetición | Lo mismo varias veces |

""" + structures_figure("es") + """

Nada de saltos a mitad del código. Se lee de arriba hacia abajo, y cuando se desvía, se ve
exactamente dónde y por qué. Antes de esta idea un programa podía saltar a cualquier línea, y
encontrar un error significaba seguir el salto a mano, uno por uno.

Las tres, una vez cada una, para que veas que no hay nada más.
"""),

code("""
# SECUENCIA: tres instrucciones, en el orden en que están escritas.
impresiones = 148230
clics = 5074
tasa = clics / impresiones

print("Tasa de conversión:", round(tasa * 100, 2), "%")
"""),

code("""
# SELECCIÓN: un camino u otro.
if tasa > 0.03:
    print("Campaña por arriba del promedio del sector")
else:
    print("Campaña por debajo del promedio del sector")
"""),

code("""
# REPETICIÓN: lo mismo varias veces, con datos distintos.
canales = ["Instagram", "Facebook", "Google"]

for canal in canales:
    print("Revisando", canal)
"""),

md("""
Eso es todo el vocabulario estructural del lenguaje. Cada semana de aquí a diciembre agrega
matices a esas tres, y ninguna agrega una cuarta.
"""),

md("""
---
# Bloque 2 · Qué es un lenguaje de programación

Un idioma intermedio. Lo suficientemente preciso para la máquina, lo suficientemente legible
para ti. Cuanto más arriba está un lenguaje, más se parece a como piensas, y Python vive en el
peldaño alto.

| Aspecto | Compilado | Interpretado |
|---|---|---|
| Cuándo traduce | Todo el programa antes de correrlo | Instrucción por instrucción, al ejecutar |
| Qué produce | Un ejecutable independiente | Nada permanente, corre y se acaba |
| Velocidad | Más rápido al ejecutar | Más lento, y a la escala de este curso no se nota |
| Cuándo avisa del error | Al compilar, antes de correr | Al llegar a la línea que falla |
| Ejemplos | C, C++, Go | Python, R, JavaScript |

La fila que te va a importar todos los días es la cuarta. **Python avisa del error cuando llega
a la línea que falla**, no antes de arrancar. Un programa puede correr veinte líneas
perfectamente y morir en la veintiuna.
"""),

code("""
# Las dos primeras líneas corren. La tercera es la que truena.
print("Esta línea sí se ejecuta")
print("Esta también")
print("Y ahora viene la que falla")

try:
    resultado = 10 / 0
except ZeroDivisionError as e:
    print("ZeroDivisionError:", e)

print("Sin el try, nada de aquí para abajo se habría ejecutado")
"""),

md("""
Un lenguaje compilado habría revisado el archivo completo antes de imprimir una sola línea. Con
Python, lo que ya salió a pantalla ya salió, aunque el programa muera después.

Eso importa cuando un script escribe archivos o manda correos: **la mitad del trabajo puede
quedar hecha.**

## Anatomía de un programa completo

Este es el primer programa del curso. Cinco sueldos, tres preguntas.
"""),

code("""
# Un comentario. Python lo ignora, tú no.
from statistics import mean

sueldos = [23200, 42800, 82700, 24500, 24500]

promedio = mean(sueldos)
mayor = max(sueldos)

print("Empleados:", len(sueldos))
print("Sueldo promedio:", promedio)
print("Sueldo mayor:", mayor)
"""),

md("""
Cuatro partes, y vale la pena nombrarlas.

**Las importaciones** van arriba y traen herramientas que no vienen listas. `mean` vive en
`statistics`, que es parte de Python y no hay que instalar.

**Los datos.** Esos cinco sueldos son los primeros de `employees.csv`, el archivo real del
curso. Entre corchetes son una lista, que es la columna de la semana 12.

**El orden.** Cada línea corre en el orden en que está escrita. No hay nada que la reordene.

**La salida.** `print` es lo único que se ve. Un cálculo sin `print` corre igual y no muestra
nada, y ese es el motivo número uno por el que un principiante cree que su programa está roto.
"""),

code("""
# Este programa hace exactamente el mismo trabajo y parece no hacer nada.
promedio_silencioso = mean(sueldos)
mayor_silencioso = max(sueldos)
"""),

md("""
Ninguna salida. El cálculo ocurrió, los valores existen, y sin un `print` nadie se entera.
"""),

code("""
print("Sí existen:", promedio_silencioso, mayor_silencioso)
"""),

md("""
### Lo que la biblioteca estándar ya trae

`mean` vino de `statistics`, pero `len` y `max` no hicieron falta importarlas. Están siempre
disponibles.
"""),

code("""
print("Suma:    ", sum(sueldos))
print("Cuántos: ", len(sueldos))
print("Mayor:   ", max(sueldos))
print("Menor:   ", min(sueldos))
print("Ordenados:", sorted(sueldos))
"""),

code("""
from statistics import mean, median, stdev

print("Promedio:", mean(sueldos))
print("Mediana: ", median(sueldos))
print("Desviación estándar:", round(stdev(sueldos), 2))
"""),

md("""
Fíjate en la distancia entre el promedio, 39 540, y la mediana, 24 500. Un solo sueldo de 82 700
jala el promedio muy por arriba de lo que gana la mayoría.

Es el mismo fenómeno que vas a dibujar en la semana 16 con un histograma, y aquí ya se ve con
dos números.
"""),

md("""
---
# Bloque 3 · La sintaxis y lo que no perdona

Las reglas de escritura del lenguaje. No son negociables, y el mensaje de error casi siempre
dice dónde fallaste.

| Regla | Qué exige | Qué pasa si la rompes |
|---|---|---|
| Sangría | Cuatro espacios marcan qué anida | `IndentationError`, y no corre nada |
| Mayúsculas | `Print` y `print` no son iguales | `NameError` sobre un nombre inexistente |
| Comillas | El texto va entre comillas, las dos | `SyntaxError` en esa línea o la siguiente |
| Paréntesis | Los que abren y cierran, en pares | `SyntaxError`, a veces una línea abajo |
| Dos puntos | Condiciones y ciclos terminan en uno | `SyntaxError` justo donde falta |

Los vas a ver cien veces este semestre. Vale más reconocerlos que evitarlos, así que aquí están
los cinco, provocados a propósito.

Estos usan una herramienta distinta a los `try` de antes: un error de sintaxis ocurre **antes**
de que el programa corra, así que no se puede atrapar con `try`. Hay que pedirle a Python que
lea el texto sin ejecutarlo.
"""),

code("""
def probar(codigo):
    \"\"\"Compila el código sin correrlo, y reporta el error tal cual.\"\"\"
    try:
        compile(codigo, "<ejemplo>", "exec")
        print("Compila bien")
    except SyntaxError as e:
        print(f"{type(e).__name__}: {e.msg}")
        print(f"  línea {e.lineno}: {(e.text or '').rstrip()}")
"""),

code("""
# ROMPE A PROPÓSITO 1: falta el paréntesis de cierre.
probar('print("Empleados:", len(sueldos)')
"""),

code("""
# ROMPE A PROPÓSITO 2: falta una comilla.
probar('print("Sueldo promedio:, promedio)')
"""),

code("""
# ROMPE A PROPÓSITO 3: faltan los dos puntos de la condición.
probar('if promedio > 30000\\n    print("alto")')
"""),

code("""
# ROMPE A PROPÓSITO 4: la sangría no corresponde.
probar('if promedio > 30000:\\nprint("alto")')
"""),

md("""
El de las mayúsculas es distinto: no es un error de sintaxis, porque `Print(...)` está
perfectamente bien escrito. El problema es que ese nombre no existe, y eso solo se descubre al
ejecutar.
"""),

code("""
# ROMPE A PROPÓSITO 5: Python distingue mayúsculas de minúsculas.
try:
    Print("Empleados:", len(sueldos))
except NameError as e:
    print("NameError:", e)
"""),

md("""
Ese mensaje incluso te sugiere la corrección. Vale la pena leerlo completo antes de tocar nada:
trae el tipo de error, el nombre que no encontró, y a veces la sugerencia.

### La trampa del paréntesis

De los cinco, el que más tiempo cuesta es el paréntesis, porque **Python reclama en la línea
siguiente**. Mira dónde dice que está el problema.
"""),

code("""
# ROMPE A PROPÓSITO 6: el paréntesis falta en la línea 1 y el error apunta a la 2.
probar('total = (23200 + 42800\\nprint(total)')
"""),

md("""
Dice línea 2, y el paréntesis que falta está en la 1. Cuando el mensaje señale un renglón que se
ve perfecto, **el problema está arriba**.

## El signo igual no compara, guarda

**Predice antes de correr.** ¿Qué imprime este programa?

- **A.** 300, porque suma y luego multiplica.
- **B.** 200, porque solo cuenta la última línea.
- **C.** 250, porque multiplica antes de sumar.
- **D.** Un error, porque `total` se redefine tres veces.
"""),

code("""
total = 100
total = total + 50
total = total * 2

print(total)
"""),

md("""
La respuesta es **A**, 300. La traza, paso a paso:

| Paso | Instrucción | `total` | Qué pasó |
|---|---|---|---|
| 1 | `total = 100` | 100 | Se crea el nombre y se le asigna un valor |
| 2 | `total = total + 50` | 150 | Se lee el valor viejo, se suma, se guarda encima |
| 3 | `total = total * 2` | 300 | Se lee 150, se duplica, se guarda encima |
| 4 | `print(total)` | 300 | Solo ahora aparece algo en pantalla |

El signo igual no compara, guarda. Cada línea pisa el valor que dejó la anterior, y por eso el
orden es todo. Compruébalo cambiando el orden.
"""),

code("""
total = 100
total = total * 2      # ahora la multiplicación va primero
total = total + 50

print(total)
"""),

md("""
250 en lugar de 300. Las mismas dos operaciones sobre el mismo número inicial, en otro orden.

Es la misma lección de la semana 2 con el bono, y va a volver a aparecer. **El orden de las
instrucciones es parte del resultado, no un detalle de estilo.**
"""),

md("""
---
# Ejercicios

Las soluciones están hasta abajo del cuaderno.

## Las tres estructuras

### Ejercicio 1 · Una de cada una

Escribe tres celdas cortas, una por estructura, con datos de una campaña o de un reporte que
conozcas. La de secuencia calcula algo, la de selección decide entre dos mensajes, y la de
repetición recorre tres elementos.

### Ejercicio 2 · Tu primer programa completo

Escribe un programa con las cuatro partes: una importación, unos datos, unos cálculos y unos
`print` con etiqueta. Usa seis sueldos inventados y reporta promedio, mediana, mayor y menor.

Que el promedio y la mediana salgan distintos. Si te salen iguales, tus datos son demasiado
parejos para ser interesantes.

## Los errores

### Ejercicio 3 · Los cinco, provocados por ti

Usa la función `probar` para provocar los cinco errores de la tabla, con código tuyo y no con
el del cuaderno. Anota el mensaje exacto de cada uno.

### Ejercicio 4 · Leer el mensaje

Este código tiene tres errores. Encuéntralos leyendo el mensaje, uno a la vez, y arréglalos.

```python
from statistics import mean

sueldos = [23200, 42800, 82700]
promedio = mean(sueldos
Print("El promedio es:, promedio)
```

Pista: arregla uno, vuelve a correr, y deja que Python te enseñe el siguiente. Buscarlos todos
de un jalón es cómo se pierde media hora.

### Ejercicio 5 · El programa que no muestra nada

Este programa corre sin errores y no imprime nada. Arréglalo.

```python
sueldos = [23200, 42800, 82700, 24500, 24500]
total = sum(sueldos)
promedio = total / len(sueldos)
```

Después explica en un comentario por qué "no imprime nada" y "está roto" no son lo mismo.

## Orden y asignación

### Ejercicio 6 · El orden importa

Empieza con `precio = 1000`. Escribe dos versiones que apliquen un descuento del 10 % y un IVA
del 16 %, en los dos órdenes posibles. Imprime los dos resultados.

Después contesta en un comentario: ¿dan lo mismo? Y si dan lo mismo, ¿por qué el orden sí
importó en el caso de `total` de arriba y aquí no?

### Ejercicio 7 · Rómpelo y arréglalo

Copia el programa de los sueldos del bloque 2, córrelo, y después rómpelo a propósito de tres
formas distintas: quita un paréntesis, cambia `print` por `Print` y borra una comilla. Anota el
mensaje exacto de cada uno en una tabla.
"""),

md("""
---
## Tres ideas para llevarse

**Tres estructuras bastan para todo.** Secuencia, selección y repetición. Todo lo demás del
semestre es una variante de esas tres.

**Python traduce mientras corre.** Por eso el error aparece cuando llega a esa línea y no antes
de arrancar, y por eso la mitad del trabajo puede quedar hecha cuando algo falla.

**El mensaje de error es una pista, no un regaño.** Trae archivo, línea y tipo. Leerlo completo
ahorra más tiempo que cualquier otra costumbre de este curso.

La siguiente sesión son los tipos de datos, y por qué un código postal no es un número aunque lo
parezca.
"""),

md("""
---
# Soluciones

### Ejercicio 1

```python
# Secuencia
inversion = 38500
clics = 5074
costo_por_clic = inversion / clics
print("Costo por clic:", round(costo_por_clic, 2))

# Selección
if costo_por_clic < 10:
    print("Costo por clic dentro del objetivo")
else:
    print("Costo por clic arriba del objetivo")

# Repetición
for canal in ["Instagram", "Facebook", "Google"]:
    print("Pendiente revisar", canal)
```

Las tres caben en quince líneas y con ellas ya se puede escribir cualquier programa. Lo que
falta el resto del semestre es soltura, no vocabulario nuevo.

### Ejercicio 2

```python
from statistics import mean, median

sueldos = [21000, 24500, 26800, 31200, 45000, 88000]

print("Empleados:", len(sueldos))
print("Promedio: ", round(mean(sueldos), 2))
print("Mediana:  ", median(sueldos))
print("Mayor:    ", max(sueldos))
print("Menor:    ", min(sueldos))
```

Promedio 39 416 y mediana 29 000. El sueldo de 88 000 empuja el promedio veinte mil pesos por
arriba de lo que gana la persona de en medio, que es exactamente lo que pasa en `employees.csv`
y en casi cualquier nómina real.

### Ejercicio 3

```python
probar('inversion = (38500 + 1200')
probar('print("Canal: , canal)')
probar('for canal in canales\\n    print(canal)')
probar('for canal in canales:\\nprint(canal)')

try:
    Len(sueldos)
except NameError as e:
    print("NameError:", e)
```

El cuarto es el que más confunde al principio, porque el código se ve casi bien. Python usa la
sangría como estructura, así que un `for` sin nada indentado abajo no tiene cuerpo, y eso es un
error de sintaxis y no de estilo.

### Ejercicio 4

```python
from statistics import mean

sueldos = [23200, 42800, 82700]
promedio = mean(sueldos)
print("El promedio es:", promedio)
```

Eran tres: el paréntesis sin cerrar en la línea 4, el `Print` con mayúscula y la comilla que
faltaba antes de la coma. Los tres se arreglan uno por uno, y el primero esconde a los otros dos
hasta que se corrige.

Ese es el patrón: un error de sintaxis impide que Python siga leyendo, así que solo ve el
primero. Por eso conviene arreglar, correr, y volver a mirar.

### Ejercicio 5

```python
sueldos = [23200, 42800, 82700, 24500, 24500]
total = sum(sueldos)
promedio = total / len(sueldos)

print("Total:   ", total)
print("Promedio:", promedio)

# "No imprime nada" y "está roto" no son lo mismo. El programa de arriba corre
# entero, calcula bien las dos cosas y termina sin errores. Lo único que le
# faltaba era decirlo. Un programa roto se detiene con un mensaje; uno silencioso
# hizo el trabajo y no lo reportó, que es un problema de comunicación y no de
# lógica.
```

Esta distinción importa más adelante, cuando un script escriba archivos. Ahí "no imprimió nada"
puede significar que todo salió bien.

### Ejercicio 6

```python
precio = 1000

# Descuento primero, IVA después
a = precio * 0.90
a = a * 1.16

# IVA primero, descuento después
b = precio * 1.16
b = b * 0.90

print("Descuento y luego IVA:", round(a, 2))
print("IVA y luego descuento:", round(b, 2))
print("¿Iguales?", round(a, 2) == round(b, 2))

# Dan lo mismo, 1044.00. Multiplicar es conmutativo: 0.90 por 1.16 da lo mismo
# que 1.16 por 0.90. En el caso de total, en cambio, una operación era suma y la
# otra multiplicación, y esas dos no se pueden intercambiar. El orden importa
# cuando las operaciones son de distinto tipo, no siempre.
```

Vale la pena saber cuándo el orden **no** importa, porque si no acabas poniendo paréntesis en
todos lados por miedo. La regla útil: mezcla de suma y multiplicación, revisa el orden; puras
multiplicaciones, da igual.

### Ejercicio 7

Los tres mensajes son `SyntaxError: '(' was never closed`, `NameError: name 'Print' is not
defined` y un `SyntaxError: unterminated string literal` con el número de línea.

La tabla se califica sobre que el mensaje esté copiado tal cual, con su tipo y su línea, y no
parafraseado. La última palabra del tipo de error es la que hay que leer primero, y copiarla
mal es no haberla leído.
"""),

]

write(OUT / "es" / "w03.ipynb", es)
print("wrote", OUT / "es" / "w03.ipynb")


en = [

md("""
# Data Analysis · Week 3
## Paradigms and an introduction to programming

**TIA502 · School of Business · Instructor David Escobar-Castillejos**

This is the first session with a computer, and it closes the computational thinking block. The
paradigms part goes quickly: what the course needs is not the full taxonomy but knowing that you
will write structured code, and why that is enough.

What makes the session worth it is the first program. That it runs today, here, and prints
something.

By the end of this notebook you will be able to:

1. Explain what a paradigm is and why structured programming is enough for this course.
2. Name the three basic structures and say why those three suffice.
3. Tell compiling from interpreting, and say what Python does with your file.
4. Read the structure of a program: imports, statements, comments and order.
5. Recognise a syntax error, locate the line and fix it without guessing.

### How to use this notebook

Run the cells in order with **Shift + Enter**. Block 3 breaks the program on purpose six times
so you meet each error once under calm conditions. All of those cells carry a comment saying so.
"""),

md("""
---
# Block 1 · Ways of programming

A paradigm is a way of organising the solution. There are several because no problem resembles
all the others.

| Paradigm | How it organises the solution | Where you see it |
|---|---|---|
| Structured | Steps in order, with decisions and loops | This course, and nearly all data analysis |
| Object oriented | Data and behaviour together in classes | Large systems, desktop applications |
| Functional | Functions that transform data without changing it | Data processing, spreadsheets |
| Declarative | You declare what you want, not how to get it | SQL, and Excel formulas |

None of them is the correct one. Each organises the solution differently, and some fit better
than others depending on the problem.

Two things in that table will surprise you. **Excel formulas are declarative**: you write
`=SUM(A1:A10)` without saying how to walk the ten cells. And **a spreadsheet is also
functional**, because a formula transforms data without modifying the original. You have already
worked in two paradigms without knowing their names.

## Structured programming

It is the form you will use all term, and it rests on a simple idea: **every program can be
written with three structures.**

| Structure | What it does |
|---|---|
| Sequence | One instruction after another |
| Selection | One path or another depending on a condition |
| Repetition | The same thing several times |

""" + structures_figure("en") + """

No jumping into the middle of the code. It reads top to bottom, and when it branches, you can
see exactly where and why. Before this idea a program could jump to any line, and finding a bug
meant following the jump by hand, one at a time.

All three, once each, so you can see there is nothing more.
"""),

code("""
# SEQUENCE: three instructions, in the order they are written.
impressions = 148230
clicks = 5074
rate = clicks / impressions

print("Conversion rate:", round(rate * 100, 2), "%")
"""),

code("""
# SELECTION: one path or the other.
if rate > 0.03:
    print("Campaign above the sector average")
else:
    print("Campaign below the sector average")
"""),

code("""
# REPETITION: the same thing several times, with different data.
channels = ["Instagram", "Facebook", "Google"]

for channel in channels:
    print("Checking", channel)
"""),

md("""
That is the whole structural vocabulary of the language. Every week between here and December
adds nuance to those three, and none of them adds a fourth.
"""),

md("""
---
# Block 2 · What a programming language is

An intermediate tongue. Precise enough for the machine, readable enough for you. The higher up a
language sits, the more it resembles how you think, and Python lives on the high rung.

| Aspect | Compiled | Interpreted |
|---|---|---|
| When it translates | The whole program before running it | Statement by statement, while running |
| What it produces | A standalone executable | Nothing permanent, it runs and it is over |
| Speed | Faster to execute | Slower, and at this course's scale you cannot tell |
| When it reports an error | At compile time, before running | On reaching the line that fails |
| Examples | C, C++, Go | Python, R, JavaScript |

The row that will matter to you daily is the fourth. **Python reports the error when it reaches
the line that fails**, not before starting. A program can run twenty lines perfectly and die on
the twenty-first.
"""),

code("""
# The first two lines run. The third is the one that blows up.
print("This line does execute")
print("So does this one")
print("And now comes the one that fails")

try:
    result = 10 / 0
except ZeroDivisionError as e:
    print("ZeroDivisionError:", e)

print("Without the try, nothing below here would have run")
"""),

md("""
A compiled language would have checked the whole file before printing a single line. With
Python, whatever already reached the screen has reached it, even if the program dies afterwards.

That matters when a script writes files or sends email: **half the work can already be done.**

## Anatomy of a complete program

This is the first program of the course. Five salaries, three questions.
"""),

code("""
# A comment. Python ignores it, you do not.
from statistics import mean

salaries = [23200, 42800, 82700, 24500, 24500]

average = mean(salaries)
highest = max(salaries)

print("Employees:", len(salaries))
print("Average salary:", average)
print("Highest salary:", highest)
"""),

md("""
Four parts, and they are worth naming.

**The imports** go at the top and bring in tools that do not come ready. `mean` lives in
`statistics`, which is part of Python and needs no installing.

**The data.** Those five salaries are the first five in `employees.csv`, the real course file.
Inside brackets they are a list, which is the column from week 12.

**The order.** Every line runs in the order it is written. Nothing reorders it.

**The output.** `print` is the only thing you see. A calculation with no `print` runs just the
same and shows nothing, and that is the number one reason a beginner thinks their program is
broken.
"""),

code("""
# This program does exactly the same work and appears to do nothing.
silent_average = mean(salaries)
silent_highest = max(salaries)
"""),

md("""
No output at all. The calculation happened, the values exist, and without a `print` nobody finds
out.
"""),

code("""
print("They do exist:", silent_average, silent_highest)
"""),

md("""
### What the standard library already carries

`mean` came from `statistics`, but `len` and `max` needed no import. They are always available.
"""),

code("""
print("Sum:     ", sum(salaries))
print("How many:", len(salaries))
print("Highest: ", max(salaries))
print("Lowest:  ", min(salaries))
print("Sorted:  ", sorted(salaries))
"""),

code("""
from statistics import mean, median, stdev

print("Average:", mean(salaries))
print("Median: ", median(salaries))
print("Standard deviation:", round(stdev(salaries), 2))
"""),

md("""
Look at the distance between the average, 39,540, and the median, 24,500. A single salary of
82,700 pulls the average well above what most people earn.

It is the same phenomenon you will draw in week 16 with a histogram, and here it already shows
with two numbers.
"""),

md("""
---
# Block 3 · Syntax, and what it will not forgive

The writing rules of the language. They are not negotiable, and the error message nearly always
says where you went wrong.

| Rule | What it demands | What happens if you break it |
|---|---|---|
| Indentation | Four spaces mark what nests | `IndentationError`, and nothing runs |
| Capitalisation | `Print` and `print` are not the same | `NameError` about a name that does not exist |
| Quotes | Text goes in quotes, both of them | `SyntaxError` on that line or the next |
| Parentheses | The ones that open and close, in pairs | `SyntaxError`, sometimes a line below |
| Colons | Conditions and loops end in one | `SyntaxError` right where it is missing |

You will see them a hundred times this term. It is worth more to recognise them than to avoid
them, so here are all five, provoked on purpose.

These use a different tool from the earlier `try` blocks: a syntax error happens **before** the
program runs, so it cannot be caught with `try`. Python has to be asked to read the text without
executing it.
"""),

code("""
def check(source):
    \"\"\"Compile the code without running it, and report the error as it comes.\"\"\"
    try:
        compile(source, "<example>", "exec")
        print("Compiles fine")
    except SyntaxError as e:
        print(f"{type(e).__name__}: {e.msg}")
        print(f"  line {e.lineno}: {(e.text or '').rstrip()}")
"""),

code("""
# BREAKS ON PURPOSE 1: the closing parenthesis is missing.
check('print("Employees:", len(salaries)')
"""),

code("""
# BREAKS ON PURPOSE 2: a quote is missing.
check('print("Average salary:, average)')
"""),

code("""
# BREAKS ON PURPOSE 3: the condition's colon is missing.
check('if average > 30000\\n    print("high")')
"""),

code("""
# BREAKS ON PURPOSE 4: the indentation does not match.
check('if average > 30000:\\nprint("high")')
"""),

md("""
The capitalisation one is different: it is not a syntax error, because `Print(...)` is perfectly
well formed. The problem is that the name does not exist, and that is only discovered at run
time.
"""),

code("""
# BREAKS ON PURPOSE 5: Python tells capitals from lowercase.
try:
    Print("Employees:", len(salaries))
except NameError as e:
    print("NameError:", e)
"""),

md("""
That message even suggests the fix. It is worth reading in full before touching anything: it
carries the error type, the name it could not find, and sometimes the suggestion.

### The parenthesis trap

Of the five, the one that costs the most time is the parenthesis, because **Python complains on
the following line**. Watch where it says the problem is.
"""),

code("""
# BREAKS ON PURPOSE 6: the parenthesis is missing on line 1 and the error points at line 2.
check('total = (23200 + 42800\\nprint(total)')
"""),

md("""
It says line 2, and the missing parenthesis is on line 1. When the message points at a line that
looks perfect, **the problem is above it**.

## The equals sign does not compare, it stores

**Predict before you run.** What does this program print?

- **A.** 300, because it adds and then multiplies.
- **B.** 200, because only the last line counts.
- **C.** 250, because it multiplies before adding.
- **D.** An error, because `total` is redefined three times.
"""),

code("""
total = 100
total = total + 50
total = total * 2

print(total)
"""),

md("""
The answer is **A**, 300. The trace, step by step:

| Step | Statement | `total` | What happened |
|---|---|---|---|
| 1 | `total = 100` | 100 | The name is created and given a value |
| 2 | `total = total + 50` | 150 | The old value is read, added to, written over |
| 3 | `total = total * 2` | 300 | 150 is read, doubled, written over |
| 4 | `print(total)` | 300 | Only now does anything reach the screen |

The equals sign does not compare, it stores. Each line writes over what the previous one left,
which is why the order is everything. Check it by swapping the order.
"""),

code("""
total = 100
total = total * 2      # now the multiplication goes first
total = total + 50

print(total)
"""),

md("""
250 instead of 300. The same two operations on the same starting number, in a different order.

It is the same lesson as week 2 with the bonus, and it will keep coming back. **The order of the
statements is part of the result, not a matter of style.**
"""),

md("""
---
# Exercises

The solutions sit at the very bottom of the notebook.

## The three structures

### Exercise 1 · One of each

Write three short cells, one per structure, using data from a campaign or a report you know. The
sequence one calculates something, the selection one chooses between two messages, and the
repetition one walks three items.

### Exercise 2 · Your first complete program

Write a program with all four parts: an import, some data, some calculations and some labelled
`print` calls. Use six made-up salaries and report the average, median, highest and lowest.

Make the average and the median come out different. If they come out the same, your data is too
even to be interesting.

## The errors

### Exercise 3 · All five, provoked by you

Use the `check` function to provoke the five errors in the table, with your own code rather than
the notebook's. Write down the exact message for each.

### Exercise 4 · Reading the message

This code has three errors. Find them by reading the message, one at a time, and fix them.

```python
from statistics import mean

salaries = [23200, 42800, 82700]
average = mean(salaries
Print("The average is:, average)
```

Hint: fix one, run again, and let Python show you the next. Hunting for all of them at once is
how you lose half an hour.

### Exercise 5 · The program that shows nothing

This program runs without errors and prints nothing. Fix it.

```python
salaries = [23200, 42800, 82700, 24500, 24500]
total = sum(salaries)
average = total / len(salaries)
```

Then explain in a comment why "prints nothing" and "is broken" are not the same thing.

## Order and assignment

### Exercise 6 · Order matters

Start with `price = 1000`. Write two versions that apply a 10 % discount and 16 % tax, in both
possible orders. Print both results.

Then answer in a comment: do they agree? And if they do, why did order matter for `total` above
and not here?

### Exercise 7 · Break it and fix it

Copy the salary program from block 2, run it, then break it on purpose three different ways:
remove a parenthesis, change `print` to `Print` and delete a quote. Write down the exact message
for each in a table.
"""),

md("""
---
## Three ideas to take away

**Three structures are enough for everything.** Sequence, selection and repetition. Everything
else this term is a variation on those three.

**Python translates while it runs.** That is why the error appears when it reaches that line and
not before starting, and why half the work can already be done when something fails.

**The error message is a clue, not a telling-off.** It carries the file, the line and the type.
Reading it in full saves more time than any other habit in this course.

Next session is data types, and why a postal code is not a number even though it looks like one.
"""),

md("""
---
# Solutions

### Exercise 1

```python
# Sequence
spend = 38500
clicks = 5074
cost_per_click = spend / clicks
print("Cost per click:", round(cost_per_click, 2))

# Selection
if cost_per_click < 10:
    print("Cost per click within target")
else:
    print("Cost per click above target")

# Repetition
for channel in ["Instagram", "Facebook", "Google"]:
    print("Still to review:", channel)
```

All three fit in fifteen lines and with them any program can already be written. What the rest of
the term adds is fluency, not new vocabulary.

### Exercise 2

```python
from statistics import mean, median

salaries = [21000, 24500, 26800, 31200, 45000, 88000]

print("Employees:", len(salaries))
print("Average:  ", round(mean(salaries), 2))
print("Median:   ", median(salaries))
print("Highest:  ", max(salaries))
print("Lowest:   ", min(salaries))
```

Average 39,416 and median 29,000. The salary of 88,000 pushes the average twenty thousand pesos
above what the middle person earns, which is exactly what happens in `employees.csv` and in
almost any real payroll.

### Exercise 3

```python
check('spend = (38500 + 1200')
check('print("Channel: , channel)')
check('for channel in channels\\n    print(channel)')
check('for channel in channels:\\nprint(channel)')

try:
    Len(salaries)
except NameError as e:
    print("NameError:", e)
```

The fourth is the most confusing at first, because the code looks nearly right. Python uses
indentation as structure, so a `for` with nothing indented below it has no body, and that is a
syntax error rather than a style one.

### Exercise 4

```python
from statistics import mean

salaries = [23200, 42800, 82700]
average = mean(salaries)
print("The average is:", average)
```

There were three: the unclosed parenthesis on line 4, the capitalised `Print`, and the quote
missing before the comma. All three get fixed one at a time, and the first hides the other two
until it is corrected.

That is the pattern: a syntax error stops Python from reading further, so it only sees the
first. Which is why you fix, run, and look again.

### Exercise 5

```python
salaries = [23200, 42800, 82700, 24500, 24500]
total = sum(salaries)
average = total / len(salaries)

print("Total:  ", total)
print("Average:", average)

# "Prints nothing" and "is broken" are not the same thing. The program above runs
# all the way through, computes both values correctly and finishes without errors.
# All it was missing was saying so. A broken program stops with a message; a silent
# one did the work and did not report it, which is a communication problem rather
# than a logic one.
```

This distinction matters later, when a script writes files. There, "it printed nothing" can mean
everything went fine.

### Exercise 6

```python
price = 1000

# Discount first, tax second
a = price * 0.90
a = a * 1.16

# Tax first, discount second
b = price * 1.16
b = b * 0.90

print("Discount then tax:", round(a, 2))
print("Tax then discount:", round(b, 2))
print("Equal?", round(a, 2) == round(b, 2))

# They agree, at 1044.00. Multiplication is commutative: 0.90 times 1.16 equals
# 1.16 times 0.90. With total, on the other hand, one operation was addition and
# the other multiplication, and those two cannot be swapped. Order matters when
# the operations are of different kinds, not always.
```

It is worth knowing when order does **not** matter, because otherwise you end up putting
parentheses everywhere out of fear. The useful rule: a mix of addition and multiplication, check
the order; multiplications only, it makes no difference.

### Exercise 7

The three messages are `SyntaxError: '(' was never closed`, `NameError: name 'Print' is not
defined` and a `SyntaxError: unterminated string literal` with its line number.

The table is graded on the message being copied verbatim, with its type and its line, rather than
paraphrased. The last word of the error type is the one to read first, and copying it wrong means
not having read it.
"""),

]

write(OUT / "en" / "w03.ipynb", en)
print("wrote", OUT / "en" / "w03.ipynb")
