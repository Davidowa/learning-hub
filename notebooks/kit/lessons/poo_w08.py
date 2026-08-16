"""notebooks/programacion-orientada-a-objetos/es/w08.ipynb

Source deck: ppts/python/programacion-orientada-a-objetos/es/w08.es.yaml
Source code:  docs/en/courses/python-course/02 - POO/6th Module/Code027.py
                  (Animal, Dog, Cat: sobrescritura y el ciclo polimórfico)
              docs/en/courses/python-course/02 - POO/6th Module/Code020.py
                  (Shape, Circle, Rectangle, con el "Area of Shape: None" del final)
              docs/en/courses/python-course/02 - POO/6th Module/Code026.py
                  (ABC, abstractmethod y la jerarquía de Stream)

Los tres archivos corren completos, comprobado. Code020.py imprime
"Area of Shape: None" en su última línea y el archivo lo documenta como
resultado esperado; aquí se cita como la falla silenciosa que justifica las
clases abstractas.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from nbkit import md, code, write, REPO

OUT = REPO / "notebooks" / "programacion-orientada-a-objetos"

es = [

md("""
# Programación Orientada a Objetos · Semana 08
## Tema 3 · Propiedades fundamentales

**COM102 · Facultad de Ingeniería · Profesor David Escobar-Castillejos**

El mismo mensaje contestado de formas distintas, el contrato que obliga a contestarlo, y el cierre de
las tres primeras unidades.

La semana pasada terminó con un ciclo que recorría tres flujos de datos sin saber de qué clase era cada
uno. Eso ya era polimorfismo. Lo que falta es el contrato que obliga a las hijas a contestar, y el
vocabulario para decir por qué ese ciclo es el pilar de todo el paradigma.

Al terminar vas a poder:

1. Sobrescribir un método y decidir a propósito si extiendes al padre o lo reemplazas.
2. Reconocer el polimorfismo donde de verdad se ve, que es en el ciclo que llama y no en la clase.
3. Escribir una clase abstracta con `ABC` y `@abstractmethod`, y decir qué pasa si falta cualquiera
   de los dos.
4. Cambiar una cadena de `if isinstance` por una llamada polimórfica.
5. Llegar al primer parcial sabiendo exactamente qué entra.

### Cómo se usa este cuaderno

Ejecuta las celdas en orden con **Shift + Enter**. Diez fallan a propósito y llevan un comentario que lo
dice.

Siete de las diez **no lanzan ninguna excepción**. Una de esas siete viene del archivo del curso:
`Code020.py` termina imprimiendo `Area of Shape: None` y el propio archivo lo anota como resultado
esperado. Esa línea es el mejor argumento a favor de las clases abstractas que hay en el repositorio.
"""),

md("""
---
# Bloque 1 · Polimorfismo y sobrescritura

Que objetos de clases distintas respondan al mismo mensaje, cada uno a su manera, y que quien los llama
no tenga que saber de cuál se trata.

Empezamos por la mitad fácil, que es la sobrescritura.
"""),

code("""
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print("Sonido de animal")


class Perro(Animal):
    def hablar(self):
        print("Guau")


class Gato(Animal):
    def hablar(self):
        print("Miau")


animales = [Perro("Bobby"), Gato("Kitty"), Perro("Rex"), Gato("Luna")]

for animal in animales:
    animal.hablar()

CICLO = "for animal in animales:\\n    animal.hablar()"

print()
print("El ciclo entero:", repr(CICLO))
print("Clases distintas que pasaron por él:", len({type(a) for a in animales}))
print("Veces que el ciclo nombra una clase:",
      sum(CICLO.count(n) for n in ["Animal", "Perro", "Gato", "isinstance", "type("]))
"""),

md("""
Cuatro objetos, dos clases, una sola línea que los llama.

Sobrescribir es volver a definir un método que ya existía arriba. `Perro.hablar` tapa a `Animal.hablar`
para los perros y no le hace nada a los gatos, porque cada clase tiene su propio diccionario.

**Sobrescribir no es sobrecargar.** Sobrecargar sería tener dos métodos con el mismo nombre y firmas
distintas, que es lo que la semana 5 demostró que Python no hace. Sobrescribir es cambiar el cuerpo en
la hija, y eso sí existe.

## Dónde se ve el polimorfismo

No en las clases. En el ciclo.

Fíjate en la línea `animal.hablar()`: no menciona a `Perro`, no menciona a `Gato`, y no va a cambiar
nunca. Esa es la propiedad que importa.
"""),

code("""
class Vaca(Animal):
    def hablar(self):
        print("Muu")


animales.append(Vaca("Lola"))

for animal in animales:          # el mismo ciclo, sin una letra de diferencia
    animal.hablar()

print()
print("Clases que ahora pasan por la misma línea:", len({type(a) for a in animales}))
print("¿El ciclo es idéntico al de la celda anterior?",
      CICLO == "for animal in animales:\\n    animal.hablar()")
"""),

md("""
Una clase nueva, y el código que la usa no se enteró.

Eso es lo que compras con el polimorfismo, y es la razón por la que es un pilar y no un truco:
**agregar un caso no obliga a tocar el código que ya funcionaba**. En el paradigma estructurado, el
mismo cambio significa buscar cada `if` que enumeraba los tipos y agregarle una rama.

