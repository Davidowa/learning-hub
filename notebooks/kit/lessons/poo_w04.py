"""notebooks/programacion-orientada-a-objetos/es/w04.ipynb

Source deck: ppts/python/programacion-orientada-a-objetos/es/w04.es.yaml
Source code:  docs/en/courses/python-course/02 - POO/6th Module/Code019.py
              docs/en/courses/python-course/02 - POO/6th Module/Code022.py

Dos errores reales de las fuentes, citados como trampa y nunca como si
corrieran:

  Code019.py línea 146 mete self.__say_age() dentro de un f-string. El método
  imprime y devuelve None, así que la salida sale en desorden y termina en
  "and None". El comentario de la línea 159 afirma otra cosa. No lanza nada.

  Code022.py línea 62 llama a Person.get_species() sobre la segunda de las
  cuatro definiciones de Person del archivo, que trae el método pero no el
  atributo species. AttributeError, y el archivo se detiene ahí.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from nbkit import md, code, write, REPO

OUT = REPO / "notebooks" / "programacion-orientada-a-objetos"

es = [

md("""
# Programación Orientada a Objetos · Semana 04
## Tema 2 · Elementos básicos

**COM102 · Facultad de Ingeniería · Profesor David Escobar-Castillejos**

Quién puede tocar qué dentro de un objeto, y las tres piezas que deciden cómo nace: modificadores de
acceso, funciones de acceso y constructores.

La semana pasada quedaron dos cosas a medias. `@property` apareció solo de lectura, y prometí que
`@setter` la completaba. `total_creados` apareció como un contador que había que escribir sobre la
clase, y prometí que los miembros estáticos eran su tema. Las dos se pagan hoy.

Al terminar vas a poder:

1. Elegir el nivel de acceso de cada miembro y decir quién lo hace cumplir en cada caso.
2. Escribir un getter y un setter que validen, y explicar por qué validar en el constructor no basta.
3. Convertirlos en una propiedad sin que cambie una sola línea del código que ya usaba la clase.
4. Separar lo que pertenece a la clase de lo que pertenece a cada objeto.
5. Escribir un constructor alternativo con `@classmethod` y saber cuándo `cls` no se puede sustituir
   por el nombre de la clase.

### Cómo se usa este cuaderno

Ejecuta las celdas en orden con **Shift + Enter**. Doce fallan a propósito y llevan un comentario que
lo dice.

Siete de las doce **no lanzan ninguna excepción**. Dos de las doce no las inventé: salieron del código
del curso, del archivo `Code019.py` y del `Code022.py` del módulo 6. Una de esas dos es de las que no
truenan, y es la peor del cuaderno. Las dos están señaladas cuando aparecen.
"""),

md("""
---
# Bloque 1 · Modificadores de acceso

Python no tiene la palabra `private`. Tiene una convención y un truco de renombrado, y conviene saber
cuál es cuál antes de confiar en ninguna de las dos.

En Java o en C# el compilador impone el nivel de acceso: si escribes desde fuera un campo privado, el
programa no compila. En Python el intérprete casi nunca se opone. Lo que hay es un acuerdo entre
quienes leen el código, más un renombrado que estorba lo suficiente para que nadie lo haga sin querer.

Empezamos con la clase del módulo 6, tal como está en el repositorio.
"""),

code("""
class Persona:
    def __init__(self, nombre: str, edad: int) -> None:
        self.__nombre = nombre       # privado: dos guiones bajos
        self.edad = edad             # público: la edad cambia con los años

    def hablar(self) -> None:
        print(f"Hola, me llamo {self.__nombre}")


persona = Persona("Ana", 20)
persona.hablar()

print("Edad:", persona.edad)
persona.edad = 21
print("Edad después:", persona.edad)
"""),

md("""
La edad se lee y se escribe desde fuera sin ninguna ceremonia, porque así se declaró. El nombre no.

La pregunta que importa no es cuál de los dos está bien, es cuál de las dos decisiones puedes
defender. La edad cambia todos los años y quien use la clase tiene que poder cambiarla. El nombre
casi nunca cambia y, si lo hiciera, no querrías que fuera con una asignación suelta a media función.

## Qué se puede leer desde fuera, medido
"""),

code("""
class Cuenta:
    def __init__(self, titular, banco, saldo):
        self.titular = titular       # público
        self._banco = banco          # protegido por convención
        self.__saldo = saldo         # privado por renombrado


cuenta = Cuenta("Ana", "Bancomer", 1500)

nombres = ["titular", "_banco", "__saldo"]
legibles = 0
for nombre in nombres:
    if hasattr(cuenta, nombre):
        legibles += 1
        print(f"  cuenta.{nombre:<9} -> {getattr(cuenta, nombre)}")
    else:
        print(f"  cuenta.{nombre:<9} -> no existe con ese nombre")

print()
print(f"{legibles} de {len(nombres)} se leen con el nombre escrito en la clase")
print("Lo que el objeto guarda de verdad:", list(vars(cuenta)))
print("Con el nombre real, el tercero también:", cuenta._Cuenta__saldo)
"""),

md("""
Dos de tres. El guion bajo simple no detuvo nada.

El único de los tres prefijos que cambia el comportamiento del intérprete es el doble. Con él, Python
reescribe `__saldo` como `_Cuenta__saldo` en el momento de compilar el cuerpo de la clase. Dentro de
los métodos la traducción es automática y por eso `self.__saldo` funciona; desde fuera hay que
escribir el nombre largo, y ese es todo el obstáculo.

`_banco` no cambió de nombre. Se lee, se escribe y no protesta nadie. Lo que dice el guion bajo es
"esto es interno, no construyas nada encima", y quien lo ignore no va a recibir un error: va a recibir
un programa que se rompe el día que cambies la parte interna.
"""),

code("""
# FALLA A PROPÓSITO. Con el nombre corto, el privado no existe.
try:
    print(cuenta.__saldo)
except AttributeError as e:
    print("AttributeError:", e)

print()
print("hasattr con el nombre corto:", hasattr(cuenta, "__saldo"))
print("hasattr con el nombre real: ", hasattr(cuenta, "_Cuenta__saldo"))
"""),

code("""
# FALLA A PROPÓSITO, y no truena. El guion bajo simple es un acuerdo, no un candado.
print("Banco antes: ", cuenta._banco)

