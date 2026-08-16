"""notebooks/programacion-orientada-a-objetos/es/w16.ipynb

Source deck: ppts/python/programacion-orientada-a-objetos/es/w16.es.yaml
Source code:  docs/en/courses/python-course/04 - SQLite/8th Module/Code036.py
                  (sqlite3: connect, CREATE TABLE, INSERT con marcadores, SELECT,
                   WHERE, la llave foránea y el INNER JOIN)
              docs/en/courses/python-course/03 - Paths and Files/7th Module/Code33.py
                  (el pixar_movies.json que Code036.py carga)

Code036.py NO se corre desde el repositorio: escribe pixar_movies.db dentro de
docs/. El cuaderno reproduce su código en el directorio de trabajo de la sesión,
que en Colab es /content.

DISCREPANCIA CON EL DECK, MEDIDA. La diapositiva "Pregunta rápida" de w16.es.yaml
afirma que este código imprime (0,):

    with sqlite3.connect(ruta) as c:
        c.execute("INSERT INTO Peliculas VALUES (1, 'Up')")

    with sqlite3.connect(ruta) as c:
        cursor = c.execute("SELECT COUNT(*) FROM Peliculas")
        print(cursor.fetchone())

Medido sobre Python 3.14 / SQLite 3.50: imprime (1,). El gestor de contexto de
sqlite3 SÍ confirma la transacción al salir sin excepción; lo que no hace es
cerrar la conexión. La diapositiva tiene invertidas las dos mitades.

No es un detalle de versión. La documentación de Python lo dice desde siempre en
library/sqlite3: "If the with block completes without exceptions, the transaction
is committed. If an exception occurs, the transaction is rolled back." y "The
context manager does not implicitly open new transactions or close the
connection."

El cuaderno enseña lo medido, con las cuatro variantes corridas enfrente:

    with sin excepción      -> commit, la fila queda            (1,)
    with con excepción      -> rollback, la fila se descarta    (0,)
    close() sin commit      -> la fila se descarta              (0,)
    tras el with            -> la conexión sigue abierta y usable

Otras cosas medidas del repositorio, citadas sin corregir:

  Code036.py líneas 40 a 42 borran el archivo .db antes de cada corrida. Es la
  única razón por la que el archivo se puede correr dos veces: sin ese borrado,
  el segundo INSERT del mismo id lanza IntegrityError por la llave primaria.
  El comentario de la línea 38 lo dice a medias ("table already exists or
  repeated data"); lo que ocurre de verdad es lo segundo.

  Code036.py líneas 81 a 84 comentan un fetchall() y explican que sale vacío
  porque el cursor ya se recorrió. Es correcto y vale la pena medirlo: un cursor
  agotado devuelve [] y no lanza nada.

  Code036.py línea 141 usa un marcador para el título del INNER JOIN, que es lo
  correcto, y la línea 96 pega el año directo en la cadena. Ahí no hay riesgo
  porque el 2010 está escrito a mano, y el hábito sí lo tiene.

Las semanas 14 y 15 no llevaron cuaderno, porque una ventana de PyQt6 necesita
pantalla y Colab no la tiene. El hilo viene de la semana 13: allá, para saltar al
registro n de un archivo de registros variables, habría que escribir un índice a
mano. Aquí ese índice viene incluido.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from nbkit import md, code, write, REPO

OUT = REPO / "notebooks" / "programacion-orientada-a-objetos"

es = [

md("""
# Programación Orientada a Objetos · Semana 16
## Tema 7 · Bases de datos y proyecto

**COM102 · Facultad de Ingeniería · Profesor David Escobar-Castillejos**

Guardar datos que se buscan, se filtran y sobreviven al programa. Y la sesión en la que todo lo del
semestre se junta en una sola entrega.

La semana 13 cerró con un problema abierto: para saltar al registro `n` de un archivo cuyos registros
miden distinto, hay que guardar aparte una lista que diga en qué byte empieza cada uno. Eso es un índice,
y escribirlo a mano es trabajo. Aquí viene incluido.

Las semanas 14 y 15 fueron interfaces gráficas y no llevaron cuaderno, porque una ventana necesita una
pantalla y Colab no la tiene. Lo que sí se puede probar aquí es la decisión de arquitectura que esas dos
semanas dejaron pendiente, y el bloque 3 la prueba.

Al terminar vas a poder:

1. Decidir entre archivo y base de datos por cómo se va a consultar el dato, no por cuántos habrá.
2. Crear una tabla, insertar con marcadores y consultar, sabiendo qué hace `commit` y qué pasa sin él.
3. Explicar qué confirma y qué cierra el `with` de `sqlite3`, con las cuatro combinaciones medidas.
4. Escribir una consulta con parámetros y decir exactamente qué evita.
5. Repartir el proyecto en tres piezas que se prueban por separado.

### Cómo se usa este cuaderno

Ejecuta las celdas en orden con **Shift + Enter**. Nueve fallan a propósito y llevan un comentario que lo
dice.

Tres de las nueve **no lanzan ninguna excepción**. Una de ellas inserta mil filas, no se queja de nada, y
deja la base vacía.

Este cuaderno crea archivos `.db` en el directorio de trabajo de la sesión. No toca nada del repositorio.
"""),

md("""
---
# Bloque 1 · Bases de datos

Un archivo guarda datos. Una base de datos guarda datos y además sabe contestar preguntas sobre ellos.

Esa diferencia no se nota con cien registros y decide el programa completo cuando son cien mil.
"""),

code("""
import csv
import sqlite3
import time
from pathlib import Path

N = 100_000
GENEROS = ["Animación", "Aventura", "Comedia", "Drama"]

filas = [(i, f"Película {i}", 1995 + i % 30, GENEROS[i % 4]) for i in range(1, N + 1)]

