"""notebooks/programacion-orientada-a-objetos/es/w03.ipynb

Source deck: ppts/python/programacion-orientada-a-objetos/es/w03.es.yaml
Source code:  punto.py, dos_puntos.py, persona.py, rectangulo.py y compartido.py
              se escribieron para el deck. El código de clases del repositorio
              empieza en 02 - POO/6th Module, que alimenta las semanas 4 a 8.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from nbkit import md, code, write, REPO

OUT = REPO / "notebooks" / "programacion-orientada-a-objetos"

es = [

md("""
# Programación Orientada a Objetos · Semana 03
## Tema 2 · Elementos básicos

**COM102 · Facultad de Ingeniería · Profesor David Escobar-Castillejos**

Clases, objetos y el estado que guardan. El vocabulario mínimo del paradigma, con código que corre
hoy mismo.

La semana pasada terminó con una pista: `vars(ana)` devolvió un diccionario. Este cuaderno explica de
dónde salió ese diccionario, quién lo llena y por qué dos objetos de la misma clase pueden terminar
apuntando al mismo.

Al terminar vas a poder:

1. Distinguir una clase de un objeto, y decir cuál de los dos ocupa memoria.
2. Escribir un constructor y explicar cuándo corre sin que nadie lo llame.
3. Declarar métodos con `self`, y decir exactamente qué pasa si se te olvida.
4. Usar `@property` para exponer un cálculo con la sintaxis de un atributo.
5. Reconocer el atributo de clase compartido antes de que te cueste una tarde.

### Cómo se usa este cuaderno

Ejecuta las celdas en orden con **Shift + Enter**. Once fallan a propósito y llevan un comentario que
lo dice.

Siete de las once **no lanzan ninguna excepción**. Dos de esas siete son las que este semestre va a
cobrar más caro: el atributo con el nombre mal escrito, y la lista declarada en el cuerpo de la clase.
"""),

md("""
---
# Bloque 1 · La clase y el objeto

Dos palabras que se confunden todo el semestre si no se separan hoy.

Una **clase** es una plantilla que describe qué recuerda un objeto y qué sabe hacer. Se escribe una
sola vez.

Un **objeto** es una cosa construida a partir de esa plantilla, con su propia copia de los datos. Se
crean tantos como haga falta.

El molde de galletas contra las galletas. El plano contra la casa.
"""),

code("""
class Punto:
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def dibujar(self) -> None:
        print(f"Punto en ({self.x}, {self.y})")


p = Punto(1, 2)
p.dibujar()
"""),

md("""
Ocho líneas, y en ellas está casi todo el vocabulario del tema.

`class Punto:` abre la plantilla. La convención es nombre en singular y con mayúscula inicial, porque
describe una cosa y no un montón.

`def __init__(self, x, y)` es el **constructor**. Nadie lo llama a mano: corre solo, en el momento
exacto en que escribes `Punto(1, 2)`. Los dos guiones bajos de cada lado son la forma en que Python
marca los métodos que el lenguaje llama por ti, y en la semana 8 vas a escribir varios más.

`self.x = x` crea un atributo en **ese** objeto. El de la izquierda es el atributo y el de la derecha
es el parámetro; se llaman igual por costumbre, no por obligación.

`def dibujar(self)` es un **método**. Recibe `self` como primer parámetro, que es el objeto sobre el
que se llamó.

## Dos objetos, dos estados
"""),

code("""
a = Punto(1, 2)
b = Punto(9, 9)

a.x = 100

a.dibujar()
b.dibujar()

print()
print("¿son el mismo objeto?", a is b)
print("¿son iguales?        ", a == b)
print()
print("vars(a):", vars(a))
print("vars(b):", vars(b))
"""),

md("""
Cambiar `a.x` no tocó a `b`. Cada objeto trae su propio diccionario de atributos, y ese diccionario es
literalmente el estado del objeto.

`a == b` da `False` aunque los dos fueran `Punto`. Por omisión, comparar dos objetos con `==` es lo
mismo que compararlos con `is`: pregunta si son el mismo objeto, no si valen lo mismo. La semana 8
enseña cómo cambiar eso escribiendo `__eq__`.

## Los métodos viven una sola vez
"""),

code("""
print("El diccionario de la clase tiene el método:")
print("  ", [n for n in vars(Punto) if not n.startswith("__")])
print()
print("El de cada objeto no:")
print("   vars(a):", list(vars(a)))
print("   vars(b):", list(vars(b)))
print()
print("¿a y b comparten la misma función dibujar?",
      a.dibujar.__func__ is b.dibujar.__func__)
