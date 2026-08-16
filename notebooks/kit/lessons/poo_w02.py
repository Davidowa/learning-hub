"""notebooks/programacion-orientada-a-objetos/es/w02.ipynb

Source deck: ppts/python/programacion-orientada-a-objetos/es/w02.es.yaml
Source code:  los dos bloques del deck, grupo_estructurado.py y grupo_poo.py,
              se escribieron para el curso. No hay archivo en el repositorio para
              esta semana; el tema es conceptual y el código de clases empieza en
              02 - POO/6th Module a partir de la semana 4.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from nbkit import md, code, write, REPO

OUT = REPO / "notebooks" / "programacion-orientada-a-objetos"

es = [

md("""
# Programación Orientada a Objetos · Semana 02
## Tema 1 · Introducción a la POO

**COM102 · Facultad de Ingeniería · Profesor David Escobar-Castillejos**

Por qué existe el paradigma. Qué problema tenían los programas de los años setenta y qué se inventó
para resolverlo.

Los cinco repasos quedaron atrás y con ellos todo el Python que hace falta para esta sesión. Aquí no
hay sintaxis nueva que memorizar. Hay una pregunta: por qué alguien decidiría escribir diez líneas
donde había cuatro, y qué gana con eso.

Al terminar este cuaderno vas a poder:

1. Definir qué es un paradigma, y por qué un lenguaje puede soportar varios a la vez.
2. Resolver el mismo problema en tres estilos y medir en qué se diferencian.
3. Nombrar los cuatro principios del paradigma y reconocerlos en código que ya usas.
4. Decidir cuándo una clase estorba y una función suelta hace mejor el trabajo.

### Cómo se usa este cuaderno

Ejecuta las celdas en orden con **Shift + Enter**. Cinco fallan a propósito, y **cuatro de las cinco
no lanzan ninguna excepción**. Este es el cuaderno donde eso importa más: el argumento de la sesión
completa es que el estilo estructurado se rompe en silencio cuando el programa crece, y la única
forma honesta de sostenerlo es enseñarlo rompiéndose.
"""),

md("""
---
# Bloque 1 · Qué es un paradigma

Un paradigma no es una sintaxis. Es un acuerdo sobre cómo se reparte el código antes de escribirlo.

No cambia lo que la computadora ejecuta al final, porque todo termina en instrucciones de máquina.
Cambia **dónde vive cada pedazo de la lógica y quién puede tocarlo**.

Vamos a resolver el mismo problema tres veces. El problema es mínimo a propósito: un grupo de alumnos
con su nombre y su calificación, el promedio, y quiénes aprobaron.

## Estilo imperativo: órdenes en secuencia
"""),

code("""
nombres = ["Ana", "Luis", "Sofía", "Beto", "Carla"]
notas = [8.5, 7.0, 9.5, 5.5, 9.0]

total = 0
for nota in notas:
    total = total + nota
promedio = total / len(notas)

aprobados = []
i = 0
while i < len(nombres):
    if notas[i] >= 7.0:
        aprobados.append(nombres[i])
    i = i + 1

print("Promedio:", promedio)
print("Aprobados:", aprobados)
"""),

md("""
Funciona y es el estilo de los años cincuenta: instrucciones una tras otra, sin una sola función.

Lo que le falta no es corrección, es nombre. Para saber que ese primer ciclo calcula un promedio hay
que leerlo completo. Y si mañana hace falta el promedio en otro lado, se copia y se pega.

## Estilo estructurado: las órdenes se agrupan
"""),

code("""
nombres = ["Ana", "Luis", "Sofía", "Beto", "Carla"]
notas = [8.5, 7.0, 9.5, 5.5, 9.0]
carreras = ["Mecatrónica", "Sistemas", "Mecatrónica", "Industrial", "Sistemas"]


def promedio(valores):
    return sum(valores) / len(valores)


def aprobados(nombres, notas, minimo=7.0):
    return [n for n, c in zip(nombres, notas) if c >= minimo]


def reporte(nombres, notas):
    for nombre, nota in zip(nombres, notas):
        print(f"  {nombre:<7}{nota}")


print("Promedio:", promedio(notas))
print("Aprobados:", aprobados(nombres, notas))
print("Reporte:")
reporte(nombres, notas)
"""),

md("""
Este es el estilo de los setenta, y con cinco alumnos no hay nada que criticarle. Cada función tiene
un nombre, se prueba sola y se usa en varios lugares. Es exactamente lo que el repaso 3 pedía.

El problema no está en las funciones. Está en las tres listas.

**Lo que mantiene juntos a un alumno con su calificación es la posición.** Nada más. `nombres[1]` y
`notas[1]` son la misma persona porque los dos están en el índice 1, y ese acuerdo no está escrito en
ninguna parte: vive en la cabeza de quien escribió el archivo.

## Lo que pasa cuando alguien se da de baja
"""),

code("""
# FALLA A PROPÓSITO, y no truena. Luis se da de baja y se borra de una sola lista.
nombres.remove("Luis")

