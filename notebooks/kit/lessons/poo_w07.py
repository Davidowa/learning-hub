"""notebooks/programacion-orientada-a-objetos/es/w07.ipynb

Source deck: ppts/python/programacion-orientada-a-objetos/es/w07.es.yaml
Source code:  docs/en/courses/python-course/02 - POO/6th Module/Code020.py
                  (Animal, Mammal, Fish; Person y Student; el guion bajo simple)
              docs/en/courses/python-course/02 - POO/6th Module/Code021.py
                  (multinivel con la gallina, herencia múltiple y el orden)
              docs/en/courses/python-course/02 - POO/6th Module/Code026.py
                  (la jerarquía de Stream)

Los tres archivos corren completos, comprobado.

Esta semana paga la promesa de la semana 3: "una clase hija define un atributo
con el mismo nombre y pisa el de la madre sin enterarse". Está en el bloque 2.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from nbkit import md, code, write, REPO

OUT = REPO / "notebooks" / "programacion-orientada-a-objetos"

es = [

md("""
# Programación Orientada a Objetos · Semana 07
## Tema 3 · Propiedades fundamentales

**COM102 · Facultad de Ingeniería · Profesor David Escobar-Castillejos**

Qué recibe una clase de su padre, hasta dónde conviene que crezca el árbol, y el guion bajo que le abre
la puerta a las hijas.

La semana pasada terminamos diciendo que la composición se prefiere. Eso no significa que la herencia
esté mal: significa que compromete más, y que hay que saber a qué. Este cuaderno enseña la sintaxis en
diez minutos y dedica el resto a los cuatro lugares donde se rompe.

Al terminar vas a poder:

1. Escribir una subclase, encadenar constructores con `super`, y decir qué pasa si se te olvida.
2. Elegir entre un guion bajo y dos, ahora sabiendo cuál de los dos llega a las hijas.
3. Explicar por qué dos niveles alcanzan casi siempre y qué se rompe a partir del tercero.
4. Leer un `__mro__` y predecir qué método corre con dos padres.
5. Aplicar la prueba de "es un" y reescribir con composición la relación que no la pase.

### Cómo se usa este cuaderno

Ejecuta las celdas en orden con **Shift + Enter**. Once fallan a propósito y llevan un comentario que
lo dice.

Siete de las once **no lanzan ninguna excepción**. Entre ellas está la que la semana 3 dejó anunciada:
una clase hija que define un atributo con el mismo nombre que el de su madre y lo pisa sin que nadie se
entere.
"""),

md("""
---
# Bloque 1 · Herencia

Una clase que empieza donde otra terminó. La parte fácil es la sintaxis.
"""),

code("""
class Animal:
    def __init__(self, nombre: str) -> None:
        self.nombre = nombre

    def comer(self) -> None:
        print(f"{self.nombre} come")


class Pez(Animal):
    def __init__(self, nombre: str) -> None:
        super().__init__(nombre)

    def nadar(self) -> None:
        print(f"{self.nombre} nada")


tiburon = Pez("tiburón")
tiburon.comer()
tiburon.nadar()

print()
print("¿Un pez es un animal?", isinstance(tiburon, Animal))
print("¿Pez hereda de object?", issubclass(Pez, object))
print("Estado del objeto:", vars(tiburon))
"""),

md("""
`Pez` tiene `nombre` y `comer` sin escribirlos. Eso es la herencia entera en dos líneas.

`super().__init__(nombre)` corre el constructor del padre. Sin esa línea, `self.nombre` nunca se asigna,
y `comer` truena la primera vez que alguien lo llame.

`nadar` vive solo en `Pez`. El padre no lo conoce y no debería: si mañana `Animal` aprende a nadar,
todos los perros y las gallinas del programa aprenden también.

## Lo que se hereda, contado
"""),

code("""
propios_animal = {n for n in dir(Animal) if not n.startswith("__")}
propios_pez = {n for n in dir(Pez) if not n.startswith("__")}

print("Miembros de Animal:", sorted(propios_animal))
print("Miembros de Pez:   ", sorted(propios_pez))
print()
print("Heredados sin escribirlos:", sorted(propios_pez & propios_animal))
print("Escritos en Pez:          ", sorted(propios_pez - propios_animal))
print()
print("Escritos en el cuerpo de Pez:",
      sorted(n for n in vars(Pez) if not n.startswith("__")))
print("Cadena de búsqueda:", [c.__name__ for c in Pez.__mro__])
"""),

md("""
`dir(Pez)` incluye `comer` aunque `vars(Pez)` no. La diferencia entre las dos es exactamente la
herencia: `vars` enseña lo que la clase escribió, `dir` enseña lo que la clase alcanza.

La última línea es la cadena de búsqueda, el **MRO**, que quiere decir orden de resolución de métodos.
Cuando pides `tiburon.comer`, Python recorre esa lista de izquierda a derecha y se queda con la primera
que tenga el nombre. Vale la pena acostumbrarse a leerlo, porque en el bloque 3 es lo que decide qué
método corre.

## Predice antes de correr

```python
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre


class Perro(Animal):
    def __init__(self, nombre, raza):
        self.raza = raza


p = Perro("Bobby", "pastor")
print(p.nombre)
```

- **A.** `Bobby`, porque el padre guardó el nombre.
- **B.** `AttributeError`, el objeto no tiene nombre.
- **C.** `None`, porque `nombre` quedó sin asignar.
- **D.** `TypeError`, faltan argumentos en `Perro`.
"""),

code("""
# FALLA A PROPÓSITO. El constructor del padre que nunca corrió.
class Perro(Animal):
    def __init__(self, nombre, raza):
        self.raza = raza          # falta super().__init__(nombre)


bobby = Perro("Bobby", "pastor")

print("Estado del objeto:", vars(bobby))
print("Atributos:", len(vars(bobby)), "<- esperábamos 2")
print()
try:
    print(bobby.nombre)
