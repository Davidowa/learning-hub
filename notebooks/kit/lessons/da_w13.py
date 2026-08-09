"""notebooks/analisis-de-datos/es/w13.ipynb

Source deck: ppts/python/analisis-de-datos/es/w13.es.yaml
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from nbkit import md, code, write, REPO

OUT = REPO / "notebooks" / "analisis-de-datos"

es = [

md("""
# Análisis de Datos · Semana 13
## Conjuntos y diccionarios · Segundo parcial

**TIA502 · Facultad de Empresariales · Profesor David Escobar-Castillejos**

El diccionario es la pieza que más rendimiento da en todo el curso. Es el `BUSCARV`, y en la
semana 15 es lo que hace `groupby` por dentro.

Al terminar este cuaderno vas a poder:

1. Crear y consultar un diccionario, por llave y con `get`.
2. Recorrer llaves, valores y pares con `keys`, `values` e `items`.
3. Quitar duplicados con un conjunto, en una línea.
4. Usar las cuatro operaciones de conjuntos.
5. Elegir la colección correcta por la pregunta que va a contestar.

### El segundo parcial

| Aspecto | Detalle |
|---|---|
| Contenido | Unidades 4, 5 y 6: repetición, funciones y colecciones |
| Peso | 20 % de la calificación final |
| Formato | En la computadora del salón, y se sube comprimido a Blackboard |
| Puedes llevar | Apuntes, tareas, libros y lo que hayas generado con IA antes |
| No puedes | Teléfono, audífonos, lentes con IA ni mensajería |

### Cómo se usa este cuaderno

Ejecuta las celdas en orden. Cinco fallan a propósito y llevan un comentario que lo dice.
"""),

md("""
---
# Bloque 1 · El diccionario

Una tabla de dos columnas donde la primera es única. Es lo que buscas con `BUSCARV`, sin la
columna número tres.

En la hoja escribirías:

```
=BUSCARV(B2, Catalogo, 2, FALSO)
```

Tres argumentos y hay que contar en cuál columna está lo que quieres. En Python:
"""),

code("""
tasas = {"AAA": 0.12, "AA": 0.18, "A": 0.24, "B": 0.32}

print(tasas)
print("La tasa de AA:", tasas["AA"])
"""),

md("""
A la izquierda de los dos puntos la **llave**, a la derecha el **valor**. Las llaves no se
repiten, y el acceso es con corchetes igual que una lista, solo que el índice es la llave en
lugar de un número.

La columna número tres no existe porque no hace falta. Y a diferencia del `BUSCARV`, agregar una
calificación no descoloca nada.

## Cuando la llave no existe
"""),

code("""
# FALLA A PROPÓSITO. Una llave que no está.
try:
    print(tasas["C"])
except KeyError as e:
    print("KeyError:", e)
"""),

md("""
`KeyError` detiene el programa ahí mismo. Cuando la llave puede no existir, `get` es la salida.
"""),

code("""
print("get sin omisión: ", tasas.get("C"))
print("get con omisión: ", tasas.get("C", 0.40))
print("get de una que sí:", tasas.get("AA"))
"""),

md("""
`get` devuelve `None` si la llave no existe, en lugar de reventar, y admite un valor por omisión.

**Cuál usar.** Corchetes cuando la llave *tiene* que estar y su ausencia es un error que quieres
ver. `get` cuando la ausencia es normal y tienes un valor razonable de respaldo.
"""),

code("""
# Un cliente sin calificación registrada paga la tasa más alta.
CALIFICACIONES = {"Insumos SA": "AAA", "Papelera": "A", "Log Express": "B"}
TASA_SIN_CALIFICAR = 0.40

for cliente in ["Insumos SA", "Papelera", "Nuevo Cliente"]:
    calif = CALIFICACIONES.get(cliente, "sin calificar")
    tasa = tasas.get(calif, TASA_SIN_CALIFICAR)
    print(f"{cliente:<15} {calif:<14} {tasa:.0%}")
"""),

md("""
Dos `get` encadenados y ningún `if`. El cliente nuevo cae en la tasa de respaldo sin que el
programa se detenga.

## Recorrer un diccionario

