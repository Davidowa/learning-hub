"""notebooks/analisis-de-datos/{es,en}/w01.1.ipynb

Source deck: ppts/python/analisis-de-datos/{es,en}/w01.1.*.yaml
The bridge session. No repository source: the deck's own code, verified here.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from nbkit import md, code, write, bootstrap_cell, REPO

OUT = REPO / "notebooks" / "analisis-de-datos"

# ════════════════════════════════════════════════════════════════════ ESPAÑOL

es = [

md("""
# Análisis de Datos · Semana 1 · Puente
## De Excel a Python

**TIA502 · Facultad de Empresariales · Profesor David Escobar-Castillejos**

Este cuaderno no empieza de cero, porque tú tampoco. Si ya armaste una fórmula en una hoja de
cálculo, ya programaste: tomaste datos, aplicaste una operación y guardaste el resultado en un
lugar con nombre. Python no te pide una idea nueva. Te pide escribir esa misma idea de otra
forma.

Al terminar este cuaderno vas a poder:

1. Traducir una fórmula de hoja de cálculo a una expresión de Python.
2. Nombrar los datos en lugar de señalarlos, y decir por qué eso importa.
3. Reconocer los cuatro puntos donde la analogía con Excel se rompe.
4. Resumir una tabla de doce meses sin abrir la hoja de cálculo.
5. Explicar qué deja de poder una hoja cuando la tabla crece.

### Cómo se usa este cuaderno

Este es tu primer contacto con código que corre. Para ejecutar una celda, haz clic en ella y
presiona **Shift + Enter**. El resultado aparece justo debajo.

Ejecuta las celdas en orden, de arriba hacia abajo. Varias usan un valor que definió la
anterior, así que saltarte una da un error que no tiene que ver con el tema.

Dos celdas fallan a propósito, para que veas cómo se ve un error antes de encontrártelo solo.
Llevan un comentario que lo dice.
"""),

md("""
---
# Bloque 1 · Ya programas, solo que en otra sintaxis

Una hoja de cálculo es un lenguaje. Tiene valores, nombres, funciones y condiciones. Lo que
cambia es dónde se escribe.

| Concepto | En la hoja de cálculo | En Python |
|---|---|---|
| Dato con nombre | Una celda con nombre | Una variable |
| Fórmula | Precio por cantidad | `importe = precio * cantidad` |
| Función | `PROMEDIO` sobre un rango | `mean()` sobre una lista |
| Condición | `SI` con dos salidas | `if` y `else` |
| Columna | El rango `B2:B500` | Una lista |
| Tabla de búsqueda | `BUSCARV` en un catálogo | Un diccionario |
| La hoja completa | Filas, columnas y encabezados | Un `DataFrame` |

Las últimas tres se ven completas más adelante en el semestre. Las cuatro primeras empiezan
hoy.

## Una fórmula ya es un programa

En la hoja escribirías `=B2*C2`. La celda toma dos datos, los multiplica y guarda el resultado
donde escribiste la fórmula.

En Python es lo mismo, con una diferencia: el resultado va a un nombre que tú eliges, no a una
celda que la posición te impuso.
"""),

code("""
precio = 8990.0
cantidad = 3

importe = precio * cantidad

print(importe)
"""),

md("""
Esas tres líneas son la fórmula completa. `precio` y `cantidad` son los datos de entrada,
`precio * cantidad` es la operación, e `importe` es el nombre donde vive el resultado.

Fíjate en el signo igual, porque es la única diferencia de puntuación que importa hoy. **El
igual de la hoja abre una fórmula. El igual de Python guarda un resultado.**

Y una vez que el resultado tiene nombre, ese nombre se usa en la línea siguiente.
"""),

code("""
iva = importe * 0.16
total = importe + iva

print("Importe:", importe)
print("IVA:    ", iva)
print("Total:  ", total)
"""),

md("""
### Por qué el nombre importa más de lo que parece

`B7` no dice nada. Dentro de seis meses, abriendo tu propia hoja, vas a tener que rastrear de
dónde salió esa celda para saber qué guarda.

`total_con_iva` sí dice algo. Es la diferencia entre un archivo que puedes retomar y uno que
tienes que reconstruir.
"""),

code("""
# Los mismos números, con nombres que se explican solos.
precio_unitario = 8990.0
piezas_vendidas = 3
subtotal = precio_unitario * piezas_vendidas
total_con_iva = subtotal * 1.16

print(f"{piezas_vendidas} piezas a {precio_unitario:,.2f} dan {total_con_iva:,.2f} con IVA")
"""),

md("""
Esa última línea usa una **f-string**: el texto empieza con `f` y todo lo que va entre llaves
se sustituye por su valor. El `:,.2f` es formato, y dice "sepárame los miles con comas y
déjame dos decimales". Es lo mismo que darle formato de moneda a una celda.

## Las mismas cuatro operaciones, escritas dos veces

En la hoja:

```
=B2*C2
=SUMA(D2:D13)
=PROMEDIO(D2:D13)
=SI(D2>50000; "meta"; "abajo")
```

En Python, con las mismas cuentas:
"""),

code("""
importes = [42000, 51500, 38900, 60100, 55300, 47800]

total = sum(importes)
promedio = total / len(importes)
estado = "meta" if importes[0] > 50000 else "abajo"

print("Total:   ", total)
print("Promedio:", round(promedio, 2))
print("Enero:   ", estado)
"""),

md("""
`sum` es `SUMA`, `len` es `CONTAR`, y la división que las junta es la de siempre.