Lo vas a ver claro dentro de dos celdas, cuando escriba esa versión.

## Extender en vez de reemplazar
"""),

code("""
class Documento:
    def guardar(self):
        print("  validando campos")


class Factura(Documento):
    def guardar(self):
        super().guardar()             # primero lo del padre
        print("  timbrando la factura")


class Borrador(Documento):
    def guardar(self):
        print("  guardando sin validar")     # reemplaza, no extiende


print("Factura:")
Factura().guardar()
print()
print("Borrador:")
Borrador().guardar()
"""),

md("""
Las dos hijas sobrescriben `guardar`. Una llama al padre y la otra no, y las dos decisiones son
defendibles.

`Factura` **extiende**: hace lo del padre y algo más. `Borrador` **reemplaza**: hace algo distinto y el
trabajo del padre estorbaría.

El orden también se decide. Poner `super().guardar()` al final invierte la secuencia, y a veces eso es
exactamente lo que quieres. Lo que no conviene es escribirlo por costumbre sin mirar qué pasa antes y
qué pasa después.
"""),

code("""
# FALLA A PROPÓSITO, y no truena. La hija olvida llamar al padre.
class Auditoria:
    def __init__(self):
        self.registro = []

    def guardar(self, dato):
        self.registro.append(dato)
        print(f"  guardado: {dato}")


class AuditoriaConAviso(Auditoria):
    def guardar(self, dato):
        print(f"  aviso enviado por {dato}")     # falta super().guardar(dato)


a = AuditoriaConAviso()
a.guardar("factura 001")
a.guardar("factura 002")

print()
print("Renglones en el registro:", len(a.registro), "<- esperábamos 2")
print("Registro:", a.registro)
print("Método que corrió, escrito en:",
      next(c.__name__ for c in AuditoriaConAviso.__mro__ if "guardar" in vars(c)))
"""),

md("""
Dos avisos enviados y cero renglones guardados.

Sobrescribir un método sin llamar al padre **elimina** lo que el padre hacía. Aquí lo que se perdió es
el registro completo, y el síntoma es que la auditoría está vacía, no que algo truene.

Es la cara silenciosa de la sobrescritura, y es fácil de provocar sin querer: alguien abre la clase
hija, ve un método con el nombre correcto, le agrega su línea, y nunca mira la clase madre.

## Y la cara contraria: el método que la hija debió sobrescribir y no
"""),

code("""
# FALLA A PROPÓSITO, y no truena. La hija agrega un dato y hereda un __eq__ que no lo conoce.
class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, otro):
        return self.x == otro.x and self.y == otro.y

    def __repr__(self):
        return f"Punto({self.x}, {self.y})"


class Punto3D(Punto):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z

    def __repr__(self):
        return f"Punto3D({self.x}, {self.y}, {self.z})"


a = Punto3D(1, 2, 3)
b = Punto3D(1, 2, 99)

print("a:", a, " b:", b)
print("¿a == b?", a == b, "<- tienen distinta z")
print()
print("__eq__ que corrió, escrito en:",
      next(c.__name__ for c in Punto3D.__mro__ if "__eq__" in vars(c)))
print("Coordenadas que compara:", 2, "de", len(vars(a)))
print()
puntos = [Punto3D(1, 2, 3), Punto3D(1, 2, 99), Punto3D(0, 0, 0)]
print("Puntos distintos según ==:", len([p for i, p in enumerate(puntos)
                                        if p not in puntos[:i]]))
"""),

md("""
Dos puntos con la misma `x` y la misma `y` y distinta `z`, y el `==` dice que son iguales.

`Punto3D` sobrescribió `__repr__` porque saltaba a la vista que hacía falta, y no sobrescribió `__eq__`
porque no saltaba a la vista nada. El método heredado sigue comparando dos coordenadas de las tres, y
como funciona, nadie lo revisa.

**Cada vez que una hija agrega un atributo, hay que preguntarse qué métodos heredados dejaron de estar
completos.** Los sospechosos habituales son `__eq__`, `__hash__`, `__repr__` y cualquier método que
recorra el estado del objeto.

La corrección aquí es escribir `__eq__` y `__hash__` en la hija, con la tupla de las tres coordenadas,
que es la regla de la semana 5.

## Predice antes de correr

```python
class Forma:
    def area(self):
        return 0

    def mostrar(self):
        print(self.area())


class Circulo(Forma):
    def area(self):
        return 12.56


Circulo().mostrar()
```

- **A.** `0`, porque `mostrar` vive en `Forma` y usa el `area` de `Forma`.
- **B.** `12.56`, porque `self` es un `Circulo` y su `area` gana.
- **C.** `AttributeError`, `Circulo` no tiene `mostrar`.
- **D.** `TypeError`, `area` recibe un argumento de más.
"""),

code("""
class Forma:
    def area(self):
        return 0

    def mostrar(self):
        print(f"  {type(self).__name__}: {self.area()}")


class Circulo(Forma):
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return 3.1416 * self.radio ** 2


Circulo(2).mostrar()

print()
print("mostrar está escrito en:",
      next(c.__name__ for c in Circulo.__mro__ if "mostrar" in vars(c)))
print("area que corrió, escrita en:",
      next(c.__name__ for c in Circulo.__mro__ if "area" in vars(c)))