| Método | Qué entrega | Cuándo se usa |
|---|---|---|
| `keys` | Solo las llaves | Cuando basta con saber cuáles hay |
| `values` | Solo los valores | Para sumar o promediar |
| `items` | Los pares completos | Para imprimir la tabla entera |
"""),

code("""
print("Llaves: ", list(tasas.keys()))
print("Valores:", list(tasas.values()))
print("Pares:  ", list(tasas.items()))
"""),

code("""
for clave, valor in tasas.items():
    print(f"{clave:<4} {valor:.0%}")
"""),

md("""
`items` entrega una tupla por vuelta y el `for` la desempaca, exactamente como el `zip` de la
semana pasada.

Y con `values` las funciones de siempre funcionan igual.
"""),

code("""
valores = list(tasas.values())

print("Tasa promedio:", f"{sum(valores) / len(valores):.2%}")
print("La más alta:  ", f"{max(valores):.0%}")
print("La más baja:  ", f"{min(valores):.0%}")
"""),

md("""
## Modificar

Asignar a una llave que existe la sobreescribe. Asignar a una que no existe la crea. **Es la misma
línea.**

**Predice antes de correr.** ¿Qué imprime la última línea?

- **A.** 4, porque se agregaron dos entradas.
- **B.** 3, porque Norte ya existía y se sobreescribió.
- **C.** 2, porque el diccionario no crece.
- **D.** Un error, porque Este no existía.
"""),

code("""
conteo = {"Norte": 3, "Sur": 1}
conteo["Norte"] = 5
conteo["Este"] = 2

print(conteo)
print(len(conteo))
"""),

md("""
La respuesta es **B**, tres. `conteo["Norte"] = 5` sobreescribió y `conteo["Este"] = 2` creó.

Que sea la misma sintaxis es cómodo y peligroso: un error de dedo en el nombre de una llave no
lanza nada, crea una entrada nueva.
"""),

code("""
# FALLA A PROPÓSITO. Un dedazo en la llave crea una entrada, no un error.
inventario = {"Espresso": 42, "Molino": 18}
inventario["Esprseso"] = 50      # dedazo

print(inventario)
print("Ahora hay", len(inventario), "productos, y uno no existe.")
"""),

md("""
Es el mismo problema de las ocho regiones de `sales.csv`. Un diccionario no valida sus llaves, así
que la validación tiene que estar en otro lado.
"""),

code("""
PRODUCTOS_VALIDOS = {"Espresso", "Molino", "Hervidor"}

def registrar(inventario, producto, cantidad):
    \"\"\"Agrega al inventario, rechazando productos que no están en el catálogo.\"\"\"
    if producto not in PRODUCTOS_VALIDOS:
        return f"'{producto}' no está en el catálogo"
    inventario[producto] = cantidad
    return f"{producto}: {cantidad}"


inv = {}
print(registrar(inv, "Espresso", 42))
print(registrar(inv, "Esprseso", 50))
print("Inventario:", inv)
"""),

md("""
## Contar con un diccionario

Este es el patrón que más vas a usar, y es lo que `value_counts` de pandas hace por dentro.
"""),

code("""
regiones = ["Norte", "Centro", "Norte", "Sur", "Centro", "Norte"]

conteo = {}
for r in regiones:
    conteo[r] = conteo.get(r, 0) + 1

print(conteo)
"""),

md("""
El `conteo.get(r, 0) + 1` es la línea entera: si la región ya estaba, suma uno a lo que había; si
no, empieza en cero y suma uno.

Sin `get` haría falta un `if` para el primer caso de cada región.
"""),

code("""
# Lo mismo, con la herramienta que ya existe para esto.
from collections import Counter

print(Counter(regiones))
print(Counter(regiones).most_common(2))
"""),

md("""
`Counter` es un diccionario especializado en contar, y `most_common` da los más frecuentes ya
ordenados. Es literalmente lo que `value_counts` devuelve en la semana 15.
"""),

md("""
---
# Bloque 2 · El conjunto

Valores distintos, sin repetidos y sin orden. Es quitar duplicados en una línea.
"""),

code("""
regiones = ["Norte", "Centro", "Norte", "Sur", "Centro", "Norte"]

unicas = set(regiones)