print("Longitudes:", len(nombres), len(notas), len(carreras))
print()
print("El reporte que sale:")
reporte(nombres, notas)
print()
print("Promedio:", promedio(notas))
print("Aprobados:", aprobados(nombres, notas))
"""),

md("""
Ni un error. Ni una advertencia. Un reporte completo, con nombres reales y calificaciones reales.

Y está mal de tres formas distintas a la vez.

**Sofía aparece con 7.0 y tenía 9.5.** A partir de la posición donde estaba Luis, cada nombre quedó
emparejado con la calificación del siguiente. Beto pasó de 5.5 a 9.5 y aprobó sin haber aprobado.

**Una calificación se quedó sin dueño.** `zip` se detiene en la lista más corta, así que los cuatro
nombres que quedaron consumieron cuatro de las cinco calificaciones y el 9.0 de Carla nunca se
imprimió. `zip` no avisa de eso, nunca.

**El promedio sigue diciendo 7.9**, que es el promedio correcto de cinco calificaciones repartidas
entre cuatro alumnos. Un número exacto de una población que ya no existe.

La celda de abajo mide el daño en lugar de describirlo.
"""),

code("""
ORIGINAL = {"Ana": 8.5, "Luis": 7.0, "Sofía": 9.5, "Beto": 5.5, "Carla": 9.0}

print(f"{'Alumno':<8}{'Real':>7}{'Reportado':>11}   ")
for nombre, nota in zip(nombres, notas):
    marca = "ok" if ORIGINAL[nombre] == nota else "MAL"
    print(f"{nombre:<8}{ORIGINAL[nombre]:>7}{nota:>11}   {marca}")

perdidos = set(ORIGINAL) - set(nombres)
print()
print("Alumnos que ya no aparecen:", sorted(perdidos))
print("Parejas que produjo zip:", len(list(zip(nombres, notas))),
      "sobre", len(notas), "calificaciones")
"""),

md("""
Tres de cuatro renglones están mal y el programa nunca dijo nada.

Este es el argumento completo de la sesión, y no hace falta ninguno más. El estilo estructurado no
tiene ningún mecanismo para impedir que dos listas que deberían ir juntas se separen. La disciplina
del programador es lo único que las sostiene, y la disciplina falla.

## La segunda forma de romperlo
"""),

code("""
# FALLA A PROPÓSITO, y no truena. Ordenar las notas para hacer un ranking.
nombres = ["Ana", "Luis", "Sofía", "Beto", "Carla"]
notas = [8.5, 7.0, 9.5, 5.5, 9.0]

notas_ordenadas = sorted(notas, reverse=True)

print("Ranking del grupo:")
for lugar, (nombre, nota) in enumerate(zip(nombres, notas_ordenadas), start=1):
    real = ORIGINAL[nombre]
    marca = "" if real == nota else f"  (su nota real es {real})"
    print(f"  {lugar}. {nombre:<7}{nota}{marca}")
"""),

md("""
Ana encabeza el ranking con un 9.5 que es de Sofía. Beto sale con 7.0 y aprueba con una calificación
de 5.5.

Ordenar una de las dos listas rompe el acuerdo de posiciones de un golpe, y es lo primero que se le
ocurre a cualquiera para hacer un ranking. En la versión con objetos esto no se puede escribir mal,
porque no hay dos listas que ordenar.

## Estilo orientado a objetos: los datos viajan con sus funciones
"""),

code("""
class Alumno:
    def __init__(self, nombre: str, nota: float, carrera: str) -> None:
        self.nombre = nombre
        self.nota = nota
        self.carrera = carrera

    def aprobo(self, minimo: float = 7.0) -> bool:
        return self.nota >= minimo

    def __repr__(self) -> str:
        return f"Alumno({self.nombre!r}, {self.nota})"


grupo = [
    Alumno("Ana", 8.5, "Mecatrónica"),
    Alumno("Luis", 7.0, "Sistemas"),
    Alumno("Sofía", 9.5, "Mecatrónica"),
    Alumno("Beto", 5.5, "Industrial"),
    Alumno("Carla", 9.0, "Sistemas"),
]

print(grupo)
print("Promedio:", sum(a.nota for a in grupo) / len(grupo))
print("Aprobados:", [a.nombre for a in grupo if a.aprobo()])
"""),

md("""
Diez líneas donde antes había cuatro. Esa es la factura, y hay que reconocerla antes de cobrar el
beneficio.

Nada de la sintaxis es nuevo del todo: `class`, `def`, parámetros con valor por defecto, anotaciones
de tipo que no obligan, `return`. Lo único que no habías visto es `self`, y la semana 3 se dedica
entera a él. Por ahora basta con leerlo como "este objeto".

Ahora las dos operaciones que rompieron la versión anterior.
"""),

code("""
# Dar de baja a Luis.
grupo = [a for a in grupo if a.nombre != "Luis"]