print("Tipo de self durante mostrar:", type(Circulo(2)).__name__)
"""),

md("""
La respuesta es **B**.

`mostrar` se heredó de `Forma`, pero `self` sigue siendo un `Circulo`. Python busca `area` empezando por
la clase real del objeto y no por la clase donde estaba escrito el método que la llama.

Es la misma regla que en la semana 7 hizo que el constructor del padre llamara al método de la hija.
Vista desde aquí es una herramienta: **el padre puede escribir el algoritmo y dejar huecos que las hijas
llenan**. Ese patrón tiene nombre, se llama método plantilla, y es la mitad de lo que hace útil a una
clase abstracta.

## La línea de `Code020.py` que lo estropea todo
"""),

code("""
# FALLA A PROPÓSITO, y no truena. Esta viene del archivo del curso.
class Rectangulo(Forma):
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto

    def area(self):
        return self.ancho * self.alto


formas = [Forma(), Circulo(5), Rectangulo(4, 5)]

for forma in formas:
    forma.mostrar()

print()
print("Área de la forma genérica:", Forma().area())
print("Tipo de ese resultado:", type(Forma().area()).__name__)
print()
total = sum(f.area() for f in formas)
print(f"Total de las tres áreas: {total:.2f}")
print("Cuánto aportó la forma genérica:", Forma().area())
"""),

md("""
`Forma: 0` en el primer renglón, y un total que incluye una forma que no tiene forma.

En el archivo original, `Forma.area` es `pass`, así que devuelve `None` y la salida documentada del
archivo dice `Area of Shape: None`. Aquí devuelve cero, que es peor: el `None` por lo menos se ve raro y
rompe la suma. El cero se suma sin protestar y desaparece.

El problema de fondo no es el valor de retorno. **Es que `Forma()` se pudo construir.** Una forma sin
forma no es nada; existe solo porque nadie lo impidió. Cualquier valor que devuelva su `area` va a ser
mentira.

Ahí empieza el bloque 2.
"""),

md("""
---
# Bloque 2 · Clases abstractas e interfaces

Una clase que existe para obligar a otras a escribir un método. No se instancia, y en eso está toda su
utilidad.
"""),

code("""
from abc import ABC, abstractmethod


class FormaAbstracta(ABC):
    def mostrar(self):
        print(f"  {type(self).__name__}: {self.area():.2f}")

    @abstractmethod
    def area(self):
        \"\"\"Cada hija tiene que escribir esto.\"\"\"


class CirculoBueno(FormaAbstracta):
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return 3.1416 * self.radio ** 2


class RectanguloBueno(FormaAbstracta):
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto

    def area(self):
        return self.ancho * self.alto


for forma in [CirculoBueno(5), RectanguloBueno(4, 5)]:
    forma.mostrar()

print()
print("Métodos que FormaAbstracta obliga a escribir:",
      sorted(FormaAbstracta.__abstractmethods__))
"""),

code("""
# FALLA A PROPÓSITO. La clase abstracta no se puede construir.
try:
    FormaAbstracta()
except TypeError as e:
    print("TypeError:", e)

print()


class Triangulo(FormaAbstracta):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    # se nos olvidó escribir area


try:
    Triangulo(3, 4)
except TypeError as e:
    print("TypeError:", e)

print()
print("Lo que le falta a Triangulo:", sorted(Triangulo.__abstractmethods__))
"""),

md("""
Las dos construcciones fallan, y las dos fallan **en el momento de construir**, que es lo que uno quiere.

`FormaAbstracta()` no se puede construir porque declara un método abstracto y no lo implementa.
`Triangulo(3, 4)` tampoco, porque heredó el hueco y no lo llenó.

Compara eso con la celda de hace un rato. Ahí la forma genérica se construía, entraba en la lista,
sumaba cero y nadie se enteraba nunca. Aquí el error aparece en la línea que lo causó, con el nombre del
método que falta.

**Ese es el trato: la clase abstracta cambia una falla silenciosa y tardía por un error ruidoso y
temprano.**

## Los dos ingredientes tienen que ir juntos
"""),

code("""
# FALLA A PROPÓSITO, y no truena. El decorador sin heredar de ABC.
class FormaFloja:                     # no hereda de ABC
    @abstractmethod
    def area(self):
        ...


class CirculoFlojo(FormaFloja):
    pass                              # tampoco escribe area


floja = FormaFloja()
flojo = CirculoFlojo()

print("La abstracta se construyó:", floja)
print("La hija incompleta también:", flojo)
print()
print("¿Tiene __abstractmethods__?", hasattr(FormaFloja, "__abstractmethods__"))
print("Metaclase de FormaFloja:     ", type(FormaFloja).__name__)
print("Metaclase de FormaAbstracta: ", type(FormaAbstracta).__name__)
print()
print("Y al llamar al método vacío:", flojo.area())
"""),

md("""
Las dos clases se construyeron sin una queja, y `area()` devolvió `None`.

`@abstractmethod` por su cuenta **no impide nada**. Lo único que hace es poner una marca en la función.
Quien revisa esa marca y se niega a construir el objeto es `ABCMeta`, la metaclase que llega al heredar
de `ABC`, y la última línea de la celda lo enseña: `type(FormaFloja)` es `type` a secas, mientras que
`type(FormaAbstracta)` es `ABCMeta`.

