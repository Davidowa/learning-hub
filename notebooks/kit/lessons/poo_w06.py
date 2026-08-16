"""notebooks/programacion-orientada-a-objetos/es/w06.ipynb

Source deck: ppts/python/programacion-orientada-a-objetos/es/w06.es.yaml
Source code:  docs/en/courses/python-course/02 - POO/6th Module/Code023.py
                  (la nube de etiquetas, abierta y cerrada, y el KeyError final)
              docs/en/courses/python-course/02 - POO/6th Module/Code021.py
                  (composición: CPU, RAM, HardDrive y Computer)

Los dos archivos corren completos, comprobado.

Esta es la semana a la que apuntan los hilos que vienen desde el repaso 3: la
lista por omisión, el alias del repaso 4 y el atributo de clase de la semana 3.
El bloque 2 los cobra explícitamente.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from nbkit import md, code, write, REPO

OUT = REPO / "notebooks" / "programacion-orientada-a-objetos"

es = [

md("""
# Programación Orientada a Objetos · Semana 06
## Tema 3 · Propiedades fundamentales

**COM102 · Facultad de Ingeniería · Profesor David Escobar-Castillejos**

Juntar los datos con quien los cuida, decidir qué se ve desde fuera, y reutilizar sin heredar.

Este cuaderno paga una deuda vieja. Desde el repaso 3 vengo prometiendo que en la semana 6 iba a
quedar claro por qué dos objetos terminan compartiendo estado sin que nadie lo haya pedido. Ese
párrafo llega en el bloque 2, y ahora ya tienes todo el vocabulario para leerlo.

Al terminar vas a poder:

1. Distinguir encapsular de ocultar, que no son la misma decisión ni se toman al mismo tiempo.
2. Diseñar una interfaz pública y defender qué quedó fuera de ella.
3. Detectar una fuga: el getter que devuelve la estructura interna y deshace todo el trabajo.
4. Aplicar la prueba del cambio para saber si un dato está bien guardado.
5. Reutilizar por composición, y decir en qué caso la herencia sí se gana el lugar.

### Cómo se usa este cuaderno

Ejecuta las celdas en orden con **Shift + Enter**. Diez fallan a propósito y llevan un comentario que
lo dice.

Siete de las diez **no lanzan ninguna excepción**. Esta semana esa proporción no es casualidad: una
fuga de encapsulamiento nunca truena. Produce un programa que funciona hoy y que se rompe el día que
alguien cambie algo que creía interno.
"""),

md("""
---
# Bloque 1 · Encapsulamiento

La palabra suena a candado, y de entrada no significa eso.

**Encapsular** es poner en la misma clase un dato y el comportamiento que lo cuida. Nada más.

**Ocultar** es la decisión, posterior y distinta, de no dejar que ese dato se vea desde fuera.

Se puede encapsular sin ocultar nada, y ahí empiezan los problemas. La clase de abajo está
encapsulada: el diccionario y la regla que lo normaliza viven juntos. No está oculta.
"""),

code("""
class NubeAbierta:
    def __init__(self) -> None:
        self.etiquetas = {}          # público

    def agregar(self, etiqueta: str) -> None:
        clave = etiqueta.lower()     # la única regla de la clase
        actual = self.etiquetas.get(clave, 0)
        self.etiquetas[clave] = actual + 1


nube = NubeAbierta()
nube.agregar("Python")
nube.agregar("python")
nube.agregar("PYTHON")
nube.agregar("sql")

print(nube.etiquetas)
print("Etiquetas distintas:", len(nube.etiquetas))
"""),

md("""
Tres formas de escribir "python" y una sola llave. La regla funciona.

La regla es `etiqueta.lower()`, vive dentro de `agregar`, y ese es todo el encapsulamiento que tiene la
clase. Quien use `agregar` no necesita saber que existe.

El problema es que `agregar` no es la única puerta.
"""),

code("""
# FALLA A PROPÓSITO. Leer una llave que no está, por la puerta de atrás.
try:
    print(nube.etiquetas["c++"])
except KeyError as e:
    print("KeyError:", e)

print()
print("La misma pregunta, con la respuesta que uno querría:",
      nube.etiquetas.get("c++", 0))

print()
try:
    print(len(nube))
except TypeError as e:
    print("TypeError:", e)
print("Hay que saber que por dentro es un diccionario:", len(nube.etiquetas))
"""),

md("""
Dos síntomas de la misma cosa.

`nube.etiquetas["c++"]` revienta porque preguntar por una etiqueta que nadie usó pasa por el
diccionario, y un diccionario contesta con `KeyError`. Esa no es la respuesta que el problema pide: la
respuesta es cero.

Y `len(nube)` ni siquiera existe. Para contar hay que escribir `len(nube.etiquetas)`, que obliga a quien
usa la clase a saber que por dentro hay un diccionario. Ahí, en esa línea, el detalle interno se
convirtió en parte del contrato sin que nadie lo decidiera.
"""),

code("""
# FALLA A PROPÓSITO, y no truena. Escribir directo en el diccionario.
nube.etiquetas["Python"] = 99        # con mayúscula, saltándose la regla

print(nube.etiquetas)
print("Etiquetas distintas:", len(nube.etiquetas), "<- eran 2")
print()
print('nube.etiquetas["python"]:', nube.etiquetas["python"])
print('nube.etiquetas["Python"]:', nube.etiquetas["Python"])
print()
nube.agregar("PYTHON")
print("Después de agregar PYTHON otra vez:", nube.etiquetas)
print("El 99 quedó en una llave que agregar nunca va a tocar.")
"""),

md("""
Dos llaves para la misma etiqueta, y la clase no se enteró.

Quien escribió esa línea no estaba saboteando nada. Estaba usando un diccionario público, que es
exactamente lo que la clase le ofreció. La regla de normalizar existe, pero solo se aplica si entras
por `agregar`, y nadie te obliga a entrar por ahí.

Esa es la diferencia entre encapsular y ocultar, y cabe en una pregunta: **¿quién tiene que recordar
esta regla?** Si vive dentro de la clase y no hay otra puerta, nadie. Si el atributo está abierto,
todos los archivos que lo tocan, y alguno no se va a acordar.

