"""notebooks/analisis-de-datos/{es,en}/w11.ipynb

Source deck: ppts/python/analisis-de-datos/{es,en}/w11.*.yaml
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from nbkit import md, code, write, REPO

OUT = REPO / "notebooks" / "analisis-de-datos"

es = [

md("""
# Análisis de Datos · Semana 11
## Argumentos, funciones predefinidas y módulos

**TIA502 · Facultad de Empresariales · Profesor David Escobar-Castillejos**

Los argumentos por omisión y por nombre son lo que hace legible una llamada con cinco
parámetros, y eso lo vas a ver todo el semestre en pandas y en matplotlib.

Y los módulos son la puerta a la semana 15. Cuando entiendas que `import` trae herramientas de
fuera, importar pandas deja de ser magia.

Al terminar este cuaderno vas a poder:

1. Pasar argumentos por nombre, para que una llamada con cinco valores se lea sin contar
   posiciones.
2. Definir valores por omisión, y explicar por qué los opcionales van siempre al final.
3. Usar `len`, `sum`, `max`, `min`, `round` y `sorted` sin escribirlas a mano.
4. Importar un módulo con las dos formas de `import`.
5. Leer la documentación oficial y encontrar ahí qué recibe y qué devuelve una función.

### Cómo se usa este cuaderno

Ejecuta las celdas en orden. Cinco fallan a propósito y llevan un comentario que lo dice.
"""),

md("""
---
# Bloque 1 · Cómo se pasan los argumentos

Tres formas, y la diferencia se nota cuando la función tiene más de tres parámetros.

| Forma | Cómo se ve | Cuándo conviene |
|---|---|---|
| Por posición | `f(250000, 0.18, 36)` | Dos o tres valores obvios |
| Por nombre | `f(capital=250000, meses=36)` | Cuando hay muchos o son ambiguos |
| Por omisión | `def f(seguro=0.0)` | Lo que casi siempre vale lo mismo |
"""),

code("""
def pago_mensual(capital, tasa_anual, meses, comision=0.0, seguro=0.0):
    \"\"\"Pago mensual de un crédito, con costos opcionales.

    comision  como decimal sobre el capital, repartida en todo el plazo
    seguro    una cantidad fija que se suma cada mes
    \"\"\"
    i = tasa_anual / 12
    factor = (1 + i) ** meses
    base = capital * (i * factor) / (factor - 1)

    return base + capital * comision / meses + seguro


print(pago_mensual(250000, 0.18, 36))
print(pago_mensual(250000, 0.18, 36, seguro=350))
"""),

md("""
**Los obligatorios.** Los tres primeros no tienen valor por omisión, así que hay que darlos
siempre.

**Los opcionales.** `comision` y `seguro` valen cero si no los mencionas, y por eso la llamada
corta sigue dando exactamente el mismo número que la semana pasada.

**Por nombre.** La segunda llamada se salta `comision` y nombra `seguro`. Sin nombrarlo tendría
que pasar los dos.
"""),

code("""
# Las cuatro combinaciones, para ver qué cambia cada opcional.
print(f"Sin nada:            {pago_mensual(250000, 0.18, 36):>10,.2f}")
print(f"Con seguro:          {pago_mensual(250000, 0.18, 36, seguro=350):>10,.2f}")
print(f"Con comisión del 3%: {pago_mensual(250000, 0.18, 36, comision=0.03):>10,.2f}")
print(f"Con las dos:         {pago_mensual(250000, 0.18, 36, 0.03, 350):>10,.2f}")
"""),

md("""
## Por qué lo opcional va al final

No es estilo. Python lo rechaza al leer el archivo.
"""),

code("""
# FALLA A PROPÓSITO. Un parámetro con valor por omisión antes de uno sin él.
try:
    compile("def f(iva=0.16, base):\\n    return base", "<ejemplo>", "exec")
except SyntaxError as e:
    print(f"SyntaxError: {e.msg}")
"""),

md("""
La razón es sencilla: si `iva` tuviera valor por omisión y `base` no, entonces `f(1000)` sería
ambiguo. ¿El 1000 es la base, o es el iva y falta la base?

Python prefiere no adivinar.

## Saltarse un parámetro sin nombrarlo

