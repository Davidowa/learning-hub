"""notebooks/programacion-orientada-a-objetos/es/w10.ipynb

Source deck: ppts/python/programacion-orientada-a-objetos/es/w10.es.yaml
Source code:  docs/en/courses/python-course/01 - Basics/4th Module/Code012.py
                  (listas: índices, cortes, append, insert, remove, pop, copy)
              docs/en/courses/python-course/01 - Basics/4th Module/Code016.py
                  (array.array y el append de un tipo que no entra)
              docs/en/courses/python-course/01 - Basics/4th Module/Code017.py
                  (comprensiones, map, filter, generadores, desempaquetado, zip,
                   pila y cola)

Code012.py y Code016.py corren completos, comprobado.

Code017.py NO corre completo. Su línea 292 es numbers.append(*new_numbers) y
lanza TypeError: list.append() takes exactly one argument (3 given). El archivo
se detiene ahí, así que sus últimas noventa y ocho líneas -el desempaquetado en
literal, el desempaquetado de diccionarios, zip, la pila y la cola- nunca se
ejecutan en el original. El cuaderno cita la línea como trampa, la corre dentro
de un try, y después revive a mano el tramo muerto.

Otras tres cosas medidas que no coinciden con lo que dice el repositorio, todas
citadas sin corregir:

  Code017.py líneas 257 y 261 anuncian "gen: 112" y "com: 824456". Hoy esa misma
  medición da otros valores, porque getsizeof mide la representación interna y
  esa cambia entre versiones de Python. La conclusión del archivo se sostiene.

  Code017.py líneas 366 a 369 tienen la condición invertida: el comentario
  promete evitar el pop de una pila vacía y el if llama a pop justo cuando está
  vacía. No se dispara porque la pila trae dos elementos, y porque el archivo ya
  se detuvo doscientas líneas antes.

  Code016.py línea 55 deja comentado un append con el mensaje "an integer is
  required (got type str)". Corrido de verdad hoy, el mensaje es otro.

Code017.py línea 12 define sum y tapa la de Python para el resto del archivo.

La semana 9 cerró apuntando a colecciones. Este cuaderno arranca de ahí y cierra
apuntando al manejo de excepciones de la semana 11.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from nbkit import md, code, write, REPO

OUT = REPO / "notebooks" / "programacion-orientada-a-objetos"

es = [

md("""
# Programación Orientada a Objetos · Semana 10
## Tema 4 · Funciones y estructuras avanzadas

**COM102 · Facultad de Ingeniería · Profesor David Escobar-Castillejos**

Cuatro maneras de guardar varias cosas en una variable, cómo crece una lista por dentro, y qué se puede
hacer sin tocar el disco.

La semana pasada terminamos partiendo un script en funciones. Cada una de esas funciones recibía una
colección y devolvía otra, y ninguna se preguntó cuál convenía. Esta semana es esa pregunta.

Al terminar vas a poder:

1. Elegir entre lista, tupla, conjunto y diccionario con tres preguntas sobre orden, cambio y forma de
   buscar.
2. Explicar qué es un arreglo dinámico y por qué agregar al final sale barato y al principio no.
3. Filtrar, transformar y agrupar en memoria con comprensiones y con un diccionario acumulador.
4. Distinguir copiar de compartir, y decir cuándo el signo igual dejó dos nombres sobre un mismo objeto.
5. Leer un desempaquetado con asterisco y decir cuántos argumentos llegan del otro lado.

### Cómo se usa este cuaderno

Ejecuta las celdas en orden con **Shift + Enter**. Doce fallan a propósito y llevan un comentario que lo
dice.

Nueve de las doce **no lanzan ninguna excepción**. Entre ellas está la más cara de todas: la que borra
elementos de una lista mientras la recorre, nunca llega a mirar dos de los seis nombres, y entrega una
lista más corta con toda naturalidad.
"""),

md("""
---
# Bloque 1 · Las cuatro colecciones

Lista, tupla, conjunto y diccionario. Los cuatro guardan varias cosas en una variable y los cuatro se
recorren con el mismo `for`, así que a primera vista parecen intercambiables.

No lo son. Cada uno contesta rápido a una pregunta distinta y lento a todas las demás.
"""),

code("""
frutas_lista = ["manzana", "plátano", "cereza", "manzana"]
frutas_tupla = ("manzana", "plátano", "cereza", "manzana")
frutas_conjunto = {"manzana", "plátano", "cereza", "manzana"}
frutas_dicc = {"manzana": 32, "plátano": 18, "cereza": 95}

for nombre, coleccion in [("lista", frutas_lista), ("tupla", frutas_tupla),
                          ("conjunto", frutas_conjunto), ("diccionario", frutas_dicc)]:
    print(f"  {nombre:<12}{len(coleccion)} elementos   {coleccion}")

print()
print("Los cuatro elementos escritos, después de guardarlos:")
print("  lista:      ", len(frutas_lista), "<- conservó la manzana repetida")
print("  conjunto:   ", len(frutas_conjunto), "<- la repetida desapareció")
print()
print("¿La lista tiene un orden?     ", frutas_lista[0], "sigue siendo el primero")
print("¿La tupla se puede modificar?  no, y por eso sirve de llave:",
      {("a", 1): "vale"}[("a", 1)])
"""),

md("""
Cuatro contenedores escritos con las mismas frutas, y el conjunto ya devolvió tres.

El conjunto no guarda repetidos. Eso no es un error, es su definición, y es exactamente por lo que
sirve: preguntar si algo está adentro le sale inmediato porque no guarda un montón de copias del mismo
dato.

Las tres preguntas que eligen el contenedor, en este orden:

1. **¿Importa el orden?** Si sí, lista o tupla.
2. **¿Va a cambiar?** Si no, tupla.
3. **¿Se busca por llave?** Si sí, diccionario. Si solo se pregunta si está, conjunto.