## La regla que se muda hacia afuera
"""),

code("""
# FALLA A PROPÓSITO, y no truena. La regla repetida en cada lugar que llama.
otra = NubeAbierta()

# Tres archivos distintos del proyecto, cada uno acordándose de normalizar:
otra.etiquetas["python"] = otra.etiquetas.get("python", 0) + 1     # archivo A
otra.etiquetas["sql".lower()] = 1                                  # archivo B
otra.etiquetas["C++"] = 1                                          # archivo C, se olvidó

print(otra.etiquetas)
print()
minusculas = [k for k in otra.etiquetas if k == k.lower()]
print(f"{len(minusculas)} de {len(otra.etiquetas)} llaves respetan la regla")
print("La que falla:", [k for k in otra.etiquetas if k != k.lower()])
"""),

md("""
Dos de tres. La tercera se escribió en otro archivo, por otra persona, seis meses después.

Cuando la regla se repite en cada lugar que llama, la regla ya no vive en la clase. Vive en la memoria
de un equipo, y esa memoria tiene rotación.

**Si tres archivos hacen `.lower()` antes de llamar a tu método, la regla está en el lugar
equivocado.**

## La misma clase, con el diccionario adentro
"""),

code("""
class Nube:
    def __init__(self) -> None:
        self.__etiquetas: dict[str, int] = {}

    def agregar(self, etiqueta: str) -> None:
        clave = etiqueta.lower()
        self.__etiquetas[clave] = self.__etiquetas.get(clave, 0) + 1

    def __getitem__(self, etiqueta: str) -> int:
        return self.__etiquetas.get(etiqueta.lower(), 0)

    def __setitem__(self, etiqueta: str, cuenta: int) -> None:
        self.__etiquetas[etiqueta.lower()] = cuenta

    def __len__(self) -> int:
        return len(self.__etiquetas)

    def __iter__(self):
        return iter(self.__etiquetas)

    def __repr__(self) -> str:
        return f"Nube({self.__etiquetas})"


cerrada = Nube()
for etiqueta in ["Python", "python", "PYTHON", "sql"]:
    cerrada.agregar(etiqueta)

print(cerrada)
print()
print('cerrada["c++"]:', cerrada["c++"], "<- cero en lugar de KeyError")
cerrada["Python"] = 99               # la misma línea de hace un rato
print("Después de cerrada['Python'] = 99:", cerrada)
print("Etiquetas distintas:", len(cerrada))
"""),

md("""
La misma línea que antes creó una llave duplicada, ahora entra por `__setitem__`, se normaliza, y
actualiza la que ya estaba.

Y `cerrada["c++"]` devolvió cero en lugar de reventar, porque preguntar por una etiqueta que nadie ha
usado no es un error: es una pregunta con respuesta cero.

Fíjate en lo que **no** cambió: la regla sigue siendo una sola línea, `etiqueta.lower()`, escrita dos
veces en la clase. Lo que cambió es que ya no hay ninguna otra puerta.

## Las dos nubes, contadas
"""),

code("""
OPERACIONES = ["Python", "python", "PYTHON", "SQL", "sql", "C++"]

abierta = NubeAbierta()
for etiqueta in OPERACIONES:
    abierta.etiquetas[etiqueta] = abierta.etiquetas.get(etiqueta, 0) + 1

limpia = Nube()
for etiqueta in OPERACIONES:
    limpia.agregar(etiqueta)

print("Con el diccionario abierto, tocado desde fuera:")
print("  ", abierta.etiquetas)
print("  ", len(abierta.etiquetas), "llaves para", len(set(e.lower() for e in OPERACIONES)),
      "etiquetas reales")
print()
print("Con la clase cerrada:")
print("  ", limpia)
print("  ", len(limpia), "llaves para", len(set(e.lower() for e in OPERACIONES)),
      "etiquetas reales")
"""),

md("""
Seis llaves contra tres, con exactamente las mismas seis operaciones.

Ese es el costo medido de dejar abierta la estructura interna. No hay un error, no hay una excepción,
hay un reporte de etiquetas que dice que "Python" y "python" son cosas distintas y un usuario que no
entiende por qué.
"""),

md("""
---
# Bloque 2 · Ocultamiento de información

Todo lo que dejes visible es una promesa. Cuanto más chica la interfaz, menos promesas que sostener.

| Miembro | Qué es | Quién lo usa |
|---|---|---|
| `agregar` | Contrato público | Cualquiera |
| `__getitem__` | Contrato público | El operador de corchetes |
| `__len__` | Contrato público | La función `len` |
| `__etiquetas` | Detalle interno | Solo la clase |
| `etiqueta.lower()` | Detalle interno | Solo la clase |

La tabla se lee en una dirección que importa: lo de arriba no lo puedes cambiar sin avisar, lo de abajo
sí.

## La prueba del cambio

Un dato está bien encapsulado si **puedes cambiar cómo se guarda por dentro sin tocar una sola línea
fuera de la clase**.

No es una opinión, es una prueba que se corre. Aquí está.
"""),

code("""
def probar(clase):
    \"\"\"Las mismas seis comprobaciones, sobre cualquier nube que respete el contrato.\"\"\"
    nube = clase()
    for etiqueta in ["Python", "python", "sql"]:
        nube.agregar(etiqueta)

    comprobaciones = [
        ("python cuenta 2", nube["python"] == 2),
        ("PYTHON cuenta 2", nube["PYTHON"] == 2),
        ("sql cuenta 1", nube["sql"] == 1),
        ("c++ cuenta 0", nube["c++"] == 0),
        ("hay 2 etiquetas", len(nube) == 2),
        ("se puede recorrer", sorted(nube) == ["python", "sql"]),
    ]
    return comprobaciones


for nombre, ok in probar(Nube):
    print(f"  {'OK ' if ok else 'NO '}{nombre}")

