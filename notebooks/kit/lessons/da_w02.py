"""notebooks/analisis-de-datos/{es,en}/w02.ipynb

Source deck: ppts/python/analisis-de-datos/{es,en}/w02.*.yaml
No repository source: the deck's own pseudocode, translated and verified here.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from nbkit import md, code, write, REPO
from diagram import bonus_flowchart, symbols_figure

OUT = REPO / "notebooks" / "analisis-de-datos"

# ════════════════════════════════════════════════════════════════════ ESPAÑOL

es = [

md("""
# Análisis de Datos · Semana 2
## Diseño de algoritmos

**TIA502 · Facultad de Empresariales · Profesor David Escobar-Castillejos**

La sesión en clase es en papel, a propósito: si el algoritmo no está claro escrito a mano, el
código no lo va a aclarar. Este cuaderno es lo que sigue. Toma el mismo caso de la clase, el
bono anual, y lo ejecuta, para que puedas comprobar en lugar de creer.

Sobre todo hay una afirmación que la clase hace y que aquí se demuestra: **el orden de dos
condiciones cambia quién cobra**, aunque las dos versiones se vean igual de correctas.

Al terminar este cuaderno vas a poder:

1. Definir qué es un algoritmo y distinguirlo de una instrucción que suena clara.
2. Nombrar las cinco propiedades y reconocer cómo se rompe cada una.
3. Leer pseudocódigo y traducirlo a Python casi línea por línea.
4. Medir el efecto de cambiar el orden de dos condiciones.
5. Descomponer un problema grande en partes que se resuelven por separado.

### Cómo se usa este cuaderno

Ejecuta las celdas en orden. Dos fallan a propósito y llevan un comentario que lo dice.

No necesitas archivos ni instalar nada: todo lo de esta sesión son cuentas sobre datos que el
cuaderno escribe él mismo.
"""),

md("""
---
# Bloque 1 · Qué es un algoritmo

Un algoritmo es una secuencia finita de pasos que resuelve un problema. Lo que lo separa de
una instrucción cualquiera no es la longitud ni el vocabulario: es que **no deja nada a
criterio de quien lo ejecuta**.

Dos personas siguiendo el mismo algoritmo con los mismos datos tienen que llegar al mismo
resultado. Esa es la prueba práctica, y sirve igual para un cálculo de nómina que para un
proceso documentado de la empresa.

## La misma instrucción, dicha dos veces

Esto llegó por correo:

> Calcula el bono de fin de año de cada empleado según su antigüedad y su desempeño.

Suena claro. No lo es. Cuánto es "según su antigüedad" lo decide quien lo lea, y dos personas
van a decidir distinto. Esto sí es un algoritmo:

```
SI antiguedad < 12 ENTONCES
    bono = 0
SI NO SI evaluacion >= 4.5 ENTONCES
    bono = sueldo * 0.20
SI NO
    bono = sueldo * 0.10
```

Nadie que lo siga tiene que adivinar.

## Las cinco propiedades

| Propiedad | Qué significa | Cómo se rompe |
|---|---|---|
| Finito | Termina en pasos contables | "Repite hasta que quede bien" |
| Preciso | Ningún paso admite lectura doble | "Aplica el descuento habitual" |
| Definido | Mismos datos, mismo resultado | Un paso que depende de quien lo lee |
| Con entrada | Recibe cero o más datos | Un cálculo sin origen de sus números |
| Con salida | Produce al menos un resultado | Termina sin decir qué obtuvo |

Las tres primeras se pueden comprobar corriendo código. Vamos con la tercera, que es la más
fácil de romper sin darse cuenta.

## "Definido": mismos datos, mismo resultado

Escribamos el bono como una función. Una función es un algoritmo con nombre: recibe entradas,
hace pasos y devuelve una salida.
"""),

code("""
def bono_anual(sueldo, antiguedad, evaluacion):
    \"\"\"Calcula el bono de fin de año. Devuelve una cantidad en pesos.\"\"\"
    if antiguedad < 12:
        return 0
    elif evaluacion >= 4.5:
        return sueldo * 0.20
    else:
        return sueldo * 0.10


print(bono_anual(45000, 30, 4.8))
print(bono_anual(45000, 30, 4.8))
print(bono_anual(45000, 30, 4.8))
"""),

md("""
Tres veces los mismos datos, tres veces el mismo resultado. Eso es estar definido. Suena obvio
hasta que ves lo contrario.
"""),

code("""
# FALLA LA PRUEBA A PROPÓSITO. Este procedimiento no es un algoritmo.
import random

def bono_a_ojo(sueldo, antiguedad, evaluacion):
    \"\"\"«Aplica el bono habitual según cómo veas al empleado.»\"\"\"
    criterio = random.choice([0.0, 0.10, 0.20])
    return sueldo * criterio


print(bono_a_ojo(45000, 30, 4.8))
print(bono_a_ojo(45000, 30, 4.8))
print(bono_a_ojo(45000, 30, 4.8))
"""),

md("""
Mismos datos, tres resultados. `bono_a_ojo` no es un algoritmo, es un procedimiento que
depende de algo que no está escrito.

El `random` de arriba es un truco para hacerlo visible en tres líneas. En la vida real ese
azar tiene otro nombre: se llama "criterio del que revisa", y produce exactamente el mismo
efecto. Si el proceso de tu empresa no está escrito con precisión, dos personas van a dar dos
respuestas y las dos van a creer que siguieron el proceso.

## La prueba, escrita como código

Que dos ejecuciones coincidan se puede verificar en lugar de mirar a ojo.
"""),

code("""
def es_definido(funcion, datos, intentos=50):
    \"\"\"Corre la función muchas veces con los mismos datos y dice si siempre coincide.\"\"\"
    resultados = {funcion(*datos) for _ in range(intentos)}
    return len(resultados) == 1


print("bono_anual está definido:", es_definido(bono_anual, (45000, 30, 4.8)))
print("bono_a_ojo está definido:", es_definido(bono_a_ojo, (45000, 30, 4.8)))
"""),

md("""
`es_definido` guarda los resultados en un conjunto, que es una colección que no admite
repetidos. Si al final el conjunto tiene un solo elemento, las cincuenta corridas dieron lo
mismo. Los conjuntos se ven a fondo en la semana 13, y por ahora basta con esa idea.
"""),

# ──────────────────────────────────────────────────────────── bloque 2

md("""
---
# Bloque 2 · Cómo se escribe un algoritmo