## Lo que cuesta preguntar "¿está adentro?"
"""),

code("""
# FALLA A PROPÓSITO, y no truena. Buscar en una lista lo que un conjunto contesta de inmediato.
import time

MATRICULAS = [f"A{n:06d}" for n in range(200_000)]
COMO_CONJUNTO = set(MATRICULAS)
BUSCADA = "A199999"          # la última, que es el peor caso de la lista

inicio = time.perf_counter()
for _ in range(20):
    BUSCADA in MATRICULAS
con_lista = time.perf_counter() - inicio

inicio = time.perf_counter()
for _ in range(20):
    BUSCADA in COMO_CONJUNTO
con_conjunto = time.perf_counter() - inicio

print("Los dos contestan lo mismo:", BUSCADA in MATRICULAS, BUSCADA in COMO_CONJUNTO)
print()
print(f"20 búsquedas en la lista:    {con_lista:.4f} s")
print(f"20 búsquedas en el conjunto: {con_conjunto:.6f} s")
print(f"La lista tardó unas {con_lista / con_conjunto:,.0f} veces más.")
"""),

md("""
La misma respuesta, el mismo `in`, y una diferencia de cientos de veces que la celda acaba de medir en
tu propia sesión.

`x in lista` recorre la lista de principio a fin comparando uno por uno. Si el dato está al final, o si
no está, recorre los doscientos mil. `x in conjunto` calcula el lugar donde ese valor tendría que estar y
mira ahí nada más.

Es el error 03 de la diapositiva y es el único de la sesión que no se ve leyendo el código. La línea es
idéntica en los dos casos. Lo que cambia es qué se escribió tres pantallas antes.

**Regla:** si una colección solo existe para preguntarle si algo está adentro, se guarda como conjunto.

## El signo igual no copia
"""),

code("""
# FALLA A PROPÓSITO, y no truena. Dos nombres, un solo objeto.
numeros = [1, 2, 3, 4]
copia = numeros

copia.append(5)

print("numeros:", numeros)
print("copia:  ", copia)
print()
print("¿Son iguales?", numeros == copia)
print("¿Son el mismo objeto?", numeros is copia)
print("Dirección de numeros:", id(numeros))
print("Dirección de copia:  ", id(copia))
print()
de_verdad = numeros.copy()
de_verdad.append(6)
print("Con .copy():")
print("  numeros:", numeros)
print("  de_verdad:", de_verdad)
print("  ¿el mismo objeto?", numeros is de_verdad)
"""),

md("""
`copia = numeros` no copió nada. Le puso un segundo nombre a la misma lista.

`==` pregunta si el contenido es igual. `is` pregunta si es el mismo objeto, y esa es la pregunta que
importa aquí: `id()` devuelve el mismo número para los dos nombres.

Es el error 02 de la diapositiva. `Code012.py`, en la línea 109, lo dice con estas palabras: *"You cannot
copy a list simply by typing list2 = list1"*, y se arregla pidiendo la copia, con `.copy()` o con
`list(...)`.

Lo mismo pasa cuando una lista viaja como argumento: la función recibe el nombre, no una copia, y lo que
le haga adentro se ve afuera. Ese fue el problema de la lista por omisión de la semana 9, visto desde el
otro lado.

## Predice antes de correr

```python
alumnos = ["Ana", "Luis", "Sofía", "Marco", "Paula", "Rubén"]

for alumno in alumnos:
    if alumno.startswith(("L", "S", "M")):
        alumnos.remove(alumno)

print(alumnos)
```

- **A.** `['Ana', 'Paula', 'Rubén']`, el ciclo quitó a los tres.
- **B.** `['Ana', 'Sofía', 'Paula', 'Rubén']`, se saltó a uno.
- **C.** `[]`, el ciclo vació la lista.
- **D.** `RuntimeError`, la lista cambió de tamaño mientras se recorría.
"""),

code("""
# FALLA A PROPÓSITO, y no truena. Borrar dentro del for que recorre la lista.
alumnos = ["Ana", "Luis", "Sofía", "Marco", "Paula", "Rubén"]

visitados = []
for alumno in alumnos:
    visitados.append(alumno)
    if alumno.startswith(("L", "S", "M")):
        alumnos.remove(alumno)

print("Quedó:", alumnos)
print("El ciclo miró:", visitados, "<-", len(visitados), "de 6")
print()
print("¿Se fueron los tres?", not any(a[0] in "LSM" for a in alumnos))
print()

alumnos = ["Ana", "Luis", "Sofía", "Marco", "Paula", "Rubén"]
alumnos = [a for a in alumnos if not a.startswith(("L", "S", "M"))]
print("Con una comprensión:", alumnos)
"""),

md("""
La respuesta es **B**.

El `for` lleva un índice por dentro que avanza de uno en uno. Cuando `remove` saca a `Luis` de la
posición 1, `Sofía` se recorre a la posición 1, pero el índice ya va en la 2, así que `Sofía` no se
mira nunca. Por eso el ciclo solo visitó cuatro de los seis nombres.

Ninguna excepción. Ninguna advertencia. Una lista más corta que se ve perfectamente razonable.

Es el error 01 de la diapositiva y es el más caro de la sesión, porque el síntoma aparece lejos: el
programa sigue, y el dato que sobra reaparece tres funciones después.

**La corrección es no borrar mientras recorres.** Se construye una lista nueva con lo que sí se queda,
que además dice en una línea lo que el ciclo decía en cuatro.

## Lo que un conjunto tira sin avisar
"""),

code("""
# FALLA A PROPÓSITO, y no truena. Un conjunto para quitar repetidos, y el orden se va con ellos.
CAPTURAS = ["A001", "A004", "A002", "A001", "A003", "A002"]