La última línea se lee casi como se dice en voz alta: *"meta" si el importe pasa de 50000, y
si no, "abajo"*. Es el `SI` de la hoja, con las partes en otro orden.

## Una columna es una lista

El rango `B2:B500` de tu hoja es, en Python, una lista: valores en orden, dentro de un solo
nombre.
"""),

code("""
meses = ["ene", "feb", "mar", "abr", "may", "jun"]
ventas = [42000, 51500, 38900, 60100, 55300, 47800]

print("Cuántos meses:", len(meses))
print("Cuántas ventas:", len(ventas))
print("El primer mes:", meses[0])
print("La primera venta:", ventas[0])
"""),

md("""
Dos listas, dos columnas. La posición 0 de una corresponde a la posición 0 de la otra, igual
que la fila 2 de la columna B corresponde a la fila 2 de la columna C.

Ese emparejamiento por posición es cómodo y también frágil, y es exactamente el problema que
`pandas` viene a resolver en la semana 15.
"""),

# ──────────────────────────────────────────────────────────── bloque 2

md("""
---
# Bloque 2 · Dónde deja de parecerse

Cuatro diferencias reales. Ninguna es difícil, y todas cuestan una tarde si nadie las dice a
tiempo.

| Punto | En la hoja de cálculo | En Python |
|---|---|---|
| Primer elemento | La fila número 1 | El índice 0 |
| Recálculo | Automático al cambiar un dato | Solo cuando vuelves a ejecutar |
| Tipos | La celda adivina el formato | El valor tiene tipo y no se adivina |
| Rastro | El clic no queda registrado | El script es la receta completa |
| Tamaño | Se arrastra y deja de responder | Millones de filas sin problema |

## Quiebre 1 · El índice empieza en cero

Este es el que más tiempo cuesta en las primeras semanas.
"""),

code("""
print("meses[0] es", meses[0])
print("meses[1] es", meses[1])
print("meses[5] es", meses[5])
print()
print("La lista tiene", len(meses), "elementos, y el último índice es", len(meses) - 1)
"""),

md("""
**Predice antes de correr.** La lista de abajo tiene doce meses. ¿Qué imprime `meses_12[12]`?

- **A.** `dic`, porque diciembre es el mes número doce.
- **B.** `ene`, porque la lista vuelve a empezar.
- **C.** `IndexError`, porque el último índice es 11.
- **D.** `None`, porque esa posición está vacía.
"""),

code("""
# FALLA A PROPÓSITO. Doce elementos van del índice 0 al 11.
meses_12 = ["ene", "feb", "mar", "abr", "may", "jun",
            "jul", "ago", "sep", "oct", "nov", "dic"]

try:
    print(meses_12[12])
except IndexError as e:
    print("IndexError:", e)

print()
print("Diciembre está en:", meses_12[11])
print("Y también en:     ", meses_12[-1], "· el índice negativo cuenta desde el final")
"""),

md("""
La respuesta es **C**. Doce elementos van del 0 al 11, así que el 12 se sale.

El índice negativo es un regalo que la hoja de cálculo no tiene: `-1` es el último, `-2` el
penúltimo, y no necesitas saber cuántos hay.

## Quiebre 2 · Nada se recalcula solo

En la hoja, cambias B2 y todo lo que dependía de B2 se actualiza al instante. En Python no.
"""),

code("""
precio = 100
cantidad = 5
importe = precio * cantidad

print("Importe calculado:", importe)

# Ahora cambio el precio, como si hubiera corregido una celda.
precio = 200

print("Precio ahora:     ", precio)
print("Importe sigue en: ", importe, "· nadie lo volvió a calcular")
"""),

md("""
`importe` guarda el resultado de una multiplicación que ya ocurrió, no la instrucción para
repetirla. Para actualizarlo hay que volver a ejecutar la operación.
"""),

code("""
importe = precio * cantidad
print("Importe recalculado:", importe)
"""),

md("""
Esto suena a desventaja y es lo contrario. Significa que el orden en que corren las líneas es
tuyo, y que un número no cambia bajo tus pies mientras trabajas. En una hoja grande, un
recálculo automático puede tardar y puede sorprenderte; aquí no pasa nada hasta que tú lo
pides.

En un cuaderno de Colab hay una consecuencia práctica: **el orden en que ejecutas las celdas
es el orden que cuenta**, no el orden en que están escritas. Si corres una celda de más
abajo y luego una de más arriba, el estado es el que dejó la última que corriste. Por eso el
cuaderno se ejecuta de arriba hacia abajo.

## Quiebre 3 · El valor tiene tipo, y el tipo no se adivina

Una celda de Excel adivina. Escribes `01000` y decide si eso es un número o un texto, y a
veces decide mal.

En Python el tipo es explícito y se puede preguntar.
"""),

code("""
print(type(42000))
print(type(42000.5))
print(type("42000"))
print(type(True))
"""),

md("""
`int` son enteros, `float` decimales, `str` texto y `bool` verdadero o falso. Cuatro tipos, y
con eso alcanza para casi todo el semestre.

El problema aparece cuando un número llega guardado como texto, que es lo que pasa con los
códigos postales, los folios y cualquier cosa que empiece con cero.
"""),

code("""
# FALLA A PROPÓSITO, y esta es la peor clase de falla: no lanza error.
cp_uno = "01000"
cp_dos = "02000"

print("Sumando dos textos:", cp_uno + cp_dos)
print("Su tipo:", type(cp_uno + cp_dos))
"""),

md("""
No dio 3000 ni dio error. Pegó los dígitos uno tras otro, porque para Python el `+` entre dos
textos significa unirlos.

