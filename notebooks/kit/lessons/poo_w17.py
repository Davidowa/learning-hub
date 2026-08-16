"""notebooks/programacion-orientada-a-objetos/es/w17.ipynb

Source deck: ppts/python/programacion-orientada-a-objetos/es/w17.es.yaml
Source code:  ninguno nuevo. Esta sesión es de repaso, así que el cuaderno vuelve
              sobre las trampas que ya se citaron y midieron en las semanas 3 a
              16, todas con su semana de origen anotada en la celda.

Las cuatro que abren el bloque 2 son las de la diapositiva de diagnóstico, que
salen de las entregas de los dos parciales:

  Constructor de la hija sin super            -> AttributeError, semana 7
  Atributo declarado fuera de __init__        -> estado compartido, semana 6
  Archivo abierto sin with                    -> nada llega al disco, semana 12
  except sin tipo                             -> se traga el error real, semana 11

El autodiagnóstico del bloque 2 recorre las siete unidades con veinte
predicciones. Cada una imprime la semana a la que hay que volver si sorprende, y
las veinte se comprobaron corriendo el cuaderno.

Las semanas 14 y 15 no llevaron cuaderno, así que las dos preguntas de interfaz
gráfica del autodiagnóstico no ejecutan PyQt6: comprueban el mecanismo de Python
que está debajo, que es el que se evalúa en el examen. El cuaderno lo dice.

Este es el último cuaderno del curso.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from nbkit import md, code, write, REPO

OUT = REPO / "notebooks" / "programacion-orientada-a-objetos"

es = [

md("""
# Programación Orientada a Objetos · Semana 17
## Evaluación final

**COM102 · Facultad de Ingeniería · Profesor David Escobar-Castillejos**

Sesión de cierre. Qué cubre el examen final, dónde se practicó cada tema, y los cuatro errores que más
puntos costaron.

La semana pasada terminamos repartiendo el proyecto en tres piezas: el dominio, la persistencia y la
ventana. Ese reparto es también la forma de una pregunta del examen final, porque **integrador** quiere
decir que una sola pregunta puede tocar tres unidades.

Al terminar vas a poder:

1. Ubicar cada tema del examen, con la sesión en que se vio y el laboratorio en que se practicó.
2. Reconocer los cuatro errores que aparecieron en la mayoría de las entregas de los dos parciales.
3. Resolver una pregunta que toca modelado, colecciones, archivos y persistencia al mismo tiempo.
4. Autodiagnosticarte con veinte predicciones que cubren las siete unidades.
5. Presentarte sin dudas de formato, con las reglas de entrega y los materiales permitidos resueltos.

### Cómo se usa este cuaderno

Ejecuta las celdas en orden con **Shift + Enter**. Cuatro fallan a propósito y llevan un comentario que
lo dice. Son exactamente los cuatro errores que más puntos costaron en los dos parciales.

Tres de los cuatro **no lanzan ninguna excepción**, que es la mitad de lo que el semestre entero vino
enseñando: el error caro casi nunca es el que truena.

Este cuaderno no cita ningún archivo nuevo del repositorio. Vuelve sobre las trampas de las semanas 3 a
16, con la semana de origen anotada en cada celda.
"""),

md("""
---
# Bloque 1 · Alcance del examen final

Integrador quiere decir que una sola pregunta puede tocar tres unidades. No hay secciones separadas por
tema.

| Tema | Qué cubre |
|---|---|
| **T1** · Paradigma y elementos básicos | Cuándo conviene una clase, y clases, objetos, atributos, métodos, acceso y propiedades |
| **T2** · Propiedades fundamentales | Encapsulamiento, ocultamiento, reutilización, herencia, polimorfismo y abstractas |
| **T3** · Funciones, colecciones y errores | Parámetros, modularidad, recursividad, las cuatro colecciones y el manejo de excepciones |
| **T4** · Archivos, interfaces y datos | Rutas, modos, texto y binarios, ventanas con PyQt6, y tablas con `sqlite3` |

Y dónde repasar cada uno:

| Tema | Sesiones | Laboratorio de referencia |
|---|---|---|
| Clases y acceso | 3 y 4 | La cuenta bancaria de la sesión 4 |
| Herencia y polimorfismo | 7 y 8 | La jerarquía de transporte de la 7 |
| Colecciones y errores | 10 y 11 | El lector de calificaciones de la 11 |
| Archivos | 12 y 13 | El reporte desde CSV de la 12 |
| Interfaz y datos | 14 a 16 | El formulario de captura de la 15 |

## Cómo se ve una pregunta integradora

La celda de abajo es una pregunta completa, resuelta. Toca los cuatro temas y ninguna de sus piezas pasa
de quince líneas.
"""),

code("""
import csv
import sqlite3
from pathlib import Path