sin_repetir = set(CAPTURAS)
print("Capturas:", CAPTURAS, f"({len(CAPTURAS)})")
print("Conjunto:", sin_repetir, f"({len(sin_repetir)})")
print()
print("Primer capturado según la lista:    ", CAPTURAS[0])
print("Primer elemento del conjunto:       ", next(iter(sin_repetir)))
print("¿El conjunto conserva el orden?", list(sin_repetir) == ["A001", "A004", "A002", "A003"])
print()
en_orden = list(dict.fromkeys(CAPTURAS))
print("Sin repetir y en orden:", en_orden)
"""),

md("""
El conjunto quitó los repetidos y de paso tiró el orden en que llegaron.

Eso está bien mientras a nadie le importe el orden. El problema es cuando sí importaba y nadie lo dijo:
la colección se ve limpia, tiene el número correcto de elementos, y el primero ya no es el primero.

`dict.fromkeys` sirve de truco porque los diccionarios de Python sí conservan el orden de inserción y
tampoco aceptan llaves repetidas. Quita duplicados y respeta quién llegó antes.

## La tupla que no se puede corregir
"""),

code("""
# FALLA A PROPÓSITO. Una tupla para un dato que sí cambia.
alumno = ("A001", "Ana Robles", 9.2)

try:
    alumno[2] = 9.5
except TypeError as e:
    print("TypeError:", e)

print()
alumno = alumno[:2] + (9.5,)          # hay que armar la tupla entera otra vez
print("Corregido a mano:", alumno)
print()
como_lista = ["A001", "Ana Robles", 9.2]
como_lista[2] = 9.5
print("Con lista:", como_lista)
print()
print("Y aun así la tupla sirve para algo que la lista no:")
CALIFICACIONES = {("A001", "COM102"): 9.5, ("A002", "COM102"): 7.8}
print("  llave compuesta:", CALIFICACIONES[("A001", "COM102")])
try:
    {["A001", "COM102"]: 9.5}
except TypeError as e:
    print("  con lista de llave:", e)
"""),

md("""
`'tuple' object does not support item assignment`.

Es el error 04 de la diapositiva. Una tupla para una calificación obliga a reconstruir el registro
completo cada vez que alguien corrige un decimal, y la corrección se ve fea justamente porque el
contenedor estaba mal elegido.

La segunda mitad enseña lo contrario, que es la razón de que las tuplas existan: **una lista no puede
ser llave de un diccionario y una tupla sí**. La razón es la misma inmutabilidad. Una llave que puede
cambiar después de guardarse dejaría el diccionario buscando en el lugar equivocado.
"""),

md("""
---
# Bloque 2 · Arreglos dinámicos

Una lista de Python no es una fila de casillas del tamaño exacto. Es un bloque de memoria con hueco de
sobra, que se muda a uno más grande cuando se llena.

Eso no es un detalle de trivia. Explica por qué `append` sale casi gratis y por qué `insert(0, x)` no.
"""),

code("""
from sys import getsizeof

lista = []
anterior = getsizeof(lista)
print(f"{'largo':>6}{'bytes':>8}{'se mudó':>10}")
print(f"{0:>6}{anterior:>8}{'':>10}")

for n in range(1, 40):
    lista.append(n)
    ahora = getsizeof(lista)
    if ahora != anterior:
        print(f"{n:>6}{ahora:>8}{'sí':>10}")
        anterior = ahora

print()
print("Largo final:", len(lista), " bytes:", getsizeof(lista))
print("Bytes por elemento si estuviera justo:", 8, "(una referencia)")
print("Bytes que sobran ahora mismo:", getsizeof(lista) - getsizeof([]) - 8 * len(lista))
"""),

md("""
La lista no crece de uno en uno. Se queda igual varias veces seguidas y de pronto pega un salto.

Ese salto es la mudanza: cuando el hueco reservado se acaba, Python pide un bloque mayor, copia lo que
había y sigue. Como el bloque nuevo trae de sobra, los siguientes `append` no cuestan nada, y por eso el
costo de la copia se reparte entre muchas llamadas baratas.

Eso es un **arreglo dinámico**, y es el nombre técnico de lo que has estado usando desde el primer día.

## Agregar al final contra agregar al principio
"""),

code("""
import time

N = 40_000

inicio = time.perf_counter()
al_final = []
for i in range(N):
    al_final.append(i)
costo_final = time.perf_counter() - inicio

inicio = time.perf_counter()
al_principio = []
for i in range(N):
    al_principio.insert(0, i)
costo_principio = time.perf_counter() - inicio

print(f"{N:,} append(x):     {costo_final:.4f} s")
print(f"{N:,} insert(0, x):  {costo_principio:.4f} s")
print(f"Insertar al principio tardó unas {costo_principio / costo_final:,.0f} veces más.")
print()
print("Las dos listas tienen el mismo largo:", len(al_final) == len(al_principio))
print("Y contenido opuesto:", al_final[:3], "contra", al_principio[:3])
"""),

md("""
El mismo número de inserciones, el mismo resultado en largo, y una diferencia enorme en tiempo.

`append` escribe en el primer hueco libre del final. `insert(0, x)` tiene que correr un lugar a la
derecha **todos** los elementos que ya estaban, para hacerle sitio al nuevo. Con cuarenta mil elementos
eso son ochocientos millones de movimientos repartidos en el ciclo.

Si de verdad necesitas meter y sacar por los dos extremos, la biblioteca estándar trae `deque`, que
`Code017.py` usa al final para su ejemplo de cola.

## Cuando todos los datos son del mismo tipo
"""),

code("""
import array

# Code016.py, líneas 26 a 51, tal cual
array1 = array.array('i', [1, 2, 3, 4, 5])
array1.append(6)
print(array1)
array1.insert(0, 0)
print(array1)
array1.pop(0)
print(array1)
array1.remove(6)
print(array1)
print(array1[0])