print()
print("Pasaron:", sum(1 for _, ok in probar(Nube) if ok), "de 6")
"""),

code("""
class NubeDeListas:
    \"\"\"Por dentro no hay diccionario. Por fuera no se nota.\"\"\"

    def __init__(self) -> None:
        self.__pares: list[list] = []          # [[clave, cuenta], ...]

    def __buscar(self, clave):
        for par in self.__pares:
            if par[0] == clave:
                return par
        return None

    def agregar(self, etiqueta: str) -> None:
        clave = etiqueta.lower()
        par = self.__buscar(clave)
        if par is None:
            self.__pares.append([clave, 1])
        else:
            par[1] += 1

    def __getitem__(self, etiqueta: str) -> int:
        par = self.__buscar(etiqueta.lower())
        return par[1] if par else 0

    def __setitem__(self, etiqueta: str, cuenta: int) -> None:
        par = self.__buscar(etiqueta.lower())
        if par is None:
            self.__pares.append([etiqueta.lower(), cuenta])
        else:
            par[1] = cuenta

    def __len__(self) -> int:
        return len(self.__pares)

    def __iter__(self):
        return iter(clave for clave, _ in self.__pares)


resultados = probar(NubeDeListas)
for nombre, ok in resultados:
    print(f"  {'OK ' if ok else 'NO '}{nombre}")

print()
print("Pasaron:", sum(1 for _, ok in resultados if ok), "de 6")
print("Líneas de la función probar que hubo que cambiar: 0")
"""),

md("""
Seis de seis, con una implementación que por dentro no se parece en nada, y la función de prueba se
usó tal cual.

Eso es ocultamiento de información funcionando. El diccionario nunca fue parte del contrato, así que
cambiarlo por una lista de pares no rompió a nadie. Si `etiquetas` hubiera sido público, esta misma
prueba habría requerido reescribir cada línea que lo tocaba.

La prueba se aplica al revés también, y ahí es donde sirve para diseñar: cuando dudes si un atributo
debe ser público, pregúntate **si estarías dispuesto a sostener su forma exacta durante los próximos
dos años**. Si no, ciérralo hoy.

## Lo que la interfaz prometió sin que nadie lo escribiera

Fíjate en una línea de la función de prueba: `sorted(nube) == ["python", "sql"]`. Ese `sorted` no está
ahí de adorno.
"""),

code("""
# FALLA A PROPÓSITO, y no truena. El orden que nadie prometió y todos usan.
class NubeAlfabetica(Nube):
    \"\"\"Mismo contrato, mismos métodos, otra decisión interna sobre el recorrido.\"\"\"

    def __iter__(self):
        return iter(sorted(super().__iter__()))


def reporte(nube):
    return " · ".join(f"{e}={nube[e]}" for e in nube)


ENTRADAS = ["zeta", "alfa", "media", "alfa"]

original = Nube()
alfabetica = NubeAlfabetica()
for etiqueta in ENTRADAS:
    original.agregar(etiqueta)
    alfabetica.agregar(etiqueta)

print("Reporte con la primera: ", reporte(original))
print("Reporte con la segunda: ", reporte(alfabetica))
print()
print("¿Los dos reportes son iguales?", reporte(original) == reporte(alfabetica))
print("¿Y las mismas etiquetas?     ", sorted(original) == sorted(alfabetica))
print("¿Las mismas cuentas?         ",
      {e: original[e] for e in original} == {e: alfabetica[e] for e in alfabetica})
"""),

md("""
Las mismas etiquetas, las mismas cuentas, y dos reportes distintos.

Ninguna de las dos clases rompió el contrato de la tabla: `agregar`, corchetes, `len`. Lo que cambió es
el orden del recorrido, que **nunca estuvo en la tabla** y que sin embargo quedó prometido desde el
momento en que la clase expuso `__iter__`.

Ese es el filo de este bloque. Cada método público promete más de lo que su nombre dice: promete su
resultado, su orden, su velocidad y hasta el tipo exacto que devuelve. Por eso la función de prueba de
hace dos celdas escribió `sorted(nube)` y no `list(nube)`: para no depender de algo que no quería
sostener.

Cuando escribas una interfaz, la pregunta no es solo qué métodos expones. Es **qué se puede observar a
través de ellos**.

## Predice antes de correr

```python
class Carrito:
    def __init__(self):
        self.__productos = []

    def obtener(self):
        return self.__productos


c = Carrito()
c.obtener().append("X1")
print(len(c.obtener()))
```

- **A.** 0, porque `__productos` es privado.
- **B.** 1, porque el getter devolvió la lista de verdad.
- **C.** `AttributeError`, `obtener` no puede tocar `__productos`.
- **D.** `TypeError`, no se puede hacer `append` sobre un método.
"""),

code("""
# FALLA A PROPÓSITO, y no truena. La fuga: un getter que devuelve la estructura interna.
class CarritoConFuga:
    def __init__(self):
        self.__productos = []

    def agregar(self, sku):
        if not sku.startswith("X"):
            raise ValueError("el SKU tiene que empezar con X")
        self.__productos.append(sku)

    def obtener(self):
        return self.__productos          # devuelve la lista, no una copia


carrito = CarritoConFuga()
carrito.agregar("X1")

print("Por la puerta principal:", carrito.obtener())

carrito.obtener().append("basura sin validar")
carrito.obtener().append(42)

print("Por la fuga:            ", carrito.obtener())
print("Productos:", len(carrito.obtener()))
print()
print("¿Sigue valiendo la validación?")
try:
    carrito.agregar("Z9")
except ValueError as e:
    print("  Por agregar:", e)
print("  Por obtener: ninguna. La lista acepta lo que sea.")
"""),

md("""
La respuesta del quiz es **B**.

`obtener` devolvió **la lista**, no una copia, y desde ese momento quien la tenga puede hacer con ella
lo que quiera. El validador de `agregar` sigue ahí, intacto, y completamente rodeado.

Los dos guiones bajos protegieron el **nombre** del atributo. No protegieron el objeto que hay dentro.
Encapsular el nombre no encapsula la lista.

**Y aquí está el párrafo que vengo prometiendo desde el repaso 3.**

Cuando dos nombres apuntan al mismo objeto mutable, escribir por cualquiera de los dos se ve por los
dos. Eso es lo que pasó en el repaso 3 con la lista por omisión, que era una sola para todas las
llamadas. Es lo que pasó en el repaso 4 con `b = a`, que no copiaba nada. Es lo que pasó en la semana 3
con el carrito declarado en el cuerpo de la clase, que era uno solo para todos los objetos. Es lo que
pasó en la semana 5 con la lista en la firma del constructor.