print("¿y es la que está en la clase?          ",
      a.dibujar.__func__ is Punto.dibujar)
"""),

md("""
La función `dibujar` existe una sola vez, guardada en la clase. Ni `a` ni `b` la tienen; los dos la
piden prestada cuando alguien escribe el punto.

Eso es lo que hace barato crear objetos. Diez mil puntos son diez mil diccionarios con dos números
cada uno, no diez mil copias del método.

## Qué es `self`, sin misterio
"""),

code("""
Punto.dibujar(a)          # llamando por la clase, pasando el objeto a mano
a.dibujar()               # la forma normal, exactamente lo mismo

print()
print("a.dibujar es de tipo    ", type(a.dibujar).__name__)
print("Punto.dibujar es de tipo", type(Punto.dibujar).__name__)
"""),

md("""
Las dos líneas hacen lo mismo. `a.dibujar()` es azúcar sintáctica de `Punto.dibujar(a)`.

Ahí está `self` completo: **el objeto sobre el que llamaste el método, pasado como primer argumento
por el lenguaje**. No es una palabra reservada, no es magia, y de hecho podrías nombrarlo `yo` y
funcionaría. No lo hagas: `self` es la convención universal y cambiarla solo confunde a quien lea tu
código.

Lo que sí importa es que ya lo conocías. En el repaso 4 escribiste `lista.append(3)`, que es
`list.append(lista, 3)` con otra cara. Los métodos de las listas siempre recibieron su objeto como
primer parámetro.
"""),

code("""
# FALLA A PROPÓSITO. El método sin self en la definición.
class PuntoRoto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dibujar():           # sin self
        print("no llego a imprimirme")


roto = PuntoRoto(1, 2)
try:
    roto.dibujar()
except TypeError as e:
    print("TypeError:", e)
"""),

md("""
"takes 0 positional arguments but 1 was given". El mensaje confunde a todo el mundo la primera vez,
porque la llamada fue `roto.dibujar()` y ahí no hay ningún argumento a la vista.

El argumento lo puso Python. `roto.dibujar()` se convierte en `PuntoRoto.dibujar(roto)`, y esa función
no acepta ninguno. Cuando leas ese mensaje, lo primero que hay que revisar es si falta el `self`.
"""),

code("""
# FALLA A PROPÓSITO, y no truena. El método sin paréntesis.
print(p.dibujar)
print()
print("¿Se imprimió el punto? No. Se imprimió la referencia al método.")
print("Tipo:", type(p.dibujar).__name__)
"""),

md("""
Es el mismo error del repaso 3 con las funciones sueltas, con otro disfraz. Sin paréntesis, el nombre
es solo el nombre.

Aquí duele más porque los `@property` de dentro de un rato **sí** se leen sin paréntesis, así que
`r.area` y `r.calcular()` conviven en la misma clase y hay que saber cuál es cuál.
"""),

md("""
---
# Bloque 2 · Atributos, métodos y propiedades

Qué recuerda el objeto, qué sabe hacer, y qué finge ser un dato sin serlo.

## Los atributos se pueden crear desde cualquier parte
"""),

code("""
# FALLA A PROPÓSITO, y no truena. Un atributo mal escrito se crea en silencio.
punto = Punto(1, 2)
punto.dibujar()

punto.cordenada_x = 500      # queríamos escribir punto.x

punto.dibujar()
print()
print("Estado del objeto:", vars(punto))
print("Atributos que tiene:", len(vars(punto)))
"""),

md("""
El punto sigue en (1, 2) y ahora carga un atributo de más que nadie va a leer nunca.

Python permite agregarle atributos a un objeto en cualquier momento, y no revisa contra la clase.
Escribir `punto.cordenada_x` en vez de `punto.x` no es un error de nombre, es un atributo nuevo, y el
único síntoma es que el valor que asignaste no aparece por ningún lado.

Es el mismo mecanismo del diccionario del repaso 4: `d["llave_mal_escrita"] = 5` tampoco falla, crea
una llave. Y no es casualidad, porque **el estado del objeto es un diccionario**, el que imprime
`vars`.

## El atributo que no se toca desde fuera
"""),

code("""
class Persona:
    def __init__(self, nombre: str, edad: int) -> None:
        self.__nombre = nombre       # dos guiones bajos al principio
        self.edad = edad             # la edad cambia con los años, va pública

    def hablar(self) -> None:
        print(f"Hola, me llamo {self.__nombre}")


ana = Persona("Ana", 20)
ana.hablar()
ana.edad = 21
print("Edad:", ana.edad)