Dos formas, y las dos sirven para lo mismo: dejarlo claro antes de traducirlo a un lenguaje.

## El diagrama de flujo

Cuatro símbolos y ya está.

| Símbolo | Qué representa | Ejemplo del caso |
|---|---|---|
| Óvalo | El inicio o el final | `INICIO` · `FIN` |
| Paralelogramo | Entrada de datos o salida de resultados | `LEER antiguedad` · `ESCRIBIR bono` |
| Rectángulo | Un proceso: un cálculo o una asignación | `bono = sueldo * 0.20` |
| Rombo | Una decisión con dos salidas | `¿antiguedad menor a 12?` |
| Flecha | El orden en que se recorren los pasos | Del rombo a uno de sus dos caminos |

""" + symbols_figure("es") + """

## El caso completo, dibujado

El algoritmo del bono como diagrama de flujo. Síguelo con el dedo desde `INICIO` y fíjate en dos
cosas: del rombo salen siempre dos flechas, y las tres ramas vuelven a juntarse antes de escribir
el resultado.

""" + bonus_flowchart("es") + """

Un rombo con una sola salida no es una decisión, y una rama que no llega a `FIN` deja al programa
a medias. Las dos cosas saltan a la vista en el dibujo y no se ven leyendo código.

## El pseudocódigo

El mismo algoritmo, escrito.

```
INICIO
    LEER sueldo, antiguedad, evaluacion

    SI antiguedad < 12 ENTONCES
        bono = 0
    SI NO SI evaluacion >= 4.5 ENTONCES
        bono = sueldo * 0.20
    SI NO
        bono = sueldo * 0.10

    ESCRIBIR bono
FIN
```

No es Python ni ningún otro lenguaje. Es el plan, y por eso lo entiende quien no programa. La
sangría marca qué instrucciones pertenecen a cada rama, y es la única estructura que tiene.

## La traducción

Del plan al lenguaje, casi línea por línea. Cambian cinco palabras y aparecen dos puntos al
final de cada condición.

| Pseudocódigo | Python |
|---|---|
| `SI ... ENTONCES` | `if ...:` |
| `SI NO SI ... ENTONCES` | `elif ...:` |
| `SI NO` | `else:` |
| `ESCRIBIR` | `print` |
| `LEER` | un parámetro de la función |
"""),

code("""
# El pseudocódigo de arriba, corriendo. Compáralos línea por línea.
sueldo, antiguedad, evaluacion = 45000, 30, 4.8

if antiguedad < 12:
    bono = 0
elif evaluacion >= 4.5:
    bono = sueldo * 0.20
else:
    bono = sueldo * 0.10

print(bono)
"""),

md("""
Esa es toda la traducción. El plan es el mismo, y por eso escribirlo bien en papel es la mitad
del trabajo.

## La traza, ejecutada

En clase la traza se llena a mano en el pizarrón. Aquí la puede llenar el propio programa.

**Predice antes de correr.** Un empleado con 11 meses y evaluación de 5.0. ¿Cuánto bono le
toca?

- **A.** El 20 %, porque su evaluación es excelente.
- **B.** Cero, porque la antigüedad se revisa primero.
- **C.** El 10 %, porque no cumple una de las dos.
- **D.** Depende de su sueldo.
"""),

code("""
def bono_con_traza(sueldo, antiguedad, evaluacion):
    \"\"\"El mismo cálculo, contando en voz alta por dónde pasa.\"\"\"
    print(f"LEER: sueldo={sueldo}, antiguedad={antiguedad}, evaluacion={evaluacion}")

    print(f"  ¿antiguedad < 12?  {antiguedad} < 12  ->  {antiguedad < 12}")
    if antiguedad < 12:
        bono = 0
        print("  Entra a la primera rama. Las demás ya no se evalúan.")
    else:
        print(f"  ¿evaluacion >= 4.5?  {evaluacion} >= 4.5  ->  {evaluacion >= 4.5}")
        if evaluacion >= 4.5:
            bono = sueldo * 0.20
            print("  Entra a la segunda rama.")
        else:
            bono = sueldo * 0.10
            print("  Ninguna se cumplió. Entra al SI NO final.")

    print(f"ESCRIBIR: bono = {bono:,.2f}")
    return bono


bono_con_traza(38000, 11, 5.0)
"""),

md("""
La respuesta es **B**. La evaluación de 5.0 **ni se revisa**: cuando una rama se cumple, las
siguientes no se leen. Esa es la regla del `elif`, y es la fuente de la mitad de los errores
lógicos que vas a escribir este semestre.

Corre la traza con otros datos para verla tomar los otros caminos.
"""),

code("""
print("=== Antigüedad suficiente y buena evaluación ===")
bono_con_traza(45000, 30, 4.8)

print()
print("=== Antigüedad suficiente y evaluación regular ===")
bono_con_traza(52000, 60, 4.2)
"""),

# ──────────────────────────────────────────────────────────── el orden

md("""
---
## La trampa del orden, demostrada

En clase se dice que cambiar el orden de las dos condiciones cambia quién cobra bono. Aquí se
puede medir.

Esta es la versión con las condiciones al revés. Léela: se ve igual de razonable que la
original, y alguien podría escribirla sin sospechar nada.
"""),

code("""
def bono_orden_cambiado(sueldo, antiguedad, evaluacion):
    \"\"\"Las mismas tres reglas, con la evaluación revisada primero.\"\"\"
    if evaluacion >= 4.5:
        return sueldo * 0.20
    elif antiguedad < 12:
        return 0
    else:
        return sueldo * 0.10
"""),

md("""
Ahora una plantilla de seis personas, escrita a mano, y las dos versiones aplicadas a cada una.
"""),

code("""
PLANTILLA = [
    # nombre, sueldo, antigüedad en meses, evaluación
    ("Ana",   45000, 30, 4.8),
    ("Beto",  38000, 11, 5.0),
    ("Carla", 52000, 60, 4.2),
    ("Diego", 41000, 24, 4.5),
    ("Elena", 36000,  6, 3.9),
    ("Fer",   30000,  3, 4.9),
]