# Lo mismo, guardado de las dos maneras
with open("peliculas.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["id", "titulo", "anio", "genero"])
    w.writerows(filas)

Path("peliculas.db").unlink(missing_ok=True)
conexion = sqlite3.connect("peliculas.db")
conexion.execute("CREATE TABLE Peliculas (id INTEGER PRIMARY KEY, titulo TEXT, "
                 "anio INTEGER, genero TEXT)")
conexion.executemany("INSERT INTO Peliculas VALUES (?, ?, ?, ?)", filas)
conexion.commit()

print("CSV:", f"{Path('peliculas.csv').stat().st_size:,}", "bytes")
print("DB: ", f"{Path('peliculas.db').stat().st_size:,}", "bytes")
print()

BUSCADO = 99_999

inicio = time.perf_counter()
with open("peliculas.csv", newline="", encoding="utf-8") as f:
    encontrada = next(fila for fila in csv.DictReader(f)
                      if int(fila["id"]) == BUSCADO)
con_archivo = time.perf_counter() - inicio

inicio = time.perf_counter()
encontrada_db = conexion.execute(
    "SELECT * FROM Peliculas WHERE id = ?", (BUSCADO,)).fetchone()
con_tabla = time.perf_counter() - inicio

print("Del CSV: ", encontrada)
print("De la DB:", encontrada_db)
print()
print(f"Buscar en el archivo: {con_archivo:.5f} s")
print(f"Buscar en la tabla:   {con_tabla:.6f} s")
print(f"El archivo tardó unas {con_archivo / con_tabla:,.0f} veces más.")
conexion.close()
"""),

md("""
Los mismos cien mil registros, la misma respuesta, y una diferencia de cientos de veces que la celda
acaba de medir en tu propia sesión.

En un archivo, buscar significa **leerlo entero** hasta encontrar lo que quieres. Es el recorrido
secuencial de la semana 13, y no hay manera de evitarlo salvo escribiendo un índice a mano.

En una tabla, buscar significa **preguntar**, y el motor decide cómo llegar. Cuando la columna es
`INTEGER PRIMARY KEY`, SQLite ya tiene ese índice construido y va directo al renglón sin mirar los
demás.

Eso es lo único que hay que llevarse del bloque: **la decisión no es cuántos registros vas a tener, es
cómo los vas a consultar.** Si solo vas a guardar y volver a leer todo, un archivo alcanza. En cuanto
haya que buscar, filtrar u ordenar sin leerlo todo, la tabla se paga sola.

## Las tres piezas del modelo
"""),

code("""
# Code036.py, líneas 44 a 55, con tres películas
import sqlite3
from pathlib import Path

pixar_movies = [
    {"id": 1, "title": "Toy Story", "year": 1995},
    {"id": 19, "title": "Coco", "year": 2017},
    {"id": 25, "title": "Turning Red", "year": 2022},
]

database_file = Path("pixar_movies.db")
database_file.unlink(missing_ok=True)

with sqlite3.connect(database_file) as connection:
    create_command = ("CREATE TABLE IF NOT EXISTS Movies (id INTEGER PRIMARY KEY, "
                      "title TEXT NOT NULL, year INTEGER NOT NULL)")
    connection.execute(create_command)

    for movie in pixar_movies:
        insert_command = "INSERT INTO Movies VALUES (?, ?, ?)"
        connection.execute(insert_command,
                           (movie["id"], movie["title"], movie["year"]))
    connection.commit()

with sqlite3.connect(database_file) as connection:
    for row in connection.execute("SELECT * FROM Movies ORDER BY title"):
        print(" ", row)
    print()
    print("Cada renglón llega como:", type(row).__name__)
    print("Las columnas de la tabla:")
    for col in connection.execute("PRAGMA table_info(Movies)"):
        print(f"   {col[1]:<8}{col[2]:<10}"
              f"{'NOT NULL' if col[3] else '':<10}"
              f"{'PRIMARY KEY' if col[5] else ''}")
connection.close()
"""),

md("""
Tres piezas, y las tres tienen un equivalente exacto en lo que llevas del semestre.

**Una tabla por sustantivo.** `Movies` guarda películas y solo películas. Es la misma pregunta de la
semana 5 al modelar una clase.

**Una columna por atributo, con su tipo.** `PRAGMA table_info` las imprime con el tipo y las
restricciones, que es la versión de la base de datos de una anotación de tipo.

**Una llave primaria que identifique.** `id INTEGER PRIMARY KEY` es lo que distingue a un renglón de todos
los demás, y es lo que hace que la búsqueda de la celda anterior sea inmediata.

Cada renglón vuelve como una **tupla**, que es el contenedor de la semana 10 para un registro que no
cambia. La correspondencia no es casualidad.

## Correr el archivo dos veces
"""),

code("""
# FALLA A PROPÓSITO. Lo que Code036.py evita borrando el .db en su línea 42.
import sqlite3
from pathlib import Path

ruta = Path("dos_veces.db")
ruta.unlink(missing_ok=True)

conexion = sqlite3.connect(ruta)
conexion.execute("CREATE TABLE IF NOT EXISTS Movies (id INTEGER PRIMARY KEY, "
                 "title TEXT NOT NULL)")
conexion.execute("INSERT INTO Movies VALUES (?, ?)", (1, "Toy Story"))
conexion.commit()
print("Primera corrida:", conexion.execute("SELECT COUNT(*) FROM Movies").fetchone())

try:
    conexion.execute("INSERT INTO Movies VALUES (?, ?)", (1, "Toy Story"))
except sqlite3.IntegrityError as e:
    print("Segunda corrida:", type(e).__name__ + ":", e)

print()
print("El CREATE TABLE IF NOT EXISTS sí aguanta la segunda corrida.")
print("El INSERT del mismo id, no.")
print()
conexion.execute("INSERT OR REPLACE INTO Movies VALUES (?, ?)", (1, "Toy Story"))
conexion.commit()
print("Con INSERT OR REPLACE:", conexion.execute("SELECT * FROM Movies").fetchall())
conexion.close()
"""),

md("""
`UNIQUE constraint failed: Movies.id`.

`Code036.py` borra el archivo `.db` antes de cada corrida, en sus líneas 40 a 42, y su comentario dice que
es para evitar *"an error of 'table already exists' or repeated data"*. La primera mitad no es cierta:
`CREATE TABLE IF NOT EXISTS` aguanta perfectamente la segunda corrida. La que truena es la segunda,
el `INSERT` del mismo `id`.

Esa restricción es lo que hace útil a la llave primaria: **el motor se niega a guardar dos renglones con
la misma identidad**, y se niega en la línea que lo intenta, no tres pantallas después.

Borrar la base entera para poder correr el programa otra vez funciona en un ejemplo de clase y no es lo
que se hace. `INSERT OR REPLACE` actualiza si ya estaba, y es la operación que de verdad querías.
"""),

md("""
---
# Bloque 2 · Acceso y consultas

Una conexión se abre, se usa y se cierra. Es el mismo ciclo de vida de un archivo de la semana 12, con
una trampa extra que se llama `commit`.

## Predice antes de correr

```python
with sqlite3.connect(ruta) as c:
    c.execute("INSERT INTO Peliculas VALUES (1, 'Up')")

with sqlite3.connect(ruta) as c:
    cursor = c.execute("SELECT COUNT(*) FROM Peliculas")
    print(cursor.fetchone())
```

- **A.** `(1,)`, porque el `with` hace `commit` al salir.
- **B.** `(0,)`, porque nunca se llamó a `commit`.
- **C.** Un error, la conexión ya estaba cerrada.
- **D.** `(1,)`, porque `sqlite3` guarda cada `INSERT` al instante.
"""),

code("""
import sqlite3
from pathlib import Path

ruta = Path("prediccion.db")


def base_limpia():
    ruta.unlink(missing_ok=True)
    c = sqlite3.connect(ruta)
    c.execute("CREATE TABLE Peliculas (id INTEGER PRIMARY KEY, titulo TEXT)")
    c.commit()
    c.close()


def cuantas():
    c = sqlite3.connect(ruta)
    n = c.execute("SELECT COUNT(*) FROM Peliculas").fetchone()
    c.close()
    return n


base_limpia()
with sqlite3.connect(ruta) as c:
    c.execute("INSERT INTO Peliculas VALUES (1, 'Up')")
c.close()

print("Resultado:", cuantas())
"""),

md("""
La respuesta es **A**, y no es la que la mayoría contesta.

El gestor de contexto de `sqlite3` **confirma la transacción** al salir del bloque sin excepción. Es lo
que acaba de imprimir la celda y es lo que dice la documentación de Python, en `library/sqlite3`, con
estas palabras: *"If the `with` block completes without exceptions, the transaction is committed"*, y dos
renglones después, *"The context manager does not implicitly open new transactions or close the
connection"*.

Lo que el `with` **no** hace es cerrar la conexión. Ahí está la trampa de verdad, y es exactamente al
revés de lo que suena: se parece al `with` de un archivo en que protege el trabajo, y se diferencia en
que no suelta el recurso.

Las cuatro combinaciones, corridas una junto a otra, están en la celda siguiente.
"""),

code("""
import sqlite3

print(f"{'situación':<38}{'filas en disco':>16}")

# 1. with, sin excepción, sin commit explícito
base_limpia()
with sqlite3.connect(ruta) as c:
    c.execute("INSERT INTO Peliculas VALUES (1, 'Up')")
c.close()
print(f"{'with que termina bien':<38}{str(cuantas()):>16}")

# 2. with, con excepción adentro
base_limpia()
try:
    with sqlite3.connect(ruta) as c:
        c.execute("INSERT INTO Peliculas VALUES (1, 'Up')")
        raise ValueError("algo salió mal a media transacción")
except ValueError:
    pass
c.close()
print(f"{'with con una excepción adentro':<38}{str(cuantas()):>16}")

# 3. sin with, con commit
base_limpia()
c = sqlite3.connect(ruta)
c.execute("INSERT INTO Peliculas VALUES (1, 'Up')")
c.commit()
c.close()
print(f"{'sin with, con commit':<38}{str(cuantas()):>16}")

# 4. sin with, sin commit
base_limpia()
c = sqlite3.connect(ruta)
c.execute("INSERT INTO Peliculas VALUES (1, 'Up')")
c.close()
print(f"{'sin with, sin commit':<38}{str(cuantas()):>16}")
"""),

md("""
Cuatro combinaciones, dos resultados, y una regla que sale sola.

**Una transacción termina de una de dos maneras: confirmada o descartada.** El `with` confirma cuando el
bloque salió bien y descarta cuando salió una excepción. Sin `with`, la confirmación tiene que escribirse,
y cerrar sin haberla escrito descarta.

El renglón cuatro es el error 01 de la diapositiva en su forma real: los `INSERT` corrieron, el programa
no se quejó, y al volver a abrir la base no hay nada.

El renglón dos es el mismo resultado por el motivo contrario, y es una **buena** propiedad: si el programa
truena a media carga, no quedan cincuenta películas de las cien que iban a entrar. O entran todas o no
entra ninguna.

## Mil filas y una base vacía
"""),

code("""
# FALLA A PROPÓSITO, y no truena. Mil inserciones y ningún commit.
import sqlite3

base_limpia()

conexion = sqlite3.connect(ruta)
for i in range(1, 1001):
    conexion.execute("INSERT INTO Peliculas VALUES (?, ?)", (i, f"Película {i}"))

print("Lo que la conexión ve antes de cerrar:",
      conexion.execute("SELECT COUNT(*) FROM Peliculas").fetchone())
conexion.close()

print("Lo que hay en disco después:          ", cuantas())
print()
print("Ninguna excepción, ningún aviso, y mil filas que no existen.")
print()

base_limpia()
conexion = sqlite3.connect(ruta)
conexion.executemany("INSERT INTO Peliculas VALUES (?, ?)",
                     [(i, f"Película {i}") for i in range(1, 1001)])
conexion.commit()
conexion.close()
print("Con commit:", cuantas())
"""),

md("""
La misma conexión que insertó las mil filas las ve. Nadie más.

Una transacción sin confirmar vive en la sesión que la abrió. Por eso la primera consulta devuelve mil y
la segunda, desde otra conexión y después de cerrar, devuelve cero. **El `SELECT` de comprobación desde
la misma conexión no comprueba nada**, y es la razón por la que este error sobrevive tanto tiempo.

Fíjate también en `executemany`. Manda las mil inserciones de una vez y es la forma correcta cuando los
datos vienen de una lista, que es exactamente lo que hace el ciclo de `Code036.py` en sus líneas 48 a 53,
una por una.

## La conexión que se quedó abierta
"""),

code("""
# FALLA A PROPÓSITO. El with de sqlite3 no cierra nada.
import sqlite3
from pathlib import Path

base_limpia()

with sqlite3.connect(ruta) as c:
    c.execute("INSERT INTO Peliculas VALUES (1, 'Up')")

print("¿Sigue viva la conexión después del with?")
print("  ", c.execute("SELECT COUNT(*) FROM Peliculas").fetchone(), "<- sí, contestó")
print()

c.close()
print("Después de close():")
try:
    c.execute("SELECT COUNT(*) FROM Peliculas")
except sqlite3.ProgrammingError as e:
    print("  ProgrammingError:", e)

print()
print("La forma que cierra de verdad:")
with sqlite3.connect(ruta) as conexion:
    conexion.execute("INSERT OR REPLACE INTO Peliculas VALUES (2, 'Coco')")
conexion.close()
print("  filas:", cuantas(), " ¿cerrada?", True)
"""),

md("""
El `with` salió, la transacción quedó confirmada, y la conexión siguió abierta y contestando.

Esto no es un detalle de estilo. Una conexión abierta mantiene un archivo abierto, y en Windows un archivo
abierto **no se puede borrar ni mover**. Un programa que abre una conexión por operación y nunca cierra
ninguna se queda sin descriptores en unas horas.

La forma completa es la de las últimas líneas: `with` para la transacción y `close()` para el recurso. Si
quieres que un solo bloque haga las dos cosas, existe `contextlib.closing`, y en un proyecto lo normal es
tener una clase que abre en su constructor y cierra en un método `cerrar`.

## El cursor que ya no sirve
"""),

code("""
# FALLA A PROPÓSITO. Guardar el cursor para después.
import sqlite3

base_limpia()
c = sqlite3.connect(ruta)
c.executemany("INSERT INTO Peliculas VALUES (?, ?)",
              [(1, "Up"), (2, "Coco"), (3, "Luca")])
c.commit()

cursor = c.execute("SELECT * FROM Peliculas ORDER BY titulo")
c.close()

try:
    print(cursor.fetchall())
except sqlite3.ProgrammingError as e:
    print("ProgrammingError:", e)

print()
print("Lo correcto es sacar los datos antes de cerrar:")
c = sqlite3.connect(ruta)
filas = c.execute("SELECT * FROM Peliculas ORDER BY titulo").fetchall()
c.close()
print(" ", filas)
print("  tipo:", type(filas).__name__, "de", type(filas[0]).__name__)
"""),

md("""
`Cannot operate on a closed database.`

Es el error 04 de la diapositiva. **Un cursor no trae las filas: apunta a ellas.** Mientras la conexión
viva, las va entregando; en cuanto se cierra, el cursor deja de servir y el error aparece lejos de donde
se causó, que es lo que lo hace caro.

La corrección es de una palabra: `fetchall()` antes de cerrar. Lo que devuelve es una lista de tuplas,
que ya es un objeto de Python normal y sobrevive a todo.

Ese `fetchall` es también la frontera de la que hablaba la semana 11. Lo que sale de la base de datos entra
al programa una sola vez, en un lugar, y de ahí en adelante son estructuras de Python.

## El cursor que ya se recorrió
"""),

code("""
# FALLA A PROPÓSITO, y no truena. Code036.py, líneas 81 a 84.
import sqlite3

c = sqlite3.connect(ruta)
cursor = c.execute("SELECT * FROM Peliculas ORDER BY titulo")

for row in cursor:
    print(" ", row)

fetched = cursor.fetchall()
print()
print("Y ahora fetchall() devuelve:", fetched)
print("Sin ningún error, y con la tabla llena:",
      c.execute("SELECT COUNT(*) FROM Peliculas").fetchone())
print()
print("Es lo mismo que el generador de la semana 10: se recorre una vez.")
c.close()
"""),

md("""
El `for` consumió el cursor y `fetchall()` devolvió una lista vacía.

`Code036.py` lo documenta en sus líneas 83 y 84 y tiene toda la razón: *"as we have already iterated
through the cursor, it is empty"*. Vale la pena medirlo porque la lista vacía no viene con ninguna
advertencia, y quien reciba ese `[]` va a concluir que la tabla no tiene datos.

Es exactamente el generador agotado de la semana 10, con otro nombre. **Lo que se produce mientras se
recorre se recorre una vez.**

## Pegar el dato dentro de la consulta
"""),

code("""
# FALLA A PROPÓSITO. Un título con comilla rompe la consulta.
import sqlite3

base_limpia()
c = sqlite3.connect(ruta)
c.executemany("INSERT INTO Peliculas VALUES (?, ?)",
              [(1, "Up"), (2, "Coco"), (3, "O'Brien")])
c.commit()

buscado = "O'Brien"

malo = "SELECT * FROM Peliculas WHERE titulo = '" + buscado + "'"
print("La consulta que se armó:", malo)
try:
    print(c.execute(malo).fetchall())
except sqlite3.OperationalError as e:
    print("  OperationalError:", e)

print()
print("Con marcador:", c.execute(
    "SELECT * FROM Peliculas WHERE titulo = ?", (buscado,)).fetchall())
c.close()
"""),

md("""
Un apóstrofo en el dato y la consulta dejó de ser una consulta.

La comilla del dato cerró la cadena de SQL antes de tiempo, y lo que venía después pasó a ser sintaxis. El
motor no tiene manera de saber que ese apóstrofo era parte de un apellido: recibió texto y lo leyó como
texto.

Con un marcador, el valor **nunca se interpreta como SQL**. Viaja aparte, en una tupla, y el motor lo mete
en el lugar del signo de interrogación ya sabiendo que es un dato.

Y ahora la versión que no es un accidente.
"""),

code("""
# FALLA A PROPÓSITO. Lo mismo, escrito a propósito por quien teclea.
import sqlite3

c = sqlite3.connect(ruta)

buscado = input("Título: ") if False else "x' OR '1'='1"

malo = f"SELECT * FROM Peliculas WHERE titulo = '{buscado}'"
print("Lo que alguien tecleó:", repr(buscado))
print("La consulta que quedó: ", malo)
print()
print("Devuelve la tabla completa:")
for fila in c.execute(malo):
    print(" ", fila)

print()
print("Con marcador, lo mismo tecleado:")
print(" ", c.execute("SELECT * FROM Peliculas WHERE titulo = ?",
                     (buscado,)).fetchall())
print("  <- ninguna película se llama así, y eso es exactamente lo correcto")
c.close()
"""),

md("""
Pidió una película y le entregaron la tabla entera.

`x' OR '1'='1` cierra la comilla, agrega un `OR` que siempre es verdadero, y deja una comilla suelta que
casa con la que el programa iba a poner al final. La condición `WHERE` deja de filtrar.

Es el error 02 de la diapositiva y se llama **inyección de SQL**. Con un `SELECT` la consecuencia es que
alguien ve datos que no le tocaban; con un `DELETE` o un `UPDATE`, la consecuencia es peor.

La corrección no es escapar las comillas a mano, ni revisar que el texto no traiga caracteres raros. Es
el marcador, siempre, sin excepciones y también cuando el dato "viene de adentro", porque el dato de
adentro de hoy es el campo de captura de mañana.

## La coma que convierte un paréntesis en tupla
"""),

code("""
# FALLA A PROPÓSITO. La tupla de un elemento, sin su coma.
import sqlite3

c = sqlite3.connect(ruta)

print('type(("Coco")) es', type(("Coco")).__name__, "<- solo un paréntesis")
print('type(("Coco",)) es', type(("Coco",)).__name__, "<- ahora sí")
print()

try:
    c.execute("SELECT * FROM Peliculas WHERE titulo = ?", ("Coco"))
except sqlite3.ProgrammingError as e:
    print("Sin la coma:", type(e).__name__)
    print(" ", e)

print()
print("Con la coma:", c.execute(
    "SELECT * FROM Peliculas WHERE titulo = ?", ("Coco",)).fetchall())
c.close()
"""),

md("""
`Incorrect number of bindings supplied. The current statement uses 1, and there are 4 supplied.`

Cuatro, porque `"Coco"` tiene cuatro letras. Sin la coma, los paréntesis no crean una tupla: agrupan una
expresión, igual que en aritmética. Lo que llegó fue la cadena, y `sqlite3` la recorrió carácter por
carácter buscando parámetros.

**La coma es lo que hace la tupla, no los paréntesis.** Es cierto en todo Python y aquí se cobra en la
primera consulta con un solo parámetro que alguien escriba.

## Relacionar dos tablas
"""),

code("""
# Code036.py, líneas 117 a 144: la llave foránea y el INNER JOIN
import sqlite3
from pathlib import Path

ruta_join = Path("join.db")
ruta_join.unlink(missing_ok=True)

movie_viewers = [
    {"id": 1, "movie_id": 1, "name": "Ana", "last_name": "Robles"},
    {"id": 2, "movie_id": 1, "name": "Luis", "last_name": "Ferrer"},
    {"id": 3, "movie_id": 19, "name": "Sofía", "last_name": "Ines"},
]

with sqlite3.connect(ruta_join) as connection:
    connection.execute("CREATE TABLE Movies (id INTEGER PRIMARY KEY, "
                       "title TEXT NOT NULL, year INTEGER NOT NULL)")
    connection.executemany("INSERT INTO Movies VALUES (?, ?, ?)",
                           [(1, "Toy Story", 1995), (19, "Coco", 2017)])
    connection.execute(
        "CREATE TABLE IF NOT EXISTS MovieViewers (id INTEGER PRIMARY KEY, "
        "movie_id INTEGER NOT NULL, name TEXT NOT NULL, last_name TEXT NOT NULL, "
        "FOREIGN KEY (movie_id) REFERENCES Movies(id))")
    for viewer in movie_viewers:
        connection.execute("INSERT INTO MovieViewers VALUES (?, ?, ?, ?)",
                           (viewer["id"], viewer["movie_id"], viewer["name"],
                            viewer["last_name"]))
    connection.commit()

movie_title = "Toy Story"
with sqlite3.connect(ruta_join) as connection:
    select_command = ("SELECT Movies.title, MovieViewers.name, MovieViewers.last_name "
                      "FROM Movies INNER JOIN MovieViewers "
                      "ON Movies.id = MovieViewers.movie_id "
                      "WHERE Movies.title = ?")
    for row in connection.execute(select_command, (movie_title,)):
        print(" ", row)
connection.close()
"""),

md("""
Dos tablas, una llave foránea, y una consulta que las junta.

`movie_id INTEGER NOT NULL, FOREIGN KEY (movie_id) REFERENCES Movies(id)` dice que esa columna guarda el
`id` de una película. Es la misma relación de composición de la semana 6, escrita en la tabla en lugar de
en el objeto.

`INNER JOIN ... ON` es la operación que la sigue: toma los renglones de las dos tablas donde la llave
foránea coincide con la primaria. Lo que sale es un renglón por espectador con el título pegado.

Fíjate en que el título va por marcador, como debe. `Code036.py` lo hace bien en su línea 142.
"""),

md("""
---
# Bloque 3 · Proyecto integrador

La entrega que junta las siete unidades. Se califica el código y el reporte, y el código pesa más del
doble.

**Las cuatro piezas.** Modelado orientado a objetos, persistencia, interfaz gráfica y reporte escrito.

**Cómo se reparte.** Empieza por las clases del dominio, sin ventana y sin base de datos. Si esas clases
corren desde la terminal, el resto es conectar cables.

La celda de abajo es esa arquitectura completa, en miniatura y corriendo.
"""),

code("""
import sqlite3
from pathlib import Path


# ── Capa 1: el dominio. No importa sqlite3 ni PyQt6.
class Prestamo:
    def __init__(self, matricula: str, titulo: str, dias: int = 14) -> None:
        if not matricula.strip():
            raise ValueError("la matrícula no puede ir vacía")
        if dias <= 0:
            raise ValueError(f"los días deben ser positivos, llegaron {dias}")
        self.matricula = matricula.strip()
        self.titulo = titulo
        self.dias = dias

    @property
    def multa(self) -> float:
        return max(0, self.dias - 14) * 12.50

    def __repr__(self) -> str:
        return f"Prestamo({self.matricula!r}, {self.titulo!r}, {self.dias})"


# ── Capa 2: la persistencia. Todo el SQL vive aquí y en ningún otro lado.
class RepositorioPrestamos:
    def __init__(self, ruta):
        self.conexion = sqlite3.connect(ruta)
        self.conexion.execute(
            "CREATE TABLE IF NOT EXISTS Prestamos ("
            "matricula TEXT NOT NULL, titulo TEXT NOT NULL, dias INTEGER NOT NULL, "
            "PRIMARY KEY (matricula, titulo))")
        self.conexion.commit()

    def guardar(self, prestamo):
        self.conexion.execute(
            "INSERT OR REPLACE INTO Prestamos VALUES (?, ?, ?)",
            (prestamo.matricula, prestamo.titulo, prestamo.dias))
        self.conexion.commit()

    def de(self, matricula):
        filas = self.conexion.execute(
            "SELECT matricula, titulo, dias FROM Prestamos WHERE matricula = ?",
            (matricula,)).fetchall()
        return [Prestamo(m, t, d) for m, t, d in filas]

    def cerrar(self):
        self.conexion.close()


# El dominio se prueba sin base de datos y sin ventana
p = Prestamo("A001", "El Quijote", 20)
print("Sin tocar el disco:", p, " multa:", p.multa)
print("A tiempo:", Prestamo("A002", "Rayuela", 10).multa)
try:
    Prestamo("  ", "Pedro Páramo")
except ValueError as e:
    print("Y valida:", e)

print()
Path("biblioteca.db").unlink(missing_ok=True)
repo = RepositorioPrestamos("biblioteca.db")
for prestamo in [p, Prestamo("A001", "Rayuela", 30), Prestamo("A002", "Aura", 7)]:
    repo.guardar(prestamo)

recuperados = repo.de("A001")
print("Recuperados de la base:", recuperados)
print("¿Volvieron como objetos del dominio?",
      all(isinstance(x, Prestamo) for x in recuperados))
print("Multa total de A001:", sum(x.multa for x in recuperados))
repo.cerrar()
"""),

md("""
Dos clases, dos responsabilidades, y ninguna sabe de la otra más de lo necesario.

`Prestamo` no importa `sqlite3`. Se construye, valida en el constructor como la semana 11, calcula la
multa con una propiedad como la semana 5, y se prueba desde la consola sin que exista una base de datos.

`RepositorioPrestamos` es la única clase que escribe SQL. Todas las consultas del proyecto pasan por aquí,
y por eso cambiar una columna se arregla en un archivo. Fíjate en `de()`: recibe filas y **devuelve
objetos del dominio**, así que el resto del programa nunca ve una tupla.

Lo que falta es la tercera capa, la ventana, y su regla cabe en un renglón: **un slot lee los controles,
llama a estas dos clases, y muestra el resultado.** Nada más. Si un slot calcula una multa, la multa se
volvió imposible de probar.

## El SQL repartido por toda la ventana
"""),

code("""
# FALLA A PROPÓSITO, y no truena. La misma consulta escrita en cuatro lugares.
import sqlite3
from pathlib import Path

ruta = Path("repartido.db")
ruta.unlink(missing_ok=True)
c = sqlite3.connect(ruta)
c.execute("CREATE TABLE Prestamos (matricula TEXT, titulo TEXT, dias INTEGER)")
c.executemany("INSERT INTO Prestamos VALUES (?, ?, ?)",
              [("A001", "El Quijote", 20), ("A002", "Rayuela", 10)])
c.commit()

# Cuatro slots de la ventana, cada uno con su propio SELECT
SLOTS = {
    "al_buscar":   "SELECT matricula, titulo FROM Prestamos WHERE matricula = ?",
    "al_listar":   "SELECT matricula, titulo, dias FROM Prestamos",
    "al_contar":   "SELECT COUNT(*) FROM Prestamos WHERE matricula = ?",
    "al_exportar": "SELECT titulo, dias FROM Prestamos ORDER BY titulo",
}

print("Con la tabla como está:")
for nombre, sql in SLOTS.items():
    parametros = ("A001",) if "?" in sql else ()
    print(f"  {nombre:<14}ok  {c.execute(sql, parametros).fetchall()[:1]}")

# Mañana alguien renombra una columna
c.execute("ALTER TABLE Prestamos RENAME COLUMN dias TO dias_prestamo")
c.commit()

print()
print("Después de renombrar la columna 'dias':")
rotos = 0
for nombre, sql in SLOTS.items():
    parametros = ("A001",) if "?" in sql else ()
    try:
        c.execute(sql, parametros).fetchall()
        print(f"  {nombre:<14}sigue funcionando")
    except sqlite3.OperationalError as e:
        rotos += 1
        print(f"  {nombre:<14}roto: {e}")

print()
print(f"Se rompieron {rotos} de {len(SLOTS)} slots, y hay que encontrarlos uno por uno.")
c.close()
"""),

md("""
Un cambio en la tabla y dos slots rotos, en dos archivos distintos.

Es el error 03 de la diapositiva. El SQL repartido por la interfaz convierte cualquier cambio del modelo
en una cacería: hay que abrir el proyecto entero y buscar la palabra `dias`, con el riesgo de que alguna
consulta viva dentro de una cadena armada por partes y no aparezca en la búsqueda.

Con la capa de acceso a datos del ejemplo anterior, ese mismo cambio toca **un archivo**, y los slots ni
se enteran porque reciben objetos `Prestamo` y no tuplas.

Fíjate además en que los dos slots que sobrevivieron lo hicieron por casualidad: no mencionaban la
columna. **Que un cambio no rompa todo no quiere decir que el diseño aguante; quiere decir que esta vez
tuviste suerte.**
"""),

md("""
---
## Cuatro errores de esta sesión

**Olvidar el `commit`.** Los `INSERT` corren, la conexión que los hizo los ve, y al cerrar sin confirmar
se descartan. El `SELECT` de comprobación desde la misma conexión no comprueba nada.

**Pegar valores con f-strings.** Un apóstrofo rompe la consulta y una cadena escrita a propósito la
convierte en otra distinta. El marcador mantiene el dato como dato.

**SQL repartido por toda la ventana.** Cambiar una columna obliga a revisar el proyecto entero. Todo el
SQL vive en una sola clase.

**Guardar el cursor para después.** Al cerrarse la conexión el cursor deja de servir, y un cursor ya
recorrido devuelve una lista vacía sin quejarse.
"""),

md("""
---
# Ejercicios

El laboratorio de esta semana es convertir dos clases de tu proyecto en tablas. Los ejercicios construyen
hacia eso.

Las soluciones están hasta abajo del cuaderno.

### Ejercicio 1 · Archivo contra tabla

Guarda diez mil registros en un CSV y en una tabla con llave primaria. Busca el último de las dos maneras
y mide con `time.perf_counter`.

Explica en un comentario por qué la diferencia crece con el número de registros.

### Ejercicio 2 · La llave primaria

Crea una tabla con `id INTEGER PRIMARY KEY` e inserta el mismo `id` dos veces. Atrapa el
`IntegrityError` e imprime su mensaje.

Repítelo con `INSERT OR REPLACE` y muestra cuántas filas quedaron.

### Ejercicio 3 · Las cuatro combinaciones

Escribe las cuatro situaciones de la tabla del bloque 2 y comprueba cada una desde una conexión nueva.
Imprime una tabla con el resultado.

### Ejercicio 4 · El cursor

Ejecuta un `SELECT`, recorre el cursor con un `for` y después llama a `fetchall()`. Imprime lo que
devuelve.

Después cierra la conexión antes de llamar a `fetchall()` y atrapa el `ProgrammingError`.

### Ejercicio 5 · El marcador

Inserta un título que traiga un apóstrofo. Búscalo pegando el dato en la cadena y con marcador, y muestra
qué pasa en cada caso.

Prueba también con el texto `x' OR '1'='1`.

### Ejercicio 6 · La tupla de uno

Ejecuta una consulta con un parámetro pasando `("Coco")` y `("Coco",)`. Atrapa el error del primero y
explica en un comentario cuántos parámetros creyó recibir `sqlite3`.

### Ejercicio 7 · Dos tablas

Modela `Alumno` y `Inscripcion` con una llave foránea. Inserta tres alumnos y cinco inscripciones, y
escribe un `INNER JOIN` que liste el nombre del alumno y la materia.

### Ejercicio 8 · La capa de acceso

Toma una clase de tu proyecto y escribe su repositorio: una clase con `guardar`, `de` y `cerrar`, donde
todo el SQL viva adentro y los métodos devuelvan objetos del dominio, nunca tuplas.

### Ejercicio 9 · El laboratorio

En parejas, tomen dos clases de su proyecto y escriban el `CREATE TABLE` que les corresponde, más los
métodos `guardar` y `cargar` que las convierten en filas y de vuelta.

Restricciones: todo el SQL vive en una sola clase de acceso a datos, y ninguna otra lo escribe.

Entregan un archivo `.py` con las clases y un script de prueba que guarda, cierra, abre y recupera. El
criterio es que las clases del dominio sigan corriendo sin importar `sqlite3` ni `PyQt6`.
"""),

md("""
---
## Tres ideas para llevarse

**Una tabla contesta, un archivo solo guarda.** La diferencia aparece cuando hay que buscar, filtrar u
ordenar sin leerlo todo, y no depende de cuántos registros haya.

**El `with` de `sqlite3` confirma la transacción y no cierra la conexión.** Es al revés de como suena.
Cerrar sin confirmar descarta lo pendiente, y una excepción adentro del bloque también, que en ese caso es
lo que quieres.

**Los valores viajan como parámetros.** El marcador mantiene el dato como dato, y una comilla deja de
poder cambiar la consulta. Con la coma puesta, que es lo que hace la tupla.

La semana 17 es la última: repaso general y examen final integrador. Una sola pregunta puede tocar
modelado, archivos y persistencia al mismo tiempo, así que el cuaderno de cierre vuelve a pasar por los
errores que más puntos costaron en los dos parciales.
"""),

md("""
---
# Soluciones

### Ejercicio 1

```python
import csv, sqlite3, time
from pathlib import Path

N = 10_000
filas = [(i, f"registro {i}") for i in range(1, N + 1)]

with open("datos.csv", "w", newline="", encoding="utf-8") as f:
    csv.writer(f).writerows(filas)

Path("datos.db").unlink(missing_ok=True)
c = sqlite3.connect("datos.db")
c.execute("CREATE TABLE R (id INTEGER PRIMARY KEY, texto TEXT)")
c.executemany("INSERT INTO R VALUES (?, ?)", filas)
c.commit()

inicio = time.perf_counter()
with open("datos.csv", newline="", encoding="utf-8") as f:
    ultimo = [fila for fila in csv.reader(f) if int(fila[0]) == N][0]
print(f"archivo: {time.perf_counter() - inicio:.5f} s")

inicio = time.perf_counter()
c.execute("SELECT * FROM R WHERE id = ?", (N,)).fetchone()
print(f"tabla:   {time.perf_counter() - inicio:.6f} s")
c.close()

# La búsqueda en el archivo compara contra todos los registros, así que su
# costo crece con N. La de la tabla usa el índice de la llave primaria y llega
# al renglón sin recorrer, así que su costo casi no se mueve.
```

### Ejercicio 2

```python
import sqlite3
from pathlib import Path

Path("llave.db").unlink(missing_ok=True)
c = sqlite3.connect("llave.db")
c.execute("CREATE TABLE M (id INTEGER PRIMARY KEY, t TEXT)")
c.execute("INSERT INTO M VALUES (1, 'Up')")

try:
    c.execute("INSERT INTO M VALUES (1, 'Coco')")
except sqlite3.IntegrityError as e:
    print("IntegrityError:", e)

c.execute("INSERT OR REPLACE INTO M VALUES (1, 'Coco')")
c.commit()
print(c.execute("SELECT COUNT(*) FROM M").fetchone())
print(c.execute("SELECT * FROM M").fetchall())
c.close()
```

### Ejercicio 3

```python
import sqlite3
from pathlib import Path

ruta = Path("cuatro.db")


def limpia():
    ruta.unlink(missing_ok=True)
    c = sqlite3.connect(ruta)
    c.execute("CREATE TABLE M (id INTEGER PRIMARY KEY)")
    c.commit()
    c.close()


def cuantas():
    c = sqlite3.connect(ruta)
    n = c.execute("SELECT COUNT(*) FROM M").fetchone()[0]
    c.close()
    return n


limpia()
with sqlite3.connect(ruta) as c:
    c.execute("INSERT INTO M VALUES (1)")
c.close()
print("with que termina bien:", cuantas())

limpia()
try:
    with sqlite3.connect(ruta) as c:
        c.execute("INSERT INTO M VALUES (1)")
        raise ValueError()
except ValueError:
    pass
c.close()
print("with con excepción:   ", cuantas())

limpia()
c = sqlite3.connect(ruta)
c.execute("INSERT INTO M VALUES (1)")
c.commit()
c.close()
print("sin with, con commit: ", cuantas())

limpia()
c = sqlite3.connect(ruta)
c.execute("INSERT INTO M VALUES (1)")
c.close()
print("sin with, sin commit: ", cuantas())
```

### Ejercicio 4

```python
import sqlite3

c = sqlite3.connect("cuatro.db")
c.execute("INSERT OR REPLACE INTO M VALUES (1)")
c.commit()

cur = c.execute("SELECT * FROM M")
for fila in cur:
    print(fila)
print("fetchall tras el for:", cur.fetchall())

cur = c.execute("SELECT * FROM M")
c.close()
try:
    cur.fetchall()
except sqlite3.ProgrammingError as e:
    print("ProgrammingError:", e)
```

### Ejercicio 5

```python
import sqlite3
from pathlib import Path

Path("comillas.db").unlink(missing_ok=True)
c = sqlite3.connect("comillas.db")
c.execute("CREATE TABLE P (titulo TEXT)")
c.executemany("INSERT INTO P VALUES (?)", [("Up",), ("O'Brien",)])
c.commit()

for buscado in ["O'Brien", "x' OR '1'='1"]:
    sql = "SELECT * FROM P WHERE titulo = '" + buscado + "'"
    try:
        print("pegado: ", c.execute(sql).fetchall())
    except sqlite3.OperationalError as e:
        print("pegado: ", type(e).__name__, e)
    print("marcador:", c.execute(
        "SELECT * FROM P WHERE titulo = ?", (buscado,)).fetchall())
c.close()
```

### Ejercicio 6

```python
import sqlite3

c = sqlite3.connect("comillas.db")
try:
    c.execute("SELECT * FROM P WHERE titulo = ?", ("Up"))
except sqlite3.ProgrammingError as e:
    print(e)
print(c.execute("SELECT * FROM P WHERE titulo = ?", ("Up",)).fetchall())
c.close()

# sqlite3 creyó recibir dos parámetros, uno por cada letra de "Up", porque sin
# la coma lo que llegó fue la cadena y una cadena es iterable.
```

### Ejercicio 7

```python
import sqlite3
from pathlib import Path

Path("escuela.db").unlink(missing_ok=True)
c = sqlite3.connect("escuela.db")
c.execute("CREATE TABLE Alumno (id INTEGER PRIMARY KEY, nombre TEXT NOT NULL)")
c.execute("CREATE TABLE Inscripcion (id INTEGER PRIMARY KEY, "
          "alumno_id INTEGER NOT NULL, materia TEXT NOT NULL, "
          "FOREIGN KEY (alumno_id) REFERENCES Alumno(id))")

c.executemany("INSERT INTO Alumno VALUES (?, ?)",
              [(1, "Ana Robles"), (2, "Luis Ferrer"), (3, "Sofía Ines")])
c.executemany("INSERT INTO Inscripcion VALUES (?, ?, ?)",
              [(1, 1, "COM102"), (2, 1, "COM101"), (3, 2, "COM102"),
               (4, 3, "COM103"), (5, 3, "COM102")])
c.commit()

for fila in c.execute(
        "SELECT Alumno.nombre, Inscripcion.materia FROM Alumno "
        "INNER JOIN Inscripcion ON Alumno.id = Inscripcion.alumno_id "
        "ORDER BY Alumno.nombre, Inscripcion.materia"):
    print(fila)
c.close()
```

### Ejercicio 8 y 9

```python
import sqlite3


class Alumno:
    \"\"\"Dominio puro: no importa sqlite3 y se prueba desde la consola.\"\"\"

    def __init__(self, matricula: str, nombre: str, promedio: float = 0.0) -> None:
        if not matricula.strip():
            raise ValueError("la matrícula no puede ir vacía")
        if not 0 <= promedio <= 10:
            raise ValueError(f"el promedio debe ir de 0 a 10, llegó {promedio}")
        self.matricula = matricula.strip()
        self.nombre = nombre
        self.promedio = promedio

    @property
    def aprobado(self) -> bool:
        return self.promedio >= 7

    def __repr__(self) -> str:
        return f"Alumno({self.matricula!r}, {self.nombre!r}, {self.promedio})"


class RepositorioAlumnos:
    \"\"\"La única clase del proyecto que escribe SQL.\"\"\"

    CREAR = ("CREATE TABLE IF NOT EXISTS Alumnos ("
             "matricula TEXT PRIMARY KEY, nombre TEXT NOT NULL, "
             "promedio REAL NOT NULL)")

    def __init__(self, ruta):
        self.conexion = sqlite3.connect(ruta)
        self.conexion.execute(self.CREAR)
        self.conexion.commit()

    def guardar(self, alumno):
        self.conexion.execute(
            "INSERT OR REPLACE INTO Alumnos VALUES (?, ?, ?)",
            (alumno.matricula, alumno.nombre, alumno.promedio))
        self.conexion.commit()

    def cargar(self, matricula):
        fila = self.conexion.execute(
            "SELECT matricula, nombre, promedio FROM Alumnos WHERE matricula = ?",
            (matricula,)).fetchone()
        return Alumno(*fila) if fila else None

    def todos(self):
        return [Alumno(*f) for f in self.conexion.execute(
            "SELECT matricula, nombre, promedio FROM Alumnos ORDER BY matricula")]

    def cerrar(self):
        self.conexion.close()


if __name__ == "__main__":
    from pathlib import Path

    Path("escuela2.db").unlink(missing_ok=True)

    # El dominio, sin disco
    ana = Alumno("A001", "Ana Robles", 9.2)
    print(ana, ana.aprobado)

    # Guardar, cerrar, abrir y recuperar
    repo = RepositorioAlumnos("escuela2.db")
    repo.guardar(ana)
    repo.guardar(Alumno("A002", "Luis Ferrer", 6.4))
    repo.cerrar()

    repo = RepositorioAlumnos("escuela2.db")
    print(repo.cargar("A001"))
    print(repo.todos())
    print("Aprobados:", [a.matricula for a in repo.todos() if a.aprobado])
    repo.cerrar()
```

Tres decisiones que vale la pena defender en la entrega.

**`Alumno` no importa `sqlite3`.** Se construye, valida y calcula desde la consola. Si mañana el proyecto
cambia de SQLite a un archivo JSON, esta clase no se toca.

**`cargar` y `todos` devuelven objetos del dominio, nunca tuplas.** Ese es el punto entero de la capa:
la frontera convierte una vez y hacia adentro solo hay `Alumno`.

**El `CREATE TABLE` es una constante de la clase.** Está escrito una vez, se lee en el mismo archivo que
las consultas, y cuando haya que agregar una columna hay un solo lugar donde buscar.
"""),

]

write(OUT / "es" / "w16.ipynb", es)
print("wrote", OUT / "es" / "w16.ipynb")