# ── T1 y T2: modelado, acceso y herencia
class Material:
    \"\"\"Clase base. El precio se valida en el setter y en ningún otro lado.\"\"\"

    def __init__(self, clave: str, nombre: str, precio: float) -> None:
        if not clave.strip():
            raise ValueError("la clave no puede ir vacía")
        self._clave = clave.strip()
        self.nombre = nombre
        self.precio = precio

    @property
    def precio(self) -> float:
        return self._precio

    @precio.setter
    def precio(self, valor: float) -> None:
        if valor < 0:
            raise ValueError(f"el precio no puede ser negativo, llegó {valor}")
        self._precio = float(valor)

    @property
    def clave(self) -> str:
        return self._clave

    def costo_total(self, cantidad: int) -> float:
        return self.precio * cantidad

    def __repr__(self) -> str:
        return f"{type(self).__name__}({self._clave!r}, {self.nombre!r}, {self._precio})"


class MaterialPerecedero(Material):
    \"\"\"Subclase. Encadena el constructor y sobrescribe un solo método.\"\"\"

    def __init__(self, clave, nombre, precio, merma: float = 0.05) -> None:
        super().__init__(clave, nombre, precio)
        self.merma = merma

    def costo_total(self, cantidad: int) -> float:
        return super().costo_total(cantidad) * (1 + self.merma)


CATALOGO = [
    Material("M001", "Tornillo M6", 2.50),
    MaterialPerecedero("M002", "Adhesivo epóxico", 180.00, merma=0.12),
    Material("M003", "Placa de acero", 940.00),
]

for m in CATALOGO:
    print(f"  {m.clave}  {m.nombre:<20}{m.costo_total(10):>10,.2f}")

print()
print("Polimorfismo:", [type(m).__name__ for m in CATALOGO])
print("El mismo método, dos cuentas distintas, un solo ciclo.")
"""),

code("""
# ── T3: colecciones y errores. La frontera de entrada, con todo lo demás confiando.
class CapturaInvalida(Exception):
    def __init__(self, renglon, motivo):
        self.renglon = renglon
        self.motivo = motivo
        super().__init__(f"renglón {renglon}: {motivo}")


def leer_catalogo(ruta):
    \"\"\"Devuelve objetos del dominio y una lista de problemas. No imprime nada.\"\"\"
    materiales, problemas = [], []
    try:
        with open(ruta, newline="", encoding="utf-8") as f:
            for numero, fila in enumerate(csv.DictReader(f), start=2):
                try:
                    materiales.append(Material(fila["clave"], fila["nombre"],
                                               float(fila["precio"])))
                except (KeyError, TypeError):
                    problemas.append(CapturaInvalida(numero, "faltan columnas"))
                except ValueError as e:
                    problemas.append(CapturaInvalida(numero, str(e)))
    except FileNotFoundError:
        problemas.append(CapturaInvalida(0, f"no existe {ruta}"))
    return materiales, problemas


Path("catalogo.csv").write_text(
    "clave,nombre,precio\\n"
    "M001,Tornillo M6,2.50\\n"
    "M002,Adhesivo epóxico,ciento ochenta\\n"
    "M003,Placa de acero,-940\\n"
    "M004,Perfil de aluminio,315.00\\n", encoding="utf-8")

materiales, problemas = leer_catalogo("catalogo.csv")
print("Entraron:", len(materiales), materiales)
for p in problemas:
    print("  rechazado ->", p)

print()
por_clave = {m.clave: m for m in materiales}          # diccionario: búsqueda por llave
claves = {m.clave for m in materiales}                # conjunto: pertenencia
print("Búsqueda por llave:", por_clave["M004"].nombre)
print("¿Está M002?", "M002" in claves)
print("¿Suman todas?", len(materiales) + len(problemas) == 4)
"""),

code("""
# ── T4: persistencia. Todo el SQL en una clase, y devuelve objetos del dominio.
class RepositorioMateriales:
    CREAR = ("CREATE TABLE IF NOT EXISTS Materiales ("
             "clave TEXT PRIMARY KEY, nombre TEXT NOT NULL, precio REAL NOT NULL)")

    def __init__(self, ruta):
        self.conexion = sqlite3.connect(ruta)
        self.conexion.execute(self.CREAR)
        self.conexion.commit()

    def guardar_todos(self, materiales):
        self.conexion.executemany(
            "INSERT OR REPLACE INTO Materiales VALUES (?, ?, ?)",
            [(m.clave, m.nombre, m.precio) for m in materiales])
        self.conexion.commit()

    def todos(self):
        return [Material(*fila) for fila in self.conexion.execute(
            "SELECT clave, nombre, precio FROM Materiales ORDER BY clave")]

    def cerrar(self):
        self.conexion.close()