print(f"{'Nombre':<8}{'Meses':>6}{'Eval':>6}{'Original':>12}{'Cambiado':>12}   ")
for nombre, sueldo, meses, evalua in PLANTILLA:
    uno = bono_anual(sueldo, meses, evalua)
    dos = bono_orden_cambiado(sueldo, meses, evalua)
    marca = "  <-- distinto" if uno != dos else ""
    print(f"{nombre:<8}{meses:>6}{evalua:>6}{uno:>12,.0f}{dos:>12,.0f}{marca}")
"""),

md("""
Dos de seis cobran distinto, y no son dos cualesquiera: son justamente los empleados nuevos con
buena evaluación. La versión original les da cero, la cambiada les da el 20 %.

Cuál de las dos es la correcta depende de la política de la empresa, y ese es el punto. **El
código no puede decidirlo, y las dos versiones corren igual de bien.** Lo único que separa una
política de la otra es el orden en que escribiste dos renglones.

Ponle número al costo.
"""),

code("""
costo_uno = sum(bono_anual(s, m, e) for _, s, m, e in PLANTILLA)
costo_dos = sum(bono_orden_cambiado(s, m, e) for _, s, m, e in PLANTILLA)

print(f"Costo total con el orden original:  {costo_uno:>12,.2f}")
print(f"Costo total con el orden cambiado:  {costo_dos:>12,.2f}")
print(f"Diferencia:                         {costo_dos - costo_uno:>12,.2f}")
print(f"Sobre seis empleados. Multiplícalo por una plantilla de trescientos.")
"""),

md("""
Trece mil seiscientos pesos de diferencia en seis personas, por el orden de dos condiciones.
Nadie que lea el código va a notarlo, porque las dos versiones son correctas por separado.

Por eso el pseudocódigo se revisa en papel con alguien más antes de traducirlo.
"""),

# ──────────────────────────────────────────────────────────── bloque 3

md("""
---
# Bloque 3 · Cómo se ataca un problema grande

Partiéndolo hasta que cada pedazo sea algo que ya sabes resolver.

## Las cinco fases

| Fase | Qué se hace |
|---|---|
| 01 · Entender el problema | Qué se pide exactamente, y qué no se está pidiendo |
| 02 · Identificar datos | Qué entra, qué sale y qué falta por conseguir |
| 03 · Diseñar la solución | El algoritmo en papel, en pseudocódigo o en diagrama |
| 04 · Escribirlo en código | La traducción, que es la parte más mecánica de todas |
| 05 · Probarlo y corregir | Con casos normales y con los casos límite que rompen todo |

Fíjate en la proporción: cuatro de las cinco fases ocurren antes o después de escribir código.
La cuarta, que es la que la gente cree que es "programar", es la más corta.

## Descomponer, con el mismo caso

"Haz el reporte de bonos del año" es un problema grande. Partido, son cuatro problemas chicos
y cada uno cabe en una función.
"""),

code("""
def calcular_bono(sueldo, antiguedad, evaluacion):
    \"\"\"Parte 1: la regla de negocio, una sola.\"\"\"
    if antiguedad < 12:
        return 0
    elif evaluacion >= 4.5:
        return sueldo * 0.20
    else:
        return sueldo * 0.10


def clasificar(bono, sueldo):
    \"\"\"Parte 2: traducir una cantidad a una etiqueta que la gente entienda.\"\"\"
    if bono == 0:
        return "sin bono"
    elif bono >= sueldo * 0.20:
        return "bono completo"
    else:
        return "bono parcial"


print(calcular_bono(45000, 30, 4.8), clasificar(9000, 45000))
print(calcular_bono(38000, 11, 5.0), clasificar(0, 38000))
"""),

code("""
def procesar_plantilla(plantilla):
    \"\"\"Parte 3: aplicar las dos anteriores a todos, y devolver el resultado.\"\"\"
    resultado = []
    for nombre, sueldo, meses, evalua in plantilla:
        bono = calcular_bono(sueldo, meses, evalua)
        resultado.append((nombre, sueldo, bono, clasificar(bono, sueldo)))
    return resultado


def imprimir_reporte(filas):
    \"\"\"Parte 4: presentarlo. Ninguna cuenta ocurre aquí.\"\"\"
    print(f"{'Nombre':<8}{'Sueldo':>10}{'Bono':>10}  Estado")
    print("-" * 44)
    for nombre, sueldo, bono, estado in filas:
        print(f"{nombre:<8}{sueldo:>10,.0f}{bono:>10,.0f}  {estado}")
    print("-" * 44)
    print(f"{'Total':<8}{'':>10}{sum(f[2] for f in filas):>10,.0f}")


imprimir_reporte(procesar_plantilla(PLANTILLA))
"""),

md("""
Cuatro funciones, cada una con un trabajo. `calcular_bono` no sabe imprimir, `imprimir_reporte`
no sabe calcular, y por eso puedes cambiar la política de bonos sin tocar el reporte.

Esa separación es lo que hace que un programa se pueda arreglar seis meses después. Si las
cuatro cosas estuvieran en un solo bloque de treinta líneas, cambiar el porcentaje te obligaría
a leerlo entero.

## Fase 05: los casos límite

La quinta fase es la que casi nadie hace y la que encuentra los errores. Un caso límite es un
dato que está justo en la frontera de una condición.
"""),

code("""
LIMITES = [
    ("Exactamente 12 meses", 40000, 12, 4.0),
    ("Exactamente 4.5",      40000, 24, 4.5),
    ("Justo abajo de 4.5",   40000, 24, 4.49),
    ("Cero meses",           40000,  0, 5.0),
    ("Sueldo cero",              0, 24, 5.0),
]

for etiqueta, sueldo, meses, evalua in LIMITES:
    print(f"{etiqueta:<22} -> {calcular_bono(sueldo, meses, evalua):>10,.2f}")
"""),

md("""
Los dos primeros son los importantes. `antiguedad < 12` deja fuera al de exactamente doce
meses, o sea que **sí cobra**. Y `evaluacion >= 4.5` incluye al de exactamente 4.5.

Ninguna de las dos decisiones es obvia leyendo el correo original, y las dos están tomadas en
el código. Si la política decía "a partir del año cumplido", el código está bien; si decía
"más de un año", está mal por un mes.

