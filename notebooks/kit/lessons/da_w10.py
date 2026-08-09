"""notebooks/analisis-de-datos/{es,en}/w10.ipynb

Source deck: ppts/python/analisis-de-datos/{es,en}/w10.*.yaml
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from nbkit import md, code, write, REPO

OUT = REPO / "notebooks" / "analisis-de-datos"

es = [

md("""
# Análisis de Datos · Semana 10
## Funciones definidas por el usuario

**TIA502 · Facultad de Empresariales · Profesor David Escobar-Castillejos**

Ya usas `PROMEDIO` en una hoja sin saber cómo suma ni cómo divide. Hoy aprendes a fabricar el
tuyo.

El argumento que convence no es "reutilizar código". Es que **una función se puede probar sola**,
y una fórmula pegada en trescientas celdas no.

Al terminar este cuaderno vas a poder:

1. Explicar qué resuelve una función, más allá de ahorrar líneas.
2. Definir una función con `def`, con nombre, parámetros y cuerpo.
3. Distinguir parámetro de argumento.
4. Devolver un valor con `return`, y decir en qué se diferencia de imprimirlo.
5. Reconocer el ámbito de un nombre y por qué lo de adentro no sale.

### Cómo se usa este cuaderno

Ejecuta las celdas en orden. Cinco fallan a propósito y llevan un comentario que lo dice.

El caso de aquí a la semana 13 es de finanzas: el pago mensual de un crédito.
"""),

md("""
---
# Bloque 1 · Por qué existen las funciones

No para escribir menos. Para tener **un solo lugar** donde el cálculo pueda estar bien o estar
mal.

Así se ve el mismo cálculo repetido a mano, para dos créditos:
"""),

code("""
# Crédito A
i = 0.18 / 12
pago_a = 250000 * (i * (1 + i) ** 36) / ((1 + i) ** 36 - 1)

# Crédito B
i = 0.24 / 12
pago_b = 120000 * (i * (1 + i) ** 24) / ((1 + i) ** 24 - 1)

print(f"A: {pago_a:,.2f}")
print(f"B: {pago_b:,.2f}")
"""),

md("""
Funciona, y tiene dos problemas que no se ven al leerlo.

La fórmula está escrita dos veces, así que si está mal hay que encontrar y arreglar cada copia.
Y la variable `i` se reusó: la segunda línea pisó a la primera, y si alguien mueve el orden de
los bloques el resultado cambia sin avisar.

La misma cuenta, empaquetada:
"""),

code("""
def pago_mensual(capital, tasa_anual, meses):
    i = tasa_anual / 12
    factor = (1 + i) ** meses
    return capital * (i * factor) / (factor - 1)


pago_a = pago_mensual(250000, 0.18, 36)
pago_b = pago_mensual(120000, 0.24, 24)

print(f"A: {pago_a:,.2f}")
print(f"B: {pago_b:,.2f}")
"""),

md("""
Los mismos dos números. La diferencia es qué pasa cuando la fórmula está mal: arriba hay que
arreglar cada copia, abajo se arregla una vez y las dos llamadas quedan correctas.

## El argumento de verdad

Una función **se puede probar sola**. Una fórmula pegada en trescientas celdas solo se puede
revisar celda por celda, y nadie lo hace.

Probar significa esto: le das entradas cuya respuesta ya conoces y compruebas que la devuelve.
"""),

code("""
# Un crédito de 12,000 al 0.0000001 % anual a 12 meses debería pagar casi 1,000 al mes,
# porque casi no hay intereses.
print("Sin intereses prácticamente:", round(pago_mensual(12000, 0.0000001, 12), 2))

# Y el pago siempre tiene que ser mayor que capital entre meses, porque hay intereses.
print("Pago:", round(pago_mensual(250000, 0.18, 36), 2))
print("Capital entre meses:", round(250000 / 36, 2))
print("¿El pago es mayor?", pago_mensual(250000, 0.18, 36) > 250000 / 36)
"""),

md("""
Esas tres comprobaciones caben en una celda y se pueden volver a correr cada vez que alguien
toque la fórmula. Eso es lo que la hoja de cálculo no te da.
"""),

md("""
---
# Bloque 2 · Cómo se escribe una función

Cinco partes, y cada una tiene una regla que no se negocia.

| Parte | Qué es | En el ejemplo |
|---|---|---|
| `def` | La palabra que la declara | `def` |
| Nombre | Cómo se le llama después | `pago_mensual` |
| Parámetros | Los huecos que hay que llenar | `capital, tasa_anual, meses` |
| Cuerpo | El cálculo, con sangría | Las tres líneas de adentro |
| `return` | Lo que entrega al terminar | El pago calculado |
"""),

code("""
def pago_mensual(capital, tasa_anual, meses):
    \"\"\"Calcula el pago fijo mensual de un crédito.

    capital     lo que se presta, en pesos
    tasa_anual  la tasa nominal anual, como decimal: 0.18 es 18 %
    meses       el plazo
    \"\"\"
    i = tasa_anual / 12
    factor = (1 + i) ** meses

    return capital * (i * factor) / (factor - 1)


pago = pago_mensual(250000, 0.18, 36)
print(f"Pago mensual: ${pago:,.2f}")
"""),

md("""
**`def` y el nombre.** El nombre dice qué devuelve, no qué hace por dentro. `pago_mensual`, no
`calcular_cosas`.

**Los parámetros.** Los tres huecos que la función necesita. Al llamarla se llenan en ese mismo
orden.

**El docstring**, esa cadena entre comillas triples. Explica para qué sirve, y lo lee quien la
use sin abrir el cuerpo. Python lo guarda y se puede consultar.
"""),

code("""
print(pago_mensual.__doc__)
"""),

code("""
help(pago_mensual)
"""),

md("""
**`return`** devuelve el resultado y termina la función ahí mismo. Lo que venga después no corre.
"""),

code("""
def con_codigo_muerto(capital):
    return capital * 1.16
    print("Esta línea nunca se ejecuta")


