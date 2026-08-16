"""notebooks/programacion-orientada-a-objetos/es/w01.4.ipynb

Source deck: ppts/python/programacion-orientada-a-objetos/es/w01.4.es.yaml
Source code:  docs/en/courses/python-course/01 - Basics/4th Module/
              Code012.py, Code013.py, Code014.py, Code015.py

Code013.py no corre: la línea 31 llama a tuple.extend. El cuaderno lo enseña
como trampa en lugar de citarlo como si funcionara. Lo mismo con la línea 50
(tuple.copy), la 117 (tuple.clear) y la afirmación falsa de las líneas 46 y 47.
Code014.py línea 159 imprime False y su comentario dice True.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from nbkit import md, code, write, REPO

OUT = REPO / "notebooks" / "programacion-orientada-a-objetos"

es = [

md("""
# Programación Orientada a Objetos · Repaso 4 de 5
## Módulo 4 · Colecciones

**COM102 · Facultad de Ingeniería · Profesor David Escobar-Castillejos**

Cuatro formas de guardar varias cosas en una sola variable, y cuándo usar cada una.

El repaso 3 terminó con una advertencia: la lista que se pone como valor por defecto de una función
se comparte entre todas las llamadas. Este cuaderno explica por qué. La respuesta es que asignar una
lista no la copia, y esa sola frase es la que en la semana 6 va a explicar por qué dos objetos de la
misma clase terminan viendo los mismos datos.

Al terminar este cuaderno vas a poder:

1. Elegir entre lista, tupla, conjunto y diccionario con tres preguntas.
2. Indexar y rebanar una lista, y decir por qué el último índice es `n - 1`.
3. Usar los métodos de lista sabiendo cuáles modifican y cuáles devuelven.
4. Buscar por llave con `get` en vez de con corchetes cuando el dato puede faltar.
5. Distinguir copiar de renombrar, y demostrar la diferencia con `id`.

### Cómo se usa este cuaderno

Ejecuta las celdas en orden con **Shift + Enter**. Diecinueve fallan a propósito y llevan un
comentario que lo dice.

En diez de esas diecinueve **no aparece ninguna excepción**. Son las que importan: el programa sigue
corriendo, entrega un resultado creíble, y está mal. Dos de las diecinueve reproducen errores que el
archivo del curso trae sin corregir.
"""),

md("""
---
# Bloque 1 · Las cuatro colecciones

Una variable guarda un valor. Cuando lo que necesitas guardar son treinta calificaciones, cuatro
regiones o los datos de un alumno, hace falta un contenedor.

Python trae cuatro, y no son intercambiables. Se eligen contestando tres preguntas:

1. **¿Importa el orden?** Si vas a hablar del "primero" o del "tercero", sí.
2. **¿Va a cambiar después de crearse?** Si nadie debe tocarlo, hay una que lo garantiza.
3. **¿Puede haber repetidos?** Si el repetido es un dato válido, no puedes usar la que los borra.
"""),

code("""
lista = ["café", "filtro", "taza"]
tupla = ("café", "filtro", "taza")
conjunto = {"café", "filtro", "taza"}
diccionario = {"café": 45, "filtro": 12, "taza": 89}

for nombre, valor in [("lista", lista), ("tupla", tupla),
                      ("conjunto", conjunto), ("diccionario", diccionario)]:
    print(f"{nombre:<13}{type(valor).__name__:<7}{len(valor)} elementos   {valor}")
"""),

md("""
Los corchetes hacen una lista, los paréntesis una tupla, y las llaves hacen conjunto o diccionario
según lo que lleven adentro: valores sueltos dan conjunto, pares `llave: valor` dan diccionario.

Un detalle que muerde: `{}` vacío **no** es un conjunto vacío, es un diccionario vacío. El conjunto
vacío se escribe `set()`.

## Las tres preguntas, medidas

La tabla de la diapositiva dice cuál es ordenada, cuál se puede cambiar y cuál admite repetidos. En
lugar de creerle, la celda de abajo lo prueba con las cuatro.
"""),

code("""
import copy as copiar_modulo

CRUDOS = ["a", "b", "a", "c"]        # cuatro elementos, uno repetido

candidatas = [
    ("lista", list(CRUDOS)),
    ("tupla", tuple(CRUDOS)),
    ("conjunto", set(CRUDOS)),
    ("diccionario", dict.fromkeys(CRUDOS, 0)),
]


def acepta_indice_cero(coleccion):
    try:
        coleccion[0]
    except (TypeError, KeyError):
        return "no"
    return "sí"


def acepta_asignacion(coleccion):
    prueba = copiar_modulo.copy(coleccion)
    try:
        prueba[0] = "z"
    except TypeError:
        return "no"
    return "sí"


print(f"{'Colección':<13}{'Elementos':>10}{'[0] lee':>10}{'[0] = z':>10}")
for nombre, valor in candidatas:
    print(f"{nombre:<13}{len(valor):>10}"
          f"{acepta_indice_cero(valor):>10}{acepta_asignacion(valor):>10}")
"""),

md("""
Los cuatro elementos de entrada salieron como cuatro en lista y tupla, y como tres en conjunto y
diccionario. Ese uno que falta es la `"a"` repetida, y desapareció sin que nadie avisara.

Las dos columnas de la derecha dicen "no" en el conjunto y en el diccionario, pero por razones
distintas. El conjunto no tiene posiciones y punto. El diccionario sí acepta corchetes, solo que
adentro va una llave y no una posición, y la llave `0` no existe: por eso leer falla y asignar
funciona, creando una llave nueva.

La tupla es la única de las cuatro que lee sin problema y rechaza la asignación, y esa es su única
diferencia con la lista.

## Los repetidos se van en silencio
"""),

code("""
# FALLA A PROPÓSITO, y no truena. Un conjunto para quitar duplicados que no lo eran.
calificaciones = [8, 9, 8, 10, 9, 8]

unicas = set(calificaciones)

print("Capturadas:", calificaciones, "->", len(calificaciones), "calificaciones")
print("En conjunto:", unicas, "->", len(unicas), "calificaciones")
print()
print(f"Promedio real:         {sum(calificaciones) / len(calificaciones):.2f}")
print(f"Promedio del conjunto: {sum(unicas) / len(unicas):.2f}")
"""),

md("""
Seis calificaciones entraron y tres salieron. El promedio pasó de 8.67 a 9.00, y los dos números son
igual de creíbles.