print("Quedan", len(grupo), "alumnos")
for a in grupo:
    print(f"  {a.nombre:<7}{a.nota}")
print("Promedio:", sum(a.nota for a in grupo) / len(grupo))

print()
# El ranking.
for lugar, a in enumerate(sorted(grupo, key=lambda a: -a.nota), start=1):
    print(f"  {lugar}. {a.nombre:<7}{a.nota}")
"""),

md("""
El promedio pasó de 7.9 a 8.125 porque ahora se calcula sobre los cuatro alumnos que quedan, y no
sobre cinco calificaciones repartidas entre cuatro personas. El ranking está bien sin que nadie
tuviera cuidado.

No es que el código de arriba sea más listo. Es que **la pregunta que rompía el programa ya no se
puede formular**. No hay forma de borrar el nombre y dejar la calificación, porque no hay dos lugares
donde vivan. No hay forma de ordenar las notas sin llevarse los nombres, porque no hay una lista de
notas suelta.

Ese es el beneficio exacto de la POO: no hace posible nada que antes fuera imposible, hace imposible
cierta clase de error.

## El costo del cambio, medido
"""),

code("""
# Agregar un campo nuevo: la fecha de inscripción.

# Versión estructurada: una lista más, y hay que tocar cada función que la use.
fechas = ["2026-01-15", "2026-01-16", "2026-01-15", "2026-01-20", "2026-01-15"]
LISTAS = ["nombres", "notas", "carreras", "fechas"]
print("Estructurado:", len(LISTAS), "listas paralelas que hay que mantener alineadas")
print("            ", len(LISTAS) * (len(LISTAS) - 1) // 2,
      "parejas que se pueden desalinear")


# Versión con objeto: una línea en el constructor.
class AlumnoConFecha(Alumno):
    def __init__(self, nombre, nota, carrera, fecha):
        super().__init__(nombre, nota, carrera)
        self.fecha = fecha


ana = AlumnoConFecha("Ana", 8.5, "Mecatrónica", "2026-01-15")
print()
print("POO:", len(vars(ana)), "atributos en 1 objeto")
print("     0 parejas que se pueden desalinear")
print(vars(ana))
"""),

md("""
Con cuatro listas hay seis parejas que pueden salirse de sincronía, y cada una es un bug esperando.
Con cinco listas serían diez. El número crece más rápido que la cantidad de datos, y ese es el
momento exacto en que el estilo estructurado deja de escalar.

Fíjate también en lo que imprimió `vars(ana)`: un diccionario. **Un objeto de Python guarda sus
atributos en un diccionario de verdad**, el mismo tipo del repaso 4. La semana 3 empieza justo ahí.

## Un cuarto estilo, para completar el mapa
"""),

code("""
from collections import namedtuple

AlumnoTupla = namedtuple("AlumnoTupla", "nombre nota carrera")

grupo_funcional = [
    AlumnoTupla("Ana", 8.5, "Mecatrónica"),
    AlumnoTupla("Luis", 7.0, "Sistemas"),
    AlumnoTupla("Sofía", 9.5, "Mecatrónica"),
]

# Nada se modifica: cada operación devuelve algo nuevo.
subidos = [a._replace(nota=a.nota + 0.5) for a in grupo_funcional]

print("Originales:", [(a.nombre, a.nota) for a in grupo_funcional])
print("Subidos:   ", [(a.nombre, a.nota) for a in subidos])

# FALLA A PROPÓSITO. Esta sí truena, y ahí está la garantía del estilo.
try:
    grupo_funcional[0].nota = 10.0
except AttributeError as e:
    print()
    print("AttributeError:", e)
"""),

md("""
El estilo funcional lleva la idea al extremo contrario: los datos no se modifican nunca, y cada
operación devuelve una estructura nueva.

`namedtuple` es una tupla con nombres, así que hereda la inmutabilidad del repaso 4 y por eso la
asignación truena. Eso, que parece una limitación, es la garantía completa del estilo: si nada cambia,
nada se puede desalinear.

| Pregunta | Estructurado | Orientado a objetos | Funcional |
|---|---|---|---|
| Unidad básica | La función | La clase | La función pura |
| Dónde viven los datos | Variables sueltas | Dentro del objeto | Se pasan y se devuelven |
| Quién los modifica | Cualquier función | Solo sus métodos | Nadie, se crean nuevos |
| Se rompe cuando | Hay muchos datos ligados | Hay poco estado real | Hay que guardar estado |

Los tres estilos están en Python y ninguno es obligatorio. Un lenguaje soporta varios paradigmas a la
vez, y la decisión sigue siendo tuya en cada archivo.

## Tres respuestas al mismo problema

**Años cincuenta, imperativo.** Instrucciones una tras otra, con saltos `GOTO` a cualquier parte del
programa.

**Años setenta, estructurado.** Las órdenes se agrupan en funciones con entrada y salida definidas.