print(con_codigo_muerto(1000))
print("Y no apareció ningún mensaje de adentro.")
"""),

md("""
## Parámetro no es lo mismo que argumento

Se confunden todo el tiempo y la distinción es sencilla.

**El parámetro** es el hueco que dejas al definirla: `capital`, `tasa_anual`, `meses`.

**El argumento** es el valor que llega al llamarla: `250000`, `0.18`, `36`.

El parámetro vive en la definición y el argumento en la llamada. Uno es la etiqueta del cajón,
el otro es lo que metes.
"""),

code("""
def describir_credito(capital, tasa_anual, meses):
    \"\"\"Los parámetros son capital, tasa_anual y meses.\"\"\"
    return f"{capital:,} pesos al {tasa_anual:.0%} a {meses} meses"


# Aquí los argumentos son 250000, 0.18 y 36.
print(describir_credito(250000, 0.18, 36))

# Y se pueden pasar por nombre, en cualquier orden.
print(describir_credito(meses=24, capital=120000, tasa_anual=0.24))
"""),

md("""
Pasarlos por nombre cuesta más letras y quita toda duda. Con tres números seguidos, nadie que
lea `pago_mensual(250000, 0.18, 36)` puede jurar cuál es cuál sin ir a ver la definición.
"""),

code("""
# FALLA A PROPÓSITO, y de dos formas distintas según cuáles dos intercambies.
import itertools

for orden in itertools.permutations([250000, 0.18, 36]):
    etiqueta = f"{orden[0]:>10,} {orden[1]:>10,} {orden[2]:>10,}"
    try:
        print(f"{etiqueta} -> {pago_mensual(*orden):>18,.2f}")
    except OverflowError as e:
        print(f"{etiqueta} -> OverflowError: {e}")
"""),

md("""
Seis órdenes posibles y tres desenlaces.

Uno es correcto, 9,038.10. Dos truenan con `OverflowError`, porque elevar 1.015 a la
doscientos cincuenta mil se sale de lo que cabe en un decimal. Y **tres devuelven un número sin
protestar.**

El peor de los tres es `pago_mensual(0.18, 250000, 36)`, que da 3,750.00. Es un pago mensual
perfectamente creíble para un crédito, y está calculado con el capital en el lugar de la tasa.

Los que truenan te avisan. El de 3,750 se va al reporte.
"""),

code("""
# Por eso conviene pasarlos por nombre cuando son varios y del mismo tipo.
print(pago_mensual(capital=250000, tasa_anual=0.18, meses=36))

# Y así, ni siquiera importa el orden en que los escribas.
print(pago_mensual(meses=36, capital=250000, tasa_anual=0.18))
"""),

md("""
## Reutilizada
"""),

code("""
creditos = [
    (250000, 0.18, 36),
    (120000, 0.24, 24),
    (80000, 0.15, 12),
]

print(f"{'Capital':>10}{'Tasa':>7}{'Meses':>7}{'Pago':>12}")
print("-" * 36)
for capital, tasa, meses in creditos:
    print(f"{capital:>10,}{tasa:>7.0%}{meses:>7}{pago_mensual(capital, tasa, meses):>12,.2f}")
"""),

md("""
Tres créditos, una sola fórmula. Agrega un cuarto a la lista y el ciclo no se toca.

## Devolver no es imprimir

Este es el error que más aparece en la primera entrega con funciones.
"""),

code("""
# FALLA A PROPÓSITO. La función imprime en lugar de devolver.
def pago_que_imprime(capital, tasa_anual, meses):
    i = tasa_anual / 12
    factor = (1 + i) ** meses
    print(capital * (i * factor) / (factor - 1))


total = pago_que_imprime(250000, 0.18, 36)

print("Lo que quedó en total:", total)
print("Su tipo:", type(total))
"""),

md("""
El número apareció en pantalla y `total` quedó en `None`. Una función que solo imprime es un
callejón sin salida: no se puede sumar, ni guardar, ni graficar.

Y el `None` no truena ahí. Truena tres líneas después.
"""),

code("""
# FALLA A PROPÓSITO. El None de arriba, usado como si fuera un número.
try:
    print(total * 36)
except TypeError as e:
    print("TypeError:", e)
"""),

md("""
Ese es el patrón que hay que reconocer: **`TypeError` con `NoneType` casi siempre significa que
a una función le falta el `return`.**

La regla: la función devuelve, y quien la llama decide si imprime.
"""),

code("""
def pago_que_devuelve(capital, tasa_anual, meses):
    i = tasa_anual / 12
    factor = (1 + i) ** meses
    return capital * (i * factor) / (factor - 1)


total = pago_que_devuelve(250000, 0.18, 36)

print("El pago:", round(total, 2))
print("A 36 meses:", round(total * 36, 2))
print("Intereses:", round(total * 36 - 250000, 2))
"""),

md("""
El mismo cálculo, y ahora el resultado sirve para tres cosas más.

## Una función que usa otra

Con la de arriba ya se puede escribir la que reporta el crédito completo, sin volver a escribir
la fórmula.
"""),

code("""
def resumen_credito(capital, tasa_anual, meses):
    \"\"\"Devuelve el pago mensual, el total pagado y los intereses.\"\"\"
    pago = pago_mensual(capital, tasa_anual, meses)
    total = pago * meses
    return pago, total, total - capital


pago, total, intereses = resumen_credito(250000, 0.18, 36)

print(f"Pago mensual: {pago:>12,.2f}")
print(f"Total pagado: {total:>12,.2f}")
print(f"Intereses:    {intereses:>12,.2f}")
print(f"Los intereses son el {intereses / capital if False else intereses / 250000:.1%} del capital")
"""),

md("""
`return pago, total, total - capital` devuelve tres cosas de golpe, empaquetadas en una tupla.
La línea que la recibe las desempaca en tres nombres.

