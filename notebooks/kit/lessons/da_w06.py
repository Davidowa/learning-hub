"""notebooks/analisis-de-datos/{es,en}/w06.ipynb

Source deck: ppts/python/analisis-de-datos/{es,en}/w06.*.yaml
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from nbkit import md, code, write, REPO

OUT = REPO / "notebooks" / "analisis-de-datos"

es = [

md("""
# Análisis de Datos · Semana 6
## Estructuras de selección

**TIA502 · Facultad de Empresariales · Profesor David Escobar-Castillejos**

Aquí empieza lo que separa un programa de una fórmula. Ya usas `SI` en una hoja de cálculo, así
que la idea no es nueva; lo nuevo es que ahora la decisión puede ocupar varias líneas y llevar
dentro todo lo que quieras.

Al terminar este cuaderno vas a poder:

1. Usar los seis operadores de comparación, incluidos los dos que incluyen el límite.
2. Leer una expresión booleana y saber que su resultado es siempre `True` o `False`.
3. Escribir una decisión simple y una doble, y decir qué cambia entre las dos.
4. Encadenar varios casos con `elif` y explicar por qué solo corre la primera rama que se cumple.
5. Reconocer el error del límite: la diferencia entre mayor que y mayor o igual que.

### Cómo se usa este cuaderno

Ejecuta las celdas en orden. Cinco fallan a propósito y llevan un comentario que lo dice.

El caso de toda la sesión es clasificar una campaña por su tasa de conversión: 5 074 clics sobre
148 230 impresiones, o sea 3.42 %.
"""),

md("""
---
# Bloque 1 · Comparar

Antes de decidir hay que preguntar. Una comparación siempre contesta lo mismo: verdadero o
falso.

| Operador | La pregunta | Ejemplo | Resultado |
|---|---|---|---|
| `==` | ¿Son iguales? | `conversion == 0.0342` | `True` |
| `!=` | ¿Son distintos? | `canal != "TikTok"` | `True` |
| `>` | ¿Es mayor? | `clics > 5000` | `True` |
| `<` | ¿Es menor? | `clics < 5000` | `False` |
| `>=` | ¿Es mayor o igual? | `conversion >= 0.03` | `True` |
| `<=` | ¿Es menor o igual? | `inversion <= 38500` | `True` |

Los seis, corriendo.
"""),

code("""
canal = "Instagram"
impresiones = 148230
clics = 5074
inversion = 38500.00
conversion = clics / impresiones

print("conversion == 0.0342 :", round(conversion, 4) == 0.0342)
print("canal != 'TikTok'    :", canal != "TikTok")
print("clics > 5000         :", clics > 5000)
print("clics < 5000         :", clics < 5000)
print("conversion >= 0.03   :", conversion >= 0.03)
print("inversion <= 38500   :", inversion <= 38500)
"""),

md("""
El que más se olvida es `!=`, el de distinto. El que más se confunde es `==`, y de ese hablamos
en un segundo.

## Una comparación devuelve un valor

Compares lo que compares, el resultado es `True` o `False`. No hay "casi" ni "depende".

Eso significa que una comparación es un valor como cualquier otro: se puede guardar, imprimir y
preguntar de qué tipo es.
"""),

code("""
meta = 0.03
llego_a_la_meta = conversion >= meta

print(llego_a_la_meta)
print(type(llego_a_la_meta))
print("Se puede guardar en una variable y usarla después.")
"""),

md("""
Esa es toda la materia prima de una decisión. Y por eso una condición que parece complicada casi
siempre se puede partir en dos comparaciones simples y volver a juntarlas.

## Un igual guarda, dos iguales preguntan

Este es el error clásico, y Python te protege de él.
"""),

code("""
# FALLA A PROPÓSITO. Un solo igual dentro de un if.
codigo = 'if conversion = 0.03:\\n    print("igual")'

try:
    compile(codigo, "<ejemplo>", "exec")
except SyntaxError as e:
    print(f"SyntaxError: {e.msg}")
"""),

md("""
Python lo marca como error de sintaxis y no lo deja correr. Ese rigor te está protegiendo de un
error mucho peor: en otros lenguajes esa línea compila, guarda 0.03 en `conversion` y la
condición siempre da verdadero.

Aquí no hay forma de escribirlo por accidente.
"""),

code("""
# El de uno guarda.
resultado = 0.03
print("Después de un igual:", resultado)

# El de dos pregunta y no guarda nada.
print("Con dos iguales:", resultado == 0.03)
print("resultado sigue en:", resultado)
"""),

md("""
## Comparar textos

Los seis operadores también funcionan con texto, y ahí hay dos sorpresas.
"""),

code("""
print('"Instagram" == "Instagram" :', "Instagram" == "Instagram")
print('"Instagram" == "instagram" :', "Instagram" == "instagram")
print('"Instagram" == " Instagram":', "Instagram" == " Instagram")
"""),

md("""
La comparación de texto distingue mayúsculas y no perdona espacios. Es exactamente el problema
de las ocho regiones de `sales.csv` que viste en la semana 1.1, y la razón por la que en la
semana 15 hay que normalizar antes de agrupar.