Es el error 02 de la diapositiva y es especialmente traicionero porque el código **parece** correcto. El
decorador está ahí, se lee bien, y no hace absolutamente nada.

## Cuatro maneras de declarar un contrato

| Tipo de clase | Se instancia | Trae código | En Python |
|---|---|---|---|
| Concreta | Sí | Todo | `class Perro(Animal):` |
| Abstracta | No | Una parte | `class Stream(ABC):` |
| Interfaz | No | Nada | Solo `@abstractmethod` |
| Protocolo | No aplica | Nada | `typing.Protocol` |

Los dos de en medio se distinguen por cuánto código traen y no por la sintaxis. Una interfaz es una
abstracta donde **todos** los métodos son abstractos: declara el contrato completo y no implementa nada.

El cuarto es distinto y vale la pena verlo, porque es lo que llevas usando desde la semana 6 sin
nombrarlo.
"""),

code("""
from typing import Protocol


class SabeLeer(Protocol):
    def leer(self) -> str:
        ...


class LectorDeArchivo:               # no hereda de nada
    def leer(self):
        return "contenido del archivo"


class LectorDeRed:                   # tampoco
    def leer(self):
        return "contenido de la red"


def procesar(fuente: SabeLeer) -> None:
    print("  ", fuente.leer())


for fuente in [LectorDeArchivo(), LectorDeRed()]:
    procesar(fuente)

print()
print("¿SabeLeer está en la cadena de LectorDeArchivo?",
      SabeLeer in LectorDeArchivo.__mro__)
print("Cadena de LectorDeArchivo:", [c.__name__ for c in LectorDeArchivo.__mro__])
print("Cadena de LectorDeRed:    ", [c.__name__ for c in LectorDeRed.__mro__])
print("Lo único que comparten:", sorted(
    {n for n in dir(LectorDeArchivo) if not n.startswith("_")} &
    {n for n in dir(LectorDeRed) if not n.startswith("_")}))
"""),

md("""
Ninguna de las dos clases hereda de `SabeLeer`, y las dos funcionan.

Eso es **tipado de pato**: si camina como pato y grazna como pato, es un pato. En Python lo único que
hace falta para que un objeto sirva es que tenga el método, y esa fue la razón por la que en la semana 6
la computadora aceptó tres discos que no compartían nada.

`typing.Protocol` le pone nombre a esa expectativa para que las herramientas de análisis la revisen, sin
obligar a nadie a heredar. Es lo más parecido a una interfaz de Java que Python tiene, y no cambia nada
en tiempo de ejecución.

**Cuándo usar cada una.** Si quieres compartir código además del contrato, clase abstracta. Si solo
quieres declarar qué métodos hacen falta y las clases ya existen o vienen de otra biblioteca, protocolo.

Dos cosas que sorprenden del protocolo.
"""),

code("""
# FALLA A PROPÓSITO. Un protocolo no se puede usar con isinstance así nomás.
try:
    print(isinstance(LectorDeArchivo(), SabeLeer))
except TypeError as e:
    print("TypeError:", e)

print()

from typing import runtime_checkable


@runtime_checkable
class SabeLeerRevisable(Protocol):
    def leer(self) -> str:
        ...


print("Con @runtime_checkable:", isinstance(LectorDeArchivo(), SabeLeerRevisable))
print("Y con algo que no lee: ", isinstance(42, SabeLeerRevisable))
"""),

md("""
Un protocolo, tal cual, es una declaración para las herramientas de análisis y no existe en tiempo de
ejecución. Para usarlo con `isinstance` hay que marcarlo con `@runtime_checkable`, y aun así solo revisa
que el método exista, no que haga lo que promete.

Eso último es la debilidad de fondo del tipado de pato, y se ve mejor con un ejemplo.
"""),

code("""
# FALLA A PROPÓSITO, y no truena. Dos clases con el mismo método y significados distintos.
class Circulo3:
    def dibujar(self):
        return "un circulito en el lienzo"


class Vaquero:
    def dibujar(self):
        return "el vaquero desenfunda"        # dibujar, como sacar la pistola


lienzo = [Circulo3(), Circulo3(), Vaquero()]

for figura in lienzo:
    print(" ", figura.dibujar())

print()
print("Todos tienen el método:", all(hasattr(f, "dibujar") for f in lienzo))
print("Todos pasan el protocolo:", all(callable(getattr(f, "dibujar")) for f in lienzo))
print("Todos significan lo mismo: no")
"""),

md("""
El vaquero pasó todas las revisiones que Python puede hacer y aun así no tenía nada que hacer en un
lienzo.

Un nombre de método no es un contrato: es media palabra. `isinstance` con un protocolo revisa la firma,
`hasattr` revisa el nombre, y ninguno de los dos puede revisar el significado.

Cuando eso importa de verdad, la clase abstracta gana: heredar de `FormaAbstracta` es una declaración
explícita de intención, y el vaquero nunca la habría escrito. El tipado de pato es más flexible y más
barato; la abstracta es más estricta y más clara. Los dos se usan, y saber cuál pediste es la parte que
se aprende.