except AttributeError as e:
    print("AttributeError:", e)

print()
try:
    bobby.comer()
except AttributeError as e:
    print("Y comer tampoco:", e)
"""),

md("""
La respuesta es **B**.

Definir `__init__` en la subclase **reemplaza** al del padre, no lo agrega. Es el mismo mecanismo del
segundo `def` de la semana pasada, aplicado a lo largo de la herencia: `Perro.__init__` tapa a
`Animal.__init__`, y si nadie lo llama, el del padre no corre nunca.

Fíjate en el orden en que se descubre. El objeto se construyó sin protestar, con un solo atributo. El
error aparece más tarde, en la primera línea que lea `nombre`, que puede estar en otro archivo.

Ese es el error 03 de la diapositiva y es el más común de toda la unidad.
"""),

code("""
class Perro(Animal):
    def __init__(self, nombre, raza):
        super().__init__(nombre)      # primero lo del padre
        self.raza = raza              # después lo propio

    def ladrar(self):
        print(f"{self.nombre} ({self.raza}) ladra")


bobby = Perro("Bobby", "pastor")
bobby.comer()
bobby.ladrar()

print()
print("Estado del objeto:", vars(bobby))
print("Atributos:", len(vars(bobby)))
"""),

md("""
Dos atributos, uno de cada constructor.

El orden importa y tiene una razón: `super().__init__` va primero porque lo propio puede depender de lo
heredado, y casi nunca al revés.

## El constructor del padre que llama a un método de la hija
"""),

code("""
# FALLA A PROPÓSITO. El padre usa algo que la hija todavía no asignó.
class Empleado:
    def __init__(self, nombre):
        self.nombre = nombre
        print("  ficha:", self.ficha())      # el padre llama al método

    def ficha(self):
        return self.nombre


class Vendedor(Empleado):
    def __init__(self, nombre, zona):
        super().__init__(nombre)             # aquí corre ficha()
        self.zona = zona                     # y zona todavía no existe

    def ficha(self):
        return f"{self.nombre} ({self.zona})"


print("Un empleado normal:")
Empleado("Ana")

print()
print("Un vendedor:")
try:
    Vendedor("Luis", "Norte")
except AttributeError as e:
    print("  AttributeError:", e)
"""),

md("""
El padre llamó a `ficha`, y la que corrió fue la de la hija, porque el objeto ya era un `Vendedor` desde
antes de que empezara el primer constructor.

Ese es el punto que cuesta ver: **el tipo del objeto se decide al construirlo, no a medio construirlo**.
Desde la primera línea de `Empleado.__init__`, `self` ya es un `Vendedor`, así que cualquier método que
el padre llame va a ser la versión sobrescrita, trabajando sobre un objeto a medio armar.

La regla que sale de aquí: **un constructor no llama métodos que se puedan sobrescribir**. Si el padre
necesita el resultado, que lo reciba como parámetro o que el trabajo se haga después, en un método
aparte, como en la semana 3 con el constructor que abría archivos.

## `type` no es `isinstance`
"""),

code("""
# FALLA A PROPÓSITO, y no truena. Un filtro escrito con type en lugar de isinstance.
animales = [Animal("genérico"), Pez("tiburón"), Perro("Bobby", "pastor")]

con_type = [a for a in animales if type(a) == Animal]
con_isinstance = [a for a in animales if isinstance(a, Animal)]

print("Con type == Animal:      ", len(con_type), "de", len(animales))
print("Con isinstance(a, Animal):", len(con_isinstance), "de", len(animales))
print()
for a in animales:
    igual = "sí" if type(a) is Animal else "no"
    instancia = "sí" if isinstance(a, Animal) else "no"
    print(f"  {type(a).__name__:<8}type: {igual:<4}isinstance: {instancia}")
"""),

md("""
Uno contra tres. El filtro con `type` dejó fuera al pez y al perro, que son animales.

`type(x) == Animal` pregunta si el objeto es **exactamente** de esa clase. `isinstance(x, Animal)`
pregunta si es de esa clase o de cualquiera que herede de ella, que es casi siempre lo que uno quiere
decir.

No truena, no avisa, y produce un conteo equivocado. En un programa con jerarquías, un `type ==` es casi
siempre un error esperando a que alguien agregue la primera subclase.
"""),

md("""
---
# Bloque 2 · El modificador protegido

Un guion bajo abre la puerta a las hijas. Dos la cierran incluso para ellas, y eso sorprende a casi
todos.

Aquí, por fin, el guion bajo simple tiene un uso técnico y no solo un acuerdo. Sigue sin impedir nada
desde fuera, pero adentro de una jerarquía dice algo preciso: **esto es mío y de mis hijas**.
"""),

code("""
class Persona:
    def __init__(self, nombre: str) -> None:
        self._nombre = nombre           # protegido: para mí y para mis hijas
        self.__clave = "secreta"        # privado: solo para mí

    def presentarse(self):
        print(f"Soy {self._nombre} y mi clave empieza con {self.__clave[0]}")


class Alumno(Persona):
    def saludar(self):
        print(f"Hola, soy {self._nombre}")      # el protegido sí baja


ana = Alumno("Ana")
ana.presentarse()
ana.saludar()

print()
print("Estado del objeto:", vars(ana))
print("Desde fuera, el protegido también:", ana._nombre)
"""),

code("""
# FALLA A PROPÓSITO. El privado del padre no baja a la hija con ese nombre.
class AlumnoCurioso(Persona):
    def espiar(self):
        return self.__clave             # se traduce a self._AlumnoCurioso__clave


curioso = AlumnoCurioso("Luis")

try:
    curioso.espiar()
except AttributeError as e:
    print("AttributeError:", e)

