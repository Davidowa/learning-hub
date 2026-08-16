"""notebooks/programacion-orientada-a-objetos/es/w05.ipynb

Source deck: ppts/python/programacion-orientada-a-objetos/es/w05.es.yaml
Source code:  docs/en/courses/python-course/02 - POO/6th Module/Code022.py
                  (bloque de métodos mágicos, líneas 70 a 206)
              docs/en/courses/python-course/02 - POO/6th Module/Code023.py
                  (contenedores propios: __getitem__, __setitem__, __len__, __iter__)
              docs/en/courses/python-course/02 - POO/6th Module/MagicMethods.md

Code022.py no corre completo: se detiene en su línea 62, que es la trampa que
cita la semana 4. El bloque de métodos mágicos vive después de esa línea, así
que en el archivo original nunca se ejecuta. Aquí se cita el código de las
líneas 92 en adelante, comprobado a mano, y el cuaderno lo dice.

Los módulos y el paquete del bloque 3 se escriben con open() en el directorio de
trabajo antes de importarlos, que es lo que hace el resto del kit.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from nbkit import md, code, write, REPO

OUT = REPO / "notebooks" / "programacion-orientada-a-objetos"

es = [

md("""
# Programación Orientada a Objetos · Semana 05
## Tema 2 · Elementos básicos

**COM102 · Facultad de Ingeniería · Profesor David Escobar-Castillejos**

Un mismo nombre para varias formas de llamar, los operadores que se pueden enseñar a trabajar con tus
objetos, dónde vive cada clase cuando el proyecto crece, y el paso del enunciado al modelo.

Esta semana cierra el tema 2. Las tres anteriores construyeron una clase; esta enseña a que se deje
usar, a que se deje encontrar y a que se haya pensado antes de escribirse.

Al terminar vas a poder:

1. Explicar por qué el segundo `def` con el mismo nombre borra al primero.
2. Cubrir varias formas de llamada con un solo método, con valores por omisión, `*args` y `**kwargs`.
3. Sobrecargar `__str__`, `__eq__` y `__add__`, y decir qué se rompe cuando falta cada uno.
4. Repartir clases en módulos y paquetes, y saber qué corre en el momento de importar.
5. Sacar las clases de un enunciado sin inventar una que se llame Gestor.

### Cómo se usa este cuaderno

Ejecuta las celdas en orden con **Shift + Enter**. Doce fallan a propósito y llevan un comentario que
lo dice.

Nueve de las doce **no lanzan ninguna excepción**, que es la proporción más alta del curso hasta ahora.
Casi todo lo de esta semana falla sin avisar, porque casi todo produce un objeto que existe y una
salida que se ve razonable. El bloque 3 escribe archivos de verdad en el
directorio de trabajo, así que las celdas de módulos hay que correrlas en orden o los `import` no van a
encontrar nada.
"""),

md("""
---
# Bloque 1 · Métodos sobrecargados

En Java o en C# puedes escribir dos métodos con el mismo nombre y distinta firma, y el compilador
decide cuál llamar según los argumentos. Eso se llama sobrecarga, y **Python no la tiene**.

Vale la pena entender por qué no, porque la razón explica media docena de comportamientos que si no se
ven arbitrarios.

## Predice antes de correr

```python
class Calculadora:
    def sumar(self, a, b):
        return a + b

    def sumar(self, a, b, c):
        return a + b + c


c = Calculadora()
print(c.sumar(1, 2))
```

- **A.** 3, porque Python elige el método de dos parámetros.
- **B.** `TypeError`, falta un argumento posicional.
- **C.** 6, porque `c` vale cero cuando no se pasa.
- **D.** `SyntaxError`, `sumar` está definido dos veces.
"""),

code("""
# FALLA A PROPÓSITO. Dos métodos con el mismo nombre, y solo sobrevive uno.
class Calculadora:
    def sumar(self, a, b):
        return a + b

    def sumar(self, a, b, c):
        return a + b + c


calc = Calculadora()

try:
    print(calc.sumar(1, 2))
except TypeError as e:
    print("TypeError:", e)

print()
print("Con tres argumentos sí:", calc.sumar(1, 2, 3))
print()
print("Métodos que quedaron en la clase:", [n for n in vars(Calculadora) if not n.startswith("__")])
print("Parámetros que acepta sumar:", Calculadora.sumar.__code__.co_varnames[:4])
"""),

md("""
La respuesta es **B**.

En la clase quedó **un** `sumar`, no dos. El cuerpo de una clase se ejecuta de arriba abajo como
cualquier otro bloque, y cada `def` es una asignación: mete una función en el diccionario de la clase
bajo ese nombre. La segunda asignación pisa a la primera, igual que `x = 1` seguido de `x = 2`.

Es el mismo mecanismo de la función redefinida del repaso 3 y el de la clase redefinida de la semana 4.
Tercera aparición, tercer disfraz, misma frase: **un nombre guarda un valor**.

Lo que Python ofrece en su lugar es mejor, y cabe en una línea.
"""),

code("""
class Calculadora:
    def sumar(self, a, b, c=0):
        return a + b + c


calc = Calculadora()
print("Dos argumentos: ", calc.sumar(1, 2))
print("Tres argumentos:", calc.sumar(1, 2, 3))
print()
print("Un solo método:", [n for n in vars(Calculadora) if not n.startswith("__")])
"""),

md("""
Un método, dos formas de llamarlo, cero ambigüedad sobre cuál corre.

La tabla de equivalencias, para tenerla junta.

| Necesidad | En Java o C# | En Python |
|---|---|---|
| Un parámetro opcional | Dos métodos con firma distinta | `def saludar(self, formal=False)` |
| Cuántos datos sean | Un método por cantidad | `def agregar(self, *skus)` |
| Opciones con nombre | Un objeto de configuración | `def crear(self, **opciones)` |
| Tipos distintos | Una firma por tipo | `isinstance` o `functools.singledispatch` |
| Operadores propios | operator overloading | `__add__` · `__eq__` · `__str__` |

## Cuando no sabes cuántos van a llegar
"""),

code("""
class Carrito:
    def __init__(self, dueno: str) -> None:
        self.dueno = dueno
        self.productos: list[str] = []

    def agregar(self, *skus: str, **opciones: bool) -> None:
        for sku in skus:
            self.productos.append(sku)
        if opciones.get("avisar"):
            print(f"{len(skus)} productos agregados")


carrito = Carrito("Ana")

carrito.agregar("X1")
carrito.agregar("X2", "X3", avisar=True)
carrito.agregar()                        # cero argumentos también es válido

print()
print("Carrito:", carrito.productos)
print("Productos:", len(carrito.productos))
"""),

md("""
`*skus` recoge en una **tupla** cuantos argumentos posicionales lleguen, incluyendo ninguno.
`**opciones` recoge en un **diccionario** los que vengan con nombre.

Los dos asteriscos son la misma idea aplicada a las dos mitades de una llamada. Y los nombres `args` y
`kwargs` son pura costumbre: lo que hace el trabajo es el asterisco, no la palabra.

