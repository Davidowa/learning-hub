"""notebooks/analisis-de-datos/{es,en}/w05.ipynb

Source deck: ppts/python/analisis-de-datos/{es,en}/w05.*.yaml

input() blocks a notebook, so the real thing is shown exactly once, guarded so a
headless "run all" falls through instead of hanging. Everything else uses values
already assigned.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from nbkit import md, code, write, REPO

OUT = REPO / "notebooks" / "analisis-de-datos"

es = [

md("""
# Análisis de Datos · Semana 5
## Instrucciones, entrada y salida

**TIA502 · Facultad de Empresariales · Profesor David Escobar-Castillejos**

Un número correcto mal presentado es un número que nadie va a usar. Esta sesión es sobre cómo
entran los datos al programa, cómo salen los resultados y cómo se presentan para que se
entiendan sin que tú estés ahí explicándolos.

Al terminar este cuaderno vas a poder:

1. Clasificar los cuatro tipos de instrucción y decir para qué sirve cada uno.
2. Leer datos desde el teclado con `input`, convirtiendo antes de operar.
3. Componer texto con f-strings, mezclando texto fijo y valores calculados.
4. Dar formato a un número con separador de miles, decimales fijos y porcentaje.
5. Escribir una salida con etiquetas, alineación y unidades.

### Una advertencia sobre `input` en Colab

`input` detiene el cuaderno y abre un cuadro de texto arriba de la celda. Mientras no escribas
algo y presiones Enter, **nada más se ejecuta**.

Por eso en este cuaderno hay **una sola celda con `input` de verdad**, marcada con claridad, y
todo lo demás usa valores ya asignados. Así puedes usar "Ejecutar todo" sin que se quede
esperando.

Cuatro celdas fallan a propósito y llevan un comentario que lo dice.
"""),

md("""
---
# Bloque 1 · Qué puede hacer una línea

Cuatro tipos de instrucción, y con ellos se arma cualquier programa del semestre.

| Tipo | Qué hace | Ejemplo |
|---|---|---|
| Asignación | Guarda un valor en un nombre | `clics = 5074` |
| Entrada | Trae un dato desde fuera del programa | `canal = input("Canal: ")` |
| Salida | Muestra un resultado | `print(costo_por_clic)` |
| Control | Decide o repite | `if`, `else`, `while`, `for` |

Las tres primeras son de hoy. El control llega la semana que entra.

## Un programa es entrada, proceso y salida

Toda la estructura cabe en tres partes. Primero se consiguen los datos, ya sea del teclado, de
un archivo o escritos en el propio código. Después se calculan los resultados. Al final se
muestran.

Cuando un programa no funciona, la primera pregunta útil es **en cuál de las tres partes se
rompió**.
"""),

code("""
# ENTRADA: los datos, aquí escritos en el código.
canal = "Instagram"
impresiones = 148230
clics = 5074
inversion = 38500.00

# PROCESO: las cuentas, sin imprimir nada.
conversion = clics / impresiones
costo_por_clic = inversion / clics

# SALIDA: solo mostrar. Ninguna cuenta ocurre aquí.
print(canal, conversion, costo_por_clic)
"""),

md("""
Mezclar las tres partes es lo que impide probarlas. Si el cálculo está enredado con los `print`,
no puedes revisar el número sin volver a correr todo y leer la pantalla.

Separadas, cada parte se revisa sola. Puedes cambiar los datos de entrada sin tocar las cuentas,
y cambiar la presentación sin arriesgar los números.
"""),

code("""
# Cambio solo la entrada. El proceso y la salida siguen igual.
canal = "Facebook"
impresiones = 96400
clics = 2891
inversion = 21300.00

conversion = clics / impresiones
costo_por_clic = inversion / clics

print(canal, conversion, costo_por_clic)
"""),

md("""
---
# Bloque 2 · Entrada de datos

Todo lo que llega de fuera llega como texto. Sin excepción, y sin avisar.

## La única celda con `input` de este cuaderno

Esta es la forma real. En Colab abre un cuadro de texto arriba de la celda y espera a que
escribas algo.

Si estás leyendo el cuaderno de corrido y no quieres detenerte, sáltala: la de abajo hace lo
mismo con valores ya puestos.
"""),

code("""
# ESTA CELDA ESPERA POR TI. En Colab abre un cuadro de texto arriba.
# El try es para que un "Ejecutar todo" sin teclado no se quede colgado.
try:
    canal_capturado = input("Canal de la campaña: ")
    clics_capturados = int(input("Clics registrados: "))
    inversion_capturada = float(input("Inversión en pesos: "))
except Exception:
    print("(sin teclado disponible, se usan valores de ejemplo)")
    canal_capturado, clics_capturados, inversion_capturada = "Instagram", 5074, 38500.0

print(canal_capturado, inversion_capturada / clics_capturados)
"""),

md("""
Tres cosas de esa celda merecen nombre.

**El mensaje.** Lo que va dentro de `input` se muestra antes de esperar. Sin él, el programa se
queda quieto con la pantalla en blanco y parece colgado.

**La conversión.** `int` y `float` envuelven al `input`. El canal no se convierte porque ya es
texto.

**El orden.** El programa se detiene en cada `input` hasta que alguien escribe algo y presiona
Enter. Tres `input` son tres paradas.

## Por qué `input` devuelve texto, siempre

De aquí en adelante todo usa valores ya asignados. Pero conviene ver qué habría pasado sin la
conversión, y eso se puede simular sin teclado.
"""),

code("""
# Lo que input habría devuelto: texto, aunque el usuario escriba dígitos.
respuesta_cruda = "5074"