cuenta._banco = "otro banco cualquiera"      # nadie se opone

print("Banco después:", cuenta._banco)
print()
print("Estado del objeto:", vars(cuenta))
print("Atributos:", len(vars(cuenta)))
"""),

md("""
Se escribió, se guardó, y el objeto quedó igual de largo que antes.

Esta celda es la razón por la que el guion bajo simple aparece en la tabla de vocabulario y no en la
lista de mecanismos. Sirve para hablar con otro programador. No sirve para impedir nada.

Compáralo con la celda anterior: ahí sí hubo un `AttributeError`, y con eso te enteras en el momento.
Aquí no hay síntoma.

## Los métodos también se cierran
"""),

code("""
class PersonaCompleta:
    def __init__(self, nombre: str, edad: int) -> None:
        self.__nombre = nombre
        self.edad = edad

    def hablar(self) -> None:
        print(f"Hola, me llamo {self.__nombre}")
        self.__decir_edad()

    def __decir_edad(self) -> None:
        print(f"y tengo {self.edad} años")


ana = PersonaCompleta("Ana", 20)
ana.hablar()

print()
print("Métodos y atributos propios de la clase:")
print("  ", [n for n in vars(PersonaCompleta) if not n.startswith("__")])
"""),

md("""
`__decir_edad` no tiene sentido fuera de `hablar`. No es un servicio que la clase ofrezca, es un
pedazo de `hablar` con nombre propio, y cerrarlo dice exactamente eso.

Fíjate en el diccionario de la clase: el método aparece como `_PersonaCompleta__decir_edad`. El
renombrado es el mismo que el de los atributos, porque es la misma regla aplicada a cualquier nombre
con dos guiones bajos al principio dentro del cuerpo de una clase.
"""),

code("""
# FALLA A PROPÓSITO. Llamar al método privado desde fuera.
try:
    ana.__decir_edad()
except AttributeError as e:
    print("AttributeError:", e)

print()
print("Con el nombre real sí corre:")
ana._PersonaCompleta__decir_edad()
"""),

md("""
El mensaje dice `'PersonaCompleta' object has no attribute '__decir_edad'`, y no dice nada de
permisos. Para el intérprete ese método no existe con ese nombre, y punto.

Eso también explica por qué el renombrado no es seguridad. La segunda línea lo llamó sin ningún
problema. Lo que evita es que alguien construya su programa encima de un método interno **sin darse
cuenta**, que es un accidente mucho más común que el sabotaje.

## La trampa del archivo del curso

`02 - POO/6th Module/Code019.py` cierra con esta clase. La escribo tal como está ahí, y el comentario
de la línea 159 del archivo dice que imprime `Hi, my name is John and I am 20 years old`.

Córrela antes de creerle.
"""),

code("""
# FALLA A PROPÓSITO, y no truena. Esta viene del archivo del curso, línea 146.
class PersonaCharlatana:
    def __init__(self, nombre: str, edad: int) -> None:
        self.__nombre = nombre
        self.edad = edad

    def hablar(self) -> None:
        print(f"Hola, me llamo {self.__nombre} y {self.__decir_edad()}")

    def __decir_edad(self) -> None:
        print(f"tengo {self.edad} años")


charlatana = PersonaCharlatana("Ana", 20)
charlatana.hablar()

print()
print("Lo que devuelve __decir_edad:", charlatana._PersonaCharlatana__decir_edad())
"""),

md("""
Una sola llamada a `hablar()` y salieron dos renglones, en el orden equivocado, terminando en `None`.

Lo que pasó cabe en una frase: **para armar el texto del f-string, Python tuvo que llamar primero a
`__decir_edad`**. Ese método imprime por su cuenta, así que su renglón salió antes que el de afuera. Y
como no tiene `return`, devolvió `None`, que es lo que se pegó al final del texto.

Es la lección del repaso 3 dentro de una clase: **imprimir no es devolver**. Una función que imprime
sirve para verla; una que devuelve sirve para usarla. Meter la primera donde hacía falta la segunda no
lanza ninguna excepción, porque `None` se convierte a texto sin protestar.

La versión de la diapositiva de esta semana ya está corregida: llama a `self.__decir_edad()` en su
propia línea, después del `print`. Compara las dos y vas a ver que la diferencia es una sola llave.

Las dos correcciones posibles, para tenerlas juntas.
"""),

code("""
class PersonaQueDevuelve:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.edad = edad

    def hablar(self):
        print(f"Hola, me llamo {self.__nombre} y {self.__decir_edad()}")

    def __decir_edad(self):
        return f"tengo {self.edad} años"      # devuelve, no imprime


class PersonaQueImprime:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.edad = edad

    def hablar(self):
        print(f"Hola, me llamo {self.__nombre}")
        self.__decir_edad()                   # fuera del f-string

    def __decir_edad(self):
        print(f"y tengo {self.edad} años")


PersonaQueDevuelve("Ana", 20).hablar()
print()
PersonaQueImprime("Ana", 20).hablar()
"""),

md("""
La primera es la que yo defendería. Un método que devuelve texto se puede imprimir, se puede meter en
otro texto, se puede guardar en un archivo y se puede comparar en una prueba. Uno que imprime solo
sirve para lo primero.

En la semana 8 esa decisión vuelve con nombre propio. `__str__` **devuelve** una cadena, y por eso
`print(objeto)` funciona sin que la clase sepa nada de la consola.

## Los cuatro prefijos, y quién los hace cumplir

| Prefijo | Qué significa | Lo hace cumplir | Ejemplo |
|---|---|---|---|
| Ninguno | Público, parte del contrato | Nadie | `self.edad` |
| `_uno` | Interno, no lo uses | La convención | `self._banco` |
| `__dos` | Privado, se renombra | El intérprete | `self.__saldo` |
| `__ambos__` | Método mágico de Python | El lenguaje | `__init__` |

La regla práctica: **empieza con todo público**. Cierra un atributo el día que descubras que desde
fuera se puede dejar el objeto en un estado imposible, no el día que te lo pida un libro. Un objeto
con doce atributos privados y doce parejas de getters y setters está exactamente igual de abierto que
uno con doce atributos públicos, y tiene tres veces más código.
"""),

md("""
---
# Bloque 2 · Funciones de acceso