Path("almacen.db").unlink(missing_ok=True)

repo = RepositorioMateriales("almacen.db")
repo.guardar_todos(materiales)
repo.cerrar()

repo = RepositorioMateriales("almacen.db")
recuperados = repo.todos()
repo.cerrar()

print("Recuperados de la base:", recuperados)
print("¿Son objetos del dominio?", all(isinstance(m, Material) for m in recuperados))
print("¿Sobrevivieron al cierre?", len(recuperados) == len(materiales))
print()
print("Las cuatro capas, y ninguna sabe de la de arriba:")
print("  Material              no importa csv ni sqlite3")
print("  leer_catalogo         conoce csv, no conoce sqlite3")
print("  RepositorioMateriales conoce sqlite3, no conoce csv")
print("  la ventana            no existe aquí, y nada de esto la necesita")
"""),

md("""
Tres celdas, cuatro temas, y una sola pregunta de examen.

Fíjate en lo que **no** hay. Ninguna clase del dominio importa `csv` ni `sqlite3`. Ninguna función
imprime y calcula a la vez. Ninguna revisión de datos aparece dos veces. Ningún `except` sin tipo.

Esa es la forma de una respuesta que saca los cuatro criterios de la rúbrica:

| Criterio | Peso | Dónde se ve arriba |
|---|---|---|
| Modelado | 30 % | `Material` y `MaterialPerecedero`, con el precio validado en el `setter` |
| Aplicación | 35 % | El diccionario, el conjunto, el CSV y la tabla, cada uno donde toca |
| Robustez | 20 % | `CapturaInvalida` con el renglón adentro, y tres `except` por tipo |
| Ejecución | 15 % | Las tres celdas corren y producen la salida que el enunciado pediría |

**Lo que separa un 7 de un 10 casi nunca es la sintaxis.** Es dónde pusiste la revisión y qué devuelve
cada función.
"""),

md("""
---
# Bloque 2 · Repaso de lo que salió mal

Cuatro errores concretos que aparecieron en la mayoría de las entregas de los dos parciales. Los cuatro
están corridos abajo.

## Predice antes de correr

```python
class Base:
    def __init__(self):
        self.items = []


class Hija(Base):
    def __init__(self):
        self.nombre = "x"


h = Hija()
print(len(h.items))
```

- **A.** `0`, porque la lista se creó vacía.
- **B.** `AttributeError`, `items` nunca se creó.
- **C.** `TypeError`, faltan argumentos en `Hija`.
- **D.** `1`, porque `nombre` se agregó a la lista.
"""),

code("""
# FALLA A PROPÓSITO. Primer parcial: el constructor de la hija sin super. (Semana 7)
class Base:
    def __init__(self):
        self.items = []


class Hija(Base):
    def __init__(self):
        self.nombre = "x"          # falta super().__init__()


h = Hija()

print("El objeto se construyó sin protestar:", vars(h))
print("Atributos:", len(vars(h)), "<- esperábamos 2")
print()
try:
    print(len(h.items))
except AttributeError as e:
    print("AttributeError:", e)

print()


class HijaBien(Base):
    def __init__(self):
        super().__init__()         # primero lo del padre
        self.nombre = "x"


b = HijaBien()
print("Con super():", vars(b), " items:", len(b.items))
"""),

md("""
La respuesta es **B**, y es el error número uno del semestre.

Definir `__init__` en la hija **reemplaza** al del padre, no lo agrega. Sin `super().__init__()`, el
constructor de `Base` no corre nunca y `items` no existe.

Fíjate en el orden en que se descubre. El objeto se construyó sin una sola queja, con un atributo en lugar
de dos. El error aparece más tarde, en la primera línea que lea `items`, que puede estar en otro archivo y
escrita por otra persona.

## El atributo que viven todos
"""),

code("""
# FALLA A PROPÓSITO, y no truena. Primer parcial: el atributo fuera de __init__. (Semana 6)
class Grupo:
    alumnos = []                    # <- fuera de __init__: es de la clase

    def __init__(self, clave):
        self.clave = clave

    def inscribir(self, nombre):
        self.alumnos.append(nombre)


com102 = Grupo("COM102")
com103 = Grupo("COM103")

com102.inscribir("Ana")
com102.inscribir("Luis")
com103.inscribir("Sofía")

print("COM102:", com102.alumnos)
print("COM103:", com103.alumnos)
print("¿Es la misma lista?", com102.alumnos is com103.alumnos)
print("¿Y también es la de la clase?", com102.alumnos is Grupo.alumnos)
print()
print("Estado propio de cada objeto:", vars(com102), vars(com103))
print("  <- alumnos no aparece: no es de ningún objeto")
print()