Ahora las dos maneras de que esto te salga mal sin que nadie te avise.
"""),

code("""
# FALLA A PROPÓSITO, y no truena. Pasarle una lista a un método que espera argumentos sueltos.
otro = Carrito("Luis")
otro.agregar(["X1", "X2", "X3"])

print("Carrito:", otro.productos)
print("Productos:", len(otro.productos), "<- esperábamos 3")
print("Tipo del primero:", type(otro.productos[0]).__name__)
print()
print("Con el asterisco al llamar:")
tercero = Carrito("Sofía")
tercero.agregar(*["X1", "X2", "X3"])
print("Productos:", len(tercero.productos))
"""),

md("""
Un producto que es una lista de tres productos.

`*skus` no desempaqueta lo que le llegue, recoge lo que le manden. Si le mandas una lista, la lista
entera es un argumento posicional y `skus` vale `(["X1", "X2", "X3"],)`, una tupla de un elemento.

El asterisco del lado de la llamada es el que desempaqueta. `agregar(*lista)` reparte los tres
elementos en tres argumentos, y por eso la segunda parte de la celda sí cuenta tres.

El síntoma aparece tarde y disfrazado: el carrito dice que tiene un producto, y la primera vez que
alguien haga `sku.upper()` va a recibir un `AttributeError` sobre una lista, muy lejos de aquí.
"""),

code("""
# FALLA A PROPÓSITO, y no truena. Una opción con el nombre mal escrito.
cuarto = Carrito("Marco")
cuarto.agregar("X1", "X2", avizar=True)      # queríamos avisar

print("Se agregaron:", cuarto.productos)
print("¿Se imprimió el aviso? No.")
print()


class CarritoEstricto(Carrito):
    CONOCIDAS = {"avisar"}

    def agregar(self, *skus, **opciones):
        desconocidas = set(opciones) - self.CONOCIDAS
        if desconocidas:
            raise TypeError(f"opción desconocida: {', '.join(sorted(desconocidas))}")
        super().agregar(*skus, **opciones)


quinto = CarritoEstricto("Marco")
try:
    quinto.agregar("X1", avizar=True)
except TypeError as e:
    print("TypeError:", e)
"""),

md("""
`**opciones` acepta cualquier palabra. Es su trabajo: recoge todo lo que venga con nombre y no tiene
manera de saber cuáles esperabas.

Es exactamente el atributo mal escrito de la semana 3, con otro disfraz. Ahí `punto.cordenada_x = 500`
creaba una llave nueva en el diccionario del objeto; aquí `avizar=True` crea una llave nueva en el
diccionario de opciones. En los dos casos el valor se guarda, nadie lo lee, y no hay error.

La segunda mitad de la celda enseña el precio de arreglarlo: si aceptas cualquier cosa, tienes que
escribir tú la revisión que el lenguaje ya no hace. Por eso `**kwargs` no es gratis. **Un método que
acepta cualquier cosa no le dice a nadie qué se le puede pasar.**

## Tipos distintos en el mismo método
"""),

code("""
class Reporte:
    def __init__(self, titulo):
        self.titulo = titulo
        self.filas = []

    def agregar(self, dato):
        if isinstance(dato, str):
            self.filas.append(dato)
        elif isinstance(dato, (list, tuple)):
            self.filas.extend(dato)
        elif isinstance(dato, dict):
            self.filas.extend(f"{k}: {v}" for k, v in dato.items())
        else:
            raise TypeError(f"no sé qué hacer con un {type(dato).__name__}")


r = Reporte("Ventas")
r.agregar("total: 120")
r.agregar(["norte: 40", "sur: 30"])
r.agregar({"centro": 50})

for fila in r.filas:
    print(" ", fila)

print()
print("Filas:", len(r.filas))
try:
    r.agregar(3.14)
except TypeError as e:
    print("TypeError:", e)
"""),

md("""
Funciona, y aun así es una advertencia.

Cuando el cuerpo de un método se llena de `if isinstance`, casi siempre eran dos o tres métodos con
nombres distintos. `agregar_texto`, `agregar_varias` y `agregar_pares` se leen mejor, se prueban por
separado y no obligan a nadie a entender toda la cadena para saber qué pasa con su dato.

La regla práctica: **un método, una responsabilidad**. Si necesitas de verdad despachar por tipo, la
biblioteca estándar trae `functools.singledispatch`, que hace lo mismo sin la escalera de `if`.

## El valor por omisión que no querías
"""),

code("""
# FALLA A PROPÓSITO, y no truena. Una lista como valor por omisión de un método.
class CarritoRoto:
    def __init__(self, dueno, productos=[]):
        self.dueno = dueno
        self.productos = productos

    def agregar(self, sku):
        self.productos.append(sku)


ana = CarritoRoto("Ana")
luis = CarritoRoto("Luis")

ana.agregar("X1")

print("Carrito de Ana: ", ana.productos)
print("Carrito de Luis:", luis.productos, "<- sin haber agregado nada")
print("¿Es la misma lista?", ana.productos is luis.productos)
print()
print("La lista vive en la firma del método:")
print("  ", CarritoRoto.__init__.__defaults__)
"""),

md("""
La última línea es la que resuelve el misterio: **la lista está guardada en la función**, en
`__defaults__`, y se creó una sola vez, cuando Python leyó el `def`.

Cada `CarritoRoto("Ana")` que no pase productos recibe esa misma lista. No una copia. La misma.

Este es el cuarto lugar donde aparece el mismo mecanismo, y ya conviene verlos en fila:

| Dónde | Cómo se vio |
|---|---|
| Repaso 3 | `def f(lista=[])` acumulaba entre llamadas |
| Repaso 4 | `b = a` dejaba dos nombres sobre una sola lista |
| Semana 3 | `productos = []` en el cuerpo de la clase se compartía entre objetos |
| Hoy | `productos=[]` en la firma del constructor se comparte entre objetos |

La corrección es la misma de siempre y cabe en dos líneas.
"""),

code("""
class CarritoBueno:
    def __init__(self, dueno, productos=None):
        self.dueno = dueno
        self.productos = list(productos) if productos else []

    def agregar(self, sku):
        self.productos.append(sku)


ana = CarritoBueno("Ana")
luis = CarritoBueno("Luis")
ana.agregar("X1")

print("Ana: ", ana.productos)
print("Luis:", luis.productos)
print("¿La misma lista?", ana.productos is luis.productos)
print()
print("Por omisión ahora:", CarritoBueno.__init__.__defaults__)

inicial = ["Y1", "Y2"]
sofia = CarritoBueno("Sofía", inicial)
sofia.agregar("Y3")
print()
print("La lista que le pasamos:", inicial, "<- intacta")
print("La del carrito:        ", sofia.productos)
"""),

md("""
`None` por omisión, la lista adentro, y una copia de lo que le pasen.

Ese `list(productos)` de la tercera línea es la parte que casi nadie escribe. Sin él, el carrito se
queda con la lista de quien lo construyó y las dos se modifican juntas, que es el alias del repaso 4
otra vez. Con él, quien te pasa datos no tiene que enterarse de lo que tu clase les hace.

En la semana 6 esto tiene nombre: se llama **no compartir estado mutable**, y es la mitad práctica del
encapsulamiento.
"""),

md("""
---
# Bloque 2 · Operadores propios