Un atributo cerrado no sirve de nada si no hay manera de leerlo. Aquí está la manera larga, y después
la que no se nota.

## Getter y setter, la versión con paréntesis
"""),

code("""
class ProductoLargo:
    def __init__(self, precio: float) -> None:
        self.set_precio(precio)          # el constructor pasa por el setter

    def get_precio(self) -> float:
        return self.__precio

    def set_precio(self, valor: float) -> None:
        if valor < 0:
            raise ValueError("El precio no puede ser negativo")
        self.__precio = valor


cafe = ProductoLargo(45)
print("Precio:", cafe.get_precio())

cafe.set_precio(52)
print("Precio nuevo:", cafe.get_precio())
print()
print("Estado del objeto:", vars(cafe))
"""),

md("""
El setter existe por una sola razón: **un atributo público no puede rechazar un valor**. Ese es el
punto entero y no hay otro.

Fíjate en la primera línea del constructor. No dice `self.__precio = precio`, dice
`self.set_precio(precio)`. Con eso la validación corre desde el primer valor que entra al objeto, y no
hay forma de construir un producto con precio negativo.
"""),

code("""
# FALLA A PROPÓSITO. El setter rechaza y el constructor hereda ese rechazo.
try:
    ProductoLargo(-5)
except ValueError as e:
    print("ValueError:", e)

try:
    cafe.set_precio(-1)
except ValueError as e:
    print("ValueError:", e)

print()
print("El precio no se movió:", cafe.get_precio())
"""),

md("""
Las dos rutas de entrada quedaron cerradas con el mismo `if`, escrito una sola vez.

Ahora la versión que se ve razonable y no lo es.
"""),

code("""
# FALLA A PROPÓSITO, y no truena. Validar en el constructor y dejar el atributo público.
class ProductoIngenuo:
    def __init__(self, precio):
        if precio < 0:
            raise ValueError("El precio no puede ser negativo")
        self.precio = precio


te = ProductoIngenuo(38)
print("Precio al construir:", te.precio)

te.precio = -1000              # la validación quedó atrás, en el constructor

print("Precio después:     ", te.precio)
print()
print("¿El objeto es válido?", te.precio >= 0)
print("¿Alguien se enteró?  No. No hubo excepción ni mensaje.")
"""),

md("""
El objeto nació correcto y quedó inválido en la siguiente línea.

Validar solo en el constructor protege el primer instante de vida del objeto y ninguno de los
siguientes. Es la trampa que la diapositiva llama Error 02, y es la más común de las cuatro porque se
siente como si ya hubieras hecho el trabajo.

La pregunta que la desarma: **¿cuántas maneras hay de cambiar este atributo?** Si la respuesta es más
de una, la validación tiene que estar donde se cambia, no donde se crea.

## La misma validación, sin paréntesis
"""),

code("""
class Producto:
    def __init__(self, precio: float) -> None:
        self.precio = precio             # esto llama al setter de abajo

    @property
    def precio(self) -> float:
        return self.__precio

    @precio.setter
    def precio(self, valor: float) -> None:
        if valor < 0:
            raise ValueError("El precio no puede ser negativo")
        self.__precio = valor


pan = Producto(28)
print("Precio:", pan.precio)             # sin paréntesis

pan.precio = 31
print("Precio nuevo:", pan.precio)

print()
print("Estado del objeto:", vars(pan))
"""),

md("""
La clase valida igual que la anterior y quien la usa escribe `pan.precio` en lugar de
`pan.get_precio()`.

Tres detalles que valen la pena.

`self.precio = precio` dentro del constructor **no crea un atributo**. Como `precio` es una propiedad
declarada en la clase, la asignación entra por el setter, con su `if` y todo.

El método se escribe dos veces con el mismo nombre, y está bien. `@precio.setter` toma la propiedad
que ya existe y le agrega la mitad de escritura, así que el nombre tiene que repetirse exacto. Si te
equivocas en una letra, terminas con dos propiedades distintas y una de ellas sin getter.

El diccionario del objeto sigue mostrando `_Producto__precio`. La propiedad vive en la clase, el dato
vive en el objeto, y por eso `vars` enseña el nombre renombrado y no el bonito.

## Las dos versiones rechazan lo mismo, medido
"""),

code("""
CANDIDATOS = [10, 0, -1, 99.99, -0.01, 250, -1000]

def probar(clase, poner):
    aceptados, rechazados = [], []
    for valor in CANDIDATOS:
        try:
            objeto = clase(1)
            poner(objeto, valor)
            aceptados.append(valor)
        except ValueError:
            rechazados.append(valor)
    return aceptados, rechazados


largo = probar(ProductoLargo, lambda o, v: o.set_precio(v))
corto = probar(Producto, lambda o, v: setattr(o, "precio", v))

print("Con getters:  ", len(largo[1]), "rechazados de", len(CANDIDATOS), "->", largo[1])
print("Con propiedad:", len(corto[1]), "rechazados de", len(CANDIDATOS), "->", corto[1])
print()
print("¿Las dos rechazan exactamente lo mismo?", largo[1] == corto[1])
print("¿Y aceptan exactamente lo mismo?      ", largo[0] == corto[0])
"""),

md("""
Tres de siete, la misma terna, en las dos implementaciones.

Eso es lo que hace valiosa a la propiedad, y no es que sea más corta. La validación no se movió ni un
milímetro; lo único que cambió es la sintaxis de quien llama. Si mañana decides cerrar un atributo que
llevaba dos años público, con `@property` el código que ya usaba `objeto.precio` sigue compilando y
sigue corriendo. Con getters, alguien tiene que ir a cambiar cada línea.

## El error que la diapositiva marca en rojo
"""),

code("""
# FALLA A PROPÓSITO. El setter que se llama a sí mismo.
import sys


class ProductoRecursivo:
    def __init__(self, precio):
        self.precio = precio

    @property
    def precio(self):
        return self.__precio

    @precio.setter
    def precio(self, valor):
        if valor < 0:
            raise ValueError("El precio no puede ser negativo")
        self.precio = valor          # sin los dos guiones bajos