print()
print("Lo que el objeto guarda de verdad:", vars(ana))
"""),

md("""
El atributo no se llama `__nombre` en el diccionario. Se llama `_Persona__nombre`.

Eso es **name mangling**: cuando Python ve un atributo que empieza con dos guiones bajos dentro de una
clase, le pega el nombre de la clase adelante. Dentro de los métodos la traducción es automática y por
eso `self.__nombre` funciona; desde fuera hay que escribir el nombre largo.
"""),

code("""
# FALLA A PROPÓSITO. Desde fuera, ese nombre no existe.
try:
    print(ana.__nombre)
except AttributeError as e:
    print("AttributeError:", e)

print()
print("Pero con el nombre real sí:", ana._Persona__nombre)
"""),

md("""
No es un candado. Es un cerrojo de los que se abren empujando: el dato sigue ahí y con el nombre
completo se lee sin problema.

Lo que sí evita es tocarlo por accidente, que es su propósito real. Y evita otra cosa que se ve en la
semana 7: que una clase hija defina un atributo con el mismo nombre y pise el de la madre sin
enterarse.

## La consecuencia que nadie espera
"""),

code("""
# FALLA A PROPÓSITO, y no truena. Asignar el nombre corto desde fuera.
ana.__nombre = "impostor"

ana.hablar()
print()
print("Estado del objeto:", vars(ana))
print("Atributos:", len(vars(ana)))
"""),

md("""
El objeto ahora tiene dos atributos que parecen el mismo, `_Persona__nombre` con `"Ana"` y `__nombre`
con `"impostor"`, y `hablar` sigue diciendo Ana.

Quien escribió esa línea creía estar cambiando el nombre. No cambió nada visible, no recibió ningún
error, y dejó basura en el objeto. Es el error del typo de hace unas celdas, agravado porque aquí
parece que sabes lo que estás haciendo.

## Propiedades: un cálculo que se lee como dato
"""),

code("""
class Rectangulo:
    def __init__(self, ancho: float, alto: float) -> None:
        self.ancho = ancho
        self.alto = alto

    @property
    def area(self) -> float:
        return self.ancho * self.alto

    @property
    def perimetro(self) -> float:
        return 2 * (self.ancho + self.alto)


r = Rectangulo(3, 4)
print("Área:     ", r.area)          # sin paréntesis
print("Perímetro:", r.perimetro)

r.ancho = 10
print()
print("Tras cambiar el ancho a 10:")
print("Área:     ", r.area)
print("Perímetro:", r.perimetro)
print()
print("Lo que el objeto guarda:", vars(r))
"""),

md("""
El área pasó de 12 a 40 sola. Y fíjate en la última línea: **el área no está en el diccionario del
objeto**. No se guarda, se calcula cada vez que alguien la lee.

`@property` convierte un método en algo que se lee sin paréntesis. Eso no es cosmética, es una
garantía: un valor que se calcula al momento de leerlo no puede quedar desactualizado.

La versión sin propiedad enseña por qué importa.
"""),

code("""
# FALLA A PROPÓSITO, y no truena. El área guardada como atributo normal.
class RectanguloRoto:
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto
        self.area = ancho * alto      # se calcula una vez, al construir


caja = RectanguloRoto(3, 4)
print("Área al construir:", caja.area)

caja.ancho = 10

print("Ancho:", caja.ancho, "· alto:", caja.alto)
print("Área que reporta: ", caja.area)
print("Área verdadera:   ", caja.ancho * caja.alto)
print()
print("Estado:", vars(caja))
"""),

md("""
Un rectángulo de 10 por 4 que reporta un área de 12.

El número se calculó una vez, cuando el ancho era 3, y ahí se quedó. Nadie lo volvió a mirar. Es el
mismo problema de las listas paralelas de la semana 2, encogido hasta caber dentro de un solo objeto:
dos datos que deberían estar sincronizados y nada que los sincronice.

Con `@property` ese estado imposible no se puede alcanzar, porque el área no existe hasta que la
pides.
"""),

code("""
# FALLA A PROPÓSITO. Una propiedad de solo lectura no acepta asignación.
try:
    r.area = 99
except AttributeError as e:
    print("AttributeError:", e)

print()
print("El área sigue en:", r.area)
"""),

md("""
`AttributeError: property 'area' of 'Rectangulo' object has no setter`.

Eso también es una garantía y no una molestia. El área es una consecuencia del ancho y el alto, así
que fijarla directamente no tendría sentido: ¿cuál de los dos lados cambiaría?