print()
print("Lo que el objeto sí guarda:", list(vars(curioso)))
print("Con el nombre de la madre:", curioso._Persona__clave)
"""),

md("""
El mensaje dice `'AlumnoCurioso' object has no attribute '_AlumnoCurioso__clave'`, y ahí está la
explicación completa.

El renombrado usa el nombre de **la clase donde se escribió la línea**, no el del objeto. `self.__clave`
dentro de `Persona` se traduce a `_Persona__clave`; la misma expresión escrita dentro de `AlumnoCurioso`
se traduce a `_AlumnoCurioso__clave`, que nunca existió.

| Miembro | En la clase | En la subclase | Desde fuera |
|---|---|---|---|
| `edad` | Sí | Sí | Sí |
| `_nombre` | Sí | Sí | Sí, aunque no deberías |
| `__clave` | Sí | No | No, con ese nombre |
| `comer()` | Sí | Sí | Sí |
| `__decir()` | Sí | No | No, con ese nombre |

## La colisión que la semana 3 dejó anunciada

En la semana 3 escribí que el renombrado evita "que una clase hija defina un atributo con el mismo
nombre y pise el de la madre sin enterarse". Aquí está esa celda.
"""),

code("""
# FALLA A PROPÓSITO, y no truena. La hija pisa el atributo de la madre.
class Sesion:
    def __init__(self, usuario):
        self._usuario = usuario
        self._estado = "abierta"        # el estado de la sesión

    def cerrar(self):
        self._estado = "cerrada"

    def esta_abierta(self):
        return self._estado == "abierta"


class SesionDeExamen(Sesion):
    def __init__(self, usuario, examen):
        super().__init__(usuario)
        self.examen = examen
        self._estado = "sin empezar"    # el estado del examen, mismo nombre

    def entregar(self):
        self._estado = "entregado"


s = SesionDeExamen("Ana", "COM102-P1")
print("Estado del objeto:", vars(s))
print("Atributos:", len(vars(s)), "<- son dos estados en una sola llave")
print()
print("¿La sesión está abierta?", s.esta_abierta(), "<- acaba de crearse")
s.entregar()
print("Después de entregar el examen:")
print("  _estado:", s._estado)
print("  ¿la sesión está abierta?", s.esta_abierta())
s.cerrar()
print("Después de cerrar la sesión, el examen dice:", s._estado)
"""),

md("""
Una sola llave `_estado` para dos ideas distintas, y las dos se pisan por turnos.

La sesión nació cerrada porque el constructor de la hija sobrescribió el valor del padre. Entregar el
examen no cerró la sesión y sin embargo la dejó "no abierta". Cerrar la sesión borró el estado del
examen.

Nadie escribió un error. Las dos clases son correctas por separado, y la colisión ocurrió porque las dos
eligieron la misma palabra para cosas distintas. Cuanto más grande el árbol, más probable es que pase,
y el síntoma nunca señala a la herencia.

Con dos guiones bajos esto no ocurre.
"""),

code("""
class SesionSegura:
    def __init__(self, usuario):
        self.__estado = "abierta"

    def cerrar(self):
        self.__estado = "cerrada"

    def esta_abierta(self):
        return self.__estado == "abierta"


class ExamenSeguro(SesionSegura):
    def __init__(self, usuario, examen):
        super().__init__(usuario)
        self.examen = examen
        self.__estado = "sin empezar"       # el mismo nombre, otra clase

    def entregar(self):
        self.__estado = "entregado"

    def estado_examen(self):
        return self.__estado


e = ExamenSeguro("Ana", "COM102-P1")
print("Estado del objeto:", vars(e))
print("Atributos:", len(vars(e)), "<- dos estados, dos llaves")
print()
print("¿La sesión está abierta?", e.esta_abierta())
e.entregar()
print("Examen:", e.estado_examen(), "· sesión abierta:", e.esta_abierta())
e.cerrar()
print("Examen:", e.estado_examen(), "· sesión abierta:", e.esta_abierta())
"""),

md("""
Dos llaves, `_SesionSegura__estado` y `_ExamenSeguro__estado`, y cada clase manda en la suya.

**Ese es el uso real del doble guion bajo**, y no la seguridad. Sirve para que una jerarquía larga no
se pise los nombres, que es un accidente mucho más frecuente que un ataque.

La regla que sale de las dos celdas:

- **Un guion bajo** cuando quieras que las hijas lo usen. Es parte del contrato hacia abajo.
- **Dos guiones bajos** cuando el dato sea asunto tuyo y de nadie más, ni siquiera de tus hijas.
- Nada cuando sea parte del contrato hacia afuera.
"""),

md("""
---
# Bloque 3 · Jerarquía de clases

Cada nivel nuevo es un archivo más que abrir para entender una sola llamada. El árbol se paga en
lecturas.

El archivo `Code026.py` del módulo 6 arma la jerarquía sana: un padre con lo común y tres hermanos con
lo que cambia.
"""),

code("""
class ErrorDeOperacion(Exception):
    pass


class Stream:
    def __init__(self) -> None:
        self.abierto = False

    def abrir(self) -> None:
        if self.abierto:
            raise ErrorDeOperacion("el flujo ya estaba abierto")
        self.abierto = True

    def cerrar(self) -> None:
        if not self.abierto:
            raise ErrorDeOperacion("el flujo ya estaba cerrado")
        self.abierto = False


class StreamDeArchivo(Stream):
    def leer(self):
        print("  leyendo de un archivo")


class StreamDeRed(Stream):
    def leer(self):
        print("  leyendo de la red")


class StreamDeMemoria(Stream):
    def leer(self):
        print("  leyendo de la memoria")


for stream in [StreamDeArchivo(), StreamDeRed(), StreamDeMemoria()]:
    print(type(stream).__name__)
    stream.abrir()
    stream.leer()
    stream.cerrar()

print()
print("Niveles del árbol:", len(StreamDeArchivo.__mro__) - 1,
      "->", [c.__name__ for c in StreamDeArchivo.__mro__])