print("Límite de recursión de esta sesión:", sys.getrecursionlimit())
try:
    ProductoRecursivo(45)
except RecursionError as e:
    print("RecursionError:", str(e)[:60])
"""),

md("""
`self.precio = valor` dentro del setter vuelve a entrar al setter, que vuelve a entrar al setter.

La corrección es escribir `self.__precio = valor`, con los dos guiones bajos, porque ese sí es un
atributo normal y no pasa por la propiedad. La regla: **dentro de la propiedad se toca el atributo, no
la propiedad**.

Por lo menos este error truena, y truena fuerte. Los tres que siguen no.

## Encapsular sin encapsular nada
"""),

code("""
# FALLA A PROPÓSITO, y no truena. Getters y setters para todo, que no validan nada.
class Empleado:
    def __init__(self, nombre, salario, antiguedad):
        self.__nombre = nombre
        self.__salario = salario
        self.__antiguedad = antiguedad

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, v):
        self.__nombre = v

    def get_salario(self):
        return self.__salario

    def set_salario(self, v):
        self.__salario = v

    def get_antiguedad(self):
        return self.__antiguedad

    def set_antiguedad(self, v):
        self.__antiguedad = v


emp = Empleado("Ana", 42000, 36)
emp.set_salario(-8000)
emp.set_antiguedad(-14)

print("Salario:   ", emp.get_salario())
print("Antigüedad:", emp.get_antiguedad(), "meses")
print()
metodos = [n for n in vars(Empleado) if not n.startswith("__")]
print(f"{len(metodos)} métodos de acceso, {len([m for m in metodos if 'set' in m])} de escritura")
print("Validaciones en total: 0")
"""),

md("""
Un empleado con salario de menos ocho mil pesos y antigüedad negativa, escrito a través de la interfaz
oficial de la clase.

Seis métodos de acceso, cero validaciones, y el objeto está exactamente igual de abierto que si los
tres atributos fueran públicos. Lo único que se logró fue que ahora haya que escribir paréntesis.

**Un setter sin validación es un atributo público con más pasos.** Si el atributo acepta cualquier
cosa, déjalo público y ahórrate el ruido. Cierra el día que tengas una regla que defender, y escribe
la regla dentro del setter el mismo día.

## La propiedad que hace cosas a tus espaldas
"""),

code("""
# FALLA A PROPÓSITO, y no truena. Una propiedad con efecto secundario.
class Sensor:
    def __init__(self, temperatura):
        self.__temperatura = temperatura
        self.bitacora = []

    @property
    def temperatura(self):
        self.bitacora.append(self.__temperatura)     # escribe al leer
        return self.__temperatura


s = Sensor(21.5)

print(f"Lectura: {s.temperatura} grados")
if s.temperatura > 20:
    print("Por arriba del umbral")
print(f"Reporte final: {s.temperatura}")

print()
print("Renglones en la bitácora:", len(s.bitacora))
print("Bitácora:", s.bitacora)
"""),

md("""
Cuenta cuántas veces aparece `s.temperatura` en la celda de arriba. Tres. La bitácora también trae
tres renglones, y ni una sola de las tres menciones se ve como una escritura.

Aquí la bitácora es una lista en memoria y el daño es cero. Cambia la lista por un `INSERT` en la base
de datos o por una petición a un servidor y ya tienes un programa que hace tres viajes a la red porque
alguien puso una condición y un mensaje de depuración.

**Leer una propiedad tiene que verse gratis, porque se lee como un atributo.** Si detrás hay trabajo,
ponle paréntesis y llámalo método: los paréntesis son la señal de que ahí va a pasar algo.

## Cuatro maneras de encapsular sin encapsular nada

| | El error | Cómo se ve cuando muerde |
|---|---|---|
| 01 | Getter y setter para cada atributo | El objeto sigue abierto y hay el doble de código |
| 02 | Validar en el constructor y no en el setter | El objeto nace válido y se pudre en la línea siguiente |
| 03 | Confiar en el guion bajo simple | Alguien construyó encima de `_banco` y no te enteraste |
| 04 | Propiedades con efectos secundarios | Tres lecturas, tres escrituras en disco |

Las cuatro tienen algo en común y por eso van juntas: en las cuatro el código **parece** encapsulado.
"""),

md("""
---
# Bloque 3 · Constructores y miembros estáticos

Qué le toca hacer a `__init__`, y qué cosas pertenecen a la clase entera y no a cada objeto.

## Hasta dónde llega el constructor

La semana pasada lo dejamos en una frase: un constructor recibe lo indispensable y deja el objeto
listo para usarse. Con lo del bloque 2 se puede afinar.

**Le toca** recibir lo indispensable, validarlo, y dejarlo asignado sobre `self`, de preferencia
pasando por el setter para que la regla viva en un solo lugar.

**No le toca** abrir archivos, consultar la red ni preguntarle nada a una base de datos.

**La prueba** es una pregunta: ¿este constructor puede fallar por algo que no es culpa de quien lo
llamó? Si la respuesta es sí, eso que puede fallar va en otro método. Un precio negativo es culpa de
quien llamó. Un archivo que no está no lo es.

## Lo que pertenece a la clase

Aquí retomamos el archivo `Code022.py` del módulo 6, que se llama justamente "Class vs Instance
attributes".
"""),

code("""
class Persona:
    especie = "humano"               # atributo de clase

    def __init__(self, nombre: str, edad: int) -> None:
        self.nombre = nombre         # atributos de instancia
        self.edad = edad


juan = Persona("Juan", 36)
print(juan.nombre, juan.edad, juan.especie)
print("Desde la clase:", Persona.especie)

print()
print("vars(juan):        ", vars(juan))
print("¿especie está ahí?", "especie" in vars(juan))
"""),

md("""
`juan.especie` respondió `humano` y `especie` no está en el diccionario del objeto.

El mecanismo es el de la semana pasada, el del carrito de compras. Cuando pides un atributo, Python lo
busca primero en el objeto y, si no lo encuentra, sube a la clase. Aquí no lo encuentra, sube, y ahí
está.