El conjunto hizo exactamente lo que promete: guardar valores únicos. El problema es que tres alumnos
distintos pueden sacar 8, y ahí el repetido no es basura sino un dato. `set` sirve para preguntar
**qué valores aparecieron**, nunca para contar cuántas veces apareció cada uno.

La misma pérdida ocurre en un diccionario cuando una llave se repite.
"""),

code("""
# FALLA A PROPÓSITO, y no truena. Dos veces la misma llave.
carro = {
    "marca": "Ford",
    "modelo": "Mustang",
    "año": 1964,
    "año": 2020,
}

print(carro)
print("Llaves:", len(carro))
"""),

md("""
El 1964 nunca existió. Python leyó el diccionario de arriba a abajo, guardó `1964` y encima escribió
`2020` antes de que la primera línea de tu programa corriera.

Eso viene del archivo `Code015.py` del curso, y ahí está bien: es el ejemplo de que la última gana.
En un archivo de configuración de doscientas líneas, la misma llave escrita dos veces por descuido
hace exactamente esto y no deja rastro.

## Y hay una versión peor
"""),

code("""
# FALLA A PROPÓSITO, y no truena. Tres llaves que Python considera la misma.
raro = {True: "uno", 1: "otro", 1.0: "tercero"}

print(raro, "· llaves:", len(raro))
print()
print("True == 1 :", True == 1)
print("1 == 1.0  :", 1 == 1.0)
print("hash iguales:", hash(True) == hash(1) == hash(1.0))
"""),

md("""
Tres llaves escritas, una guardada, y el valor que quedó es el último.

Dos llaves son la misma cuando son iguales con `==` y tienen el mismo `hash`. `True`, `1` y `1.0`
cumplen las dos condiciones, porque en Python `bool` es una subclase de `int` y el flotante `1.0`
vale lo mismo que el entero. El diccionario conservó la primera llave que vio, que fue `True`, y le
puso encima el último valor.

Es raro escribirlo así a propósito. Es muy fácil llegar a lo mismo con llaves calculadas, cuando una
viene de un `int` y otra de una división que dio `1.0`.
"""),

md("""
---
# Bloque 2 · Listas

La colección que vas a usar el noventa por ciento de las veces. Ordenada, modificable, y con
repetidos permitidos.

Se indexa igual que una cadena, con todo lo que ya viste en el repaso 1: posiciones desde cero,
índices negativos desde el final, rebanadas y paso.
"""),

code("""
frutas = ["apple", "banana", "cherry", "blackcurrant"]

print("frutas[1]     ", frutas[1])          # banana
print("frutas[-1]    ", frutas[-1])         # el último
print("frutas[1:3]   ", frutas[1:3])        # del 1 al 2, el 3 no entra
print("frutas[:2]    ", frutas[:2])         # desde el principio
print("frutas[1:]    ", frutas[1:])         # hasta el final
print("frutas[-3:-1] ", frutas[-3:-1])      # negativos, misma regla
print("frutas[::2]   ", frutas[::2])        # de dos en dos
print("frutas[::-1]  ", frutas[::-1])       # al revés
print("len(frutas)   ", len(frutas))
"""),

md("""
Una rebanada devuelve **una lista nueva**. La original no se toca, igual que con las cadenas.

El límite derecho nunca entra. `frutas[1:3]` trae dos elementos, no tres, y esa resta es la misma que
hace que `len` sea 4 y el último índice válido sea 3.
"""),

code("""
# FALLA A PROPÓSITO. Cuatro elementos, y el índice 4 no existe.
try:
    print(frutas[4])
except IndexError as e:
    print("IndexError:", e)

# La rebanada, en cambio, no se queja de salirse.
print("frutas[1:99]:", frutas[1:99])
print("frutas[99:] :", frutas[99:])
"""),

md("""
Las dos líneas de abajo son las que sorprenden. Indexar fuera de rango lanza `IndexError`, pero
**rebanar fuera de rango no lanza nada**: recorta hasta donde alcance y, si no alcanza para nada,
devuelve una lista vacía.

Esa asimetría explica un bug común. Un `datos[0]` sobre una lista vacía truena y te dice dónde. Un
`datos[:1]` sobre la misma lista devuelve `[]` y el programa sigue con las manos vacías tres
funciones más adelante.

## Modificar en el lugar
"""),

code("""
frutas = ["apple", "banana", "cherry", "blackcurrant"]

frutas[1] = "blackcurrant"          # esto una cadena no lo permite
print(frutas)

print()
for fruta in frutas:
    print(" -", fruta)

print()
print("¿Está apple?", "apple" in frutas)
print("¿Está mango?", "mango" in frutas)
print("Cuántas blackcurrant:", frutas.count("blackcurrant"))
"""),

md("""
Esta es la diferencia de fondo con las cadenas. `"hola"[0] = "H"` es un `TypeError`, porque una
cadena es inmutable y sus métodos siempre devuelven una copia. Una lista sí acepta la asignación, y
sus métodos casi siempre modifican la que ya tienes.

## Los métodos que cambian la lista
"""),

code("""
frutas = ["apple", "banana", "cherry"]
print("inicio          ", frutas)

frutas.append("orange")
print("append('orange')", frutas)

frutas.insert(1, "lemon")
print("insert(1,'lemon')", frutas)

frutas.remove("lemon")
print("remove('lemon') ", frutas)

sacada = frutas.pop()
print("pop()           ", frutas, "· devolvió", repr(sacada))

del frutas[0]
print("del frutas[0]   ", frutas)

frutas.extend(["kiwi", "pear"])
print("extend([...])   ", frutas)

frutas.clear()
print("clear()         ", frutas)
"""),

md("""
`pop` es el único de la lista que hace las dos cosas: quita el elemento **y** lo devuelve. Todos los
demás devuelven `None`.

Esa palabra, `None`, es la que provoca el error más caro del módulo.
"""),

code("""
# FALLA A PROPÓSITO, y no truena en la línea que tiene la culpa.
numeros = [3, 1, 2]
numeros = numeros.sort()        # se ve razonable y borra la lista

print("numeros vale:", numeros, "· de tipo", type(numeros).__name__)

try:
    print(len(numeros))
except TypeError as e:
    print("TypeError:", e)
"""),

md("""
La asignación no falló. `sort` ordenó la lista, devolvió `None`, y ese `None` se guardó encima de la
única referencia que había a los datos ordenados. La lista se perdió en la misma línea que la ordenó.