"""),

md("""
Tres hermanos colgando del mismo padre, dos niveles contando `object`, y para entender cualquier llamada
hay que leer dos clases.

`abrir` y `cerrar` se escribieron una vez. `leer` se escribió tres veces porque de verdad cambia entre
un hijo y otro, que es exactamente lo que justifica que sean tres clases.

**La regla de la jerarquía sana: los hermanos cuelgan del mismo padre, ninguno cuelga de otro
hermano.**

## El atributo de clase, ahora repartido entre primos
"""),

code("""
# FALLA A PROPÓSITO, y no truena. Una lista declarada en el padre.
class StreamConBitacora(Stream):
    bitacora = []                    # en el cuerpo de la clase

    def registrar(self, mensaje):
        self.bitacora.append(f"{type(self).__name__}: {mensaje}")


class DeArchivo(StreamConBitacora):
    pass


class DeRed(StreamConBitacora):
    pass


archivo = DeArchivo()
red = DeRed()

archivo.registrar("abrí un archivo")
red.registrar("abrí un socket")

print("Bitácora de archivo:", archivo.bitacora)
print("Bitácora de red:    ", red.bitacora)
print()
print("¿Es la misma lista?", archivo.bitacora is red.bitacora
      is StreamConBitacora.bitacora)
print("vars(archivo):", vars(archivo))
print("Objetos con bitácora propia:",
      sum(1 for o in [archivo, red] if "bitacora" in vars(o)), "de 2")
"""),

md("""
Dos clases distintas, dos objetos distintos, una sola lista.

Es el carrito de la semana 3, ahora repartido entre toda una rama del árbol. La búsqueda de atributos
sube por el `__mro__` hasta encontrar `bitacora`, la encuentra en `StreamConBitacora`, y la devuelve; el
`append` modifica esa única lista.

Lo que la herencia agrega al problema es alcance. En la semana 3 se compartían los objetos de una clase;
aquí se comparten los de todas las clases de la rama, incluidas las que alguien escriba el año que
viene. La corrección es la misma de siempre: `self.bitacora = []` dentro de `__init__`, y en una
jerarquía eso significa dentro del `__init__` que sí corre, encadenado con `super`.

## Lo que pasa a partir del tercer nivel
"""),

code("""
# FALLA A PROPÓSITO, y no truena. La cadena que le enseña a volar a una gallina.
class Ave(Animal):
    def __init__(self, nombre):
        super().__init__(nombre)

    def volar(self):
        print(f"{self.nombre} vuela")


class Gallina(Ave):
    def __init__(self, nombre):
        super().__init__(nombre)


gallina = Gallina("Lola")
gallina.comer()
gallina.volar()          # nadie lo escribió y ahí está

print()
print("Cadena de búsqueda:", [c.__name__ for c in Gallina.__mro__])
print("Niveles hasta object:", len(Gallina.__mro__) - 1)
print("¿La gallina puede volar?", hasattr(gallina, "volar"))

dueno = next(c for c in Gallina.__mro__ if "volar" in vars(c))
print("volar está escrito en:", dueno.__name__,
      "· escalón de la cadena:", Gallina.__mro__.index(dueno))
"""),

md("""
Una gallina que vuela, sin una sola línea que lo diga.

`Gallina` no escribió `volar`. Lo recibió de `Ave`, que a su vez lo escribió porque casi todas las aves
vuelan. La cadena hizo verdadera una afirmación que nadie quiso hacer.

Y fíjate en el costo de lectura. Para entender qué hace `gallina.volar()` hay que subir hasta `Ave`,
saltándose `Gallina`. Con un nivel más, hay que subir dos. Ese es el error 01 de la diapositiva: **para
entender una llamada hay que abrir cuatro archivos, y en el camino la gallina aprende a volar.**

La corrección no es agregarle a `Gallina` un `volar` que imprima "no puedo". Es que `Ave` no tenía por
qué prometer que vuela: volar es de algunas aves, no de las aves. Ahí va una clase `Volador` aparte, o
mejor, composición.

## Dos padres, y el orden que decide en silencio
"""),

code("""
class PersonaSaludo:
    def saludar(self):
        print("Hola, soy una persona")


class Empleado:
    def saludar(self):
        print("Hola, soy un empleado")


class Gerente(Empleado, PersonaSaludo):
    pass


class GerenteAlReves(PersonaSaludo, Empleado):
    pass


Gerente().saludar()
GerenteAlReves().saludar()

print()
print("Gerente.__mro__:        ", [c.__name__ for c in Gerente.__mro__])
print("GerenteAlReves.__mro__: ", [c.__name__ for c in GerenteAlReves.__mro__])
"""),

md("""
Dos clases idénticas salvo el orden de los paréntesis, y dos comportamientos distintos.

Python busca el método recorriendo el `__mro__` de izquierda a derecha y se queda con el primero que lo
tenga. `Empleado` va primero en la primera clase, así que gana su `saludar`.

Ahora la parte incómoda.
"""),

code("""
# FALLA A PROPÓSITO, y no truena. Alguien reordena los padres en un refactor.
class Gerente(PersonaSaludo, Empleado):       # antes decía (Empleado, PersonaSaludo)
    pass


print("El mismo código de siempre:")
Gerente().saludar()
print()
print("Ni un error, ni una advertencia, ni una línea de diferencia en quien llama.")
print("Lo único que cambió está en la declaración de la clase:")
print("  ", [c.__name__ for c in Gerente.__mro__])
"""),

md("""
El programa cambió de comportamiento y nadie tocó una línea de quien lo usa.

Es el error 04 de la diapositiva, y el riesgo real no es que alguien reordene los padres a propósito.
Es que el orden nunca se lee: `class Gerente(Empleado, Persona)` parece una lista de etiquetas, no una
decisión de precedencia, y quien la edite seis meses después no va a saber que estaba decidiendo algo.