Y es lo que acaba de pasar aquí, con la diferencia de que esta vez el segundo nombre está **fuera de la
clase**, en manos de alguien que ni sabe que existe una regla.

Las cuatro son la misma frase: **asignar no copia**. Lo que cambia es quién termina con el segundo
nombre.

## Las dos correcciones, y la que no alcanza
"""),

code("""
class CarritoCopia:
    def __init__(self):
        self.__productos = []

    def agregar(self, sku):
        if not sku.startswith("X"):
            raise ValueError("el SKU tiene que empezar con X")
        self.__productos.append(sku)

    def obtener(self):
        return list(self.__productos)    # una copia


class CarritoTupla:
    def __init__(self):
        self.__productos = []

    def agregar(self, sku):
        if not sku.startswith("X"):
            raise ValueError("el SKU tiene que empezar con X")
        self.__productos.append(sku)

    def obtener(self):
        return tuple(self.__productos)   # algo que no se puede modificar


for clase in [CarritoCopia, CarritoTupla]:
    c = clase()
    c.agregar("X1")
    try:
        c.obtener().append("basura")
    except AttributeError as e:
        print(f"{clase.__name__:<16}AttributeError: {e}")
    else:
        print(f"{clase.__name__:<16}el append funcionó, pero sobre la copia")
    print(f"{'':<16}Productos reales: {len(c.obtener())}")
"""),

md("""
Las dos cierran la fuga y lo hacen de maneras distintas.

`list(...)` devuelve una copia. El `append` de afuera funciona y no afecta a nadie, porque la lista que
modificó ya no es la del carrito.

`tuple(...)` devuelve algo que no se puede modificar. El `append` truena con un `AttributeError`, y quien
lo escribió se entera en el momento en lugar de creer que hizo algo.

Prefiero la tupla cuando puedo. Un error que truena en la línea equivocada vale más que un silencio que
funciona.

## La misma fuga, en la dirección contraria

Cerramos la salida. Falta la entrada.
"""),

code("""
# FALLA A PROPÓSITO, y no truena. La clase se queda con la lista que le pasaron.
class CarritoQueGuarda:
    def __init__(self, iniciales=None):
        self.__productos = iniciales if iniciales is not None else []

    def agregar(self, sku):
        if not sku.startswith("X"):
            raise ValueError("el SKU tiene que empezar con X")
        self.__productos.append(sku)

    def cuantos(self):
        return len(self.__productos)


mios = ["X1", "X2"]
carrito = CarritoQueGuarda(mios)
print("Al construir:", carrito.cuantos())

mios.append("basura sin validar")        # tocando mi propia lista, no la del carrito
mios.append(42)

print("Después de tocar mi lista:", carrito.cuantos())
print("Mi lista:", mios)
print()


class CarritoQueCopia:
    def __init__(self, iniciales=None):
        self.__productos = list(iniciales) if iniciales else []

    def agregar(self, sku):
        if not sku.startswith("X"):
            raise ValueError("el SKU tiene que empezar con X")
        self.__productos.append(sku)

    def cuantos(self):
        return len(self.__productos)


mios = ["X1", "X2"]
seguro = CarritoQueCopia(mios)
mios.append("basura sin validar")
print("Con copia defensiva:", seguro.cuantos(), "<- se quedó en 2")
"""),

md("""
El carrito creció sin que nadie llamara a `agregar`.

Es la fuga de hace dos celdas al revés. Ahí la lista salía de la clase; aquí entró, y el que la
construyó se quedó con el otro nombre. El atributo es privado, la validación existe, y el estado del
objeto lo controla alguien de fuera que ni sabe que hay reglas.

`list(iniciales)` en el constructor cierra esa puerta, y es exactamente la línea que apareció en la
semana 5 cuando arreglamos el valor por omisión. Se llama **copia defensiva**, y la regla es corta:
**copia lo que entra y copia lo que sale.**

Ahora la corrección que parece corrección.
"""),

code("""
# FALLA A PROPÓSITO, y no truena. La copia que solo copia el primer nivel.
class Pedido:
    def __init__(self, cliente):
        self.__cliente = cliente
        self.__lineas = [{"sku": "X1", "cantidad": 1}]

    def agregar(self, sku, cantidad):
        if cantidad <= 0:
            raise ValueError("la cantidad tiene que ser positiva")
        self.__lineas.append({"sku": sku, "cantidad": cantidad})

    def obtener(self):
        return list(self.__lineas)       # copia la lista, no los diccionarios

    def total(self):
        return sum(linea["cantidad"] for linea in self.__lineas)


pedido = Pedido("Ana")
pedido.agregar("X2", 3)

print("Total antes:", pedido.total())

copia = pedido.obtener()
copia.append({"sku": "X9", "cantidad": 5})     # esto sí queda fuera
copia[0]["cantidad"] = -1000                   # esto no

print("Total después:", pedido.total())
print("Renglones del pedido:", len(pedido.obtener()))
print("Primer renglón:", pedido.obtener()[0])
"""),

md("""
El `append` sobre la copia no llegó al pedido. La asignación dentro del primer renglón sí.

`list(otra_lista)` construye una lista nueva **con las mismas referencias adentro**. Los diccionarios no
se duplicaron: la copia y el original apuntan a los mismos. Se llama copia superficial, y es la
corrección a medias que más veces he visto.

Las salidas: `copy.deepcopy`, que duplica todo hacia abajo y cuesta lo que cuesta; guardar objetos
inmutables en lugar de diccionarios, que en la semana 8 se vuelve una clase con `__eq__`; o no devolver
la estructura y ofrecer en su lugar los métodos que responden las preguntas que la gente realmente hace,
como `total()`.

La tercera es casi siempre la correcta. **Si nadie necesita la lista, no la devuelvas.**

## Cerrar todo tampoco es la respuesta
"""),

code("""
# FALLA A PROPÓSITO. Una clase donde nada es público.
class InventarioCerrado:
    def __init__(self):
        self.__productos = {}

    def __agregar(self, sku, cantidad):
        self.__productos[sku] = cantidad

    def __contar(self):
        return len(self.__productos)