**Años ochenta, orientado a objetos.** Los datos viajan con las funciones que los manipulan, en una
sola unidad.

Cada salto ocurrió cuando el estilo anterior dejó de escalar. El primer lenguaje con clases y objetos
es **Simula 67**, de 1967, doce años antes de que el término se volviera común. Lo diseñaron
Ole-Johan Dahl y Kristen Nygaard en Noruega para simular sistemas físicos, no para escribir software
de negocio, y la POO se volvió común hasta que los programas pasaron de miles a cientos de miles de
líneas.
"""),

md("""
---
# Bloque 2 · Los cuatro principios

Abstracción, encapsulamiento, herencia y polimorfismo. Se sostienen entre sí y por eso se enseñan
juntos.

Los cuatro tienen su semana propia más adelante. Aquí solo se nombran, con la versión más corta que
corre, porque ya los has estado usando sin llamarlos así.

## Abstracción: describir la cosa por lo que hace

Quedarse con lo esencial y esconder el resto.
"""),

code("""
for valor in ["texto", [1, 2, 3], {"a": 1, "b": 2}, {1, 2, 3}, (1, 2)]:
    print(f"{str(valor):<18}{type(valor).__name__:<7}len = {len(valor)}")
"""),

md("""
`len` te dio la longitud de cinco estructuras que por dentro no se parecen en nada. Una cadena cuenta
caracteres, un diccionario cuenta llaves, un conjunto cuenta elementos únicos.

Tú escribiste `len(valor)` cinco veces y ninguna de las cinco supiste cómo estaba implementado.
**Eso es abstracción**: usar algo por lo que hace y no por cómo está hecho. Ya la usabas.

## Encapsulamiento: el objeto decide qué expone
"""),

code("""
class Cuenta:
    def __init__(self, titular, saldo=0.0):
        self.titular = titular
        self._saldo = saldo          # el guion bajo dice "esto es asunto mío"
        self.movimientos = []

    def depositar(self, monto):
        if monto <= 0:
            raise ValueError("El depósito tiene que ser positivo")
        self._saldo += monto
        self.movimientos.append(("depósito", monto))

    def saldo(self):
        return self._saldo


cuenta = Cuenta("Ana", 1000.0)
cuenta.depositar(500)
print("Saldo:", cuenta.saldo())
print("Movimientos:", cuenta.movimientos)

try:
    cuenta.depositar(-200)
except ValueError as e:
    print("ValueError:", e)
"""),

code("""
# FALLA A PROPÓSITO, y no truena. El guion bajo es un acuerdo, no un candado.
cuenta._saldo = 999999

print("Saldo:", cuenta.saldo())
print("Movimientos:", cuenta.movimientos)
print()
print("El saldo dice", cuenta.saldo(), "y los movimientos suman",
      sum(m for _, m in cuenta.movimientos) + 1000.0)
"""),

md("""
El objeto quedó mintiendo. El saldo dice un número y la lista de movimientos cuenta otra historia, y
las dos viven en el mismo objeto.

`depositar` no dejaba pasar un monto negativo, pero tocar `_saldo` directamente saltó esa validación
completa. El guion bajo es una convención entre programadores, no un mecanismo del lenguaje: dice
"esto es asunto mío", y Python no lo hace cumplir.

La semana 4 se dedica a los modificadores de acceso y la 6 al encapsulamiento en serio, incluido el
doble guion bajo, que sí cambia algo. Por ahora quédate con la idea: **encapsular es que el objeto
sea el único que puede dejar sus datos en un estado imposible**, y una asignación desde fuera lo
rompe sin avisar.

## Herencia: reusar sin copiar
"""),

code("""
class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

    def saludar(self):
        return f"Hola, soy {self.nombre}"


class Profesor(Persona):
    def __init__(self, nombre, materia):
        super().__init__(nombre)
        self.materia = materia

    def saludar(self):
        return f"{super().saludar()} y doy {self.materia}"


for quien in [Persona("Ana"), Profesor("David", "COM102")]:
    print(quien.saludar())

print()
print("¿Un profesor es una persona?", isinstance(Profesor("D", "X"), Persona))
print("Cadena de herencia:", [c.__name__ for c in Profesor.__mro__])
"""),

md("""
`Profesor` no volvió a escribir cómo se guarda un nombre. Lo heredó, y solo añadió lo suyo.

Esa cadena que imprime `__mro__` es la misma que viste en el repaso 5 con las excepciones:
`IndexError` desciende de `LookupError` que desciende de `Exception`. Python usa el mismo mecanismo
para las excepciones de la biblioteca estándar y para las clases que escribes tú. Las semanas 7 y 8
van de eso.

## Polimorfismo: el mismo mensaje, respuestas distintas
"""),

code("""
print(3 + 4)
print("ab" + "cd")
print([1, 2] + [3])
print((1,) + (2,))