**Predice antes de correr.** ¿Qué imprime la segunda llamada?

- **A.** 1160.0 y 1210.0
- **B.** 1160.0 y 51000
- **C.** 1160.0 y un error, faltan argumentos
- **D.** 1160.0 y 1050.0
"""),

code("""
def total(base, iva=0.16, envio=0):
    return base * (1 + iva) + envio


print(total(1000))
print(total(1000, 50))
"""),

md("""
La respuesta es **B**, 51000.

El 50 cayó en `iva`, porque es el siguiente por posición. La función calculó `1000 * 51` y
devolvió un total cincuenta veces más grande, sin protestar.

Quien escribió esa línea quería 50 pesos de envío.
"""),

code("""
# Lo que quería, dicho por nombre.
print("Con envío de 50:", total(1000, envio=50))

# Y por posición, pasando el iva aunque no quisiera tocarlo.
print("Con las dos posiciones:", total(1000, 0.16, 50))
"""),

md("""
Esa es la regla práctica: **en cuanto te saltas un parámetro, nombra los que sigan.**

## Cuándo nombrar y cuándo no

Nombrar todo es ruido. No nombrar nada es adivinanza. La línea que la mayoría traza:
"""),

code("""
# Dos argumentos obvios: por posición se lee bien.
print(round(9038.098883979254, 2))

# Cinco argumentos de los cuales tres son números sueltos: nombrar salva.
print(pago_mensual(capital=250000, tasa_anual=0.18, meses=36,
                   comision=0.03, seguro=350))
"""),

md("""
Lo vas a ver en cada llamada de pandas y de matplotlib del resto del curso:

```python
ventas.pivot_table(index="region", columns="channel", values="amount", aggfunc="sum")
ax.plot(meses, valores, marker="o", linewidth=2, color="#2B5F8F")
```

Ninguna de esas dos pasa nada por posición después del primer par. Ahora sabes por qué.
"""),

md("""
---
# Bloque 2 · Lo que Python ya trae puesto

Media docena de funciones que ya usabas, y que ahora sabes que son funciones como las que
escribes tú.

| Función | Qué devuelve | Ejemplo |
|---|---|---|
| `len` | Cuántos elementos hay | `len(pagos)` |
| `sum` | La suma de todos | `sum(pagos)` |
| `max` | El mayor | `max(pagos)` |
| `min` | El menor | `min(pagos)` |
| `round` | El número redondeado | `round(promedio, 2)` |
| `sorted` | Una copia ordenada | `sorted(pagos)` |
"""),

code("""
pagos = [9038.10, 6344.53, 7220.66, 4180.25, 11902.44]

print("Cuántos:  ", len(pagos))
print("Suma:     ", round(sum(pagos), 2))
print("Mayor:    ", max(pagos))
print("Menor:    ", min(pagos))
print("Ordenados:", sorted(pagos))
"""),

md("""
Fíjate en `sorted`: devuelve **una copia** ordenada y deja la lista original como estaba.
"""),

code("""
print("Original después de sorted:", pagos)
"""),

md("""
Ese comportamiento es el mismo de `sort_values` en pandas, que ya viste en la semana 15.2 si
llegaste ahí primero: casi todo en Python devuelve algo nuevo en lugar de modificar lo que
recibió.

Existe la otra forma, `.sort()`, que sí modifica y no devuelve nada.
"""),

code("""
copia = pagos.copy()
resultado = copia.sort()

print("copia después de .sort():", copia)
print("Lo que devolvió .sort():", resultado)
"""),

md("""
`None`, igual que la función sin `return` de la semana pasada. Es la señal de que ese método
trabaja sobre el original en lugar de entregar algo.

Confundirlas produce este clásico:
"""),

code("""
# FALLA A PROPÓSITO. Guardar el resultado de .sort() en lugar de usar sorted().
mal = pagos.copy().sort()
bien = sorted(pagos)

print("Con .sort():", mal)
print("Con sorted():", bien[:3], "...")
"""),

md("""
## `round` y sus sorpresas

`round` redondea, y con decimales binarios hace cosas que sorprenden.
"""),

code("""
print(round(2.675, 2), "<- no es 2.68")
print(round(0.5), round(1.5), round(2.5), round(3.5), "<- redondeo al par")
"""),

md("""
Lo primero es el mismo problema de la semana 4: `2.675` en binario es un poquito menos que
2.675, así que redondea hacia abajo.