Esa clase de error es la que solo aparece probando la frontera.
"""),

code("""
# FALLA A PROPÓSITO. Una entrada que la función nunca esperó.
try:
    print(calcular_bono(40000, "veinticuatro", 4.8))
except TypeError as e:
    print("TypeError:", e)
"""),

md("""
La función supone que le pasan números. Cuando no, truena, y esa es la buena noticia: truena
en el momento y con un mensaje que nombra el problema.

La semana 4 entra a los tipos en serio, y ahí verás por qué esto es preferible a que el
programa siga como si nada.
"""),

# ──────────────────────────────────────────────────────────── ejercicios

md("""
---
# Ejercicios

Las soluciones están hasta abajo del cuaderno.

## Leer y traducir

### Ejercicio 1 · De instrucción a algoritmo

Esta instrucción llegó por correo:

> Dale descuento a los clientes frecuentes, y uno más grande si además compran mucho.

Escríbela como pseudocódigo, inventando los umbrales que hagan falta. Después dila en un
comentario: cuáles fueron las tres cosas que tuviste que decidir tú porque el correo no las
decía.

### Ejercicio 2 · Del pseudocódigo a Python

Traduce este pseudocódigo a una función y pruébala con tres envíos distintos.

```
INICIO
    LEER peso, destino

    SI destino = "local" ENTONCES
        costo = 50
    SI NO SI peso <= 5 ENTONCES
        costo = 120
    SI NO
        costo = 120 + (peso - 5) * 18

    ESCRIBIR costo
FIN
```

### Ejercicio 3 · La traza a mano

Sin correr nada, escribe qué devuelve tu función del ejercicio 2 con estos tres casos:
`(3, "local")`, `(5, "nacional")` y `(8, "nacional")`. Después córrela y compara.

## Medir y romper

### Ejercicio 4 · El orden, otra vez

Toma tu función del ejercicio 2 y escribe una segunda versión con las condiciones en otro
orden. Aplica las dos a una lista de seis envíos e imprime en cuáles difieren.

### Ejercicio 5 · Los casos límite del envío

Prueba tu función con los valores que están justo en la frontera: peso exactamente 5, peso 0,
peso negativo y un destino que no sea ni "local" ni "nacional".

Di en un comentario cuáles de esos casos la función maneja bien y cuáles habría que arreglar.

### Ejercicio 6 · Descomponer un proceso

Toma el cálculo del bono y agrégale una regla: quien tenga más de 60 meses de antigüedad recibe
5 000 pesos extra, sin importar su evaluación.

Hazlo sin tocar `calcular_bono`. Escribe una función nueva que use la anterior y le sume el
extra, y explica en un comentario por qué esa forma es mejor que editar la original.

## Con tu área

### Ejercicio 7 · Tu propio proceso

Elige un proceso que ya exista en tu carrera, como aprobar un gasto, calificar a un proveedor o
segmentar a un cliente, y escríbelo en pseudocódigo con al menos una decisión. Después
tradúcelo a una función y pruébalo con cinco casos, incluidos dos casos límite.

La prueba: pásale tu pseudocódigo a un compañero. Si él obtiene otro resultado con los mismos
datos, algo quedó ambiguo y todavía no era un algoritmo.
"""),

# ──────────────────────────────────────────────────────────── resumen

md("""
---
## Tres ideas para llevarse

**Un algoritmo no deja nada a criterio.** Si dos personas siguiendo tus pasos obtienen
resultados distintos, todavía no es un algoritmo. La prueba se puede escribir como código, y la
escribiste hoy.

**El orden de las condiciones decide.** Revisar antigüedad antes que desempeño le cambió el
bono a dos de seis personas y trece mil seiscientos pesos al total, sin que ninguna de las dos
versiones se vea mal.

**El código es la parte mecánica.** Cuatro de las cinco fases ocurren antes o después de
escribirlo. Si el plan está claro en papel, traducirlo es cuestión de sintaxis.

La siguiente sesión es por qué existen los paradigmas de programación y qué hace un lenguaje
con lo que escribes.
"""),

# ──────────────────────────────────────────────────────────── soluciones

md("""
---
# Soluciones

### Ejercicio 1

```
INICIO
    LEER compras_al_anio, monto_total

    SI compras_al_anio >= 12 Y monto_total >= 50000 ENTONCES
        descuento = 0.15
    SI NO SI compras_al_anio >= 12 ENTONCES
        descuento = 0.08
    SI NO
        descuento = 0
    ESCRIBIR descuento
FIN
```

Las tres decisiones que tuve que tomar yo, porque el correo no las decía: **cuántas compras son
"frecuente"** (elegí doce al año), **cuánto es "comprar mucho"** (elegí cincuenta mil de monto
acumulado) y **de cuánto son los dos descuentos** (8 % y 15 %).

Tus umbrales pueden ser otros y estar igual de bien. Lo que no puede pasar es que se queden sin
decidir, porque entonces cada quien pone los suyos.

### Ejercicio 2

```python
def costo_envio(peso, destino):
    if destino == "local":
        return 50
    elif peso <= 5:
        return 120
    else:
        return 120 + (peso - 5) * 18


print(costo_envio(3, "local"))
print(costo_envio(5, "nacional"))
print(costo_envio(8, "nacional"))
```

Da 50, 120 y 174. Nota que `destino == "local"` va primero, así que un envío local de veinte
kilos cuesta 50: el peso ni se revisa. Igual que con el bono, el orden ya tomó una decisión de
negocio.

### Ejercicio 3

`(3, "local")` da 50 porque entra a la primera rama. `(5, "nacional")` da 120 porque `5 <= 5`
es verdadero, y ese es el caso límite. `(8, "nacional")` da `120 + 3 * 18`, o sea 174.

Si predijiste 174 para el tercero, ya estás leyendo condiciones encadenadas bien.

### Ejercicio 4

```python
def costo_envio_cambiado(peso, destino):
    if peso <= 5:
        return 120
    elif destino == "local":
        return 50
    else:
        return 120 + (peso - 5) * 18


ENVIOS = [(3, "local"), (5, "nacional"), (8, "nacional"),
          (2, "local"), (12, "local"), (7, "local")]

for peso, destino in ENVIOS:
    uno = costo_envio(peso, destino)
    dos = costo_envio_cambiado(peso, destino)
    marca = "  <-- distinto" if uno != dos else ""
    print(f"{peso:>3} kg  {destino:<10}{uno:>7}{dos:>7}{marca}")
```