El `TypeError` llega después, en el `len`, que es donde no está el problema. Es el mismo patrón del
repaso 3 con la función que imprime en vez de devolver: **el error aparece lejos de su causa**.

Las dos formas de ordenar, y la diferencia entre ellas.
"""),

code("""
original = [3, 1, 2]

devuelto = original.sort()
print("original.sort() devolvió", devuelto)
print("y la lista quedó en      ", original)

print()
otra = [3, 1, 2]
copia_ordenada = sorted(otra)
print("sorted(otra) devolvió", copia_ordenada)
print("y otra sigue en      ", otra)
print("¿son el mismo objeto?", copia_ordenada is otra)
"""),

md("""
`sort` ordena la que tienes y no devuelve nada. `sorted` no toca la original y te entrega una lista
nueva. La regla para elegir es una sola pregunta: si alguien más necesita la lista en su orden
original, `sorted`.

Vale la pena verlo del lado de las cadenas para tenerlo claro. `texto.upper()` devuelve una copia y
deja `texto` intacto, porque no puede hacer otra cosa. `lista.sort()` sí puede modificar, y por eso
modifica. Los dos comportamientos son consistentes con el tipo, y confundirlos cuesta datos.

## `remove` borra uno, no todos
"""),

code("""
# FALLA A PROPÓSITO, y no truena. Quitar todas las bananas con un remove.
frutas = ["apple", "banana", "cherry", "banana", "banana"]
frutas.remove("banana")

print(frutas)
print("Bananas que quedaron:", frutas.count("banana"))

# Y si ya no hay ninguna, entonces sí truena.
vacia = ["apple"]
try:
    vacia.remove("banana")
except ValueError as e:
    print("ValueError:", e)
"""),

md("""
`remove` borra **la primera** aparición y se detiene. Quedaron dos bananas y nadie lo dijo.

El instinto es meterlo en un ciclo que recorra la lista. Esa es la trampa siguiente, y es la peor de
las cuatro que la diapositiva enumera.
"""),

code("""
# FALLA A PROPÓSITO, y no truena. Borrar mientras se recorre.
frutas = ["apple", "banana", "banana", "banana", "cherry", "date"]
for fruta in frutas:
    if fruta == "banana":
        frutas.remove(fruta)

print("Pedimos quitar 3 bananas y quedó:", frutas)
print("Bananas sobrevivientes:", frutas.count("banana"))

print()
numeros = [1, 2, 3, 4, 5, 6]
for n in numeros:
    numeros.remove(n)          # "vaciar la lista"

print("Pedimos vaciar 6 elementos y quedó:", numeros)
"""),

md("""
Una banana sobrevivió, y la lista que íbamos a vaciar se quedó con tres elementos.

El `for` no recorre valores, recorre posiciones. Va por el índice 0, luego el 1, luego el 2. Cuando
borras el elemento del índice 1, todos los de la derecha se recorren un lugar a la izquierda, así que
el que ahora ocupa la posición 1 nunca se visita: el ciclo ya va en la 2.

Por eso quedó justo la mitad en el segundo caso. Cada borrado adelanta un lugar la lista mientras el
índice también avanza, y el ciclo termina a la mitad del recorrido.

Ninguna de las dos celdas lanzó nada. Ese es el punto.

Las dos salidas limpias:
"""),

code("""
frutas = ["apple", "banana", "banana", "banana", "cherry", "date"]

# 1. Recorrer una copia y borrar de la original.
for fruta in frutas.copy():
    if fruta == "banana":
        frutas.remove(fruta)
print("Recorriendo una copia:", frutas)

# 2. Construir una lista nueva con lo que sí se queda. Casi siempre es la mejor.
frutas = ["apple", "banana", "banana", "banana", "cherry", "date"]
sin_banana = [f for f in frutas if f != "banana"]
print("Con una comprensión:  ", sin_banana)
print("La original intacta:  ", frutas)
"""),

md("""
La segunda no modifica nada, y por eso no puede equivocarse. Una función que recibe una lista y
devuelve otra se puede probar con cualquier entrada, mientras que una que modifica la que le pasaron
obliga a revisar quién más la estaba usando.

Ese criterio está en la rúbrica de la tarea de esta semana, en el renglón que dice que ninguna
función debe modificar la lista que recibe.

## Desempaque y listas anidadas
"""),

code("""
frutas = ["apple", "banana", "cherry"]
x, y, z = frutas
print(x, "·", y, "·", z)

# El asterisco recoge todo lo que sobra, y siempre en una lista.
frutas = ["apple", "banana", "cherry", "strawberry", "raspberry"]
primera, segunda, *resto = frutas
print(primera, "·", segunda, "· resto:", resto, type(resto).__name__)

# Una lista puede contener listas. El segundo corchete entra al de adentro.
anidada = ["apple", "banana", "cherry", ["blackcurrant", "orange"]]
print("anidada[3]   ", anidada[3])
print("anidada[3][1]", anidada[3][1])

# Y cualquier iterable se vuelve lista.
print(list(range(1, 10)))
print(list("Hola"))
"""),

md("""
Ese `anidada[3][1]` con dos corchetes seguidos es la forma que vas a usar todo el semestre para
leer estructuras que vienen de un archivo o de una base de datos. El primero elige el renglón, el
segundo la columna.

---
# Bloque 3 · Tuplas, conjuntos y diccionarios

Las otras tres existen porque a veces necesitas justo lo que una lista no da.

## Tuplas

Una tupla es una lista de solo lectura. Se crea con paréntesis y se lee igual que una lista.
"""),

code("""
punto = (3, 4)

print("punto[0]  ", punto[0])
print("len(punto)", len(punto))

otro = punto + (5,)              # concatenar crea una tupla nueva
print("punto + (5,)", otro, "· punto sigue en", punto)

print("punto * 2  ", punto * 2)

x, y = punto                     # desempaque
print("x =", x, "· y =", y)

# El intercambio de dos variables es una tupla disfrazada.
a, b = 1, 2
a, b = b, a
print("a =", a, "· b =", b)
"""),

code("""
# FALLA A PROPÓSITO. Una tupla no acepta asignación.
try:
    punto[0] = 9
except TypeError as e:
    print("TypeError:", e)
"""),

md("""
## La trampa que trae el archivo del curso

`Code013.py`, el archivo de tuplas de `01 - Basics/4th Module`, tiene tres llamadas a métodos que las
tuplas no tienen. Están en las líneas 31, 50 y 117, y el archivo se detiene en la primera.