Cuando sí quieras permitir la asignación, `@area.setter` existe y la semana 4 lo cubre junto con los
modificadores de acceso.

**Cuándo no usar una propiedad.** Si el cálculo es caro, escóndelo detrás de un método normal. Los
paréntesis son la señal de que ahí va a pasar algo, y `r.area` sugiere que leer es gratis.

## Las cinco palabras del tema

| Término | Qué es | Sintaxis |
|---|---|---|
| Clase | La plantilla | `class Punto:` |
| Objeto | Una instancia con estado propio | `p = Punto(1, 2)` |
| Atributo | Un dato que el objeto recuerda | `self.x = x` |
| Método | Algo que el objeto sabe hacer | `def dibujar(self):` |
| Propiedad | Un cálculo que se lee como dato | `@property` |
"""),

md("""
---
# Bloque 3 · El atributo de clase

## Predice antes de correr

¿Qué imprime la última línea?

```python
class Carrito:
    productos = []

    def __init__(self, dueno):
        self.dueno = dueno

    def agregar(self, sku):
        self.productos.append(sku)


a = Carrito("Ana")
b = Carrito("Luis")
a.agregar("X1")
print(len(b.productos))
```

- **A.** 0, porque `b` nunca agregó nada.
- **B.** 1, porque la lista vive en la clase.
- **C.** Error, `productos` no está definido en `__init__`.
- **D.** 2, porque cada carrito duplica la lista.
"""),

code("""
# FALLA A PROPÓSITO, y no truena. Este es el error caro de la semana.
class Carrito:
    productos = []

    def __init__(self, dueno):
        self.dueno = dueno

    def agregar(self, sku):
        self.productos.append(sku)


a = Carrito("Ana")
b = Carrito("Luis")
a.agregar("X1")

print("len(b.productos):", len(b.productos))
print("El carrito de Luis:", b.productos)
print()
print("vars(a):", vars(a))
print("vars(b):", vars(b))
print("Carrito.productos:", Carrito.productos)
print()
print("¿es la misma lista?",
      a.productos is b.productos is Carrito.productos)
"""),

md("""
La respuesta es **B**.

Los dos diccionarios de instancia traen únicamente el dueño. `productos` no está en ninguno de los
dos, porque nunca se asignó sobre `self`: se declaró en el cuerpo de la clase, y ahí existe una sola
vez para todos los carritos.

| Paso | Instrucción | a.dueno | b.dueno | Carrito.productos |
|---|---|---|---|---|
| 1 | `a = Carrito('Ana')` | Ana | no existe | `[]` |
| 2 | `b = Carrito('Luis')` | Ana | Luis | `[]` |
| 3 | `a.agregar('X1')` | Ana | Luis | `['X1']` |
| 4 | `len(b.productos)` | Ana | Luis | `['X1']` |

Cuando escribes `b.productos`, Python busca `productos` en el diccionario de `b`, no lo encuentra, y
sube a la clase. Encuentra la lista de todos y la devuelve. Por eso los dos carritos ven lo mismo.

**Este mecanismo ya lo viste dos veces.** En el repaso 3, con la lista puesta como valor por defecto
de una función, que se creaba una sola vez y acumulaba entre llamadas. En el repaso 4, con la
asignación que no copia y deja dos nombres sobre un solo objeto. Es el mismo, con una clase encima.

## La corrección que parece corrección
"""),

code("""
# FALLA A PROPÓSITO, y no truena. "Arreglarlo" asignando en una instancia.
b.productos = []              # ahora b sí tiene la suya

print("vars(b):", vars(b))
print()
b.agregar("Y1")
a.agregar("X2")

print("Carrito de Ana: ", a.productos)
print("Carrito de Luis:", b.productos)
print("En la clase:    ", Carrito.productos)
print()
c = Carrito("Carla")
print("Carrito de Carla:", c.productos, "<- estrena con las compras de Ana")
"""),

md("""
El carrito de Luis quedó bien y el de Ana sigue siendo el de la clase. El tercer cliente que llegue
estrena su carrito con lo que compró Ana.

Asignar sobre la instancia no borra el atributo de clase: le pone uno encima solo a ese objeto. El
problema queda parchado para quien te lo reportó y sigue vivo para todos los demás, que es la peor
forma de arreglar un error.

## La corrección de verdad
"""),

code("""
class CarritoBueno:
    def __init__(self, dueno):
        self.dueno = dueno
        self.productos = []          # una lista nueva por objeto

    def agregar(self, sku):
        self.productos.append(sku)