print()
print("Tamaño de cada casilla, en bytes:", array1.itemsize)
mil_lista = list(range(1000))
mil_arreglo = array.array('i', range(1000))
print("1000 enteros en una lista:  ", getsizeof(mil_lista), "bytes")
print("1000 enteros en un array:   ", getsizeof(mil_arreglo), "bytes")
print(f"El arreglo ocupa como {getsizeof(mil_arreglo) / getsizeof(mil_lista):.0%} de lo que ocupa la lista.")
"""),

md("""
`Code016.py` corre completo y sus cinco salidas coinciden con lo que dicen sus comentarios.

La diferencia de memoria sale de lo que guarda cada uno. La lista guarda **referencias**: ocho bytes por
casilla que apuntan a un objeto entero que vive en otra parte. El `array` guarda los números, cuatro
bytes cada uno, pegados.

Por eso el `array` es más chico y por eso solo acepta un tipo. Y por eso, para el noventa por ciento de
lo que vas a escribir, la lista es la respuesta: la memoria empieza a importar cuando son millones.
"""),

code("""
# FALLA A PROPÓSITO. La línea 55 de Code016.py, que el archivo dejó comentada.
import array

array1 = array.array('i', [1, 2, 3, 4, 5])

try:
    array1.append("7")
except TypeError as e:
    print("TypeError:", e)

print()
print("El arreglo quedó intacto:", array1)
print()
mezclada = [1, "dos", 3.0, True, None]
print("Y una lista acepta la mezcla sin decir nada:", mezclada)
print("Tipos adentro:", [type(x).__name__ for x in mezclada])
"""),

md("""
`Code016.py` deja esa línea comentada en su línea 55, con el mensaje del error escrito al lado: *"an
integer is required (got type str)"*. Corrida de verdad, hoy dice otra cosa.

Es el mismo asunto de los dos números de `getsizeof`, y ahora con un texto en lugar de un número: **el
mensaje de una excepción no es parte del contrato**. Puede cambiar entre versiones de Python sin previo
aviso, y por eso los `except` se escriben por tipo y nunca comparando la cadena del mensaje.

Que el `array` se queje es la mitad útil del asunto. **El contenedor que restringe atrapa el error en la
línea que lo causó.** La lista de abajo acepta cinco tipos distintos sin protestar, y si eso era un
descuido, se descubre mucho después, cuando alguien intente sumarlos.
"""),

md("""
---
# Bloque 3 · Procesamiento de datos en memoria

Filtrar, transformar y agrupar antes de que nada toque el disco. La semana que entra ya habrá archivos y
esto va a seguir siendo lo mismo, con una lectura enfrente.
"""),

code("""
# Code017.py, líneas 147 a 208: el mismo filtro escrito de tres maneras
products = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12),
]

filtered = []
for product in products:
    if product[1] >= 10:
        filtered.append(product)
print("Con for:        ", filtered)

filtered = list(filter(lambda product: product[1] >= 10, products))
print("Con filter:     ", filtered)

filtered = [product for product in products if product[1] >= 10]
print("Con comprensión:", filtered)

print()
alumnos = [{"nombre": "Ana", "nota": 9.1}, {"nombre": "Luis", "nota": 6.4},
           {"nombre": "Sofía", "nota": 8.0}]
aprobados = [a["nombre"] for a in alumnos if a["nota"] >= 7]
print("Aprobados:", aprobados)
print("Notas:    ", [a["nota"] for a in alumnos])
print("Escaladas:", [round(a["nota"] * 10) for a in alumnos])
"""),

md("""
Tres escrituras del mismo filtro y una sola respuesta.

Una comprensión se lee de izquierda a derecha en tres tiempos: **qué guardo**, **de dónde sale**, **con
qué condición**. Reemplaza al `for` de cuatro líneas con el `append` adentro, que es exactamente el
patrón que `Code017.py` enseña primero y luego reescribe.

`filter` y `map` hacen lo mismo y hoy casi nadie los usa para esto, porque la comprensión dice la
condición en el mismo renglón y no obliga a leer una `lambda`.

**Cuándo no usarla:** si necesita dos condiciones y un `else`, el `for` de siempre se lee mejor.

## El generador que solo sirve una vez
"""),

code("""
# FALLA A PROPÓSITO, y no truena. Recorrer dos veces algo que solo se recorre una.
NOTAS = [9.1, 6.4, 8.0, 7.5, 5.9]

cuadrados = (n * n for n in NOTAS)

primera = list(cuadrados)
segunda = list(cuadrados)

print("Primera pasada:", [round(x, 2) for x in primera])
print("Segunda pasada:", segunda, "<- vacía, y nadie avisó")
print()

aprobadas = (n for n in NOTAS if n >= 7)
print("¿Cuántas aprobadas?", sum(1 for _ in aprobadas))
print("¿Y el promedio de esas?", "no se puede, ya se consumió:", list(aprobadas))
print()
como_lista = [n for n in NOTAS if n >= 7]
print("Con lista, las veces que quieras:", len(como_lista), "y promedio",
      round(sum(como_lista) / len(como_lista), 2))
"""),

md("""
La segunda pasada devolvió una lista vacía y el programa siguió como si nada.

Un generador no guarda los valores, los produce mientras lo recorres. Cuando llega al final se queda
ahí, y volver a recorrerlo no reinicia nada: entrega cero elementos. `sum` sobre un generador ya gastado
da cero, y ese cero dividido entre un conteo que salió de otra parte produce un promedio de cero que se
ve como un dato de verdad.

Esa es la diferencia real con una comprensión, y no la sintaxis. El paréntesis contra el corchete es el
síntoma; el fondo es que **uno guarda y el otro produce**.

## Los números que envejecieron dentro de un comentario
"""),

code("""
# FALLA A PROPÓSITO, y no truena. Dos números escritos a mano en Code017.py.
from sys import getsizeof
import sys

values_gen = (x * 2 for x in range(100000))
values_com = [x * 2 for x in range(100000)]