La segunda sorpresa: `<` y `>` sí funcionan con texto, y comparan alfabéticamente.
"""),

code("""
print('"Facebook" < "Instagram" :', "Facebook" < "Instagram")
print('"Zeta" < "alfa"          :', "Zeta" < "alfa", "<- las mayúsculas van antes")
"""),

md("""
Que las mayúsculas vayan antes que las minúsculas sorprende al ordenar una lista de nombres
capturados a mano. Es otra cara del mismo problema.

## Comparar decimales

Ya lo viste en la semana 4 y aquí muerde de otra forma.
"""),

code("""
# FALLA A PROPÓSITO. La igualdad exacta entre decimales.
a = 0.1 + 0.2

print("a == 0.3 ?", a == 0.3)
print("a >= 0.3 ?", a >= 0.3)
print("El valor real:", a)
"""),

md("""
`a == 0.3` da falso y `a >= 0.3` da verdadero, con el mismo par de números.

Regla práctica: **con decimales, usa `>=` o `<=` en lugar de `==`.** Y cuando de verdad necesites
igualdad, usa una tolerancia.
"""),

md("""
---
# Bloque 2 · Decidir

La misma estructura que ya usas en una hoja de cálculo, escrita en dos renglones en lugar de en
una fórmula larga.

```
=SI(D2>=0.03, "Aceptable", "Revisar")
```
"""),

code("""
impresiones = 148230
clics = 5074

conversion = clics / impresiones

if conversion >= 0.03:
    estado = "Aceptable"
    print("La campaña se queda al aire.")
else:
    estado = "Revisar"
    print("Hay que revisar la segmentación.")

print(f"{conversion:.2%} · {estado}")
"""),

md("""
Cuatro cosas que la fórmula de la hoja no puede hacer y esto sí.

**Los dos puntos** cierran la condición. Sin ellos, `SyntaxError` justo ahí.

**La sangría** es la que dice qué líneas pertenecen a cada rama. Los cuatro espacios no son
decoración, son la estructura.

**Cada rama puede tener varias líneas.** Aquí cada una asigna una variable y además imprime. Una
fórmula de hoja solo puede devolver un valor.

**Después del `if`**, la última línea está fuera de la sangría, así que se imprime pase lo que
pase.

Cámbiale la conversión y córrelo otra vez para ver la otra rama.
"""),

code("""
conversion = 0.021

if conversion >= 0.03:
    estado = "Aceptable"
    print("La campaña se queda al aire.")
else:
    estado = "Revisar"
    print("Hay que revisar la segmentación.")

print(f"{conversion:.2%} · {estado}")
"""),

md("""
Una sola rama corrió. Nunca las dos, y siempre una de las dos.

## Las tres formas de la selección

| Forma | Cuándo se usa | Estructura |
|---|---|---|
| Simple | Solo hay algo que hacer si se cumple | `if condición:` |
| Doble | Hay dos caminos y siempre se toma uno | `if` / `else` |
| Múltiple | Hay tres o más categorías excluyentes | `if` / `elif` / `else` |

La simple, que no lleva `else`, sirve cuando no hay nada que hacer en el otro caso.
"""),

code("""
conversion = 0.0342
alertas = []

if conversion < 0.01:
    alertas.append("Conversión crítica")

if inversion > 30000:
    alertas.append("Inversión alta")

print("Alertas:", alertas or "ninguna")
"""),

md("""
Dos `if` simples, uno detrás de otro. Son independientes: los dos se evalúan y **los dos pueden
cumplirse**.

Esa es la diferencia con `elif`, que va en el bloque siguiente.
"""),

md("""
---
# Bloque 3 · Varios caminos

Tres categorías, y el orden en que las escribes decide cuál gana.
"""),

code("""
conversion = 0.0342

if conversion >= 0.05:
    estado = "Excelente"
elif conversion >= 0.03:
    estado = "Aceptable"
else:
    estado = "Revisar"

print(f"{conversion:.2%} · {estado}")
"""),

md("""
Se evalúa la primera condición. Si falla, la segunda. **En cuanto una se cumple, las demás ni se
leen.**

La traza con 3.42 %:

| Paso | Condición | ¿Se cumple? | `estado` |
|---|---|---|---|
| 1 | `0.0342 >= 0.05` | No | – |
| 2 | `0.0342 >= 0.03` | Sí | `Aceptable` |
| 3 | `else` | No se evalúa | `Aceptable` |

## Por qué el orden decide

Va de lo más exigente a lo menos. Al revés, todo lo bueno caería en la categoría floja.

Con 3.42 % las dos versiones dan lo mismo, así que el error no se ve. Compáralas con una campaña
del 6 %.
"""),

code("""
def clasificar_bien(conversion):
    if conversion >= 0.05:
        return "Excelente"
    elif conversion >= 0.03:
        return "Aceptable"
    else:
        return "Revisar"


def clasificar_mal(conversion):
    \"\"\"Las mismas tres reglas, con los umbrales al revés.\"\"\"
    if conversion >= 0.03:
        return "Aceptable"
    elif conversion >= 0.05:
        return "Excelente"
    else:
        return "Revisar"


for tasa in [0.061, 0.0342, 0.021, 0.050]:
    bien = clasificar_bien(tasa)
    mal = clasificar_mal(tasa)
    marca = "  <-- distinto" if bien != mal else ""
    print(f"{tasa:>7.2%}   {bien:<10} {mal:<10}{marca}")
"""),

md("""
Ahí está. Con el orden invertido, **"Excelente" es inalcanzable**: cualquier campaña que llegue al
5 % ya pasó el 3 % y se queda atrapada en la primera rama.