print(respuesta_cruda, type(respuesta_cruda))
print("Convertido:", int(respuesta_cruda), type(int(respuesta_cruda)))
"""),

code("""
# FALLA A PROPÓSITO. Sin convertir, la suma pega los textos.
clics_texto = "5074"
nuevos_texto = "320"

print("Sin convertir:", clics_texto + nuevos_texto)
print("Convertidos:  ", int(clics_texto) + int(nuevos_texto))
"""),

md("""
Ninguna de las dos líneas lanza error. La primera contesta algo que no sirve, y esa es la
diferencia entre un programa roto y uno peligroso.

## Convertir tarde no arregla nada

Este es el error específico que más aparece en la primera entrega con teclado: envolver el
resultado en lugar del `input`.
"""),

code("""
# FALLA A PROPÓSITO. La conversión llega después de la operación.
a = "5074"
b = "320"

mal = int(a + b)          # se pegan primero, se convierte después
bien = int(a) + int(b)    # se convierte primero, se suma después

print("Convertir al final:", mal)
print("Convertir al inicio:", bien)
"""),

md("""
`int(a + b)` dio 5 074 320, y ni siquiera lanzó error, porque `"5074320"` es un entero
perfectamente válido.

La conversión va pegada al `input`, no al resultado. Es la diferencia entre `int(input(...))` y
`int(...)` al final de todo.

## Cuando el usuario escribe cualquier cosa
"""),

code("""
# FALLA A PROPÓSITO. int() sobre algo que no es un número.
for escrito in ["5074", "5,074", "cinco mil", "5074.0", ""]:
    try:
        print(f"int({escrito!r:12}) -> {int(escrito)}")
    except ValueError as e:
        print(f"int({escrito!r:12}) -> ValueError: {e}")
"""),

md("""
Cuatro de cinco fallan, y las cuatro son cosas que una persona escribiría con toda naturalidad.

Por ahora basta con saber que puede pasar. La semana que entra, con `if`, vas a poder revisar
antes de convertir; en la semana 9, con `while`, vas a poder volver a preguntar hasta que la
respuesta sirva.

## Leer varios datos sin repetir código

Una forma de trabajar con teclado sin llenar el programa de `input`: junta los datos en una sola
estructura y captúralos en un ciclo. Aquí simulado con respuestas ya escritas.
"""),

code("""
# Simulación: lo que habría escrito una persona, en el orden en que se le pidió.
RESPUESTAS = ["Instagram", "148230", "5074", "38500"]

etiquetas = ["Canal", "Impresiones", "Clics", "Inversión"]
datos = {}

for etiqueta, escrito in zip(etiquetas, RESPUESTAS):
    print(f"{etiqueta}: {escrito}")
    datos[etiqueta] = escrito

print()
print(datos)
"""),

md("""
Fíjate en que todos los valores del diccionario son texto, incluso los que son dígitos. La
conversión sigue pendiente y sigue siendo tu trabajo.
"""),

code("""
campana = {
    "canal": datos["Canal"],
    "impresiones": int(datos["Impresiones"]),
    "clics": int(datos["Clics"]),
    "inversion": float(datos["Inversión"]),
}

for nombre, valor in campana.items():
    print(f"{nombre:<14} {str(valor):<12} {type(valor).__name__}")
"""),

md("""
---
# Bloque 3 · Salida de resultados

El número correcto mal presentado es un número que nadie va a usar.

Compara. Los dos valores de abajo son correctos y ninguno de los dos sirve para un reporte.
"""),

code("""
impresiones = 148230
clics = 5074
inversion = 38500.00

conversion = clics / impresiones
cpc = inversion / clics

print("Conversion:", conversion)
print("Costo:", cpc)
"""),

md("""
`0.034230587600350804` y `7.587702010248325`. Nadie va a leer eso en una junta.

## f-strings

Una cadena que empieza con `f` permite meter valores dentro del texto, encerrados entre llaves.
Lo que va dentro de las llaves se evalúa y se sustituye por su resultado.

Reemplaza a concatenar con signos de más, que obliga a convertir todo a texto a mano y se vuelve
ilegible en cuanto hay tres valores.
"""),

code("""
canal = "Instagram"

# La forma vieja, con concatenación.
print("Canal: " + canal + ", clics: " + str(clics))

# La forma del curso.
print(f"Canal: {canal}, clics: {clics}")
"""),

md("""
Fíjate en el `str(clics)` de la primera. Sin él, concatenar un texto y un número lanza error. La
f-string convierte sola.

Dentro de las llaves puede ir una variable o una expresión completa.
"""),

code("""
print(f"Costo por clic: {inversion / clics}")
print(f"El canal tiene {len(canal)} letras")
print(f"¿Buena campaña? {conversion > 0.03}")
"""),

md("""
## Los cinco códigos de formato

Después de dos puntos va cómo se ve el número. Es el mismo tipo de código que el formato de
celda de una hoja de cálculo, solo que escrito en lugar de elegido en un menú.

| Código | Qué hace | Entrada | Se ve como |
|---|---|---|---|
| `:,` | Separador de miles | `148230` | `148,230` |
| `:.2f` | Dos decimales fijos | `7.588490` | `7.59` |
| `:,.2f` | Miles y dos decimales | `38500` | `38,500.00` |
| `:.1%` | Porcentaje con un decimal | `0.0342` | `3.4%` |
| `:>10` | Alineado a la derecha en diez espacios | `5074` | `      5074` |
"""),

code("""
print(f"{148230:,}")
print(f"{7.588490:.2f}")
print(f"{38500:,.2f}")
print(f"{0.0342:.1%}")
print(f"[{5074:>10}]")
"""),

md("""
**Predice antes de correr.** ¿Qué imprime esta línea?