Cuando dos padres traen el mismo método, la señal es que uno de los dos no era un padre. Con
composición el mismo caso se escribe sin ambigüedad, porque la llamada dice cuál es cuál:
`self.empleado.saludar()` o `self.persona.saludar()`.

## Y `super()` tampoco llama a los dos
"""),

code("""
# FALLA A PROPÓSITO. super() con dos padres solo alcanza al primero.
class Trabajador:
    def __init__(self, numero):
        self.numero = numero


class Humano:
    def __init__(self, nombre):
        self.nombre = nombre


class GerenteConSuper(Trabajador, Humano):
    def __init__(self, numero, nombre):
        super().__init__(numero)          # solo corre Trabajador.__init__


g = GerenteConSuper(1, "Ana")
print("Estado del objeto:", vars(g))
print("Atributos:", len(vars(g)), "<- esperábamos 2")

try:
    print(g.nombre)
except AttributeError as e:
    print("AttributeError:", e)

print()


class GerenteExplicito(Trabajador, Humano):
    def __init__(self, numero, nombre):
        Trabajador.__init__(self, numero)
        Humano.__init__(self, nombre)


g = GerenteExplicito(1, "Ana")
print("Llamando a los dos a mano:", vars(g))
"""),

md("""
`super()` no significa "los padres". Significa **el siguiente de la cadena**, y la cadena aquí es
`GerenteConSuper -> Trabajador -> Humano -> object`. Como `Trabajador.__init__` no llama a `super()`, la
cadena se corta ahí y `Humano.__init__` nunca corre.

La salida que usa `Code021.py` es llamar a los dos constructores por nombre, que funciona y se lee. La
otra salida es que **todas** las clases de la cadena llamen a `super().__init__()`, lo que se llama
herencia cooperativa y obliga a que las firmas encajen.

Las dos son trabajo extra que la composición no pide. Es una razón más de las que hacen que la herencia
múltiple casi nunca valga la pena.

## Cuatro formas de abusar de la herencia

| | El error | Cómo se ve |
|---|---|---|
| 01 | Un árbol de cuatro niveles | Cuatro archivos para entender una llamada, y la gallina vuela |
| 02 | Heredar para no repetir código | La relación era de uso, y un parámetro hacía el mismo trabajo |
| 03 | Olvidar `super().__init__` | El objeto nace incompleto y revienta en la primera línea que lo use |
| 04 | Dos padres con el mismo método | El orden de la lista decide en silencio |
"""),

md("""
---
# Bloque 4 · Heredar o componer

La prueba cabe en una frase que se dice en voz alta: **la hija es un caso particular del padre**.

Si suena verdadera sin explicaciones, la herencia se sostiene. Si hay que agregarle un "bueno, más o
menos", lo que había era composición.

| Frase | ¿Se sostiene? | Qué era |
|---|---|---|
| Un pez es un animal | Sí | Herencia |
| Un archivo abierto es un flujo de datos | Sí | Herencia |
| Un carrito es una lista | No | El carrito **tiene** una lista |
| Un pedido es un cliente | No | El pedido **tiene** un cliente |
| Una gallina es un ave que vuela | Con peros | El "que vuela" sobraba |

## La frase que suena verdadera y aun así falla

Un cuadrado es un rectángulo. En geometría eso es cierto sin ningún pero, y la herencia se rompe de
todas formas.
"""),

code("""
# FALLA A PROPÓSITO, y no truena. Un cuadrado que hereda de un rectángulo.
class Rectangulo:
    def __init__(self, ancho, alto):
        self._ancho = ancho
        self._alto = alto

    @property
    def ancho(self):
        return self._ancho

    @ancho.setter
    def ancho(self, valor):
        self._ancho = valor

    @property
    def alto(self):
        return self._alto

    @alto.setter
    def alto(self, valor):
        self._alto = valor

    @property
    def area(self):
        return self._ancho * self._alto


class Cuadrado(Rectangulo):
    def __init__(self, lado):
        super().__init__(lado, lado)

    @Rectangulo.ancho.setter
    def ancho(self, valor):
        self._ancho = valor
        self._alto = valor          # un cuadrado tiene que seguir siendo cuadrado


def estirar_y_medir(rect):
    \"\"\"Función escrita para rectángulos, mucho antes de que existiera Cuadrado.\"\"\"
    rect.ancho = 10
    return rect.area


print("Con un rectángulo de 3x4:", estirar_y_medir(Rectangulo(3, 4)), "-> 10 * 4")
print("Con un cuadrado de lado 4:", estirar_y_medir(Cuadrado(4)), "-> 10 * ¿4?")
print()
print("¿Un cuadrado es un rectángulo?", issubclass(Cuadrado, Rectangulo))
print("¿La función sabe con cuál está trabajando? No.")
"""),

md("""
Cuarenta contra cien, con la misma función y sin un solo error.

`estirar_y_medir` se escribió con una promesa en la cabeza: cambiar el ancho no cambia el alto. Es una
promesa que `Rectangulo` cumple y que `Cuadrado` no puede cumplir sin dejar de ser un cuadrado.

Aquí está lo incómodo. La frase de "es un" es verdadera, la geometría está de tu lado, y aun así la
subclase rompe el código escrito para la madre. La prueba de "es un" es necesaria y no es suficiente.

La versión completa se llama **principio de sustitución de Liskov** y dice algo más exigente:
cualquier lugar donde funcione la madre tiene que seguir funcionando si le pasas una hija. Cuando la
hija le quita libertad a la madre, ya no sustituye.

La salida: si el cuadrado no puede prometer lo mismo, no es una subclase del rectángulo mutable. Que
sean dos clases sueltas, o que el rectángulo sea inmutable y `con_ancho(10)` devuelva uno nuevo, que es
la lección del `__add__` de la semana 5.