Ese es el error más caro de todo el curso, porque no se anuncia. Un total de ventas hecho
sobre una columna que llegó como texto devuelve algo, se ve razonable, y está mal.

La conversión es explícita, y ahí sí avisa cuando no puede.
"""),

code("""
print("Convertidos a número:", int(cp_uno) + int(cp_dos))

# Y cuando de verdad no es un número, se queja en el momento.
try:
    int("mil pesos")
except ValueError as e:
    print("ValueError:", e)
"""),

md("""
## Quiebre 4 · El script es la receta

El clic no deja rastro. Si abriste una hoja, ordenaste, filtraste, borraste tres filas y
pegaste una fórmula, seis meses después no hay forma de saber qué hiciste ni de repetirlo.

Un script sí es la receta completa. Se puede volver a correr, se puede revisar, y se puede
defender frente a alguien que pregunte de dónde salió el número.
"""),

code("""
# Toda la cuenta de arriba, junta y en orden. Esto es un análisis reproducible.
meses = ["ene", "feb", "mar", "abr", "may", "jun"]
ventas = [42000, 51500, 38900, 60100, 55300, 47800]

total = sum(ventas)
promedio = total / len(ventas)

print(f"Periodo:  {meses[0]} a {meses[-1]} de 2025")
print(f"Total:    {total:,.0f}")
print(f"Promedio: {promedio:,.0f}")
print(f"Fuente:   captura manual, {len(ventas)} meses")
"""),

md("""
Cualquiera puede correr esa celda y llegar al mismo número. Eso es lo que una hoja de cálculo
no te da, y es la razón de fondo por la que este curso existe.
"""),

# ──────────────────────────────────────────────────────────── bloque 3

md("""
---
# Bloque 3 · El primer script

Doce meses de ventas resumidos sin abrir la hoja una sola vez. Tres preguntas: cuánto se
vendió, cuál fue el promedio y cuál fue el mejor mes.
"""),

code("""
meses = ["ene", "feb", "mar", "abr", "may", "jun"]
ventas = [42000, 51500, 38900, 60100, 55300, 47800]

total = sum(ventas)
promedio = total / len(ventas)
mejor = meses[ventas.index(max(ventas))]

print(f"Total: {total:,.0f}")
print(f"Promedio: {promedio:,.0f}")
print(f"Mejor mes: {mejor}")
"""),

md("""
La tercera línea de cálculo es la única que merece explicación, y se lee de adentro hacia
afuera:

1. `max(ventas)` da el valor más alto, 60100.
2. `ventas.index(60100)` da la posición donde está, 3.
3. `meses[3]` da el mes que le toca a esa posición, `"abr"`.

Vale la pena partirla para verla.
"""),

code("""
mayor = max(ventas)
donde = ventas.index(mayor)

print("El valor más alto es:", mayor)
print("Está en la posición: ", donde)
print("Que corresponde a:   ", meses[donde])
"""),

md("""
### El riesgo que trae esta forma de trabajar

Todo lo de arriba depende de que las dos listas tengan el mismo largo y el mismo orden. Si
alguien agrega una venta y olvida agregar su mes, el emparejamiento se rompe y nada avisa.
"""),

code("""
# FALLA A PROPÓSITO. Siete ventas contra seis meses: alguien capturó julio y
# olvidó agregar su nombre a la otra lista.
ventas_rotas = [42000, 51500, 38900, 60100, 55300, 47800, 71200]

print("Meses:", len(meses), "· Ventas:", len(ventas_rotas))

try:
    print("Mejor mes:", meses[ventas_rotas.index(max(ventas_rotas))])
except IndexError as e:
    print("IndexError:", e)
    print("El máximo está en la posición", ventas_rotas.index(max(ventas_rotas)),
          "y meses solo llega a la", len(meses) - 1)
"""),

md("""
Aquí sí avisó, y fue suerte: el máximo cayó justo en la posición que no existe.

Ahora el mismo defecto con el máximo en otro lugar. **Predice antes de correr:** ¿lanza error,
o contesta algo?
"""),

code("""
# FALLA A PROPÓSITO Y NO AVISA. Otra vez siete ventas contra seis meses, pero
# ahora el renglón de más quedó al principio: es diciembre del año pasado, que
# alguien dejó pegado arriba. Las seis ventas de abajo siguen siendo ene a jun.
ventas_rotas_2 = [30000, 42000, 51500, 38900, 60100, 55300, 47800]

mejor_roto = meses[ventas_rotas_2.index(max(ventas_rotas_2))]

print("Mejor mes según las listas rotas:", mejor_roto)
print("Mejor mes de verdad:              ", meses[ventas.index(max(ventas))])
print()
print("La venta más alta:", max(ventas_rotas_2))
print("Está en la posición", ventas_rotas_2.index(max(ventas_rotas_2)),
      "de la lista de ventas, y en la", ventas.index(max(ventas)), "de la de meses.")
print("Ningún error. Solo un mes de más recorrió todo un lugar.")
"""),

md("""
Ahí está el problema completo. El mismo defecto, dos listas de distinto largo, lanzó un error
claro la primera vez y devolvió abril como si fuera mayo la segunda. **Cuál de los dos te toca
depende de los datos, no de tu código.**

Y fíjate cuál de los dos es peor. El que truena lo arreglas en dos minutos. El que contesta
"may" cuando la respuesta es "abr" se va al reporte.

Mantener columnas emparejadas a mano no escala. Esa es la frase que justifica todo lo que
sigue en el semestre: un `DataFrame` guarda las columnas juntas, así que no pueden
desemparejarse.