- **A.** `Conversión: 0.0%`
- **B.** `Conversión: 3.4%`
- **C.** `Conversión: 0.034%`
- **D.** `Conversión: 34.2%`
"""),

code("""
tasa = 0.0342

print(f"Conversión: {tasa:.1%}")
"""),

md("""
La respuesta es **B**. El código de porcentaje **ya multiplica por cien**, así que no hay que
hacerlo a mano. Multiplicarlo tú además es el error que produce la opción D.
"""),

code("""
# FALLA A PROPÓSITO. Multiplicar y además pedir porcentaje.
print(f"Correcto: {tasa:.1%}")
print(f"Doble:    {tasa * 100:.1%}")
"""),

md("""
Trescientos cuarenta y dos por ciento de conversión. Ninguna campaña convierte así, y aun así el
programa lo imprime sin protestar.

## El formato no cambia el valor

Es importante y se olvida: el código de formato afecta cómo se ve esa línea, no lo que hay
guardado.
"""),

code("""
print(f"Formateado: {cpc:.2f}")
print(f"El valor sigue siendo: {cpc}")
print(f"Y sirve para seguir calculando: {cpc * 30:.2f} en treinta clics")
"""),

md("""
Igual que darle formato de moneda a una celda no cambia lo que hay dentro.

Si de verdad quieres modificar el valor, eso es `round`, y son cosas distintas.
"""),

code("""
redondeado = round(cpc, 2)

print("Formateado:", f"{cpc:.2f}", "· valor original:", cpc)
print("Redondeado:", redondeado, "· ya perdió los decimales")
"""),

md("""
## Un reporte completo
"""),

code("""
canal = "Instagram"
impresiones = 148230
clics = 5074
inversion = 38500.00

conversion = clics / impresiones
cpc = inversion / clics
cpm = inversion / impresiones * 1000

print(f"Canal: {canal}")
print(f"Impresiones: {impresiones:,}")
print(f"Conversión: {conversion:.2%}")
print(f"Costo por clic: ${cpc:,.2f}")
print(f"Costo por mil: ${cpm:,.2f}")
"""),

md("""
El signo de pesos es texto fijo dentro de la cadena, igual que la etiqueta. Todo lo que no va
entre llaves se imprime tal cual.

## Alinear en columna

Cuando son varias métricas, alinearlas convierte una lista en una tabla.
"""),

code("""
metricas = [
    ("Impresiones", f"{impresiones:,}"),
    ("Clics", f"{clics:,}"),
    ("Conversión", f"{conversion:.2%}"),
    ("Costo por clic", f"${cpc:,.2f}"),
    ("Costo por mil", f"${cpm:,.2f}"),
]

print(f"REPORTE · {canal}")
print("-" * 32)
for etiqueta, valor in metricas:
    print(f"{etiqueta:<18}{valor:>13}")
print("-" * 32)
"""),

md("""
`:<18` alinea a la izquierda en dieciocho espacios y `:>13` a la derecha en trece. Los dos juntos
son lo que hace que la columna de números quede pareja.

Alinear números a la derecha no es capricho: los dígitos de las unidades quedan uno debajo de
otro y las magnitudes se comparan de un vistazo.

## Cuatro errores de entrada y salida

**Olvidar la `f`.** Sin ella la cadena imprime las llaves literales. No es un error, es una
salida silenciosamente inútil.
"""),

code("""
# FALLA A PROPÓSITO. Falta la f del principio.
print("Costo por clic: {cpc:,.2f}")
print(f"Costo por clic: {cpc:,.2f}")
"""),

md("""
**Convertir después de operar.** Ya lo viste en el bloque 2: `int` va envolviendo al `input`, no
al resultado.

**Un `input` sin mensaje.** El programa se queda esperando con la pantalla en blanco y parece
congelado. Quien lo usa no sabe si tiene que escribir algo o si se trabó.

**Imprimir sin etiqueta ni unidad.** Un `7.59` suelto no dice si son pesos, clics o días. Quien
lo lea va a preguntar, y preguntar cuesta más que escribir la etiqueta.
"""),

code("""
print("Sin etiqueta:")
print(cpc)

print()
print("Con etiqueta y unidad:")
print(f"Costo por clic: ${cpc:,.2f} MXN")
"""),

md("""
---
# Ejercicios

Las soluciones están hasta abajo del cuaderno.

**Sobre `input` en los ejercicios**: si un ejercicio pide capturar por teclado, escríbelo con
`input` de verdad y córrelo tú, celda por celda. No lo pongas arriba en el cuaderno o cada
"Ejecutar todo" se va a detener ahí.

## Entrada, proceso, salida

### Ejercicio 1 · Las tres partes separadas

Escribe un programa en tres celdas: una con los datos de una campaña, una con los cálculos y una
con la salida. Después cambia solo los datos de la primera y vuelve a correr las tres.

Si tuviste que tocar la segunda o la tercera para que funcionara, las partes no estaban bien
separadas.

### Ejercicio 2 · Simular la captura

Sin usar `input`, escribe una lista `RESPUESTAS` con lo que una persona habría tecleado, y un
programa que la recorra, convierta cada valor a su tipo y arme un diccionario de campaña.

Incluye a propósito una respuesta mal escrita, como `"5,074"`, y haz que el programa diga cuál no
pudo convertir en lugar de tronar.

### Ejercicio 3 · La captura de verdad