Los operadores sí se sobrecargan. Esa es la parte de la sobrecarga que Python sí tiene, y hace más por
la legibilidad de una clase que cualquier otra cosa de este cuaderno.

El archivo `02 - POO/6th Module/Code022.py` cubre el tema a partir de su línea 70. Un aviso, porque
importa: **ese archivo se detiene en la línea 62** por el error que vimos la semana pasada, así que
todo lo que sigue nunca se ejecuta cuando lo corres. El código de esta sección es el de ese archivo,
comprobado celda por celda aquí.

## Lo que imprime un objeto sin `__str__`
"""),

code("""
# FALLA A PROPÓSITO, y no truena. Imprimir un objeto que no sabe describirse.
class Punto:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y


p = Punto(1, 2)
print(p)
print(f"En un f-string: {p}")
print("En una lista:", [Punto(1, 2), Punto(3, 4)])
"""),

md("""
`<__main__.Punto object at 0x...>`, tres veces, con una dirección de memoria distinta cada vez.

No es un error. Es lo que `object` hace por omisión cuando nadie le dice otra cosa, y es información
verdadera: la clase y dónde vive el objeto. Solo que no sirve para nada de lo que uno hace con un
`print`.

Fíjate en la tercera línea. Dentro de una lista sale peor todavía, porque ahí Python no usa `__str__`
sino `__repr__`, y por eso ni siquiera respeta lo que arregles con el primero.
"""),

code("""
class Punto:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"

    def __repr__(self) -> str:
        return f"Punto({self.x}, {self.y})"


p = Punto(1, 2)
print(p)
print(f"En un f-string: {p}")
print("En una lista:", [Punto(1, 2), Punto(3, 4)])
print()
print("str(p): ", str(p))
print("repr(p):", repr(p))
"""),

md("""
Dos métodos con trabajos distintos.

`__str__` es para la persona que va a leer la salida. `__repr__` es para quien está depurando, y la
convención es que se parezca a la llamada que construiría el objeto. Cuando solo escribes uno, escribe
`__repr__`: Python cae a él cuando falta `__str__`, y así las listas también salen bien.

Y fíjate en lo que `__str__` hace: **devuelve** una cadena. No imprime. Es la misma frase de la semana
pasada, la del método privado dentro del f-string, ahora del lado correcto.

## Lo que pasa con `==` sin `__eq__`
"""),

code("""
# FALLA A PROPÓSITO, y no truena. Dos puntos iguales que no son iguales.
p1 = Punto(1, 2)
p2 = Punto(1, 2)

print("p1:", p1, " p2:", p2)
print("¿p1 == p2?", p1 == p2)
print("¿p1 is p2?", p1 is p2)
print()
print("Buscarlo en una lista:", p1 in [Punto(1, 2), Punto(3, 4)])
print("Meterlos en un conjunto:", len({p1, p2}), "elementos para dos puntos idénticos")
lista = [Punto(1, 2), Punto(3, 4)]
try:
    lista.remove(Punto(1, 2))
except ValueError as e:
    print("ValueError:", e)
"""),

md("""
Dos puntos con las mismas coordenadas, y `==` dice que no.

Por omisión, `==` entre objetos pregunta lo mismo que `is`: si son el mismo objeto en memoria. Eso lo
vimos en la semana 3 y prometí que hoy se arreglaba.

Lo que hace cara la omisión no es la comparación suelta, es todo lo que la usa por dentro. `in` sobre
una lista compara con `==`. `list.remove` compara con `==`, y por eso la última línea terminó en
`ValueError: list.remove(x): x not in list` teniendo el punto enfrente. `index`, `count` y la mitad de
las pruebas que vas a escribir comparan con `==`.
"""),

code("""
class Punto:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"

    def __repr__(self) -> str:
        return f"Punto({self.x}, {self.y})"

    def __eq__(self, otro) -> bool:
        return self.x == otro.x and self.y == otro.y

    def __add__(self, otro) -> "Punto":
        return Punto(self.x + otro.x, self.y + otro.y)


p1 = Punto(1, 2)
p2 = Punto(3, 4)

print("p1 == Punto(1, 2):", p1 == Punto(1, 2))
print("p1 + p2:          ", p1 + p2)
print()
puntos = [Punto(1, 2), Punto(3, 4), Punto(5, 6)]
print("¿Punto(3, 4) está en la lista?", Punto(3, 4) in puntos)
puntos.remove(Punto(3, 4))
print("Después de remove:", puntos)
"""),

md("""
`remove` encontró el punto porque `in` y `remove` usan `__eq__`, y ahora hay uno.

`__add__` devuelve un **punto nuevo**. Esa decisión no es cosmética: `a + b` no debería cambiar ni `a`
ni `b`, porque nadie que lea esa línea lo espera. Cuando el operador modifica sus operandos, lo que
sigue es una tarde de depuración.
"""),

code("""
# FALLA A PROPÓSITO, y no truena. Un operador que modifica su operando izquierdo.
class PuntoMutante:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __add__(self, otro):
        self.x += otro.x         # modifica self en lugar de construir uno nuevo
        self.y += otro.y
        return self


a = PuntoMutante(1, 2)
b = PuntoMutante(3, 4)

print("Antes:  a =", a, " b =", b)
c = a + b
print("Después: a =", a, "<- cambió sin que nadie se lo pidiera")
print("         c =", c)
print("¿a y c son el mismo objeto?", a is c)

total = PuntoMutante(0, 0)
for punto in [PuntoMutante(1, 1), PuntoMutante(2, 2)]:
    total = total + punto
print()
print("Suma acumulada:", total, "<- esta sí da lo correcto, por accidente")
"""),

md("""
`a` cambió de valor en una línea que solo lo leía, y `c` no es un punto nuevo sino un segundo nombre
para `a`. Es el alias del repaso 4, servido por un operador.

La última parte es la más incómoda: el ciclo que acumula da el resultado correcto. Por eso este error
sobrevive a las pruebas, se va a producción y sale a la luz el día que alguien suma dos puntos y
después vuelve a usar el primero.

**Un operador construye y devuelve.** Si de verdad quieres el que modifica en el lugar, existe y tiene
su propio nombre: `__iadd__`, que es el que respalda a `+=`.

## El efecto secundario de escribir `__eq__`
"""),

code("""
# FALLA A PROPÓSITO. Definir __eq__ deja la clase sin hash.
print("¿Punto tiene __hash__?", Punto.__hash__)

try:
    conjunto = {Punto(1, 2), Punto(3, 4)}
except TypeError as e:
    print("TypeError:", e)

try:
    diccionario = {Punto(1, 2): "origen"}
except TypeError as e:
    print("TypeError:", e)
"""),

md("""
`unhashable type: 'Punto'`. La clase perdió la capacidad de entrar en un conjunto o de ser llave de un
diccionario, y nadie la escribió así a propósito.

Cuando defines `__eq__`, Python pone `__hash__` en `None`. Suena arbitrario y no lo es: dos objetos que
son iguales tienen que dar el mismo hash, o los diccionarios dejan de funcionar. Como Python no puede
adivinar tu nueva definición de igualdad, prefiere apagar el hash a dejarte uno que miente.