## El `if isinstance` que hace polimorfismo a mano
"""),

code("""
# FALLA A PROPÓSITO, y no truena. La cadena de ifs que se olvida de la clase nueva.
def area_de(forma):
    if isinstance(forma, CirculoBueno):
        return 3.1416 * forma.radio ** 2
    elif isinstance(forma, RectanguloBueno):
        return forma.ancho * forma.alto
    return 0                          # el caso que se traga todo


class TrianguloBueno(FormaAbstracta):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura / 2


figuras = [CirculoBueno(5), RectanguloBueno(4, 5), TrianguloBueno(3, 4)]

print("Con la cadena de ifs:")
for f in figuras:
    print(f"  {type(f).__name__:<18}{area_de(f):.2f}")

print()
print("Con la llamada polimórfica:")
for f in figuras:
    print(f"  {type(f).__name__:<18}{f.area():.2f}")

print()
coinciden = sum(1 for f in figuras if abs(area_de(f) - f.area()) < 1e-9)
print(f"{coinciden} de {len(figuras)} coinciden con el método de la clase")
print("Diferencia en el triángulo:", f"{figuras[2].area() - area_de(figuras[2]):.2f}")
"""),

md("""
El triángulo mide seis y la cadena de `if` dice que mide cero.

La clase se escribió correctamente, hereda de la abstracta, y su `area` funciona. Lo que falló es una
función que enumeraba tipos y que nadie actualizó, porque nada la obliga a estar completa.

El `return 0` del final es el culpable de que no truene. Un `else: raise` habría convertido esto en un
error ruidoso, y esa es la corrección mínima cuando de verdad no se puede evitar la cadena. La
corrección de fondo es la línea de abajo: `f.area()`, que no enumera nada.

**Si en tu ciclo hay un `if` por tipo, todavía no estás usando polimorfismo.**

## Cuando la firma cambia
"""),

code("""
# FALLA A PROPÓSITO. La hija sobrescribe pidiendo otros argumentos.
class Exportador:
    def exportar(self, datos):
        return f"exportando {len(datos)} renglones"


class ExportadorCSV(Exportador):
    def exportar(self, datos):
        return f"csv con {len(datos)} renglones"


class ExportadorPDF(Exportador):
    def exportar(self, datos, plantilla):      # un argumento de más
        return f"pdf con {len(datos)} renglones, plantilla {plantilla}"


DATOS = [1, 2, 3]
for exp in [Exportador(), ExportadorCSV(), ExportadorPDF()]:
    try:
        print(" ", exp.exportar(DATOS))
    except TypeError as e:
        print("  TypeError:", e)
"""),

md("""
Los dos primeros contestaron y el tercero reventó, en el mismo ciclo, sin que la lista tuviera nada de
raro.

Sobrescribir cambia el cuerpo. Si además cambias la firma, el método ya no es el mismo método: es otro
con el mismo nombre, y el ciclo polimórfico no puede llamarlo.

Es el error 01 de la diapositiva, y es primo de lo que la semana 7 llamó sustitución: **donde funcionaba
la madre tiene que seguir funcionando la hija**. Una firma distinta lo rompe de la manera más directa
posible.

La salida cuando la hija de verdad necesita más datos: que los reciba en el constructor.
`ExportadorPDF(plantilla="factura")` guarda la plantilla y `exportar(datos)` la lee de `self`. La firma
vuelve a encajar y el ciclo vuelve a funcionar.

## Cuatro maneras de romper el contrato

| | El error | Cómo se ve |
|---|---|---|
| 01 | Sobrescribir cambiando la firma | El ciclo polimórfico revienta en el tercer objeto |
| 02 | `@abstractmethod` sin heredar de `ABC` | El decorador no impide nada y la clase se instancia |
| 03 | Preguntar el tipo antes de llamar | Polimorfismo a mano, que hay que tocar en cada clase nueva |
| 04 | Una abstracta con un solo hijo | Una capa extra que no abstrae nada |
"""),

code("""
# FALLA A PROPÓSITO, y no truena. Una abstracción con un solo hijo.
class RepositorioAbstracto(ABC):
    @abstractmethod
    def guardar(self, dato): ...

    @abstractmethod
    def leer(self, clave): ...

    @abstractmethod
    def borrar(self, clave): ...


class RepositorioEnMemoria(RepositorioAbstracto):
    def __init__(self):
        self.datos = {}

    def guardar(self, dato):
        self.datos[dato["id"]] = dato

    def leer(self, clave):
        return self.datos.get(clave)

    def borrar(self, clave):
        self.datos.pop(clave, None)


repo = RepositorioEnMemoria()
repo.guardar({"id": "X1", "nombre": "café"})
print("Leído:", repo.leer("X1"))

print()
hijas = RepositorioAbstracto.__subclasses__()
print("Hijas de la abstracta:", [c.__name__ for c in hijas], "->", len(hijas))
print("Métodos declarados en la abstracta:", len(RepositorioAbstracto.__abstractmethods__))
print("Clases que declaran guardar:",
      [c.__name__ for c in RepositorioEnMemoria.__mro__ if "guardar" in vars(c)])
"""),

md("""
Funciona perfecto, y no sirve para nada.