inv = InventarioCerrado()
publicos = [n for n in dir(inv) if not n.startswith("_")]
print("Miembros públicos:", publicos, "->", len(publicos))

try:
    inv.__agregar("X1", 5)
except AttributeError as e:
    print("AttributeError:", e)

print()
print("La única forma de usarla:")
inv._InventarioCerrado__agregar("X1", 5)
print("  inv._InventarioCerrado__agregar('X1', 5)")
print("  productos:", inv._InventarioCerrado__contar())
"""),

md("""
Cero miembros públicos, y la clase es inservible hasta que alguien escribe el nombre renombrado.

En cuanto la primera persona escriba `inv._InventarioCerrado__agregar(...)`, ese nombre pasó a ser el
contrato de hecho, y ahora no puedes cambiarlo sin romperle el programa. Cerrar todo no produjo una
clase más segura, produjo una interfaz peor con los mismos compromisos.

**Empieza con todo público y cierra lo que tengas una razón para cerrar.** Es la misma regla de la
semana 4, y aquí se ve por qué: la interfaz pública no es lo que sobra después de cerrar, es una
decisión de diseño que se toma mirando quién va a usar la clase.

## Cuatro maneras de encapsular a medias

| | El error | Cómo se ve |
|---|---|---|
| 01 | Encapsular y devolverlo entero | El getter regresa la lista interna y cualquiera la modifica |
| 02 | Confundir encapsular con ocultar | Dos guiones bajos en todo, sin una promesa detrás |
| 03 | Cerrar todo desde el primer día | La clase no le sirve a nadie y la abres a la primera petición |
| 04 | La regla repetida fuera de la clase | Tres archivos hacen `.lower()` y el cuarto se olvida |
"""),

md("""
---
# Bloque 3 · Reutilización

Tres maneras de no escribir el mismo código dos veces, en orden de menos a más compromiso.

**Función.** El comportamiento no depende de ningún estado, así que no necesita una clase. Es la más
barata y la que casi nadie considera.

**Composición.** La clase recibe instancias de otras y les delega el trabajo que no le toca. Cambiar una
pieza cuesta una línea.

**Herencia.** La clase toma el comportamiento del padre y queda atada a cada cambio suyo. Es la más
rígida de las tres y la que más se usa por costumbre.

El archivo `Code021.py` del módulo 6 arma una computadora por composición. Es el ejemplo del deck.
"""),

code("""
class CPU:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def ejecutar(self):
        print(f"  {self.marca} {self.modelo}: ejecutando...")


class Disco:
    def __init__(self, capacidad):
        self.capacidad = capacidad

    def leer(self, archivo):
        print(f"  Disco duro de {self.capacidad}: leyendo {archivo}...")


class Computadora:
    def __init__(self, cpu, disco):
        self.cpu = cpu
        self.disco = disco

    def iniciar(self, programa):
        self.disco.leer(f"{programa}.exe")
        self.cpu.ejecutar()


mia = Computadora(CPU("Intel", "i7"), Disco("1TB"))
mia.iniciar("Photoshop")
"""),

md("""
`Computadora` no hereda de nada. Recibe las piezas ya armadas y les pide lo que necesita.

Fíjate en lo que `Computadora` sabe de un disco: que tiene un método `leer`. No sabe si es mecánico, si
es de estado sólido o si está en la nube, y no le hace falta.
"""),

code("""
class SSD:
    def __init__(self, capacidad):
        self.capacidad = capacidad

    def leer(self, archivo):
        print(f"  SSD de {self.capacidad}: leyendo {archivo} (rápido)...")


class DiscoDeRed:
    def __init__(self, servidor):
        self.servidor = servidor

    def leer(self, archivo):
        print(f"  Red: pidiendo {archivo} a {self.servidor}...")


discos = [Disco("1TB"), SSD("500GB"), DiscoDeRed("nas.local")]
armadas = []
for disco in discos:
    compu = Computadora(CPU("Intel", "i7"), disco)
    compu.iniciar("Photoshop")
    armadas.append(compu)

print()
print(f"{len(discos)} discos distintos, {len(armadas)} computadoras armadas")
print("Clases de Computadora involucradas:", len({type(c) for c in armadas}))
print("Lo único que Computadora les pide:  un método llamado leer ->",
      all(hasattr(d, "leer") for d in discos))
print("Lo que tienen en común además de eso:",
      sorted(set.intersection(*[{n for n in dir(d) if not n.startswith("_")}
                                for d in discos])))
"""),

md("""
Tres discos distintos, ninguna línea de `Computadora` tocada, y una sola clase `Computadora` en los
tres casos.

La última línea es la que vale: lo único que los tres discos tienen en común es el método `leer`. No
comparten clase madre, no comparten atributos, no se conocen entre ellos.

Eso es lo que hace flexible a la composición: el compromiso entre `Computadora` y sus piezas es un
método, no una jerarquía. Cualquier objeto que sepa `leer` sirve.

En la semana 8 esto tiene nombre. Se llama **polimorfismo**, y lo que acabas de escribir es la versión
que Python prefiere: sin clase base, sin declaraciones, sin nada más que el método que hace falta.

## La herencia usada donde no toca
"""),

code("""
# FALLA A PROPÓSITO, y no truena. Heredar para reutilizar, en lugar de componer.
class ComputadoraHeredera(Disco, CPU):
    def __init__(self, capacidad, marca, modelo):
        Disco.__init__(self, capacidad)
        CPU.__init__(self, marca, modelo)

    def iniciar(self, programa):
        self.leer(f"{programa}.exe")
        self.ejecutar()


rara = ComputadoraHeredera("1TB", "Intel", "i7")
rara.iniciar("Photoshop")

print()
print("¿Una computadora es un disco?  ", isinstance(rara, Disco))
print("¿Una computadora es un CPU?    ", isinstance(rara, CPU))
print("Capacidad de la computadora:   ", rara.capacidad)
print("Métodos que quedaron a la vista:",
      sorted(n for n in dir(rara) if not n.startswith("_")))
"""),

md("""
Corre, imprime lo mismo, y ahora una computadora **es** un disco duro.