La diferencia con el carrito es la que importa: **la especie sí es del concepto y no del objeto**.
Todas las personas son humanas, así que guardar la palabra ciento veinte veces sería desperdicio y
además permitiría que dos personas discreparan.

## Predice antes de correr

```python
class Persona:
    especie = "humano"

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad


juan = Persona("Juan", 36)
juan.especie = "alienígena"

print(juan.especie, Persona.especie)
```

- **A.** `alienígena alienígena`, porque asignar sobre el objeto cambia el de la clase.
- **B.** `alienígena humano`, porque la asignación crea un atributo en el objeto.
- **C.** `humano humano`, porque el atributo de clase no se puede pisar.
- **D.** Error, `especie` no está declarado en `__init__`.
"""),

code("""
juan.especie = "alienígena"

print("juan.especie:   ", juan.especie)
print("Persona.especie:", Persona.especie)
print()
print("vars(juan):", vars(juan))
print("Atributos del objeto:", len(vars(juan)), "<- eran 2")

otra = Persona("Ana", 20)
print()
print("Una persona nueva:", otra.especie)
"""),

md("""
La respuesta es **B**.

Asignar sobre la instancia nunca escribe en la clase. Lo que hace es poner un atributo encima, en el
diccionario del objeto, y a partir de ahí la búsqueda lo encuentra antes de subir. El de la clase
sigue intacto y cualquier persona nueva lo sigue leyendo.

Es la misma celda de la semana pasada donde `b.productos = []` "arreglaba" un carrito y dejaba rotos
todos los demás. Y es el mismo mecanismo que hace que `self.total += 1` no cuente: la lectura sube a
la clase, la escritura se queda en el objeto, siempre.

Ahora al revés.
"""),

code("""
# FALLA A PROPÓSITO, y no truena. Cambiar el atributo de clase con dos objetos vivos.
Persona.especie = "animal"

print("juan.especie:   ", juan.especie, "<- se quedó con el suyo")
print("otra.especie:   ", otra.especie, "<- siguió a la clase")
print("Persona.especie:", Persona.especie)
print()
print("¿Los dos objetos coinciden?", juan.especie == otra.especie)
"""),

md("""
Dos personas de la misma clase con especies distintas, y ningún error en el camino.

Reasignar un atributo de clase cambia lo que ven todos los objetos que **no** lo hayan pisado.
Los que sí lo pisaron se quedaron con su copia y ya no escuchan. El resultado es un estado que
depende del orden de las líneas y que, en un programa de verdad, depende del orden en que corrieron
dos funciones en archivos distintos.

Por eso la recomendación del archivo del curso es sensata: **los atributos de clase se usan como
constantes**. Un valor que nadie reasigna nunca no tiene este problema.

## La segunda trampa del código del curso

`Code022.py` define la clase `Person` cuatro veces, en las líneas 8, 44, 92 y 107. Es un archivo
didáctico y redefinir la clase es su manera de ir agregando piezas.

La segunda definición se queda con el método de clase y pierde el atributo. **El archivo no corre**:
se detiene en su línea 62 y las dos definiciones que siguen nunca se ejecutan. Esta celda reproduce
esa segunda definición tal cual.
"""),

code("""
# FALLA A PROPÓSITO. Esta viene del archivo del curso, líneas 44 a 62.
class PersonaSegunda:
    @classmethod
    def get_especie(cls):
        return cls.especie           # especie ya no está declarada aquí

    @classmethod
    def cero(cls):
        return cls("", 0)

    def __init__(self, nombre: str, edad: int) -> None:
        self.nombre = nombre
        self.edad = edad


alguien = PersonaSegunda("Juan", 36)

try:
    print(alguien.get_especie())
except AttributeError as e:
    print("AttributeError:", e)

print()
print("Lo que sí trae la clase:", [n for n in vars(PersonaSegunda) if not n.startswith("__")])
print("¿Tiene especie?", hasattr(PersonaSegunda, "especie"))
"""),

md("""
`type object 'PersonaSegunda' has no attribute 'especie'`.

`class Persona:` escrito por segunda vez no continúa la clase anterior, **construye un objeto clase
completamente nuevo** y vuelve a amarrar el nombre. Lo que no aparezca en el cuerpo nuevo no existe en
la clase nueva. El atributo `especie` se quedó en la primera, que a partir de esa línea ya no tiene
nombre y se va a la basura.

Es el mismo mecanismo de la función redefinida del repaso 3, subido un nivel. Ahí la segunda `def`
tapaba a la primera y las llamadas de en medio seguían funcionando porque estaban antes. Aquí la
segunda `class` tapa a la primera y la llamada de después ya no encuentra lo que buscaba.

Hay un segundo detalle en ese mismo archivo. El comentario de la línea 61 dice que la salida es
`<bound method Person.get_species of <class '__main__.Person'>>`, y esa es la salida de
`my_person.get_species` **sin paréntesis**. La línea 62 sí los lleva. El comentario describe una línea
que no está escrita, que es exactamente el error del método sin paréntesis de la semana pasada, esta
vez cometido en un comentario.

Dos maneras de dejarlo corriendo, y las dos dicen algo.
"""),

code("""
class PersonaConEspecie:
    especie = "humano"               # se vuelve a declarar en la clase nueva

    @classmethod
    def get_especie(cls):
        return cls.especie

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad


class PersonaHeredada(Persona):      # continúa la primera, no la reemplaza
    @classmethod
    def get_especie(cls):
        return cls.especie


print("Redeclarando:", PersonaConEspecie("Juan", 36).get_especie())
print("Heredando:   ", PersonaHeredada("Juan", 36).get_especie())
print()
print("La heredada lee el valor actual de la clase madre:", Persona.especie)
"""),

md("""
La segunda imprime `animal` y no `humano`, porque hace unas celdas reasignamos `Persona.especie` y la
clase hija lee el valor de hoy, no el de cuando se escribió.

Esa línea es un adelanto de la semana 7. Por ahora quédate con la forma: cuando quieras agregarle algo
a una clase que ya existe, no la vuelvas a escribir; extiéndela.