Lo peor es que la función no truena, no avisa, y clasifica correctamente tres de cada cuatro
casos. Solo se equivoca con los mejores, que son justo los que querías detectar.
"""),

code("""
# Comprobación: ¿alguna tasa alcanza "Excelente" con el orden invertido?
posibles = [i / 1000 for i in range(0, 101)]
excelentes = [t for t in posibles if clasificar_mal(t) == "Excelente"]

print("Tasas que llegan a Excelente con el orden malo:", len(excelentes))
print("Con el orden bueno:", len([t for t in posibles if clasificar_bien(t) == "Excelente"]))
"""),

md("""
Cero contra cincuenta y una. Una rama inalcanzable es un error que ninguna corrida normal
encuentra, porque para verlo hay que probar el caso que nunca llega.

## El error del límite

**Predice antes de correr.** Con una conversión de exactamente 0.03, ¿qué estado imprime?

- **A.** `Aceptable`, porque llegó a la meta.
- **B.** `Revisar`, porque el operador pide estrictamente mayor.
- **C.** Un error, porque no hay `elif`.
- **D.** Los dos, porque cumple las dos condiciones.
"""),

code("""
conversion = 0.03

if conversion > 0.03:
    estado = "Aceptable"
else:
    estado = "Revisar"

print(estado)
"""),

md("""
La respuesta es **B**. `>` deja fuera al que está justo en la meta, `>=` lo incluye.

Una campaña que llegó exactamente al objetivo sale clasificada como que hay que revisarla. Ese
es el error del límite, y no se descubre probando valores redondos por arriba y por abajo: hay
que probar **el límite exacto**.
"""),

code("""
for tasa in [0.0299, 0.03, 0.0301]:
    con_mayor = "Aceptable" if tasa > 0.03 else "Revisar"
    con_mayor_igual = "Aceptable" if tasa >= 0.03 else "Revisar"
    print(f"{tasa:.4f}   con >  : {con_mayor:<10} con >= : {con_mayor_igual}")
"""),

md("""
Solo el renglón de en medio cambia. Los otros dos se comportan igual con los dos operadores, y
por eso una prueba que no incluya el valor exacto del límite no encuentra nada.

Fíjate también en el `"Aceptable" if tasa > 0.03 else "Revisar"` de esa celda. Es la forma corta
de un `if`/`else` cuando lo único que quieres es elegir entre dos valores, y cabe en una línea.

## Clasificar una tabla completa

Con lo de hoy ya se puede recorrer varias campañas y clasificarlas todas.
"""),

code("""
CAMPANAS = [
    ("Instagram", 148230, 5074),
    ("Facebook", 96400, 2891),
    ("Google", 210500, 9840),
    ("TikTok", 54800, 3510),
    ("LinkedIn", 31200, 640),
]

print(f"{'Canal':<12}{'Conversión':>12}   Estado")
print("-" * 38)

for canal, impresiones, clics in CAMPANAS:
    conversion = clics / impresiones
    estado = clasificar_bien(conversion)
    print(f"{canal:<12}{conversion:>12.2%}   {estado}")
"""),

md("""
Cinco campañas, tres categorías, y el `for` de la semana 3 haciendo el trabajo repetitivo.

## Cuatro errores de la primera decisión

**Un igual en lugar de dos.** El de uno guarda, el de dos pregunta. Python lo marca como error de
sintaxis, y eso te salva.

**Olvidar los dos puntos.** Toda condición termina en dos puntos. Es el error de sintaxis más
frecuente del semestre.
"""),

code("""
# FALLA A PROPÓSITO. Faltan los dos puntos.
try:
    compile('if conversion >= 0.03\\n    print("ok")', "<ejemplo>", "exec")
except SyntaxError as e:
    print(f"SyntaxError: {e.msg}")
"""),

md("""
**Equivocar el límite.** Mayor que deja fuera al que está justo en la meta. Mayor o igual lo
incluye. Decide cuál quieres y pruébalo con el valor exacto.

**Escribir las condiciones al revés.** De lo más exigente a lo menos. Al revés, la primera rama se
traga todos los casos y una categoría se vuelve inalcanzable.
"""),

md("""
---
# Ejercicios

Las soluciones están hasta abajo del cuaderno.

## Comparar

### Ejercicio 1 · Los seis, con tus datos

Declara tres variables de una campaña o de un reporte que conozcas y escribe seis comparaciones,
una por operador. Imprime cada una con la pregunta que contesta.

### Ejercicio 2 · Guardar una comparación

Guarda tres comparaciones en tres variables con nombres que se lean como una afirmación, por
ejemplo `supera_la_meta`. Imprímelas y después imprime cuántas de las tres son verdaderas.

Pista: `True` vale 1 en una suma.

### Ejercicio 3 · Texto que parece igual y no lo es

Escribe cinco versiones del mismo nombre de canal con distintas mayúsculas y espacios, y
compáralas todas contra `"Instagram"`. Después arregla la comparación para que las cinco den
verdadero.

Pista: `.strip()` quita espacios y `.lower()` pasa a minúsculas.

## Decidir

### Ejercicio 4 · Una decisión doble

Escribe un `if`/`else` que clasifique una inversión como "dentro de presupuesto" o "excedida",
con un presupuesto de 40 000. Que cada rama imprima dos líneas: la clasificación y una
recomendación distinta.