Difieren en los envíos locales de cinco kilos o menos: la primera versión cobra 50 y la segunda
cobra 120. Son tres de los seis, y todos los que cambian son los baratos, que suelen ser los
más frecuentes.

### Ejercicio 5

```python
print("Peso exactamente 5: ", costo_envio(5, "nacional"))
print("Peso 0:             ", costo_envio(0, "nacional"))
print("Peso negativo:      ", costo_envio(-3, "nacional"))
print("Destino desconocido:", costo_envio(4, "internacional"))

# Peso 5 está bien: la regla dice "hasta 5 kilos" y <= lo incluye.
# Peso 0 devuelve 120, que probablemente esté mal: un envío sin peso no existe,
#   y la función debería rechazarlo en vez de cobrarlo.
# Peso negativo también devuelve 120, y eso sí es un error claro.
# Destino "internacional" cae al último SI NO y se cobra como nacional, que es
#   la peor de las cuatro: no truena, y factura de menos sin avisar.
```

Los dos últimos son el mismo tipo de problema que viste con las regiones sucias en la semana
1.1. Un valor que nadie esperó no rompe nada, cae en la rama de "todo lo demás" y produce un
número equivocado con cara de correcto.

### Ejercicio 6

```python
def bono_con_antiguedad(sueldo, antiguedad, evaluacion):
    base = calcular_bono(sueldo, antiguedad, evaluacion)
    if antiguedad > 60:
        return base + 5000
    return base


for nombre, sueldo, meses, evalua in PLANTILLA:
    print(f"{nombre:<8}{calcular_bono(sueldo, meses, evalua):>10,.0f}"
          f"{bono_con_antiguedad(sueldo, meses, evalua):>12,.0f}")

# Es mejor que editar la original por tres razones. La regla vieja sigue
# existiendo y se puede seguir usando donde aplique. Si el extra resulta ser un
# error, se quita borrando una función en lugar de deshacer un cambio dentro de
# otra. Y cualquiera que lea el código ve que son dos reglas de negocio distintas,
# una de desempeño y una de permanencia, en vez de una sola enredada.
```

Solo Carla cambia, con sus 60 meses justos... y no cambia, porque la regla dice **más** de 60 y
ella tiene exactamente 60. Otro caso límite, y esta vez apareció solo.

### Ejercicio 7

No hay solución publicada porque el proceso es distinto para cada quien. Se califica sobre tres
cosas: que el pseudocódigo tenga al menos una decisión con sus dos salidas, que la traducción a
función corresponda línea por línea con el plan, y que los dos casos límite estén justo en la
frontera de una condición y no simplemente sean datos raros.
"""),

]

write(OUT / "es" / "w02.ipynb", es)
print("wrote", OUT / "es" / "w02.ipynb")


# ════════════════════════════════════════════════════════════════════ ENGLISH

en = [

md("""
# Data Analysis · Week 2
## Algorithm design

**TIA502 · School of Business · Instructor David Escobar-Castillejos**

The class session runs on paper, deliberately: if the algorithm is not clear written by hand,
code will not clarify it. This notebook is what comes next. It takes the same case from class,
the annual bonus, and runs it, so you can check rather than believe.

There is one claim in particular that the class makes and this notebook proves: **the order of
two conditions changes who gets paid**, even though both versions look equally correct.

By the end of this notebook you will be able to:

1. Define what an algorithm is and tell it apart from an instruction that merely sounds clear.
2. Name the five properties and recognise how each one breaks.
3. Read pseudocode and translate it into Python almost line by line.
4. Measure the effect of changing the order of two conditions.
5. Break a large problem into parts that can be solved separately.

### How to use this notebook

Run the cells in order. Two fail on purpose and carry a comment saying so.

You need no files and nothing installed: everything in this session is arithmetic over data the
notebook writes itself.
"""),

md("""
---
# Block 1 · What an algorithm is

An algorithm is a finite sequence of steps that solves a problem. What separates it from any
old instruction is not the length or the vocabulary: it is that it **leaves nothing to the
judgement of whoever runs it**.

Two people following the same algorithm with the same data have to arrive at the same result.
That is the practical test, and it works as well for a payroll calculation as for a documented
company process.

## The same instruction, said twice

This arrived by email:

> Work out each employee's year-end bonus according to their tenure and their performance.

It sounds clear. It is not. How much "according to their tenure" means is decided by whoever
reads it, and two people will decide differently. This one is an algorithm:

```
IF tenure < 12 THEN
    bonus = 0
ELSE IF review >= 4.5 THEN
    bonus = salary * 0.20
ELSE
    bonus = salary * 0.10
```

Nobody following it has to guess.

## The five properties

| Property | What it means | How it breaks |
|---|---|---|
| Finite | It ends in countable steps | "Repeat until it looks right" |
| Precise | No step admits two readings | "Apply the usual discount" |
| Defined | Same data, same result | A step that depends on who reads it |
| With input | It takes zero or more values | A calculation with no source for its numbers |
| With output | It produces at least one result | It ends without saying what it got |

The first three can be checked by running code. Start with the third, which is the easiest to
break without noticing.

## "Defined": same data, same result

Write the bonus as a function. A function is an algorithm with a name: it takes inputs, does
steps and returns an output.
"""),

code("""
def annual_bonus(salary, tenure, review):
    \"\"\"Work out the year-end bonus. Returns an amount in pesos.\"\"\"
    if tenure < 12:
        return 0
    elif review >= 4.5:
        return salary * 0.20
    else:
        return salary * 0.10


print(annual_bonus(45000, 30, 4.8))
print(annual_bonus(45000, 30, 4.8))
print(annual_bonus(45000, 30, 4.8))
"""),

md("""
Three times the same data, three times the same result. That is what being defined means. It
sounds obvious until you see the opposite.
"""),

code("""
# FAILS THE TEST ON PURPOSE. This procedure is not an algorithm.
import random

def bonus_by_feel(salary, tenure, review):
    \"\"\"\"Apply the usual bonus depending on how you see the employee.\"\"\"
    criterion = random.choice([0.0, 0.10, 0.20])
    return salary * criterion