Una clase abstracta con un solo hijo no abstrae: duplica. Cada método está declarado dos veces, cada
cambio hay que hacerlo en dos lugares, y para entender una llamada hay que abrir dos clases en lugar de
una. El contrato no protege a nadie porque no hay nadie del otro lado.

La abstracción se gana el lugar cuando hay dos implementaciones **reales**, no cuando imaginas que algún
día habrá una segunda. Si de verdad llega, extraer la abstracta ese día toma diez minutos y ya sabes
qué métodos tiene que declarar, porque los dos casos están enfrente.

**La regla: primero escribe la segunda clase, después extrae la abstracta.**
"""),

md("""
---
# Bloque 3 · Primer parcial

El examen cierra las unidades 1, 2 y 3. Se presenta esta misma semana, a máquina, con el repositorio del
curso abierto y sin ayuda de terceros.

| Unidad | Qué entra |
|---|---|
| U1 · Introducción | Paradigmas, concepto de objeto, ventajas del enfoque y los casos donde estorba |
| U2 · Elementos básicos | Clases, objetos, atributos, métodos, propiedades, acceso, constructores, miembros de clase |
| U3 · Propiedades fundamentales | Encapsulamiento, ocultamiento, reutilización, herencia, jerarquía, polimorfismo, abstractas |
| Fuera | Archivos, interfaces gráficas y bases de datos, que son del segundo parcial |

## Cómo prepararse

**El parcial pide escribir clases, no describirlas.** Si no puedes teclear de memoria una clase con
constructor, atributo privado, propiedad y una hija que sobrescribe un método, todavía no la sabes.

**Qué practicar.** Los laboratorios de las semanas 4, 6 y 7, resueltos otra vez sin abrir la solución.

**Qué revisar.** Los cuadros de diagnóstico de cada semana. Los cuatro errores de cada uno son los del
examen.

**Qué no hacer.** Memorizar definiciones. Ninguna pregunta pide la definición de encapsulamiento.

La celda de abajo es un repaso de una sola pasada: junta en una clase casi todo lo que entra.
"""),

code("""
class Prestamo(ABC):
    \"\"\"Repaso de las tres unidades en una sola clase.\"\"\"

    DIAS_BASE = 14                          # atributo de clase, semana 4

    def __init__(self, titulo: str, dia: int) -> None:
        self.titulo = titulo                # público, semana 3
        self.__dia = dia                    # privado, semana 4
        self._historial = []                # protegido, semana 7

    @property                               # propiedad, semana 3
    def dia(self) -> int:
        return self.__dia

    @property
    def historial(self):
        return tuple(self._historial)       # copia defensiva, semana 6

    @abstractmethod                         # contrato, semana 8
    def dias_maximos(self) -> int: ...

    def vencido(self, hoy: int) -> bool:    # método plantilla
        self._historial.append(hoy)
        return hoy - self.__dia > self.dias_maximos()

    def __repr__(self) -> str:              # método mágico, semana 5
        return f"{type(self).__name__}({self.titulo!r})"


class PrestamoDeLibro(Prestamo):
    def dias_maximos(self):
        return Prestamo.DIAS_BASE


class PrestamoDeRevista(Prestamo):
    def dias_maximos(self):
        return 7


class PrestamoDocente(PrestamoDeLibro):     # herencia de dos niveles, semana 7
    def dias_maximos(self):
        return super().dias_maximos() * 3


prestamos = [PrestamoDeLibro("El Aleph", 1),
             PrestamoDeRevista("Nature", 1),
             PrestamoDocente("Cálculo II", 1)]

for p in prestamos:                          # polimorfismo, semana 8
    print(f"  {p!r:<32}plazo {p.dias_maximos():>2}  vencido al 20: {p.vencido(20)}")

print()
print("Historial del primero:", prestamos[0].historial)
try:
    prestamos[0].historial.append(99)
except AttributeError as e:
    print("Y no se puede tocar desde fuera:", e)
"""),

md("""
Nueve conceptos del semestre en cuarenta líneas, y todos están en la rúbrica del examen.

Recórrela otra vez señalando cada uno: el atributo de clase, el privado con dos guiones bajos, el
protegido con uno, las dos propiedades, la copia defensiva, el método abstracto, el método plantilla que
llama al abstracto, el `__repr__`, los dos niveles de herencia, y el ciclo que no pregunta tipos.

Si puedes escribir esa clase desde cero explicando cada decisión, el parcial está aprobado.
"""),

md("""
---
## Cuatro errores de esta sesión

**Sobrescribir sin llamar al padre.** Lo que el padre hacía se pierde, y el síntoma es una lista vacía,
no una excepción.

**`@abstractmethod` sin `ABC`.** El decorador solo pone una marca. Quien impide construir el objeto es
la metaclase que llega con `ABC`.

**La cadena de `if isinstance` con un caso por omisión.** La clase nueva cae en el `return 0` y devuelve
un número creíble.

**Sobrescribir cambiando la firma.** El ciclo polimórfico revienta en el objeto que la cambió, y el
error señala la llamada y no la clase.
"""),

md("""
---
# Ejercicios

El laboratorio de esta semana es un simulacro del parcial en parejas. Los ejercicios recorren lo que
entra.

Las soluciones están hasta abajo del cuaderno.

### Ejercicio 1 · Tres voces