En una celda nueva al final del cuaderno, escribe la versión con `input` del ejercicio anterior:
que pida canal, impresiones, clics e inversión, y calcule las tres métricas.

Córrela tú, a mano. Que cada `input` traiga un mensaje que diga qué se espera y en qué unidad.

## Formato

### Ejercicio 4 · Los cinco códigos

Toma el número `148230.5678` e imprímelo cinco veces, una con cada código de la tabla. Después
explica en un comentario cuál usarías para dinero, cuál para un conteo y por qué.

### Ejercicio 5 · De crudo a presentable

Estos son los valores crudos de tres campañas. Imprímelos como una tabla alineada, con
separador de miles, porcentaje con dos decimales y símbolo de moneda.

```python
CRUDAS = [
    ("Instagram", 148230, 5074, 38500.00),
    ("Facebook", 96400, 2891, 21300.00),
    ("Google", 210500, 9840, 74200.00),
]
```

La tabla tiene que tener encabezado y una línea de total abajo.

### Ejercicio 6 · El porcentaje doble

Escribe dos líneas que impriman la tasa de conversión de Instagram: una correcta y una con el
error de multiplicar por cien además de pedir el formato de porcentaje.

Después di, en un comentario, cómo se detecta ese error leyendo solo la salida.

## Cierre

### Ejercicio 7 · Un reporte que se pueda mandar

Escribe un programa que produzca un reporte de cinco líneas de una campaña, con miles,
porcentaje y símbolo de moneda donde corresponda. Nada de concatenar con el signo de más.

La prueba: enséñaselo a alguien que no tomó la clase. Si pregunta qué es un número, falta una
etiqueta.
"""),

md("""
---
## Tres ideas para llevarse

**Entrada, proceso y salida.** Separar las tres partes es lo que después te deja encontrar en
cuál se rompió el programa, y cambiar una sin arriesgar las otras.

**`input` siempre devuelve texto.** Convertir es tu responsabilidad, y hacerlo tarde no arregla
la operación ya hecha. `int(input(...))`, no `int(...)` al final.

**El formato es parte del resultado.** Un `0.03423` correcto y un `3.42%` correcto no valen lo
mismo para quien recibe el reporte.

La siguiente sesión es cómo hacer que el programa tome caminos distintos según los datos.
"""),

md("""
---
# Soluciones

### Ejercicio 1

```python
# Celda 1, entrada
canal = "Google"
impresiones = 210500
clics = 9840
inversion = 74200.00

# Celda 2, proceso
conversion = clics / impresiones
cpc = inversion / clics
cpm = inversion / impresiones * 1000

# Celda 3, salida
print(f"Canal: {canal}")
print(f"Conversión: {conversion:.2%}")
print(f"Costo por clic: ${cpc:,.2f}")
print(f"Costo por mil: ${cpm:,.2f}")
```

Cambiar la primera celda y volver a correr las tres da otro reporte sin tocar una sola línea de
cálculo. Esa es toda la ventaja de separarlas, y se nota más cuanto más largo es el programa.

### Ejercicio 2

```python
RESPUESTAS = ["Instagram", "148230", "5,074", "38500"]
CAMPOS = [("canal", str), ("impresiones", int), ("clics", int), ("inversion", float)]

campana = {}
problemas = []

for (nombre, tipo), escrito in zip(CAMPOS, RESPUESTAS):
    try:
        campana[nombre] = tipo(escrito)
    except ValueError:
        campana[nombre] = None
        problemas.append(f"{nombre}: no pude convertir {escrito!r}")

print(campana)
for p in problemas:
    print("Problema ->", p)
```

`"5,074"` no convierte por la coma, así que `clics` queda en `None` y el programa lo reporta en
lugar de detenerse. Guardar la función de conversión junto al nombre del campo, en `CAMPOS`, es
lo que evita escribir cuatro `try` iguales.

### Ejercicio 3

```python
canal = input("Canal de la campaña: ")
impresiones = int(input("Impresiones (solo dígitos): "))
clics = int(input("Clics (solo dígitos): "))
inversion = float(input("Inversión en pesos, sin símbolo: "))

conversion = clics / impresiones
cpc = inversion / clics
cpm = inversion / impresiones * 1000

print(f"\\nCanal: {canal}")
print(f"Conversión: {conversion:.2%}")
print(f"Costo por clic: ${cpc:,.2f}")
print(f"Costo por mil: ${cpm:,.2f}")
```

Los mensajes dicen la unidad y el formato esperado: "solo dígitos" y "sin símbolo". Eso evita la
mitad de los `ValueError` sin escribir una sola validación, porque la mayoría de los errores de
captura son de gente que no sabía qué se le pedía.

### Ejercicio 4

```python
n = 148230.5678

print(f"{n:,}")
print(f"{n:.2f}")
print(f"{n:,.2f}")
print(f"{n / 1000000:.1%}")
print(f"[{n:>16,.2f}]")

# Para dinero, :,.2f. Los centavos siempre visibles y los miles separados, que es
# como se lee una cifra en un estado de cuenta.
# Para un conteo, :, y nada más. Las impresiones no tienen mitades, y escribir
# 148,230.00 sugiere una precisión que no existe.
```

El detalle de los decimales en un conteo importa más de lo que parece. Un `.00` en algo que se
cuenta hace dudar de si el dato es un promedio.

### Ejercicio 5