No las vamos a corregir. Se corren aquí porque leer el `AttributeError` de cada una enseña más que
leer una versión ya limpia.
"""),

code("""
# FALLA A PROPÓSITO. Las tres llamadas vienen de Code013.py y las tres truenan.
esta_tupla = ("apple", "banana", "cherry")
otra_tupla = ("orange", "mango", "grapes")

intentos = [
    ("línea 31 · esta_tupla.extend(otra_tupla)", lambda: esta_tupla.extend(otra_tupla)),
    ("línea 50 · esta_tupla.copy()", lambda: esta_tupla.copy()),
    ("línea 117 · esta_tupla.clear()", lambda: esta_tupla.clear()),
]

for descripcion, intento in intentos:
    try:
        intento()
        print(f"{descripcion:<42} funcionó")
    except AttributeError as e:
        print(f"{descripcion:<42} AttributeError: {e}")
"""),

md("""
Los tres mensajes dicen lo mismo con distinto nombre: `'tuple' object has no attribute ...`.

En lugar de memorizar cuáles faltan, cuéntalos.
"""),

code("""
for tipo in (list, tuple, set, dict):
    publicos = sorted(m for m in dir(tipo) if not m.startswith("_"))
    print(f"{tipo.__name__:<6}{len(publicos):>3} métodos   {', '.join(publicos)}")
"""),

md("""
La tupla tiene **dos** métodos y la lista tiene once. Los dos que le quedan, `count` e `index`, son
justamente los dos que solo miran y no modifican.

No es que a las tuplas les falten nueve métodos por descuido. Es que `append`, `insert`, `remove`,
`pop`, `sort`, `reverse`, `clear` y `extend` modifican en el lugar, y una tupla no puede hacer eso.
`copy` tampoco tiene sentido: si nada la puede cambiar, una copia y la original nunca se van a
diferenciar, así que Python te devuelve la misma.

## La otra afirmación del archivo, la que no truena

Las líneas 46 y 47 de `Code013.py` dicen que copiar una tupla por asignación hace que los cambios en
la primera aparezcan en la segunda. La primera mitad es cierta y la segunda no puede serlo.
"""),

code("""
# FALLA A PROPÓSITO, y no truena. La afirmación es falsa, no el código.
tupla1 = ("apple", "banana", "cherry")
tupla2 = tupla1

print("¿El mismo objeto?", tupla1 is tupla2)
print("id iguales:      ", id(tupla1) == id(tupla2))

tupla2 += ("orange",)            # se ve como modificar, y no lo es

print()
print("tupla2:", tupla2)
print("tupla1:", tupla1, "· intacta")
print("¿siguen siendo el mismo objeto?", tupla1 is tupla2)
"""),

md("""
Sí son el mismo objeto al principio, exactamente como pasa con las listas. Y aun así no se propagó
nada, porque **no hay ningún cambio que propagar**: `+=` sobre una tupla construye una tupla nueva y
le pone el nombre `tupla2` encima. El objeto original nunca se enteró.

Esa es la propiedad que hace útiles a las tuplas. Si le pasas una tupla a una función, sabes que va a
regresar como se fue. Con una lista no tienes esa garantía.

## La coma solitaria
"""),

code("""
# FALLA A PROPÓSITO, y no truena. Los paréntesis no hacen la tupla, la coma sí.
uno = (5)
otro = (5,)

print("(5)  ->", uno, "· tipo", type(uno).__name__)
print("(5,) ->", otro, "· tipo", type(otro).__name__)

print()
print("len de la tupla:", len(otro))
try:
    print(len(uno))
except TypeError as e:
    print("TypeError:", e)
"""),

md("""
`(5)` es el número cinco entre paréntesis de agrupación, los mismos de `(2 + 3) * 4`. Sin coma no hay
tupla.

Donde más muerde es al devolver de una función. `return (resultado)` devuelve el valor y
`return (resultado,)` devuelve una tupla de uno, y quien la reciba con desempaque va a ver dos cosas
distintas.

## Inmutable no quiere decir congelada
"""),

code("""
# FALLA A PROPÓSITO, y no truena. La tupla no cambió, su contenido sí.
registro = ("ID001", ["London", "Paris"])

print("antes:", registro)
registro[1].append("Athens")
print("después:", registro)

print()
print("¿Se puede usar de llave en un diccionario?")
try:
    {registro: "equipaje"}
except TypeError as e:
    print("TypeError:", e)

print("Una tupla de puros inmutables sí:", {("ID001", "London"): "equipaje"})
"""),

md("""
La tupla siguió teniendo dos elementos y siguió siendo la misma. Lo que cambió fue la lista que
guarda en la segunda posición, y la tupla no tiene forma de impedirlo: solo garantiza que sus
posiciones van a apuntar siempre a los mismos objetos, no que esos objetos no vayan a cambiar por
dentro.

El `TypeError` de abajo lo confirma desde otro ángulo. Para ser llave de un diccionario un valor
tiene que ser *hashable*, y solo lo es si nada de lo que contiene puede cambiar. La tupla con lista
adentro no califica; la tupla de puras cadenas sí.

Esa es la razón práctica de las tuplas en este curso. Una coordenada, una fecha o un identificador
compuesto sirven de llave. Una lista, nunca.
"""),

md("""
## Conjuntos

Un conjunto guarda valores únicos y sin orden. No se indexa, y su razón de ser son las operaciones de
teoría de conjuntos.
"""),

code("""
lista = ["apple", "banana", "cherry", "apple", "banana"]
conjunto = set(lista)
print(len(lista), "->", len(conjunto), conjunto)

conjunto.add("orange")
conjunto.update(["mango", "grapes"])
print("después de add y update:", len(conjunto), "elementos")

conjunto.remove("banana")        # truena si no está
conjunto.discard("kiwi")         # no truena si no está
print("después de remove y discard:", sorted(conjunto))

print()
print("¿apple está?", "apple" in conjunto)

# FALLA A PROPÓSITO. Un conjunto no tiene posiciones.
try:
    print(conjunto[0])
except TypeError as e:
    print("TypeError:", e)
"""),

md("""
`remove` lanza `KeyError` si el elemento no está y `discard` no dice nada. La elección entre los dos
es una decisión de diseño: si que falte es un error, usa `remove` y entérate; si es normal que falte,
`discard`.