Nada truena. Lo que se rompió es el modelo: `rara.leer("cualquier_cosa.txt")` es una llamada legal, la
computadora tiene un atributo `capacidad` que es la del disco, y si mañana quieres dos discos, no hay
manera.

La prueba está en la palabra. La herencia dice **"es un"**: un `Camion` es un `Vehiculo`, un `Perro` es
un `Animal`. La composición dice **"tiene un"**: una computadora tiene un disco. Cuando la frase con
"es un" suena rara al decirla en voz alta, la herencia no era.

Es el mismo error que el archivo `Code021.py` señala con la gallina que hereda de `Ave` y por lo tanto
puede volar. La semana 7 le dedica el bloque entero.

## Lo que cuesta la herencia cuando el padre cambia
"""),

code("""
# FALLA A PROPÓSITO. La clase base frágil.
class Almacen:
    def __init__(self):
        self._datos = {}

    def guardar(self, clave, valor):
        self._datos[clave] = valor


class AlmacenConBitacora(Almacen):
    def __init__(self):
        super().__init__()
        self.bitacora = []

    def guardar(self, clave, valor):
        self.bitacora.append(clave)
        super().guardar(clave, valor)


a = AlmacenConBitacora()
a.guardar("x", 1)
print("Funciona:", a._datos, a.bitacora)


# Seis meses después, alguien renombra el método en la clase base.
class Almacen:
    def __init__(self):
        self._datos = {}

    def escribir(self, clave, valor):     # antes se llamaba guardar
        self._datos[clave] = valor


class AlmacenConBitacora(Almacen):
    def __init__(self):
        super().__init__()
        self.bitacora = []

    def guardar(self, clave, valor):
        self.bitacora.append(clave)
        super().guardar(clave, valor)


b = AlmacenConBitacora()
try:
    b.guardar("x", 1)
except AttributeError as e:
    print("AttributeError:", e)
"""),

md("""
La clase hija no cambió una sola línea y dejó de funcionar.

Se llama **problema de la clase base frágil**: una subclase depende de los detalles internos de su
padre, así que un cambio que el padre considera interno rompe a todos sus descendientes. Cuanto más
larga la cadena, más lejos viaja el daño.

Con composición esto no pasa de la misma manera. Si `AlmacenConBitacora` recibiera un almacén en el
constructor y le delegara, el cambio de nombre rompería una línea, la de la delegación, y en un lugar
que se ve.

**La composición se prefiere porque una pieza se cambia sin tocar las demás.** La herencia se gana el
lugar cuando de verdad hay una relación de "es un", y la semana 7 se dedica a ese caso.

## Cuándo ninguna de las dos: una función
"""),

code("""
def normalizar(etiqueta: str) -> str:
    return etiqueta.strip().lower()


print(normalizar("  Python  "))
print(normalizar("SQL"))
print()
print("Ni clase, ni herencia, ni composición. No guarda nada entre llamadas.")
print("Es el paso 2 del modelado de la semana pasada, aplicado al revés.")
"""),

md("""
Antes de decidir entre composición y herencia, vale la pena preguntarse si hace falta una clase.

Si el comportamiento no depende de ningún estado, una función suelta hace el trabajo, se prueba en dos
líneas y no obliga a nadie a construir un objeto para usarla. Es la opción más barata de las tres y la
que menos se considera, porque suena a que uno no está haciendo POO.
"""),

md("""
---
## Cuatro errores de esta sesión

**El getter que devuelve la estructura interna.** La lista sale de la clase y desde ahí cualquiera la
modifica sin pasar por ninguna validación. Devuelve una copia, una tupla, o mejor: no la devuelvas.

**La copia superficial.** `list(otra)` duplica el envase y no el contenido. Si adentro hay
diccionarios u objetos, siguen siendo los mismos.

**Cerrar todo desde el primer día.** Una clase sin miembros públicos no le sirve a nadie, y el primero
que escriba el nombre renombrado convierte ese nombre en el contrato.

**Heredar para reutilizar.** Si la frase con "es un" suena rara, era composición. Y una vez heredado,
cualquier cambio en el padre viaja hacia abajo.
"""),

md("""
---
# Ejercicios

El laboratorio de esta semana es cerrar un inventario sin cambiar el archivo de pruebas. Los ejercicios
construyen hacia eso.

Las soluciones están hasta abajo del cuaderno.

### Ejercicio 1 · La puerta de atrás

Escribe una clase con un diccionario público y una regla dentro de un método. Úsala bien tres veces,
después escribe directo en el diccionario saltándote la regla, y muestra con un conteo cuántas llaves
quedaron de más.

### Ejercicio 2 · Cerrarla

Cierra la clase del ejercicio 1 con dos guiones bajos y agrégale `__getitem__`, `__setitem__`, `__len__`
y `__iter__`. Repite las mismas operaciones y compara los dos conteos.

### Ejercicio 3 · La prueba del cambio

Escribe una función `probar(clase)` con seis comprobaciones sobre tu clase cerrada. Después escribe una
segunda implementación que por dentro use una lista de pares en lugar de un diccionario.

Corre la misma función sobre las dos y reporta cuántas pasaron. Si tuviste que cambiar la función,
di qué parte del contrato se te había escapado.

### Ejercicio 4 · La fuga

Escribe una clase con una lista privada, un método que valide antes de agregar, y un getter que
devuelva la lista tal cual. Métele basura por la fuga y demuestra que la validación no se enteró.

### Ejercicio 5 · Las tres correcciones

Del ejercicio 4, escribe tres versiones del getter: una que devuelva una copia, una que devuelva una
tupla, y una que no devuelva la lista sino la respuesta a una pregunta concreta.

Explica en un comentario cuál elegirías y por qué.

### Ejercicio 6 · La copia que no alcanza

Escribe una clase que guarde una lista de diccionarios y un getter que devuelva `list(...)`. Demuestra
que el `append` de afuera no llega pero la modificación de un diccionario sí.

Arréglalo de dos maneras distintas.

### Ejercicio 7 · Composición

Escribe `Reproductor` que reciba un `Altavoz` y una `Pantalla` en el constructor. Después escribe un
segundo altavoz con el mismo método y cámbialo sin tocar `Reproductor`.