## `cls`, y por qué no es lo mismo que el nombre de la clase
"""),

code("""
# La clase censo.py de la diapositiva. Le pongo otro nombre a propósito, para no
# volver a hacerle a Persona lo que Code022.py le hizo hace tres celdas.
class PersonaCenso:
    especie = "humano"
    censo = 0

    def __init__(self, nombre: str, edad: int) -> None:
        self.nombre = nombre
        self.edad = edad
        PersonaCenso.censo += 1      # sobre la clase, a propósito

    @classmethod
    def anonima(cls) -> "PersonaCenso":
        return cls("Sin nombre", 0)

    @staticmethod
    def es_mayor(edad: int) -> bool:
        return edad >= 18            # no necesita ni el objeto ni la clase

    def saludar(self) -> None:
        print(f"Hola, soy {self.nombre}")


ana = PersonaCenso("Ana", 20)
nadie = PersonaCenso.anonima()

print("Censo:", PersonaCenso.censo)
nadie.saludar()
print()
print("¿20 es mayor de edad?", PersonaCenso.es_mayor(20))
print("¿15 es mayor de edad?", PersonaCenso.es_mayor(15))
print()
print("El método estático también se llama desde el objeto:", ana.es_mayor(ana.edad))
"""),

md("""
Tres tipos de método en la misma clase, y la diferencia está en el primer parámetro.

`saludar(self)` recibe el objeto. Necesita saber de quién está hablando.

`anonima(cls)` recibe la clase. No hay objeto todavía, porque su trabajo es construir uno. Por eso se
les dice **constructores alternativos** o métodos fábrica: cuando `__init__` solo puede tener una
firma y tú necesitas varias maneras de crear el objeto, cada una entra por su `@classmethod`.

`es_mayor(edad)` no recibe nada de nada. Es una función normal que vive dentro de la clase porque ahí
es donde alguien la va a buscar. `@staticmethod` es la manera de decir eso.

Y `PersonaCenso.censo += 1` va sobre la clase, escrito con el nombre completo. Con `self.censo += 1` cada
objeto se llevaría su propio contador en uno, que es el quiz de la semana pasada.
"""),

code("""
# FALLA A PROPÓSITO, y no truena. La fábrica que escribe el nombre de la clase en vez de cls.
class Vehiculo:
    def __init__(self, placas, ruedas):
        self.placas = placas
        self.ruedas = ruedas

    @classmethod
    def sin_placas(cls):
        return Vehiculo("PENDIENTE", 4)      # debería decir cls(...)


class Camion(Vehiculo):
    def __init__(self, placas, ruedas=6):
        super().__init__(placas, ruedas)


nuevo = Camion.sin_placas()

print("Pedimos un camión y salió un:", type(nuevo).__name__)
print("Ruedas:", nuevo.ruedas)
print("¿Es un Camion?", isinstance(nuevo, Camion))
print("¿Es un Vehiculo?", isinstance(nuevo, Vehiculo))
"""),

md("""
Pedimos un camión por la puerta de los camiones y salió un vehículo de cuatro ruedas.

`cls` es la clase **sobre la que se llamó el método**, no la clase donde está escrito. `Camion.sin_placas()`
le pasa `Camion`, así que `cls("PENDIENTE", 4)` habría construido un camión. Escribir el nombre a mano
congela la fábrica en la clase madre y todas las hijas heredan un método que no sirve para ellas.

Nada de esto lanza una excepción. El objeto existe, tiene placas, tiene ruedas, y `isinstance` contra
`Vehiculo` dice `True`. El síntoma aparece mucho después, el día que alguien llame a un método que solo
tienen los camiones.

Esta es la razón por la que `cls` existe teniendo el nombre de la clase a la mano, y la semana 7 la
retoma con la jerarquía completa.
"""),

md("""
---
## Cuatro errores de esta sesión

**Confiar en el guion bajo simple.** `_banco` se lee y se escribe desde fuera sin una sola protesta.
Es un acuerdo entre personas y solo funciona con quien lo conozca.

**Validar en el constructor y no en el setter.** El objeto nace correcto y queda inválido en la línea
siguiente. Si hay más de una manera de cambiar el atributo, la validación va donde se cambia.

**Escribir `self.precio` dentro del setter de `precio`.** La propiedad se llama a sí misma hasta el
`RecursionError`. Dentro de la propiedad se toca el atributo.

**Meter en un f-string un método que imprime.** Sale `None` pegado al texto y los renglones en
desorden. Imprimir no es devolver, y esa frase lleva tres semanas cobrando.
"""),

md("""
---
# Ejercicios

El laboratorio de esta semana es cerrar una cuenta bancaria, en parejas. Los ejercicios construyen
hacia eso.

Las soluciones están hasta abajo del cuaderno.

### Ejercicio 1 · Los tres prefijos

Escribe una clase `Alumno` con tres atributos, uno público, uno con guion bajo simple y uno con doble.
Desde fuera intenta leer los tres con el nombre que aparece en la clase y cuenta cuántos responden.

Después imprime `vars` del objeto y explica en un comentario por qué el tercero se ve distinto.

### Ejercicio 2 · El método que no sale de la clase

Agrega a `Alumno` un método privado que calcule algo intermedio, y un método público que lo use. Llama
al privado desde fuera, atrapa el `AttributeError`, y después llámalo con su nombre real.

Explica en un comentario qué te dice eso sobre el nivel de protección que ofrece el renombrado.

### Ejercicio 3 · Imprimir no es devolver

Escribe una clase con un método privado que **imprima** y úsalo dentro de un f-string. Enseña la salida
desordenada y el `None`.

Después escribe la versión que devuelve y compara las dos salidas en la misma celda.

### Ejercicio 4 · El setter que sirve

Escribe `Producto` con precio privado, `get_precio` y `set_precio`, y una validación que rechace los
negativos. Prueba siete precios, tres de ellos inválidos, y cuenta cuántos entraron.

El constructor tiene que pasar por el setter. Demuéstralo intentando construir un producto negativo.

### Ejercicio 5 · La misma clase con propiedad

Convierte el ejercicio 4 a `@property` y `@precio.setter`. Corre los mismos siete precios y comprueba
con una sola línea que rechaza exactamente los mismos.

Escribe en un comentario cuántas líneas del código que usa la clase tuviste que cambiar.