## A dónde vamos

La misma idea, cuando la tabla ya no cabe en la cabeza. Esta celda trae el archivo real del
curso, con 324 renglones, y contesta las mismas tres preguntas.
"""),

bootstrap_cell("es"),

code("""
import pandas as pd

ventas_reales = pd.read_csv("sales.csv")

print("Renglones:", len(ventas_reales))
print(ventas_reales.head(3))
"""),

md("""
Eso es un `DataFrame`: la hoja completa, con encabezados, dentro de una sola variable. No hay
listas que emparejar porque las columnas ya viven juntas.
"""),

code("""
print("Unidades vendidas en total:", ventas_reales["units"].sum())
print("Promedio de unidades:      ", round(ventas_reales["units"].mean(), 2))
print()
print("Regiones que aparecen:")
print(ventas_reales["region"].value_counts())
"""),

md("""
Fíjate en la última salida antes de seguir. El archivo cree que hay ocho regiones y la empresa
tiene cuatro, porque el mismo nombre se capturó con mayúsculas distintas y con espacios de
sobra.

No lo arreglamos hoy. Queda ahí como anticipo de la semana 15, y como recordatorio de que un
archivo real casi nunca llega limpio.
"""),

# ──────────────────────────────────────────────────────────── ejercicios

md("""
---
# Ejercicios

Las soluciones están hasta abajo del cuaderno. Resuélvelos en celdas nuevas debajo de cada
enunciado: para crear una, pasa el cursor bajo esta celda y usa el botón **+ Código**.

### Ejercicio 1 · Tu primera fórmula

Una venta de 12 piezas a 349 pesos cada una. Calcula el subtotal, el IVA al 16 % y el total,
cada uno en su propia variable con un nombre que se explique solo. Imprime los tres con dos
decimales.

### Ejercicio 2 · La columna

Crea dos listas: cuatro productos y lo que se vendió de cada uno. Imprime cuántos productos
hay, el primero, el último usando índice negativo, el total vendido y el promedio.

### Ejercicio 3 · El mejor y el peor

Con las listas del ejercicio anterior, encuentra el producto que más vendió y el que menos.
Imprime los dos con su cifra.

Pista: `min` funciona igual que `max`.

### Ejercicio 4 · Los tipos

Para cada valor de la lista de abajo, imprime el valor y su tipo. Después di, en un
comentario, cuáles se pueden sumar entre sí y cuáles no.

```python
valores = [42, 42.0, "42", True, "cuarenta y dos"]
```

### Ejercicio 5 · El código postal

Tienes dos códigos postales guardados como texto: `"01000"` y `"11560"`. Escribe el código
que los suma como números, e imprime también qué habría pasado si los sumaras como texto.

Después explica en un comentario por qué guardar un código postal como número es mala idea, y
qué se pierde.

### Ejercicio 6 · La condición

Con la lista de ventas mensuales del bloque 3, recorre los seis meses e imprime, por cada
uno, el mes, su venta y si llegó o no a la meta de 50000.

Pista: `for i in range(len(meses)):` te da las posiciones, y con la posición alcanzas los dos
valores.

### Ejercicio 7 · Tu propia hoja

Toma una hoja de cálculo que uses de verdad y escribe, sin código, qué hace cada una de tres
fórmulas: qué datos entran, qué operación se aplica y cómo se llamaría el resultado si le
pusieras nombre.

Empieza por la fórmula más larga que tengas. Casi siempre son tres operaciones apiladas en
una, y separarlas es la mitad del trabajo de traducirla.
"""),

# ──────────────────────────────────────────────────────────── resumen

md("""
---
## Tres ideas para llevarse

**Una fórmula ya es un programa.** Entrada, operación y resultado con nombre. Python cambia
dónde lo escribes, no cómo lo piensas.

**El índice empieza en cero.** Es el error que más tiempo cuesta en las primeras semanas y el
más fácil de evitar sabiéndolo desde hoy.

**Nada se recalcula solo.** El script es la receta, y por eso el análisis se puede repetir,
revisar y defender meses después.

La siguiente sesión es cómo se resuelve un problema antes de escribir una sola línea de
código.
"""),

# ──────────────────────────────────────────────────────────── soluciones

md("""
---
# Soluciones

### Ejercicio 1

```python
piezas = 12
precio_unitario = 349.0

subtotal = piezas * precio_unitario
iva = subtotal * 0.16
total = subtotal + iva

print(f"Subtotal: {subtotal:,.2f}")
print(f"IVA:      {iva:,.2f}")
print(f"Total:    {total:,.2f}")
```

Da 4,188.00 de subtotal y 4,858.08 de total. Escribir `total = subtotal * 1.16` en una sola
línea llega al mismo número y esconde el IVA, que casi siempre hay que reportar aparte.

### Ejercicio 2

```python
productos = ["Americano", "Capuchino", "Latte", "Concha"]
piezas = [310, 185, 142, 260]

print("Productos:", len(productos))
print("El primero:", productos[0])
print("El último: ", productos[-1])
print("Total vendido:", sum(piezas))
print("Promedio:", round(sum(piezas) / len(piezas), 2))
```

`productos[-1]` evita tener que saber cuántos hay. Si mañana agregas un quinto producto, esa
línea sigue siendo correcta y `productos[3]` ya no.

### Ejercicio 3

```python
mas = productos[piezas.index(max(piezas))]
menos = productos[piezas.index(min(piezas))]

print(f"El que más vendió: {mas} con {max(piezas)}")
print(f"El que menos:      {menos} con {min(piezas)}")
```