Y fíjate en lo que **no** hay: `resumen_credito` no vuelve a escribir la fórmula del pago. La
pide. Si mañana descubres que la fórmula estaba mal, la arreglas en un lugar y las dos funciones
quedan correctas.
"""),

md("""
---
# Bloque 3 · Dónde vive cada nombre

Lo que se declara dentro de una función existe solo mientras esa función corre.
"""),

code("""
def calcular(capital):
    comision = capital * 0.02
    return capital + comision


print(calcular(250000))

# FALLA A PROPÓSITO. comision nació y murió dentro de la función.
try:
    print(comision)
except NameError as e:
    print("NameError:", e)
"""),

md("""
Las variables que nacen dentro de una función son suyas. Se crean cuando la llamas y desaparecen
cuando termina.

Eso no es una limitación, es la garantía de que una función no puede romper el resto del
programa por accidente. Y trae una consecuencia buena: **puedes reusar el mismo nombre sin
miedo.**
"""),

code("""
def una(x):
    factor = x * 2
    return factor


def otra(x):
    factor = x * 100      # el mismo nombre, y no se estorban
    return factor


print(una(5), otra(5))
"""),

md("""
El `factor` de una función y el `factor` de la otra son dos variables distintas que nunca se van
a ver.

## Lo que sí se ve desde adentro

Una función puede **leer** un nombre de afuera. Eso funciona y casi siempre es mala idea.
"""),

code("""
IVA = 0.16                    # una constante del programa

def con_iva(monto):
    return monto * (1 + IVA)   # lee IVA de afuera


print(con_iva(1000))
"""),

md("""
Funciona porque `IVA` está definido cuando la función corre. El problema aparece al mover la
función a otro archivo: se lleva su cuerpo y deja `IVA` atrás.
"""),

code("""
# FALLA A PROPÓSITO. La misma función, sin la constante que daba por hecha.
def con_impuesto(monto):
    return monto * (1 + TASA_QUE_NO_EXISTE)


try:
    print(con_impuesto(1000))
except NameError as e:
    print("NameError:", e)
"""),

md("""
La versión que sobrevive a la mudanza recibe todo lo que necesita.
"""),

code("""
def con_iva_portatil(monto, iva=0.16):
    \"\"\"Todo lo que necesita entra por la puerta.\"\"\"
    return monto * (1 + iva)


print(con_iva_portatil(1000))
print(con_iva_portatil(1000, 0.08))      # zona fronteriza
"""),

md("""
Ese `iva=0.16` es un argumento por omisión, y es el tema de la semana que entra. Va aquí para
que veas que la solución existe.

## Modificar desde adentro

Leer de afuera funciona. Asignar, no.
"""),

code("""
contador = 0

def sumar_uno():
    contador = contador_local = 1     # esto crea una variable NUEVA, local
    return contador


print("Devuelve:", sumar_uno())
print("Y la de afuera sigue en:", contador)
"""),

md("""
La de adentro y la de afuera se llaman igual y no son la misma. La asignación creó una local que
murió al terminar la función.

Existe una palabra para forzar lo contrario, `global`, y este curso no la usa. Una función que
modifica variables de afuera es exactamente la que no se puede probar sola, que es todo lo que
estamos tratando de evitar.

## Cuatro errores de la primera función

**Olvidar el `return`.** La función corre, calcula bien y devuelve `None`. El error aparece
líneas después.

**Predice antes de correr.** ¿Qué imprime este programa?

- **A.** 42, porque multiplica por dos.
- **B.** `None`, porque a la función le falta el `return`.
- **C.** 21, porque `n` no cambió.
- **D.** Un error, porque la función no hace nada.
"""),

code("""
def duplicar(n):
    n * 2


resultado = duplicar(21)
print(resultado)
"""),

md("""
La respuesta es **B**. La multiplicación ocurrió, el resultado se calculó, y nadie lo devolvió.
Python entrega `None` cuando una función termina sin `return`.

**Imprimir en lugar de devolver.** Ya lo viste.

**Llamarla antes de definirla.** Python lee de arriba abajo.
"""),

code("""
# FALLA A PROPÓSITO. La llamada va antes que la definición.
try:
    print(todavia_no_existe(10))
except NameError as e:
    print("NameError:", e)


def todavia_no_existe(x):
    return x * 2
"""),

md("""
En un cuaderno esto muerde distinto: si corres la celda de la definición y **después** una de más
arriba, la función sí existe, porque el estado es el de la última celda que ejecutaste, no el del
orden en pantalla.

Es la misma advertencia de la semana 3, y aquí es donde empieza a costar caro.

**Confiar en variables de fuera.** Ya lo viste con `IVA`.
"""),

md("""
---
# Ejercicios

Las soluciones están hasta abajo del cuaderno.

## Escribir funciones

### Ejercicio 1 · Tres funciones cortas

Escribe tres funciones con docstring, cada una con dos parámetros y un `return`:

1. `porcentaje(parte, total)` que devuelva qué fracción es la parte del total.
2. `variacion(actual, anterior)` que devuelva el cambio porcentual.
3. `con_descuento(precio, porcentaje_descuento)` que devuelva el precio final.

Pruébalas con dos casos cada una.

### Ejercicio 2 · El caso límite de cada una

Para las tres del ejercicio anterior, encuentra el valor de entrada que las rompe y compruébalo.

Pista: piensa qué pasa con un total de cero, con un anterior de cero, y con un descuento del
120 %.

### Ejercicio 3 · Devolver varias cosas

Escribe `estadisticas(numeros)` que reciba una lista y devuelva cuatro valores: la suma, el
promedio, el mayor y el menor. Desempácalos en cuatro nombres al llamarla.

### Ejercicio 4 · Una que usa a otra

Escribe `tabla_amortizacion(capital, tasa_anual, meses)` que use `pago_mensual` y devuelva una
lista de tuplas, una por mes, con el número de mes, el interés de ese mes, el abono a capital y
el saldo restante.

El interés de cada mes es el saldo por la tasa mensual. El abono a capital es el pago menos el
interés.