print()
print(3 * 3)
print("ab" * 2)
print([1] * 3)
"""),

md("""
El mismo `+` sumó, concatenó texto, unió listas y unió tuplas. Ninguna de las cuatro operaciones se
parece a las otras por dentro.

Eso ya es polimorfismo, y lo llevas usando desde el repaso 1. Lo que la semana 8 va a enseñar es cómo
hacer que **tus** objetos contesten a `+`, a `len` y a `print`, que es para lo que sirven los métodos
mágicos.

Con las clases de arriba el mismo mecanismo se ve así.
"""),

code("""
class Alumno2(Persona):
    def saludar(self):
        return f"Qué tal, soy {self.nombre} y voy en segundo"


for quien in [Persona("Ana"), Profesor("David", "COM102"), Alumno2("Beto")]:
    print(f"{type(quien).__name__:<9}{quien.saludar()}")
"""),

md("""
El ciclo no pregunta de qué tipo es cada uno. Llama a `saludar` y cada objeto contesta a su manera.

Fíjate en lo que eso permite: agregar una clase nueva no obliga a tocar el ciclo. En la versión con
`if type(quien) == ...` habría que abrirlo y añadir una rama cada vez.
"""),

md("""
---
# Bloque 3 · Cuándo el paradigma estorba

Cuatro señales de que estás forzando una clase donde no había ninguna.

## Señal 1: la clase sin estado
"""),

code("""
# FALLA A PROPÓSITO, y no truena. Una clase que no guarda nada.
class Calculadora:
    def sumar(self, a, b):
        return a + b

    def restar(self, a, b):
        return a - b

    def multiplicar(self, a, b):
        return a * b


calc = Calculadora()
print(calc.sumar(2, 3), calc.restar(9, 4), calc.multiplicar(3, 3))

print()
print("Lo que el objeto recuerda:", vars(calc), "->", len(vars(calc)), "atributos")
print("Y después de tres operaciones sigue recordando:", vars(calc))
"""),

md("""
El diccionario del objeto está vacío antes y después. `calc` no guarda absolutamente nada entre una
llamada y la siguiente.

Eso significa que `self` no se usa en ninguno de los tres métodos, y que la clase existe únicamente
para obligarte a escribir `calc.` antes de cada llamada. Tres funciones sueltas hacen lo mismo con
menos ceremonia y se importan igual de bien.

Compáralo con la cuenta bancaria de hace unas celdas.
"""),

code("""
cuenta = Cuenta("Ana", 1000.0)
print("Recién creada:", vars(cuenta))

cuenta.depositar(500)
cuenta.depositar(250)
print("Tras dos depósitos:", vars(cuenta))
print()
print("Atributos que cambian entre llamadas:", len(vars(cuenta)))
"""),

md("""
Aquí sí hay algo que recordar, y ese recuerdo es lo que se llama **estado**. El saldo depende de
todos los depósitos anteriores, así que la cuenta no puede ser una función: una función que reciba y
devuelva el saldo cada vez le pasa el problema a quien la llama.

## Las otras tres señales

**Getters y setters para todo.** Si cada atributo privado tiene un método para leerlo y otro para
escribirlo, no encapsulaste nada: pusiste una puerta trasera con más pasos. Un `set_saldo` que asigna
sin revisar es exactamente la celda que dejó la cuenta mintiendo.

**Herencia de cinco niveles.** Cuando hay que subir cuatro clases para entender qué hace un método,
la jerarquía perdió el rumbo. La semana 7 pone el límite en la práctica.

**Un script de treinta líneas.** Para leer un CSV y sacar un promedio, una función suelta gana
siempre. La factura de diez líneas contra cuatro solo se paga cuando el programa vive lo suficiente
para cambiar.

## La prueba del nombre

Intenta nombrar la clase con un sustantivo concreto. Si el mejor nombre que se te ocurre es un verbo
o termina en "-ador", probablemente era una función.
"""),

code("""
CANDIDATOS = [
    ("Alumno", "sustantivo concreto", "clase"),
    ("Cuenta", "sustantivo concreto", "clase"),
    ("Factura", "sustantivo concreto", "clase"),
    ("Calculadora", "sustantivo, pero sin nada que recordar", "función"),
    ("ProcesadorDeDatos", "un verbo con disfraz", "función"),
    ("GestorDeArchivos", "un verbo con disfraz", "función"),
    ("ValidadorDeCorreo", "un verbo con disfraz", "función"),
]

print(f"{'Nombre':<20}{'Qué es':<40}{'Veredicto'}")
for nombre, que_es, veredicto in CANDIDATOS:
    print(f"{nombre:<20}{que_es:<40}{veredicto}")
"""),

md("""
`ValidadorDeCorreo` con un método `validar` es una función llamada `validar_correo` a la que le
pusieron una casa. `Factura` guarda conceptos, renglones, impuestos y un total que depende de todos
ellos, así que es una clase.

## Predice antes de correr

