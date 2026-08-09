"""notebooks/analisis-de-datos/es/w12.ipynb

Source deck: ppts/python/analisis-de-datos/es/w12.es.yaml
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from nbkit import md, code, write, REPO

OUT = REPO / "notebooks" / "analisis-de-datos"

es = [

md("""
# Análisis de Datos · Semana 12
## Listas y tuplas

**TIA502 · Facultad de Empresariales · Profesor David Escobar-Castillejos**

Una lista es una columna. Vale la pena decirlo temprano y sostenerlo, porque en la semana 15 una
`Series` de pandas es exactamente esto con un índice encima.

Al terminar este cuaderno vas a poder:

1. Crear y recorrer una lista, con índices que empiezan en cero y también cuentan hacia atrás.
2. Cortar una rebanada, y explicar por qué el segundo índice no entra.
3. Usar los once métodos de lista, distinguiendo los que modifican de los que consultan.
4. Distinguir lista de tupla, y decir cuándo conviene cada una.
5. Reconocer un alias, y hacer una copia de verdad.

### Cómo se usa este cuaderno

Ejecuta las celdas en orden. Seis fallan a propósito y llevan un comentario que lo dice.

Lo del alias contra la copia es contraintuitivo y no se entiende leyéndolo. Corre esas celdas dos
veces si hace falta: es el origen de errores que parecen embrujados.
"""),

md("""
---
# Bloque 1 · Una lista es una columna

Valores en orden, bajo un solo nombre. La diferencia con un rango de celdas es que la lista crece
y se encoge sola, sin declarar de antemano cuánto va a medir.
"""),

code("""
pagos = [9038.10, 6344.53, 7220.66, 4180.25, 11902.44]

print(pagos)
print("Cuántos:", len(pagos))
print("Tipo:   ", type(pagos))
"""),

md("""
## Los índices
"""),

code("""
print("El primero:  ", pagos[0])
print("El segundo:  ", pagos[1])
print("El último:   ", pagos[-1])
print("El penúltimo:", pagos[-2])
"""),

md("""
**El primero es cero.** Es el quiebre número uno para quien viene de la fila 1, y ya lo viste en
la semana 1.1.

**Los negativos** cuentan desde el final. `pagos[-1]` es el último sin importar cuántos haya, y
ahorra escribir `pagos[len(pagos) - 1]`.
"""),

code("""
# FALLA A PROPÓSITO. Cinco elementos van del índice 0 al 4.
try:
    print(pagos[5])
except IndexError as e:
    print("IndexError:", e)

print("El último índice válido es:", len(pagos) - 1)
"""),

md("""
## Las rebanadas

Una rebanada corta un pedazo y devuelve **una lista nueva**. El primer índice entra, el segundo
no.
"""),

code("""
print("pagos[1:3] ->", pagos[1:3])
print("pagos[:2]  ->", pagos[:2],  "<- desde el principio")
print("pagos[3:]  ->", pagos[3:],  "<- hasta el final")
print("pagos[:]   ->", pagos[:],   "<- la lista entera")
print("pagos[-2:] ->", pagos[-2:], "<- los dos últimos")
"""),

md("""
Que el segundo índice no entre suena arbitrario y no lo es: **`lista[a:b]` devuelve exactamente
`b - a` elementos.** Los tamaños salen redondos y las rebanadas se pegan sin traslape.
"""),

code("""
print("pagos[0:2] tiene", len(pagos[0:2]), "elementos")
print("pagos[2:5] tiene", len(pagos[2:5]), "elementos")
print()
print("Y juntas reconstruyen la lista:", pagos[0:2] + pagos[2:5] == pagos)
"""),

md("""
La rebanada también acepta un paso, igual que `range`.
"""),

code("""
print("Uno sí y uno no:", pagos[::2])
print("Al revés:       ", pagos[::-1])
print("La original:    ", pagos, "<- intacta")
"""),

md("""
`pagos[::-1]` es el truco para invertir sin tocar el original. Es el mismo `[inicio:fin:paso]` de
siempre, con el paso en negativo.

## Recorrer

Ya lo viste en la semana 8. Aquí solo el recordatorio de las tres formas y cuándo va cada una.
"""),

code("""
clientes = ["Ana", "Beto", "Carla", "Diego", "Elena"]