Comprueba que el saldo del último mes queda prácticamente en cero.

## Ámbito y errores

### Ejercicio 5 · El `None` que revienta después

Escribe a propósito una función sin `return`, guárdala en una variable, y después provoca los
tres errores distintos que ese `None` puede causar: sumarlo, indexarlo y llamar un método suyo.

Anota el mensaje de cada uno.

### Ejercicio 6 · Portátil o no

Esta función depende de algo que no recibe:

```python
COMISION = 0.02

def total_con_comision(monto):
    return monto * (1 + COMISION)
```

Reescríbela para que sea portátil, y demuestra que la primera se rompe borrando la constante y
la segunda no.

### Ejercicio 7 · El nombre repetido

Escribe dos funciones que usen internamente una variable llamada `total` para cosas distintas, y
además una variable `total` fuera de las dos. Imprime las tres y comprueba que ninguna estorba a
las otras.

## Con tu área

### Ejercicio 8 · Empaqueta un cálculo tuyo

Escribe una función que resuelva un cálculo real de tu carrera, con al menos dos parámetros y un
`return`. Escribe su docstring y pruébala con tres casos, incluido uno en el límite.

La función no puede imprimir nada. Solo recibe y devuelve.

La prueba: bórrale una línea al cuerpo. Si las tres pruebas siguen pasando, tus casos no probaban
nada.
"""),

md("""
---
## Tres ideas para llevarse

**Una función se puede probar sola.** Ese es el argumento de verdad. Ahorrar líneas es apenas el
efecto secundario más visible.

**Devolver no es imprimir.** Una función que solo imprime entrega `None`, y ese `None` revienta
tres líneas más abajo con un `TypeError` que no menciona a la función.

**Lo de adentro se queda adentro.** Y por eso puedes reusar los mismos nombres en dos funciones
sin que se estorben, y por eso una función bien escrita no puede romper el resto del programa.

La siguiente sesión son argumentos por omisión, funciones predefinidas y los módulos que ya
vienen con Python.
"""),

md("""
---
# Soluciones

### Ejercicio 1

```python
def porcentaje(parte, total):
    \"\"\"Qué fracción del total representa la parte, como decimal.\"\"\"
    return parte / total


def variacion(actual, anterior):
    \"\"\"El cambio porcentual respecto al periodo anterior, como decimal.\"\"\"
    return (actual - anterior) / anterior


def con_descuento(precio, porcentaje_descuento):
    \"\"\"El precio final después de aplicar un descuento dado como decimal.\"\"\"
    return precio * (1 - porcentaje_descuento)


print(f"{porcentaje(5074, 148230):.2%}")
print(f"{variacion(148230, 96400):+.1%}")
print(f"{con_descuento(8990, 0.15):,.2f}")
```

Nota el `+` en `{:+.1%}`: fuerza el signo, así que un crecimiento se lee `+53.8%` y una caída
`-12.0%`. En un reporte de variación eso vale más que el número solo.

### Ejercicio 2

```python
for f, args, etiqueta in [(porcentaje, (5074, 0), "total de cero"),
                          (variacion, (100, 0), "anterior de cero"),
                          (con_descuento, (8990, 1.2), "descuento del 120 %")]:
    try:
        print(f"{etiqueta:<22} -> {f(*args)}")
    except ZeroDivisionError as e:
        print(f"{etiqueta:<22} -> ZeroDivisionError: {e}")
```

Las dos primeras truenan y la tercera no: devuelve un precio negativo, `-1798.0`.

Esa es la peligrosa. Un error que truena te avisa; uno que devuelve un precio negativo se va a la
factura. Si la función va a usarse de verdad, ahí hace falta una validación.

### Ejercicio 3

```python
def estadisticas(numeros):
    \"\"\"Devuelve suma, promedio, mayor y menor de una lista de números.\"\"\"
    return sum(numeros), sum(numeros) / len(numeros), max(numeros), min(numeros)


suma, promedio, mayor, menor = estadisticas([23200, 42800, 82700, 24500, 24500])

print(f"Suma:     {suma:>10,}")
print(f"Promedio: {promedio:>10,.2f}")
print(f"Mayor:    {mayor:>10,}")
print(f"Menor:    {menor:>10,}")
```

Con una lista vacía truena en la división. Vale la pena decidir si eso está bien: para una
función de estadísticas, probablemente sí, porque el promedio de nada no existe.

### Ejercicio 4

```python
def tabla_amortizacion(capital, tasa_anual, meses):
    \"\"\"Una tupla por mes: número, interés, abono a capital y saldo.\"\"\"
    pago = pago_mensual(capital, tasa_anual, meses)
    i = tasa_anual / 12
    saldo = capital
    filas = []
    for mes in range(1, meses + 1):
        interes = saldo * i
        abono = pago - interes
        saldo -= abono
        filas.append((mes, interes, abono, saldo))
    return filas


tabla = tabla_amortizacion(250000, 0.18, 36)

print(f"{'Mes':>4}{'Interés':>12}{'Abono':>12}{'Saldo':>14}")
for mes, interes, abono, saldo in tabla[:3]:
    print(f"{mes:>4}{interes:>12,.2f}{abono:>12,.2f}{saldo:>14,.2f}")
print("  ...")
for mes, interes, abono, saldo in tabla[-2:]:
    print(f"{mes:>4}{interes:>12,.2f}{abono:>12,.2f}{saldo:>14,.2f}")

print(f"\\nSaldo final: {tabla[-1][3]:.10f}")
```

El saldo final queda en algo como `0.0000000005`, no en cero exacto. Es el mismo redondeo binario
de la semana 4: cada mes arrastra una fracción de centavo.

En un sistema real el último pago se ajusta para cerrar exacto, y eso es una decisión de negocio,
no un error de la fórmula.

### Ejercicio 5