print(sorted(unicas))
print(len(unicas), "distintas de", len(regiones), "registros")
"""),

md("""
Esa línea reemplaza al ciclo con lista auxiliar que casi todos escriben la primera vez:
"""),

code("""
# La versión larga, para que se vea qué te ahorra el conjunto.
vistas = []
for r in regiones:
    if r not in vistas:
        vistas.append(r)

print(vistas)
"""),

md("""
Las dos dan lo mismo con seis elementos. Con trescientos mil, la del conjunto es
incomparablemente más rápida, porque preguntar `x in conjunto` es inmediato y `x in lista`
recorre.
"""),

code("""
import time

grande = list(range(20000))
conjunto = set(grande)

inicio = time.perf_counter()
19999 in grande
t_lista = time.perf_counter() - inicio

inicio = time.perf_counter()
19999 in conjunto
t_conjunto = time.perf_counter() - inicio

print(f"Buscar en la lista:    {t_lista * 1e6:>8.1f} microsegundos")
print(f"Buscar en el conjunto: {t_conjunto * 1e6:>8.1f} microsegundos")
"""),

md("""
Los tiempos exactos cambian entre corridas y entre máquinas. Lo que no cambia es cuál es más
rápido, y la diferencia crece con el tamaño.

Por eso `PRODUCTOS_VALIDOS` de arriba es un conjunto y no una lista.

## Las cuatro operaciones

| Operación | Símbolo | Qué devuelve |
|---|---|---|
| Unión | `\\|` | Lo que está en cualquiera de los dos |
| Intersección | `&` | Solo lo que está en los dos |
| Diferencia | `-` | Lo del primero que no está en el segundo |
| Diferencia simétrica | `^` | Lo que está en uno pero no en ambos |
"""),

code("""
este = {"Norte", "Centro", "Sur"}
pasado = {"Centro", "Sur", "Este"}

print("Unión:               ", sorted(este | pasado))
print("Intersección:        ", sorted(este & pasado))
print("Diferencia:          ", sorted(este - pasado))
print("Al revés:            ", sorted(pasado - este))
print("Diferencia simétrica:", sorted(este ^ pasado))
"""),

md("""
Cada una contesta una pregunta de negocio distinta.

**Intersección**: en qué regiones operamos los dos años. **Diferencia**: cuáles abrimos este año.
**La diferencia al revés**: cuáles cerramos. **Diferencia simétrica**: dónde hubo movimiento, en
cualquier dirección.

Fíjate en que `este - pasado` y `pasado - este` **no** dan lo mismo. La diferencia no es
conmutativa, y confundirlas reporta aperturas como cierres.
"""),

code("""
print("Abrimos:", sorted(este - pasado))
print("Cerramos:", sorted(pasado - este))
print("¿Son iguales?", (este - pasado) == (pasado - este))
"""),

md("""
## Lo que un conjunto no tiene
"""),

code("""
# FALLA A PROPÓSITO. Un conjunto no tiene posiciones.
try:
    print(unicas[0])
except TypeError as e:
    print("TypeError:", e)

print("Y su orden al imprimir no es de fiar:", set(["b", "a", "c"]))
print("Por eso se ordena al mostrarlo:", sorted(set(["b", "a", "c"])))
"""),

md("""
Un conjunto no guarda orden, así que no se indexa y no se rebana. Cuando necesitas mostrarlo,
`sorted` lo convierte en una lista ordenada.

Y no admite elementos que puedan cambiar.
"""),

code("""
# FALLA A PROPÓSITO. Una lista no puede vivir dentro de un conjunto.
try:
    {["Norte", "Sur"]}
except TypeError as e:
    print("TypeError:", e)

print("Con una tupla sí:", {("Norte", "Sur"), ("Centro", "Este")})
"""),

md("""
Esa es una de las razones prácticas por las que las tuplas existen: **una tupla puede ser elemento
de un conjunto o llave de un diccionario, y una lista no.**
"""),

code("""
# Una llave compuesta: región y canal juntos.
ventas_por_par = {
    ("Norte", "Retail"): 1331426,
    ("Norte", "Online"): 978286,
    ("Sur", "Retail"): 271090,
}