La corrección es una línea, y tiene que ser consistente con `__eq__`.
"""),

code("""
class PuntoCompleto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"PuntoCompleto({self.x}, {self.y})"

    def __eq__(self, otro):
        return (self.x, self.y) == (otro.x, otro.y)

    def __hash__(self):
        return hash((self.x, self.y))      # los mismos datos que __eq__


conjunto = {PuntoCompleto(1, 2), PuntoCompleto(1, 2), PuntoCompleto(3, 4)}
print("Puntos distintos en el conjunto:", len(conjunto))
print(conjunto)
print()
print("Como llave de diccionario:", {PuntoCompleto(0, 0): "origen"})
"""),

md("""
Tres puntos metidos al conjunto, dos distintos. El duplicado se fue solo, que es justo lo que uno
quiere de un conjunto.

Fíjate en que `__hash__` usa **la misma tupla** que `__eq__`. Esa es la regla entera: si dos objetos
son iguales, sus hashes tienen que coincidir.

## Tu clase con sintaxis de colección

El archivo `Code023.py` construye una nube de etiquetas y le va agregando métodos mágicos hasta que se
comporta como un diccionario. Vale la pena verla completa.
"""),

code("""
class NubeDeEtiquetas:
    def __init__(self):
        self.__etiquetas = {}

    def agregar(self, etiqueta):
        clave = etiqueta.lower()
        self.__etiquetas[clave] = self.__etiquetas.get(clave, 0) + 1

    def __str__(self):
        return str(self.__etiquetas)

    def __getitem__(self, etiqueta):
        return self.__etiquetas.get(etiqueta.lower(), 0)

    def __setitem__(self, etiqueta, cuenta):
        self.__etiquetas[etiqueta.lower()] = cuenta

    def __len__(self):
        return len(self.__etiquetas)

    def __iter__(self):
        return iter(self.__etiquetas)

    def __contains__(self, etiqueta):
        return etiqueta.lower() in self.__etiquetas


nube = NubeDeEtiquetas()
for etiqueta in ["python", "Python", "PYTHON", "sql", "c++"]:
    nube.agregar(etiqueta)

print(nube)
print()
print('nube["python"]:', nube["python"])
print('nube["java"]:  ', nube["java"], "<- una etiqueta que no está")
print("len(nube):     ", len(nube))
print('"SQL" in nube: ', "SQL" in nube)
print()
nube["c++"] = 10
for etiqueta in nube:
    print(f"  {etiqueta:<8}{nube[etiqueta]}")
"""),

md("""
Cinco etiquetas agregadas, tres distintas, y las tres formas de escribir "python" cayeron en la misma
cuenta.

Eso último es lo que justifica la clase. Un diccionario suelto habría guardado `python`, `Python` y
`PYTHON` por separado, y la única manera de evitarlo sería acordarse de escribir `.lower()` en cada
uno de los lugares donde se toca. La clase se acuerda por ti, y ese es el trabajo de una clase.

Los cinco métodos mágicos le dan sintaxis conocida: corchetes para leer y escribir, `len` para contar,
`in` para preguntar, y `for` para recorrer. Quien use tu clase no tiene que aprender nada nuevo.

## Cuántos métodos mágicos ya traía tu clase antes de que escribieras uno
"""),

code("""
class Vacia:
    pass


magicos_vacia = [n for n in dir(Vacia) if n.startswith("__") and n.endswith("__")]
magicos_nube = [n for n in dir(NubeDeEtiquetas) if n.startswith("__") and n.endswith("__")]

print("Una clase vacía ya trae", len(magicos_vacia), "métodos mágicos heredados de object")
print("La nube de etiquetas trae", len(magicos_nube))
print()

SINTAXIS = ["__str__", "__getitem__", "__setitem__", "__len__", "__iter__", "__contains__"]
escritos = [n for n in SINTAXIS if n in vars(NubeDeEtiquetas)]
heredados = [n for n in SINTAXIS if hasattr(object, n)]

print("Escritos en la nube:", len(escritos), "->", escritos)
print("De esos, los que object ya traía:", len(heredados), "->", heredados)
print()
for nombre in SINTAXIS:
    print(f"  {nombre:<15}¿lo trae object? {hasattr(object, nombre)}")
"""),

md("""
Una clase con `pass` adentro ya hereda casi treinta métodos mágicos, y por eso `p1 == p2` funcionaba
desde el primer día: `__eq__` estaba, solo que comparaba identidad.

De los seis que le dan sintaxis a la nube, `object` traía uno solo, `__str__`. Ahí está la diferencia
entre los dos casos. Cuando el método existe y no hace lo que quieres, lo sobreescribes y el síntoma es
un resultado equivocado en silencio, como el `print` que enseña una dirección de memoria. Cuando no
existe, `len(objeto)` lanza `TypeError` y te enteras enseguida.

`MagicMethods.md`, en la misma carpeta del módulo 6, tiene la lista completa. No hay que memorizarla:
hay que saber que existe y buscar ahí el día que necesites que tu clase se comporte como algo conocido.
"""),

md("""
---
# Bloque 3 · Organización de clases

Un archivo de mil líneas funciona igual de bien que diez de cien. La diferencia aparece cuando hay que
encontrar algo.

Las celdas de este bloque **escriben archivos de verdad** en el directorio de trabajo del cuaderno y
después los importan. Córrelas en orden.

## Un módulo es un archivo
"""),

code("""
from pathlib import Path

Path("ventas.py").write_text('''
TASA_IVA = 0.16


def calcular_iva(monto: float) -> float:
    return monto * TASA_IVA


print("Hola desde el cuerpo de ventas.py")

if __name__ == "__main__":
    print("Esto solo corre si ejecutas el archivo")
''', encoding="utf-8")

print("Archivo escrito:", Path("ventas.py").exists())
print("Líneas:", len(Path("ventas.py").read_text(encoding="utf-8").splitlines()))
"""),

code("""
import ventas

print()
print("ventas.__name__ es:", repr(ventas.__name__))
print("IVA de 100:", ventas.calcular_iva(100))
print("La tasa:", ventas.TASA_IVA)
"""),

md("""
Al importar salió el `print` suelto y **no** salió el bloque de `__main__`.

Esa es toda la diferencia entre importar y ejecutar. Cuando importas, `__name__` vale el nombre del
módulo, `"ventas"`. Cuando ejecutas el archivo directamente, vale `"__main__"`, y por eso el `if` de
abajo es la manera estándar de decir "esto es para cuando me corran a mí, no para cuando me importen".

Vamos a ver las dos salidas una junto a la otra.
"""),

code("""
import subprocess
import sys

como_script = subprocess.run([sys.executable, "ventas.py"],
                             capture_output=True, text=True)
al_importar = subprocess.run([sys.executable, "-c", "import ventas"],
                             capture_output=True, text=True)

print("Ejecutado como script:")
for linea in como_script.stdout.splitlines():
    print("  ", linea)

print()
print("Importado desde otro archivo:")
for linea in al_importar.stdout.splitlines():
    print("  ", linea)