```python
def sin_return(x):
    x * 2


vacio = sin_return(21)

for etiqueta, accion in [("sumarlo", lambda: vacio + 1),
                         ("indexarlo", lambda: vacio[0]),
                         ("llamar un método", lambda: vacio.upper())]:
    try:
        accion()
    except TypeError as e:
        print(f"{etiqueta:<18} TypeError: {e}")
    except AttributeError as e:
        print(f"{etiqueta:<18} AttributeError: {e}")
```

Los tres mencionan `NoneType` y ninguno menciona `sin_return`. Por eso reconocer la palabra
`NoneType` en un mensaje vale tanto: es la pista de que el problema está en una función que no
devolvió, y no en la línea que truena.

### Ejercicio 6

```python
def total_con_comision_portatil(monto, comision=0.02):
    \"\"\"Todo lo que necesita entra como parámetro.\"\"\"
    return monto * (1 + comision)


print(total_con_comision_portatil(1000))
print(total_con_comision_portatil(1000, 0.05))

def total_con_comision(monto):
    return monto * (1 + COMISION_QUE_NO_DEFINI)

try:
    total_con_comision(1000)
except NameError as e:
    print("La primera versión:", e)
```

La portátil funciona sola y además ganó flexibilidad: la comisión ahora se puede cambiar por
llamada sin tocar la función. Ese es el patrón, y la semana 11 lo formaliza.

### Ejercicio 7

```python
total = "el de afuera"

def suma_precios(precios):
    total = sum(precios)
    return total

def cuenta_items(items):
    total = len(items)
    return total

print(suma_precios([100, 200, 300]))
print(cuenta_items(["a", "b", "c", "d"]))
print(total)
```

Sale 600, 4 y `el de afuera`. Tres variables con el mismo nombre y ninguna sabe de las otras.

Que el de afuera sea texto y los de adentro números es a propósito: si se estorbaran, algo habría
tronado.

### Ejercicio 8

No hay solución publicada porque el cálculo es distinto para cada quien. Se califica sobre cuatro
cosas: que tenga docstring, que no imprima nada, que las tres pruebas incluyan un caso límite, y
que borrarle una línea al cuerpo haga fallar al menos una prueba.

Esa última es la que de verdad mide. Una prueba que sigue pasando con la función rota no estaba
probando nada.
"""),

]

write(OUT / "es" / "w10.ipynb", es)
print("wrote", OUT / "es" / "w10.ipynb")


en = [

md("""
# Data Analysis · Week 10
## User-defined functions

**TIA502 · School of Business · Instructor David Escobar-Castillejos**

You already use `AVERAGE` in a sheet without knowing how it adds or divides. Today you learn to
build your own.

The convincing argument is not "reusing code". It is that **a function can be tested on its
own**, and a formula pasted into three hundred cells cannot.

By the end of this notebook you will be able to:

1. Explain what a function solves, beyond saving lines.
2. Define a function with `def`, with a name, parameters and a body.
3. Tell a parameter from an argument.
4. Return a value with `return`, and say how that differs from printing it.
5. Recognise a name's scope and why what is inside does not come out.

### How to use this notebook

Run the cells in order. Five fail on purpose and carry a comment saying so.

The case from here to week 13 is a finance one: the monthly payment on a loan.
"""),

md("""
---
# Block 1 · Why functions exist

Not to write less. To have **one single place** where the calculation can be right or wrong.

Here is the same calculation repeated by hand, for two loans:
"""),

code("""
# Loan A
i = 0.18 / 12
payment_a = 250000 * (i * (1 + i) ** 36) / ((1 + i) ** 36 - 1)

# Loan B
i = 0.24 / 12
payment_b = 120000 * (i * (1 + i) ** 24) / ((1 + i) ** 24 - 1)

print(f"A: {payment_a:,.2f}")
print(f"B: {payment_b:,.2f}")
"""),

md("""
It works, and it has two problems that do not show when you read it.

The formula is written twice, so if it is wrong every copy has to be found and fixed. And the
variable `i` was reused: the second line wrote over the first, and if somebody moves the blocks
around the result changes without warning.

The same arithmetic, packaged:
"""),

code("""
def monthly_payment(principal, annual_rate, months):
    i = annual_rate / 12
    factor = (1 + i) ** months
    return principal * (i * factor) / (factor - 1)


payment_a = monthly_payment(250000, 0.18, 36)
payment_b = monthly_payment(120000, 0.24, 24)

print(f"A: {payment_a:,.2f}")
print(f"B: {payment_b:,.2f}")
"""),

md("""
The same two numbers. The difference is what happens when the formula is wrong: above, every copy
has to be fixed; below, it gets fixed once and both calls come out right.

## The real argument

A function **can be tested on its own**. A formula pasted into three hundred cells can only be
checked cell by cell, and nobody does that.

Testing means this: you give it inputs whose answer you already know and check that it returns
them.
"""),

code("""
# A loan of 12,000 at 0.0000001 % a year over 12 months should pay almost 1,000 a
# month, because there is practically no interest.
print("Practically interest-free:", round(monthly_payment(12000, 0.0000001, 12), 2))

# And the payment always has to exceed principal over months, because interest exists.
print("Payment:", round(monthly_payment(250000, 0.18, 36), 2))
print("Principal over months:", round(250000 / 36, 2))
print("Is the payment larger?", monthly_payment(250000, 0.18, 36) > 250000 / 36)
"""),

md("""
Those three checks fit in one cell and can be rerun every time somebody touches the formula. That
is what the spreadsheet does not give you.
"""),

md("""
---
# Block 2 · How a function is written

Five parts, and each has a rule that is not negotiable.

| Part | What it is | In the example |
|---|---|---|
| `def` | The word that declares it | `def` |
| Name | What it gets called afterwards | `monthly_payment` |
| Parameters | The slots to be filled | `principal, annual_rate, months` |
| Body | The calculation, indented | The three lines inside |
| `return` | What it hands back when it ends | The computed payment |
"""),

code("""
def monthly_payment(principal, annual_rate, months):
    \"\"\"Work out the fixed monthly payment on a loan.

    principal    what is lent, in pesos
    annual_rate  the nominal annual rate, as a decimal: 0.18 is 18 %
    months       the term
    \"\"\"
    i = annual_rate / 12
    factor = (1 + i) ** months

    return principal * (i * factor) / (factor - 1)