## La misma relación, escrita de las dos maneras
"""),

code("""
# FALLA A PROPÓSITO, y no truena. Un carrito que hereda de list.
class CarritoHeredero(list):
    def agregar(self, sku):
        if not sku.startswith("X"):
            raise ValueError("el SKU tiene que empezar con X")
        self.append(sku)


c = CarritoHeredero()
c.agregar("X1")
print("Por la puerta:", c)

c.append("basura sin validar")       # heredado de list, sin validación
c.extend([1, 2, 3])
c += ["más basura"]

print("Por las otras puertas:", c)
print("Productos:", len(c))
print()
metodos_de_list = [n for n in dir(list) if not n.startswith("_")]
MODIFICAN = {"append", "extend", "insert", "pop", "remove", "clear", "sort", "reverse"}

print("Métodos públicos que el carrito heredó sin querer:", len(metodos_de_list))
print("  ", metodos_de_list)
print()
print("De esos, los que pueden cambiar el contenido:",
      len(MODIFICAN & set(metodos_de_list)))
print("De esos, los que pasan por la validación:",
      len(MODIFICAN & set(vars(CarritoHeredero))))
"""),

md("""
Un carrito con once puertas de entrada, y solo una revisa el SKU.

Heredar de `list` le regaló al carrito `append`, `extend`, `insert`, `__iadd__` y todo lo demás, y
ninguno de esos sabe nada de tu regla. La validación no está protegiendo nada: está adornando una de las
once entradas.

Además, "un carrito es una lista" es falso. Un carrito **tiene** una lista, y también tiene un dueño,
una fecha y un total. Heredar de `list` lo obliga a ser una lista para siempre.
"""),

code("""
class Carrito:
    def __init__(self, dueno):
        self.dueno = dueno
        self.__productos = []

    def agregar(self, sku):
        if not sku.startswith("X"):
            raise ValueError("el SKU tiene que empezar con X")
        self.__productos.append(sku)

    def __len__(self):
        return len(self.__productos)

    def __iter__(self):
        return iter(self.__productos)

    def __repr__(self):
        return f"Carrito({self.dueno!r}, {list(self.__productos)})"


c = Carrito("Ana")
c.agregar("X1")

for intento in ["append", "extend", "insert"]:
    print(f"c.{intento} existe:", hasattr(c, intento))

try:
    c.agregar("basura")
except ValueError as e:
    print()
    print("ValueError:", e)

print("Carrito:", c, "· productos:", len(c))
print()
print("Puertas de entrada:", len([n for n in vars(Carrito) if n == "agregar"]))
"""),

md("""
Una sola puerta, y la regla la cuida.

Fíjate en lo que no se perdió: `len(c)` funciona, el `for` funciona, y el carrito se imprime bien. Los
métodos mágicos de la semana 5 dan la sintaxis de una lista sin heredar de `list`, que es la diferencia
entre **parecerse a** y **ser**.

## Cuándo la herencia sí gana
"""),

code("""
class ErrorDeInventario(Exception):
    pass


class SinExistencias(ErrorDeInventario):
    def __init__(self, sku, pedidas, disponibles):
        super().__init__(f"{sku}: pediste {pedidas} y hay {disponibles}")
        self.sku = sku
        self.faltantes = pedidas - disponibles


class SkuInvalido(ErrorDeInventario):
    pass


for error in [SinExistencias("X1", 10, 3), SkuInvalido("Z9 no empieza con X")]:
    try:
        raise error
    except ErrorDeInventario as e:
        print(f"{type(e).__name__:<16}{e}")

print()
try:
    raise SinExistencias("X2", 5, 1)
except ErrorDeInventario as e:
    print("Atrapado por el padre:", e)
    print("Y con los datos de la hija:", e.sku, "faltan", e.faltantes)
"""),

md("""
Aquí la frase se sostiene sola: **un error de sin existencias es un error de inventario**.

Y la herencia hace un trabajo que la composición no podría: `except ErrorDeInventario` atrapa a las dos
hijas y a las que se agreguen mañana, sin tocar el `except`. Eso es lo que compras cuando heredas, y por
eso las jerarquías de excepciones son el caso donde casi nadie discute.

Lo viste en el repaso 5 desde el otro lado, cuando `except Exception` atrapaba las siete excepciones del
cuaderno. Esa jerarquía es la misma, y ahora la estás escribiendo tú.

En la semana 11 esto vuelve con excepciones propias en serio.
"""),

md("""
---
## Cuatro errores de esta sesión

**Olvidar `super().__init__`.** El objeto nace sin los atributos del padre. El error aparece más tarde,
en la primera línea que los use, que puede estar en otro archivo.

**Usar `type(x) == Clase` en un filtro.** Deja fuera a todas las subclases, sin avisar, y el conteo sale
mal.

**Reusar un nombre protegido en la hija.** Dos ideas distintas en una sola llave, y las dos clases se
pisan por turnos. Con dos guiones bajos no pasa.

**Heredar de `list` o de `dict` para reutilizar.** Se heredan diez puertas de entrada y la validación
solo cuida una.
"""),

md("""
---
# Ejercicios

El laboratorio de esta semana es ordenar una jerarquía de transporte en dos niveles como máximo. Los
ejercicios construyen hacia eso.

Las soluciones están hasta abajo del cuaderno.

### Ejercicio 1 · La subclase mínima

Escribe `Vehiculo` con placas y un método `describir`. Después escribe `Motocicleta` que herede de él y
agregue el número de cilindros.

Imprime `vars` del objeto y la cadena `__mro__`, y di qué salió de cada constructor.

### Ejercicio 2 · El olvido

Escribe la misma `Motocicleta` sin llamar a `super().__init__`. Muestra que el objeto se construye sin
protestar, y después atrapa el `AttributeError` de la primera línea que lea las placas.

### Ejercicio 3 · type contra isinstance