Escribe `Instrumento` con un método `sonar`, y tres hijas que lo sobrescriban. Recórrelas en un ciclo y
después agrega una cuarta clase sin tocar el ciclo.

Cuenta cuántas líneas del ciclo tuviste que editar.

### Ejercicio 2 · Extender contra reemplazar

Escribe un padre con un método que valide, y dos hijas: una que llame a `super()` y otra que no.
Demuestra con una lista de resultados qué se perdió en la segunda.

### Ejercicio 3 · El método plantilla

Escribe una clase con un método que llame a otro método del mismo objeto, y una hija que sobrescriba
solo el segundo. Comprueba que el primero, heredado sin cambios, usa la versión de la hija.

Imprime en qué clase está escrito cada uno usando `__mro__`.

### Ejercicio 4 · La abstracta

Convierte la clase del ejercicio 3 en abstracta con `ABC` y `@abstractmethod`. Intenta construirla,
atrapa el `TypeError`, y después escribe una hija incompleta y atrapa el otro.

Imprime `__abstractmethods__` de las dos.

### Ejercicio 5 · El decorador solo

Escribe la misma clase con `@abstractmethod` pero **sin** heredar de `ABC`. Constrúyela, llama al método
abstracto, e imprime `type()` de las dos clases para enseñar la diferencia.

### Ejercicio 6 · La cadena de ifs

Escribe una función que calcule algo con `if isinstance` para dos clases y un caso por omisión. Agrega
una tercera clase y muestra la diferencia entre lo que devuelve la función y lo que devuelve el método.

Después reescríbela en una línea.

### Ejercicio 7 · La firma que no encaja

Escribe tres clases con el mismo método, y haz que la tercera pida un argumento de más. Recórrelas en un
ciclo y atrapa el `TypeError`.

Arréglalo pasando ese dato por el constructor y vuelve a correr el mismo ciclo.

### Ejercicio 8 · Tipado de pato

Escribe dos clases sin ningún padre común pero con el mismo método, y una función que las use a las dos.
Comprueba con `__mro__` que no comparten nada arriba de `object`.

Declara el protocolo con `typing.Protocol` y explica en un comentario qué cambió en tiempo de ejecución.

### Ejercicio 9 · El laboratorio

En parejas, escriban tres preguntas de código al estilo de las que vimos, una por unidad, y ninguna que
se pueda contestar con una definición.

Intercámbienlas con otra pareja y califiquen las respuestas con una rúbrica de dos líneas.

El criterio es que cada pregunta tenga una respuesta correcta y una trampa que suene razonable.
"""),

md("""
---
## Tres ideas para llevarse

**Sobrescribir cambia el cuerpo, no el nombre.** La hija reemplaza el método del padre y quien llama no
se entera de que hubo un cambio. Si además llamas a `super()`, extiendes en lugar de reemplazar, y esa
decisión se toma a propósito.

**Una clase abstracta declara el contrato.** Dice qué métodos habrá sin escribir el cómo, y obliga a cada
hija a completarlo. Convierte una falla silenciosa y tardía en un error ruidoso al construir.

**El polimorfismo borra el `if` de tipos.** Agregar una clase nueva no toca una línea del código que ya
la va a usar, y esa propiedad es la razón por la que el paradigma existe.

Con esto cierra el tema 3 y el primer parcial. La semana 9 abre la unidad de aplicación con funciones
que se prueban solas, código repartido en piezas y funciones que se llaman a sí mismas.

### Lo que se llevan de las tres unidades

Un objeto junta datos y comportamiento. Una clase describe cómo se hace uno. Lo que dejas público es una
promesa. Lo que se declara en la clase se comparte. Asignar no copia. Y un ciclo que no pregunta de qué
clase es cada objeto es un ciclo que no vas a tener que volver a abrir.
"""),

md("""
---
# Soluciones

### Ejercicio 1

```python
class Instrumento:
    def sonar(self):
        print("sonido genérico")


class Guitarra(Instrumento):
    def sonar(self):
        print("tran")


class Bateria(Instrumento):
    def sonar(self):
        print("pum")


class Violin(Instrumento):
    def sonar(self):
        print("iiii")


orquesta = [Guitarra(), Bateria(), Violin()]
for i in orquesta:
    i.sonar()


class Trompeta(Instrumento):
    def sonar(self):
        print("tuuu")


orquesta.append(Trompeta())
for i in orquesta:            # el mismo ciclo, sin cambios
    i.sonar()

# Cero líneas del ciclo. Lo único que cambió es la lista, que es datos y no
# código.
```

### Ejercicio 2

```python
class Formulario:
    def __init__(self):
        self.errores = []

    def validar(self, dato):
        if not dato:
            self.errores.append("campo vacío")
        return len(self.errores) == 0


class FormularioConAviso(Formulario):
    def validar(self, dato):
        print("  revisando", repr(dato))
        return super().validar(dato)


class FormularioSinAviso(Formulario):
    def validar(self, dato):
        print("  revisando", repr(dato))
        return True                    # se comió la validación


a = FormularioConAviso()
b = FormularioSinAviso()

for f in [a, b]:
    print(type(f).__name__, "->", f.validar(""))
    print("  errores registrados:", f.errores)
```

### Ejercicio 3