class GrupoBien:
    def __init__(self, clave):
        self.clave = clave
        self.alumnos = []           # una lista por objeto

    def inscribir(self, nombre):
        self.alumnos.append(nombre)


a, b = GrupoBien("COM102"), GrupoBien("COM103")
a.inscribir("Ana")
b.inscribir("Sofía")
print("Con la lista en __init__:", a.alumnos, b.alumnos, a.alumnos is b.alumnos)
"""),

md("""
Tres alumnos inscritos en dos grupos, y los tres aparecen en los dos.

Un nombre escrito en el cuerpo de la clase pertenece a **la clase**, no a cada objeto. Cuando ese valor es
mutable, todos los objetos escriben en el mismo. `vars(com102)` lo prueba: `alumnos` no está en el estado
del objeto porque nunca fue suyo.

Es el mismo mecanismo del valor por omisión mutable de la semana 9 y de la lista compartida de la semana
6. La regla que los cubre a los tres: **si algo va a cambiar por objeto, se asigna dentro de `__init__`.**

## Lo escrito que no llegó al disco
"""),

code("""
# FALLA A PROPÓSITO, y no truena. Segundo parcial: el archivo sin with. (Semana 12)
from pathlib import Path

ABIERTOS = []                       # el programa lo guarda para seguir escribiendo


def exportar(materiales, ruta):
    archivo = open(ruta, "w", encoding="utf-8")
    ABIERTOS.append(archivo)
    for m in materiales:
        archivo.write(f"{m.clave},{m.nombre},{m.precio}\\n")
    # falta archivo.close()


exportar(materiales, "export.csv")

print("Materiales exportados:", len(materiales))
print("Bytes en disco:", Path("export.csv").stat().st_size)
print("¿Sigue abierto?", not ABIERTOS[0].closed)
print()
print("El programa terminó bien y el archivo está vacío.")
print()

ABIERTOS[0].close()

with open("export.csv", "w", encoding="utf-8") as archivo:
    for m in materiales:
        archivo.write(f"{m.clave},{m.nombre},{m.precio}\\n")

print("Con with:", Path("export.csv").stat().st_size, "bytes")
print(Path("export.csv").read_text(encoding="utf-8"))
"""),

md("""
Cero bytes, ninguna excepción, y un programa que terminó bien.

Escribir llena un búfer en memoria. Cerrar es lo que lo vacía al disco. Sin `close`, y mientras algo siga
apuntando al archivo, lo escrito no existe fuera del proceso.

En una entrega esto se ve como "el programa corre pero el archivo de salida está vacío", que es la frase
que más veces apareció en el segundo parcial.

## El `except` que escondió el error de verdad
"""),

code("""
# FALLA A PROPÓSITO, y no truena. Segundo parcial: el except sin tipo. (Semana 11)
def promedio_de_precios(materiales):
    try:
        total = 0
        for m in materiales:
            total += m.precio
        return total / len(materiales)
    except:                              # noqa: E722
        return 0.0


print("Promedio:", promedio_de_precios(materiales))
print("Promedio de una lista vacía:", promedio_de_precios([]))
print("Promedio de una lista de cadenas:", promedio_de_precios(["M001", "M002"]))
print()
print("Los tres devolvieron un número y solo el primero significa algo.")
print()


def promedio_bien(materiales):
    if not materiales:
        raise ValueError("no se puede promediar una lista vacía")
    return sum(m.precio for m in materiales) / len(materiales)


for entrada, etiqueta in [(materiales, "catálogo"), ([], "lista vacía"),
                          (["M001"], "lista de cadenas")]:
    try:
        print(f"  {etiqueta:<18}{promedio_bien(entrada):.2f}")
    except (ValueError, AttributeError) as e:
        print(f"  {etiqueta:<18}{type(e).__name__}: {e}")
"""),

md("""
Tres llamadas, tres números, y dos de ellos son mentira.

Un `except` desnudo convierte cualquier problema en el valor por omisión. La lista vacía habría dado
`ZeroDivisionError`; la lista de cadenas, `AttributeError` porque una cadena no tiene `precio`. Los dos
son defectos y los dos salieron como `0.0`.

La versión de abajo hace lo contrario: **rechaza lo que no puede procesar y deja subir lo que no
esperaba.** Un `AttributeError` que llega a la superficie es información; convertido en cero es un dato
falso en un reporte.
"""),

md("""
---
## Autodiagnóstico de las siete unidades

Veinte predicciones, una por comportamiento que el examen puede pedirte escribir. La celda se califica
sola e imprime a qué semana volver.