Es el mismo patrón de tres pasos del bloque 3: valor extremo, su posición, y el nombre que le
toca a esa posición.

### Ejercicio 4

```python
valores = [42, 42.0, "42", True, "cuarenta y dos"]

for v in valores:
    print(f"{str(v):<18} {type(v)}")

# Se pueden sumar entre sí: 42, 42.0 y True, porque los tres son numéricos.
# True vale 1 cuando entra en una cuenta, lo cual sorprende y es correcto.
# "42" se puede convertir con int() y entonces sí suma.
# "cuarenta y dos" no se puede convertir, y int() sobre él lanza ValueError.
```

Que `True` valga 1 no es una curiosidad: es lo que hace que `sum()` sobre una columna de
verdadero y falso cuente cuántos cumplen. Lo vas a usar mucho en la semana 15.

### Ejercicio 5

```python
cp_casa = "01000"
cp_oficina = "11560"

print("Como texto: ", cp_casa + cp_oficina)
print("Como número:", int(cp_casa) + int(cp_oficina))

# Guardar un código postal como número pierde el cero de la izquierda: 01000 se
# vuelve 1000 y ya no es un código postal válido. Además, sumar dos códigos
# postales no significa nada. Es un identificador, no una cantidad, y por eso su
# lugar correcto es el texto aunque solo tenga dígitos.
```

La prueba de si algo es número o identificador es si tiene sentido sumarlo o promediarlo. Un
folio, un código postal y un número de empleado fallan esa prueba.

### Ejercicio 6

```python
meses = ["ene", "feb", "mar", "abr", "may", "jun"]
ventas = [42000, 51500, 38900, 60100, 55300, 47800]
META = 50000

for i in range(len(meses)):
    estado = "meta" if ventas[i] >= META else "abajo"
    print(f"{meses[i]}  {ventas[i]:>7,}  {estado}")
```

Tres de seis meses llegaron. Nota que el ciclo recorre posiciones y no valores: es la forma de
mantener las dos listas emparejadas, y también la que se rompe si dejan de tener el mismo
largo.

### Ejercicio 7

No hay solución publicada porque la hoja es distinta para cada quien. Se califica sobre tres
cosas: que las tres fórmulas estén partidas en entrada, operación y resultado; que el nombre
propuesto diga qué guarda y no dónde está; y que al menos una de las tres sea de las largas,
con varias operaciones apiladas.
"""),

]

write(OUT / "es" / "w01.1.ipynb", es)
print("wrote", OUT / "es" / "w01.1.ipynb")


# ════════════════════════════════════════════════════════════════════ ENGLISH

en = [

md("""
# Data Analysis · Week 1 · Bridge
## From Excel to Python

**TIA502 · School of Business · Instructor David Escobar-Castillejos**

This notebook does not start from zero, because neither do you. If you have ever built a
formula in a spreadsheet, you have already programmed: you took data, applied an operation and
stored the result somewhere with a name. Python is not asking you for a new idea. It is asking
you to write that same idea a different way.

By the end of this notebook you will be able to:

1. Translate a spreadsheet formula into a Python expression.
2. Name your data instead of pointing at it, and say why that matters.
3. Recognise the four points where the Excel analogy breaks down.
4. Summarise a table of months without opening the spreadsheet.
5. Explain what a sheet stops being able to do as the table grows.

### How to use this notebook

This is your first contact with code that runs. To execute a cell, click it and press
**Shift + Enter**. The result appears right below it.

Run the cells in order, top to bottom. Several use a value the previous one defined, so
skipping one gives you an error that has nothing to do with the topic.

Four cells fail on purpose, so you see what an error looks like before meeting one on your
own. They carry a comment saying so.
"""),

md("""
---
# Block 1 · You already program, just in another syntax

A spreadsheet is a language. It has values, names, functions and conditions. What changes is
where you write them.

| Concept | In the spreadsheet | In Python |
|---|---|---|
| Named value | A named cell | A variable |
| Formula | Price times quantity | `amount = price * quantity` |
| Function | `AVERAGE` over a range | `mean()` over a list |
| Condition | `IF` with two outcomes | `if` and `else` |
| Column | The range `B2:B500` | A list |
| Lookup table | `VLOOKUP` into a catalogue | A dictionary |
| The whole sheet | Rows, columns and headers | A `DataFrame` |

The last three are covered properly later in the term. The first four start today.

## A formula is already a program

In the sheet you would write `=B2*C2`. The cell takes two values, multiplies them and stores
the result where you wrote the formula.

In Python it is the same, with one difference: the result goes to a name you choose, not to a
cell that its position imposed on you.
"""),

code("""
price = 8990.0
quantity = 3

amount = price * quantity

print(amount)
"""),

md("""
Those three lines are the whole formula. `price` and `quantity` are the inputs,
`price * quantity` is the operation, and `amount` is the name where the result lives.

Watch the equals sign, because it is the only piece of punctuation that matters today. **The
equals sign in a sheet opens a formula. The equals sign in Python stores a result.**

And once the result has a name, that name gets used on the next line.
"""),

code("""
tax = amount * 0.16
total = amount + tax

print("Amount:", amount)
print("Tax:   ", tax)
print("Total: ", total)
"""),

md("""
### Why the name matters more than it looks

`B7` says nothing. Six months from now, opening your own sheet, you will have to trace where
that cell came from to know what it holds.