payment = monthly_payment(250000, 0.18, 36)
print(f"Monthly payment: ${payment:,.2f}")
"""),

md("""
**`def` and the name.** The name says what it returns, not what it does inside.
`monthly_payment`, not `calculate_stuff`.

**The parameters.** The three slots the function needs. Calling it fills them in that same order.

**The docstring**, that triple-quoted string. It explains what the function is for, and whoever
uses it reads that instead of the body. Python keeps it and it can be looked up.
"""),

code("""
print(monthly_payment.__doc__)
"""),

code("""
help(monthly_payment)
"""),

md("""
**`return`** hands the result back and ends the function right there. Whatever follows does not
run.
"""),

code("""
def with_dead_code(amount):
    return amount * 1.16
    print("This line never executes")


print(with_dead_code(1000))
print("And no message from inside appeared.")
"""),

md("""
## A parameter is not an argument

They get confused constantly and the distinction is simple.

**The parameter** is the slot you leave when defining it: `principal`, `annual_rate`, `months`.

**The argument** is the value that arrives when calling it: `250000`, `0.18`, `36`.

The parameter lives in the definition and the argument in the call. One is the drawer's label,
the other is what you put in.
"""),

code("""
def describe_loan(principal, annual_rate, months):
    \"\"\"The parameters are principal, annual_rate and months.\"\"\"
    return f"{principal:,} pesos at {annual_rate:.0%} over {months} months"


# Here the arguments are 250000, 0.18 and 36.
print(describe_loan(250000, 0.18, 36))

# And they can be passed by name, in any order.
print(describe_loan(months=24, principal=120000, annual_rate=0.24))
"""),

md("""
Passing them by name costs more letters and removes all doubt. With three bare numbers, nobody
reading `monthly_payment(250000, 0.18, 36)` can swear which is which without going to look at the
definition.
"""),

code("""
# FAILS ON PURPOSE, two different ways depending on which two you swap.
import itertools

for order in itertools.permutations([250000, 0.18, 36]):
    label = f"{order[0]:>10,} {order[1]:>10,} {order[2]:>10,}"
    try:
        print(f"{label} -> {monthly_payment(*order):>18,.2f}")
    except OverflowError as e:
        print(f"{label} -> OverflowError: {e}")
"""),

md("""
Six possible orders and three outcomes.

One is right, 9,038.10. Two blow up with `OverflowError`, because raising 1.015 to the two
hundred and fifty thousandth runs past what fits in a decimal. And **three return a number
without protest.**

The worst of the three is `monthly_payment(0.18, 250000, 36)`, which gives 3,750.00. That is a
perfectly believable monthly payment for a loan, and it was computed with the principal sitting
where the rate belongs.

The ones that blow up warn you. The 3,750 goes into the report.
"""),

code("""
# Which is why passing by name pays off when there are several of the same type.
print(monthly_payment(principal=250000, annual_rate=0.18, months=36))

# And that way the order you write them in stops mattering.
print(monthly_payment(months=36, principal=250000, annual_rate=0.18))
"""),

md("""
## Reused
"""),

code("""
loans = [
    (250000, 0.18, 36),
    (120000, 0.24, 24),
    (80000, 0.15, 12),
]

print(f"{'Principal':>10}{'Rate':>7}{'Months':>8}{'Payment':>12}")
print("-" * 37)
for principal, rate, months in loans:
    print(f"{principal:>10,}{rate:>7.0%}{months:>8}"
          f"{monthly_payment(principal, rate, months):>12,.2f}")
"""),

md("""
Three loans, one formula. Add a fourth to the list and the loop is untouched.

## Returning is not printing

This is the error that turns up most in the first assignment with functions.
"""),

code("""
# FAILS ON PURPOSE. The function prints instead of returning.
def payment_that_prints(principal, annual_rate, months):
    i = annual_rate / 12
    factor = (1 + i) ** months
    print(principal * (i * factor) / (factor - 1))


total = payment_that_prints(250000, 0.18, 36)

print("What ended up in total:", total)
print("Its type:", type(total))
"""),

md("""
The number appeared on screen and `total` came back as `None`. A function that only prints is a
dead end: it cannot be added, stored or plotted.

And the `None` does not blow up there. It blows up three lines later.
"""),

code("""
# FAILS ON PURPOSE. The None from above, used as if it were a number.
try:
    print(total * 36)
except TypeError as e:
    print("TypeError:", e)
"""),

md("""
That is the pattern to recognise: **a `TypeError` mentioning `NoneType` almost always means a
function is missing its `return`.**

The rule: the function returns, and whoever calls it decides whether to print.
"""),

code("""
def payment_that_returns(principal, annual_rate, months):
    i = annual_rate / 12
    factor = (1 + i) ** months
    return principal * (i * factor) / (factor - 1)


total = payment_that_returns(250000, 0.18, 36)

print("The payment:", round(total, 2))
print("Over 36 months:", round(total * 36, 2))
print("Interest:", round(total * 36 - 250000, 2))
"""),

md("""
The same calculation, and now the result is good for three more things.

## A function that uses another

With the one above, the function that reports the whole loan can be written without repeating the
formula.
"""),

code("""
def loan_summary(principal, annual_rate, months):
    \"\"\"Returns the monthly payment, the total paid and the interest.\"\"\"
    payment = monthly_payment(principal, annual_rate, months)
    total = payment * months
    return payment, total, total - principal


payment, total, interest = loan_summary(250000, 0.18, 36)

print(f"Monthly payment: {payment:>12,.2f}")
print(f"Total paid:      {total:>12,.2f}")
print(f"Interest:        {interest:>12,.2f}")
print(f"Interest is {interest / 250000:.1%} of the principal")
"""),

md("""
`return payment, total, total - principal` hands back three things at once, packed into a tuple.
The line receiving it unpacks them into three names.