# Solo los valores.
for pago in pagos:
    print(f"{pago:>10,.2f}", end="  ")
print()

# Con la posición.
for i, pago in enumerate(pagos):
    print(f"{i}:{pago:,.0f}", end="  ")
print()

# Dos listas emparejadas.
for cliente, pago in zip(clientes, pagos):
    print(f"{cliente}={pago:,.0f}", end="  ")
print()
"""),

md("""
---
# Bloque 2 · Los métodos

Once en total. Seis cambian la lista, cinco solo preguntan por ella, y confundirlos cuesta caro.

## Los seis que modifican

| Método | Qué hace | Ejemplo |
|---|---|---|
| `append` | Agrega uno al final | `pagos.append(5500)` |
| `insert` | Agrega uno en una posición | `pagos.insert(0, 5500)` |
| `extend` | Agrega los de otra lista | `pagos.extend(otros)` |
| `remove` | Quita la primera aparición | `pagos.remove(5500)` |
| `pop` | Saca uno y lo devuelve | `ultimo = pagos.pop()` |
| `clear` | Los quita todos | `pagos.clear()` |
"""),

code("""
demo = [300, 100, 200]
print("Inicio:      ", demo)

demo.append(400)
print("append(400): ", demo)

demo.insert(0, 50)
print("insert(0,50):", demo)

demo.extend([500, 600])
print("extend:      ", demo)

demo.remove(100)
print("remove(100): ", demo)

sacado = demo.pop()
print("pop():       ", demo, "y devolvió", sacado)

demo.clear()
print("clear():     ", demo)
"""),

md("""
`pop` es el único de los seis que **modifica y además devuelve algo**. Los otros cinco devuelven
`None`, que es la señal de que trabajan sobre el original.
"""),

code("""
lista = [1, 2, 3]

print("append devuelve:", lista.append(4))
print("insert devuelve:", lista.insert(0, 0))
print("remove devuelve:", lista.remove(2))
print("pop devuelve:   ", lista.pop())
print("La lista quedó: ", lista)
"""),

md("""
## Los cinco restantes

| Método | Qué hace | Ejemplo |
|---|---|---|
| `sort` | Ordena en el lugar | `pagos.sort()` |
| `reverse` | Invierte en el lugar | `pagos.reverse()` |
| `index` | En qué posición está | `pagos.index(7220.66)` |
| `count` | Cuántas veces aparece | `pagos.count(6344.53)` |
| `copy` | Devuelve una copia nueva | `otra = pagos.copy()` |
"""),

code("""
print("index de 7220.66:", pagos.index(7220.66))
print("count de 6344.53:", pagos.count(6344.53))
print("count de 99999:  ", pagos.count(99999), "<- cero, no lanza error")

# FALLA A PROPÓSITO. index sí lanza cuando no encuentra.
try:
    pagos.index(99999)
except ValueError as e:
    print("ValueError:", e)
"""),

md("""
`count` devuelve cero cuando no encuentra y `index` lanza `ValueError`. La diferencia importa: si
solo quieres saber si algo está, `in` es más seguro que `index`.
"""),

code("""
print("¿Está 7220.66?", 7220.66 in pagos)
print("¿Está 99999?  ", 99999 in pagos)
"""),

md("""
## Modificar no es devolver

Esta es la distinción que más se cobra en el parcial.

**Predice antes de correr.** ¿Qué imprime la última línea?

- **A.** `[100, 200, 300]`, la lista ordenada.
- **B.** `None`, porque `sort` ordena y no devuelve nada.
- **C.** `[300, 100, 200]`, sin cambios.
- **D.** Un error, porque falta un argumento.
"""),

code("""
# FALLA A PROPÓSITO. Guardar lo que devuelve sort.
ventas = [300, 100, 200]
resultado = ventas.sort()

print(resultado)
print("Y la lista sí quedó ordenada:", ventas)
"""),

md("""
La respuesta es **B**. `sort` ordenó la lista y devolvió `None`.