`total_with_tax` does say something. It is the difference between a file you can pick back up
and one you have to reconstruct.
"""),

code("""
# The same numbers, with names that explain themselves.
unit_price = 8990.0
pieces_sold = 3
subtotal = unit_price * pieces_sold
total_with_tax = subtotal * 1.16

print(f"{pieces_sold} pieces at {unit_price:,.2f} come to {total_with_tax:,.2f} with tax")
"""),

md("""
That last line uses an **f-string**: the text starts with `f` and anything inside braces is
replaced by its value. The `:,.2f` is formatting, and it says "separate the thousands with
commas and give me two decimals". It is the same as applying a currency format to a cell.

## The same four operations, written twice

In the sheet:

```
=B2*C2
=SUM(D2:D13)
=AVERAGE(D2:D13)
=IF(D2>50000, "target", "below")
```

In Python, with the same arithmetic:
"""),

code("""
amounts = [42000, 51500, 38900, 60100, 55300, 47800]

total = sum(amounts)
average = total / len(amounts)
status = "target" if amounts[0] > 50000 else "below"

print("Total:  ", total)
print("Average:", round(average, 2))
print("January:", status)
"""),

md("""
`sum` is `SUM`, `len` is `COUNT`, and the division that joins them is the ordinary one.

The last line reads almost the way you would say it out loud: *"target" if the amount clears
50000, and otherwise "below"*. It is the sheet's `IF`, with the parts in a different order.

## A column is a list

The range `B2:B500` in your sheet is, in Python, a list: values in order, inside one name.
"""),

code("""
months = ["jan", "feb", "mar", "apr", "may", "jun"]
sales = [42000, 51500, 38900, 60100, 55300, 47800]

print("How many months:", len(months))
print("How many sales: ", len(sales))
print("The first month:", months[0])
print("The first sale: ", sales[0])
"""),

md("""
Two lists, two columns. Position 0 of one matches position 0 of the other, just as row 2 of
column B matches row 2 of column C.

That pairing by position is convenient and it is also fragile, and it is exactly the problem
`pandas` comes to solve in week 15.
"""),

md("""
---
# Block 2 · Where it stops looking alike

Four real differences. None of them is hard, and all of them cost you an afternoon if nobody
mentions them in time.

| Point | In the spreadsheet | In Python |
|---|---|---|
| First element | Row number 1 | Index 0 |
| Recalculation | Automatic when a value changes | Only when you run it again |
| Types | The cell guesses the format | The value has a type and nothing is guessed |
| Trace | A click leaves no record | The script is the whole recipe |
| Size | It drags and stops responding | Millions of rows without trouble |

## Break 1 · The index starts at zero

This is the one that costs the most time in the first weeks.
"""),

code("""
print("months[0] is", months[0])
print("months[1] is", months[1])
print("months[5] is", months[5])
print()
print("The list has", len(months), "items, and the last index is", len(months) - 1)
"""),

md("""
**Predict before you run.** The list below has twelve months. What does `months_12[12]` print?

- **A.** `dec`, because December is month number twelve.
- **B.** `jan`, because the list starts over.
- **C.** `IndexError`, because the last index is 11.
- **D.** `None`, because that position is empty.
"""),

code("""
# FAILS ON PURPOSE. Twelve items run from index 0 to 11.
months_12 = ["jan", "feb", "mar", "apr", "may", "jun",
             "jul", "aug", "sep", "oct", "nov", "dec"]

try:
    print(months_12[12])
except IndexError as e:
    print("IndexError:", e)

print()
print("December sits at:", months_12[11])
print("And also at:     ", months_12[-1], "· a negative index counts from the end")
"""),

md("""
The answer is **C**. Twelve items run from 0 to 11, so 12 falls off the end.

The negative index is a gift the spreadsheet does not have: `-1` is the last one, `-2` the one
before it, and you never need to know how many there are.

## Break 2 · Nothing recalculates on its own

In the sheet, you change B2 and everything that depended on B2 updates instantly. In Python it
does not.
"""),

code("""
price = 100
quantity = 5
amount = price * quantity

print("Amount calculated:", amount)

# Now I change the price, as if I had corrected a cell.
price = 200

print("Price is now:     ", price)
print("Amount is still:  ", amount, "· nobody recalculated it")
"""),

md("""
`amount` holds the result of a multiplication that already happened, not the instruction to
repeat it. To update it, the operation has to run again.
"""),

code("""
amount = price * quantity
print("Amount recalculated:", amount)
"""),

md("""
This sounds like a drawback and it is the opposite. It means the order the lines run in is
yours, and that a number does not shift under your feet while you work. In a large sheet an
automatic recalculation can be slow and can surprise you; here nothing happens until you ask.

In a Colab notebook there is a practical consequence: **the order you execute the cells in is
the order that counts**, not the order they are written in. If you run a cell further down and
then one further up, the state is whatever the last one you ran left behind. That is why the
notebook is run top to bottom.

## Break 3 · The value has a type, and the type is not guessed

An Excel cell guesses. You type `01000` and it decides whether that is a number or text, and
sometimes it decides wrong.

In Python the type is explicit and you can ask for it.
"""),

code("""
print(type(42000))
print(type(42000.5))
print(type("42000"))
print(type(True))
"""),

md("""
`int` is whole numbers, `float` decimals, `str` text and `bool` true or false. Four types, and
that covers almost the whole term.

The trouble shows up when a number arrives stored as text, which is what happens with postal
codes, reference numbers and anything that starts with a zero.
"""),

code("""
# FAILS ON PURPOSE, and this is the worst kind of failure: it raises nothing.
code_one = "01000"
code_two = "02000"