### Ejercicio 5 · Tres categorías

Escribe una función `clasificar_gasto(monto)` con tres categorías: menor a 5 000 es "menor",
de 5 000 a 50 000 es "medio", y de ahí para arriba es "mayor". Pruébala con seis montos,
incluidos los dos límites exactos.

### Ejercicio 6 · La rama inalcanzable

Escribe a propósito una versión de `clasificar_gasto` con las condiciones en el orden
equivocado. Después escribe el código que **demuestra** que una de las categorías nunca se
alcanza, recorriendo muchos montos y contando cuántos caen en cada una.

## Los límites

### Ejercicio 7 · Probar la frontera

Toma tu función del ejercicio 5 y pruébala con los valores justo por debajo, exactamente en, y
justo por arriba de cada límite. Son seis pruebas.

Di en un comentario, para cada límite, si el valor exacto debería caer en la categoría de abajo o
en la de arriba, y por qué.

### Ejercicio 8 · Una regla de negocio de tu área

Escribe un programa que clasifique algo de tu carrera en al menos tres categorías: un cliente por
su antigüedad, un proveedor por su cumplimiento o un gasto por su monto.

Las categorías tienen que ser excluyentes: ningún caso puede caer en dos. Y tienes que probar con
el valor exacto de cada límite, que es donde se descubre si querías mayor o mayor o igual.
"""),

md("""
---
## Tres ideas para llevarse

**Una comparación devuelve `True` o `False`.** Nunca "casi" ni "depende". Esa es toda la materia
prima con la que se construye una decisión, y por eso se puede guardar en una variable.

**La sangría es la estructura.** Los cuatro espacios son lo único que dice qué líneas pertenecen a
cada rama del `if`. No son estilo.

**El orden del `elif` decide.** De lo más exigente a lo menos. Invertirlo hace que la primera rama
se trague todos los casos y deja una categoría inalcanzable, sin lanzar ningún error.

La siguiente sesión es cómo combinar varias condiciones y qué pasa cuando una decisión vive
dentro de otra.
"""),

md("""
---
# Soluciones

### Ejercicio 1

```python
impresiones = 148230
clics = 5074
canal = "Instagram"

print("¿Los clics son exactamente 5074?  ", clics == 5074)
print("¿El canal no es TikTok?           ", canal != "TikTok")
print("¿Pasa de cinco mil clics?         ", clics > 5000)
print("¿Es una campaña chica?            ", impresiones < 50000)
print("¿Llegó o pasó los 5074 clics?     ", clics >= 5074)
print("¿Cabe en cien mil impresiones?    ", impresiones <= 100000)
```

Escribir la pregunta al lado no es adorno. Cuando una condición se lee mal, casi siempre es porque
la pregunta que se quería hacer no era la que quedó escrita.

### Ejercicio 2

```python
supera_la_meta = clics / impresiones >= 0.03
es_canal_pagado = canal in ("Instagram", "Facebook", "Google")
paso_el_presupuesto = 38500 > 40000

print("Supera la meta:      ", supera_la_meta)
print("Es un canal pagado:  ", es_canal_pagado)
print("Pasó el presupuesto: ", paso_el_presupuesto)
print()
print("Condiciones cumplidas:", supera_la_meta + es_canal_pagado + paso_el_presupuesto, "de 3")
```

Nombrar la comparación como una afirmación hace que el `if` de después se lea solo:
`if supera_la_meta:` dice más que `if clics / impresiones >= 0.03:`.

### Ejercicio 3

```python
VERSIONES = ["Instagram", "instagram", "INSTAGRAM", " Instagram", "Instagram "]

print("Comparación directa:")
for v in VERSIONES:
    print(f"  {v!r:<14} == 'Instagram' -> {v == 'Instagram'}")

print("\\nNormalizando antes:")
for v in VERSIONES:
    print(f"  {v!r:<14} -> {v.strip().lower() == 'instagram'}")
```

Solo una de las cinco pasa la comparación directa. Normalizando pasan las cinco.

Esto es literalmente lo que hace `str.strip().str.title()` en la semana 15, aplicado a una
columna entera en lugar de a un valor.

### Ejercicio 4

```python
PRESUPUESTO = 40000
inversion = 38500.00

if inversion <= PRESUPUESTO:
    print("Dentro de presupuesto")
    print(f"Quedan ${PRESUPUESTO - inversion:,.2f} disponibles")
else:
    print("Presupuesto excedido")
    print(f"Hay que justificar ${inversion - PRESUPUESTO:,.2f}")
```

Que `PRESUPUESTO` esté en mayúsculas y arriba es una convención: marca que es un valor fijo del
programa y no algo que se calcula. Cuando cambie la política, se cambia en un lugar.

### Ejercicio 5

```python
def clasificar_gasto(monto):
    if monto >= 50000:
        return "mayor"
    elif monto >= 5000:
        return "medio"
    else:
        return "menor"


for m in [1200, 4999, 5000, 49999, 50000, 128000]:
    print(f"{m:>8,} -> {clasificar_gasto(m)}")
```

Los dos límites exactos, 5 000 y 50 000, caen en la categoría de arriba porque usé `>=`. Con `>`
caerían en la de abajo, y las dos lecturas son defendibles: lo que no se vale es no haber
decidido.