```python
CRUDAS = [
    ("Instagram", 148230, 5074, 38500.00),
    ("Facebook", 96400, 2891, 21300.00),
    ("Google", 210500, 9840, 74200.00),
]

print(f"{'Canal':<12}{'Impresiones':>13}{'Clics':>9}{'Conv.':>8}{'Inversión':>13}{'CPC':>9}")
print("-" * 64)

for canal, impr, clics, inv in CRUDAS:
    print(f"{canal:<12}{impr:>13,}{clics:>9,}{clics / impr:>8.2%}"
          f"{inv:>13,.2f}{inv / clics:>9.2f}")

print("-" * 64)
tot_impr = sum(c[1] for c in CRUDAS)
tot_clics = sum(c[2] for c in CRUDAS)
tot_inv = sum(c[3] for c in CRUDAS)
print(f"{'Total':<12}{tot_impr:>13,}{tot_clics:>9,}{tot_clics / tot_impr:>8.2%}"
      f"{tot_inv:>13,.2f}{tot_inv / tot_clics:>9.2f}")
```

Ojo con el renglón de total: la conversión total **no** es el promedio de las tres conversiones,
es el total de clics entre el total de impresiones. Promediar porcentajes de bases distintas es
uno de los errores más comunes de un reporte, y aquí se evita calculando desde los totales.

### Ejercicio 6

```python
conversion = 5074 / 148230

print(f"Correcto: {conversion:.2%}")
print(f"Con el error: {conversion * 100:.2%}")

# Se detecta por el tamaño. Una tasa de conversión de 342% es imposible: significa
# que hubo más de tres conversiones por cada impresión. Cualquier porcentaje por
# arriba de cien en una métrica que es "una parte de un total" es este error,
# hasta que se demuestre lo contrario.
```

Vale la pena tener ese reflejo: un porcentaje mayor a cien en una métrica de proporción casi
siempre es una multiplicación de más.

### Ejercicio 7

No hay solución única. Se califica sobre cuatro cosas: que las cinco líneas usen f-strings y
ninguna concatenación, que los miles estén separados, que la tasa venga como porcentaje y no
como decimal, y que cada número traiga etiqueta y unidad.

La prueba de enseñárselo a alguien que no tomó la clase es la que de verdad decide. Un número
sin unidad siempre genera la misma pregunta, y esa pregunta es la calificación.
"""),

]

write(OUT / "es" / "w05.ipynb", es)
print("wrote", OUT / "es" / "w05.ipynb")


en = [

md("""
# Data Analysis · Week 5
## Statements, input and output

**TIA502 · School of Business · Instructor David Escobar-Castillejos**

A correct number badly presented is a number nobody will use. This session is about how data
gets into the program, how results get out, and how they get presented so they can be understood
without you standing there explaining them.

By the end of this notebook you will be able to:

1. Classify the four kinds of statement and say what each is for.
2. Read data from the keyboard with `input`, converting before operating.
3. Compose text with f-strings, mixing fixed text and computed values.
4. Format a number with a thousands separator, fixed decimals and percentages.
5. Write output with labels, alignment and units.

### A warning about `input` in Colab

`input` stops the notebook and opens a text box above the cell. Until you type something and
press Enter, **nothing else runs**.

That is why this notebook has **exactly one cell with a real `input`**, clearly marked, and
everything else uses values already assigned. That way you can use "Run all" without it sitting
there waiting.

Four cells fail on purpose and carry a comment saying so.
"""),

md("""
---
# Block 1 · What a line can do

Four kinds of statement, and any program this term is built from them.

| Kind | What it does | Example |
|---|---|---|
| Assignment | Stores a value in a name | `clicks = 5074` |
| Input | Brings a value in from outside the program | `channel = input("Channel: ")` |
| Output | Shows a result | `print(cost_per_click)` |
| Control | Decides or repeats | `if`, `else`, `while`, `for` |

The first three are today's. Control arrives next week.

## A program is input, process and output

The whole structure fits in three parts. First you get the data, whether from the keyboard, from
a file or written into the code itself. Then you compute the results. At the end you show them.

When a program does not work, the first useful question is **which of the three parts it broke
in**.
"""),

code("""
# INPUT: the data, written into the code here.
channel = "Instagram"
impressions = 148230
clicks = 5074
spend = 38500.00

# PROCESS: the arithmetic, printing nothing.
conversion = clicks / impressions
cost_per_click = spend / clicks

# OUTPUT: showing only. No arithmetic happens here.
print(channel, conversion, cost_per_click)
"""),

md("""
Mixing the three parts is what stops you testing them. If the calculation is tangled up with the
`print` calls, you cannot check the number without rerunning everything and reading the screen.

Kept apart, each part can be checked on its own. You can change the input data without touching
the arithmetic, and change the presentation without risking the numbers.
"""),

code("""
# I change only the input. The process and the output stay as they were.
channel = "Facebook"
impressions = 96400
clicks = 2891
spend = 21300.00

conversion = clicks / impressions
cost_per_click = spend / clicks

print(channel, conversion, cost_per_click)
"""),

md("""
---
# Block 2 · Getting data in

Everything that arrives from outside arrives as text. Without exception, and without warning.

## The only `input` cell in this notebook

This is the real thing. In Colab it opens a text box above the cell and waits for you to type
something.

If you are reading the notebook straight through and do not want to stop, skip it: the cell below
does the same with values already set.
"""),

code("""
# THIS CELL WAITS FOR YOU. In Colab it opens a text box above.
# The try is so that a headless "Run all" falls through instead of hanging.
try:
    captured_channel = input("Campaign channel: ")
    captured_clicks = int(input("Clicks recorded: "))
    captured_spend = float(input("Spend in pesos: "))
except Exception:
    print("(no keyboard available, using example values)")
    captured_channel, captured_clicks, captured_spend = "Instagram", 5074, 38500.0