¿Cuál de estos cuatro es el único que pide una clase?

- **A.** Convertir grados Celsius a Fahrenheit.
- **B.** Una cuenta bancaria con saldo y movimientos.
- **C.** Contar cuántas vocales tiene una palabra.
- **D.** Ordenar una lista de números de menor a mayor.

En lugar de contestar de memoria, la celda de abajo aplica el criterio: **¿el objeto recuerda algo
entre una llamada y la siguiente?**
"""),

code("""
class CelsiusAFahrenheit:
    def convertir(self, c):
        return c * 9 / 5 + 32


class ContadorDeVocales:
    def contar(self, palabra):
        return sum(1 for letra in palabra.lower() if letra in "aeiou")


class Ordenador:
    def ordenar(self, numeros):
        return sorted(numeros)


pruebas = [
    ("Celsius a Fahrenheit", CelsiusAFahrenheit(), lambda o: o.convertir(100)),
    ("Cuenta bancaria", Cuenta("Ana", 1000.0), lambda o: o.depositar(500)),
    ("Contar vocales", ContadorDeVocales(), lambda o: o.contar("murciélago")),
    ("Ordenar una lista", Ordenador(), lambda o: o.ordenar([3, 1, 2])),
]

print(f"{'Caso':<24}{'Antes':>7}{'Después':>9}{'¿Cambió?':>11}   Veredicto")
for etiqueta, objeto, operacion in pruebas:
    antes = dict(vars(objeto))
    operacion(objeto)
    despues = dict(vars(objeto))
    cambio = "sí" if antes != despues else "no"
    veredicto = "clase" if despues else "función"
    print(f"{etiqueta:<24}{len(antes):>7}{len(despues):>9}{cambio:>11}   {veredicto}")
"""),

md("""
La respuesta es **B**.

Tres de los cuatro objetos siguen con cero atributos después de hacer su trabajo, y la columna de
cambio dice que no. La cuenta bancaria tiene tres atributos y su contenido sí cambió por la
operación: el saldo pasó de 1000 a 1500 y quedó un movimiento registrado.

| Opción | ¿Guarda estado? | ¿Datos ligados? | Veredicto |
|---|---|---|---|
| Celsius a Fahrenheit | No | No | Función |
| Cuenta bancaria | Sí, el saldo | Sí, saldo y movimientos | Clase |
| Contar vocales | No | No | Función |
| Ordenar una lista | No | No | Función |

Solo la cuenta recuerda algo entre una operación y la siguiente. Ese recuerdo es el estado, y es la
única razón sólida para escribir una clase.

> La gran idea son los mensajes. El foco debería estar en cómo se comunican los objetos, no en cómo
> están hechos por dentro.
>
> Alan Kay, correspondencia sobre el diseño de Smalltalk, 1998
"""),

md("""
---
# Ejercicios

Las soluciones están hasta abajo del cuaderno.

### Ejercicio 1 · Romper las listas paralelas

Con tres listas de productos, precios y existencias, borra un producto de una sola lista y muestra el
reporte que sale. Señala cuántos renglones quedaron mal y cuántos productos desaparecieron.

### Ejercicio 2 · El mismo problema con objetos

Reescribe el ejercicio 1 con una clase `Producto`. Borra el mismo producto y demuestra que el reporte
sigue siendo correcto.

Explica en un comentario qué operación de la versión anterior ya no se puede escribir mal.

### Ejercicio 3 · La medida del acoplamiento

Escribe una función `parejas_desalineables(n)` que devuelva cuántas parejas de listas pueden salirse
de sincronía con `n` listas paralelas. Calcúlala para 2, 3, 4, 5 y 10 listas.

Di en un comentario a partir de cuántas listas el número te parece inmanejable.

### Ejercicio 4 · Abstracción que ya usabas

Encuentra tres funciones de Python, además de `len`, que funcionen sobre tipos distintos sin que
tengas que saber cómo están implementados. Pruébalas con al menos tres tipos cada una.

### Ejercicio 5 · El objeto que miente

Escribe una clase `Termometro` con un método `registrar(temperatura)` que rechace valores debajo de
-273.15. Después deja el objeto en un estado imposible modificando el atributo directamente y muestra
que el objeto ya no es coherente.

### Ejercicio 6 · Herencia mínima

Escribe `Vehiculo` con un método `describir`, y dos clases hijas que lo sobrescriban. Recórrelas en un
ciclo que no pregunte por el tipo.

Agrega una tercera clase hija y comprueba que el ciclo no cambió.

### Ejercicio 7 · Clase o función

Para cada uno de estos seis casos decide si va clase o función, y justifica con la prueba del estado:

1. Calcular el IVA de un monto.
2. Un carrito de compras.
3. Convertir una fecha de texto a objeto.
4. Un temporizador que se puede pausar y reanudar.
5. Contar palabras en un texto.
6. Una partida de ajedrez.

### Ejercicio 8 · La calculadora que sí tiene estado