### Ejercicio 6

```python
def clasificar_gasto_mal(monto):
    if monto >= 5000:
        return "medio"
    elif monto >= 50000:
        return "mayor"
    else:
        return "menor"


montos = list(range(0, 200001, 100))
conteo_bien = {"menor": 0, "medio": 0, "mayor": 0}
conteo_mal = {"menor": 0, "medio": 0, "mayor": 0}

for m in montos:
    conteo_bien[clasificar_gasto(m)] += 1
    conteo_mal[clasificar_gasto_mal(m)] += 1

print("Con el orden bueno:", conteo_bien)
print("Con el orden malo: ", conteo_mal)
```

Con el orden malo, `mayor` sale en cero sobre dos mil y un montos probados. Una categoría con
cero casos después de probar todo el rango es la firma de una rama inalcanzable.

Vale la pena guardar ese truco: cuando una clasificación se comporte raro, cuenta cuántos caen en
cada categoría antes de revisar la lógica renglón por renglón.

### Ejercicio 7

```python
for limite in [5000, 50000]:
    for m in [limite - 1, limite, limite + 1]:
        print(f"{m:>8,} -> {clasificar_gasto(m)}")
    print()

# En los dos límites, el valor exacto cae en la categoría de arriba, porque usé >=.
# Para un gasto me parece lo correcto: una política que dice "gastos de 50 000 en
# adelante requieren autorización" incluye al de exactamente 50 000. Si la política
# dijera "más de 50 000", habría que usar > y el de exactamente 50 000 pasaría sin
# autorización. La frase de la política es la que decide, no la comodidad del código.
```

Las seis pruebas caben en cuatro líneas gracias al ciclo anidado. Escribirlas a mano una por una
también funciona y se equivoca más.

### Ejercicio 8

No hay solución publicada porque la regla es distinta para cada quien. Se califica sobre tres
cosas: que las categorías sean excluyentes de verdad, que el `elif` vaya de lo más exigente a lo
menos, y que estén las pruebas con el valor exacto de cada límite con su justificación escrita.
"""),

]

write(OUT / "es" / "w06.ipynb", es)
print("wrote", OUT / "es" / "w06.ipynb")


en = [

md("""
# Data Analysis · Week 6
## Selection structures

**TIA502 · School of Business · Instructor David Escobar-Castillejos**

This is where a program starts differing from a formula. You already use `IF` in a spreadsheet,
so the idea is not new; what is new is that a decision can now span several lines and hold
whatever you like inside it.

By the end of this notebook you will be able to:

1. Use the six comparison operators, including the two that include the boundary.
2. Read a boolean expression and know its result is always `True` or `False`.
3. Write a simple decision and a double one, and say what changes between them.
4. Chain several cases with `elif` and explain why only the first matching branch runs.
5. Recognise the boundary error: the difference between greater than and greater or equal.

### How to use this notebook

Run the cells in order. Five fail on purpose and carry a comment saying so.

The case running through the session is classifying a campaign by its conversion rate: 5,074
clicks over 148,230 impressions, so 3.42 %.
"""),

md("""
---
# Block 1 · Comparing

Before deciding you have to ask. A comparison always answers the same thing: true or false.

| Operator | The question | Example | Result |
|---|---|---|---|
| `==` | Are they equal? | `conversion == 0.0342` | `True` |
| `!=` | Are they different? | `channel != "TikTok"` | `True` |
| `>` | Is it greater? | `clicks > 5000` | `True` |
| `<` | Is it less? | `clicks < 5000` | `False` |
| `>=` | Is it greater or equal? | `conversion >= 0.03` | `True` |
| `<=` | Is it less or equal? | `spend <= 38500` | `True` |

All six, running.
"""),

code("""
channel = "Instagram"
impressions = 148230
clicks = 5074
spend = 38500.00
conversion = clicks / impressions

print("conversion == 0.0342 :", round(conversion, 4) == 0.0342)
print("channel != 'TikTok'  :", channel != "TikTok")
print("clicks > 5000        :", clicks > 5000)
print("clicks < 5000        :", clicks < 5000)
print("conversion >= 0.03   :", conversion >= 0.03)
print("spend <= 38500       :", spend <= 38500)
"""),

md("""
The one people forget most is `!=`, for different. The one they confuse most is `==`, and that is
coming up in a moment.

## A comparison returns a value

Whatever you compare, the result is `True` or `False`. There is no "almost" and no "it depends".

That means a comparison is a value like any other: it can be stored, printed and asked about.
"""),

code("""
target = 0.03
hit_the_target = conversion >= target

print(hit_the_target)
print(type(hit_the_target))
print("It can be stored in a variable and used later.")
"""),

md("""
That is the whole raw material of a decision. And it is why a condition that looks complicated can
almost always be split into two simple comparisons and put back together.

## One equals stores, two equals asks

This is the classic error, and Python protects you from it.
"""),

code("""
# FAILS ON PURPOSE. A single equals sign inside an if.
source = 'if conversion = 0.03:\\n    print("equal")'

try:
    compile(source, "<example>", "exec")
except SyntaxError as e:
    print(f"SyntaxError: {e.msg}")
"""),

md("""
Python flags it as a syntax error and will not run it. That strictness is protecting you from a
much worse error: in other languages that line compiles, stores 0.03 in `conversion`, and the
condition is always true.