print(captured_channel, captured_spend / captured_clicks)
"""),

md("""
Three things in that cell deserve naming.

**The message.** Whatever goes inside `input` is shown before it waits. Without it the program
sits still with a blank screen and looks frozen.

**The conversion.** `int` and `float` wrap the `input`. The channel is not converted because it
is already text.

**The order.** The program stops at each `input` until somebody types something and presses
Enter. Three `input` calls are three stops.

## Why `input` returns text, always

From here on everything uses values already assigned. But it is worth seeing what would have
happened without the conversion, and that can be simulated with no keyboard.
"""),

code("""
# What input would have returned: text, even when the user types digits.
raw_answer = "5074"

print(raw_answer, type(raw_answer))
print("Converted:", int(raw_answer), type(int(raw_answer)))
"""),

code("""
# FAILS ON PURPOSE. Without converting, addition glues the strings together.
clicks_text = "5074"
new_text = "320"

print("Unconverted:", clicks_text + new_text)
print("Converted:  ", int(clicks_text) + int(new_text))
"""),

md("""
Neither line raises an error. The first answers something useless, and that is the difference
between a broken program and a dangerous one.

## Converting late fixes nothing

This is the specific error that turns up most in the first keyboard assignment: wrapping the
result instead of the `input`.
"""),

code("""
# FAILS ON PURPOSE. The conversion arrives after the operation.
a = "5074"
b = "320"

wrong = int(a + b)          # glued first, converted afterwards
right = int(a) + int(b)     # converted first, added afterwards

print("Converting at the end:  ", wrong)
print("Converting at the start:", right)
"""),

md("""
`int(a + b)` gave 5,074,320, and it did not even raise, because `"5074320"` is a perfectly valid
integer.

The conversion goes tight around the `input`, not around the result. It is the difference
between `int(input(...))` and `int(...)` at the very end.

## When the user types anything at all
"""),

code("""
# FAILS ON PURPOSE. int() on something that is not a number.
for typed in ["5074", "5,074", "five thousand", "5074.0", ""]:
    try:
        print(f"int({typed!r:16}) -> {int(typed)}")
    except ValueError as e:
        print(f"int({typed!r:16}) -> ValueError: {e}")
"""),

md("""
Four out of five fail, and all four are things a person would type perfectly naturally.

For now it is enough to know it can happen. Next week, with `if`, you will be able to check
before converting; in week 9, with `while`, you will be able to ask again until the answer is
usable.

## Reading several values without repeating code

One way to work with the keyboard without filling the program with `input` calls: gather the
fields into one structure and capture them in a loop. Simulated here with answers already
written.
"""),

code("""
# Simulation: what a person would have typed, in the order they were asked.
ANSWERS = ["Instagram", "148230", "5074", "38500"]

labels = ["Channel", "Impressions", "Clicks", "Spend"]
data = {}

for label, typed in zip(labels, ANSWERS):
    print(f"{label}: {typed}")
    data[label] = typed

print()
print(data)
"""),

md("""
Note that every value in the dictionary is text, even the ones that are digits. The conversion is
still pending and still your job.
"""),

code("""
campaign = {
    "channel": data["Channel"],
    "impressions": int(data["Impressions"]),
    "clicks": int(data["Clicks"]),
    "spend": float(data["Spend"]),
}

for name, value in campaign.items():
    print(f"{name:<14} {str(value):<12} {type(value).__name__}")
"""),

md("""
---
# Block 3 · Getting results out

A correct number badly presented is a number nobody will use.

Compare. Both values below are correct and neither is any use in a report.
"""),

code("""
impressions = 148230
clicks = 5074
spend = 38500.00

conversion = clicks / impressions
cpc = spend / clicks

print("Conversion:", conversion)
print("Cost:", cpc)
"""),

md("""
`0.034230587600350804` and `7.587702010248325`. Nobody is reading that in a meeting.

## f-strings

A string that starts with `f` lets you put values inside the text, wrapped in braces. Whatever
goes inside the braces is evaluated and replaced by its result.

It replaces concatenating with plus signs, which forces you to convert everything to text by hand
and becomes unreadable the moment there are three values.
"""),

code("""
channel = "Instagram"

# The old way, with concatenation.
print("Channel: " + channel + ", clicks: " + str(clicks))

# The way this course does it.
print(f"Channel: {channel}, clicks: {clicks}")
"""),

md("""
Look at the `str(clicks)` in the first one. Without it, concatenating text and a number raises an
error. The f-string converts on its own.

Inside the braces you can put a variable or a whole expression.
"""),

code("""
print(f"Cost per click: {spend / clicks}")
print(f"The channel has {len(channel)} letters")
print(f"Good campaign? {conversion > 0.03}")
"""),

md("""
## The five format codes

After a colon goes how the number looks. It is the same kind of code as a spreadsheet's cell
format, only written out instead of picked from a menu.

| Code | What it does | Input | Comes out as |
|---|---|---|---|
| `:,` | Thousands separator | `148230` | `148,230` |
| `:.2f` | Two fixed decimals | `7.588490` | `7.59` |
| `:,.2f` | Thousands and two decimals | `38500` | `38,500.00` |
| `:.1%` | Percentage with one decimal | `0.0342` | `3.4%` |
| `:>10` | Right aligned in ten spaces | `5074` | `      5074` |
"""),

code("""
print(f"{148230:,}")
print(f"{7.588490:.2f}")
print(f"{38500:,.2f}")
print(f"{0.0342:.1%}")
print(f"[{5074:>10}]")
"""),

md("""
**Predict before you run.** What does this line print?