Cuenta cuántas líneas de `Reproductor` tuviste que modificar.

### Ejercicio 8 · La herencia que no era

Escribe `Reproductor` heredando de `Altavoz` y `Pantalla` en lugar de componerlos. Muestra con
`isinstance` qué quedó afirmando el modelo, y di en voz alta la frase con "es un" para ver si se
sostiene.

### Ejercicio 9 · El laboratorio

Te entregan una clase `Inventario` con un diccionario público de productos y un archivo de pruebas.
Ciérrala sin cambiar ni una línea del archivo de pruebas.

El diccionario queda privado y la clase expone `agregar`, corchetes y `len`. Pedir un producto que no
existe tiene que devolver cero en lugar de lanzar `KeyError`.

Entrega el archivo `.py` con la clase cerrada y el archivo de pruebas tal como te lo dieron.
"""),

md("""
---
## Tres ideas para llevarse

**Encapsular junta, ocultar decide.** Lo primero pone el dato y su regla en la misma clase; lo segundo
elige qué se asoma hacia afuera. Son dos decisiones distintas y la segunda es la que cuesta trabajo.

**Un getter puede deshacer todo el encapsulamiento.** Si devuelve la estructura interna, los dos guiones
bajos protegieron un nombre y nada más. Es la misma frase que arrastramos desde el repaso 3: asignar no
copia.

**La composición reutiliza mejor que la herencia.** Cambiar una pieza que se recibe cuesta una línea;
cambiar un padre cuesta toda la rama. Y antes de elegir entre las dos, pregúntate si hacía falta una
clase.

La semana 7 se dedica a la herencia: qué recibe una clase de su padre, hasta dónde conviene que crezca
el árbol, y el guion bajo simple que sí tiene un uso técnico, el de abrirle la puerta a las hijas.

### La pregunta que resuelve casi todo esta semana

Antes de dejar un miembro público, pregúntate: **¿estoy dispuesto a sostener esto sin cambios durante
dos años?** Si la respuesta es no, ciérralo hoy, mientras nadie depende de él todavía.
"""),

md("""
---
# Soluciones

### Ejercicio 1

```python
class Agenda:
    def __init__(self):
        self.contactos = {}

    def guardar(self, nombre, telefono):
        self.contactos[nombre.strip().title()] = telefono


a = Agenda()
a.guardar("ana robles", "555-1111")
a.guardar("  LUIS FERRER ", "555-2222")
a.guardar("Paula Ines", "555-3333")
print(a.contactos)

a.contactos["ana robles"] = "555-9999"      # por la puerta de atrás

print(a.contactos)
esperadas = len({n.strip().title() for n in
                 ["ana robles", "  LUIS FERRER ", "Paula Ines"]})
print(f"{len(a.contactos)} llaves para {esperadas} contactos reales")
```

### Ejercicio 2

```python
class AgendaCerrada:
    def __init__(self):
        self.__contactos = {}

    def __clave(self, nombre):
        return nombre.strip().title()

    def guardar(self, nombre, telefono):
        self.__contactos[self.__clave(nombre)] = telefono

    def __getitem__(self, nombre):
        return self.__contactos.get(self.__clave(nombre), "")

    def __setitem__(self, nombre, telefono):
        self.__contactos[self.__clave(nombre)] = telefono

    def __len__(self):
        return len(self.__contactos)

    def __iter__(self):
        return iter(self.__contactos)


b = AgendaCerrada()
for nombre, tel in [("ana robles", "555-1111"), ("  LUIS FERRER ", "555-2222"),
                    ("Paula Ines", "555-3333")]:
    b.guardar(nombre, tel)

b["ana robles"] = "555-9999"                # la misma línea, ahora normalizada

print(len(b), "llaves")
print(b["ANA ROBLES"])
print(b["no existe"], "<- cadena vacía en lugar de KeyError")
```

### Ejercicio 3

```python
def probar(clase):
    a = clase()
    a.guardar("ana robles", "555-1111")
    a.guardar("Ana Robles", "555-9999")
    a.guardar("luis ferrer", "555-2222")
    return [
        ("ana se normaliza", a["ANA ROBLES"] == "555-9999"),
        ("luis está", a["Luis Ferrer"] == "555-2222"),
        ("el que falta da vacío", a["nadie"] == ""),
        ("hay 2 contactos", len(a) == 2),
        ("se recorre", sorted(a) == ["Ana Robles", "Luis Ferrer"]),
        ("los corchetes escriben", (a.__setitem__("x y", "1"), a["X Y"])[1] == "1"),
    ]


class AgendaDeListas:
    def __init__(self):
        self.__pares = []

    def __clave(self, nombre):
        return nombre.strip().title()

    def __buscar(self, clave):
        for par in self.__pares:
            if par[0] == clave:
                return par
        return None

    def guardar(self, nombre, telefono):
        self[nombre] = telefono

    def __getitem__(self, nombre):
        par = self.__buscar(self.__clave(nombre))
        return par[1] if par else ""

    def __setitem__(self, nombre, telefono):
        clave = self.__clave(nombre)
        par = self.__buscar(clave)
        if par is None:
            self.__pares.append([clave, telefono])
        else:
            par[1] = telefono

    def __len__(self):
        return len(self.__pares)

    def __iter__(self):
        return iter(c for c, _ in self.__pares)


for clase in [AgendaCerrada, AgendaDeListas]:
    resultados = probar(clase)
    print(clase.__name__, sum(1 for _, ok in resultados if ok), "de", len(resultados))
```

### Ejercicio 4

```python
class ListaDeCorreo:
    def __init__(self):
        self.__direcciones = []

    def suscribir(self, correo):
        if "@" not in correo:
            raise ValueError("eso no es un correo")
        self.__direcciones.append(correo)

    def obtener(self):
        return self.__direcciones


lista = ListaDeCorreo()
lista.suscribir("ana@up.edu.mx")

try:
    lista.suscribir("no es un correo")
except ValueError as e:
    print("Por la puerta:", e)

lista.obtener().append("no es un correo")       # por la fuga
lista.obtener().append(None)

print(lista.obtener())
print("Direcciones válidas:",
      sum(1 for d in lista.obtener() if isinstance(d, str) and "@" in d),
      "de", len(lista.obtener()))
```