El problema real es cuando alguien escribe `ventas = ventas.sort()`. Ahí **`ventas` deja de ser
una lista y pasa a valer `None`.** Los datos desaparecen.
"""),

code("""
# FALLA A PROPÓSITO. Reasignar el resultado de sort borra la lista.
datos = [300, 100, 200]
datos = datos.sort()

print("datos ahora vale:", datos)

try:
    print(len(datos))
except TypeError as e:
    print("TypeError:", e)
"""),

md("""
Las dos formas correctas, según lo que quieras:
"""),

code("""
originales = [300, 100, 200]

# Quiero la lista ordenada y no me importa perder el orden original.
a = originales.copy()
a.sort()
print("Con sort:  ", a)

# Quiero una copia ordenada y conservar el original.
b = sorted(originales)
print("Con sorted:", b, "· original:", originales)
"""),

md("""
`sort` es un método y trabaja sobre la lista. `sorted` es una función y devuelve otra.

La misma pareja existe para invertir: `reverse` modifica, `reversed` devuelve.
"""),

code("""
uno = [1, 2, 3]
uno.reverse()
print("reverse:", uno)

dos = [1, 2, 3]
print("reversed:", list(reversed(dos)), "· original:", dos)
"""),

md("""
## Borrar mientras recorres

Este es el error que produce resultados que no se explican.
"""),

code("""
# FALLA A PROPÓSITO. Quitar elementos dentro del for descoloca las posiciones.
numeros = [1, 2, 2, 3, 2, 4]

for n in numeros:
    if n == 2:
        numeros.remove(2)

print("Quedaron:", numeros, "<- todavía hay un 2")
"""),

md("""
Quedó un 2. El ciclo avanza por posición y `remove` recorre todo un lugar hacia la izquierda, así
que el ciclo se salta valores.

La forma correcta es construir una lista nueva en lugar de mutilar la que recorres.
"""),

code("""
numeros = [1, 2, 2, 3, 2, 4]

sin_doses = [n for n in numeros if n != 2]

print("Original:", numeros)
print("Filtrada:", sin_doses)
"""),

md("""
Eso es una **comprensión de lista**, y se lee de izquierda a derecha: "los `n` de `numeros` que no
son 2".

Es la forma más común de filtrar en Python, y es la antecesora directa de la máscara booleana de
pandas que viste en la semana 15.2.
"""),

code("""
# Filtrar, transformar, y las dos a la vez.
print("Filtrar:    ", [p for p in pagos if p > 7000])
print("Transformar:", [round(p * 1.16, 2) for p in pagos])
print("Las dos:    ", [round(p * 1.16, 2) for p in pagos if p > 7000])
"""),

md("""
`remove` tiene otra trampa: **quita solo la primera aparición.**
"""),

code("""
tres_doses = [2, 5, 2, 8, 2]
tres_doses.remove(2)

print("Después de un remove:", tres_doses, "<- quedan dos")
"""),

md("""
---
# Bloque 3 · Copias, alias y tuplas

Dos nombres pueden señalar la misma lista. Cuando eso pasa sin que lo sepas, los errores parecen
embrujados.
"""),

code("""
a = [1, 2, 3]
b = a               # esto NO copia
b.append(4)

print("b:", b)
print("a:", a, "<- también cambió")
print("¿Son el mismo objeto?", a is b)
"""),

md("""
El signo igual no copia nada. Crea **un segundo nombre para la misma lista**, y tocar cualquiera de
los dos toca la única que hay.

Es el mismo `is` de la semana 7, y aquí es donde muerde.
"""),

code("""
c = [1, 2, 3]
d = c.copy()        # esto SÍ copia
d.append(4)

print("d:", d)
print("c:", c, "<- intacta")
print("¿Son el mismo objeto?", c is d)
print("¿Valen lo mismo?", c == d)
"""),

md("""
Hay tres formas de copiar y las tres hacen lo mismo:
"""),

code("""
base = [1, 2, 3]

print(base.copy())
print(base[:])
print(list(base))
print("Las tres son objetos distintos:", base is not base.copy())
"""),

md("""
## Dónde muerde de verdad

Con una lista suelta el error se ve. Dentro de una función, no.
"""),

code("""
# FALLA A PROPÓSITO. La función modifica la lista que le pasaron.
def agregar_comision(lista_pagos):
    lista_pagos.append(500)      # toca la lista original
    return lista_pagos