print(bonus_by_feel(45000, 30, 4.8))
print(bonus_by_feel(45000, 30, 4.8))
print(bonus_by_feel(45000, 30, 4.8))
"""),

md("""
Same data, three results. `bonus_by_feel` is not an algorithm, it is a procedure that depends on
something that is not written down.

The `random` above is a trick to make that visible in three lines. In real life that randomness
goes by another name: it is called "the reviewer's judgement", and it produces exactly the same
effect. If your company's process is not written down precisely, two people will give two
answers and both will believe they followed the process.

## The test, written as code

That two runs agree can be verified rather than eyeballed.
"""),

code("""
def is_defined(function, data, attempts=50):
    \"\"\"Run the function many times on the same data and say whether it always agrees.\"\"\"
    results = {function(*data) for _ in range(attempts)}
    return len(results) == 1


print("annual_bonus is defined: ", is_defined(annual_bonus, (45000, 30, 4.8)))
print("bonus_by_feel is defined:", is_defined(bonus_by_feel, (45000, 30, 4.8)))
"""),

md("""
`is_defined` stores the results in a set, which is a collection that holds no repeats. If the
set ends up with a single element, all fifty runs gave the same thing. Sets get covered
properly in week 13, and for now that idea is enough.
"""),

md("""
---
# Block 2 · How an algorithm gets written

Two forms, and both do the same job: making it clear before it gets translated into a language.

## The flowchart

Four symbols and that is it.

| Symbol | What it represents | Example from the case |
|---|---|---|
| Oval | The start or the end | `START` · `END` |
| Parallelogram | Input of data or output of results | `READ tenure` · `WRITE bonus` |
| Rectangle | A process: a calculation or an assignment | `bonus = salary * 0.20` |
| Diamond | A decision with two exits | `is tenure under 12?` |
| Arrow | The order the steps are walked in | From the diamond to one of its two paths |

""" + symbols_figure("en") + """

## The whole case, drawn

The bonus algorithm as a flowchart. Trace it with your finger from `START` and watch for two
things: a diamond always has two arrows leaving it, and the three branches come back together
before the result gets written.

""" + bonus_flowchart("en") + """

A diamond with one exit is not a decision, and a branch that never reaches `END` leaves the
program half done. Both jump out of the drawing and neither shows up when reading code.

## The pseudocode

The same algorithm, written out.

```
START
    READ salary, tenure, review

    IF tenure < 12 THEN
        bonus = 0
    ELSE IF review >= 4.5 THEN
        bonus = salary * 0.20
    ELSE
        bonus = salary * 0.10

    WRITE bonus
END
```

It is not Python and it is not any other language. It is the plan, which is why somebody who
does not program can read it. The indentation marks which instructions belong to each branch,
and it is the only structure it has.

## The translation

From the plan to the language, almost line by line. Five words change and a colon appears at
the end of each condition.

| Pseudocode | Python |
|---|---|
| `IF ... THEN` | `if ...:` |
| `ELSE IF ... THEN` | `elif ...:` |
| `ELSE` | `else:` |
| `WRITE` | `print` |
| `READ` | a parameter of the function |
"""),

code("""
# The pseudocode above, running. Compare them line by line.
salary, tenure, review = 45000, 30, 4.8

if tenure < 12:
    bonus = 0
elif review >= 4.5:
    bonus = salary * 0.20
else:
    bonus = salary * 0.10

print(bonus)
"""),

md("""
That is the whole translation. The plan is the same, which is why writing it properly on paper
is half the work.

## The trace, executed

In class the trace is filled in by hand on the board. Here the program can fill it in itself.

**Predict before you run.** An employee with 11 months and a review of 5.0. How much bonus do
they get?

- **A.** 20 %, because their review is excellent.
- **B.** Zero, because tenure is checked first.
- **C.** 10 %, because they fail one of the two.
- **D.** It depends on their salary.
"""),

code("""
def bonus_with_trace(salary, tenure, review):
    \"\"\"The same calculation, saying out loud which way it goes.\"\"\"
    print(f"READ: salary={salary}, tenure={tenure}, review={review}")

    print(f"  is tenure < 12?  {tenure} < 12  ->  {tenure < 12}")
    if tenure < 12:
        bonus = 0
        print("  Enters the first branch. The others are never evaluated.")
    else:
        print(f"  is review >= 4.5?  {review} >= 4.5  ->  {review >= 4.5}")
        if review >= 4.5:
            bonus = salary * 0.20
            print("  Enters the second branch.")
        else:
            bonus = salary * 0.10
            print("  Neither held. Falls through to the final ELSE.")

    print(f"WRITE: bonus = {bonus:,.2f}")
    return bonus


bonus_with_trace(38000, 11, 5.0)
"""),

md("""
The answer is **B**. The review of 5.0 is **never even checked**: once a branch holds, the ones
after it are not read. That is the rule of `elif`, and it is the source of half the logic errors
you will write this term.

Run the trace with other data to watch it take the other paths.
"""),

code("""
print("=== Enough tenure and a strong review ===")
bonus_with_trace(45000, 30, 4.8)

print()
print("=== Enough tenure and an average review ===")
bonus_with_trace(52000, 60, 4.2)
"""),

md("""
---
## The ordering trap, demonstrated

In class the claim is that changing the order of the two conditions changes who gets a bonus.
Here it can be measured.

This is the version with the conditions the other way round. Read it: it looks just as
reasonable as the original, and somebody could write it without suspecting a thing.
"""),

code("""
def bonus_reordered(salary, tenure, review):
    \"\"\"The same three rules, with the review checked first.\"\"\"
    if review >= 4.5:
        return salary * 0.20
    elif tenure < 12:
        return 0
    else:
        return salary * 0.10
"""),

md("""
Now a roster of six people, written by hand, with both versions applied to each.
"""),

code("""
ROSTER = [
    # name, salary, tenure in months, review
    ("Ana",   45000, 30, 4.8),
    ("Beto",  38000, 11, 5.0),
    ("Carla", 52000, 60, 4.2),
    ("Diego", 41000, 24, 4.5),
    ("Elena", 36000,  6, 3.9),
    ("Fer",   30000,  3, 4.9),
]