Here there is no way to write it by accident.
"""),

code("""
# One equals stores.
result = 0.03
print("After one equals:", result)

# Two equals asks and stores nothing.
print("With two equals:", result == 0.03)
print("result is still:", result)
"""),

md("""
## Comparing text

The six operators work on text too, and there are two surprises there.
"""),

code("""
print('"Instagram" == "Instagram" :', "Instagram" == "Instagram")
print('"Instagram" == "instagram" :', "Instagram" == "instagram")
print('"Instagram" == " Instagram":', "Instagram" == " Instagram")
"""),

md("""
Text comparison distinguishes capitals and does not forgive spaces. It is exactly the problem of
the eight regions in `sales.csv` you saw in week 1.1, and the reason week 15 has to normalise
before grouping.

The second surprise: `<` and `>` do work on text, and they compare alphabetically.
"""),

code("""
print('"Facebook" < "Instagram" :', "Facebook" < "Instagram")
print('"Zeta" < "alpha"         :', "Zeta" < "alpha", "<- capitals sort first")
"""),

md("""
That capitals sort before lowercase surprises people when sorting a list of hand-captured names.
It is another face of the same problem.

## Comparing decimals

You saw this in week 4 and here it bites differently.
"""),

code("""
# FAILS ON PURPOSE. Exact equality between decimals.
a = 0.1 + 0.2

print("a == 0.3 ?", a == 0.3)
print("a >= 0.3 ?", a >= 0.3)
print("The real value:", a)
"""),

md("""
`a == 0.3` is false and `a >= 0.3` is true, from the same pair of numbers.

Practical rule: **with decimals, use `>=` or `<=` rather than `==`.** And when you genuinely need
equality, use a tolerance.
"""),

md("""
---
# Block 2 · Deciding

The same structure you already use in a spreadsheet, written across two lines instead of inside
one long formula.

```
=IF(D2>=0.03, "Acceptable", "Review")
```
"""),

code("""
impressions = 148230
clicks = 5074

conversion = clicks / impressions

if conversion >= 0.03:
    status = "Acceptable"
    print("The campaign stays live.")
else:
    status = "Review"
    print("The targeting needs another look.")

print(f"{conversion:.2%} · {status}")
"""),

md("""
Four things the spreadsheet formula cannot do and this can.

**The colon** closes the condition. Without it, `SyntaxError` right there.

**The indentation** is what says which lines belong to each branch. The four spaces are not
decoration, they are the structure.

**Each branch can hold several lines.** Here each one assigns a variable and prints as well. A
sheet formula can only return a value.

**After the `if`**, the last line sits outside the indentation, so it prints whatever happens.

Change the conversion and run it again to see the other branch.
"""),

code("""
conversion = 0.021

if conversion >= 0.03:
    status = "Acceptable"
    print("The campaign stays live.")
else:
    status = "Review"
    print("The targeting needs another look.")

print(f"{conversion:.2%} · {status}")
"""),

md("""
Only one branch ran. Never both, and always one of the two.

## The three forms of selection

| Form | When it is used | Structure |
|---|---|---|
| Simple | There is only something to do if it holds | `if condition:` |
| Double | There are two paths and one is always taken | `if` / `else` |
| Multiple | There are three or more mutually exclusive categories | `if` / `elif` / `else` |

The simple one, with no `else`, is for when there is nothing to do in the other case.
"""),

code("""
conversion = 0.0342
alerts = []

if conversion < 0.01:
    alerts.append("Critical conversion")

if spend > 30000:
    alerts.append("High spend")

print("Alerts:", alerts or "none")
"""),

md("""
Two simple `if` statements, one after the other. They are independent: both get evaluated and
**both can hold**.

That is the difference from `elif`, which is in the next block.
"""),

md("""
---
# Block 3 · Several paths

Three categories, and the order you write them in decides which one wins.
"""),

code("""
conversion = 0.0342

if conversion >= 0.05:
    status = "Excellent"
elif conversion >= 0.03:
    status = "Acceptable"
else:
    status = "Review"

print(f"{conversion:.2%} · {status}")
"""),

md("""
The first condition is evaluated. If it fails, the second. **Once one holds, the rest are never
even read.**

The trace at 3.42 %:

| Step | Condition | Holds? | `status` |
|---|---|---|---|
| 1 | `0.0342 >= 0.05` | No | – |
| 2 | `0.0342 >= 0.03` | Yes | `Acceptable` |
| 3 | `else` | Not evaluated | `Acceptable` |

## Why the order decides

It runs from most demanding to least. The other way round, everything good would fall into the
weak category.

At 3.42 % both versions agree, so the error does not show. Compare them with a campaign at 6 %.
"""),

code("""
def classify_right(conversion):
    if conversion >= 0.05:
        return "Excellent"
    elif conversion >= 0.03:
        return "Acceptable"
    else:
        return "Review"


def classify_wrong(conversion):
    \"\"\"The same three rules, with the thresholds the wrong way round.\"\"\"
    if conversion >= 0.03:
        return "Acceptable"
    elif conversion >= 0.05:
        return "Excellent"
    else:
        return "Review"


for rate in [0.061, 0.0342, 0.021, 0.050]:
    right = classify_right(rate)
    wrong = classify_wrong(rate)
    mark = "  <-- different" if right != wrong else ""
    print(f"{rate:>7.2%}   {right:<11} {wrong:<11}{mark}")