a = CarritoBueno("Ana")
b = CarritoBueno("Luis")
a.agregar("X1")

print("Ana: ", a.productos)
print("Luis:", b.productos)
print("¿la misma lista?", a.productos is b.productos)
print()
print("vars(a):", vars(a))
print("vars(b):", vars(b))
"""),

md("""
La corrección cabe en una línea, y la regla también: **todo lo que deba ser distinto en cada objeto se
asigna dentro de `__init__`, sobre `self`.**

`self.productos = []` corre una vez por cada objeto que se crea, así que hay tantas listas como
carritos.

## Cuándo el atributo de clase sí sirve
"""),

code("""
class Prestamo:
    DIAS_MAXIMOS = 14                # constante, igual para todos
    total_creados = 0                # contador de toda la clase

    def __init__(self, titulo, dia_prestamo):
        self.titulo = titulo
        self.dia_prestamo = dia_prestamo
        Prestamo.total_creados += 1   # sobre la clase, a propósito

    def vencido(self, dia_actual):
        return dia_actual - self.dia_prestamo > Prestamo.DIAS_MAXIMOS


uno = Prestamo("Estructuras de datos", 1)
dos = Prestamo("Cálculo II", 5)

print("Días máximos:", Prestamo.DIAS_MAXIMOS)
print("Préstamos creados:", Prestamo.total_creados)
print()
for prestamo in [uno, dos]:
    print(f"{prestamo.titulo:<24}vencido al día 20: {prestamo.vencido(20)}")
"""),

md("""
Aquí compartir es lo que se quiere. `DIAS_MAXIMOS` es una regla de la biblioteca, no de cada préstamo,
y si mañana cambia a veintiuno se cambia en un solo lugar. `total_creados` cuenta objetos, así que por
definición no puede vivir en uno de ellos.

La diferencia con el carrito no está en la sintaxis, está en la pregunta: **¿este dato es del objeto o
del concepto?** Los productos son del carrito. El plazo máximo es de la biblioteca.

Ojo con el detalle de `Prestamo.total_creados += 1`. Escribirlo como `self.total_creados += 1`
funcionaría a medias y de la peor manera: leería el de la clase, sumaría uno, y guardaría el resultado
como atributo de instancia. Cada objeto acabaría con su propio contador en 1.
"""),

code("""
# FALLA A PROPÓSITO, y no truena. self.contador += 1 sobre un atributo de clase.
class Contador:
    total = 0

    def __init__(self):
        self.total += 1          # parece incrementar el de la clase


for _ in range(5):
    Contador()

print("Contador.total:", Contador.total, "<- se quedó en cero")
print("Cada objeto se llevó el suyo:", vars(Contador()))
"""),

md("""
Cinco objetos creados y el contador de la clase sigue en cero.

`self.total += 1` se expande a `self.total = self.total + 1`. La lectura de la derecha encuentra el
cero de la clase; la asignación de la izquierda **siempre** escribe en la instancia. Es exactamente la
regla de alcance del repaso 3, la de que asignar dentro de una función crea una variable local,
trasladada del alcance de una función al de un objeto.

Con la lista del carrito eso no pasaba porque `append` no asigna: modifica el objeto que ya estaba, y
ese objeto era el de la clase. **Los mutables se comparten y los inmutables se copian sin querer**, y
las dos mitades de esa frase duelen en momentos distintos.
"""),

md("""
---
## Cuatro errores de esta sesión

**Olvidar `self` en la definición.** `TypeError: takes 0 positional arguments but 1 was given`. El
objeto se pasa solo, así que la firma tiene que recibirlo.

**Declarar el atributo fuera de `__init__`.** Queda pegado a la clase y todos los objetos comparten la
misma lista o el mismo contador. La corrección es una línea dentro del constructor.

**Llamar al método sin paréntesis.** `p.dibujar` imprime la referencia. `p.dibujar()` lo ejecuta. Con
`@property` en la misma clase, hay que tener claro cuál es cuál.

**Constructor que hace demasiado.** Si `__init__` abre archivos o consulta la red, el objeto falla
antes de existir y no hay nada que inspeccionar cuando falla.
"""),

code("""
# FALLA A PROPÓSITO. Un constructor que hace trabajo de verdad.
class ReporteRoto:
    def __init__(self, ruta):
        self.ruta = ruta
        with open(ruta) as f:        # el objeto depende de que esto salga bien
            self.contenido = f.read()


try:
    reporte = ReporteRoto("no_existe.csv")
except FileNotFoundError as e:
    print("FileNotFoundError:", e.filename)