print("Adding two strings:", code_one + code_two)
print("Its type:", type(code_one + code_two))
"""),

md("""
It did not give 3000 and it did not give an error. It glued the digits together, because to
Python a `+` between two strings means join them.

That is the most expensive error in the course, because it does not announce itself. A sales
total computed over a column that arrived as text gives you something, it looks reasonable,
and it is wrong.

Conversion is explicit, and there it does complain when it cannot do the job.
"""),

code("""
print("Converted to numbers:", int(code_one) + int(code_two))

# And when it genuinely is not a number, it objects on the spot.
try:
    int("a thousand pesos")
except ValueError as e:
    print("ValueError:", e)
"""),

md("""
## Break 4 · The script is the recipe

A click leaves no record. If you opened a sheet, sorted it, filtered it, deleted three rows
and pasted a formula, six months later there is no way to know what you did or to repeat it.

A script is the whole recipe. It can be run again, it can be reviewed, and it can be defended
in front of somebody asking where the number came from.
"""),

code("""
# All of the arithmetic above, together and in order. This is a reproducible analysis.
months = ["jan", "feb", "mar", "apr", "may", "jun"]
sales = [42000, 51500, 38900, 60100, 55300, 47800]

total = sum(sales)
average = total / len(sales)

print(f"Period:  {months[0]} to {months[-1]} 2025")
print(f"Total:   {total:,.0f}")
print(f"Average: {average:,.0f}")
print(f"Source:  manual capture, {len(sales)} months")
"""),

md("""
Anybody can run that cell and reach the same number. That is what a spreadsheet does not give
you, and it is the underlying reason this course exists.
"""),

md("""
---
# Block 3 · The first script

Months of sales summarised without opening the sheet once. Three questions: how much was sold,
what the average was, and which month was best.
"""),

code("""
months = ["jan", "feb", "mar", "apr", "may", "jun"]
sales = [42000, 51500, 38900, 60100, 55300, 47800]

total = sum(sales)
average = total / len(sales)
best = months[sales.index(max(sales))]

print(f"Total: {total:,.0f}")
print(f"Average: {average:,.0f}")
print(f"Best month: {best}")
"""),

md("""
The third calculation is the only one that needs explaining, and it reads from the inside out:

1. `max(sales)` gives the highest value, 60100.
2. `sales.index(60100)` gives the position it sits at, 3.
3. `months[3]` gives the month that belongs to that position, `"apr"`.

Worth splitting apart to see it.
"""),

code("""
highest = max(sales)
where = sales.index(highest)

print("The highest value is:", highest)
print("It sits at position: ", where)
print("Which corresponds to:", months[where])
"""),

md("""
### The risk this way of working carries

Everything above depends on both lists having the same length and the same order. If somebody
adds a sale and forgets to add its month, the pairing breaks.
"""),

code("""
# FAILS ON PURPOSE. Seven sales against six months: somebody captured July and
# forgot to add its name to the other list.
broken_sales = [42000, 51500, 38900, 60100, 55300, 47800, 71200]

print("Months:", len(months), "· Sales:", len(broken_sales))

try:
    print("Best month:", months[broken_sales.index(max(broken_sales))])
except IndexError as e:
    print("IndexError:", e)
    print("The maximum is at position", broken_sales.index(max(broken_sales)),
          "and months only reaches", len(months) - 1)
"""),

md("""
Here it did warn us, and that was luck: the maximum happened to land on the position that does
not exist.

Now the same defect with the maximum somewhere else. **Predict before you run:** does it raise
an error, or does it answer something?
"""),

code("""
# FAILS ON PURPOSE AND SAYS NOTHING. Seven sales against six months again, but now
# the extra row sits at the top: it is last December, left pasted above. The six
# below are still jan to jun.
broken_sales_2 = [30000, 42000, 51500, 38900, 60100, 55300, 47800]

broken_best = months[broken_sales_2.index(max(broken_sales_2))]

print("Best month according to the broken lists:", broken_best)
print("Best month in reality:                   ", months[sales.index(max(sales))])
print()
print("The highest sale:", max(broken_sales_2))
print("It sits at position", broken_sales_2.index(max(broken_sales_2)),
      "in the sales list, and at", sales.index(max(sales)), "in the months list.")
print("No error. Just one extra row shifting everything by one.")
"""),

md("""
There is the problem in full. The same defect, two lists of different lengths, raised a clear
error the first time and handed back April dressed as May the second.  **Which of the two you
get depends on the data, not on your code.**

And notice which one is worse. The one that blows up you fix in two minutes. The one that says
"may" when the answer is "apr" goes into the report.

Keeping columns paired up by hand does not scale. That is the sentence that justifies
everything that follows this term: a `DataFrame` keeps the columns together, so they cannot
come unpaired.

## Where this is going

The same idea, once the table no longer fits in your head. This cell brings in the real course
file, with 324 rows, and answers the same three questions.
"""),

bootstrap_cell("en"),

code("""
import pandas as pd

real_sales = pd.read_csv("sales.csv")

print("Rows:", len(real_sales))
print(real_sales.head(3))
"""),

md("""
That is a `DataFrame`: the whole sheet, headers and all, inside a single variable. There are no
lists to keep paired because the columns already live together.
"""),

code("""
print("Units sold in total:", real_sales["units"].sum())
print("Average units:      ", round(real_sales["units"].mean(), 2))
print()
print("Regions that appear:")
print(real_sales["region"].value_counts())
"""),

md("""
Look at that last output before moving on. The file thinks there are eight regions and the
company has four, because the same name was captured with different capitalisation and with
stray spaces.