print()
print("Renglones al ejecutar: ", len(como_script.stdout.splitlines()))
print("Renglones al importar:", len(al_importar.stdout.splitlines()))
"""),

md("""
Dos renglones contra uno. El bloque de `__main__` corrió solo en el segundo caso.

Y ahora la parte incómoda: el `print` suelto salió **las dos veces**. Todo lo que esté fuera de una
función o de una clase se ejecuta en el momento de importar, siempre, sin excepción. Un módulo que
imprime, que abre un archivo o que se conecta a algo al importarse convierte cada `import` en un efecto
secundario.

**La convención: cualquier módulo del proyecto debería poder importarse sin que pase nada visible.**
"""),

code("""
# FALLA A PROPÓSITO, y no truena. Un módulo que hace trabajo al importarse.
Path("catalogo.py").write_text('''
PRODUCTOS = {}

with open("catalogo.txt", "w", encoding="utf-8") as f:
    f.write("archivo creado por catalogo.py")

print("catalogo.py: cargando el catálogo...")
''', encoding="utf-8")

print("¿Existe catalogo.txt antes del import?", Path("catalogo.txt").exists())

import catalogo

print("¿Y después?                          ", Path("catalogo.txt").exists())
print()
print("Nadie llamó a ninguna función, y el disco ya cambió.")
"""),

md("""
Un `import` que escribió un archivo. Ninguna llamada de por medio.

En un cuaderno se ve inofensivo. En un proyecto real, esto es lo que hace que las pruebas fallen
dependiendo del orden en que se importaron los módulos, que un `import` tarde tres segundos, o que
correr una herramienta de análisis estático mande un correo.

## Tres formas de traer la misma clase, y un paquete de verdad
"""),

code("""
Path("tienda").mkdir(exist_ok=True)
Path("tienda/__init__.py").write_text("", encoding="utf-8")

Path("tienda/carrito.py").write_text('''
class Carrito:
    def __init__(self, dueno):
        self.dueno = dueno
        self.productos = []

    def __repr__(self):
        return f"Carrito({self.dueno!r}, {len(self.productos)} productos)"
''', encoding="utf-8")

Path("tienda/cliente.py").write_text('''
class Cliente:
    def __init__(self, nombre):
        self.nombre = nombre

    def __repr__(self):
        return f"Cliente({self.nombre!r})"
''', encoding="utf-8")

print("Paquete creado:")
for ruta in sorted(Path("tienda").rglob("*.py")):
    print("  ", ruta.as_posix())
"""),

code("""
import tienda.carrito
from tienda.carrito import Carrito
from tienda import carrito as ca

a = tienda.carrito.Carrito("Ana")
b = Carrito("Luis")
d = ca.Carrito("Sofía")

print(a)
print(b)
print(d)
print()
print("¿Las tres son la misma clase?",
      type(a) is type(b) is type(d))
print("Módulos de tienda cargados:",
      sorted(n for n in sys.modules if n.startswith("tienda")))
"""),

md("""
Tres sintaxis, una sola clase. El módulo se carga una vez y las tres formas apuntan al mismo objeto.

`import tienda.carrito` trae el módulo completo. Las llamadas quedan largas, y a cambio se ve de dónde
salió cada nombre.

`from tienda.carrito import Carrito` trae un solo nombre. Es la forma más común y la que menos ruido
hace dentro del archivo.

`from tienda import carrito as ca` renombra. Sirve cuando dos módulos se llaman igual, y estorba cuando
se usa por escribir menos.

Falta la cuarta, que es la que hay que evitar.
"""),

code("""
# FALLA A PROPÓSITO, y no truena. El asterisco trae todo, y el segundo pisa al primero.
Path("colores.py").write_text('''
def formato(texto):
    return f"[color] {texto}"
''', encoding="utf-8")

Path("fechas.py").write_text('''
def formato(texto):
    return f"[fecha] {texto}"
''', encoding="utf-8")

from colores import *
from fechas import *

print(formato("hola"))
print()
print("¿Cuál de los dos ganó? El del último import.")
print("Y si alguien cambia el orden de las dos líneas, el programa cambia de comportamiento.")
"""),

md("""
`from modulo import *` trae todos los nombres públicos del módulo y los suelta en tu archivo. Dos
módulos con una función que se llama igual y el segundo gana, sin aviso.

Fíjate en lo que se perdió: al leer `formato("hola")` ya no hay manera de saber de dónde salió esa
función. Con `import colores` y `colores.formato(...)`, la línea lo dice sola.

## Las importaciones circulares
"""),

code("""
# FALLA A PROPÓSITO. Dos módulos que se importan entre sí.
Path("pedido.py").write_text('''
import factura


class Pedido:
    def facturar(self):
        return factura.Factura()
''', encoding="utf-8")

Path("factura.py").write_text('''
from pedido import Pedido


class Factura:
    def __init__(self):
        self.pedido = Pedido()
''', encoding="utf-8")

for nombre in ["pedido", "factura"]:
    sys.modules.pop(nombre, None)

try:
    import pedido
except ImportError as e:
    print("ImportError:", e)
"""),

md("""
Python carga `pedido`, que en su primera línea pide `factura`, que en su primera línea pide un nombre
de `pedido`, que todavía no terminó de cargarse y por lo tanto no tiene ese nombre.

El mensaje habla de un módulo "parcialmente inicializado", y esa es la descripción exacta de lo que
pasó.

Una importación circular casi nunca es un problema de importaciones: **es un problema de diseño**. Si
`pedido` necesita a `factura` y `factura` necesita a `pedido`, o las dos clases van en el mismo módulo
porque son una sola idea, o falta una tercera pieza que las coordine.

## Cuatro formas de organizar mal un proyecto

| | El error | Cuándo se nota |
|---|---|---|
| 01 | Un solo archivo con todo | Pasadas las trescientas líneas, encontrar una clase cuesta más que escribirla |
| 02 | Un archivo por clase, sin excepción | Diez archivos de quince líneas para entender una sola idea |
| 03 | Importaciones circulares | `ImportError` a media carga, con un mensaje que no señala el diseño |
| 04 | Código suelto en el módulo | Cada `import` dispara los prints, las pruebas y lo que haya |

**Un módulo se justifica cuando dos clases del mismo archivo ya no se leen juntas.** Un paquete se
justifica cuando los módulos empiezan a repetir prefijos en el nombre: si tienes `tienda_carrito.py`,
`tienda_cliente.py` y `tienda_pago.py`, lo que tienes es una carpeta.
"""),

md("""
---
# Bloque 4 · Modelado básico

El paso que casi nadie hace y que decide la mitad del resultado: dibujar antes de teclear.

La caja de UML tiene tres compartimentos y cada uno corresponde a una parte de la clase. El nombre
arriba, lo que recuerda en medio, lo que sabe hacer abajo.

```
┌─────────────────────────────┐
│          Prestamo           │   class Prestamo:
├─────────────────────────────┤
│ - libro: Libro              │       def __init__(self, libro, socio, dia):
│ - socio: Socio              │           self.libro = libro
│ - dia_prestamo: int         │           ...
├─────────────────────────────┤
│ + vencido(dia): bool        │       def vencido(self, dia): ...
│ + multa(dia): float         │       def multa(self, dia): ...
└─────────────────────────────┘
```