Lo segundo es a propósito: Python redondea al par más cercano cuando la fracción es exactamente
un medio. Con muchos números, eso evita que el redondeo empuje siempre hacia arriba y la suma se
infle.

Para dinero, formatea al imprimir en lugar de redondear el valor. Es lo que vienes haciendo desde
la semana 5.
"""),

md("""
---
# Bloque 3 · Módulos

Python trae cientos de funciones que no carga de entrada, porque cargarlas todas haría lento cada
programa. Están agrupadas por tema en **módulos**, y se traen con `import` cuando hacen falta.

| Módulo | Para qué sirve | Cuándo llega |
|---|---|---|
| `statistics` | Promedio, mediana, moda | Hoy |
| `math` | Raíz, potencias, redondeos | Hoy |
| `datetime` | Fechas y diferencias entre ellas | Semana 14 |
| `csv` | Leer y escribir archivos de datos | Semana 14 |
| `pandas` | Tablas completas, y viene aparte | Semana 15 |

Los cuatro primeros son parte de Python mismo. `pandas` no lo es, pero Colab ya lo trae, así que
los cinco se importan igual y ninguno descarga nada.

## Las dos formas de importar
"""),

code("""
# Forma 1: el módulo entero. Queda claro de dónde salió cada función.
import statistics

print(round(statistics.mean(pagos), 2))
print(statistics.median(pagos))
"""),

code("""
# Forma 2: solo lo que usas. Se escribe menos.
from statistics import mean, median

print(round(mean(pagos), 2))
print(median(pagos))
"""),

md("""
Las dos hacen lo mismo. La primera se prefiere cuando importas de varios módulos, porque
`statistics.mean` y `math.floor` dicen de dónde vienen. La segunda cuando usas una función
muchas veces y el nombre ya es inequívoco.

Y hay una tercera, el alias, que es la que vas a usar con pandas:
"""),

code("""
import statistics as st

print(round(st.mean(pagos), 2))
print("Y en la semana 15 esto va a ser: import pandas as pd")
"""),

md("""
## Promedio y mediana no dicen lo mismo
"""),

code("""
print(f"Promedio: {mean(pagos):>10,.2f}")
print(f"Mediana:  {median(pagos):>10,.2f}")
print(f"Diferencia: {mean(pagos) - median(pagos):>8,.2f}")
"""),

md("""
Quinientos pesos de diferencia sobre cinco créditos. El pago de 11,902 jala el promedio hacia
arriba y la mediana no se mueve, porque a la mediana solo le importa cuál queda a la mitad.

Es la misma lección de los sueldos de la semana 3 y del histograma de la semana 16. Cuando esos
dos números se separan, la separación es el hallazgo.

## Qué más trae `statistics`
"""),

code("""
import statistics

print([n for n in dir(statistics) if not n.startswith("_")])
"""),

md("""
`dir` lista todo lo que un módulo trae. La comprensión de lista filtra los nombres que empiezan
con guión bajo, que son de uso interno.

Esa línea sirve para cualquier módulo, y es la forma más rápida de ver qué hay antes de ir a la
documentación.
"""),

code("""
from statistics import stdev, mode, quantiles

print("Desviación estándar:", round(stdev(pagos), 2))
print("Cuartiles:", [round(q, 2) for q in quantiles(pagos)])

# mode necesita que algo se repita.
try:
    print(mode(pagos))
except statistics.StatisticsError as e:
    print("StatisticsError:", e)
"""),

md("""
Ojo: en versiones recientes `mode` devuelve el primero cuando no hay repetidos, y en otras lanza
error. Si tu salida dice un número en lugar del error, tu versión es de las que devuelven.

Eso también es información: **una función puede cambiar de comportamiento entre versiones**, y por
eso la documentación dice a cuál corresponde.

## `math`
"""),

code("""
import math