print()
print("¿Existe la variable reporte?", "reporte" in dir())


class Reporte:
    def __init__(self, ruta):
        self.ruta = ruta
        self.contenido = None        # el objeto nace válido y vacío

    def cargar(self):
        with open(self.ruta) as f:
            self.contenido = f.read()
        return self


reporte = Reporte("no_existe.csv")
print("El objeto sí existe:", vars(reporte))
try:
    reporte.cargar()
except FileNotFoundError:
    print("La carga falló, pero el objeto se puede inspeccionar:", reporte.ruta)
"""),

md("""
En la primera versión la excepción ocurrió a media construcción, así que no quedó ningún objeto que
mirar: ni siquiera se sabe qué ruta se intentó, porque la variable nunca llegó a asignarse.

En la segunda, el constructor solo guarda datos y el trabajo va en un método aparte. Cuando la carga
falla, el objeto está ahí, con su ruta, listo para reintentar o para aparecer en un mensaje de error
útil.

**Un constructor recibe lo indispensable y deja el objeto listo para usarse.** Nada más.
"""),

md("""
---
# Ejercicios

El laboratorio de esta semana es modelar una biblioteca. Los ejercicios construyen hacia eso.

Las soluciones están hasta abajo del cuaderno.

### Ejercicio 1 · La clase más pequeña

Escribe una clase `Libro` con título y autor, y un método `describir` que los imprima. Crea tres
libros y descríbelos.

Después imprime `vars` de los tres y di qué tienen en común y qué no.

### Ejercicio 2 · El `self` que falta

Escribe a propósito un método sin `self`, llámalo y atrapa el `TypeError`. Después llama al mismo
método por la clase, pasando el objeto a mano, y explica en un comentario por qué esa forma sí
funciona.

### Ejercicio 3 · El atributo fantasma

Crea un objeto y asígnale un atributo con el nombre mal escrito. Demuestra con `vars` que el objeto
quedó con un dato de más y que el que querías cambiar sigue igual.

Escribe en un comentario cómo lo detectarías en un programa de mil líneas.

### Ejercicio 4 · La propiedad que no envejece

Escribe `Circulo` con un radio y dos propiedades, `area` y `perimetro`. Cambia el radio y comprueba
que las dos se actualizan.

Después escribe `CirculoRoto` que guarde el área como atributo normal y demuestra que se queda vieja.

### Ejercicio 5 · La lista compartida

Escribe `Grupo` con una lista de alumnos declarada en el cuerpo de la clase. Crea dos grupos, agrega
un alumno a uno, y muestra qué ve el otro.

Después arréglala y demuestra con `is` que ahora son dos listas distintas.

### Ejercicio 6 · El contador que no cuenta

Escribe una clase con un atributo de clase `total` que intente incrementarse con `self.total += 1`.
Crea cinco objetos y muestra que el total sigue en cero.

Arréglalo y explica en un comentario por qué la lista del ejercicio 5 sí se compartía y el entero no.

### Ejercicio 7 · Préstamo

Escribe `Prestamo` con título, día de préstamo y una constante de clase con el plazo máximo. Agrega un
método `vencido(dia_actual)`.

Pruébalo con tres préstamos y dos fechas distintas, incluyendo el día exacto del vencimiento.

### Ejercicio 8 · El constructor honesto

Escribe una clase que necesite leer un archivo. Hazla primero con la lectura dentro de `__init__` y
demuestra que un archivo faltante te deja sin objeto. Después sepárala en un método `cargar`.

### Ejercicio 9 · El laboratorio

Escribe las clases `Libro` y `Prestamo` de modo que el sistema pueda decir si un préstamo ya venció.

Máximo tres atributos por clase, sin librerías externas, un método público por clase. Entrega un
archivo con las dos clases y tres objetos de prueba impresos en consola.

El criterio es que los nombres se entiendan sin leer el cuerpo de los métodos.
"""),

md("""
---
## Tres ideas para llevarse

**La clase describe, el objeto recuerda.** Una definición en el código, tantos estados independientes
como instancias crees. Los métodos viven una sola vez y `__func__ is` lo demuestra.

**Lo que va en `__init__` es de cada objeto.** Lo que se declara en el cuerpo de la clase se comparte,
casi siempre sin querer. Es el tercer disfraz del mismo mecanismo que ya viste en los repasos 3 y 4.

**Una propiedad es un método disfrazado.** Se lee como dato y se calcula al vuelo, así que nunca queda
desactualizada. No aparece en `vars` porque no se guarda en ninguna parte.