```python
class Reporte:
    def imprimir(self):
        print(f"  {self.encabezado()} | {self.cuerpo()}")

    def encabezado(self):
        return "REPORTE"

    def cuerpo(self):
        return "sin datos"


class ReporteDeVentas(Reporte):
    def cuerpo(self):
        return "ventas: 120"


ReporteDeVentas().imprimir()

for nombre in ["imprimir", "encabezado", "cuerpo"]:
    dueno = next(c.__name__ for c in ReporteDeVentas.__mro__ if nombre in vars(c))
    print(f"  {nombre:<12}escrito en {dueno}")
```

### Ejercicio 4

```python
from abc import ABC, abstractmethod


class Reporte(ABC):
    def imprimir(self):
        print(f"  {self.encabezado()} | {self.cuerpo()}")

    def encabezado(self):
        return "REPORTE"

    @abstractmethod
    def cuerpo(self): ...


try:
    Reporte()
except TypeError as e:
    print("TypeError:", e)


class ReporteVacio(Reporte):
    pass


try:
    ReporteVacio()
except TypeError as e:
    print("TypeError:", e)

print(sorted(Reporte.__abstractmethods__))
print(sorted(ReporteVacio.__abstractmethods__))
```

### Ejercicio 5

```python
class ReporteFlojo:
    @abstractmethod
    def cuerpo(self): ...


r = ReporteFlojo()
print("Se construyó:", r)
print("El método abstracto devuelve:", r.cuerpo())
print("type(ReporteFlojo):", type(ReporteFlojo).__name__)
print("type(Reporte):     ", type(Reporte).__name__)

# El decorador solo pone una marca en la función. Quien la revisa es ABCMeta, que
# llega heredando de ABC. Sin ella, la marca no la lee nadie.
```

### Ejercicio 6

```python
class Circulo:
    def __init__(self, r):
        self.r = r

    def area(self):
        return 3.1416 * self.r ** 2


class Cuadrado:
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado ** 2


class Triangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura / 2


def area_de(f):
    if isinstance(f, Circulo):
        return 3.1416 * f.r ** 2
    elif isinstance(f, Cuadrado):
        return f.lado ** 2
    return 0


for f in [Circulo(1), Cuadrado(2), Triangulo(3, 4)]:
    print(f"{type(f).__name__:<10}ifs: {area_de(f):>7.2f}   método: {f.area():>7.2f}")

# La versión de una línea:
print([round(f.area(), 2) for f in [Circulo(1), Cuadrado(2), Triangulo(3, 4)]])
```

### Ejercicio 7

```python
class Notificador:
    def enviar(self, mensaje):
        return f"generico: {mensaje}"


class PorCorreo(Notificador):
    def enviar(self, mensaje):
        return f"correo: {mensaje}"


class PorSMSRoto(Notificador):
    def enviar(self, mensaje, numero):
        return f"sms a {numero}: {mensaje}"


for n in [Notificador(), PorCorreo(), PorSMSRoto()]:
    try:
        print(" ", n.enviar("hola"))
    except TypeError as e:
        print("  TypeError:", e)


class PorSMS(Notificador):
    def __init__(self, numero):
        self.numero = numero

    def enviar(self, mensaje):
        return f"sms a {self.numero}: {mensaje}"


for n in [Notificador(), PorCorreo(), PorSMS("555-1111")]:
    print(" ", n.enviar("hola"))
```

### Ejercicio 8

```python
from typing import Protocol


class Imprimible(Protocol):
    def imprimir(self) -> None: ...


class Ticket:
    def imprimir(self):
        print("  ticket de compra")


class Etiqueta:
    def imprimir(self):
        print("  etiqueta de envío")


def mandar_a_la_impresora(cosa: Imprimible) -> None:
    cosa.imprimir()


for cosa in [Ticket(), Etiqueta()]:
    mandar_a_la_impresora(cosa)

print([c.__name__ for c in Ticket.__mro__])
print([c.__name__ for c in Etiqueta.__mro__])

# En tiempo de ejecución no cambió nada: Python nunca revisó el protocolo. Lo que
# cambió es que ahora una herramienta de análisis puede avisarme antes de correr
# el programa si le paso algo sin imprimir, y que la firma documenta lo que la
# función espera.
```

### Ejercicio 9

Tres preguntas de ejemplo, una por unidad, con la trampa que las hace útiles.

**U1.** Este programa resuelve el mismo problema con funciones y con una clase. ¿En cuál de los dos
agregar un tercer campo al cliente obliga a tocar más líneas, y por qué? La trampa: la versión con
clases es más larga, así que parece la peor.

**U2.** Esta clase tiene un `@property` sin `setter` y un atributo con dos guiones bajos. Escribe dos
líneas que intenten romperla desde fuera y di cuál de las dos lanza y cuál no. La trampa: las dos
parecen equivalentes.

**U3.** Esta jerarquía tiene tres clases y un ciclo que las recorre. Agrega una cuarta clase y di
cuántas líneas del ciclo cambian. La trampa: el ciclo tiene un `if isinstance` escondido a la mitad.

La rúbrica de dos líneas: **la respuesta correcta vale la mitad y explicar por qué la trampa era trampa
vale la otra mitad.**
"""),

]

write(OUT / "es" / "w08.ipynb", es)
print("wrote", OUT / "es" / "w08.ipynb")