"""),

md("""
There it is. With the order reversed, **"Excellent" is unreachable**: any campaign that clears 5 %
has already cleared 3 % and gets caught by the first branch.

The worst part is that the function does not blow up, does not warn, and classifies three out of
four cases correctly. It only gets the best ones wrong, which are exactly the ones you wanted to
spot.
"""),

code("""
# Check: does any rate reach "Excellent" with the reversed order?
possible = [i / 1000 for i in range(0, 101)]
excellent = [r for r in possible if classify_wrong(r) == "Excellent"]

print("Rates reaching Excellent with the bad order:", len(excellent))
print("With the good order:", len([r for r in possible if classify_right(r) == "Excellent"]))
"""),

md("""
Zero against fifty-one. An unreachable branch is an error no ordinary run finds, because seeing it
means testing the case that never arrives.

## The boundary error

**Predict before you run.** With a conversion of exactly 0.03, which status prints?

- **A.** `Acceptable`, because it reached the target.
- **B.** `Review`, because the operator asks for strictly greater.
- **C.** An error, because there is no `elif`.
- **D.** Both, because it satisfies both conditions.
"""),

code("""
conversion = 0.03

if conversion > 0.03:
    status = "Acceptable"
else:
    status = "Review"

print(status)
"""),

md("""
The answer is **B**. `>` leaves out whoever sits exactly on the target, `>=` includes them.

A campaign that hit the objective precisely comes out classified as needing review. That is the
boundary error, and it is not found by testing round values above and below: you have to test
**the exact boundary**.
"""),

code("""
for rate in [0.0299, 0.03, 0.0301]:
    with_gt = "Acceptable" if rate > 0.03 else "Review"
    with_gte = "Acceptable" if rate >= 0.03 else "Review"
    print(f"{rate:.4f}   with >  : {with_gt:<11} with >= : {with_gte}")
"""),

md("""
Only the middle row changes. The other two behave identically under both operators, which is why a
test that skips the exact boundary finds nothing.

Notice the `"Acceptable" if rate > 0.03 else "Review"` in that cell. It is the short form of an
`if`/`else` when all you want is to pick between two values, and it fits on one line.

## Classifying a whole table

With today's material you can already walk several campaigns and classify all of them.
"""),

code("""
CAMPAIGNS = [
    ("Instagram", 148230, 5074),
    ("Facebook", 96400, 2891),
    ("Google", 210500, 9840),
    ("TikTok", 54800, 3510),
    ("LinkedIn", 31200, 640),
]

print(f"{'Channel':<12}{'Conversion':>12}   Status")
print("-" * 39)

for channel, impressions, clicks in CAMPAIGNS:
    conversion = clicks / impressions
    status = classify_right(conversion)
    print(f"{channel:<12}{conversion:>12.2%}   {status}")
"""),

md("""
Five campaigns, three categories, and the `for` from week 3 doing the repetitive work.

## Four errors on your first decision

**One equals instead of two.** One stores, two asks. Python flags it as a syntax error, and that
saves you.

**Forgetting the colon.** Every condition ends in a colon. It is the most frequent syntax error of
the term.
"""),

code("""
# FAILS ON PURPOSE. The colon is missing.
try:
    compile('if conversion >= 0.03\\n    print("ok")', "<example>", "exec")
except SyntaxError as e:
    print(f"SyntaxError: {e.msg}")
"""),

md("""
**Getting the boundary wrong.** Greater than leaves out whoever sits exactly on target. Greater or
equal includes them. Decide which you want and test it with the exact value.

**Writing the conditions backwards.** From most demanding to least. The other way round, the first
branch swallows every case and one category becomes unreachable.
"""),

md("""
---
# Exercises

The solutions sit at the very bottom of the notebook.

## Comparing

### Exercise 1 · All six, with your data

Declare three variables from a campaign or a report you know and write six comparisons, one per
operator. Print each one alongside the question it answers.

### Exercise 2 · Storing a comparison

Store three comparisons in three variables with names that read like a statement, for example
`beats_the_target`. Print them and then print how many of the three are true.

Hint: `True` counts as 1 in a sum.

### Exercise 3 · Text that looks equal and is not

Write five versions of the same channel name with different capitals and spaces, and compare them
all against `"Instagram"`. Then fix the comparison so all five come back true.

Hint: `.strip()` removes spaces and `.lower()` goes to lowercase.

## Deciding

### Exercise 4 · A double decision

Write an `if`/`else` that classifies a spend as "within budget" or "over budget", with a budget of
40,000. Have each branch print two lines: the classification and a different recommendation.

### Exercise 5 · Three categories

Write a function `classify_spend(amount)` with three categories: under 5,000 is "small", from
5,000 to 50,000 is "medium", and above that is "large". Test it with six amounts, including both
exact boundaries.

### Exercise 6 · The unreachable branch

Deliberately write a version of `classify_spend` with the conditions in the wrong order. Then write
the code that **proves** one of the categories is never reached, by walking many amounts and
counting how many land in each.

## The boundaries

### Exercise 7 · Testing the frontier

Take your function from exercise 5 and test it with the values just below, exactly on, and just
above each boundary. That is six tests.

Say in a comment, for each boundary, whether the exact value should fall into the lower or the
upper category, and why.

### Exercise 8 · A business rule from your field