print(ventas_por_par[("Norte", "Retail")])
for (region, canal), monto in ventas_por_par.items():
    print(f"{region:<8}{canal:<10}{monto:>12,}")
"""),

md("""
Eso es exactamente lo que devuelve `groupby(["region", "channel"])` en la semana 15.3: un índice
de dos niveles, que por dentro son tuplas.
"""),

md("""
---
# Bloque 3 · Cuál usar

Cuatro colecciones y una sola pregunta que decide entre ellas.

| Si necesitas | Usa | Por qué |
|---|---|---|
| Orden y repetidos | Lista | Es la columna de tu tabla |
| Que nadie la cambie | Tupla | Los términos de un contrato |
| Valores distintos | Conjunto | Quita duplicados solo |
| Buscar por llave | Diccionario | Es el `BUSCARV`, y es inmediato |

Las cuatro, con los mismos datos, para ver qué conserva cada una.
"""),

code("""
datos = ["Norte", "Centro", "Norte", "Sur"]

print("Lista:      ", list(datos), "· orden sí, repetidos sí")
print("Tupla:      ", tuple(datos), "· orden sí, repetidos sí, y no se puede cambiar")
print("Conjunto:   ", sorted(set(datos)), "· orden no, repetidos no")
print("Diccionario:", {r: datos.count(r) for r in set(datos)}, "· llave única, valor libre")
"""),

md("""
Ese `{r: datos.count(r) for r in set(datos)}` es una **comprensión de diccionario**, hermana de la
de listas de la semana pasada. Se lee igual: "para cada `r` distinto, la llave es `r` y el valor
es cuántas veces aparece".

## Todo junto: un reporte de campañas
"""),

code("""
CAMPANAS = [
    ("Instagram", 38500), ("Google", 51200), ("Meta", 29800),
    ("Instagram", 12400), ("TikTok", 9600), ("Google", 18300),
]

# Diccionario: acumular la inversión por canal.
inversion = {}
for canal, monto in CAMPANAS:
    inversion[canal] = inversion.get(canal, 0) + monto

for canal, monto in sorted(inversion.items(), key=lambda par: par[1], reverse=True):
    print(f"{canal:<12}{monto:>10,}")

print(f"{'Total':<12}{sum(inversion.values()):>10,}")
"""),

code("""
# Conjunto: qué canales aparecen este año y no el pasado.
este_anio = set(inversion)
pasado = {"Instagram", "Meta", "Radio", "Espectacular"}

print("Nuevos este año:  ", sorted(este_anio - pasado))
print("Los que dejamos:  ", sorted(pasado - este_anio))
print("Los que siguen:   ", sorted(este_anio & pasado))
"""),

md("""
Dos canales nuevos, dos abandonados y dos que siguen. Ese `sorted(inversion.items(), key=...)` de
la celda anterior ordena un diccionario por su valor, y es el `key` que viste en la semana 11.

## Cuatro errores de colecciones

**Corchetes donde iba `get`.** `KeyError` detiene el programa.

**Suponer que un conjunto conserva el orden.** No lo conserva, y el orden que muestra puede cambiar
entre corridas.

**Confundir el sentido de la diferencia.** `a - b` y `b - a` contestan preguntas opuestas.

**Un dedazo en una llave.** No lanza error, crea una entrada nueva.
"""),

md("""
---
# Ejercicios

Las soluciones están hasta abajo del cuaderno.

## Diccionarios

### Ejercicio 1 · Tu catálogo

Construye un diccionario que traduzca un código de tu carrera a su descripción o a su valor, con
al menos seis entradas. Recórrelo con `items` imprimiendo la tabla alineada.

### Ejercicio 2 · La consulta que no revienta

Escribe una función `consultar(catalogo, clave)` que devuelva el valor, o un texto que diga que no
existe, sin usar `try`.

Pruébala con tres llaves que existan y dos que no.

### Ejercicio 3 · Contar sin `Counter`

Con una lista de al menos quince valores repetidos de tu área, construye un diccionario de
conteos usando `get`. Después imprime el más frecuente y el menos frecuente.

Pista: `max(conteo, key=conteo.get)`.

### Ejercicio 4 · Sumar por categoría