mis_pagos = [9038.10, 6344.53]
resultado = agregar_comision(mis_pagos)

print("Lo que devolvió:", resultado)
print("Mi lista:       ", mis_pagos, "<- también creció")
"""),

md("""
La función recibió el nombre, no una copia. Modificarla adentro modificó la de afuera.

Eso a veces es lo que quieres. Cuando no lo es, la función copia primero.
"""),

code("""
def con_comision(lista_pagos):
    \"\"\"Devuelve una lista nueva. No toca la que recibió.\"\"\"
    nueva = lista_pagos.copy()
    nueva.append(500)
    return nueva


mis_pagos = [9038.10, 6344.53]
resultado = con_comision(mis_pagos)

print("Lo que devolvió:", resultado)
print("Mi lista:       ", mis_pagos, "<- intacta")
"""),

md("""
Esta es la razón de fondo por la que la semana 15.2 empieza haciendo `ventas.copy()` antes de la
demostración de Copy-on-Write. El problema es el mismo, un nivel más arriba.

## Tuplas

| Aspecto | Lista | Tupla |
|---|---|---|
| Se escribe | Entre corchetes | Entre paréntesis |
| Se puede cambiar | Sí | No, nunca |
| Para qué sirve | Datos que crecen | Datos que no deben cambiar |
| Ejemplo del curso | La columna de pagos | Los términos de un crédito |
"""),

code("""
terminos = (250000, 0.18, 36)

print(terminos)
print("El segundo:", terminos[1])
print("Rebanada:  ", terminos[:2])
print("Largo:     ", len(terminos))
"""),

md("""
Se indexa y se rebana igual que una lista. Lo único que no se puede es cambiarla.
"""),

code("""
# FALLA A PROPÓSITO. Una tupla no se puede modificar.
try:
    terminos[0] = 300000
except TypeError as e:
    print("TypeError:", e)

try:
    terminos.append(12)
except AttributeError as e:
    print("AttributeError:", e)
"""),

md("""
Que no se pueda cambiar suena a limitación y es una decisión de diseño. **Una tupla dice "esto no
debería cambiar"**, y el lenguaje lo hace cumplir.

Los términos de un crédito firmado son exactamente eso: si alguien los modifica a media ejecución,
el error está en quien los modificó, no en la tupla.

Y ya la venías usando sin saberlo.
"""),

code("""
def resumen(numeros):
    return min(numeros), max(numeros), sum(numeros)


devuelto = resumen(pagos)
print("Lo que devuelve:", devuelto, type(devuelto))

menor, mayor, total = devuelto
print(f"menor={menor:,.2f}  mayor={mayor:,.2f}  total={total:,.2f}")
"""),

md("""
`return a, b, c` construye una tupla, y la línea que la recibe la desempaca. Es lo que hiciste en
la semana 10 sin ponerle nombre.

También aparece en cada `for cliente, pago in zip(...)`: cada vuelta entrega una tupla y el `for`
la desempaca.
"""),

code("""
for par in zip(clientes, pagos):
    print(par, type(par).__name__)
    break

print()
print("Y en un ciclo normal se desempaca sola:")
for cliente, pago in zip(clientes[:2], pagos[:2]):
    print(f"  {cliente}: {pago:,.2f}")
"""),

md("""
## Cuatro trampas de listas

**Guardar lo que devuelve `sort`.** `pagos = pagos.sort()` deja `pagos` valiendo `None`.

**Copiar con el signo igual.** `otra = pagos` no copia nada.

**Borrar mientras recorres.** El ciclo se salta valores.

**Suponer que `remove` quita todos.** Quita solo la primera aparición.

Las cuatro las viste correr arriba.
"""),

md("""
---
# Ejercicios

Las soluciones están hasta abajo del cuaderno.

## Índices y rebanadas

### Ejercicio 1 · Los seis accesos

Con una lista de doce valores de tu área, imprime: el primero, el último, los tres primeros, los
tres últimos, los de en medio, y la lista al revés.

Comprueba al final que la lista original no cambió.

### Ejercicio 2 · Por qué el segundo no entra