### Ejercicio 5

```python
class ListaSegura:
    def __init__(self):
        self.__direcciones = []

    def suscribir(self, correo):
        if "@" not in correo:
            raise ValueError("eso no es un correo")
        self.__direcciones.append(correo)

    def obtener_copia(self):
        return list(self.__direcciones)

    def obtener_tupla(self):
        return tuple(self.__direcciones)

    def cuantos(self):
        return len(self.__direcciones)

    def esta_suscrito(self, correo):
        return correo in self.__direcciones


lista = ListaSegura()
lista.suscribir("ana@up.edu.mx")

lista.obtener_copia().append("basura")
print("Después de tocar la copia:", lista.cuantos())

try:
    lista.obtener_tupla().append("basura")
except AttributeError as e:
    print("La tupla se defiende:", e)

print("¿Está suscrita Ana?", lista.esta_suscrito("ana@up.edu.mx"))

# Elegiría la tercera. Nadie que use esta clase necesita la lista: necesita saber
# cuántos hay y si alguien está. Devolver esas dos respuestas cierra la fuga sin
# copiar nada, y además me deja cambiar la lista por un set mañana.
```

### Ejercicio 6

```python
import copy


class Carrito:
    def __init__(self):
        self.__lineas = [{"sku": "X1", "cantidad": 1}]

    def obtener_superficial(self):
        return list(self.__lineas)

    def obtener_profundo(self):
        return copy.deepcopy(self.__lineas)

    def obtener_congelado(self):
        return tuple(tuple(sorted(linea.items())) for linea in self.__lineas)

    def total(self):
        return sum(l["cantidad"] for l in self.__lineas)


c = Carrito()
c.obtener_superficial().append({"sku": "X9", "cantidad": 9})
print("Tras el append:", c.total())

c.obtener_superficial()[0]["cantidad"] = 999
print("Tras tocar el diccionario:", c.total(), "<- se coló")

d = Carrito()
d.obtener_profundo()[0]["cantidad"] = 999
print("Con deepcopy:", d.total())

e = Carrito()
print("Congelado:", e.obtener_congelado())
```

### Ejercicio 7

```python
class Altavoz:
    def sonar(self, pista):
        print(f"  altavoz: reproduciendo {pista}")


class AltavozBluetooth:
    def __init__(self, nombre):
        self.nombre = nombre

    def sonar(self, pista):
        print(f"  {self.nombre} por bluetooth: reproduciendo {pista}")


class Pantalla:
    def mostrar(self, texto):
        print(f"  pantalla: {texto}")


class Reproductor:
    def __init__(self, altavoz, pantalla):
        self.altavoz = altavoz
        self.pantalla = pantalla

    def reproducir(self, pista):
        self.pantalla.mostrar(f"Ahora suena: {pista}")
        self.altavoz.sonar(pista)


Reproductor(Altavoz(), Pantalla()).reproducir("Bohemian Rhapsody")
Reproductor(AltavozBluetooth("JBL"), Pantalla()).reproducir("Bohemian Rhapsody")

# Cero líneas de Reproductor. El compromiso es un método llamado sonar, y
# cualquier objeto que lo tenga entra.
```

### Ejercicio 8

```python
class ReproductorHeredero(Altavoz, Pantalla):
    def reproducir(self, pista):
        self.mostrar(f"Ahora suena: {pista}")
        self.sonar(pista)


r = ReproductorHeredero()
r.reproducir("Bohemian Rhapsody")

print("¿Un reproductor es un altavoz?", isinstance(r, Altavoz))
print("¿Un reproductor es una pantalla?", isinstance(r, Pantalla))

# "Un reproductor es un altavoz" es falso y suena falso al decirlo. Un
# reproductor tiene un altavoz. Además, con herencia no hay manera de darle dos
# altavoces, y cambiar el altavoz obliga a cambiar la declaración de la clase.
```

### Ejercicio 9

```python
# pruebas.py, tal como te lo entregaron. No se toca.
def correr_pruebas(Inventario):
    inv = Inventario()
    inv.agregar("X1", 5)
    inv.agregar("X2", 3)
    inv.agregar("X1", 2)

    assert inv["X1"] == 7, "las cantidades se suman"
    assert inv["X2"] == 3
    assert inv["NO EXISTE"] == 0, "un producto que no está vale cero"
    assert len(inv) == 2
    inv["X3"] = 10
    assert inv["X3"] == 10
    return "las 5 pruebas pasaron"


# inventario.py, la clase cerrada.
class Inventario:
    def __init__(self):
        self.__productos = {}

    def agregar(self, sku, cantidad):
        if cantidad <= 0:
            raise ValueError("la cantidad tiene que ser positiva")
        self.__productos[sku] = self.__productos.get(sku, 0) + cantidad

    def __getitem__(self, sku):
        return self.__productos.get(sku, 0)

    def __setitem__(self, sku, cantidad):
        self.__productos[sku] = cantidad

    def __len__(self):
        return len(self.__productos)

    def __iter__(self):
        return iter(self.__productos)


print(correr_pruebas(Inventario))
```

Tres decisiones que vale la pena defender en la entrega.

**`__getitem__` devuelve cero y no lanza.** Un producto que no está en el inventario tiene cantidad
cero; eso es una respuesta, no un error. `KeyError` obligaría a cada lugar que consulta a envolverse en
un `try`, y esa es la regla mudándose fuera de la clase otra vez.

**No hay un método `obtener_productos`.** Nadie de fuera necesita el diccionario. Si mañana alguien lo
pide, la pregunta correcta es qué quiere hacer con él, porque casi siempre la respuesta es un método
nuevo y no una fuga.

**La validación vive en `agregar`.** Las cantidades negativas se rechazan en el único lugar donde entran
cantidades por la puerta principal. Fíjate en que `__setitem__` no valida, y eso es un hueco real de
esta solución: si el archivo de pruebas lo permitiera, cerrarlo sería la siguiente línea.
"""),

]

write(OUT / "es" / "w06.ipynb", es)
print("wrote", OUT / "es" / "w06.ipynb")