Las dos de interfaz gráfica no abren ninguna ventana: comprueban el mecanismo de Python que está debajo,
que es lo que el examen evalúa. Las semanas 14 y 15 se trabajaron en clase, sobre el editor.
"""),

code("""
import csv
import sqlite3
from pathlib import Path

P = []


def p(tema, semana, obtenido, esperado):
    P.append((tema, semana, obtenido, esperado))


# ── T1 · Paradigma y elementos básicos
class Punto:
    def __init__(self, x):
        self.x = x


a, b = Punto(1), Punto(1)
p("Dos objetos con el mismo valor son el mismo", 3, a is b, False)
p("El estado vive en el objeto", 3, vars(a), {"x": 1})


class Cuenta:
    def __init__(self):
        self.__saldo = 0


p("El doble guion bajo cambia de nombre", 4,
  "_Cuenta__saldo" in vars(Cuenta()), True)


class Temp:
    def __init__(self):
        self._c = 0

    @property
    def c(self):
        return self._c

    @c.setter
    def c(self, v):
        self._c = max(-273, v)


t = Temp()
t.c = -400
p("El setter corre al asignar", 5, t.c, -273)

# ── T2 · Propiedades fundamentales
class Padre:
    def saludar(self):
        return "padre"


class Hijo(Padre):
    def saludar(self):
        return "hijo"


p("La hija tapa el método del padre", 7, Hijo().saludar(), "hijo")
p("Y sigue siendo un Padre", 7, isinstance(Hijo(), Padre), True)
p("type() no es isinstance()", 7, type(Hijo()) is Padre, False)

from abc import ABC, abstractmethod


class Figura(ABC):
    @abstractmethod
    def area(self):
        ...


try:
    Figura()
    abstracta = "se construyó"
except TypeError:
    abstracta = "TypeError"
p("Una clase abstracta no se instancia", 8, abstracta, "TypeError")

# ── T3 · Funciones, colecciones y errores
def agregar(x, lista=[]):
    lista.append(x)
    return lista


agregar(1)
p("El valor por omisión se evalúa una vez", 9, len(agregar(2)), 2)

lista = [1, 2, 3]
alias = lista
alias.append(4)
p("El igual no copia, comparte", 10, len(lista), 4)

p("Un conjunto no guarda repetidos", 10, len({1, 1, 2, 2, 3}), 3)
p("zip corta con la más corta", 10, len(list(zip("abcde", "xyz"))), 3)

corrio = []


def leer():
    try:
        return 7
    finally:
        corrio.append("finally")


leer()
p("finally corre con un return esperando", 11, corrio, ["finally"])


def clasificar():
    try:
        raise FileNotFoundError()
    except OSError:
        return "general"
    except FileNotFoundError:
        return "específico"


p("El except general tapa al específico", 11, clasificar(), "general")

# ── T4 · Archivos, interfaces y datos
ruta = Path("final.txt")
ruta.write_text("primera", encoding="utf-8")
f = open(ruta, "w", encoding="utf-8")
p("El modo w vacía al abrir", 12, ruta.stat().st_size, 0)
f.close()

Path("final.csv").write_text("n,v\\nAna,9.1\\n", encoding="utf-8")
with open("final.csv", newline="", encoding="utf-8") as f:
    fila = next(csv.DictReader(f))
p("Un CSV no guarda tipos", 12, type(fila["v"]).__name__, "str")

Path("final.bin").write_bytes(b"ABCDEFGH")
with open("final.bin", "rb") as f:
    f.seek(3)
    leido = f.read(2)
p("Las posiciones se cuentan desde cero", 13, leido, b"DE")


class Boton:
    \"\"\"Sin PyQt6: el mecanismo de Python que hay debajo de connect().\"\"\"

    def __init__(self):
        self.slot = None

    def connect(self, funcion):
        self.slot = funcion


def al_hacer_clic():
    return "clic"


boton = Boton()
boton.connect(al_hacer_clic())            # con paréntesis: se llamó ya
p("connect con paréntesis guarda el resultado", 14, boton.slot, "clic")
boton.connect(al_hacer_clic)              # sin paréntesis: se guarda la función
p("connect sin paréntesis guarda la función", 14, callable(boton.slot), True)

Path("final.db").unlink(missing_ok=True)
c = sqlite3.connect("final.db")
c.execute("CREATE TABLE T (id INTEGER PRIMARY KEY)")
c.commit()
c.close()
c = sqlite3.connect("final.db")
c.execute("INSERT INTO T VALUES (1)")
c.close()
c = sqlite3.connect("final.db")
n = c.execute("SELECT COUNT(*) FROM T").fetchone()
c.close()
p("Cerrar sin commit descarta", 16, n, (0,))