print(f"{'Name':<8}{'Months':>7}{'Review':>7}{'Original':>12}{'Reordered':>12}   ")
for name, salary, months, review in ROSTER:
    one = annual_bonus(salary, months, review)
    two = bonus_reordered(salary, months, review)
    mark = "  <-- different" if one != two else ""
    print(f"{name:<8}{months:>7}{review:>7}{one:>12,.0f}{two:>12,.0f}{mark}")
"""),

md("""
Two of six get paid differently, and they are not just any two: they are precisely the new
employees with strong reviews. The original version gives them zero, the reordered one gives
them 20 %.

Which of the two is correct depends on company policy, and that is the point. **The code cannot
decide it, and both versions run equally well.** The only thing separating one policy from the
other is the order you wrote two lines in.

Put a number on the cost.
"""),

code("""
cost_one = sum(annual_bonus(s, m, r) for _, s, m, r in ROSTER)
cost_two = sum(bonus_reordered(s, m, r) for _, s, m, r in ROSTER)

print(f"Total cost with the original order:  {cost_one:>12,.2f}")
print(f"Total cost with the reordered one:   {cost_two:>12,.2f}")
print(f"Difference:                          {cost_two - cost_one:>12,.2f}")
print(f"Over six employees. Multiply it by a roster of three hundred.")
"""),

md("""
Thirteen thousand six hundred pesos of difference across six people, from the order of two
conditions. Nobody reading the code will notice, because both versions are correct on their
own.

That is why pseudocode gets reviewed on paper with somebody else before it is translated.
"""),

md("""
---
# Block 3 · How a large problem gets attacked

By splitting it until each piece is something you already know how to solve.

## The five phases

| Phase | What happens |
|---|---|
| 01 · Understand the problem | What exactly is being asked, and what is not |
| 02 · Identify the data | What goes in, what comes out and what is still missing |
| 03 · Design the solution | The algorithm on paper, as pseudocode or as a diagram |
| 04 · Write it in code | The translation, the most mechanical part of all |
| 05 · Test it and fix it | With ordinary cases and with the edge cases that break everything |

Look at the proportion: four of the five phases happen before or after code gets written. The
fourth, the one people think of as "programming", is the shortest.

## Decomposing, with the same case

"Produce the annual bonus report" is a large problem. Split up, it is four small problems and
each one fits in a function.
"""),

code("""
def compute_bonus(salary, tenure, review):
    \"\"\"Part 1: the business rule, and only that.\"\"\"
    if tenure < 12:
        return 0
    elif review >= 4.5:
        return salary * 0.20
    else:
        return salary * 0.10


def classify(bonus, salary):
    \"\"\"Part 2: turning an amount into a label people understand.\"\"\"
    if bonus == 0:
        return "no bonus"
    elif bonus >= salary * 0.20:
        return "full bonus"
    else:
        return "partial bonus"


print(compute_bonus(45000, 30, 4.8), classify(9000, 45000))
print(compute_bonus(38000, 11, 5.0), classify(0, 38000))
"""),

code("""
def process_roster(roster):
    \"\"\"Part 3: applying the two above to everyone, and returning the result.\"\"\"
    result = []
    for name, salary, months, review in roster:
        bonus = compute_bonus(salary, months, review)
        result.append((name, salary, bonus, classify(bonus, salary)))
    return result


def print_report(rows):
    \"\"\"Part 4: presenting it. No arithmetic happens here.\"\"\"
    print(f"{'Name':<8}{'Salary':>10}{'Bonus':>10}  Status")
    print("-" * 46)
    for name, salary, bonus, status in rows:
        print(f"{name:<8}{salary:>10,.0f}{bonus:>10,.0f}  {status}")
    print("-" * 46)
    print(f"{'Total':<8}{'':>10}{sum(r[2] for r in rows):>10,.0f}")


print_report(process_roster(ROSTER))
"""),

md("""
Four functions, each with one job. `compute_bonus` cannot print, `print_report` cannot
calculate, and that is why you can change the bonus policy without touching the report.

That separation is what makes a program fixable six months later. Were all four things in a
single thirty-line block, changing the percentage would force you to read the whole thing.

## Phase 05: the edge cases

The fifth phase is the one almost nobody does and the one that finds the errors. An edge case
is a value sitting right on the boundary of a condition.
"""),

code("""
EDGES = [
    ("Exactly 12 months", 40000, 12, 4.0),
    ("Exactly 4.5",       40000, 24, 4.5),
    ("Just under 4.5",    40000, 24, 4.49),
    ("Zero months",       40000,  0, 5.0),
    ("Zero salary",           0, 24, 5.0),
]

for label, salary, months, review in EDGES:
    print(f"{label:<20} -> {compute_bonus(salary, months, review):>10,.2f}")
"""),

md("""
The first two are the important ones. `tenure < 12` leaves out the person with exactly twelve
months, meaning they **do** get paid. And `review >= 4.5` includes the person at exactly 4.5.

Neither decision is obvious from reading the original email, and both are taken in the code. If
the policy said "from the completed year onwards", the code is right; if it said "more than a
year", it is wrong by one month.

That class of error only shows up by testing the boundary.
"""),

code("""
# FAILS ON PURPOSE. An input the function never expected.
try:
    print(compute_bonus(40000, "twenty four", 4.8))
except TypeError as e:
    print("TypeError:", e)
"""),

md("""
The function assumes it is handed numbers. When it is not, it blows up, and that is the good
news: it blows up on the spot and with a message that names the problem.

Week 4 gets into types properly, and there you will see why this is preferable to the program
carrying on as if nothing happened.
"""),

md("""
---
# Exercises

The solutions sit at the very bottom of the notebook.

## Reading and translating

### Exercise 1 · From instruction to algorithm

This instruction arrived by email:

> Give a discount to frequent customers, and a bigger one if they also buy a lot.

Write it as pseudocode, inventing whatever thresholds it needs. Then say in a comment which
three things you had to decide yourself because the email did not say.

### Exercise 2 · From pseudocode to Python

Translate this pseudocode into a function and test it with three different shipments.

```
START
    READ weight, destination

    IF destination = "local" THEN
        cost = 50
    ELSE IF weight <= 5 THEN
        cost = 120
    ELSE
        cost = 120 + (weight - 5) * 18

    WRITE cost
END
```