And notice what is **not** there: `loan_summary` does not rewrite the payment formula. It asks for
it. If tomorrow you find the formula was wrong, you fix it in one place and both functions come
out right.
"""),

md("""
---
# Block 3 · Where each name lives

What gets declared inside a function exists only while that function runs.
"""),

code("""
def compute(principal):
    fee = principal * 0.02
    return principal + fee


print(compute(250000))

# FAILS ON PURPOSE. fee was born and died inside the function.
try:
    print(fee)
except NameError as e:
    print("NameError:", e)
"""),

md("""
Variables born inside a function belong to it. They are created when you call it and disappear
when it ends.

That is not a limitation, it is the guarantee that a function cannot break the rest of the
program by accident. And it brings a good consequence: **you can reuse the same name without
worry.**
"""),

code("""
def one(x):
    factor = x * 2
    return factor


def another(x):
    factor = x * 100      # the same name, and they do not collide
    return factor


print(one(5), another(5))
"""),

md("""
One function's `factor` and the other's are two different variables that will never meet.

## What can be seen from inside

A function can **read** a name from outside. That works and is nearly always a bad idea.
"""),

code("""
TAX = 0.16                    # a constant of the program

def with_tax(amount):
    return amount * (1 + TAX)  # reads TAX from outside


print(with_tax(1000))
"""),

md("""
It works because `TAX` is defined when the function runs. The problem shows up when the function
moves to another file: it takes its body and leaves `TAX` behind.
"""),

code("""
# FAILS ON PURPOSE. The same function, without the constant it took for granted.
def with_duty(amount):
    return amount * (1 + RATE_THAT_DOES_NOT_EXIST)


try:
    print(with_duty(1000))
except NameError as e:
    print("NameError:", e)
"""),

md("""
The version that survives the move receives everything it needs.
"""),

code("""
def with_tax_portable(amount, tax=0.16):
    \"\"\"Everything it needs comes in through the door.\"\"\"
    return amount * (1 + tax)


print(with_tax_portable(1000))
print(with_tax_portable(1000, 0.08))      # border zone
"""),

md("""
That `tax=0.16` is a default argument, and it is next week's topic. It appears here so you can see
the solution exists.

## Modifying from inside

Reading from outside works. Assigning does not.
"""),

code("""
counter = 0

def add_one():
    counter = 1     # this creates a NEW, local variable
    return counter


print("Returns:", add_one())
print("And the outer one is still:", counter)
"""),

md("""
The inner one and the outer one share a name and are not the same. The assignment created a local
that died when the function ended.

There is a word to force the opposite, `global`, and this course does not use it. A function that
modifies outside variables is exactly the one that cannot be tested on its own, which is all we
are trying to avoid.

## Four errors on your first function

**Forgetting the `return`.** The function runs, computes correctly and returns `None`. The error
appears lines later.

**Predict before you run.** What does this program print?

- **A.** 42, because it multiplies by two.
- **B.** `None`, because the function is missing its `return`.
- **C.** 21, because `n` did not change.
- **D.** An error, because the function does nothing.
"""),

code("""
def double(n):
    n * 2


result = double(21)
print(result)
"""),

md("""
The answer is **B**. The multiplication happened, the result was computed, and nobody returned it.
Python hands back `None` when a function ends without a `return`.

**Printing instead of returning.** You saw it.

**Calling it before defining it.** Python reads top to bottom.
"""),

code("""
# FAILS ON PURPOSE. The call comes before the definition.
try:
    print(not_yet_defined(10))
except NameError as e:
    print("NameError:", e)


def not_yet_defined(x):
    return x * 2
"""),

md("""
In a notebook this bites differently: if you run the definition cell and **then** one further up,
the function does exist, because the state is whatever the last cell you executed left behind, not
the order on screen.

It is the same warning from week 3, and this is where it starts costing.

**Relying on outside variables.** You saw it with `TAX`.
"""),

md("""
---
# Exercises

The solutions sit at the very bottom of the notebook.

## Writing functions

### Exercise 1 · Three short functions

Write three functions with docstrings, each with two parameters and a `return`:

1. `share(part, total)` returning what fraction of the total the part is.
2. `change(current, previous)` returning the percentage change.
3. `discounted(price, discount)` returning the final price.

Test each with two cases.

### Exercise 2 · Each one's edge case

For all three, find the input value that breaks them and prove it.

Hint: think about a total of zero, a previous of zero, and a discount of 120 %.

### Exercise 3 · Returning several things

Write `statistics_of(numbers)` taking a list and returning four values: the sum, the average, the
largest and the smallest. Unpack them into four names when calling it.

### Exercise 4 · One that uses another

Write `amortisation(principal, annual_rate, months)` that uses `monthly_payment` and returns a
list of tuples, one per month, with the month number, that month's interest, the principal repaid
and the remaining balance.

Each month's interest is the balance times the monthly rate. The principal repaid is the payment
minus the interest.

Check that the last month's balance ends up practically at zero.

## Scope and errors

### Exercise 5 · The `None` that blows up later

Deliberately write a function with no `return`, store it in a variable, then provoke the three
different errors that `None` can cause: adding it, indexing it and calling a method on it.

Write down each message.

### Exercise 6 · Portable or not

This function depends on something it does not receive:

```python
FEE = 0.02

def total_with_fee(amount):
    return amount * (1 + FEE)
```

Rewrite it to be portable, and show that the first breaks when the constant is deleted and the
second does not.

### Exercise 7 · The repeated name

Write two functions that internally use a variable called `total` for different things, plus a
`total` outside both. Print all three and check that none interferes with the others.

## With your own field

### Exercise 8 · Package a calculation of your own

Write a function that solves a real calculation from your field, with at least two parameters and
a `return`. Write its docstring and test it with three cases, one of them at the boundary.

The function may not print anything. It only receives and returns.