## Sin orden quiere decir sin orden
"""),

code("""
# FALLA A PROPÓSITO, y no truena. Confiar en el orden de un conjunto.
print("Escrito {100, 2, 33} y sale:", {100, 2, 33})
print("Escrito {'z', 'a', 'm'} y sale:", {"z", "a", "m"})

print()
numeros = {100, 2, 33}
print("Ni el de escritura ni el ordenado:", list(numeros), "contra", sorted(numeros))
"""),

md("""
No salió en el orden en que se escribió ni ordenado de menor a mayor. Salió en el orden en que las
posiciones internas del conjunto quedaron acomodadas, que depende del `hash` de cada valor.

Con cadenas es todavía menos predecible: Python le pone una semilla aleatoria al `hash` de los
textos en cada arranque, así que el mismo conjunto puede imprimirse distinto mañana. Si vas a
mostrarle un conjunto a alguien, `sorted` no es un adorno.

## Las operaciones, y un comentario del curso que no cuadra
"""),

code("""
set1 = {"a", "b", "c"}
set2 = {"c", "d", "e"}

print("union       ", sorted(set1 | set2))
print("intersection", sorted(set1 & set2))
print("difference  ", sorted(set1 - set2))
print("symmetric   ", sorted(set1 ^ set2))
print("isdisjoint  ", set1.isdisjoint(set2))
"""),

code("""
# FALLA A PROPÓSITO, y no truena. Code014.py línea 159 dice True y sale False.
chico = {"a", "b", "c"}
grande = {"c", "b", "a", "d", "e"}

print("chico.issubset(grande)  ", chico.issubset(grande))
print("chico.issuperset(grande)", chico.issuperset(grande), " <- el archivo dice True")
print("grande.issuperset(chico)", grande.issuperset(chico), " <- esto es lo que quería decir")
"""),

md("""
El archivo del curso arma un conjunto que sí contiene al otro y luego pregunta al revés. `issuperset`
se lee de izquierda a derecha: `chico.issuperset(grande)` pregunta si el chico contiene al grande, y
la respuesta es que no.

Es el mismo tipo de error que `a > b` cuando querías `b > a`. No truena, devuelve un booleano
perfectamente válido, y una condición escrita al revés deja pasar exactamente los casos que quería
detener.

## Por qué existen los conjuntos, medido
"""),

code("""
import timeit

N = 200_000
como_lista = list(range(N))
como_conjunto = set(como_lista)
buscado = N - 1                  # el peor caso para la lista: el último

t_lista = timeit.timeit(lambda: buscado in como_lista, number=200)
t_conjunto = timeit.timeit(lambda: buscado in como_conjunto, number=200)

print(f"{N:,} elementos, 200 búsquedas cada uno")
print(f"  en la lista:    {t_lista * 1000:8.2f} ms")
print(f"  en el conjunto: {t_conjunto * 1000:8.2f} ms")
print(f"  el conjunto fue {t_lista / t_conjunto:,.0f} veces más rápido")
"""),

md("""
El número exacto depende de la máquina y de lo que Colab tenga ocupado en ese momento, pero el orden
de magnitud no cambia: la diferencia se cuenta en miles de veces, no en porcentajes.

La razón es que `in` sobre una lista compara elemento por elemento hasta encontrarlo, así que el
trabajo crece con el tamaño. Un conjunto calcula el `hash` del valor buscado y va directo a la
posición donde tendría que estar, y ese trabajo es el mismo con diez elementos que con doscientos
mil.

Ese es el criterio real para elegir un conjunto: preguntar "¿está esto aquí?" muchas veces sobre una
colección grande.
"""),

md("""
## Diccionarios

Guardan pares de llave y valor. Es la colección que más se parece a un objeto, y por eso es la última
antes de entrar a clases: en la semana 3 vas a descubrir que un objeto de Python guarda sus atributos
en un diccionario de verdad.
"""),

code("""
alumno = {
    "nombre": "Ana",
    "carrera": "Mecatrónica",
    "semestre": 2,
}

print(alumno["nombre"])
print(alumno.get("carrera"))

print()
print("get de algo que no está:        ", alumno.get("beca"))
print("get con valor por defecto:      ", alumno.get("beca", False))
print("¿el diccionario cambió?         ", alumno)
"""),

code("""
# FALLA A PROPÓSITO. Los corchetes no perdonan la llave que falta.
try:
    print(alumno["beca"])
except KeyError as e:
    print("KeyError:", e)
"""),

md("""
`get` devuelve `None` y sigue; los corchetes cortan el programa. La elección es la misma que entre
`remove` y `discard`, y se decide con una pregunta: si el campo falta, ¿es un error o es normal?

En la tarea de esta semana el criterio de "Acceso" pide `get` justo donde el campo puede faltar. Una
beca puede no existir. Un nombre no, y ahí los corchetes son mejores porque avisan.
"""),

code("""
alumno["beca"] = "parcial"       # asignar una llave nueva la crea
alumno["semestre"] = 3           # asignar una que existe la reemplaza

print("Llaves: ", list(alumno.keys()))
print("Valores:", list(alumno.values()))
print()
for llave, valor in alumno.items():
    print(f"  {llave:<10}{valor}")

print()
print("¿tiene carrera?", "carrera" in alumno)
print("cuántos campos:", len(alumno))

quitado = alumno.pop("beca")
print("pop devolvió:", repr(quitado), "· quedan", len(alumno), "campos")
"""),

md("""
`items()` entrega una tupla por cada par, y por eso el `for` de arriba puede desempacarla en dos
nombres. Es el mismo desempaque de tuplas de hace unas celdas, aplicado sin decirlo.

Recorrer solo el diccionario, sin `.items()`, recorre las llaves. Es un detalle que confunde al
principio porque parece que debería recorrer los valores.

## Diccionarios dentro de diccionarios
"""),

code("""
grupo = {
    "A01": {"nombre": "Ana", "calificaciones": [8, 9, 10]},
    "A02": {"nombre": "Beto", "calificaciones": [7, 6]},
    "A03": {"nombre": "Carla", "calificaciones": []},
}

for matricula, datos in grupo.items():
    notas = datos["calificaciones"]
    promedio = sum(notas) / len(notas) if notas else None
    print(f"{matricula}  {datos['nombre']:<7}{len(notas)} notas  promedio {promedio}")
"""),

md("""
Esa estructura de diccionario de diccionarios es la forma en que llegan casi todos los datos reales:
una respuesta de una API, un archivo JSON, un renglón de base de datos.