Demuestra con código que `lista[a:b]` devuelve exactamente `b - a` elementos, probando con cuatro
pares distintos.

Después parte tu lista de doce en tres pedazos de cuatro y comprueba que al pegarlos vuelve a
salir la original.

### Ejercicio 3 · El índice que no existe

Provoca un `IndexError` con un índice positivo y otro con uno negativo. Anota los dos mensajes.

Después escribe una función `elemento_seguro(lista, i)` que devuelva `None` en lugar de tronar.

## Métodos

### Ejercicio 4 · Los seis que modifican

Empieza con una lista de tres elementos y aplica los seis métodos que modifican, en orden,
imprimiendo la lista después de cada uno. Termina con una lista distinta a la inicial y no vacía.

### Ejercicio 5 · La pareja peligrosa

Escribe cuatro líneas que demuestren la diferencia entre `sort` y `sorted`, y entre `reverse` y
`reversed`. Imprime en cada caso qué devolvió y cómo quedó la lista.

### Ejercicio 6 · Filtrar sin romper

Toma una lista con valores repetidos y quita todas las apariciones de uno de ellos, de dos formas:
con un ciclo `while` y `remove`, y con una comprensión de lista.

Di en un comentario cuál prefieres y por qué.

## Copias y tuplas

### Ejercicio 7 · El alias que muerde

Escribe una función que reciba una lista y le agregue un elemento, y demuestra que modifica la
original. Después arréglala y demuestra que ya no.

### Ejercicio 8 · Lista o tupla

Para cada uno, di en un comentario si lo guardarías en lista o en tupla y por qué: las coordenadas
de una sucursal, los pagos mensuales de un crédito, los meses del año, los clientes atendidos hoy,
los términos de un contrato firmado.

### Ejercicio 9 · Una columna de tu área

Toma doce valores reales de tu carrera en una lista y responde cuatro preguntas: el mayor, el
menor, los tres más altos, y en qué posición está uno que tú elijas.

La lista original tiene que quedar en su orden inicial al terminar. Imprímela al principio y al
final: si cambió, usaste un método donde iba una función.
"""),

md("""
---
## Tres ideas para llevarse

**Una lista es una columna.** Y en la semana 15 esa misma columna se llamará `Series`, con un
índice puesto encima. Todo lo de hoy sobre recorrer, cortar y ordenar sigue valiendo ahí.

**Modificar no es devolver.** `sort` ordena y devuelve `None`; `sorted` deja la lista quieta y
devuelve otra. La confusión no da error, borra datos.

**El igual no copia.** Crea un segundo nombre para la misma lista, y tocar cualquiera de los dos
toca la única que hay.

La siguiente sesión son diccionarios y conjuntos, y el segundo examen parcial.
"""),

md("""
---
# Soluciones

### Ejercicio 1

```python
unidades = [15, 8, 22, 5, 11, 35, 20, 18, 9, 27, 13, 31]

print("Original:     ", unidades)
print("El primero:   ", unidades[0])
print("El último:    ", unidades[-1])
print("Los tres 1ros:", unidades[:3])
print("Los tres últ.:", unidades[-3:])
print("Los de enmedio:", unidades[4:8])
print("Al revés:     ", unidades[::-1])
print("Sin cambios:  ", unidades)
```

Ninguna rebanada tocó la original, porque todas devuelven listas nuevas. Esa es la diferencia con
los métodos del bloque 2.

### Ejercicio 2

```python
for a, b in [(0, 3), (2, 7), (4, 12), (5, 6)]:
    print(f"[{a}:{b}] devuelve {len(unidades[a:b])} elementos, y b-a es {b - a}")

uno, dos, tres = unidades[0:4], unidades[4:8], unidades[8:12]
print("\\nJuntas:", uno + dos + tres == unidades)
```

Los tres pedazos se pegan sin traslape y sin huecos precisamente porque el final no entra. Si
entrara, habría que escribir `[0:3]`, `[4:7]`, `[8:11]` y acordarse de sumar uno cada vez.

### Ejercicio 3