Con una lista de tuplas `(categoria, monto)`, arma un diccionario que acumule el monto por
categoría, y otro que cuente cuántos registros hay de cada una.

Imprime las dos tablas y el promedio por categoría.

## Conjuntos

### Ejercicio 5 · Lo distinto

Con la lista del ejercicio 3, imprime cuántos valores distintos hay, cuáles son en orden, y
cuántos aparecen una sola vez.

### Ejercicio 6 · Las cuatro operaciones

Arma dos conjuntos con los proveedores de dos años distintos y contesta con las cuatro
operaciones: cuáles siguen, cuáles llegaron, cuáles se fueron, y en cuáles hubo movimiento.

Comprueba con código que `a - b` no es lo mismo que `b - a`.

### Ejercicio 7 · Por qué la tupla

Demuestra que una lista no puede ser elemento de un conjunto y una tupla sí. Después construye un
diccionario con llaves compuestas de dos valores y recórrelo desempacando la llave.

## Elegir

### Ejercicio 8 · La colección correcta

Para cada uno, di en un comentario qué colección usarías y por qué: los folios de las facturas del
mes, el catálogo de códigos postales a ciudad, las calificaciones que ha tenido un cliente en
orden, los productos que se vendieron hoy sin repetir, y las coordenadas de una sucursal.

### Ejercicio 9 · Un catálogo con todo

Junta las cuatro: una lista de registros, un diccionario de catálogo, un conjunto para los
distintos, y una tupla para algo que no debe cambiar. Produce un reporte de cinco líneas.

La consulta al catálogo tiene que usar `get` con valor por omisión, y el programa tiene que seguir
corriendo cuando le pases una llave que no existe.
"""),

md("""
---
## Tres ideas para llevarse

**Un diccionario es un `BUSCARV`.** La llave, el valor, y ninguna columna número tres. En la
semana 15 esto es lo que hace `groupby` por dentro.

**`get` no revienta.** Los corchetes lanzan `KeyError` con una llave que falta, y `get` devuelve lo
que tú decidas.

**Un conjunto quita duplicados solo.** Una línea reemplaza al ciclo con lista auxiliar, y además
buscar dentro de él es inmediato en lugar de recorrer.

La siguiente sesión son archivos. Ahí dejan de escribirse los datos a mano y empiezan a leerse de
verdad.
"""),

md("""
---
# Soluciones

### Ejercicio 1

```python
AREAS = {
    "SLS": "Ventas", "MKT": "Mercadotecnia", "FIN": "Finanzas",
    "HRS": "Recursos Humanos", "OPS": "Operaciones", "LEG": "Jurídico",
}

print(f"{'Código':<8}{'Área'}")
print("-" * 30)
for codigo, nombre in AREAS.items():
    print(f"{codigo:<8}{nombre}")
```

Los diccionarios conservan el orden en que se insertaron desde Python 3.7. Antes no, y por eso
todavía hay código viejo que ordena las llaves por si acaso.

### Ejercicio 2

```python
def consultar(catalogo, clave):
    \"\"\"Devuelve el valor, o un aviso si la clave no está.\"\"\"
    return catalogo.get(clave, f"'{clave}' no está en el catálogo")


for c in ["SLS", "FIN", "OPS", "XYZ", ""]:
    print(f"{c!r:<8} -> {consultar(AREAS, c)}")
```

Sin un solo `try`. `get` con valor por omisión cubre el caso ausente, y el valor por omisión puede
ser cualquier cosa, incluido un mensaje construido con la propia clave.

### Ejercicio 3

```python
canales = ["Instagram", "Google", "Instagram", "Meta", "Google", "Instagram",
           "TikTok", "Meta", "Google", "Instagram", "LinkedIn", "Google",
           "Meta", "Instagram", "TikTok"]

conteo = {}
for c in canales:
    conteo[c] = conteo.get(c, 0) + 1

print(conteo)
print("El más frecuente:", max(conteo, key=conteo.get), "con", max(conteo.values()))
print("El menos:        ", min(conteo, key=conteo.get), "con", min(conteo.values()))
```

`max(conteo, key=conteo.get)` recorre las llaves y compara por su valor. Sin el `key` compararía
las llaves como texto y devolvería la última alfabéticamente.

### Ejercicio 4