La semana 4 sigue con lo que hoy quedó a medias: los modificadores de acceso, el `@setter` que
completa a `@property`, y los miembros estáticos, que son primos del `total_creados` de este cuaderno.

### Un método de depuración para el laboratorio

Explica tu código en voz alta, línea por línea, a alguien que no puede ayudarte. Se llama **rubber
duck debugging** y funciona porque verbalizar obliga a revisar las suposiciones que al leer se saltan
solas. Úsalo cuando lleves más de diez minutos sin una hipótesis nueva sobre el error.
"""),

md("""
---
# Soluciones

### Ejercicio 1

```python
class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def describir(self):
        print(f"{self.titulo}, de {self.autor}")


libros = [
    Libro("El Aleph", "Borges"),
    Libro("Pedro Páramo", "Rulfo"),
    Libro("La tregua", "Benedetti"),
]

for libro in libros:
    libro.describir()

print()
for libro in libros:
    print(vars(libro))

# Los tres tienen las mismas dos llaves, porque salieron del mismo constructor.
# Ninguno comparte un valor con otro, porque cada self.titulo = titulo corrió
# en su propia llamada. La clase da la forma; el objeto pone el contenido.
```

### Ejercicio 2

```python
class Ejemplo:
    def __init__(self, valor):
        self.valor = valor

    def mostrar():
        print("nunca llego")


e = Ejemplo(7)

try:
    e.mostrar()
except TypeError as error:
    print("TypeError:", error)

# Por la clase, pasando el objeto a mano:
try:
    Ejemplo.mostrar(e)
except TypeError as error:
    print("TypeError:", error)

Ejemplo.mostrar()          # sin objeto, esta sí corre

# e.mostrar() se convierte en Ejemplo.mostrar(e), así que llega un argumento a
# una función que no acepta ninguno. Llamarla por la clase sin argumentos
# funciona porque nadie inserta el objeto: es una función normal que vive
# dentro de una clase.
```

### Ejercicio 3

```python
class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio


p = Producto("café", 45.0)
p.preico = 39.0            # el typo

print("Precio:", p.precio)
print("Estado:", vars(p))
print("Atributos:", len(vars(p)))

# En mil líneas lo detectaría por el síntoma, no por el error: el descuento se
# aplica y el total no baja. Para atraparlo antes, imprimir vars() del objeto
# justo después de la asignación, o usar __slots__, que hace que Python
# rechace cualquier atributo que no esté declarado.
```

### Ejercicio 4

```python
import math


class Circulo:
    def __init__(self, radio):
        self.radio = radio

    @property
    def area(self):
        return math.pi * self.radio ** 2

    @property
    def perimetro(self):
        return 2 * math.pi * self.radio


class CirculoRoto:
    def __init__(self, radio):
        self.radio = radio
        self.area = math.pi * radio ** 2


c = Circulo(1)
print(f"radio 1 -> área {c.area:.4f}  perímetro {c.perimetro:.4f}")
c.radio = 3
print(f"radio 3 -> área {c.area:.4f}  perímetro {c.perimetro:.4f}")

print()
roto = CirculoRoto(1)
roto.radio = 3
print(f"radio {roto.radio} -> área reportada {roto.area:.4f}")
print(f"          área verdadera  {math.pi * roto.radio ** 2:.4f}")
```

El círculo roto reporta el área de radio 1 con radio 3. Ningún error, un número que se ve
perfectamente razonable, y una diferencia de nueve veces.

### Ejercicio 5

```python
class GrupoCompartido:
    alumnos = []

    def __init__(self, clave):
        self.clave = clave

    def inscribir(self, nombre):
        self.alumnos.append(nombre)


uno = GrupoCompartido("COM102-01")
dos = GrupoCompartido("COM102-02")
uno.inscribir("Ana")

print("Grupo 1:", uno.alumnos)
print("Grupo 2:", dos.alumnos, "<- sin haber inscrito a nadie")
print("¿la misma lista?", uno.alumnos is dos.alumnos)

print()


class Grupo:
    def __init__(self, clave):
        self.clave = clave
        self.alumnos = []

    def inscribir(self, nombre):
        self.alumnos.append(nombre)


uno = Grupo("COM102-01")
dos = Grupo("COM102-02")
uno.inscribir("Ana")

print("Grupo 1:", uno.alumnos)
print("Grupo 2:", dos.alumnos)
print("¿la misma lista?", uno.alumnos is dos.alumnos)
```

### Ejercicio 6