print("Lo que dice Code017.py en sus líneas 257 y 261:")
print("   gen: 112")
print("   com: 824456")
print()
print("Lo que mide esta sesión, con", f"Python {sys.version_info.major}.{sys.version_info.minor}:")
print("   gen:", getsizeof(values_gen))
print("   com:", getsizeof(values_com))
print()
print("¿Coinciden?", getsizeof(values_gen) == 112 and getsizeof(values_com) == 824456)
print("¿Sigue siendo cierto lo que el archivo quería enseñar?",
      getsizeof(values_gen) < getsizeof(values_com) / 100)
"""),

md("""
Los dos números del comentario ya no son los de hoy, y la conclusión del archivo sigue siendo correcta.

`getsizeof` mide la representación interna de un objeto, y esa representación cambia entre versiones de
Python. El comentario congeló la medición del día en que se escribió el archivo; la línea de código, en
cambio, la vuelve a hacer cada vez que corre.

De ahí sale una regla que vale para todo el semestre: **un número escrito en un comentario se pudre y un
número medido no.** Cuando el número importa, la línea que lo produce va en el programa.

Fíjate también en la última comparación. Lo que el archivo enseñaba —que un generador ocupa una
fracción minúscula de lo que ocupa la lista— se sostiene sin depender de los dos valores exactos. Esa es
la manera de escribir una afirmación que dure.

## Agrupar con un diccionario acumulador
"""),

code("""
CAPTURAS = [
    {"alumno": "Ana", "materia": "COM102", "nota": 9.1},
    {"alumno": "Luis", "materia": "COM102", "nota": 6.4},
    {"alumno": "Sofía", "materia": "COM101", "nota": 8.0},
    {"alumno": "Marco", "materia": "COM101", "nota": 5.5},
    {"alumno": "Paula", "materia": "COM102", "nota": 7.2},
]

conteo = {}
for c in CAPTURAS:
    clave = "aprobado" if c["nota"] >= 7 else "reprobado"
    conteo[clave] = conteo.get(clave, 0) + 1

print("Conteo:", conteo)

por_materia = {}
for c in CAPTURAS:
    por_materia.setdefault(c["materia"], []).append(c["nota"])

print("Agrupado:", por_materia)
print()
for materia, notas in por_materia.items():
    print(f"  {materia}  n={len(notas)}  promedio={sum(notas) / len(notas):.2f}")

print()
print("Las cinco capturas siguen contadas:",
      sum(len(v) for v in por_materia.values()) == len(CAPTURAS))
"""),

md("""
Dos patrones que vas a escribir el resto del semestre.

`conteo.get(clave, 0) + 1` resuelve el problema de la primera vez: la llave todavía no existe y `get`
devuelve el valor por omisión en lugar de lanzar `KeyError`.

`setdefault(clave, []).append(...)` hace lo mismo para agrupar: si la llave no está, la crea con una
lista vacía, y en cualquier caso devuelve la lista para agregarle.

Fíjate en la última línea. **Después de agrupar, la suma de los grupos tiene que dar el total de
entrada.** Es la comprobación más barata que existe y atrapa la mitad de los errores de agrupación.

## El desempaquetado que detiene el archivo
"""),

code("""
# FALLA A PROPÓSITO. Code017.py, línea 292. El archivo se detiene aquí.
numbers = [1, 2, 3]
new_numbers = [4, 5, 6]

numbers.append(new_numbers)
print("Sin desempaquetar:", numbers, "<- la línea 285, que sí corre")

numbers = [1, 2, 3]
new_numbers = [4, 5, 6]

try:
    numbers.append(*new_numbers)          # la línea 292
except TypeError as e:
    print()
    print("TypeError:", e)

print()
print("La lista quedó como estaba:", numbers)
print("El comentario de la línea 293 anuncia:  [1, 2, 3, 4, 5, 6]")
"""),

md("""
`list.append() takes exactly one argument (3 given)`.

El asterisco **desempaqueta**: convierte `[4, 5, 6]` en tres argumentos sueltos. `print(*numbers)` de la
línea 276 funciona porque `print` acepta cuantos le lleguen. `append` acepta exactamente uno, así que
recibir tres es un error de firma, no de tipo.

El método que sí junta dos listas es `extend`, o el `+` de siempre, o el desempaquetado dentro de un
literal, que es lo que el propio archivo escribe tres líneas más abajo.

Lo importante no es la línea. Es lo que la línea se lleva por delante.
"""),

code("""
LINEAS_DEL_ARCHIVO = 390
SE_DETIENE_EN = 292
muertas = LINEAS_DEL_ARCHIVO - SE_DETIENE_EN

print("Code017.py tiene", LINEAS_DEL_ARCHIVO, "líneas.")
print("Se detiene en la", SE_DETIENE_EN)
print("Nunca se ejecutan:", muertas, "líneas, o sea el",
      f"{muertas / LINEAS_DEL_ARCHIVO:.0%}", "del archivo.")
print()
print("Lo que queda del otro lado del error:")
for tema, linea in [("desempaquetado dentro de un literal", 301),
                    ("desempaquetado de diccionarios", 317),
                    ("zip de dos listas", 336),
                    ("zip con listas de distinto largo", 346),
                    ("pila con append y pop", 357),
                    ("cola con deque y popleft", 380)]:
    print(f"  línea {linea:>4}  {tema}")
"""),

md("""
Noventa y ocho líneas que el archivo escribió, comentó y nunca corrió.

Esto es lo que hace que un error temprano cueste más de lo que parece: no rompe una línea, **corta el
archivo en dos**. Todo lo que estaba después quedó sin probar, y los comentarios que anuncian su salida
son predicciones que nadie verificó.

El resto de este bloque revive ese tramo, celda por celda, y comprueba cada predicción.

## El tramo que no se ejecutaba, corrido
"""),

code("""
# Code017.py, líneas 299 a 318, ahora sí
numbers = [1, 2, 3]
new_numbers = [4, 5, 6]
numbers = [*numbers, *new_numbers]
print(numbers)
print("¿Coincide con su comentario [1, 2, 3, 4, 5, 6]?", numbers == [1, 2, 3, 4, 5, 6])