### Ejercicio 6 · La validación que llegó tarde

Escribe una clase que valide solo en el constructor y deje el atributo público. Constrúyela bien,
rómpela con una asignación, y muestra que el objeto quedó inválido sin ningún error.

Arréglala con una propiedad y repite exactamente las mismas dos líneas.

### Ejercicio 7 · Clase contra instancia

Escribe `Curso` con un atributo de clase `CLAVE_MATERIA` y dos de instancia. Crea tres cursos, pisa el
atributo de clase en uno solo, y después reasigna el de la clase.

Imprime lo que ve cada uno de los tres y explica en un comentario por qué no coinciden.

### Ejercicio 8 · El constructor alternativo

Agrega a `Curso` un `@classmethod` llamado `vacio` que construya un curso sin alumnos, escrito con
`cls`. Después escribe la versión con el nombre de la clase a mano, hereda de `Curso`, y muestra que
las dos fábricas devuelven tipos distintos.

### Ejercicio 9 · El laboratorio

Escribe la clase `Cuenta` con el titular público, el saldo privado y una propiedad de solo lectura que
lo exponga, más los métodos `depositar` y `retirar`.

`retirar` no puede dejar el saldo negativo, y `saldo` no lleva setter. Entrega un archivo con la clase
y cinco operaciones de prueba impresas en consola, de las cuales por lo menos dos tienen que ser
rechazadas.

El criterio es que sea imposible dejar la cuenta en un estado inválido desde fuera de la clase.
Pruébalo: intenta romperla y enseña el intento fallido.
"""),

md("""
---
## Tres ideas para llevarse

**Un guion bajo pide permiso, dos lo quitan.** El primero es un acuerdo entre personas y no lo hace
cumplir nadie. El segundo renombra el atributo dentro del intérprete, y eso evita accidentes, no
sabotajes.

**La propiedad es el setter que no se nota.** Valida igual que un método y se lee como un atributo, así
que el día que cierres un atributo público, ninguna línea de quien ya usaba la clase tiene que cambiar.

**Lo que se declara en la clase se comparte.** Constantes y contadores viven ahí; el estado de cada
objeto se asigna dentro de `__init__`. Es el cuarto disfraz del mismo mecanismo: la lista por omisión
del repaso 3, el alias del repaso 4, el carrito de la semana 3 y la especie de hoy.

La semana 5 sigue con métodos que aceptan varias formas de llamarse, con dónde vive cada clase cuando
el proyecto crece, y con el paso del enunciado al modelo. La semana 6 retoma el encapsulamiento en
serio, ya con la propiedad de hoy como herramienta.

### Cómo saber si encapsulaste algo

Una pregunta, aplicada a cada atributo cerrado: **¿qué estado imposible impide?** Si tienes la
respuesta, el candado está justificado. Si la respuesta es "ninguno, pero así se ve más profesional",
quítalo y déjalo público.
"""),

md("""
---
# Soluciones

### Ejercicio 1

```python
class Alumno:
    def __init__(self, nombre, grupo, promedio):
        self.nombre = nombre
        self._grupo = grupo
        self.__promedio = promedio


a = Alumno("Ana", "COM102-01", 9.2)

respondieron = 0
for nombre in ["nombre", "_grupo", "__promedio"]:
    if hasattr(a, nombre):
        respondieron += 1
        print(f"  a.{nombre:<12} -> {getattr(a, nombre)}")
    else:
        print(f"  a.{nombre:<12} -> no existe con ese nombre")

print()
print(f"{respondieron} de 3 respondieron")
print(vars(a))

# El tercero se ve como _Alumno__promedio porque Python le pegó el nombre de la
# clase al compilar el cuerpo. El dato está ahí completo; lo único que cambió es
# con qué nombre se pide. Los otros dos se guardaron tal cual se escribieron.
```

### Ejercicio 2

```python
class Alumno:
    def __init__(self, nombre, calificaciones):
        self.nombre = nombre
        self.calificaciones = calificaciones

    def boleta(self):
        print(f"{self.nombre}: promedio {self.__promedio():.2f}")

    def __promedio(self):
        return sum(self.calificaciones) / len(self.calificaciones)


a = Alumno("Ana", [8, 9, 10])
a.boleta()

try:
    a.__promedio()
except AttributeError as e:
    print("AttributeError:", e)

print("Con el nombre real:", a._Alumno__promedio())

# El renombrado no protege, estorba. Cualquiera que sepa la regla llega al
# método en un renglón. Lo que sí evita es que alguien lo llame sin saber que
# era interno, y por lo tanto que un cambio mío le rompa su código.
```

### Ejercicio 3

```python
class Reporte:
    def __init__(self, titulo, filas):
        self.titulo = titulo
        self.filas = filas

    def encabezado_roto(self):
        print(f"{self.titulo} ({self.__conteo()})")

    def __conteo(self):
        print(f"{len(self.filas)} filas")

    def encabezado(self):
        print(f"{self.titulo} ({self.__conteo_texto()})")

    def __conteo_texto(self):
        return f"{len(self.filas)} filas"


r = Reporte("Ventas", [1, 2, 3])

r.encabezado_roto()
print()
r.encabezado()

# La primera imprime "3 filas" y después "Ventas (None)". El método interno tuvo
# que correr para armar el texto, imprimió por su cuenta, y devolvió None.
# La segunda imprime "Ventas (3 filas)" en un solo renglón y en el orden que se
# lee en el código.
```

### Ejercicio 4

```python
class Producto:
    def __init__(self, precio):
        self.set_precio(precio)

    def get_precio(self):
        return self.__precio

    def set_precio(self, valor):
        if valor < 0:
            raise ValueError("El precio no puede ser negativo")
        self.__precio = valor


CANDIDATOS = [10, 0, -1, 99.99, -0.01, 250, -1000]

p = Producto(1)
aceptados = 0
for valor in CANDIDATOS:
    try:
        p.set_precio(valor)
        aceptados += 1
    except ValueError:
        pass

print(f"{aceptados} de {len(CANDIDATOS)} entraron")
print("Precio final:", p.get_precio())

try:
    Producto(-5)
except ValueError as e:
    print("El constructor también rechaza:", e)
```

### Ejercicio 5