print("Raíz de 144:      ", math.sqrt(144))
print("Redondeo abajo:   ", math.floor(9038.98))
print("Redondeo arriba:  ", math.ceil(9038.02))
print("Valor absoluto:   ", abs(-350))
print("Pi:               ", round(math.pi, 4))
"""),

md("""
`abs` no necesitó import: es de las predefinidas. `floor` y `ceil` sí, y son las que sirven para
"cuántos meses completos" y "cuántas cajas hacen falta".
"""),

code("""
piezas = 47
por_caja = 12

print("Cajas completas:", math.floor(piezas / por_caja))
print("Cajas a pedir:  ", math.ceil(piezas / por_caja))
print("Con //:         ", piezas // por_caja, "<- lo mismo que floor, sin importar nada")
"""),

md("""
## Leer la documentación

`help` funciona sobre cualquier función, incluidas las que no escribiste.
"""),

code("""
help(round)
"""),

md("""
Esa primera línea, `round(number, ndigits=None)`, es la firma: dice qué recibe y qué es opcional.
El `ndigits=None` es exactamente lo mismo que los valores por omisión del bloque 1.

La documentación oficial está en `docs.python.org`, y dice lo mismo con más contexto y ejemplos.
Saber leerla es media batalla del proyecto final, porque nadie va a poder enseñarte de memoria
todo lo que trae pandas.

## Cuatro errores de argumentos y módulos

**Poner lo opcional antes de lo obligatorio.** Ya lo viste: `SyntaxError` al leer el archivo.

**Saltarse un parámetro sin nombrarlo.** Ya lo viste: el 50 que cayó en `iva`.

**Importar dentro de una función.** Funciona, y esconde la dependencia.
"""),

code("""
def promedio_escondido(numeros):
    from statistics import mean      # funciona, y nadie que lea el archivo lo espera aquí
    return mean(numeros)


print(promedio_escondido(pagos))
print("Corre bien, y quien lea el archivo no sabe que depende de statistics.")
"""),

md("""
El `import` va hasta arriba, donde quien lea el archivo lo encuentre en tres segundos.

**Nombrar tu archivo como un módulo.** Un archivo llamado `math.py` en tu carpeta hace que
`import math` traiga el tuyo, y el error resultante no tiene sentido.
"""),

code("""
# Demostración segura: creo un módulo falso y le doy prioridad a mano.
import sys, types

falso = types.ModuleType("statistics")
falso.mean = lambda x: "esto no es un promedio"

verdadero = sys.modules["statistics"]
sys.modules["statistics"] = falso

from statistics import mean as mean_falso
print("Con el archivo equivocado:", mean_falso(pagos))

sys.modules["statistics"] = verdadero      # dejo todo como estaba
from statistics import mean
print("Con el de verdad:", round(mean(pagos), 2))
"""),

md("""
En la vida real esto pasa sin que nadie lo provoque: alguien guarda su tarea como `math.py` o
`csv.py` en la misma carpeta, y a partir de ahí el programa hace cosas inexplicables.

La regla: **nunca le pongas a tu archivo el nombre de un módulo.**
"""),

md("""
---
# Ejercicios

Las soluciones están hasta abajo del cuaderno.

## Argumentos

### Ejercicio 1 · Los tres opcionales

Escribe `precio_final(base, iva=0.16, descuento=0.0, envio=0.0)` que aplique el descuento
primero, después el IVA, y sume el envío al final.

Llámala cuatro veces: sin opcionales, con descuento, con envío, y con las tres.

### Ejercicio 2 · El salto sin nombre

Con la función del ejercicio 1, escribe la llamada que **parece** poner 100 de envío y en realidad
lo pone en otro lado. Imprime los dos resultados y explica en un comentario dónde cayó el 100.

### Ejercicio 3 · Legible con cinco

Escribe una función con cinco parámetros, tres de ellos numéricos, y después dos llamadas: una
solo por posición y otra solo por nombre. Léelas en voz alta y di cuál entenderías dentro de seis
meses.

## Predefinidas

### Ejercicio 4 · Las seis sobre tus datos

Con una lista de al menos ocho números de tu área, usa las seis funciones predefinidas de la
tabla e imprime cada resultado con su etiqueta.

Después comprueba que la lista original no quedó ordenada.

### Ejercicio 5 · `sorted` contra `.sort()`

Demuestra con código la diferencia: haz dos copias de la misma lista, ordena una con `sorted` y
la otra con `.sort()`, e imprime las dos listas y los dos valores devueltos.

### Ejercicio 6 · `max` con criterio

Busca en la documentación qué hace el parámetro `key` de `max`. Después úsalo sobre esta lista
para encontrar el crédito con el pago más alto:

```python
CREDITOS = [("A", 250000, 9038.10), ("B", 120000, 6344.53), ("C", 480000, 11902.44)]
```

Pista: `max(CREDITOS, key=...)` recibe una función que dice por cuál valor comparar.

## Módulos

### Ejercicio 7 · Explorar un módulo

Usa `dir` sobre `math` y elige tres funciones que no vimos. Lee su `help` y explica en un
comentario qué recibe y qué devuelve cada una.

### Ejercicio 8 · Una función de `statistics` que no vimos

Busca en `docs.python.org` una función del módulo `statistics` que no apareció en el cuaderno,
explica en tres renglones qué recibe y qué devuelve, y úsala sobre los cinco pagos de la sesión.

### Ejercicio 9 · Tu función, con lo opcional opcional

Toma la función que escribiste la semana pasada y agrégale dos parámetros con valor por omisión,
de forma que la llamada corta siga funcionando igual que antes. Úsala tres veces con distintas
combinaciones.

La tercera llamada tiene que pasar un argumento por nombre saltándose otro.

La prueba: la llamada sin argumentos opcionales tiene que dar exactamente el mismo número que la
semana pasada.
"""),

md("""
---
## Tres ideas para llevarse

**Lo opcional va al final.** Un parámetro con valor por omisión antes de uno sin él es un error
de sintaxis, no una decisión de estilo.

**Nombrar el argumento se lee mejor.** En cuanto la función pasa de tres parámetros, contar
posiciones deja de ser viable, y el 50 que cae en `iva` no lanza ningún error.

**`import` es la puerta a todo.** Lo que hoy trae `statistics` es exactamente lo que en la semana
15 va a traer pandas, con la misma línea y sin instalar nada.

La siguiente sesión son listas y tuplas, que son la columna de tu hoja de cálculo.
"""),

md("""
---
# Soluciones

### Ejercicio 1

```python
def precio_final(base, iva=0.16, descuento=0.0, envio=0.0):
    \"\"\"Precio final: descuento primero, IVA después, envío al final.\"\"\"
    con_descuento = base * (1 - descuento)
    return con_descuento * (1 + iva) + envio


print(f"Sin opcionales: {precio_final(1000):>10,.2f}")
print(f"Con descuento:  {precio_final(1000, descuento=0.10):>10,.2f}")
print(f"Con envío:      {precio_final(1000, envio=150):>10,.2f}")
print(f"Con las tres:   {precio_final(1000, 0.08, 0.10, 150):>10,.2f}")
```

Que el descuento vaya antes del IVA no es un detalle técnico, es una decisión fiscal: el IVA se
calcula sobre el precio ya descontado. Al revés daría un número distinto y estaría mal.

### Ejercicio 2

```python
print("Lo que quería:", precio_final(1000, envio=100))
print("Lo que escribió:", precio_final(1000, 100))

# El 100 cayó en iva, porque es el siguiente parámetro por posición. La función
# calculó 1000 * (1 + 100), o sea 101,000. Es cien veces el precio y no lanzó
# ningún error, porque un iva de 100 es un número perfectamente válido.
```

Cien mil pesos por algo de mil. La escala del error es lo único que lo delata, y en un reporte con
muchas cifras eso no siempre salta.

### Ejercicio 3

```python
def cotizar(cliente, base, iva, descuento, dias_credito):
    return f"{cliente}: {base * (1 - descuento) * (1 + iva):,.2f} a {dias_credito} días"


print(cotizar("Insumos SA", 12000, 0.16, 0.05, 30))
print(cotizar(cliente="Insumos SA", base=12000, iva=0.16,
              descuento=0.05, dias_credito=30))

# Dentro de seis meses entendería la segunda. En la primera, 0.16 y 0.05 son dos
# decimales seguidos y no hay forma de saber cuál es cuál sin abrir la definición.
```

La regla que se saca sola: cuando dos parámetros seguidos son del mismo tipo y podrían
intercambiarse sin que nada truene, nómbralos.

### Ejercicio 4

```python
unidades = [15, 8, 22, 5, 11, 35, 20, 18]

print("Cuántos:  ", len(unidades))
print("Suma:     ", sum(unidades))
print("Mayor:    ", max(unidades))
print("Menor:    ", min(unidades))
print("Promedio: ", round(sum(unidades) / len(unidades), 2))
print("Ordenados:", sorted(unidades))
print("Original: ", unidades)
```

La última línea es la que importa: la lista original sigue en su orden. `sorted` no la tocó.

### Ejercicio 5

```python
a = [15, 8, 22, 5]
b = [15, 8, 22, 5]

devuelve_sorted = sorted(a)
devuelve_sort = b.sort()

print("a después de sorted:", a)
print("sorted devolvió:    ", devuelve_sorted)
print("b después de .sort():", b)
print(".sort() devolvió:   ", devuelve_sort)
```

`sorted` deja `a` intacta y devuelve la ordenada. `.sort()` cambia `b` y devuelve `None`.

La regla de bolsillo de Python: si un método modifica el objeto, devuelve `None`, para que no
puedas encadenarlo por error.

### Ejercicio 6

```python
CREDITOS = [("A", 250000, 9038.10), ("B", 120000, 6344.53), ("C", 480000, 11902.44)]

mayor_pago = max(CREDITOS, key=lambda c: c[2])
mayor_capital = max(CREDITOS, key=lambda c: c[1])

print("Pago más alto:   ", mayor_pago)
print("Capital más alto:", mayor_capital)
print("Sin key:         ", max(CREDITOS), "<- compara por el primer elemento, la letra")
```

`key` recibe una función que dice por cuál valor comparar. Sin ella, `max` compara las tuplas
completas empezando por el primer elemento, que aquí es la letra, y devuelve la C por orden
alfabético. Que coincida con la respuesta correcta es casualidad.

Ese `lambda` es una función sin nombre escrita en una línea. Hace exactamente lo mismo que un
`def` de dos líneas y se usa cuando la función es tan corta que ponerle nombre estorba.

### Ejercicio 7

```python
import math

for nombre in ["trunc", "hypot", "log10"]:
    print("=" * 50)
    help(getattr(math, nombre))

# trunc  recibe un número y devuelve su parte entera, cortando hacia cero.
#        Con negativos difiere de floor: trunc(-2.7) da -2 y floor(-2.7) da -3.
# hypot  recibe dos o más números y devuelve la raíz de la suma de sus cuadrados.
#        Es la distancia en línea recta, y sirve para comparar dos métricas a la vez.
# log10  recibe un número positivo y devuelve su logaritmo base diez. Sirve para
#        comparar cantidades que difieren en órdenes de magnitud.
```

`getattr(math, nombre)` saca una función de un módulo por su nombre en texto. Es lo que permite
recorrer una lista de nombres en un ciclo en lugar de escribir tres `help` a mano.

### Ejercicio 8

```python
from statistics import fmean, pstdev

print("fmean:", round(fmean(pagos), 2))
print("pstdev:", round(pstdev(pagos), 2))
print("stdev: ", round(stdev(pagos), 2))

# fmean recibe una lista de números y devuelve su promedio como float, igual que
# mean pero más rápido porque no intenta conservar tipos exactos.
# pstdev recibe una lista y devuelve la desviación estándar de la POBLACIÓN,
# dividiendo entre n. stdev divide entre n-1 porque supone que la lista es una
# muestra de algo más grande. Cuál usar depende de si tus cinco créditos son todos
# los que existen o una muestra de una cartera mayor.
```

Esa distinción entre población y muestra es de las que un curso de estadística cubre y un curso de
programación suele saltarse. Aquí importa porque elegir la función equivocada cambia el número y
ninguna de las dos lanza error.

### Ejercicio 9

No hay solución publicada porque la función es distinta para cada quien. Se califica sobre tres
cosas: que la llamada corta dé exactamente el mismo resultado que la versión de la semana pasada,
que los dos parámetros nuevos tengan valor por omisión y estén al final, y que la tercera llamada
se salte uno nombrando el siguiente.
"""),

]

write(OUT / "es" / "w11.ipynb", es)
print("wrote", OUT / "es" / "w11.ipynb")