El guion es privado y el más es público, que es la notación de UML y no de Python. En Python el guion
se escribe con dos guiones bajos.

## Del enunciado a las cajas, en cinco pasos

El enunciado del laboratorio:

> La biblioteca presta libros a los socios por catorce días. Si un socio devuelve un libro tarde, paga
> una multa de cinco pesos por día de retraso. Un socio no puede tener más de tres libros prestados al
> mismo tiempo.

**Paso 1. Subraya los sustantivos.** biblioteca, libro, socio, días, multa, día de retraso.

**Paso 2. Descarta los que no recuerdan nada.** "Días" y "día de retraso" son números, no cosas.
"Multa" es el resultado de una cuenta, así que probablemente sea un método y no una clase.

**Paso 3. Lista lo que recuerda cada uno.** El libro recuerda su título y su autor. El socio recuerda
su nombre y qué tiene prestado. El préstamo recuerda qué libro, qué socio y qué día salió.

**Paso 4. Subraya los verbos.** prestar, devolver, pagar, tener prestados. Cada verbo va a la clase
que tiene los datos con los que trabaja.

**Paso 5. Dibuja la caja.** Si los tres compartimentos no caben en media hoja, la clase hace demasiado.

Fíjate en que "préstamo" no está en la lista del paso 1. Salió del verbo "prestar", y es la clase más
importante del modelo. Los sustantivos son el punto de partida, no la respuesta.
"""),

code("""
class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def __repr__(self):
        return f"Libro({self.titulo!r})"


class Socio:
    MAXIMO = 3

    def __init__(self, nombre):
        self.nombre = nombre
        self.prestamos = []

    def puede_pedir(self):
        return len(self.prestamos) < Socio.MAXIMO

    def __repr__(self):
        return f"Socio({self.nombre!r}, {len(self.prestamos)} libros)"


class Prestamo:
    DIAS = 14
    MULTA_DIARIA = 5.0

    def __init__(self, libro, socio, dia_prestamo):
        self.libro = libro
        self.socio = socio
        self.dia_prestamo = dia_prestamo

    def vencido(self, dia_actual):
        return dia_actual - self.dia_prestamo > Prestamo.DIAS

    def multa(self, dia_actual):
        retraso = dia_actual - self.dia_prestamo - Prestamo.DIAS
        return max(0, retraso) * Prestamo.MULTA_DIARIA

    def __repr__(self):
        return f"Prestamo({self.libro.titulo!r} -> {self.socio.nombre})"


ana = Socio("Ana")
catalogo = [Libro("El Aleph", "Borges"), Libro("Pedro Páramo", "Rulfo"),
            Libro("La tregua", "Benedetti"), Libro("Aura", "Fuentes")]

for libro in catalogo:
    if ana.puede_pedir():
        ana.prestamos.append(Prestamo(libro, ana, 1))
    else:
        print("Rechazado por el límite:", libro.titulo)

print()
print(ana)
for prestamo in ana.prestamos:
    print(f"  {prestamo}  vencido al día 20: {prestamo.vencido(20)}  multa: ${prestamo.multa(20):.2f}")
"""),

md("""
Tres clases, tres atributos cada una, y las reglas del enunciado viven cada una en un solo lugar.

`MAXIMO` y `DIAS` son atributos de clase porque son reglas de la biblioteca y no de cada socio ni de
cada préstamo. Es la lección de la semana 3, usada esta vez para lo que sirve.

`multa` devuelve un número y no lo imprime, así que el ciclo de abajo pudo acomodarlo en una columna.
Es la lección del repaso 3, otra vez.

## La clase que casi todos escriben en su lugar
"""),

code("""
# FALLA A PROPÓSITO, y no truena. La clase que es un archivo de funciones con techo.
class SistemaGestorDeBiblioteca:
    def __init__(self):
        pass

    def prestar_libro(self, titulo, socio, dia):
        return {"titulo": titulo, "socio": socio, "dia": dia}

    def esta_vencido(self, prestamo, dia):
        return dia - prestamo["dia"] > 14

    def calcular_multa(self, prestamo, dia):
        return max(0, dia - prestamo["dia"] - 14) * 5.0

    def puede_pedir(self, prestamos_del_socio):
        return len(prestamos_del_socio) < 3


sistema = SistemaGestorDeBiblioteca()
prestamo = sistema.prestar_libro("El Aleph", "Ana", 1)

print("Préstamo:", prestamo)
print("¿Vencido al 20?", sistema.esta_vencido(prestamo, 20))
print("Multa:", sistema.calcular_multa(prestamo, 20))
print()
print("Estado del sistema:", vars(sistema))
print("Atributos que recuerda:", len(vars(sistema)))
print()
print("La biblioteca cambia el plazo de 14 a 21 días.")
Prestamo.DIAS = 21               # una línea, y ya

del_modelo = Prestamo(Libro("El Aleph", "Borges"), ana, 1)
print("  Con el modelo, ¿vencido al día 20?  ", del_modelo.vencido(20))
print("  Con el gestor,  ¿vencido al día 20?  ", sistema.esta_vencido(prestamo, 20))
print()
print("El mismo préstamo, el mismo día, dos respuestas.")
Prestamo.DIAS = 14
"""),

md("""
Corre, da los mismos números, y el objeto no recuerda absolutamente nada. `vars(sistema)` está vacío.

Una clase cuyo estado es un diccionario vacío no es una clase, es un archivo de funciones con un techo
encima. La prueba está en el paso 2 del método: si no guarda nada entre una llamada y la siguiente,
era una función. Esta ya la viste en la semana 2, cuando comparamos el paradigma con el estructurado;
lo nuevo es que ahora tienes el vocabulario para decir qué le falta.

La segunda mitad de la celda es la prueba que importa. La biblioteca cambia su plazo a veintiún días, y
en el modelo eso es una línea: `Prestamo.DIAS = 21`. El préstamo deja de estar vencido enseguida.

En el sistema-gestor el catorce está escrito dentro de `esta_vencido` y otra vez dentro de
`calcular_multa`, así que no hay ninguna línea que cambiar desde fuera y hay dos que buscar adentro. El
mismo préstamo, el mismo día, y dos respuestas distintas.

Ese es el argumento entero a favor de modelar. No es que quede más bonito: es que las reglas del
enunciado terminan cada una en un solo lugar, y ese lugar tiene nombre.

**El criterio del laboratorio: que ninguna clase se llame Gestor, Manejador o Sistema.** Ninguno de los
tres es un sustantivo del enunciado, y las tres palabras son la manera de posponer la decisión de qué
clases hay.
"""),

md("""
---
## Cuatro errores de esta sesión

**Esperar que el segundo `def` conviva con el primero.** Solo queda uno, el de abajo. Los parámetros
por omisión cubren el caso real.

**Pasarle una lista a un método que declara `*args`.** Llega un argumento que es una lista, no tres
argumentos. El asterisco que desempaqueta va del lado de la llamada.

**Definir `__eq__` y olvidar `__hash__`.** La clase deja de servir como llave de diccionario y como
elemento de conjunto, con un `TypeError` que no menciona a `__eq__` por ningún lado.