Convierte la `Calculadora` sin estado en una que sí lo tenga: que recuerde el resultado anterior y
permita encadenar operaciones. Demuestra con `vars` que ahora sí guarda algo.

### Ejercicio 9 · La tarea

Elige un sistema que uses a diario, la app del transporte, la cafetería o el gimnasio, y describe el
mismo módulo en los tres paradigmas.

Entrega una tabla de tres columnas con la unidad básica, dónde viven los datos y quién los modifica.
El módulo tiene que caber en media cuartilla. La columna de POO nombra objetos concretos, no
categorías como "gestor" o "manejador".

Agrega un párrafo con qué paradigma elegirías para ese sistema y por qué, argumentando con el sistema
que elegiste y no con generalidades.
"""),

md("""
---
## Tres ideas para llevarse

**El paradigma resuelve un problema de escala.** Con cien líneas cualquiera de los tres funciona. La
diferencia aparece cuando el programa crece, y aparece como listas que se desalinean sin lanzar una
sola excepción.

**Los cuatro principios son un conjunto.** Abstracción, encapsulamiento, herencia y polimorfismo se
sostienen entre sí, y los cuatro ya estaban en el Python que usabas antes de esta sesión.

**Forzar clases cuesta caro.** Una clase sin estado es una función con pasos extra y un nombre peor.
El diccionario vacío de `vars` es la prueba, y cabe en una línea.

La semana 3 arranca con el primer código que corre de verdad: qué es una clase, qué es un objeto, y
qué demonios es `self`. La pista ya está en este cuaderno: `vars(ana)` devolvió un diccionario.
"""),

md("""
---
# Soluciones

### Ejercicio 1

```python
productos = ["café", "filtro", "taza", "prensa"]
precios = [45.0, 12.0, 89.0, 340.0]
existencias = [30, 120, 45, 8]

REAL = dict(zip(productos, precios))

productos.remove("filtro")

print("Reporte:")
mal = 0
for producto, precio in zip(productos, precios):
    correcto = REAL[producto] == precio
    mal += 0 if correcto else 1
    print(f"  {producto:<8}{precio:>8}  {'ok' if correcto else 'MAL'}")

print()
print("Renglones incorrectos:", mal, "de", len(list(zip(productos, precios))))
print("Productos que desaparecieron:", sorted(set(REAL) - set(productos)))
print("Existencias sin dueño:", len(existencias) - len(productos))
```

Dos renglones quedan mal, uno desaparece del reporte y una existencia se queda sin producto. Ninguna
línea lanza nada.

### Ejercicio 2

```python
class Producto:
    def __init__(self, nombre, precio, existencia):
        self.nombre = nombre
        self.precio = precio
        self.existencia = existencia

    def __repr__(self):
        return f"Producto({self.nombre!r}, {self.precio}, {self.existencia})"


inventario = [
    Producto("café", 45.0, 30),
    Producto("filtro", 12.0, 120),
    Producto("taza", 89.0, 45),
    Producto("prensa", 340.0, 8),
]

inventario = [p for p in inventario if p.nombre != "filtro"]

for p in inventario:
    print(f"  {p.nombre:<8}{p.precio:>8}{p.existencia:>6}")

print("Valor del inventario:", sum(p.precio * p.existencia for p in inventario))

# La operación que ya no se puede escribir mal es borrar de una lista y no de
# las otras. No hay otras: el precio y la existencia viven dentro del mismo
# objeto que el nombre, así que se van con él o se quedan con él.
```

### Ejercicio 3

```python
def parejas_desalineables(n):
    return n * (n - 1) // 2


for n in [2, 3, 4, 5, 10]:
    print(f"{n:>3} listas -> {parejas_desalineables(n):>3} parejas")

# A partir de cinco listas ya son diez parejas, y ninguna persona revisa diez
# invariantes a mano en cada cambio. Ahí es donde el estilo deja de escalar, y
# no coincide con que el programa sea largo: coincide con que los datos estén
# ligados entre sí.
```

### Ejercicio 4

```python
VALORES = ["texto", [1, 2, 3], (4, 5), {"a": 1}, {7, 8, 9}]

for funcion in [len, sorted, list]:
    print(funcion.__name__)
    for valor in VALORES:
        print(f"  {str(valor):<14}{funcion(valor)}")
    print()

print("bool sobre cada uno:", [bool(v) for v in VALORES])
print("bool sobre los vacíos:", [bool(v) for v in ["", [], (), {}, set()]])
```

`sorted`, `list` y `bool` funcionan sobre los cinco sin que tú sepas nada de su implementación. `bool`
es el más interesante: cada tipo decide qué significa estar vacío, y todos contestan la misma
pregunta.

### Ejercicio 5