Y es también la última parada antes de las clases. Un diccionario junta datos que van juntos, pero no
trae consigo las funciones que los manipulan, así que el promedio se calcula afuera y nada garantiza
que todos los diccionarios tengan las mismas llaves. Una clase resuelve las dos cosas de un golpe, y
eso es la semana 3.
"""),

md("""
---
# Bloque 4 · Copiar contra renombrar

El bloque que más se olvida, y el que reaparece en la semana 6 con otro nombre.

## Predice antes de correr

¿Qué imprime la última línea?

```python
numeros = [1, 2, 3]
copia = numeros

copia.append(4)

print(len(numeros))
```

- **A.** 3, porque `copia` es otra lista.
- **B.** 4, porque los dos nombres apuntan a la misma lista.
- **C.** Error, no se puede asignar una lista a otra variable.
- **D.** 7, porque se concatenan las dos listas.
"""),

code("""
# FALLA A PROPÓSITO, y no truena. La respuesta del quiz, con la prueba al lado.
numeros = [1, 2, 3]
copia = numeros

copia.append(4)

print("len(numeros):", len(numeros))
print("numeros:", numeros)
print("copia:  ", copia)
print()
print("¿mismo objeto? ", numeros is copia)
print("¿mismo id?     ", id(numeros) == id(copia))
"""),

md("""
La respuesta es **B**.

| Paso | Instrucción | numeros | copia | ¿Mismo objeto? |
|---|---|---|---|---|
| 1 | `numeros = [1, 2, 3]` | `[1, 2, 3]` | no existe | |
| 2 | `copia = numeros` | `[1, 2, 3]` | `[1, 2, 3]` | sí |
| 3 | `copia.append(4)` | `[1, 2, 3, 4]` | `[1, 2, 3, 4]` | sí |
| 4 | `len(numeros)` | 4 | 4 | sí |

El signo igual nunca copia el contenido de una lista. Copia la referencia, que es la dirección donde
vive. Después de la línea 2 hay dos nombres y **una** lista, y `append` la modifica sin importar por
cuál de los dos nombres lo pidas.

Con números y cadenas parece que sí copia, y por eso el error es tan común. Lo que pasa ahí es que
son inmutables: como no se pueden modificar en el lugar, cualquier operación construye un valor nuevo
y el original queda intacto de todos modos. La diferencia estaba siempre, solo que no se notaba.

## Las tres formas de copiar de verdad
"""),

code("""
originales = [1, 2, 3]

con_metodo = originales.copy()
con_funcion = list(originales)
con_rebanada = originales[:]

originales.append(99)

print("originales  ", originales)
print("copy()      ", con_metodo)
print("list()      ", con_funcion)
print("rebanada [:]", con_rebanada)
print()
for nombre, valor in [("copy()", con_metodo), ("list()", con_funcion),
                      ("[:]", con_rebanada)]:
    print(f"{nombre:<12} ¿es el mismo objeto que originales? {valor is originales}")
"""),

md("""
Las tres hacen lo mismo. `copy()` es la más explícita y es la que conviene escribir; `list()` sirve
además para convertir desde una tupla o un conjunto, y `[:]` es la más corta y la que peor se lee.

Los diccionarios y los conjuntos tienen su propio `copy()` y funcionan igual.

## La copia es superficial
"""),

code("""
# FALLA A PROPÓSITO, y no truena. copy() copió la lista de afuera, no las de adentro.
equipos = [["Ana", "Beto"], ["Carla", "Diego"]]
respaldo = equipos.copy()

respaldo[0].append("Elena")

print("respaldo:", respaldo)
print("equipos: ", equipos, " <- también cambió")
print()
print("¿la lista de afuera es la misma?", equipos is respaldo)
print("¿la de adentro es la misma?     ", equipos[0] is respaldo[0])
"""),

md("""
La primera pregunta da `False` y la segunda `True`. `copy()` construyó una lista nueva, y la llenó con
las mismas dos referencias que tenía la original. Las listas de adentro nunca se copiaron.

Se le llama copia superficial, y la diapositiva lo menciona en la nota al margen. La versión profunda
está en la biblioteca estándar.
"""),

code("""
from copy import deepcopy

equipos = [["Ana", "Beto"], ["Carla", "Diego"]]
superficial = equipos.copy()
profunda = deepcopy(equipos)

superficial[0].append("Elena")
profunda[1].append("Fernanda")

print("equipos:     ", equipos)
print("superficial: ", superficial)
print("profunda:    ", profunda)
print()
print("¿la de adentro es la misma que la original?")
print("  superficial:", equipos[0] is superficial[0])
print("  profunda:   ", equipos[1] is profunda[1])
"""),

md("""
`equipos` se llevó a Elena, que se agregó a la copia superficial, y no se llevó a Fernanda, que se
agregó a la profunda.

`deepcopy` recorre la estructura completa y duplica todo lo que encuentra. Cuesta más y casi nunca
hace falta, pero cuando hace falta no hay sustituto.

## El multiplicador que parece atajo
"""),

code("""
# FALLA A PROPÓSITO, y no truena. Tres renglones que son el mismo renglón.
matriz = [[0] * 3] * 3
print("recién creada:", matriz)

matriz[0][0] = 9
print("tras matriz[0][0] = 9:", matriz)
print("¿los tres renglones son el mismo objeto?",
      matriz[0] is matriz[1] is matriz[2])

print()
buena = [[0] * 3 for _ in range(3)]
buena[0][0] = 9
print("con una comprensión:", buena)
print("¿el mismo objeto?", buena[0] is buena[1])
"""),

md("""
`[[0] * 3] * 3` repite la referencia a **una** lista interna tres veces. Cambiar un elemento cambia
los tres renglones, y sin embargo `[0] * 3` para el renglón sencillo sí funciona, porque el cero es
inmutable y ahí no hay nada que compartir.

La comprensión evalúa `[0] * 3` una vez por vuelta y crea tres listas distintas.

## A dónde va todo esto

Guarda estas tres celdas. El mismo mecanismo aparece dos veces más en el curso, con otro disfraz.

En la **semana 3**, cuando un objeto guarde una lista y dos objetos terminen viendo la misma. En la
**semana 6**, cuando un atributo escrito en la clase en lugar de en el constructor se comparta entre
todas las instancias y nadie entienda por qué el carrito del segundo cliente ya trae los productos
del primero.