**Dejar código suelto en un módulo.** Corre al importar, siempre, y convierte cada `import` en un
efecto secundario que nadie ve en la línea que lo dispara.
"""),

md("""
---
# Ejercicios

El laboratorio de esta semana es modelar el préstamo de la biblioteca, en parejas, entregando las cajas
antes que el código.

Las soluciones están hasta abajo del cuaderno.

### Ejercicio 1 · El segundo def

Escribe una clase con dos métodos del mismo nombre y firmas distintas. Llama al de la primera firma,
atrapa el error, e imprime el diccionario de la clase para mostrar que solo quedó uno.

Después reescríbela con un valor por omisión y prueba las dos formas de llamarla.

### Ejercicio 2 · Cuántos sean

Escribe una clase `Bitacora` con un método `registrar(*mensajes)` que acepte cero, uno o varios.
Pruébalo con las tres cantidades y cuenta los renglones.

Después llámalo con una lista sin asterisco y muestra qué se guardó en realidad.

### Ejercicio 3 · Opciones con nombre

Agrega a `Bitacora` un `**opciones` que acepte `mayusculas=True` y `prefijo="..."`. Llámalo con una
opción bien escrita y con una mal escrita, y demuestra que la segunda no hace nada ni avisa.

Agrega la revisión que sí avisa.

### Ejercicio 4 · La lista de la firma

Escribe una clase con una lista como valor por omisión en el constructor. Crea dos objetos, agrega a
uno, y demuestra con `is` que comparten la lista.

Imprime `__defaults__` del constructor para enseñar dónde vive esa lista, y después arréglalo.

### Ejercicio 5 · Que se pueda imprimir

Escribe `Fraccion` con numerador y denominador. Imprímela antes de escribir `__str__` y después.
Agrega `__repr__` y muestra la diferencia metiendo dos fracciones en una lista.

### Ejercicio 6 · Que se pueda comparar

Agrega `__eq__` a `Fraccion`, de modo que 1/2 sea igual a 2/4. Comprueba con `in` sobre una lista y con
`remove`.

Después mete dos fracciones en un conjunto, atrapa el `TypeError`, y arréglalo con `__hash__`.

### Ejercicio 7 · Que se pueda sumar

Agrega `__add__` a `Fraccion` de modo que devuelva una fracción nueva. Demuestra con `is` que los dos
operandos quedaron intactos.

Después escribe a propósito la versión que modifica `self` y enseña en qué se nota.

### Ejercicio 8 · Un paquete

Crea un paquete `biblioteca` con dos módulos, uno para `Libro` y otro para `Socio`, y un
`if __name__ == "__main__"` en cada uno. Impórtalos de las tres formas y comprueba que la clase es la
misma.

Después ejecuta uno de los dos como script y compara las salidas.

### Ejercicio 9 · El laboratorio

Modela el préstamo de la biblioteca. Quién pide prestado, qué se presta, cuándo vence y quién cobra la
multa.

Máximo cuatro clases y tres atributos por clase, con los métodos declarados y el cuerpo vacío. Entrega
un diagrama con las cajas y un archivo `.py` con las clases y las firmas de sus métodos.

Que ninguna clase se llame Gestor, Manejador ni Sistema, porque ninguno de los tres es un sustantivo
del problema.
"""),

md("""
---
## Tres ideas para llevarse

**Python no sobrecarga por firma.** El segundo `def` sobrescribe al primero porque el nombre de un
método es una entrada de diccionario. Los valores por omisión, `*args` y `**kwargs` cubren el caso
real y con menos código.

**Los operadores sí se sobrecargan.** `__str__`, `__eq__` y `__add__` le dan a tu clase la sintaxis que
todo el mundo ya conoce, y el que falta se nota en el lugar menos esperado: en un `remove` que no
encuentra nada o en un `print` que enseña una dirección de memoria.

**El modelo se dibuja antes de escribirse.** Sustantivos a cajas, verbos a métodos, y recién entonces
el editor. Los cinco pasos toman diez minutos y ahorran la tarde en que descubres que la clase
equivocada tiene los datos.

Con esto cierra el tema 2. La semana 6 abre el tema 3 con encapsulamiento, ocultamiento de información
y reutilización, y ahí se cobra todo lo que llevamos: la propiedad de la semana 4, el estado
compartido que arrastramos desde el repaso 3, y la copia defensiva del bloque 1 de hoy.

### Un ejercicio para la semana

Toma el archivo más largo que hayas escrito este semestre y pártelo en módulos sin cambiar una sola
línea de lógica. Si no puedes, es porque hay algo que depende de todo, y eso es exactamente lo que hay
que encontrar.
"""),

md("""
---
# Soluciones

### Ejercicio 1

```python
class Calculadora:
    def sumar(self, a, b):
        return a + b

    def sumar(self, a, b, c):
        return a + b + c


calc = Calculadora()

try:
    calc.sumar(1, 2)
except TypeError as e:
    print("TypeError:", e)

print(vars(Calculadora))
print("Métodos:", [n for n in vars(Calculadora) if not n.startswith("__")])


class CalculadoraBuena:
    def sumar(self, a, b, c=0):
        return a + b + c


buena = CalculadoraBuena()
print(buena.sumar(1, 2), buena.sumar(1, 2, 3))
```

### Ejercicio 2

```python
class Bitacora:
    def __init__(self):
        self.renglones = []

    def registrar(self, *mensajes):
        for mensaje in mensajes:
            self.renglones.append(mensaje)


b = Bitacora()
b.registrar()
b.registrar("uno")
b.registrar("dos", "tres", "cuatro")
print(b.renglones, "->", len(b.renglones), "renglones")

c = Bitacora()
c.registrar(["uno", "dos"])
print(c.renglones, "->", len(c.renglones), "renglón")
print("Tipo del primero:", type(c.renglones[0]).__name__)

# Con la lista sin asterisco se guardó un solo renglón, que es una lista. El
# método no desempaqueta: recoge lo que le manden.
```

### Ejercicio 3

```python
class Bitacora:
    CONOCIDAS = {"mayusculas", "prefijo"}

    def __init__(self, estricta=False):
        self.renglones = []
        self.estricta = estricta

    def registrar(self, *mensajes, **opciones):
        if self.estricta:
            desconocidas = set(opciones) - Bitacora.CONOCIDAS
            if desconocidas:
                raise TypeError(f"opción desconocida: {sorted(desconocidas)}")
        prefijo = opciones.get("prefijo", "")
        for mensaje in mensajes:
            texto = f"{prefijo}{mensaje}"
            self.renglones.append(texto.upper() if opciones.get("mayusculas") else texto)


b = Bitacora()
b.registrar("bien escrita", mayusculas=True)
b.registrar("mal escrita", mayuskulas=True)
for renglon in b.renglones:
    print(" ", renglon)

estricta = Bitacora(estricta=True)
try:
    estricta.registrar("x", mayuskulas=True)
except TypeError as e:
    print("TypeError:", e)
```

### Ejercicio 4