```python
class Termometro:
    CERO_ABSOLUTO = -273.15

    def __init__(self, ubicacion):
        self.ubicacion = ubicacion
        self._lecturas = []

    def registrar(self, temperatura):
        if temperatura < self.CERO_ABSOLUTO:
            raise ValueError(f"Imposible: {temperatura} está bajo el cero absoluto")
        self._lecturas.append(temperatura)

    def minima(self):
        return min(self._lecturas) if self._lecturas else None


t = Termometro("laboratorio")
t.registrar(21.5)
t.registrar(19.0)
print("Mínima:", t.minima())

try:
    t.registrar(-300)
except ValueError as e:
    print("ValueError:", e)

# Y ahora por la puerta de atrás.
t._lecturas.append(-300)
print("Mínima después:", t.minima())
print("El objeto reporta una temperatura que su propio método rechazó.")
```

La validación vive en `registrar` y la lista está expuesta, así que basta con no llamar al método. La
semana 6 cierra esa puerta.

### Ejercicio 6

```python
class Vehiculo:
    def __init__(self, placa):
        self.placa = placa

    def describir(self):
        return f"Vehículo {self.placa}"


class Auto(Vehiculo):
    def describir(self):
        return f"Auto {self.placa}, cuatro ruedas"


class Motocicleta(Vehiculo):
    def describir(self):
        return f"Motocicleta {self.placa}, dos ruedas"


class Camion(Vehiculo):
    def describir(self):
        return f"Camión {self.placa}, seis ruedas"


flota = [Auto("ABC-123"), Motocicleta("XY-99"), Camion("TRK-001")]
for v in flota:
    print(v.describir())
```

El ciclo es idéntico antes y después de agregar `Camion`. Esa es la propiedad que hace útil al
polimorfismo: el código que usa los objetos no cambia cuando aparecen tipos nuevos.

### Ejercicio 7

```python
CASOS = [
    ("Calcular el IVA", "función", "entra un monto, sale otro, no recuerda nada"),
    ("Carrito de compras", "clase", "los renglones y el total viven entre llamadas"),
    ("Fecha de texto a objeto", "función", "una conversión sin memoria"),
    ("Temporizador con pausa", "clase", "el tiempo acumulado y si está corriendo"),
    ("Contar palabras", "función", "el texto entra y el número sale"),
    ("Partida de ajedrez", "clase", "el tablero, el turno y la lista de jugadas"),
]

for caso, veredicto, razon in CASOS:
    print(f"{caso:<26}{veredicto:<9}{razon}")
```

Los tres que piden clase tienen algo en común: la siguiente operación depende de las anteriores.
Pausar un temporizador solo significa algo si el objeto recuerda cuánto llevaba.

### Ejercicio 8

```python
class Calculadora:
    def __init__(self):
        self.resultado = 0
        self.historial = []

    def sumar(self, n):
        self.resultado += n
        self.historial.append(f"+ {n}")
        return self

    def multiplicar(self, n):
        self.resultado *= n
        self.historial.append(f"× {n}")
        return self


calc = Calculadora()
print("Recién creada:", vars(calc))

calc.sumar(5).multiplicar(3).sumar(2)

print("Después de tres operaciones:", vars(calc))
print("Resultado:", calc.resultado)
print("Historial:", " ".join(calc.historial))
```

Cada método devuelve `self`, y por eso las llamadas se encadenan. Eso solo tiene sentido porque hay
estado: sin un resultado guardado, encadenar no significaría nada.

### Ejercicio 9

La tabla del laboratorio, con la cafetería de la facultad como ejemplo y el módulo de pedidos.

| Pregunta | Estructurado | Orientado a objetos | Funcional |
|---|---|---|---|
| Unidad básica | `calcular_total`, `agregar_producto` | `Pedido`, `Producto`, `Cliente` | `agregar(pedido, producto) -> pedido` |
| Dónde viven los datos | Listas paralelas de productos, cantidades y precios | Cada `Pedido` guarda sus renglones y su total | En el pedido que entra y en el que sale |
| Quién los modifica | Cualquier función del archivo | Solo los métodos de `Pedido` | Nadie, cada operación devuelve un pedido nuevo |

Para la cafetería elegiría orientado a objetos, y la razón es concreta: un pedido cambia varias veces
antes de cerrarse. Se agrega un café, se quita, se aplica el descuento de estudiante, se marca como
pagado. Cada uno de esos pasos depende del anterior, y el total tiene que cuadrar con los renglones en
todo momento. Eso es estado ligado, que es exactamente el caso que el paradigma resuelve.

Si el módulo fuera el letrero del menú, que solo lee una lista de precios y la imprime, elegiría
funciones sueltas. No hay nada que recordar entre una impresión y la siguiente.

Fíjate en que la columna de POO nombra `Pedido`, `Producto` y `Cliente`, que son cosas que existen en
la cafetería y que el personal nombraría igual. Si la columna dijera `GestorDePedidos` estaría
nombrando el código en lugar del problema.
"""),

]

write(OUT / "es" / "w02.ipynb", es)
print("wrote", OUT / "es" / "w02.ipynb")