### Exercise 3 · The trace by hand

Without running anything, write down what your function from exercise 2 returns for these three
cases: `(3, "local")`, `(5, "national")` and `(8, "national")`. Then run it and compare.

## Measuring and breaking

### Exercise 4 · The order, again

Take your function from exercise 2 and write a second version with the conditions in a
different order. Apply both to a list of six shipments and print which ones differ.

### Exercise 5 · The shipping edge cases

Test your function with the values sitting right on the boundary: weight exactly 5, weight 0, a
negative weight, and a destination that is neither "local" nor "national".

Say in a comment which of those the function handles well and which would need fixing.

### Exercise 6 · Decomposing a process

Take the bonus calculation and add a rule: anyone with more than 60 months of tenure receives an
extra 5,000 pesos, regardless of their review.

Do it without touching `compute_bonus`. Write a new function that uses the old one and adds the
extra, and explain in a comment why that is better than editing the original.

## With your own field

### Exercise 7 · Your own process

Pick a process that already exists in your field, such as approving an expense, rating a
supplier or segmenting a customer, and write it as pseudocode with at least one decision. Then
translate it into a function and test it with five cases, two of them edge cases.

The test: hand your pseudocode to a classmate. If they get a different result from the same
data, something stayed ambiguous and it was not an algorithm yet.
"""),

md("""
---
## Three ideas to take away

**An algorithm leaves nothing to judgement.** If two people following your steps get different
results, it is not an algorithm yet. The test can be written as code, and you wrote it today.

**The order of the conditions decides.** Checking tenure before performance changed the bonus
for two people out of six and thirteen thousand six hundred pesos on the total, without either
version looking wrong.

**Code is the mechanical part.** Four of the five phases happen before or after writing it. If
the plan is clear on paper, translating it is a matter of syntax.

Next session is why programming paradigms exist and what a language does with what you write.
"""),

md("""
---
# Solutions

### Exercise 1

```
START
    READ purchases_per_year, total_spend

    IF purchases_per_year >= 12 AND total_spend >= 50000 THEN
        discount = 0.15
    ELSE IF purchases_per_year >= 12 THEN
        discount = 0.08
    ELSE
        discount = 0
    WRITE discount
END
```

The three decisions I had to make myself, because the email did not: **how many purchases count
as "frequent"** (I chose twelve a year), **how much is "buying a lot"** (I chose fifty thousand
of accumulated spend) and **how big the two discounts are** (8 % and 15 %).

Your thresholds can be different and equally right. What cannot happen is that they go
undecided, because then everyone picks their own.

### Exercise 2

```python
def shipping_cost(weight, destination):
    if destination == "local":
        return 50
    elif weight <= 5:
        return 120
    else:
        return 120 + (weight - 5) * 18


print(shipping_cost(3, "local"))
print(shipping_cost(5, "national"))
print(shipping_cost(8, "national"))
```

That gives 50, 120 and 174. Note that `destination == "local"` comes first, so a local shipment
of twenty kilos costs 50: the weight is never checked. As with the bonus, the order has already
taken a business decision.

### Exercise 3

`(3, "local")` gives 50 because it enters the first branch. `(5, "national")` gives 120 because
`5 <= 5` is true, and that is the edge case. `(8, "national")` gives `120 + 3 * 18`, so 174.

If you predicted 174 for the third one, you are already reading chained conditions properly.

### Exercise 4

```python
def shipping_cost_reordered(weight, destination):
    if weight <= 5:
        return 120
    elif destination == "local":
        return 50
    else:
        return 120 + (weight - 5) * 18


SHIPMENTS = [(3, "local"), (5, "national"), (8, "national"),
             (2, "local"), (12, "local"), (7, "local")]

for weight, destination in SHIPMENTS:
    one = shipping_cost(weight, destination)
    two = shipping_cost_reordered(weight, destination)
    mark = "  <-- different" if one != two else ""
    print(f"{weight:>3} kg  {destination:<10}{one:>7}{two:>7}{mark}")
```

They differ on local shipments of five kilos or less: the first version charges 50 and the
second charges 120. That is three of the six, and everything that changes is at the cheap end,
which tends to be the most frequent.

### Exercise 5

```python
print("Weight exactly 5:  ", shipping_cost(5, "national"))
print("Weight 0:          ", shipping_cost(0, "national"))
print("Negative weight:   ", shipping_cost(-3, "national"))
print("Unknown destination:", shipping_cost(4, "international"))

# Weight 5 is fine: the rule says "up to 5 kilos" and <= includes it.
# Weight 0 returns 120, which is probably wrong: a shipment with no weight does
#   not exist, and the function should reject it rather than bill it.
# A negative weight also returns 120, and that is a clear error.
# Destination "international" falls into the final ELSE and gets billed as
#   national, which is the worst of the four: it does not blow up, and it
#   under-bills without saying anything.
```

The last two are the same kind of problem you saw with the dirty regions in week 1.1. A value
nobody expected breaks nothing, falls into the "everything else" branch and produces a wrong
number wearing a correct face.

### Exercise 6

```python
def bonus_with_seniority(salary, tenure, review):
    base = compute_bonus(salary, tenure, review)
    if tenure > 60:
        return base + 5000
    return base


for name, salary, months, review in ROSTER:
    print(f"{name:<8}{compute_bonus(salary, months, review):>10,.0f}"
          f"{bonus_with_seniority(salary, months, review):>12,.0f}")

# It beats editing the original for three reasons. The old rule still exists and
# can still be used where it applies. If the extra turns out to be a mistake, it
# comes off by deleting a function instead of undoing a change inside another one.
# And anyone reading the code sees two distinct business rules, one about
# performance and one about staying, instead of a single tangled one.
```

Only Carla would change, with her exactly 60 months... and she does not change, because the rule
says **more** than 60 and she has exactly 60. Another edge case, and this time it turned up by
itself.

### Exercise 7

There is no published solution, because the process is different for everyone. It is graded on
three things: that the pseudocode has at least one decision with both exits, that the
translation into a function matches the plan line for line, and that the two edge cases sit
right on the boundary of a condition rather than simply being odd data.
"""),

]

write(OUT / "en" / "w02.ipynb", en)
print("wrote", OUT / "en" / "w02.ipynb")