Y ya lo viste una vez, en el repaso 3: la lista puesta como valor por defecto de una función es este
mismo problema. Una sola lista, muchos nombres, y ninguna advertencia.
"""),

md("""
---
## Cuatro errores de este módulo

**Guardar lo que devuelve `sort`.** `lista = lista.sort()` deja la variable en `None` y pierde los
datos. `sort` ordena y no devuelve nada; `sorted` sí devuelve.

**Índice fuera de rango.** La última posición de una lista de `n` elementos es `n - 1`. Indexar
truena con `IndexError`, pero rebanar fuera de rango devuelve una lista corta o vacía y sigue.

**Llave que no existe.** Los corchetes lanzan `KeyError`. Usa `get` donde el dato pueda faltar, y
corchetes donde su ausencia sea un error que quieras ver.

**Modificar la lista mientras la recorres.** El ciclo salta elementos y no avisa. Recorre una copia,
o mejor, construye una lista nueva con lo que se queda.

De los cuatro, tres corrieron arriba sin lanzar nada.
"""),

md("""
---
# Ejercicios

Las soluciones están hasta abajo del cuaderno.

### Ejercicio 1 · Las cuatro, con los mismos datos

Toma la lista `["rojo", "azul", "rojo", "verde"]` y conviértela a tupla, a conjunto y a diccionario
con `dict.fromkeys`. Imprime las cuatro con su longitud.

Explica en un comentario por qué dos de ellas perdieron un elemento.

### Ejercicio 2 · Índices y rebanadas

Con `meses = ["ene", "feb", "mar", "abr", "may", "jun"]`, imprime el tercero, el último, el primer
trimestre, el segundo trimestre, los meses en posición par y la lista al revés.

Después pide `meses[6]` y atrapa el error. Compáralo con lo que devuelve `meses[6:]`.

### Ejercicio 3 · Ordenar sin perder

Con `precios = [340, 120, 890, 55]`, imprime la lista ordenada sin modificar la original. Después
ordénala en el lugar. Muestra qué devuelve cada una de las dos operaciones.

### Ejercicio 4 · El filtro que salta

Escribe un ciclo que quite todos los ceros de `[0, 1, 0, 0, 2, 3, 0]` borrando mientras recorre.
Muestra cuántos ceros quedaron.

Después resuélvelo con una comprensión y comprueba que la original no se tocó.

### Ejercicio 5 · La coma solitaria

Escribe una función `envolver(valor)` que devuelva su argumento en una tupla de un elemento. Pruébala
con un número y con una cadena, e imprime el tipo y la longitud del resultado.

Después escribe la versión equivocada, sin la coma, y explica en un comentario qué pasa cuando el
argumento es una cadena de cinco letras.

### Ejercicio 6 · Conjuntos para responder preguntas

Con `inscritos = {"Ana", "Beto", "Carla", "Diego"}` y `asistieron = {"Beto", "Diego", "Elena"}`,
responde con operaciones de conjunto: quiénes faltaron, quién asistió sin estar inscrito, quiénes
estuvieron en las dos listas, y el total de personas involucradas.

### Ejercicio 7 · `get` contra corchetes

Con una lista de diccionarios de alumnos donde algunos traen `"beca"` y otros no, imprime un renglón
por alumno con su nombre y su beca. Hazlo primero con corchetes, atrapa el `KeyError` y di en qué
alumno se detuvo. Después hazlo con `get`.

### Ejercicio 8 · Copiar de verdad

Escribe una función `agregar_alumno(grupo, nombre)` que devuelva un grupo nuevo con el alumno
agregado, sin modificar el que recibió. Demuestra con `is` que el resultado es una lista distinta.

Después escribe la versión que sí modifica y muestra la diferencia con las mismas dos llamadas.

### Ejercicio 9 · La tarea

Con una lista de diccionarios de alumnos, cada uno con `nombre`, `carrera`, `calificaciones` y a
veces `beca`, escribe tres funciones que devuelvan:

1. Los alumnos aprobados, con promedio de 7 o más.
2. El promedio del grupo.
3. Las carreras sin repetir.

Las carreras se resuelven con un conjunto, no con un ciclo que revisa si ya está. La beca se lee con
`get`. Ninguna de las tres modifica la lista que recibe, y lo tienes que demostrar imprimiendo la
lista original al final.
"""),

md("""
---
## Tres ideas para llevarse

**Tres preguntas eligen la colección.** Importa el orden, va a cambiar, puede haber repetidos. Con
esas tres se decide, y decidir mal cuesta datos perdidos en silencio.

**Los métodos de lista modifican y devuelven `None`.** Justo al revés que los de cadena, que
devuelven una copia y no tocan nada. `sort` contra `sorted` es el par que hay que tener memorizado.

**Asignar una lista no la copia.** Deja dos nombres sobre un solo objeto, y `id` o `is` lo demuestran
en una línea. En la semana 6 esto vuelve como el atributo de clase que todas las instancias comparten.

El siguiente repaso es el último: qué hace un programa cuando algo sale mal. Ahí van a volver casi
todos los errores de este cuaderno, `IndexError`, `KeyError`, `ValueError` y `TypeError`, pero
atrapados con `try` en vez de sufridos.
"""),

md("""
---
# Soluciones

### Ejercicio 1

```python
colores = ["rojo", "azul", "rojo", "verde"]

como_tupla = tuple(colores)
como_conjunto = set(colores)
como_dict = dict.fromkeys(colores, 0)

for nombre, valor in [("lista", colores), ("tupla", como_tupla),
                      ("conjunto", como_conjunto), ("diccionario", como_dict)]:
    print(f"{nombre:<13}{len(valor)}  {valor}")

# El conjunto y el diccionario perdieron un "rojo". Los dos guardan valores
# únicos, el conjunto en sus elementos y el diccionario en sus llaves, así que
# el segundo "rojo" no se agregó. La lista y la tupla admiten repetidos y por
# eso conservaron los cuatro.
```

### Ejercicio 2

```python
meses = ["ene", "feb", "mar", "abr", "may", "jun"]

print("tercero:  ", meses[2])
print("último:   ", meses[-1])
print("trim 1:   ", meses[:3])
print("trim 2:   ", meses[3:])
print("posición par:", meses[::2])
print("al revés: ", meses[::-1])

try:
    print(meses[6])
except IndexError as e:
    print("IndexError:", e)

print("meses[6:] devuelve:", meses[6:])
```