print()
numbers = [1, 2, 3]
new_numbers = [4, 5, 6]
numbers = [*numbers, "a", *new_numbers, *"hello"]
print(numbers)

print()
first = {"x": 1}
second = {"x": 10, "y": 2}
combined = {**first, **second, "z": 1}
print(combined)
print("La x quedó en", combined["x"], "porque el segundo diccionario pisó al primero.")
"""),

md("""
Las tres predicciones eran correctas. Nadie lo sabía, porque nadie llegó hasta aquí.

La tercera línea merece un segundo. `{**first, **second}` mezcla dos diccionarios y, cuando los dos
traen la misma llave, **gana el último**. Eso no truena y casi nunca se documenta, así que conviene
saberlo antes de mezclar la configuración por omisión con la del usuario y preguntarse por qué se perdió
un valor.

## `zip` y el corte silencioso
"""),

code("""
# FALLA A PROPÓSITO, y no truena. zip se detiene con la lista más corta.
nombres = ["Ana", "Luis", "Sofía", "Marco", "Paula"]
notas = [9.1, 6.4, 8.0]

pares = list(zip(nombres, notas))

print("Nombres:", len(nombres))
print("Notas:  ", len(notas))
print("Pares:  ", len(pares), "<- se perdieron", len(nombres) - len(pares))
print()
for nombre, nota in pares:
    print(f"  {nombre:<8}{nota}")
print()
print("Marco y Paula desaparecieron del reporte sin una sola advertencia.")
print()
try:
    list(zip(nombres, notas, strict=True))
except ValueError as e:
    print("Con strict=True:", e)
"""),

md("""
Cinco alumnos entran, tres salen, y el reporte se ve completo.

`zip` se detiene con la más corta. Es el comportamiento documentado y es útil cuando de verdad quieres
recorrer en paralelo hasta donde alcance, pero cuando las dos listas *deberían* medir lo mismo, ese corte
es una pérdida de datos silenciosa.

`strict=True` convierte el silencio en un `ValueError`. Existe desde Python 3.10 y es la clase de bandera
que conviene poner siempre que las longitudes tengan que coincidir.

Es el mismo problema de las listas paralelas de la semana 2, ahora con la herramienta que se supone que
lo resuelve.

## La pila, la cola, y una comprobación al revés
"""),

code("""
from collections import deque

# Pila: lo último que entra es lo primero que sale
browsing_session = []
browsing_session.append("inicio")
browsing_session.append("cursos")
browsing_session.append("com102")
print("Pila:", browsing_session)
print("Atrás:", browsing_session.pop())
print("Pila:", browsing_session)

print()
# Cola: lo primero que entra es lo primero que sale
queue = deque([])
queue.append("doc1")
queue.append("doc2")
queue.append("doc3")
print("Cola:", queue)
print("Se imprime:", queue.popleft())
print("Cola:", queue)
"""),

code("""
# FALLA A PROPÓSITO, y no truena. Code017.py, líneas 366 a 369.
browsing_session = ["inicio", "cursos"]

# El comentario del archivo dice: "To avoid getting an error when popping an
# empty stack, you can check if the stack is empty before popping"
if not browsing_session:
    browsing_session.pop()

print("Con la pila llena no pasa nada:", browsing_session)
print("Y por eso el archivo nunca se enteró.")
print()

browsing_session = []
try:
    if not browsing_session:
        browsing_session.pop()
except IndexError as e:
    print("Con la pila vacía:", type(e).__name__ + ":", e)

print()
browsing_session = []
if browsing_session:                      # sin el not
    print("saco:", browsing_session.pop())
else:
    print("Con la condición al derecho: la pila está vacía, no saco nada.")
"""),

md("""
La condición está invertida y hace exactamente lo contrario de lo que su comentario promete.

`if not browsing_session` es verdadero **cuando la pila está vacía**, y adentro llama a `pop`. Es la
única situación en la que `pop` truena, y es justo la que el comentario dice que quiere evitar.

Con la pila llena la condición es falsa, el `pop` no corre, y todo parece bien. Por eso el archivo
convive con el error: nunca lo alcanza. Es la misma lección de la celda del `for` que borra: **un error
que no se dispara sigue siendo un error, y lo que decide si se dispara son los datos de ese día.**

En `Code017.py` este bloque vive después de la línea 292, así que ni siquiera llegaba a no dispararse.

## Una función que tapó a una de Python
"""),

code("""
# FALLA A PROPÓSITO, y no truena. Code017.py, línea 12.
def sum(*numbers: tuple) -> int:
    total = 0
    for number in numbers:
        total += number
    return total


print("Con la del archivo:", sum(1, 2, 3, 4, 5))

try:
    print(sum([1, 2, 3, 4, 5]))
except TypeError as e:
    print("Y con una lista:", e)

print()
del sum
print("Con la de Python:  ", sum([1, 2, 3, 4, 5]))
print("Y con argumentos sueltos:")
try:
    sum(1, 2, 3, 4, 5)
except TypeError as e:
    print("  ", e)
"""),

md("""
Dos funciones con el mismo nombre y firmas incompatibles.

`Code017.py` define `sum` en su línea 12 y con eso tapa la de Python para todo lo que venga después en
ese archivo. La del archivo recibe números sueltos; la de Python recibe un iterable. Cambiar de una a
otra rompe todas las llamadas.

El archivo se salva porque no vuelve a usar `sum` en ningún lado. Un programa más largo no se salva: se
descubre cuando alguien escribe `sum(notas)` doscientas líneas después y recibe un `TypeError` que no
tiene ningún sentido con la documentación abierta.

**Regla:** antes de nombrar una función, teclea el nombre en una celda. Si Python te contesta con algo,
el nombre está ocupado.
"""),

md("""
---
## Cuatro errores de esta sesión