aciertos = 0
print(f"{'#':<4}{'sem':<6}{'comportamiento':<48}{'resultado'}")
for i, (tema, semana, obtenido, esperado) in enumerate(P, start=1):
    ok = obtenido == esperado
    aciertos += ok
    marca = "" if ok else f"   <- se esperaba {esperado!r}"
    print(f"{i:<4}{semana:<6}{tema:<48}{obtenido!r}{marca}")

print()
print(f"Predicciones que coincidieron: {aciertos} de {len(P)}")
print("La columna 'sem' dice a qué cuaderno volver por cada una que te sorprendió.")
"""),

md("""
Veinte comportamientos, siete unidades, y ninguno se contesta con una definición.

El examen final funciona igual. **Ninguna pregunta pide que expliques qué es el encapsulamiento**; piden
que escribas una clase donde el precio no pueda quedar negativo, que es lo mismo dicho de la única manera
que se puede calificar.

Las dos preguntas de la semana 14 usan una clase `Boton` escrita aquí en lugar de `QPushButton`, y
comprueban exactamente lo que el examen evalúa: pasar una función sin paréntesis guarda la función; con
paréntesis la llama en ese instante y guarda lo que devolvió. El `TypeError` real aparece después, cuando
Qt intenta llamar a lo que le dieron.
"""),

md("""
---
## Cómo se estudia esto

**Ninguna pregunta pide una definición.** Todas piden escribir código que corra, así que la única
preparación que sirve es volver a resolver los laboratorios sin ver la solución.

**Qué practicar.** Un laboratorio por unidad, resuelto desde cero y sin abrir el archivo de la solución.

**Qué revisar.** Las diapositivas de diagnóstico y los cuatro errores de cada una. Son los del examen.

**Qué no hacer.** Releer las diapositivas de concepto. Se entienden al leerlas y no se retienen al
escribir.

## Lo que hay que saber antes de sentarse

| | |
|---|---|
| **Formato** | A máquina, un archivo `.py` por pregunta, con el nombre que indique el enunciado |
| **Materiales** | El repositorio del curso y la documentación oficial de Python, abiertos |
| **Sin ayuda de terceros** | Ni personas ni asistentes. Aplica el Código de Honor de la Universidad. |
| **Entrega** | Por Blackboard, dentro del horario del examen. No se aceptan entregas por correo. |

Y los pesos, para que sepas dónde invertir el tiempo:

| Criterio | Peso |
|---|---|
| Modelado | 30 % |
| Aplicación | 35 % |
| Robustez | 20 % |
| Ejecución | 15 % |

**La ejecución vale quince por ciento y condiciona los otros ochenta y cinco.** Un archivo que no corre no
se puede evaluar en modelado. Los últimos cinco minutos se usan en correr todo otra vez desde cero, no en
mejorar una respuesta.
"""),

md("""
---
# Ejercicios

Un simulacro de examen final. Cuatro preguntas, con los pesos de la rúbrica de verdad.

Las soluciones están hasta abajo del cuaderno.

### Pregunta 1 · Modelado (30 %)

Modela un `Vehiculo` con placa, marca y kilometraje, y un `VehiculoElectrico` que herede de él y agregue
la autonomía en kilómetros.

El kilometraje no puede bajar nunca, y esa regla vive en el `setter`. La placa se lee y no se escribe.
`VehiculoElectrico` sobrescribe un método de costo por kilómetro y encadena con `super()`.

Construye tres objetos, con al menos uno de cada tipo, y demuestra con un ciclo que el mismo método da
cuentas distintas.

### Pregunta 2 · Aplicación (35 %)

Te dan un CSV con `placa`, `fecha` y `kilometros` de cada viaje. Escribe funciones que:

1. Lean el archivo y devuelvan objetos, no diccionarios.
2. Agrupen los kilómetros por placa con un diccionario acumulador.
3. Devuelvan el conjunto de placas que aparecen.
4. Devuelvan la placa con más kilómetros.

Ninguna función imprime. Ninguna pasa de quince líneas.

### Pregunta 3 · Robustez (20 %)

Define `ViajeInvalido(Exception)` que guarde el número de renglón y el motivo. Lánzala desde la lectura
cuando el kilometraje no sea un número o sea negativo.

El programa tiene que terminar bien con un CSV que no existe, con uno vacío, con uno al que le falte una
columna, y con uno que traiga tres renglones malos de diez.

### Pregunta 4 · Persistencia y ejecución (15 %)

Escribe la clase de acceso a datos que guarda los vehículos en `sqlite3` y los recupera como objetos del
dominio. Todo el SQL vive ahí.