`meses[6]` truena y `meses[6:]` devuelve `[]`. La diferencia importa: un índice fuera de rango te
avisa dónde está el problema, y una rebanada fuera de rango te deja seguir con una lista vacía que
más adelante va a dar un promedio de cero o una división entre cero.

### Ejercicio 3

```python
precios = [340, 120, 890, 55]

copia_ordenada = sorted(precios)
print("sorted devolvió:", copia_ordenada)
print("precios sigue en:", precios)

devuelto = precios.sort()
print("sort devolvió:  ", devuelto)
print("precios quedó en:", precios)
```

`sorted` devuelve una lista y no toca nada. `sort` devuelve `None` y deja la lista ordenada. Guardar
lo que devuelve `sort` es el error número uno de este módulo.

### Ejercicio 4

```python
numeros = [0, 1, 0, 0, 2, 3, 0]
for n in numeros:
    if n == 0:
        numeros.remove(n)

print("borrando mientras recorre:", numeros)
print("ceros que quedaron:", numeros.count(0))

numeros = [0, 1, 0, 0, 2, 3, 0]
sin_ceros = [n for n in numeros if n != 0]
print("con comprensión:", sin_ceros)
print("original intacta:", numeros)
```

Quedan ceros. Cada borrado recorre la lista a la izquierda mientras el índice del ciclo avanza a la
derecha, así que el elemento que ocupó el lugar del borrado nunca se visita. La comprensión no puede
fallar así porque no modifica nada mientras lee.

### Ejercicio 5

```python
def envolver(valor):
    return (valor,)


def envolver_mal(valor):
    return (valor)


for prueba in [7, "hola"]:
    bien = envolver(prueba)
    mal = envolver_mal(prueba)
    print(f"{repr(prueba):<8} bien: {bien} len {len(bien)}   "
          f"mal: {repr(mal)} tipo {type(mal).__name__}")

# Con la cadena "hola", la versión sin coma devuelve la cadena tal cual. len da
# 4 en vez de 1, y un for sobre el resultado recorre letras en lugar de recorrer
# un solo elemento. El error no truena, solo entrega otra cosa.
```

### Ejercicio 6

```python
inscritos = {"Ana", "Beto", "Carla", "Diego"}
asistieron = {"Beto", "Diego", "Elena"}

print("faltaron:      ", sorted(inscritos - asistieron))
print("sin inscribir: ", sorted(asistieron - inscritos))
print("en las dos:    ", sorted(inscritos & asistieron))
print("total de gente:", len(inscritos | asistieron))
```

Las cuatro respuestas son un operador cada una. La versión con ciclos y banderas ocupa veinte líneas
y se equivoca en el tercer caso.

### Ejercicio 7

```python
alumnos = [
    {"nombre": "Ana", "beca": "parcial"},
    {"nombre": "Beto"},
    {"nombre": "Carla", "beca": "total"},
]

try:
    for alumno in alumnos:
        print(alumno["nombre"], "->", alumno["beca"])
except KeyError as e:
    print("KeyError:", e, "· se detuvo en Beto")

print()
for alumno in alumnos:
    print(alumno["nombre"], "->", alumno.get("beca", "sin beca"))
```

La primera versión alcanzó a imprimir a Ana y se detuvo. Los corchetes están bien para `"nombre"`,
que siempre tiene que estar, y mal para `"beca"`, que legítimamente puede faltar.

### Ejercicio 8

```python
def agregar_alumno(grupo, nombre):
    nuevo = grupo.copy()
    nuevo.append(nombre)
    return nuevo


def agregar_alumno_mutando(grupo, nombre):
    grupo.append(nombre)
    return grupo


grupo = ["Ana", "Beto"]
resultado = agregar_alumno(grupo, "Carla")
print("devuelto:", resultado)
print("original:", grupo)
print("¿mismo objeto?", resultado is grupo)

print()
grupo = ["Ana", "Beto"]
resultado = agregar_alumno_mutando(grupo, "Carla")
print("devuelto:", resultado)
print("original:", grupo, " <- también cambió")
print("¿mismo objeto?", resultado is grupo)
```

La segunda es peligrosa justamente porque también devuelve. Quien la llama ve una lista con Carla y
supone que la suya quedó intacta.

### Ejercicio 9

```python
ALUMNOS = [
    {"nombre": "Ana", "carrera": "Mecatrónica", "calificaciones": [8, 9, 10],
     "beca": "parcial"},
    {"nombre": "Beto", "carrera": "Sistemas", "calificaciones": [6, 7, 5]},
    {"nombre": "Carla", "carrera": "Mecatrónica", "calificaciones": [9, 9, 8]},
    {"nombre": "Diego", "carrera": "Industrial", "calificaciones": [7, 7, 7]},
]


def promedio_de(alumno):
    notas = alumno["calificaciones"]
    return sum(notas) / len(notas) if notas else None


def obtener_aprobados(alumnos, minima=7):
    return [a for a in alumnos
            if promedio_de(a) is not None and promedio_de(a) >= minima]


def calcular_promedio_grupo(alumnos):
    promedios = [promedio_de(a) for a in alumnos if promedio_de(a) is not None]
    return sum(promedios) / len(promedios) if promedios else None


def listar_carreras(alumnos):
    return sorted({a["carrera"] for a in alumnos})


print("Aprobados:", [a["nombre"] for a in obtener_aprobados(ALUMNOS)])
print(f"Promedio del grupo: {calcular_promedio_grupo(ALUMNOS):.2f}")
print("Carreras:", listar_carreras(ALUMNOS))
print()
for alumno in ALUMNOS:
    print(f"  {alumno['nombre']:<7}{alumno.get('beca', 'sin beca')}")

print()
print("La lista original, sin tocar:")
for alumno in ALUMNOS:
    print(" ", alumno)
```

`listar_carreras` usa una comprensión de conjunto, que es la forma corta de `set(...)` sobre lo que
va saliendo. Las tres funciones leen y ninguna escribe, así que la última impresión muestra la lista
tal como se declaró.

`promedio_de` devuelve `None` para el alumno sin calificaciones capturadas, y las dos funciones que
la usan tienen que decidir qué hacer con ese `None`. Eso no es un detalle molesto, es la misma
decisión del repaso 3: no hay promedio no es lo mismo que el promedio es cero.
"""),

]

write(OUT / "es" / "w01.4.ipynb", es)
print("wrote", OUT / "es" / "w01.4.ipynb")