- **A.** `Conversion: 0.0%`
- **B.** `Conversion: 3.4%`
- **C.** `Conversion: 0.034%`
- **D.** `Conversion: 34.2%`
"""),

code("""
rate = 0.0342

print(f"Conversion: {rate:.1%}")
"""),

md("""
The answer is **B**. The percentage code **already multiplies by a hundred**, so you do not have
to. Multiplying it yourself as well is the error that produces option D.
"""),

code("""
# FAILS ON PURPOSE. Multiplying and asking for a percentage as well.
print(f"Correct: {rate:.1%}")
print(f"Double:  {rate * 100:.1%}")
"""),

md("""
Three hundred and forty-two per cent conversion. No campaign converts like that, and the program
prints it without protest all the same.

## Formatting does not change the value

It matters and it gets forgotten: the format code affects how that line looks, not what is
stored.
"""),

code("""
print(f"Formatted: {cpc:.2f}")
print(f"The value is still: {cpc}")
print(f"And it still calculates: {cpc * 30:.2f} over thirty clicks")
"""),

md("""
Just as giving a cell a currency format does not change what is inside it.

If you genuinely want to change the value, that is `round`, and they are different things.
"""),

code("""
rounded = round(cpc, 2)

print("Formatted:", f"{cpc:.2f}", "· original value:", cpc)
print("Rounded:  ", rounded, "· the decimals are gone for good")
"""),

md("""
## A complete report
"""),

code("""
channel = "Instagram"
impressions = 148230
clicks = 5074
spend = 38500.00

conversion = clicks / impressions
cpc = spend / clicks
cpm = spend / impressions * 1000

print(f"Channel: {channel}")
print(f"Impressions: {impressions:,}")
print(f"Conversion: {conversion:.2%}")
print(f"Cost per click: ${cpc:,.2f}")
print(f"Cost per thousand: ${cpm:,.2f}")
"""),

md("""
The currency sign is fixed text inside the string, and so is the label. Anything not inside braces
prints exactly as written.

## Lining up a column

When there are several metrics, aligning them turns a list into a table.
"""),

code("""
metrics = [
    ("Impressions", f"{impressions:,}"),
    ("Clicks", f"{clicks:,}"),
    ("Conversion", f"{conversion:.2%}"),
    ("Cost per click", f"${cpc:,.2f}"),
    ("Cost per thousand", f"${cpm:,.2f}"),
]

print(f"REPORT · {channel}")
print("-" * 34)
for label, value in metrics:
    print(f"{label:<20}{value:>13}")
print("-" * 34)
"""),

md("""
`:<20` aligns left in twenty spaces and `:>13` aligns right in thirteen. The two together are what
keeps the column of numbers even.

Right-aligning numbers is not a whim: the units digits end up one under another and the magnitudes
compare at a glance.

## Four input and output errors

**Forgetting the `f`.** Without it the string prints the literal braces. It is not an error, it is
silently useless output.
"""),

code("""
# FAILS ON PURPOSE. The leading f is missing.
print("Cost per click: {cpc:,.2f}")
print(f"Cost per click: {cpc:,.2f}")
"""),

md("""
**Converting after operating.** You saw it in block 2: `int` wraps the `input`, not the result.

**An `input` with no message.** The program sits waiting with a blank screen and looks frozen.
Whoever is using it does not know whether to type something or whether it crashed.

**Printing with no label and no unit.** A bare `7.59` does not say whether it is pesos, clicks or
days. Whoever reads it will ask, and asking costs more than writing the label.
"""),

code("""
print("Without a label:")
print(cpc)

print()
print("With a label and a unit:")
print(f"Cost per click: ${cpc:,.2f} MXN")
"""),

md("""
---
# Exercises

The solutions sit at the very bottom of the notebook.

**About `input` in the exercises**: if an exercise asks for keyboard capture, write it with a real
`input` and run it yourself, cell by cell. Do not put it higher up in the notebook or every "Run
all" will stop there.

## Input, process, output

### Exercise 1 · The three parts kept apart

Write a program across three cells: one with the campaign data, one with the calculations and one
with the output. Then change only the first and run all three again.

If you had to touch the second or the third to make it work, the parts were not properly
separated.

### Exercise 2 · Simulating the capture

Without using `input`, write an `ANSWERS` list holding what a person would have typed, and a
program that walks it, converts each value to its type and builds a campaign dictionary.

Include a badly typed answer on purpose, such as `"5,074"`, and make the program say which one it
could not convert rather than blowing up.

### Exercise 3 · The real capture

In a new cell at the end of the notebook, write the `input` version of the previous exercise: it
should ask for channel, impressions, clicks and spend, and compute the three metrics.

Run it yourself, by hand. Make every `input` carry a message saying what is expected and in what
unit.

## Formatting

### Exercise 4 · The five codes

Take the number `148230.5678` and print it five times, once with each code from the table. Then
explain in a comment which one you would use for money, which for a count, and why.

### Exercise 5 · From raw to presentable

These are the raw values for three campaigns. Print them as an aligned table, with a thousands
separator, a percentage to two decimals and a currency symbol.

```python
RAW = [
    ("Instagram", 148230, 5074, 38500.00),
    ("Facebook", 96400, 2891, 21300.00),
    ("Google", 210500, 9840, 74200.00),
]
```

The table needs a header and a total line at the bottom.

### Exercise 6 · The double percentage

Write two lines that print Instagram's conversion rate: one correct and one with the error of
multiplying by a hundred as well as asking for the percentage format.

Then say, in a comment, how that error can be spotted from the output alone.

## Closing