```python
REGISTROS = [
    ("Retail", 12400), ("Online", 38500), ("Retail", 8900),
    ("Mayoreo", 51200), ("Online", 18300), ("Mayoreo", 29800),
    ("Retail", 5600),
]

monto = {}
cuantos = {}
for categoria, valor in REGISTROS:
    monto[categoria] = monto.get(categoria, 0) + valor
    cuantos[categoria] = cuantos.get(categoria, 0) + 1

print(f"{'Categoría':<12}{'Monto':>12}{'Registros':>11}{'Promedio':>12}")
for cat in monto:
    print(f"{cat:<12}{monto[cat]:>12,}{cuantos[cat]:>11}"
          f"{monto[cat] / cuantos[cat]:>12,.2f}")
```

Dos diccionarios llenados en el mismo ciclo. Es el acumulador y el contador de la semana 9, uno
por categoría en lugar de uno global.

Y es exactamente lo que `groupby("categoria").agg(["sum", "count", "mean"])` hace en una línea en
la semana 15.3.

### Ejercicio 5

```python
distintos = set(canales)

print("Cuántos distintos:", len(distintos))
print("Cuáles:", sorted(distintos))
print("Aparecen una sola vez:", sorted(c for c in distintos if canales.count(c) == 1))
```

Solo LinkedIn aparece una vez. Nota que `canales.count(c)` recorre la lista entera por cada canal
distinto: con quince elementos da igual, y con un millón habría que usar el diccionario de conteos
del ejercicio 3.

### Ejercicio 6

```python
este = {"Insumos SA", "Papelera", "Log Express", "Cafés del Sur"}
pasado = {"Papelera", "Log Express", "Empaques MX", "Tinta y Papel"}

print("Siguen:      ", sorted(este & pasado))
print("Llegaron:    ", sorted(este - pasado))
print("Se fueron:   ", sorted(pasado - este))
print("Hubo cambio: ", sorted(este ^ pasado))
print()
print("¿a - b es igual a b - a?", (este - pasado) == (pasado - este))
```

Dos siguen, dos llegaron, dos se fueron. La diferencia simétrica junta los cuatro que se movieron,
que es la lista que le interesa a quien revisa la cartera de proveedores.

### Ejercicio 7

```python
try:
    {["a", "b"]}
except TypeError as e:
    print("Con lista ->", e)

print("Con tupla ->", {("a", "b"), ("c", "d")})

ventas = {
    ("Norte", "2025"): 4351976,
    ("Norte", "2024"): 3980112,
    ("Sur", "2025"): 1553003,
}

for (region, anio), monto in sorted(ventas.items()):
    print(f"{region:<8}{anio:<7}{monto:>12,}")
```

La razón técnica es que un conjunto y un diccionario necesitan que sus elementos no cambien
después de guardarlos, porque los acomodan según su contenido. Una lista puede cambiar, y entonces
quedaría en el lugar equivocado.

### Ejercicio 8

```python
# Folios de las facturas del mes -> conjunto, si solo quieres saber cuáles hay y
#   detectar duplicados. Lista si el orden de emisión importa.
# Catálogo de código postal a ciudad -> diccionario. Es el BUSCARV puro.
# Calificaciones que ha tenido un cliente, en orden -> lista. El orden es el dato:
#   pasar de B a AAA no es lo mismo que al revés.
# Productos vendidos hoy sin repetir -> conjunto. Es literalmente su definición.
# Coordenadas de una sucursal -> tupla. Dos números que van juntos y no cambian.
```

El primero es el interesante porque depende de la pregunta. "¿Cuántas facturas distintas?" pide
conjunto; "¿en qué orden se emitieron?" pide lista. La colección la elige la pregunta, no el dato.

### Ejercicio 9

No hay solución publicada porque el catálogo es distinto para cada quien. Se califica sobre cuatro
cosas: que aparezcan las cuatro colecciones y cada una haga algo que las otras no harían bien, que
la consulta use `get` con valor por omisión, que el programa siga corriendo con una llave
inexistente, y que el reporte tenga encabezado y total.
"""),

]

write(OUT / "es" / "w13.ipynb", es)
print("wrote", OUT / "es" / "w13.ipynb")