```python
for i in [12, -13]:
    try:
        unidades[i]
    except IndexError as e:
        print(f"unidades[{i}] -> IndexError: {e}")


def elemento_seguro(lista, i):
    \"\"\"Devuelve el elemento, o None si la posición no existe.\"\"\"
    try:
        return lista[i]
    except IndexError:
        return None


print(elemento_seguro(unidades, 3), elemento_seguro(unidades, 99))
```

Los dos mensajes dicen lo mismo, `list index out of range`, sin decir cuál era el índice ni cuántos
elementos había. Por eso conviene imprimir `len` al lado cuando estés depurando.

### Ejercicio 4

```python
lista = [10, 20, 30]
print("Inicio:  ", lista)

lista.append(40);        print("append:  ", lista)
lista.insert(0, 5);      print("insert:  ", lista)
lista.extend([50, 60]);  print("extend:  ", lista)
lista.remove(20);        print("remove:  ", lista)
lista.pop();             print("pop:     ", lista)
lista.clear();           print("clear:   ", lista)

lista.extend([1, 2, 3])
print("Al final:", lista)
```

`clear` deja la lista vacía y no la destruye: sigue siendo la misma lista, y por eso el `extend`
de después funciona.

### Ejercicio 5

```python
a = [3, 1, 2]
print("sort devolvió:  ", a.sort(), "· lista:", a)

b = [3, 1, 2]
print("sorted devolvió:", sorted(b), "· lista:", b)

c = [3, 1, 2]
print("reverse devolvió:", c.reverse(), "· lista:", c)

d = [3, 1, 2]
print("reversed devolvió:", list(reversed(d)), "· lista:", d)
```

Los dos métodos devuelven `None` y cambian la lista. Las dos funciones devuelven algo y no la
tocan. `reversed` además devuelve un objeto perezoso, por eso el `list()` alrededor.

### Ejercicio 6

```python
valores = [2, 5, 2, 8, 2, 9]

con_while = valores.copy()
while 2 in con_while:
    con_while.remove(2)

con_comprension = [v for v in valores if v != 2]

print("Con while+remove:", con_while)
print("Con comprensión: ", con_comprension)

# Prefiero la comprensión. Dice qué quiero en una línea en lugar de decir cómo
# quitarlo en tres, no modifica nada, y no puede quedarse en un ciclo infinito si
# me equivoco en la condición. El while+remove además recorre la lista una vez por
# cada elemento que quita.
```

La comprensión también es la que se parece a lo que vas a escribir en pandas:
`ventas[ventas["region"] != "North"]` es la misma idea con otra sintaxis.

### Ejercicio 7

```python
def agrega_mal(lista):
    lista.append(999)
    return lista


def agrega_bien(lista):
    nueva = lista.copy()
    nueva.append(999)
    return nueva


original = [1, 2, 3]
agrega_mal(original)
print("Después de agrega_mal: ", original)

original = [1, 2, 3]
devuelta = agrega_bien(original)
print("Después de agrega_bien:", original, "· devolvió", devuelta)
```

La regla práctica: si tu función devuelve algo, que no modifique además lo que recibió. Hacer las
dos cosas es lo que sorprende a quien la llama.

### Ejercicio 8

```python
# Coordenadas de una sucursal -> tupla. Son dos números que van juntos y no
#   cambian. Además una tupla se puede usar como llave de diccionario y una
#   lista no.
# Pagos mensuales de un crédito -> lista. Se van agregando conforme se pagan.
# Meses del año -> tupla. Son doce, siempre los mismos, y nadie debería poder
#   agregarle un decimotercero por accidente.
# Clientes atendidos hoy -> lista. Crece durante el día.
# Términos de un contrato firmado -> tupla. Cambiarlos después de firmar es
#   exactamente lo que no debe pasar, y la tupla lo impide.
```

La pregunta que decide: ¿esto va a crecer o a cambiar durante la ejecución? Si no, tupla, y el
lenguaje te cuida la espalda.

### Ejercicio 9

No hay solución publicada porque los valores son distintos para cada quien. Se califica sobre tres
cosas: que las cuatro respuestas estén etiquetadas, que la lista impresa al final sea idéntica a
la del principio, y que para "los tres más altos" hayas usado `sorted` y no `sort`.
"""),

]

write(OUT / "es" / "w12.ipynb", es)
print("wrote", OUT / "es" / "w12.ipynb")