**Borrar de una lista mientras se recorre.** El índice del `for` avanza aunque la lista se encoja, así
que el ciclo se salta elementos. Se arregla construyendo una lista nueva.

**Copiar con el signo igual.** `copia = lista` deja dos nombres sobre el mismo objeto. `is` e `id()` lo
demuestran en dos líneas.

**Usar una lista para buscar.** `x in lista` recorre todo. Un conjunto contesta de inmediato y la línea
que lo pregunta se escribe igual.

**Tuplas para datos que cambian.** Corregir un dato obliga a construir la tupla entera otra vez. La
inmutabilidad se elige cuando es una ventaja, no por costumbre.
"""),

md("""
---
# Ejercicios

El laboratorio de esta semana es elegir el contenedor correcto para cinco consultas sobre un padrón. Los
ejercicios construyen hacia eso.

Las soluciones están hasta abajo del cuaderno.

### Ejercicio 1 · Las tres preguntas

Escribe los mismos seis datos como lista, tupla, conjunto y diccionario. Para cada uno imprime cuántos
elementos quedaron y explica en un comentario qué se perdió.

### Ejercicio 2 · Buscar en la colección que toca

Arma una lista de cincuenta mil matrículas y un conjunto con las mismas. Mide con `time.perf_counter`
cuánto tarda cada uno en contestar `in` para una matrícula que no existe.

Explica en un comentario por qué el peor caso de la lista es el dato ausente.

### Ejercicio 3 · Copiar contra compartir

Escribe una función que reciba una lista y le agregue un elemento. Llámala y muestra que la lista de
afuera cambió. Después escribe la versión que no toca la original.

Comprueba las dos con `is`.

### Ejercicio 4 · El ciclo que se salta

Toma una lista de ocho nombres y borra dentro del `for` los que empiecen con vocal. Imprime cuántos
visitó el ciclo y cuántos quedaron.

Reescríbelo con una comprensión y comprueba que ahora sí se fueron todos.

### Ejercicio 5 · Cómo crece

Agrega mil elementos a una lista e imprime `getsizeof` cada vez que el número cambie. Cuenta cuántas
mudanzas hubo.

Explica en un comentario por qué son tan pocas.

### Ejercicio 6 · El generador de una sola pasada

Crea un generador con una condición, recórrelo dos veces y muestra que la segunda vuelve vacío.
Arréglalo con una comprensión y explica en un comentario cuándo conviene cada uno.

### Ejercicio 7 · Agrupar y comprobar

Toma una lista de veinte capturas con materia y nota. Agrúpalas por materia en un diccionario e imprime
el promedio de cada grupo.

Termina comprobando que la suma de los largos de los grupos da veinte.

### Ejercicio 8 · El desempaquetado

Junta dos listas de cuatro maneras: con `extend`, con `+`, con `[*a, *b]` y con `append` desempaquetando.
Atrapa el `TypeError` de la última y explica en un comentario en qué se diferencia de `print(*a)`.

### Ejercicio 9 · El laboratorio

Te entregan un padrón de alumnos con matrícula, nombre, carrera y promedio. Contesta estas cinco
consultas eligiendo un contenedor para cada una y justificando la elección en una línea:

1. Listar a los alumnos en el orden en que se inscribieron.
2. Decir si una matrícula está registrada.
3. Obtener el nombre a partir de la matrícula.
4. Listar las carreras distintas que aparecen.
5. Guardar los cinco promedios más altos, que no vuelven a cambiar.

Usa al menos tres de los cuatro contenedores. El criterio es que ninguna consulta recorra la colección
completa si otro contenedor lo evita.
"""),

md("""
---
## Tres ideas para llevarse

**Tres preguntas eligen el contenedor.** Si importa el orden, si va a cambiar y si se busca por llave. En
ese orden, y ya está.

**La lista es un arreglo dinámico.** Reserva de más y copia cuando se llena, y por eso agregar al final
casi nunca cuesta mientras insertar al principio siempre cuesta.

**El igual no copia, comparte.** Dos nombres sobre la misma lista se ven idénticos hasta que uno de los
dos escribe, y ahí ya es tarde.

La semana 11 sigue con el manejo de excepciones. Seis celdas de este cuaderno atraparon un error con
`try` y `except` sin explicar la sintaxis; la semana que entra empieza justo ahí, con qué es lo que se
levanta, hacia dónde sube y quién decide atenderlo.
"""),

md("""
---
# Soluciones

### Ejercicio 1

```python
DATOS = ["A001", "A004", "A002", "A001", "A003", "A002"]

como_lista = list(DATOS)
como_tupla = tuple(DATOS)
como_conjunto = set(DATOS)
como_dicc = {m: i for i, m in enumerate(DATOS)}

for nombre, c in [("lista", como_lista), ("tupla", como_tupla),
                  ("conjunto", como_conjunto), ("diccionario", como_dicc)]:
    print(f"{nombre:<12}{len(c)}  {c}")

# La lista y la tupla conservan los seis, con repetidos y en orden.
# El conjunto se quedó con cuatro: perdió los repetidos y el orden.
# El diccionario también se quedó con cuatro, porque la llave repetida se
# sobrescribe, pero conserva el orden de inserción y guarda la última posición.
```

### Ejercicio 2

```python
import time

MATRICULAS = [f"A{n:06d}" for n in range(50_000)]
CONJUNTO = set(MATRICULAS)
AUSENTE = "Z999999"

for nombre, coleccion in [("lista", MATRICULAS), ("conjunto", CONJUNTO)]:
    inicio = time.perf_counter()
    for _ in range(50):
        AUSENTE in coleccion
    print(f"{nombre:<12}{time.perf_counter() - inicio:.5f} s")

# El dato ausente es el peor caso de la lista porque para contestar "no está"
# hay que comparar contra los cincuenta mil. Un dato presente puede aparecer al
# principio y cortar el recorrido; uno ausente nunca corta.
```

### Ejercicio 3