```python
class GrupoRoto:
    def __init__(self, clave, alumnos=[]):
        self.clave = clave
        self.alumnos = alumnos

    def inscribir(self, nombre):
        self.alumnos.append(nombre)


uno = GrupoRoto("01")
dos = GrupoRoto("02")
uno.inscribir("Ana")

print("Grupo 1:", uno.alumnos)
print("Grupo 2:", dos.alumnos)
print("¿La misma lista?", uno.alumnos is dos.alumnos)
print("Dónde vive:", GrupoRoto.__init__.__defaults__)


class Grupo:
    def __init__(self, clave, alumnos=None):
        self.clave = clave
        self.alumnos = list(alumnos) if alumnos else []

    def inscribir(self, nombre):
        self.alumnos.append(nombre)


uno = Grupo("01")
dos = Grupo("02")
uno.inscribir("Ana")
print("Ahora:", uno.alumnos, dos.alumnos, uno.alumnos is dos.alumnos)
```

### Ejercicio 5

```python
from math import gcd


class FraccionMuda:
    def __init__(self, num, den):
        self.num = num
        self.den = den


print(FraccionMuda(1, 2))


class Fraccion:
    def __init__(self, num, den):
        self.num = num
        self.den = den

    def __str__(self):
        return f"{self.num}/{self.den}"

    def __repr__(self):
        return f"Fraccion({self.num}, {self.den})"


f = Fraccion(1, 2)
print(f)
print([Fraccion(1, 2), Fraccion(3, 4)])

# Dentro de la lista Python usa __repr__, no __str__. Si solo vas a escribir uno,
# escribe __repr__: print cae a él cuando __str__ no está.
```

### Ejercicio 6

```python
class Fraccion:
    def __init__(self, num, den):
        factor = gcd(num, den)
        self.num = num // factor
        self.den = den // factor

    def __repr__(self):
        return f"{self.num}/{self.den}"

    def __eq__(self, otro):
        return (self.num, self.den) == (otro.num, otro.den)


print(Fraccion(1, 2) == Fraccion(2, 4))

fracciones = [Fraccion(1, 2), Fraccion(3, 4)]
print(Fraccion(2, 4) in fracciones)
fracciones.remove(Fraccion(2, 4))
print(fracciones)

try:
    {Fraccion(1, 2), Fraccion(2, 4)}
except TypeError as e:
    print("TypeError:", e)


class FraccionCompleta(Fraccion):
    def __hash__(self):
        return hash((self.num, self.den))


print(len({FraccionCompleta(1, 2), FraccionCompleta(2, 4), FraccionCompleta(3, 4)}))

# Simplificar en el constructor es lo que hace que 1/2 y 2/4 sean el mismo par de
# números, y por lo tanto que __eq__ y __hash__ coincidan sin esfuerzo.
```

### Ejercicio 7

```python
class Fraccion:
    def __init__(self, num, den):
        factor = gcd(num, den)
        self.num = num // factor
        self.den = den // factor

    def __repr__(self):
        return f"{self.num}/{self.den}"

    def __add__(self, otro):
        return Fraccion(self.num * otro.den + otro.num * self.den,
                        self.den * otro.den)


a = Fraccion(1, 2)
b = Fraccion(1, 3)
c = a + b

print(a, "+", b, "=", c)
print("¿a cambió?", a, "· ¿c es a?", c is a)


class FraccionMutante(Fraccion):
    def __add__(self, otro):
        self.num = self.num * otro.den + otro.num * self.den
        self.den = self.den * otro.den
        return self


a = FraccionMutante(1, 2)
b = FraccionMutante(1, 3)
c = a + b
print("a quedó en", a, "y c es a:", c is a)

# El total del ciclo acumulado sale bien con las dos versiones, y por eso el error
# pasa las pruebas. Se nota el día que alguien suma y después vuelve a usar el
# operando izquierdo.
```

### Ejercicio 8

```python
from pathlib import Path
import sys, subprocess

Path("biblioteca").mkdir(exist_ok=True)
Path("biblioteca/__init__.py").write_text("", encoding="utf-8")

Path("biblioteca/libro.py").write_text('''
class Libro:
    def __init__(self, titulo):
        self.titulo = titulo

    def __repr__(self):
        return f"Libro({self.titulo!r})"


if __name__ == "__main__":
    print("prueba:", Libro("El Aleph"))
''', encoding="utf-8")

Path("biblioteca/socio.py").write_text('''
class Socio:
    def __init__(self, nombre):
        self.nombre = nombre

    def __repr__(self):
        return f"Socio({self.nombre!r})"


if __name__ == "__main__":
    print("prueba:", Socio("Ana"))
''', encoding="utf-8")

import biblioteca.libro
from biblioteca.libro import Libro
from biblioteca import libro as lb

print(type(biblioteca.libro.Libro("A")) is type(Libro("B")) is type(lb.Libro("C")))

salida = subprocess.run([sys.executable, "biblioteca/libro.py"],
                        capture_output=True, text=True)
print("Como script:", salida.stdout.strip() or "(sin salida)")
print("Al importar: sin salida, que es como debe ser")
```

### Ejercicio 9

```python
class Libro:
    def __init__(self, titulo: str, autor: str, isbn: str) -> None:
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn

    def ficha(self) -> str:
        ...


class Socio:
    MAXIMO_SIMULTANEO = 3

    def __init__(self, nombre: str, numero: int) -> None:
        self.nombre = nombre
        self.numero = numero
        self.prestamos: list["Prestamo"] = []

    def puede_pedir(self) -> bool:
        ...


class Prestamo:
    DIAS = 14

    def __init__(self, libro: Libro, socio: Socio, dia_prestamo: int) -> None:
        self.libro = libro
        self.socio = socio
        self.dia_prestamo = dia_prestamo

    def vencido(self, dia_actual: int) -> bool:
        ...

    def dias_de_retraso(self, dia_actual: int) -> int:
        ...


class Multa:
    POR_DIA = 5.0

    def __init__(self, prestamo: Prestamo, dias_de_retraso: int) -> None:
        self.prestamo = prestamo
        self.dias_de_retraso = dias_de_retraso
        self.pagada = False

    def monto(self) -> float:
        ...
```

Cuatro decisiones que vale la pena defender en la entrega.

**No hay clase `Biblioteca`.** El enunciado la menciona, pero no guarda nada que las otras cuatro no
guarden ya. En cuanto tenga una lista de libros y una de socios se justifica; con este enunciado, no.

**`Multa` es una clase y no un método.** Se decidió en el paso 3: una multa recuerda si ya se pagó, y
eso sobrevive a la operación que la creó. Si el enunciado no dijera nada de pagar, `multa()` sería un
método de `Prestamo` y bastaría.

**`Prestamo` guarda el objeto `Libro` completo**, no el título. Así no hay dos lugares donde el título
pueda diferir. Es la lección de la semana 2 dentro de un modelo.

**Las constantes van en la clase a la que pertenecen.** El plazo es del préstamo, el tope simultáneo es
del socio, la tarifa es de la multa. Cuando la biblioteca cambie su reglamento, cada número está en un
solo lugar y se sabe cuál.
"""),

]

write(OUT / "es" / "w05.ipynb", es)
print("wrote", OUT / "es" / "w05.ipynb")