Write a program that classifies something from your field into at least three categories: a
customer by tenure, a supplier by compliance, or an expense by amount.

The categories have to be mutually exclusive: no case may fall into two. And you have to test the
exact value of every boundary, which is where you discover whether you wanted greater or greater
or equal.
"""),

md("""
---
## Three ideas to take away

**A comparison returns `True` or `False`.** Never "almost" and never "it depends". That is the
whole raw material a decision is built from, and it is why it can be stored in a variable.

**Indentation is the structure.** The four spaces are the only thing saying which lines belong to
each branch of the `if`. They are not style.

**The order of the `elif` decides.** From most demanding to least. Reversing it makes the first
branch swallow every case and leaves a category unreachable, without raising anything.

Next session is how to combine several conditions and what happens when one decision lives inside
another.
"""),

md("""
---
# Solutions

### Exercise 1

```python
impressions = 148230
clicks = 5074
channel = "Instagram"

print("Are the clicks exactly 5074?     ", clicks == 5074)
print("Is the channel not TikTok?       ", channel != "TikTok")
print("Does it clear five thousand clicks?", clicks > 5000)
print("Is it a small campaign?          ", impressions < 50000)
print("Did it reach or pass 5074 clicks?", clicks >= 5074)
print("Does it fit in a hundred thousand?", impressions <= 100000)
```

Writing the question beside it is not decoration. When a condition reads wrong, it is almost always
because the question you meant to ask is not the one that ended up written.

### Exercise 2

```python
beats_the_target = clicks / impressions >= 0.03
is_paid_channel = channel in ("Instagram", "Facebook", "Google")
over_budget = 38500 > 40000

print("Beats the target:", beats_the_target)
print("Is a paid channel:", is_paid_channel)
print("Over budget:      ", over_budget)
print()
print("Conditions met:", beats_the_target + is_paid_channel + over_budget, "of 3")
```

Naming a comparison as a statement makes the later `if` read by itself: `if beats_the_target:` says
more than `if clicks / impressions >= 0.03:`.

### Exercise 3

```python
VERSIONS = ["Instagram", "instagram", "INSTAGRAM", " Instagram", "Instagram "]

print("Direct comparison:")
for v in VERSIONS:
    print(f"  {v!r:<14} == 'Instagram' -> {v == 'Instagram'}")

print("\\nNormalising first:")
for v in VERSIONS:
    print(f"  {v!r:<14} -> {v.strip().lower() == 'instagram'}")
```

Only one of the five passes the direct comparison. Normalising, all five pass.

This is literally what `str.strip().str.title()` does in week 15, applied to a whole column instead
of a single value.

### Exercise 4

```python
BUDGET = 40000
spend = 38500.00

if spend <= BUDGET:
    print("Within budget")
    print(f"${BUDGET - spend:,.2f} still available")
else:
    print("Over budget")
    print(f"${spend - BUDGET:,.2f} needs justifying")
```

That `BUDGET` is capitalised and sits at the top is a convention: it marks a fixed value of the
program rather than something computed. When the policy changes, it changes in one place.

### Exercise 5

```python
def classify_spend(amount):
    if amount >= 50000:
        return "large"
    elif amount >= 5000:
        return "medium"
    else:
        return "small"


for a in [1200, 4999, 5000, 49999, 50000, 128000]:
    print(f"{a:>8,} -> {classify_spend(a)}")
```

Both exact boundaries, 5,000 and 50,000, fall into the upper category because I used `>=`. With `>`
they would fall into the lower one, and both readings are defensible: what is not acceptable is not
having decided.

### Exercise 6

```python
def classify_spend_wrong(amount):
    if amount >= 5000:
        return "medium"
    elif amount >= 50000:
        return "large"
    else:
        return "small"


amounts = list(range(0, 200001, 100))
count_right = {"small": 0, "medium": 0, "large": 0}
count_wrong = {"small": 0, "medium": 0, "large": 0}

for a in amounts:
    count_right[classify_spend(a)] += 1
    count_wrong[classify_spend_wrong(a)] += 1

print("With the good order:", count_right)
print("With the bad order: ", count_wrong)
```

With the bad order, `large` comes out at zero across two thousand and one amounts tested. A category
with zero cases after covering the whole range is the signature of an unreachable branch.

That trick is worth keeping: when a classification behaves oddly, count how many land in each
category before reading the logic line by line.

### Exercise 7

```python
for boundary in [5000, 50000]:
    for a in [boundary - 1, boundary, boundary + 1]:
        print(f"{a:>8,} -> {classify_spend(a)}")
    print()

# At both boundaries the exact value falls into the upper category, because I used >=.
# For an expense that seems right to me: a policy saying "expenses of 50,000 and above
# require approval" includes the one at exactly 50,000. If the policy said "more than
# 50,000", it would need > and the one at exactly 50,000 would pass without approval.
# The wording of the policy decides, not the convenience of the code.
```

The six tests fit in four lines thanks to the nested loop. Writing them out one by one also works
and gets miscounted more often.

### Exercise 8

There is no published solution, because the rule is different for everyone. It is graded on three
things: that the categories are genuinely mutually exclusive, that the `elif` runs from most
demanding to least, and that the tests on each exact boundary are there with their reasoning
written down.
"""),

]

write(OUT / "en" / "w06.ipynb", en)
print("wrote", OUT / "en" / "w06.ipynb")