```python
class ContadorRoto:
    total = 0

    def __init__(self):
        self.total += 1


for _ in range(5):
    ContadorRoto()
print("Roto:", ContadorRoto.total)


class Contador:
    total = 0

    def __init__(self):
        Contador.total += 1


for _ in range(5):
    Contador()
print("Bueno:", Contador.total)

# La lista se compartía porque append no asigna: modifica el objeto que ya
# estaba, y ese objeto era el de la clase. El entero es inmutable, así que
# sumarle uno construye un entero nuevo y la asignación tiene que escribirlo en
# alguna parte. Escribe en la instancia, siempre. Por eso el mutable se
# comparte sin querer y el inmutable se copia sin querer.
```

### Ejercicio 7

```python
class Prestamo:
    DIAS_MAXIMOS = 14

    def __init__(self, titulo, dia_prestamo):
        self.titulo = titulo
        self.dia_prestamo = dia_prestamo

    def vencido(self, dia_actual):
        return dia_actual - self.dia_prestamo > Prestamo.DIAS_MAXIMOS


prestamos = [
    Prestamo("El Aleph", 1),
    Prestamo("Pedro Páramo", 5),
    Prestamo("La tregua", 12),
]

for dia in [15, 20]:
    print(f"Al día {dia}:")
    for p in prestamos:
        print(f"  {p.titulo:<15}prestado el {p.dia_prestamo:>2}  vencido: {p.vencido(dia)}")
    print()

# El día exacto del vencimiento: prestado el 1, plazo 14, se vence el 15.
uno = Prestamo("Prueba", 1)
print("día 15:", uno.vencido(15), "· día 16:", uno.vencido(16))
```

Con `>` el día 15 todavía no está vencido y el 16 sí. Con `>=` se vencería un día antes. La frontera la
decide el reglamento de la biblioteca, no la comodidad del código, y por eso hay que probarla con el
valor exacto.

### Ejercicio 8

```python
class ConfiguracionRota:
    def __init__(self, ruta):
        self.ruta = ruta
        with open(ruta) as f:
            self.lineas = f.readlines()


try:
    cfg = ConfiguracionRota("falta.txt")
except FileNotFoundError:
    print("No quedó objeto que inspeccionar. Ni siquiera se sabe qué ruta era.")


class Configuracion:
    def __init__(self, ruta):
        self.ruta = ruta
        self.lineas = []

    def cargar(self):
        with open(self.ruta) as f:
            self.lineas = f.readlines()
        return self


cfg = Configuracion("falta.txt")
try:
    cfg.cargar()
except FileNotFoundError:
    print(f"Falló la carga de {cfg.ruta}, y el objeto sigue disponible.")
    print("Estado:", vars(cfg))
```

### Ejercicio 9

```python
class Libro:
    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn

    def ficha(self):
        return f"{self.titulo} · {self.autor} · ISBN {self.isbn}"


class Prestamo:
    DIAS_MAXIMOS = 14

    def __init__(self, libro, socio, dia_prestamo):
        self.libro = libro
        self.socio = socio
        self.dia_prestamo = dia_prestamo

    def vencido(self, dia_actual):
        return dia_actual - self.dia_prestamo > Prestamo.DIAS_MAXIMOS


catalogo = [
    Libro("El Aleph", "Borges", "978-84-206-3311-0"),
    Libro("Pedro Páramo", "Rulfo", "978-968-16-7729-7"),
    Libro("La tregua", "Benedetti", "978-84-206-3350-9"),
]

prestamos = [
    Prestamo(catalogo[0], "Ana", 1),
    Prestamo(catalogo[1], "Luis", 5),
    Prestamo(catalogo[2], "Carla", 12),
]

HOY = 20
for p in prestamos:
    estado = "VENCIDO" if p.vencido(HOY) else "en tiempo"
    print(f"{p.socio:<7}{p.libro.ficha():<48}{estado}")
```

Tres decisiones que vale la pena defender.

`Prestamo` guarda el objeto `Libro` completo y no el título, así que no hay dos lugares donde el
título pueda diferir. Es la lección de la semana 2 aplicada dentro de una clase.

`DIAS_MAXIMOS` es un atributo de clase porque es una regla de la biblioteca y no de cada préstamo. Si
mañana la política cambia, se cambia una vez.

`ficha` devuelve en lugar de imprimir, y eso permite que el ciclo de arriba la acomode en una columna.
Es la lección del repaso 3, y es también lo que va a permitir que en la semana 8 ese mismo texto salga
de `__str__`.
"""),

]

write(OUT / "es" / "w03.ipynb", es)
print("wrote", OUT / "es" / "w03.ipynb")