Arma una lista con tres objetos de tres clases de tu jerarquía. Fíltrala con `type(x) == Vehiculo` y con
`isinstance(x, Vehiculo)` y compara los dos conteos.

Escribe en un comentario en qué caso usarías `type` a propósito.

### Ejercicio 4 · Protegido contra privado

Escribe una clase con un atributo de un guion bajo y otro de dos. Desde una subclase intenta leer los
dos. Atrapa el error del segundo e imprime `vars` para enseñar los dos nombres reales.

### Ejercicio 5 · La colisión

Escribe una clase madre con `_estado` y una hija que también use `_estado` para otra cosa. Demuestra con
tres llamadas que las dos se pisan.

Arréglalo de dos maneras: con dos guiones bajos, y cambiándole el nombre a uno de los dos. Di cuál
prefieres.

### Ejercicio 6 · La jerarquía sana

Escribe un padre `Documento` con `abrir` y `cerrar`, y tres hijos que solo cambien `leer`. Recórrelos en
un ciclo y comprueba que el ciclo no sabe de qué clase es cada uno.

Cuenta con `__mro__` cuántos niveles tiene tu árbol.

### Ejercicio 7 · El orden que decide

Escribe dos clases con un método del mismo nombre y una tercera que herede de las dos. Imprime el
`__mro__`, corre el método, y después invierte el orden de los padres y vuelve a correrlo.

Explica en un comentario por qué esto es peligroso en un proyecto con varias personas.

### Ejercicio 8 · La prueba de es un

Escribe `Carrito(list)` con un método que valide, y demuestra con tres llamadas distintas que la
validación se puede rodear. Después reescríbelo por composición con `__len__` y `__iter__`.

Di en voz alta las dos frases, la de "es un" y la de "tiene un", y anota cuál suena verdadera.

### Ejercicio 9 · El laboratorio

Te entregan siete clases sueltas de un sistema de transporte. Acomódalas en una jerarquía de dos niveles
como máximo, justificando cada padre en una línea.

Dos niveles como máximo, sin herencia múltiple, y todo método repetido sube al padre. Entrega el
diagrama de la jerarquía y un archivo `.py` con las clases y sus constructores encadenados.

El criterio es que cada relación pase la prueba de "es un", dicha en voz alta frente al otro integrante.
"""),

md("""
---
## Tres ideas para llevarse

**La hija recibe todo menos lo privado.** Lo público y lo protegido se heredan; el doble guion bajo
cambia de nombre y se queda arriba. Y ese renombrado, que en la semana 4 parecía un candado flojo, aquí
resulta ser lo que evita que dos clases de la misma rama se pisen un nombre.

**Dos niveles alcanzan casi siempre.** Cada nivel extra es un archivo más que abrir para entender una
sola llamada, y en el camino aparecen promesas que nadie quiso hacer, como la gallina que vuela.

**Heredar compromete, componer presta.** Si la frase de tipo no suena verdadera, la relación era de uso
y se resuelve con un parámetro. Donde la herencia sí gana es en las jerarquías de excepciones, porque
`except` en el padre atrapa a todas las hijas.

La semana 8 cierra el tema 3 con polimorfismo, sobrescritura, clases abstractas e interfaces, y con el
primer parcial. El ciclo que recorre los tres `Stream` de este cuaderno sin saber de qué clase es cada
uno ya es polimorfismo; lo que falta es el contrato que obliga a las hijas a implementar `leer`.
"""),

md("""
---
# Soluciones

### Ejercicio 1

```python
class Vehiculo:
    def __init__(self, placas):
        self.placas = placas

    def describir(self):
        print(f"{type(self).__name__} con placas {self.placas}")


class Motocicleta(Vehiculo):
    def __init__(self, placas, cilindros):
        super().__init__(placas)
        self.cilindros = cilindros


m = Motocicleta("ABC-123", 2)
m.describir()
print(vars(m))
print([c.__name__ for c in Motocicleta.__mro__])

# placas salió del constructor de Vehiculo, llamado con super. cilindros salió
# del de Motocicleta. describir se heredó y no aparece en vars porque los
# métodos viven en la clase, no en el objeto.
```

### Ejercicio 2

```python
class MotocicletaRota(Vehiculo):
    def __init__(self, placas, cilindros):
        self.cilindros = cilindros


m = MotocicletaRota("ABC-123", 2)
print("Se construyó sin protestar:", vars(m))

try:
    m.describir()
except AttributeError as e:
    print("AttributeError:", e)
```

### Ejercicio 3

```python
class Camion(Vehiculo):
    pass


flota = [Vehiculo("A"), Motocicleta("B", 2), Camion("C")]

print("type:      ", len([v for v in flota if type(v) == Vehiculo]))
print("isinstance:", len([v for v in flota if isinstance(v, Vehiculo)]))

# Usaría type a propósito para distinguir el caso base de sus especializaciones,
# por ejemplo al serializar: un Vehiculo genérico se guarda distinto de una
# Motocicleta. Fuera de eso, isinstance es lo que uno quiere decir.
```

### Ejercicio 4

```python
class Cuenta:
    def __init__(self, titular):
        self._titular = titular
        self.__nip = "1234"


class CuentaDeAhorro(Cuenta):
    def leer_protegido(self):
        return self._titular

    def leer_privado(self):
        return self.__nip


c = CuentaDeAhorro("Ana")
print("Protegido:", c.leer_protegido())

try:
    c.leer_privado()
except AttributeError as e:
    print("AttributeError:", e)

print(vars(c))
print("Con el nombre real:", c._Cuenta__nip)
```

### Ejercicio 5