We are not fixing it today. It sits there as a preview of week 15, and as a reminder that a
real file almost never arrives clean.
"""),

md("""
---
# Exercises

The solutions sit at the very bottom of the notebook. Solve them in new cells below each
brief: to make one, hover below this cell and use the **+ Code** button.

### Exercise 1 · Your first formula

A sale of 12 pieces at 349 pesos each. Work out the subtotal, the 16 % tax and the total, each
in its own variable with a name that explains itself. Print all three with two decimals.

### Exercise 2 · The column

Create two lists: four products and how much of each was sold. Print how many products there
are, the first one, the last one using a negative index, the total sold and the average.

### Exercise 3 · The best and the worst

With the lists from the previous exercise, find the product that sold most and the one that
sold least. Print both with their figure.

Hint: `min` works just like `max`.

### Exercise 4 · The types

For every value in the list below, print the value and its type. Then say, in a comment, which
ones can be added together and which cannot.

```python
values = [42, 42.0, "42", True, "forty two"]
```

### Exercise 5 · The postal code

You have two postal codes stored as text: `"01000"` and `"11560"`. Write the code that adds
them as numbers, and print what would have happened had you added them as text.

Then explain in a comment why storing a postal code as a number is a bad idea, and what gets
lost.

### Exercise 6 · The condition

With the monthly sales list from block 3, walk the six months and print, for each one, the
month, its sale and whether it reached the target of 50000.

Hint: `for i in range(len(months)):` gives you the positions, and with a position you can reach
both values.

### Exercise 7 · Your own sheet

Take a spreadsheet you actually use and write down, without code, what each of three formulas
does: what data goes in, what operation is applied, and what the result would be called if you
gave it a name.

Start with the longest formula you have. They are almost always three operations stacked into
one, and pulling them apart is half the work of translating it.
"""),

md("""
---
## Three ideas to take away

**A formula is already a program.** Input, operation and a named result. Python changes where
you write it, not how you think about it.

**The index starts at zero.** It is the error that costs the most time in the first weeks and
the easiest to avoid by knowing it from today.

**Nothing recalculates on its own.** The script is the recipe, and that is why the analysis can
be repeated, reviewed and defended months later.

Next session is how a problem gets solved before a single line of code is written.
"""),

md("""
---
# Solutions

### Exercise 1

```python
pieces = 12
unit_price = 349.0

subtotal = pieces * unit_price
tax = subtotal * 0.16
total = subtotal + tax

print(f"Subtotal: {subtotal:,.2f}")
print(f"Tax:      {tax:,.2f}")
print(f"Total:    {total:,.2f}")
```

That gives 4,188.00 subtotal and 4,858.08 total. Writing `total = subtotal * 1.16` on one line
reaches the same number and hides the tax, which usually has to be reported separately.

### Exercise 2

```python
products = ["Americano", "Cappuccino", "Latte", "Sweet bread"]
pieces = [310, 185, 142, 260]

print("Products:", len(products))
print("The first:", products[0])
print("The last: ", products[-1])
print("Total sold:", sum(pieces))
print("Average:", round(sum(pieces) / len(pieces), 2))
```

`products[-1]` saves you having to know how many there are. If you add a fifth product
tomorrow, that line is still right and `products[3]` no longer is.

### Exercise 3

```python
most = products[pieces.index(max(pieces))]
least = products[pieces.index(min(pieces))]

print(f"Sold most:  {most} with {max(pieces)}")
print(f"Sold least: {least} with {min(pieces)}")
```

It is the same three-step pattern from block 3: extreme value, its position, and the name that
belongs to that position.

### Exercise 4

```python
values = [42, 42.0, "42", True, "forty two"]

for v in values:
    print(f"{str(v):<14} {type(v)}")

# Can be added together: 42, 42.0 and True, because all three are numeric.
# True counts as 1 when it enters arithmetic, which surprises people and is correct.
# "42" can be converted with int() and then it adds fine.
# "forty two" cannot be converted, and int() on it raises ValueError.
```

That `True` counts as 1 is not a curiosity: it is what makes `sum()` over a column of true and
false count how many qualify. You will use it constantly in week 15.

### Exercise 5

```python
home_code = "01000"
office_code = "11560"

print("As text:  ", home_code + office_code)
print("As numbers:", int(home_code) + int(office_code))

# Storing a postal code as a number loses the leading zero: 01000 becomes 1000 and
# is no longer a valid code. On top of that, adding two postal codes means nothing.
# It is an identifier, not a quantity, and that is why its correct home is text even
# though it only contains digits.
```

The test for whether something is a number or an identifier is whether it makes sense to add
or average it. A reference number, a postal code and an employee number all fail that test.

### Exercise 6

```python
months = ["jan", "feb", "mar", "apr", "may", "jun"]
sales = [42000, 51500, 38900, 60100, 55300, 47800]
TARGET = 50000

for i in range(len(months)):
    status = "target" if sales[i] >= TARGET else "below"
    print(f"{months[i]}  {sales[i]:>7,}  {status}")
```

Three of six months made it. Note that the loop walks positions rather than values: that is
how the two lists stay paired, and also what breaks the moment they stop being the same length.

### Exercise 7

There is no published solution, because the sheet is different for everyone. It is graded on
three things: that all three formulas are split into input, operation and result; that the
proposed name says what it holds rather than where it sits; and that at least one of the three
is a long one, with several operations stacked together.
"""),

]

write(OUT / "en" / "w01.1.ipynb", en)
print("wrote", OUT / "en" / "w01.1.ipynb")