```python
class ProductoPropiedad:
    def __init__(self, precio):
        self.precio = precio

    @property
    def precio(self):
        return self.__precio

    @precio.setter
    def precio(self, valor):
        if valor < 0:
            raise ValueError("El precio no puede ser negativo")
        self.__precio = valor


def rechazados(poner):
    fuera = []
    for valor in CANDIDATOS:
        try:
            poner(valor)
        except ValueError:
            fuera.append(valor)
    return fuera


viejo = Producto(1)
nuevo = ProductoPropiedad(1)

a = rechazados(viejo.set_precio)
b = rechazados(lambda v: setattr(nuevo, "precio", v))

print("Getters:  ", a)
print("Propiedad:", b)
print("¿Idénticos?", a == b)

# Cero líneas del código que lee el precio. p.precio ya funcionaba cuando el
# atributo era público y sigue funcionando ahora que pasa por el getter. Ese es
# el argumento entero a favor de las propiedades.
```

### Ejercicio 6

```python
class CursoIngenuo:
    def __init__(self, cupo):
        if cupo <= 0:
            raise ValueError("El cupo tiene que ser positivo")
        self.cupo = cupo


c = CursoIngenuo(30)
c.cupo = -5
print("Cupo:", c.cupo, "· ¿válido?", c.cupo > 0)


class Curso:
    def __init__(self, cupo):
        self.cupo = cupo

    @property
    def cupo(self):
        return self.__cupo

    @cupo.setter
    def cupo(self, valor):
        if valor <= 0:
            raise ValueError("El cupo tiene que ser positivo")
        self.__cupo = valor


c = Curso(30)
try:
    c.cupo = -5
except ValueError as e:
    print("ValueError:", e)
print("Cupo:", c.cupo, "· ¿válido?", c.cupo > 0)
```

### Ejercicio 7

```python
class Curso:
    CLAVE_MATERIA = "COM102"

    def __init__(self, grupo, cupo):
        self.grupo = grupo
        self.cupo = cupo


uno = Curso("01", 30)
dos = Curso("02", 28)
tres = Curso("03", 25)

dos.CLAVE_MATERIA = "COM102-B"        # solo este se la pisa
Curso.CLAVE_MATERIA = "COM103"        # y ahora cambia la de la clase

for curso in [uno, dos, tres]:
    print(f"Grupo {curso.grupo}: {curso.CLAVE_MATERIA}")

print("En la clase:", Curso.CLAVE_MATERIA)
print("vars(dos):", vars(dos))

# El grupo 02 no coincide porque su asignación creó un atributo de instancia, y
# la búsqueda lo encuentra antes de subir a la clase. Los otros dos no tienen
# nada propio, así que suben y leen el valor de hoy. La reasignación de la clase
# alcanza a quien no se haya independizado y a nadie más.
```

### Ejercicio 8

```python
class Curso:
    def __init__(self, grupo, alumnos):
        self.grupo = grupo
        self.alumnos = alumnos

    @classmethod
    def vacio(cls, grupo):
        return cls(grupo, [])

    @classmethod
    def vacio_congelado(cls, grupo):
        return Curso(grupo, [])       # el nombre a mano


class Taller(Curso):
    pass


bien = Taller.vacio("01")
mal = Taller.vacio_congelado("01")

print("Con cls: ", type(bien).__name__)
print("Con Curso:", type(mal).__name__)
print("¿El segundo es un Taller?", isinstance(mal, Taller))

# cls es la clase sobre la que se llamó el método. Taller.vacio le pasa Taller y
# la fábrica construye un taller. La otra versión construye siempre un Curso, así
# que todo lo que Taller agregue queda fuera y nadie recibe un error.
```

### Ejercicio 9

```python
class Cuenta:
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self.__saldo = 0
        if saldo_inicial:
            self.depositar(saldo_inicial)

    @property
    def saldo(self):
        return self.__saldo           # solo lectura: no hay setter

    def depositar(self, monto):
        if monto <= 0:
            raise ValueError("El depósito tiene que ser positivo")
        self.__saldo += monto
        return self.__saldo

    def retirar(self, monto):
        if monto <= 0:
            raise ValueError("El retiro tiene que ser positivo")
        if monto > self.__saldo:
            raise ValueError(f"Saldo insuficiente: hay {self.__saldo}")
        self.__saldo -= monto
        return self.__saldo


cuenta = Cuenta("Ana", 1000)

OPERACIONES = [
    ("depositar", 500),
    ("retirar", 200),
    ("retirar", 5000),      # más de lo que hay
    ("depositar", -50),     # negativo
    ("retirar", 1300),
]

rechazadas = 0
for accion, monto in OPERACIONES:
    try:
        saldo = getattr(cuenta, accion)(monto)
        print(f"  {accion:<10}{monto:>7}  ->  saldo {saldo}")
    except ValueError as e:
        rechazadas += 1
        print(f"  {accion:<10}{monto:>7}  ->  RECHAZADA: {e}")

print()
print(f"{rechazadas} de {len(OPERACIONES)} rechazadas")
print("Saldo final:", cuenta.saldo)

# El intento de romperla desde fuera:
try:
    cuenta.saldo = 1000000
except AttributeError as e:
    print("AttributeError:", e)

cuenta.__saldo = 1000000              # esto no truena, y tampoco sirve
print("Saldo después del intento:", cuenta.saldo)
print("Basura que quedó en el objeto:", vars(cuenta))
```

Las dos últimas líneas son la parte que vale del ejercicio.

`cuenta.saldo = 1000000` truena, porque `saldo` es una propiedad sin setter y Python se niega.

`cuenta.__saldo = 1000000` no truena. Crea un atributo nuevo llamado `__saldo`, distinto de
`_Cuenta__saldo`, que nadie lee jamás. El saldo real no se movió. Es el atributo fantasma de la semana
pasada, con la coartada de que parece que sabes lo que estás haciendo.

Las dos maneras de atacar la cuenta desde fuera fallaron, una ruidosa y otra callada. Eso es lo que
significa que el estado inválido sea inalcanzable.
"""),

]

write(OUT / "es" / "w04.ipynb", es)
print("wrote", OUT / "es" / "w04.ipynb")