```python
class Tarea:
    def __init__(self, titulo):
        self.titulo = titulo
        self._estado = "pendiente"

    def terminar(self):
        self._estado = "terminada"

    def esta_pendiente(self):
        return self._estado == "pendiente"


class TareaRevisada(Tarea):
    def __init__(self, titulo, revisor):
        super().__init__(titulo)
        self.revisor = revisor
        self._estado = "sin revisar"      # otra idea, mismo nombre

    def aprobar(self):
        self._estado = "aprobada"


t = TareaRevisada("Entrega 1", "Ana")
print("¿Pendiente al crearse?", t.esta_pendiente())
t.aprobar()
print("Después de aprobar, ¿pendiente?", t.esta_pendiente())
t.terminar()
print("Después de terminar, el estado de revisión dice:", t._estado)
print(vars(t))


# Corrección 1: dos guiones bajos en cada clase.
# Corrección 2: nombres distintos, _estado y _revision.
class TareaClara(Tarea):
    def __init__(self, titulo, revisor):
        super().__init__(titulo)
        self.revisor = revisor
        self._revision = "sin revisar"

    def aprobar(self):
        self._revision = "aprobada"


t = TareaClara("Entrega 1", "Ana")
t.aprobar()
print(vars(t))
print("¿Pendiente?", t.esta_pendiente())

# Prefiero la segunda. El doble guion bajo tapa el síntoma y deja dos cosas
# distintas llamándose igual, que es el problema de fondo. Ponerles nombres
# distintos obliga a decidir qué es cada una, y eso se lee.
```

### Ejercicio 6

```python
class Documento:
    def __init__(self):
        self.abierto = False

    def abrir(self):
        self.abierto = True

    def cerrar(self):
        self.abierto = False


class DocumentoPDF(Documento):
    def leer(self):
        print("  leyendo un PDF")


class DocumentoWord(Documento):
    def leer(self):
        print("  leyendo un Word")


class DocumentoTexto(Documento):
    def leer(self):
        print("  leyendo texto plano")


for doc in [DocumentoPDF(), DocumentoWord(), DocumentoTexto()]:
    doc.abrir()
    doc.leer()
    doc.cerrar()

print("Niveles:", len(DocumentoPDF.__mro__) - 1)
print([c.__name__ for c in DocumentoPDF.__mro__])
```

### Ejercicio 7

```python
class Registrador:
    def procesar(self):
        print("guardando en la bitácora")


class Validador:
    def procesar(self):
        print("validando los datos")


class Pipeline(Registrador, Validador):
    pass


print([c.__name__ for c in Pipeline.__mro__])
Pipeline().procesar()


class Pipeline(Validador, Registrador):
    pass


print([c.__name__ for c in Pipeline.__mro__])
Pipeline().procesar()

# Es peligroso porque la lista de padres se lee como una enumeración y no como
# una decisión. Nadie ordena alfabéticamente una lista sabiendo que está
# cambiando el comportamiento del programa, y sin embargo eso es lo que pasa.
```

### Ejercicio 8

```python
class CarritoHeredero(list):
    def agregar(self, sku):
        if not sku.startswith("X"):
            raise ValueError("el SKU tiene que empezar con X")
        self.append(sku)


c = CarritoHeredero()
c.agregar("X1")
c.append("basura")
c.insert(0, "más basura")
c += [42]
print(c, "->", len(c), "elementos y una sola validación")


class Carrito:
    def __init__(self):
        self.__productos = []

    def agregar(self, sku):
        if not sku.startswith("X"):
            raise ValueError("el SKU tiene que empezar con X")
        self.__productos.append(sku)

    def __len__(self):
        return len(self.__productos)

    def __iter__(self):
        return iter(self.__productos)


c = Carrito()
c.agregar("X1")
print(hasattr(c, "append"), len(c), list(c))

# "Un carrito es una lista" suena falsa: un carrito tiene dueño, fecha y total, y
# una lista no. "Un carrito tiene una lista" suena verdadera.
```

### Ejercicio 9

```python
class Vehiculo:
    def __init__(self, placas: str, capacidad: int) -> None:
        self.placas = placas
        self.capacidad = capacidad

    def describir(self) -> str:
        return f"{type(self).__name__} {self.placas}, capacidad {self.capacidad}"


class Automovil(Vehiculo):
    def __init__(self, placas, capacidad, puertas):
        super().__init__(placas, capacidad)
        self.puertas = puertas


class Autobus(Vehiculo):
    def __init__(self, placas, capacidad, ruta):
        super().__init__(placas, capacidad)
        self.ruta = ruta


class Camion(Vehiculo):
    def __init__(self, placas, capacidad, toneladas):
        super().__init__(placas, capacidad)
        self.toneladas = toneladas


class Motocicleta(Vehiculo):
    def __init__(self, placas, capacidad, cilindros):
        super().__init__(placas, capacidad)
        self.cilindros = cilindros


flota = [
    Automovil("AAA-111", 5, 4),
    Autobus("BBB-222", 40, "Centro-Norte"),
    Camion("CCC-333", 2, 12.5),
    Motocicleta("DDD-444", 2, 2),
]

for v in flota:
    print(v.describir())

print()
print("Niveles del árbol:", max(len(type(v).__mro__) for v in flota) - 1)
```

Las justificaciones, una línea cada una.

**`Vehiculo` es el padre** porque placas y capacidad los tienen los cuatro, y `describir` se escribiría
igual cuatro veces.

**Los cuatro cuelgan directo de `Vehiculo`** y ninguno de otro hermano. Un autobús no es un automóvil
grande: es un vehículo con ruta.

**No hay clase `VehiculoDeCarga` entre `Vehiculo` y `Camion`.** Con un solo hijo, ese nivel no reúne
nada y solo agrega un archivo que abrir.

**Ninguna hereda de dos padres.** Si mañana aparece un vehículo anfibio, va a ser tentador; la salida es
recibir un motor marino en el constructor y no colgarse de una segunda rama.
"""),

]

write(OUT / "es" / "w07.ipynb", es)
print("wrote", OUT / "es" / "w07.ipynb")