### Exercise 7 · A report you could send

Write a program that produces a five-line report for a campaign, with thousands, percentage and a
currency symbol where they belong. No concatenating with plus signs.

The test: show it to somebody who did not take the class. If they ask what a number is, a label is
missing.
"""),

md("""
---
## Three ideas to take away

**Input, process and output.** Keeping the three parts apart is what later lets you find which one
the program broke in, and change one without risking the others.

**`input` always returns text.** Converting is your responsibility, and doing it late does not fix
an operation already performed. `int(input(...))`, not `int(...)` at the very end.

**Formatting is part of the result.** A correct `0.03423` and a correct `3.42%` are not worth the
same to whoever receives the report.

Next session is how to make the program take different paths depending on the data.
"""),

md("""
---
# Solutions

### Exercise 1

```python
# Cell 1, input
channel = "Google"
impressions = 210500
clicks = 9840
spend = 74200.00

# Cell 2, process
conversion = clicks / impressions
cpc = spend / clicks
cpm = spend / impressions * 1000

# Cell 3, output
print(f"Channel: {channel}")
print(f"Conversion: {conversion:.2%}")
print(f"Cost per click: ${cpc:,.2f}")
print(f"Cost per thousand: ${cpm:,.2f}")
```

Changing the first cell and running all three gives a different report without touching a single
line of arithmetic. That is the whole advantage of keeping them apart, and it shows more the longer
the program gets.

### Exercise 2

```python
ANSWERS = ["Instagram", "148230", "5,074", "38500"]
FIELDS = [("channel", str), ("impressions", int), ("clicks", int), ("spend", float)]

campaign = {}
problems = []

for (name, kind), typed in zip(FIELDS, ANSWERS):
    try:
        campaign[name] = kind(typed)
    except ValueError:
        campaign[name] = None
        problems.append(f"{name}: could not convert {typed!r}")

print(campaign)
for p in problems:
    print("Problem ->", p)
```

`"5,074"` does not convert because of the comma, so `clicks` ends up as `None` and the program
reports it instead of stopping. Storing the conversion function alongside the field name, in
`FIELDS`, is what saves writing four identical `try` blocks.

### Exercise 3

```python
channel = input("Campaign channel: ")
impressions = int(input("Impressions (digits only): "))
clicks = int(input("Clicks (digits only): "))
spend = float(input("Spend in pesos, no symbol: "))

conversion = clicks / impressions
cpc = spend / clicks
cpm = spend / impressions * 1000

print(f"\\nChannel: {channel}")
print(f"Conversion: {conversion:.2%}")
print(f"Cost per click: ${cpc:,.2f}")
print(f"Cost per thousand: ${cpm:,.2f}")
```

The messages state the unit and the expected format: "digits only" and "no symbol". That prevents
half the `ValueError`s without writing a single validation, because most capture errors come from
people who did not know what was being asked of them.

### Exercise 4

```python
n = 148230.5678

print(f"{n:,}")
print(f"{n:.2f}")
print(f"{n:,.2f}")
print(f"{n / 1000000:.1%}")
print(f"[{n:>16,.2f}]")

# For money, :,.2f. Cents always visible and thousands separated, which is how a
# figure reads on a statement.
# For a count, :, and nothing more. Impressions have no halves, and writing
# 148,230.00 suggests a precision that does not exist.
```

The detail about decimals on a count matters more than it looks. A `.00` on something that gets
counted makes people wonder whether the value is an average.

### Exercise 5

```python
RAW = [
    ("Instagram", 148230, 5074, 38500.00),
    ("Facebook", 96400, 2891, 21300.00),
    ("Google", 210500, 9840, 74200.00),
]

print(f"{'Channel':<12}{'Impressions':>13}{'Clicks':>9}{'Conv.':>8}{'Spend':>13}{'CPC':>9}")
print("-" * 64)

for channel, impr, clicks, spend in RAW:
    print(f"{channel:<12}{impr:>13,}{clicks:>9,}{clicks / impr:>8.2%}"
          f"{spend:>13,.2f}{spend / clicks:>9.2f}")

print("-" * 64)
tot_impr = sum(r[1] for r in RAW)
tot_clicks = sum(r[2] for r in RAW)
tot_spend = sum(r[3] for r in RAW)
print(f"{'Total':<12}{tot_impr:>13,}{tot_clicks:>9,}{tot_clicks / tot_impr:>8.2%}"
      f"{tot_spend:>13,.2f}{tot_spend / tot_clicks:>9.2f}")
```

Careful with the total row: the overall conversion is **not** the average of the three
conversions, it is total clicks over total impressions. Averaging percentages with different
bases is one of the commonest errors in a report, and it is avoided here by computing from the
totals.

### Exercise 6

```python
conversion = 5074 / 148230

print(f"Correct: {conversion:.2%}")
print(f"With the error: {conversion * 100:.2%}")

# You spot it by the size. A conversion rate of 342% is impossible: it would mean
# more than three conversions per impression. Any percentage above a hundred in a
# metric that is "a part of a total" is this error until proven otherwise.
```

That reflex is worth having: a percentage above a hundred in a proportion metric is almost always
one multiplication too many.

### Exercise 7

There is no single solution. It is graded on four things: that all five lines use f-strings and no
concatenation, that the thousands are separated, that the rate comes out as a percentage rather
than a decimal, and that every number carries a label and a unit.

The test of showing it to somebody who did not take the class is what really decides. A number
with no unit always draws the same question, and that question is the grade.
"""),

]

write(OUT / "en" / "w05.ipynb", en)
print("wrote", OUT / "en" / "w05.ipynb")