```python
def agregar_mal(lista, valor):
    lista.append(valor)
    return lista


def agregar_bien(lista, valor):
    return lista + [valor]


original = [1, 2, 3]
devuelta = agregar_mal(original, 4)
print(original, devuelta, original is devuelta)

original = [1, 2, 3]
devuelta = agregar_bien(original, 4)
print(original, devuelta, original is devuelta)
```

### Ejercicio 4

```python
nombres = ["Ana", "Elena", "Iván", "Luis", "Óscar", "Ubaldo", "Sofía", "Marco"]

visitados = []
copia = list(nombres)
for n in copia:
    visitados.append(n)
    if n[0] in "AEIOUÁÉÍÓÚ":
        copia.remove(n)

print("Visitó:", len(visitados), "de", len(nombres))
print("Quedó:", copia)

limpio = [n for n in nombres if n[0] not in "AEIOUÁÉÍÓÚ"]
print("Con comprensión:", limpio)
print("¿Se fueron todos?", all(n[0] not in "AEIOUÁÉÍÓÚ" for n in limpio))
```

### Ejercicio 5

```python
from sys import getsizeof

lista = []
anterior = getsizeof(lista)
mudanzas = 0
for n in range(1000):
    lista.append(n)
    ahora = getsizeof(lista)
    if ahora != anterior:
        mudanzas += 1
        anterior = ahora

print("Mudanzas para llegar a 1000:", mudanzas)

# Son pocas porque cada bloque nuevo es proporcionalmente más grande que el
# anterior, no una casilla más. Con mil elementos caben en torno a veinte
# mudanzas, y con un millón no llegan a cincuenta.
```

### Ejercicio 6

```python
NOTAS = [9.1, 6.4, 8.0, 7.5, 5.9]

gen = (n for n in NOTAS if n >= 7)
print("Primera:", list(gen))
print("Segunda:", list(gen))

lista = [n for n in NOTAS if n >= 7]
print("Primera:", lista)
print("Segunda:", lista)

# El generador conviene cuando los datos no caben en memoria o cuando solo se
# van a recorrer una vez. La comprensión conviene en cuanto haya que recorrer
# dos veces, medir el largo o indexar.
```

### Ejercicio 7

```python
import random

rng = random.Random(2026)
MATERIAS = ["COM101", "COM102", "COM103"]
CAPTURAS = [{"materia": rng.choice(MATERIAS), "nota": round(rng.uniform(5, 10), 1)}
            for _ in range(20)]

por_materia = {}
for c in CAPTURAS:
    por_materia.setdefault(c["materia"], []).append(c["nota"])

for materia, notas in sorted(por_materia.items()):
    print(f"{materia}  n={len(notas):<4}promedio={sum(notas) / len(notas):.2f}")

print("¿Se contaron todas?",
      sum(len(v) for v in por_materia.values()) == len(CAPTURAS))
```

### Ejercicio 8

```python
a = [1, 2, 3]
b = [4, 5, 6]

con_extend = list(a)
con_extend.extend(b)
print(con_extend)

print(a + b)
print([*a, *b])

try:
    lista = list(a)
    lista.append(*b)
except TypeError as e:
    print("TypeError:", e)

# print(*a) funciona porque print acepta cuantos argumentos le lleguen.
# append acepta exactamente uno, así que desempaquetar tres es un error de
# firma. El asterisco no junta listas: reparte una lista en argumentos sueltos.
```

### Ejercicio 9

```python
PADRON = [
    {"matricula": "A001", "nombre": "Ana Robles", "carrera": "Mecatrónica", "promedio": 9.2},
    {"matricula": "A002", "nombre": "Luis Ferrer", "carrera": "Industrial", "promedio": 7.8},
    {"matricula": "A003", "nombre": "Sofía Ines", "carrera": "Mecatrónica", "promedio": 9.5},
    {"matricula": "A004", "nombre": "Marco Duarte", "carrera": "Civil", "promedio": 6.4},
    {"matricula": "A005", "nombre": "Paula Lara", "carrera": "Industrial", "promedio": 8.7},
]

# 1. En orden de inscripción -> lista. Es el único contenedor que conserva el
#    orden y admite recorrerlo entero, que es justo lo que pide la consulta.
inscritos = [a["nombre"] for a in PADRON]
print(inscritos)

# 2. ¿Está registrada? -> conjunto. Solo se pregunta pertenencia y contesta sin
#    recorrer.
REGISTRADAS = {a["matricula"] for a in PADRON}
print("A003" in REGISTRADAS, "Z999" in REGISTRADAS)

# 3. Nombre a partir de la matrícula -> diccionario. Es una búsqueda por llave.
POR_MATRICULA = {a["matricula"]: a["nombre"] for a in PADRON}
print(POR_MATRICULA["A003"])

# 4. Carreras distintas -> conjunto. El requisito es "distintas", que es su
#    definición.
print(sorted({a["carrera"] for a in PADRON}))

# 5. Los cinco más altos, que ya no cambian -> tupla. Se calcula una vez y la
#    inmutabilidad documenta que el corte quedó cerrado.
TOP = tuple(sorted(PADRON, key=lambda a: a["promedio"], reverse=True)[:5])
print([a["nombre"] for a in TOP])
```

Tres decisiones que vale la pena defender en la entrega.

**Ninguna consulta recorre el padrón completo salvo la primera**, que necesita recorrerlo por
definición. Las otras cuatro se apoyan en un contenedor construido una sola vez.

**Los contenedores auxiliares se construyen una vez y se reutilizan.** Si `REGISTRADAS` se armara dentro
de la consulta, la consulta volvería a recorrer el padrón y el conjunto no habría servido de nada.

**La tupla del punto 5 no es adorno.** Dice, en el tipo, que ese corte ya no admite correcciones. Es la
única de las cinco donde la inmutabilidad aporta algo.
"""),

]

write(OUT / "es" / "w10.ipynb", es)
print("wrote", OUT / "es" / "w10.ipynb")