Demuestra que los datos sobreviven cerrando la conexión y volviéndola a abrir. Entrega un bloque
`if __name__ == "__main__":` que corra el flujo completo de principio a fin.
"""),

md("""
---
## Tres ideas para llevarse del semestre

**La clase describe, el objeto recuerda.** Todo lo demás del curso se apoya en esa distinción, incluida la
mitad de aplicación: un archivo, una conexión y una ventana son objetos con estado y con ciclo de vida.

**Lo que se abre se cierra.** Un archivo, una conexión y una ventana tienen el mismo ciclo de vida y la
misma trampa. El `with` lo resuelve para los dos primeros; el tercero se cierra solo cuando el ciclo de
eventos termina.

**El código que se puede probar dura.** Sacar la lógica de los slots, de los ciclos y de los `print` es lo
que permite corregirla sin adivinar. Es la misma decisión desde la semana 9 hasta la 16: qué recibe una
función, qué devuelve, y qué deja modificado fuera de sí misma.

Con esto cierra COM102. El repositorio del curso queda abierto, y los diecinueve cuadernos de tu idioma
siguen corriendo enteros en Colab sin instalar nada.

Lo que sigue son estructuras de datos: listas ligadas, árboles, grafos y el costo de cada operación. Todo
esto es la base. La semana 10 ya midió por qué agregar al final de una lista es barato y al principio no,
y esa pregunta, hecha en serio, es la materia completa.
"""),

md("""
---
# Soluciones

### Pregunta 1

```python
class Vehiculo:
    def __init__(self, placa: str, marca: str, kilometraje: float = 0.0) -> None:
        if not placa.strip():
            raise ValueError("la placa no puede ir vacía")
        self._placa = placa.strip().upper()
        self.marca = marca
        self._kilometraje = 0.0
        self.kilometraje = kilometraje

    @property
    def placa(self) -> str:
        return self._placa

    @property
    def kilometraje(self) -> float:
        return self._kilometraje

    @kilometraje.setter
    def kilometraje(self, valor: float) -> None:
        if valor < self._kilometraje:
            raise ValueError(f"el kilometraje no puede bajar de "
                             f"{self._kilometraje} a {valor}")
        self._kilometraje = float(valor)

    def costo_por_km(self) -> float:
        return 3.80

    def __repr__(self) -> str:
        return f"{type(self).__name__}({self._placa!r}, {self.marca!r}, {self._kilometraje})"


class VehiculoElectrico(Vehiculo):
    def __init__(self, placa, marca, kilometraje=0.0, autonomia_km=320) -> None:
        super().__init__(placa, marca, kilometraje)
        self.autonomia_km = autonomia_km

    def costo_por_km(self) -> float:
        return super().costo_por_km() * 0.35


FLOTA = [Vehiculo("ABC123", "Nissan", 41_000),
         VehiculoElectrico("XYZ789", "BYD", 12_400, autonomia_km=400),
         Vehiculo("JKL456", "Toyota", 88_200)]

for v in FLOTA:
    print(f"{v.placa}  {type(v).__name__:<18}{v.costo_por_km():.2f} por km")

try:
    FLOTA[0].kilometraje = 100
except ValueError as e:
    print("ValueError:", e)
```

### Pregunta 2

```python
import csv


class Viaje:
    def __init__(self, placa, fecha, kilometros):
        self.placa = placa
        self.fecha = fecha
        self.kilometros = kilometros

    def __repr__(self):
        return f"Viaje({self.placa!r}, {self.fecha!r}, {self.kilometros})"


def leer_viajes(ruta):
    with open(ruta, newline="", encoding="utf-8") as f:
        return [Viaje(r["placa"], r["fecha"], float(r["kilometros"]))
                for r in csv.DictReader(f)]


def km_por_placa(viajes):
    acumulado = {}
    for v in viajes:
        acumulado[v.placa] = acumulado.get(v.placa, 0.0) + v.kilometros
    return acumulado


def placas(viajes):
    return {v.placa for v in viajes}


def la_que_mas_recorrio(viajes):
    acumulado = km_por_placa(viajes)
    return max(acumulado, key=acumulado.get)
```

### Pregunta 3