The test: delete a line from the body. If all three tests still pass, your cases were not testing
anything.
"""),

md("""
---
## Three ideas to take away

**A function can be tested on its own.** That is the real argument. Saving lines is only the most
visible side effect.

**Returning is not printing.** A function that only prints hands back `None`, and that `None`
blows up three lines later with a `TypeError` that never mentions the function.

**What is inside stays inside.** Which is why you can reuse the same names in two functions
without collision, and why a well-written function cannot break the rest of the program.

Next session is default arguments, built-in functions and the modules that already ship with
Python.
"""),

md("""
---
# Solutions

### Exercise 1

```python
def share(part, total):
    \"\"\"What fraction of the total the part represents, as a decimal.\"\"\"
    return part / total


def change(current, previous):
    \"\"\"The percentage change against the previous period, as a decimal.\"\"\"
    return (current - previous) / previous


def discounted(price, discount):
    \"\"\"The final price after applying a discount given as a decimal.\"\"\"
    return price * (1 - discount)


print(f"{share(5074, 148230):.2%}")
print(f"{change(148230, 96400):+.1%}")
print(f"{discounted(8990, 0.15):,.2f}")
```

Note the `+` in `{:+.1%}`: it forces the sign, so growth reads `+53.8%` and a fall reads `-12.0%`.
In a variance report that is worth more than the number alone.

### Exercise 2

```python
for f, args, label in [(share, (5074, 0), "total of zero"),
                       (change, (100, 0), "previous of zero"),
                       (discounted, (8990, 1.2), "discount of 120 %")]:
    try:
        print(f"{label:<20} -> {f(*args)}")
    except ZeroDivisionError as e:
        print(f"{label:<20} -> ZeroDivisionError: {e}")
```

The first two blow up and the third does not: it returns a negative price, `-1798.0`.

That is the dangerous one. An error that blows up warns you; one that returns a negative price
goes onto the invoice. If the function is going to be used for real, that is where a validation
belongs.

### Exercise 3

```python
def statistics_of(numbers):
    \"\"\"Returns sum, average, largest and smallest of a list of numbers.\"\"\"
    return sum(numbers), sum(numbers) / len(numbers), max(numbers), min(numbers)


total, average, largest, smallest = statistics_of([23200, 42800, 82700, 24500, 24500])

print(f"Sum:      {total:>10,}")
print(f"Average:  {average:>10,.2f}")
print(f"Largest:  {largest:>10,}")
print(f"Smallest: {smallest:>10,}")
```

With an empty list it blows up on the division. Worth deciding whether that is right: for a
statistics function it probably is, because the average of nothing does not exist.

### Exercise 4

```python
def amortisation(principal, annual_rate, months):
    \"\"\"One tuple per month: number, interest, principal repaid and balance.\"\"\"
    payment = monthly_payment(principal, annual_rate, months)
    i = annual_rate / 12
    balance = principal
    rows = []
    for month in range(1, months + 1):
        interest = balance * i
        repaid = payment - interest
        balance -= repaid
        rows.append((month, interest, repaid, balance))
    return rows


table = amortisation(250000, 0.18, 36)

print(f"{'Month':>6}{'Interest':>12}{'Repaid':>12}{'Balance':>14}")
for month, interest, repaid, balance in table[:3]:
    print(f"{month:>6}{interest:>12,.2f}{repaid:>12,.2f}{balance:>14,.2f}")
print("  ...")
for month, interest, repaid, balance in table[-2:]:
    print(f"{month:>6}{interest:>12,.2f}{repaid:>12,.2f}{balance:>14,.2f}")

print(f"\\nFinal balance: {table[-1][3]:.10f}")
```

The final balance lands on something like `0.0000000005`, not exactly zero. It is the same binary
rounding from week 4: every month drags a fraction of a cent along.

In a real system the last payment is adjusted to close exactly, and that is a business decision,
not a flaw in the formula.

### Exercise 5

```python
def no_return(x):
    x * 2


empty = no_return(21)

for label, action in [("adding it", lambda: empty + 1),
                      ("indexing it", lambda: empty[0]),
                      ("calling a method", lambda: empty.upper())]:
    try:
        action()
    except TypeError as e:
        print(f"{label:<18} TypeError: {e}")
    except AttributeError as e:
        print(f"{label:<18} AttributeError: {e}")
```

All three mention `NoneType` and none mentions `no_return`. That is why recognising the word
`NoneType` in a message is worth so much: it is the clue that the problem sits in a function that
did not return, not in the line that blew up.

### Exercise 6

```python
def total_with_fee_portable(amount, fee=0.02):
    \"\"\"Everything it needs arrives as a parameter.\"\"\"
    return amount * (1 + fee)


print(total_with_fee_portable(1000))
print(total_with_fee_portable(1000, 0.05))

def total_with_fee(amount):
    return amount * (1 + FEE_I_NEVER_DEFINED)

try:
    total_with_fee(1000)
except NameError as e:
    print("The first version:", e)
```

The portable one works on its own and gained flexibility besides: the fee can now be changed per
call without touching the function. That is the pattern, and week 11 formalises it.

### Exercise 7

```python
total = "the outer one"

def sum_prices(prices):
    total = sum(prices)
    return total

def count_items(items):
    total = len(items)
    return total

print(sum_prices([100, 200, 300]))
print(count_items(["a", "b", "c", "d"]))
print(total)
```

You get 600, 4 and `the outer one`. Three variables sharing a name and none of them knows about
the others.

That the outer one is text and the inner ones are numbers is deliberate: if they collided,
something would have blown up.

### Exercise 8

There is no published solution, because the calculation differs for everyone. It is graded on four
things: that it has a docstring, that it prints nothing, that the three tests include an edge
case, and that deleting a line from the body makes at least one test fail.

That last one is what really measures. A test that still passes with the function broken was not
testing anything.
"""),

]

write(OUT / "en" / "w10.ipynb", en)
print("wrote", OUT / "en" / "w10.ipynb")