```python
import csv
from pathlib import Path

COLUMNAS = ["placa", "fecha", "kilometros"]


class ViajeInvalido(Exception):
    def __init__(self, renglon, motivo):
        self.renglon = renglon
        self.motivo = motivo
        super().__init__(f"renglón {renglon}: {motivo}")


def leer_viajes(ruta):
    \"\"\"Frontera de entrada. Devuelve viajes buenos y problemas, y no imprime.\"\"\"
    viajes, problemas = [], []
    try:
        with open(ruta, newline="", encoding="utf-8") as f:
            lector = csv.DictReader(f)
            if lector.fieldnames is None:
                return [], [ViajeInvalido(0, "el archivo está vacío")]
            faltan = [c for c in COLUMNAS if c not in lector.fieldnames]
            if faltan:
                return [], [ViajeInvalido(0, f"faltan columnas: {faltan}")]
            for numero, fila in enumerate(lector, start=2):
                try:
                    km = float(fila["kilometros"])
                except (TypeError, ValueError):
                    problemas.append(ViajeInvalido(
                        numero, f"{fila.get('kilometros')!r} no es un número"))
                    continue
                if km < 0:
                    problemas.append(ViajeInvalido(numero, f"{km} es negativo"))
                    continue
                viajes.append(Viaje(fila["placa"], fila["fecha"], km))
    except FileNotFoundError:
        problemas.append(ViajeInvalido(0, f"no existe {ruta}"))
    return viajes, problemas
```

### Pregunta 4

```python
import sqlite3
from pathlib import Path


class RepositorioVehiculos:
    CREAR = ("CREATE TABLE IF NOT EXISTS Vehiculos ("
             "placa TEXT PRIMARY KEY, marca TEXT NOT NULL, "
             "kilometraje REAL NOT NULL, tipo TEXT NOT NULL, "
             "autonomia_km INTEGER)")

    def __init__(self, ruta):
        self.conexion = sqlite3.connect(ruta)
        self.conexion.execute(self.CREAR)
        self.conexion.commit()

    def guardar(self, vehiculo):
        self.conexion.execute(
            "INSERT OR REPLACE INTO Vehiculos VALUES (?, ?, ?, ?, ?)",
            (vehiculo.placa, vehiculo.marca, vehiculo.kilometraje,
             type(vehiculo).__name__,
             getattr(vehiculo, "autonomia_km", None)))
        self.conexion.commit()

    def todos(self):
        vehiculos = []
        for placa, marca, km, tipo, autonomia in self.conexion.execute(
                "SELECT placa, marca, kilometraje, tipo, autonomia_km "
                "FROM Vehiculos ORDER BY placa"):
            if tipo == "VehiculoElectrico":
                vehiculos.append(VehiculoElectrico(placa, marca, km, autonomia))
            else:
                vehiculos.append(Vehiculo(placa, marca, km))
        return vehiculos

    def cerrar(self):
        self.conexion.close()


if __name__ == "__main__":
    Path("flota.db").unlink(missing_ok=True)
    Path("viajes.csv").write_text(
        "placa,fecha,kilometros\\n"
        "ABC123,2026-03-01,142.5\\n"
        "XYZ789,2026-03-01,88.0\\n"
        "ABC123,2026-03-02,doscientos\\n"
        "JKL456,2026-03-02,-30\\n"
        "XYZ789,2026-03-03,210.0\\n", encoding="utf-8")

    viajes, problemas = leer_viajes("viajes.csv")
    print(f"{len(viajes)} viajes buenos, {len(problemas)} rechazados")
    for p in problemas:
        print("  ", p)

    print("Kilómetros por placa:", km_por_placa(viajes))
    print("La que más recorrió: ", la_que_mas_recorrio(viajes))

    repo = RepositorioVehiculos("flota.db")
    for v in FLOTA:
        repo.guardar(v)
    repo.cerrar()

    repo = RepositorioVehiculos("flota.db")
    recuperados = repo.todos()
    repo.cerrar()

    print("Recuperados:", recuperados)
    print("Con su tipo:", [type(v).__name__ for v in recuperados])

    _, problemas = leer_viajes("no_existe.csv")
    print("Archivo faltante:", problemas[0])
```

Cuatro decisiones que valen los cuatro criterios.

**El kilometraje se valida en el `setter` y en ningún otro lado.** Por eso `__init__` asigna a
`self.kilometraje` en lugar de a `self._kilometraje`: la regla corre también al construir.

**`leer_viajes` devuelve dos listas y no imprime.** Los viajes buenos y los problemas salen juntos, así
que quien llama decide qué hacer con cada uno, y la función se prueba con un CSV escrito a mano.

**El repositorio guarda el tipo y lo usa para reconstruir la subclase correcta.** Una tabla no sabe de
herencia, así que la columna `tipo` es lo que permite que `todos()` devuelva `VehiculoElectrico` donde
toca.

**El bloque `if __name__ == "__main__":` corre el flujo completo.** Es lo que se califica en el quince por
ciento de ejecución, y es lo primero que hay que comprobar antes de entregar.
"""),

]

write(OUT / "es" / "w17.ipynb", es)
print("wrote", OUT / "es" / "w17.ipynb")
