"""notebooks/programacion-orientada-a-objetos/es/w12.ipynb

Source deck: ppts/python/programacion-orientada-a-objetos/es/w12.es.yaml
Source code:  docs/en/courses/python-course/03 - Paths and Files/7th Module/Code029.py
                  (pathlib: exists, resolve, name, stem, suffix, parent, glob)
              docs/en/courses/python-course/03 - Paths and Files/7th Module/Code030.py
                  (read_text, write_text, los modos a y w, shutil.copy)
              docs/en/courses/python-course/03 - Paths and Files/7th Module/Code31.py
                  (texto: read, recorrer por líneas, separadores, dict(zip(...)))
              docs/en/courses/python-course/03 - Paths and Files/7th Module/Code32.py
                  (csv.reader, csv.DictReader, csv.writer)
              docs/en/courses/python-course/07 - Activities/Exams/2ndMidTerm/
                  script1.py, script3.py

Ninguno de los archivos del 7th Module se corre desde el repositorio: Code030.py
escribe test.txt y test_copy.txt dentro de docs/, y Code34.py deja files.zip y
extracted_files/. El cuaderno reproduce su código en el directorio de trabajo de
la sesión, que en Colab es /content y aquí es un directorio temporal.

Cosas medidas del repositorio que el cuaderno enseña como trampa, sin corregir:

  script1.py líneas 9 a 12 arman la ruta con filepath + filename, donde filepath
  es la cadena "./07 - Activities/Exams/2ndMidTerm/". El script corre si el
  directorio actual es docs/en/courses/python-course y muere con
  FileNotFoundError desde su propia carpeta. Comprobado en las dos.

  Code030.py líneas 35 y 36 afirman que read_text es más eficiente que open
  "because in the read_text method, the file is opened and closed
  automatically". read_text llama a open por dentro; el código fuente se imprime
  en una celda.

  Code030.py línea 20 documenta st_ctime como "time of creation". Eso es cierto
  en Windows y falso en Linux y macOS, donde es la hora del último cambio de
  metadatos. Colab corre sobre Linux.

  script3.py línea 25 parte cada renglón del CSV con split(","). Funciona con el
  videogames.csv de hoy, cuyos ocho títulos no traen comas, y revienta con un
  ValueError de desempaquetado en cuanto uno la traiga.

La semana 11 cerró apuntando aquí: una de sus celdas abrió un archivo a mano,
escribió el finally que lo cerraba, y se cayó con un NameError adentro de ese
finally. Este cuaderno cierra apuntando a los archivos binarios y al acceso
aleatorio de la semana 13.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from nbkit import md, code, write, REPO

OUT = REPO / "notebooks" / "programacion-orientada-a-objetos"

es = [

md("""
# Programación Orientada a Objetos · Semana 12
## Tema 5 · Archivos

**COM102 · Facultad de Ingeniería · Profesor David Escobar-Castillejos**

Los datos dejan de vivir en memoria. Rutas que sirven en cualquier sistema, el bloque que cierra solo, y
el CSV de siempre.

La semana pasada, una celda abrió un archivo a mano, escribió el `finally` que lo cerraba, y se cayó con
un `NameError` adentro de ese mismo `finally`. Este cuaderno empieza por hacer que ese `finally` deje de
escribirse.

Al terminar vas a poder:

1. Armar rutas con `pathlib` y leer el nombre, la extensión y la carpeta padre sin cortar cadenas.
2. Explicar qué se rompe cuando se abre un archivo sin `with`, con la prueba en disco.
3. Elegir el modo de apertura sabiendo cuál crea, cuál conserva y cuál deja el archivo vacío al abrirlo.
4. Leer y escribir un CSV con `DictReader` y `DictWriter`, sin depender del orden de las columnas.
5. Decir por qué una ruta relativa escrita a mano funciona en una máquina y falla en la de al lado.

### Cómo se usa este cuaderno

Ejecuta las celdas en orden con **Shift + Enter**. Once fallan a propósito y llevan un comentario que lo
dice.

Siete de las once **no lanzan ninguna excepción**. La peor de todas escribe cien renglones, el programa
termina sin quejarse, y el archivo en disco queda vacío.

Todo lo que este cuaderno escribe se queda en el directorio de trabajo de la sesión, que en Colab es
`/content`. No toca nada del repositorio.
"""),

md("""
---
# Bloque 1 · Rutas y archivos

Antes de leer nada hay que saber dónde está. Y una ruta escrita a mano funciona en tu máquina y falla en
la de al lado.
"""),

code("""
import os
from pathlib import Path, PureWindowsPath, PurePosixPath

ruta = Path("datos") / "alumnos.csv"

print("La ruta:      ", ruta)
print("El nombre:    ", ruta.name)
print("Sin extensión:", ruta.stem)
print("La extensión: ", ruta.suffix)
print("La carpeta:   ", ruta.parent)
print("¿Existe?      ", ruta.exists())
print("Las partes:   ", ruta.parts)

print()
print("Este cuaderno corre sobre", "Windows" if os.name == "nt" else "Linux o macOS",
      f"(os.name = {os.name!r})")
print()
print("La misma ruta, escrita por cada sistema:")
print("  Windows:", PureWindowsPath("datos") / "alumnos.csv")
print("  Linux:  ", PurePosixPath("datos") / "alumnos.csv")
print()
print("Por eso la diagonal se escribe siempre igual y Python pone la barra que toca.")
"""),

md("""
La diagonal une pedazos de ruta. No es una división: `Path` la sobrecarga para que signifique "adentro
de".

La celda imprime la misma ruta escrita por los dos sistemas. Si escribes la ruta como cadena con la barra
puesta a mano, estás eligiendo un sistema operativo, y quien califique la tarea puede estar en el otro.

`parts` es la ruta ya partida, que es lo que hace que `name`, `stem`, `suffix` y `parent` salgan sin
tocar una sola cadena. Con `split("/")` y `[-1]` se llega al mismo lugar, hasta el día en que alguien
guarda un archivo con un punto en el nombre.

## La barra invertida que Python lee como otra cosa
"""),

code("""
# FALLA A PROPÓSITO. Una ruta escrita como cadena con barras invertidas.
mala = "datos\\notas.txt"

print("Lo que escribiste:  datos" + chr(92) + "notas.txt")
print("Lo que Python guardó:", repr(mala))
print("Caracteres:", len(mala), "y la barra ya no está:", chr(92) not in mala)
print()
print("Impreso se ve así:")
print(mala)
print()
print("Con Path no hay nada que escapar:")
buena = Path("datos") / "notas.txt"
print(" ", repr(str(buena)))
print()
print("Y si de verdad necesitas la cadena, va con r delante:")
print(" ", repr(r"datos\\notas.txt"))
"""),

md("""
`\\n` no son dos caracteres. Es un salto de línea, y la carpeta `datos` se quedó pegada a una `otas.txt`
que no existe.

Es el error 02 de la diapositiva y le pasa a todo el mundo una vez. Los nombres que empiezan con `n`,
`t`, `r` y `b` son los peligrosos, porque `\\n`, `\\t`, `\\r` y `\\b` son secuencias de escape de verdad.
El resto de las letras produce un aviso y sobrevive, que es peor, porque el error se vuelve
intermitente.

Las dos salidas: `Path` con la diagonal, o una cadena cruda con `r` delante. La primera además funciona
en los dos sistemas.

## `exists()` contesta por lo que hay ahora
"""),

code("""
# FALLA A PROPÓSITO, y no truena. Preguntar antes en lugar de intentar.
ruta = Path("temporal.txt")
ruta.write_text("dato importante", encoding="utf-8")

if ruta.exists():
    ruta.unlink()                 # alguien más borra el archivo aquí en medio
    try:
        contenido = ruta.read_text(encoding="utf-8")
    except FileNotFoundError as e:
        contenido = None
        print("El if dijo que existía y la lectura falló igual.")
        print("  FileNotFoundError:", e.strerror)

print()
print("Contenido:", contenido)
print()
ruta.write_text("dato importante", encoding="utf-8")
try:
    contenido = ruta.read_text(encoding="utf-8")
except FileNotFoundError:
    contenido = ""
print("Intentando y atrapando:", repr(contenido))
"""),

md("""
El `if` contestó que sí y la lectura falló de todos modos.

`exists()` contesta por el estado del disco **en ese instante**. Entre la pregunta y la lectura pasa
tiempo, y en ese hueco otro programa, otro usuario o el propio sistema pueden borrar, mover o bloquear el
archivo. La celda hace el borrado a propósito para que el hueco se vea; en producción lo hace el azar, y
por eso el error aparece una vez cada mil ejecuciones.

Es la comparación de la diapositiva entre preguntar antes e intentar y atrapar. **La segunda no deja
rendija**: no pregunta, intenta, y atiende exactamente el caso en el que falló.

`exists()` sigue sirviendo para decidir, no para proteger. Preguntar si un archivo de configuración está
para elegir entre leerlo y usar valores por omisión está bien. Preguntarlo para evitar un
`FileNotFoundError` no.

## La ruta relativa del segundo parcial
"""),

code("""
# FALLA A PROPÓSITO. script1.py, líneas 9 a 12, con su ruta tal cual.
import os

# Se reconstruye el árbol que el script espera, dentro del directorio de trabajo
destino = Path("07 - Activities/Exams/2ndMidTerm")
destino.mkdir(parents=True, exist_ok=True)
(destino / "menu.txt").write_text("Main menu\\n1.- Option 1\\n0.- Exit\\n", encoding="utf-8")

filepath = "./07 - Activities/Exams/2ndMidTerm/"
filename = "menu.txt"


def print_menu(menu: list) -> None:
    for item in menu:
        print(item)


def cargar_menu():
    with open(filepath + filename, "r") as file:
        return [linea.strip() for linea in file.readlines()]


PARTIDA = Path.cwd()
print("Directorio actual:", PARTIDA.name)
print_menu(cargar_menu())

print()
try:
    os.chdir(destino)
    print("Ahora el directorio actual es:", Path.cwd().name)
    cargar_menu()
except FileNotFoundError as e:
    print("  FileNotFoundError:", e.filename)
finally:
    os.chdir(PARTIDA)

print()
print("De vuelta en", Path.cwd().name)
"""),

md("""
El mismo archivo, el mismo script, dos directorios, y en el segundo no lo encuentra.

Una ruta relativa se resuelve contra el **directorio actual del proceso**, no contra el archivo `.py` que
la escribió. Cambiar de carpeta antes de correr el script cambia a qué archivo apunta la ruta, y eso no
se ve leyendo el código.

Los tres scripts del segundo parcial traen esta misma línea. Corren si quien los ejecuta está parado en
`docs/en/courses/python-course` y mueren desde su propia carpeta.

La corrección de una línea, para un script que quiere sus datos al lado:

```python
AQUI = Path(__file__).resolve().parent
ruta = AQUI / "menu.txt"
```

`__file__` es la ruta del archivo que se está ejecutando, así que la ruta deja de depender de dónde se
paró quien lo corrió. En un cuaderno `__file__` no existe, y ahí el directorio actual sí es la referencia
correcta porque es el único que hay.

**Y de paso: `filepath + filename` funciona solo porque alguien se acordó de la diagonal final.** Sin
ella la cadena se pega y el archivo pasa a llamarse `2ndMidTermmenu.txt`. Con `/` de `Path` no hay nada
que acordarse.
"""),

md("""
---
# Bloque 2 · Abrir, procesar y cerrar

Un archivo abierto es un recurso prestado. Todo lo que se presta se devuelve, y conviene que se devuelva
solo.
"""),

code("""
ruta = Path("notas.txt")

# A mano, con la protección que hace falta para que sea correcto
archivo = None
try:
    archivo = open(ruta, "w", encoding="utf-8")
    archivo.write("Ana,9.2\\n")
finally:
    if archivo is not None:
        archivo.close()

print("A mano:", repr(ruta.read_text(encoding="utf-8")))

# Con with, lo mismo
with open(ruta, "a", encoding="utf-8") as archivo:
    archivo.write("Luis,7.8\\n")

print("Con with:", repr(ruta.read_text(encoding="utf-8")))
print()
print("¿El with lo cerró?", archivo.closed)
print("Y sigue cerrado aunque adentro truene:")

try:
    with open(ruta, encoding="utf-8") as f:
        raise ValueError("algo salió mal a media lectura")
except ValueError as e:
    print("  ValueError:", e)
print("  ¿f quedó cerrado?", f.closed)
"""),

md("""
Las dos primeras mitades hacen lo mismo. La diferencia son seis líneas contra dos, y que la primera hay
que acordarse de escribirla completa.

Fíjate en el `archivo = None` de arriba. Es la corrección de la celda de la semana 11 que se caía con
`NameError`: sin esa línea, si `open` falla, el `finally` toca una variable que no existe.

La tercera parte es el argumento entero. El bloque `with` cierra el archivo **al salir del bloque, con
error o sin él**, y lo hace antes de que la excepción siga subiendo. Eso es lo que un `finally` bien
escrito consigue, y el `with` lo consigue sin escribirlo.

## Lo que pasa cuando nadie cierra
"""),

code("""
# FALLA A PROPÓSITO, y no truena. Cien renglones escritos y un archivo vacío.
ruta = Path("reporte.txt")
FILAS = [f"alumno-{i:03d}" for i in range(1, 101)]

BITACORA = []          # el programa guarda el archivo abierto para seguir usándolo


def escribir_reporte(filas):
    archivo = open(ruta, "w", encoding="utf-8")
    BITACORA.append(archivo)
    for numero, fila in enumerate(filas, start=1):
        archivo.write(f"{numero:>4}  {fila}\\n")
    # falta archivo.close()


escribir_reporte(FILAS)

print("Renglones que el programa escribió:", len(FILAS))
print("Bytes en disco ahora mismo:", ruta.stat().st_size)
print("¿El archivo sigue abierto?", not BITACORA[0].closed)
print()
print("Ninguna excepción. El programa terminó bien.")
print()

BITACORA[0].close()
print("Después de cerrarlo a mano:", ruta.stat().st_size, "bytes")
print("Primer renglón:", repr(ruta.read_text(encoding="utf-8").splitlines()[0]))
"""),

md("""
Cien renglones escritos, cero bytes en disco, y ni una advertencia.

Escribir no manda nada al disco de inmediato. Lo que hace es llenar un **búfer** en memoria, y ese búfer
se vacía cuando se llena o cuando alguien cierra el archivo. Cerrar es lo que hace que lo escrito exista.

El `BITACORA.append(archivo)` de la celda no es un adorno: es lo que hace un programa de verdad cuando
guarda el archivo abierto en un atributo, en una lista o en un diccionario para seguir escribiéndole.
Mientras algo apunte al archivo, nadie lo cierra.

## Cuándo el descuido no se cobra
"""),

code("""
# FALLA A PROPÓSITO, y no truena. El mismo error, y esta vez sí funciona.
ruta = Path("suerte.txt")


def escribir_sin_guardar(filas):
    archivo = open(ruta, "w", encoding="utf-8")
    for numero, fila in enumerate(filas, start=1):
        archivo.write(f"{numero:>4}  {fila}\\n")
    # falta archivo.close(), igual que arriba


escribir_sin_guardar(FILAS)

print("Bytes en disco:", ruta.stat().st_size, "<- esta vez sí se escribió")
print()
print("La diferencia con la celda anterior es una sola línea:")
print("  allá el archivo se guardó en una lista y aquí no.")
print()
print("Al terminar la función nadie apunta al archivo, así que CPython lo destruye")
print("en ese instante y destruirlo lo cierra. El error sigue estando escrito.")
print()

with open(ruta, "w", encoding="utf-8") as archivo:
    for numero, fila in enumerate(FILAS, start=1):
        archivo.write(f"{numero:>4}  {fila}\\n")

print("Con with:")
print("  Bytes en disco:", ruta.stat().st_size)
print("  ¿Se cerró?", archivo.closed)
"""),

md("""
El mismo descuido, y esta vez el archivo salió completo.

CPython cuenta cuántos nombres apuntan a cada objeto y lo destruye en cuanto el conteo llega a cero.
Cuando la función termina, la variable local desaparece, nadie más apunta al archivo, y destruirlo lo
cierra. El descuido se cobró en la celda anterior y aquí no, y la única diferencia es que allá alguien
guardó la referencia.

Eso es lo peor que le puede pasar a un error: **que casi siempre funcione**. Aparece cuando el archivo se
guarda en un atributo, cuando el programa sigue vivo en un servidor, cuando el búfer se llenó a la mitad,
o cuando el intérprete no es CPython, porque esa destrucción inmediata no es parte del lenguaje.

Es el error 01 de la diapositiva. **El `with` cierra, y cerrar vacía el búfer.** Esa es la cadena
completa, y no depende de la suerte.

## Los cinco modos de apertura
"""),

code("""
resumen = []

Path("m.txt").write_text("original", encoding="utf-8")

# r: lee y no toca nada
with open("m.txt", encoding="utf-8") as f:
    resumen.append(("r", "existía", repr(f.read()), Path("m.txt").stat().st_size))

# a: conserva y agrega al final
with open("m.txt", "a", encoding="utf-8") as f:
    f.write("+agregado")
resumen.append(("a", "existía", repr(Path("m.txt").read_text(encoding="utf-8")),
                Path("m.txt").stat().st_size))

# w: vacía al abrirlo
f = open("m.txt", "w", encoding="utf-8")
resumen.append(("w", "existía", "(recién abierto, sin escribir)",
                Path("m.txt").stat().st_size))
f.close()

# x: solo si no existe
Path("nuevo.txt").unlink(missing_ok=True)
with open("nuevo.txt", "x", encoding="utf-8") as f:
    f.write("creado con x")
try:
    open("nuevo.txt", "x", encoding="utf-8")
except FileExistsError as e:
    resumen.append(("x", "ya existía", type(e).__name__, 0))

# r sobre algo que no existe
try:
    open("fantasma.txt", encoding="utf-8")
except FileNotFoundError as e:
    resumen.append(("r", "no existía", type(e).__name__, 0))

print(f"{'modo':<6}{'el archivo':<14}{'qué pasó':<40}{'bytes'}")
for modo, estado, que, bytes_ in resumen:
    print(f"{modo:<6}{estado:<14}{que:<40}{bytes_}")
"""),

md("""
La tabla de la diapositiva, medida.

El renglón que hay que memorizar es el tercero: **`w` deja el archivo en cero bytes en el momento de
abrirlo**, antes de que se escriba un solo carácter. Si el programa truena entre el `open` y el primer
`write`, el archivo que había se perdió y no se escribió el nuevo.

`x` es el seguro contra eso: crea si no existe y lanza `FileExistsError` si ya estaba. Cuando el
programa nunca debería pisar un archivo previo, `x` lo dice en una letra.

## Predice antes de correr

```python
ruta = Path("notas.txt")

with open(ruta, "w") as f:
    f.write("primera")

with open(ruta, "w") as f:
    f.write("segunda")

print(ruta.read_text())
```

- **A.** `primerasegunda`
- **B.** `segunda`, porque `w` vacía el archivo al abrirlo.
- **C.** `primera`, porque el archivo ya existía.
- **D.** `FileExistsError` al abrirlo la segunda vez.
"""),

code("""
ruta = Path("prediccion.txt")

with open(ruta, "w", encoding="utf-8") as f:
    print("  tras abrir en w:", ruta.stat().st_size, "bytes")
    f.write("primera")
print("  tras cerrar:      ", ruta.stat().st_size, "bytes ->",
      repr(ruta.read_text(encoding="utf-8")))

with open(ruta, "w", encoding="utf-8") as f:
    print("  tras abrir en w otra vez:", ruta.stat().st_size, "bytes <- ya se vació")
    f.write("segunda")

print()
print("Resultado:", repr(ruta.read_text(encoding="utf-8")))
print()
with open(ruta, "a", encoding="utf-8") as f:
    f.write("+tercera")
print("Con el modo a:", repr(ruta.read_text(encoding="utf-8")))
"""),

md("""
La respuesta es **B**.

La segunda línea de la salida es la prueba: al abrir en `w` por segunda vez, el archivo ya tenía cero
bytes y todavía no se había escrito nada. **El vaciado ocurre al abrir, no al escribir.**

Para conservar lo que había, el modo es `a`.

## El encoding que no se escribió
"""),

code("""
# FALLA A PROPÓSITO. Un archivo escrito con un encoding y leído con otro.
import locale

ruta = Path("acentos.txt")
ruta.write_bytes("niño, año, señor".encode("latin-1"))

print("Bytes en disco:", ruta.read_bytes())
print()

try:
    print(ruta.read_text(encoding="utf-8"))
except UnicodeDecodeError as e:
    print("Leído como utf-8:", type(e).__name__)
    print("  ", e.reason, "en la posición", e.start)

print()
print("Leído como latin-1:", ruta.read_text(encoding="latin-1"))
print()
print("Y sin decir nada, Python usa el del sistema:")
print("  encoding por omisión de esta máquina:", locale.getpreferredencoding(False))
print("  <- que es distinto en Windows, en Linux y en la máquina de quien califica")
"""),

md("""
Los mismos bytes, tres lecturas, dos resultados y un error.

Un archivo de texto en el disco es una fila de bytes. El **encoding** es la tabla que dice qué letra es
cada byte, y esa tabla no viaja dentro del archivo. Si quien escribe y quien lee no usan la misma, los
acentos salen rotos o la lectura truena.

Es el error 04 de la diapositiva. `open` sin `encoding` usa el del sistema, que es el que imprime la
última línea, y es distinto entre Windows y Linux. Por eso el archivo se lee bien en tu máquina y con los
acentos rotos en la de al lado.

**Regla:** `encoding="utf-8"` en todos los `open` y en todos los `read_text` y `write_text`. Sin
excepciones y sin pensarlo.

## Cargar todo contra recorrer por líneas
"""),

code("""
from sys import getsizeof

ruta = Path("grande.txt")
with open(ruta, "w", encoding="utf-8") as f:
    for i in range(200_000):
        f.write(f"A{i:06d},alumno-{i},{(i % 100) / 10:.1f}\\n")

print("Tamaño del archivo:", f"{ruta.stat().st_size:,}", "bytes")
print()

with open(ruta, encoding="utf-8") as f:
    todo = f.read()
print("Con read():          la cadena en memoria pesa", f"{getsizeof(todo):,}", "bytes")

with open(ruta, encoding="utf-8") as f:
    mayor = ""
    for linea in f:
        if len(linea) > len(mayor):
            mayor = linea
print("Recorriendo líneas:  la variable más grande pesa",
      f"{getsizeof(mayor):,}", "bytes")

print()
print("Las dos leen el archivo completo. Solo una lo tiene entero en memoria.")
print("Renglones:", todo.count(chr(10)))
"""),

md("""
El mismo archivo leído de dos maneras, y una de ellas nunca tuvo más de un renglón en memoria.

`read()` devuelve el archivo entero como una cadena. Con seis megas cabe; con seis gigas, no. Recorrer el
archivo con un `for` entrega **una línea a la vez**, y eso cuesta lo mismo en tiempo y no crece en
memoria.

Es el error 03 de la diapositiva. `read()` no está mal: está mal cuando no sabes de qué tamaño es el
archivo, que es casi siempre.

## Dos afirmaciones del repositorio, medidas
"""),

code("""
# FALLA A PROPÓSITO, y no truena. Code030.py, líneas 35 y 36.
import inspect
import time

print("Lo que dice el archivo:")
print('  "the read_text method is more efficient than the open method"')
print('  "because in the read_text method, the file is opened and closed automatically"')
print()
print("El código de read_text, tal como viene en esta versión de Python:")
try:
    print(inspect.getsource(Path.read_text))
except (OSError, TypeError):
    print("  (no se pudo leer el fuente en esta sesión)")

ruta = Path("medir.txt")
ruta.write_text("x" * 2_000_000, encoding="utf-8")

inicio = time.perf_counter()
for _ in range(20):
    ruta.read_text(encoding="utf-8")
con_read_text = time.perf_counter() - inicio

inicio = time.perf_counter()
for _ in range(20):
    with open(ruta, encoding="utf-8") as f:
        f.read()
con_open = time.perf_counter() - inicio

print(f"20 lecturas con read_text: {con_read_text:.4f} s")
print(f"20 lecturas con open:      {con_open:.4f} s")
print("Vuelve a correr la celda: el que gana cambia de una corrida a otra.")
"""),

md("""
`read_text` **llama a `open` por dentro**. Es el `with` de su propio código fuente, impreso arriba.

Así que no puede ser más eficiente: es lo mismo con menos que teclear. Lo que el archivo describe como
eficiencia es comodidad, y la comodidad es una razón perfectamente buena para preferirlo. Solo que se
llama de otra manera.

Los dos tiempos salen parecidos y cuál gana cambia entre corridas, porque la diferencia que queda es
ruido de medición y no del código.

Vale la pena quedarse con la técnica más que con la corrección. **Cuando una afirmación sobre rendimiento
se puede medir, se mide.** Dos llamadas a `perf_counter` y una función de la biblioteca estándar
resolvieron una discusión que llevaba años escrita en un comentario.

`read_text` sigue siendo la forma correcta de leer un archivo chico completo, y `open` con `with` la
forma correcta de recorrerlo.

## La fecha que significa dos cosas distintas
"""),

code("""
# FALLA A PROPÓSITO, y no truena. Code030.py, línea 20.
import os
from time import ctime

ruta = Path("fecha.txt")
ruta.write_text("primera versión", encoding="utf-8")
datos = ruta.stat()

print("Lo que dice el archivo: 'st_ctime: time of creation'")
print()
print("st_atime (último acceso):        ", ctime(datos.st_atime))
print("st_mtime (última modificación):  ", ctime(datos.st_mtime))
print("st_ctime (según el sistema):     ", ctime(datos.st_ctime))
print()
sistema = "Windows" if os.name == "nt" else "Linux o macOS"
print("Esta sesión corre sobre", sistema)
if os.name == "nt":
    print("  Aquí st_ctime sí es la hora de creación, y el comentario acierta.")
else:
    print("  Aquí st_ctime es la hora del último cambio de metadatos, no la de creación.")
    print("  El comentario del archivo es falso en este sistema.")
print()
print("La forma que significa lo mismo en todos lados:")
print("  st_birthtime, si existe:", hasattr(datos, "st_birthtime"))
"""),

md("""
`st_ctime` no quiere decir lo mismo en todos los sistemas.

En Windows es la hora de creación, que es lo que dice el comentario. En Linux y en macOS es la hora del
último cambio de **metadatos**: cambiar los permisos de un archivo la mueve, y el contenido no se tocó.
Colab corre sobre Linux, así que ahí el comentario es falso.

La `c` es de *change*, no de *create*, y esa letra ha costado muchos reportes de auditoría mal fechados.

Lo que hay que llevarse no es la trivia: **una afirmación sobre el sistema operativo se comprueba en el
sistema operativo donde va a correr el programa.** `os.name` está a una línea de distancia.
"""),

md("""
---
# Bloque 3 · Archivos de texto y CSV

El formato más simple que sigue siendo legible por una persona, y el que abre Excel sin preguntar nada.
"""),

code("""
# Code31.py, líneas 73 a 105: separadores distintos de la coma
ruta = Path("data.txt")
ruta.write_text(
    "Username;Identifier;First name;Last name\\n"
    "booker12;9012;Rachel;Booker\\n"
    "grey07;2070;Laura;Grey\\n"
    "johnson81;4081;Craig;Johnson\\n", encoding="utf-8")

with open(ruta, 'r', encoding="utf-8") as file:
    for line in file:
        parts = line.strip().split(';')
        print(parts)

print()
with open(ruta, 'r', encoding="utf-8") as file:
    header = file.readline().strip().split(';')
    for line in file:
        parts = line.strip().split(';')
        row_dict = dict(zip(header, parts))
        print(row_dict)
"""),

md("""
`readline()` saca una línea y **deja el cursor donde la dejó**, así que el `for` de abajo empieza en la
segunda. Ese es el truco entero de leer el encabezado aparte.

`dict(zip(header, parts))` empareja cada nombre de columna con su valor. Es la misma operación que hace
`csv.DictReader`, escrita a mano, y sirve para cualquier separador.

Fíjate en el `.strip()`. Cada línea de un archivo trae su salto de línea pegado al final, y sin quitarlo
el último campo de cada fila termina con un `\\n` invisible que arruina cualquier comparación.

## El `zip` que se come una columna
"""),

code("""
# FALLA A PROPÓSITO, y no truena. Una fila a la que le falta un campo.
ruta = Path("incompleto.txt")
ruta.write_text(
    "Username;Identifier;First name;Last name\\n"
    "booker12;9012;Rachel;Booker\\n"
    "grey07;2070;Laura\\n"                       # a esta le falta el apellido
    "johnson81;4081;Craig;Johnson\\n", encoding="utf-8")

with open(ruta, encoding="utf-8") as file:
    header = file.readline().strip().split(';')
    filas = [dict(zip(header, l.strip().split(';'))) for l in file]

for f in filas:
    print(f)

print()
print("Campos por fila:", [len(f) for f in filas])
print("¿Todas tienen las cuatro columnas?", all(len(f) == len(header) for f in filas))
print()
for numero, f in enumerate(filas, start=2):
    faltan = [c for c in header if c not in f]
    if faltan:
        print(f"  renglón {numero}: faltan {faltan}")
"""),

md("""
La segunda fila salió con tres llaves y el programa siguió como si nada.

Es el `zip` de la semana 10, ahora leyendo un archivo: se detiene con la lista más corta, y la más corta
era la fila. El diccionario resultante no tiene la llave `Last name`, así que el `KeyError` va a aparecer
mucho después, en el punto donde alguien la use.

Con `strict=True` esto sería un `ValueError` en la línea que lo causó. Sin él, hace falta la comprobación
de las últimas líneas: **contar las columnas de cada fila contra el encabezado**, que es la validación
más barata que existe para un archivo tabular.

## El módulo `csv`
"""),

code("""
import csv

ruta = Path("sample.csv")
ruta.write_text(
    "Username,Identifier,First name,Last name\\n"
    "booker12,9012,Rachel,Booker\\n"
    "grey07,2070,Laura,Grey\\n"
    "smith79,5079,Jamie,Smith\\n", encoding="utf-8")

# Code32.py, líneas 44 a 54: con csv.reader cada fila es una lista
with open(ruta, "r", newline="", encoding="utf-8") as file:
    csv_reader = csv.reader(file)
    data = list(csv_reader)
    header = data.pop(0)

print("Encabezado:", header)
print("Primera fila:", data[0])
print("El apellido, por índice:", data[0][3], "<- hay que saber que es el 3")

print()
# Code32.py, líneas 59 a 71: con DictReader cada fila es un diccionario
with open(ruta, "r", newline="", encoding="utf-8") as file:
    filas = list(csv.DictReader(file))

print("Primera fila:", filas[0])
print("El apellido, por nombre:", filas[0]["Last name"])
print()
print("Y si mañana alguien mete una columna en medio:")
ruta.write_text(
    "Username,Email,Identifier,First name,Last name\\n"
    "booker12,rb@up.edu.mx,9012,Rachel,Booker\\n", encoding="utf-8")
with open(ruta, newline="", encoding="utf-8") as file:
    fila = next(csv.DictReader(file))
print("  por índice [3] daría:", list(fila.values())[3])
print("  por nombre sigue dando:", fila["Last name"])
"""),

md("""
Las dos leen el mismo archivo. La diferencia aparece el día en que alguien agrega una columna.

`csv.reader` entrega listas, y el código que las usa tiene que saber que el apellido es el índice 3. Meter
una columna en medio corre todos los índices y el programa sigue corriendo con los datos cambiados de
lugar.

`csv.DictReader` toma la primera fila como encabezado y entrega diccionarios. El apellido se pide por su
nombre y la columna nueva no le hace nada.

**Regla:** `DictReader` salvo que tengas una razón para lo contrario.

## El `split(",")` del tercer script
"""),

code("""
# FALLA A PROPÓSITO. script3.py, línea 25, con un título que trae coma.
ruta = Path("videogames.csv")
ruta.write_text(
    "The Legend of Zelda: Breath of the Wild,2017,Action-Adventure,Nintendo Switch\\n"
    "Super Mario Wonder,2023,Platformer,Nintendo Switch\\n"
    "God of War,2018,Action,PlayStation 4\\n", encoding="utf-8")


class Videogame:
    def __init__(self, title, year, genre, platform):
        self.title = title
        self.year = year
        self.genre = genre
        self.platform = platform

    def print_info(self):
        print(f"{self.title}, ({self.year}) - {self.genre} - {self.platform}")


def cargar(ruta):
    juegos = []
    with open(ruta, "r", encoding="utf-8") as file:
        for line in file:
            title, year, genre, platform = line.strip().split(",")
            juegos.append(Videogame(title, year, genre, platform))
    return juegos


for juego in cargar(ruta):
    juego.print_info()

print()
print("Ahora con un título que trae coma, que es legal en un CSV:")
with open(ruta, "a", encoding="utf-8") as f:
    f.write('"Crash Bandicoot: N. Sane Trilogy, Remastered",2017,Platformer,PS4\\n')

try:
    cargar(ruta)
except ValueError as e:
    print("  ValueError:", e)
"""),

md("""
`too many values to unpack (expected 4, got 5)`, y el archivo estaba bien escrito.

Un CSV admite comas dentro de un campo siempre que el campo vaya entre comillas. `split(",")` no sabe
nada de comillas: parte por todas las comas, incluidas las que estaban adentro del título.

Los ocho títulos de `videogames.csv` no traen comas, así que `script3.py` funciona hoy. Lo que hace falta
para romperlo es un juego más.

Ese es el patrón de la sesión completa: **el código que funciona con los datos de hoy no es lo mismo que
el código que funciona.** El módulo `csv` sí sabe de comillas, y son dos líneas.
"""),

code("""
import csv
import io

crudo = '"Crash Bandicoot: N. Sane Trilogy, Remastered",2017,Platformer,PS4'

print("Con split(','):   ", crudo.split(","))
print("Con csv.reader:   ", next(csv.reader(io.StringIO(crudo))))
print()

ruta = Path("videogames.csv")
with open(ruta, newline="", encoding="utf-8") as f:
    filas = list(csv.reader(f))

print("Los cuatro renglones, ya partidos bien:")
for fila in filas:
    print(f"  {len(fila)} campos  {fila[0]}")
print()
print("¿Todos con cuatro campos?", all(len(f) == 4 for f in filas))
"""),

md("""
Cuatro campos en las cuatro filas, incluida la que traía la coma adentro.

`csv.reader` sabe leer las comillas, sabe que una comilla doble dentro de un campo entrecomillado se
escribe `""`, y sabe que un salto de línea dentro de comillas no termina la fila. Eso es lo que separa un
formato de una convención.

## Escribir un CSV, y el `newline` que se le pide
"""),

code("""
import csv

filas = [{"nombre": "Ana", "materia": "COM102", "nota": 9.1},
         {"nombre": "Luis", "materia": "COM102", "nota": 6.4},
         {"nombre": "Sofía", "materia": "COM101", "nota": 8.0}]

ruta = Path("reporte.csv")
with open(ruta, "w", newline="", encoding="utf-8") as f:
    escritor = csv.DictWriter(f, fieldnames=["nombre", "materia", "nota"])
    escritor.writeheader()
    escritor.writerows(filas)

print(ruta.read_text(encoding="utf-8"))
print("Los bytes que quedaron en disco:")
print(" ", ruta.read_bytes())

print()
with open(ruta, newline="", encoding="utf-8") as f:
    leidas = list(csv.DictReader(f))

print("Leídas de vuelta:", len(leidas))
print("La primera:", leidas[0])
print("¿La nota volvió como número?", type(leidas[0]["nota"]).__name__)
"""),

md("""
Tres filas escritas y tres leídas, y la nota volvió como cadena.

Eso último es lo que más sorprende del CSV y es su naturaleza: **un CSV no tiene tipos**. Todo lo que sale
de un archivo de texto es texto, y convertir a número es trabajo de quien lee. `DictWriter` escribió
`9.1`; `DictReader` devolvió `'9.1'`.

Fíjate también en los bytes crudos. El módulo `csv` termina cada fila con `\\r\\n`, que es lo que dice el
estándar, y por eso pide `newline=""` al abrir.

## Por qué `newline=""` no es opcional
"""),

code("""
# FALLA A PROPÓSITO, y no truena. Abrir un CSV para escribir sin newline="".
import csv
import os

filas = [["nombre", "nota"], ["Ana", "9.1"], ["Luis", "6.4"]]

with open("con.csv", "w", newline="", encoding="utf-8") as f:
    csv.writer(f).writerows(filas)

with open("sin.csv", "w", encoding="utf-8") as f:
    csv.writer(f).writerows(filas)

print("Este sistema es", "Windows" if os.name == "nt" else "Linux o macOS")
print("  con newline='':", Path("con.csv").read_bytes())
print("  sin newline='':", Path("sin.csv").read_bytes())
print()
print("El modo texto de Windows traduce cada \\\\n a \\\\r\\\\n al escribir.")
print("El módulo csv ya escribió \\\\r\\\\n, así que la traducción lo deja así:")
lo_que_escribe_csv = "nombre,nota\\r\\n"
print("  ", repr(lo_que_escribe_csv.replace("\\n", os.linesep)))
print()
print("Al leerlo, cada \\\\r de sobra queda como un renglón en blanco entre filas.")
print("Con newline='' no hay traducción y el módulo csv escribe lo que quería.")
"""),

md("""
En Linux las dos versiones salen idénticas, y en Windows no.

El modo texto de Windows traduce cada `\\n` a `\\r\\n` al escribir. El módulo `csv` ya escribió `\\r\\n`,
así que la traducción lo convierte en `\\r\\r\\n`, y quien lea el archivo va a ver un renglón en blanco
entre cada dos filas.

Si esta sesión corre sobre Linux, la salida de arriba no muestra el problema y aun así hay que escribir
`newline=""`, porque la tarea se va a abrir en la máquina de alguien más. Es el mismo argumento del
`encoding`: **la corrección de un programa no se mide en la máquina donde se escribió.**
"""),

md("""
---
## Cuatro errores de esta sesión

**Abrir sin `with`.** Lo escrito se queda en el búfer y no llega al disco. Cien renglones y cero bytes,
sin una sola excepción.

**Rutas con barras escritas a mano.** `"datos\\notas.txt"` lleva un salto de línea escondido, y una ruta
relativa depende del directorio desde el que alguien corrió el programa.

**`read()` sobre un archivo grande.** Carga todo en memoria de golpe. Recorrer línea por línea cuesta lo
mismo y siempre cabe.

**Olvidar el `encoding`.** El archivo se lee bien en tu máquina y con los acentos rotos en la de quien
califica, y a veces ni siquiera se lee.
"""),

md("""
---
# Ejercicios

El laboratorio de esta semana es un reporte que sale de un CSV y termina en un archivo de texto. Los
ejercicios construyen hacia eso.

Las soluciones están hasta abajo del cuaderno.

### Ejercicio 1 · Las partes de una ruta

Arma una ruta de tres niveles con `Path` y la diagonal. Imprime `name`, `stem`, `suffix`, `parent`,
`parts` y `exists`.

Después imprime la misma ruta con `PureWindowsPath` y con `PurePosixPath` y explica en un comentario por
qué se ven distintas.

### Ejercicio 2 · La barra invertida

Escribe una ruta como cadena con barras invertidas y un nombre que empiece con `n`. Imprime su `repr` y
su largo, y demuestra que la barra desapareció.

Escríbela de las otras dos maneras correctas.

### Ejercicio 3 · Con `with` y sin él

Escribe cincuenta renglones a un archivo sin cerrarlo e imprime el tamaño en disco. Repítelo con `with`.

Explica en un comentario dónde estaban los datos en el primer caso.

### Ejercicio 4 · Los cinco modos

Escribe un programa que pruebe `r`, `w`, `a` y `x` sobre un archivo que existe y sobre uno que no,
atrapando las excepciones. Imprime una tabla con lo que pasó en cada caso.

### Ejercicio 5 · El encoding

Escribe un archivo con `encoding="latin-1"` y una palabra con eñe. Léelo con `utf-8` y atrapa el
`UnicodeDecodeError`. Léelo con `latin-1` y comprueba que sale bien.

Imprime el encoding por omisión de tu sistema.

### Ejercicio 6 · Línea por línea

Genera un archivo de cien mil renglones. Encuentra el renglón más largo de dos maneras: cargando todo con
`read()` y recorriendo con un `for`.

Compara el tamaño de la variable más grande de cada versión con `getsizeof`.

### Ejercicio 7 · El CSV que se defiende

Escribe un CSV con una fila a la que le falte una columna y otra con una coma dentro de un campo
entrecomillado. Léelo con `DictReader` e imprime, por cada fila, cuántos campos trajo y cuáles faltan.

### Ejercicio 8 · De ida y de vuelta

Escribe una lista de diccionarios a un CSV con `DictWriter` y vuélvela a leer con `DictReader`. Comprueba
que el número de filas coincide y convierte a `float` la columna numérica.

Explica en un comentario por qué esa conversión hace falta.

### Ejercicio 9 · El laboratorio

Te entregan un CSV con cien calificaciones y las columnas `matricula`, `materia` y `nota`. Escribe un
programa que lo lea, saque el promedio por materia y guarde un reporte en un archivo de texto nuevo.

Restricciones: todo acceso va con `with`, todas las rutas con `Path` y todas las aperturas con
`encoding`.

El criterio es que el programa termine bien aunque el CSV venga vacío o le falte una columna.
"""),

md("""
---
## Tres ideas para llevarse

**`Path` arma rutas que sirven en todo.** Unir con la diagonal evita el problema de las barras, el del
carácter de escape escondido y el de la diagonal final que alguien olvidó al concatenar cadenas.

**El `with` cierra aunque truene.** Abrir a mano obliga a escribir un `finally`, y ese `finally` es justo
el que se olvida. Cerrar es lo que vacía el búfer, y sin eso lo escrito no existe.

**El modo `w` borra al abrir.** No al escribir. El archivo queda vacío en el instante en que se abre,
aunque el programa truene antes del primer `write`.

La semana 13 cierra la unidad con los archivos que no se pueden abrir en un editor: bytes en crudo, un
zip tratado como carpeta, y la manera de saltar al registro que interesa sin leer los anteriores. Esta
semana el cursor avanzó solo, un renglón a la vez; la que entra lo mueve a mano.
"""),

md("""
---
# Soluciones

### Ejercicio 1

```python
from pathlib import Path, PureWindowsPath, PurePosixPath

ruta = Path("datos") / "2026" / "alumnos.csv"

for atributo in ["name", "stem", "suffix", "parent", "parts"]:
    print(f"{atributo:<10}{getattr(ruta, atributo)}")
print("exists   ", ruta.exists())

print(PureWindowsPath(ruta))
print(PurePosixPath(ruta))

# Se ven distintas porque cada sistema usa una barra diferente para separar
# carpetas. Path elige la del sistema donde corre; las dos Pure sirven para
# escribir la de otro sistema sin depender de dónde estés.
```

### Ejercicio 2

```python
mala = "datos\\notas.txt"
print(repr(mala), len(mala))
print("¿Quedó la barra?", "\\\\" in mala)

print(repr(str(Path("datos") / "notas.txt")))
print(repr(r"datos\\notas.txt"))
```

### Ejercicio 3

```python
from pathlib import Path

ruta = Path("sin_cerrar.txt")
f = open(ruta, "w", encoding="utf-8")
for i in range(50):
    f.write(f"renglón {i}\\n")
print("Sin cerrar:", ruta.stat().st_size, "bytes")

with open(ruta, "w", encoding="utf-8") as g:
    for i in range(50):
        g.write(f"renglón {i}\\n")
print("Con with:  ", ruta.stat().st_size, "bytes")

# En el primer caso los datos estaban en el búfer de escritura, en memoria.
# El archivo existe y está vacío hasta que alguien cierra.
```

### Ejercicio 4

```python
from pathlib import Path

Path("existe.txt").write_text("hola", encoding="utf-8")
Path("no_existe.txt").unlink(missing_ok=True)

for modo in ["r", "w", "a", "x"]:
    for nombre in ["existe.txt", "no_existe.txt"]:
        try:
            with open(nombre, modo, encoding="utf-8"):
                resultado = "abrió"
        except Exception as e:
            resultado = type(e).__name__
        print(f"{modo:<4}{nombre:<16}{resultado}")
        Path("no_existe.txt").unlink(missing_ok=True)
```

### Ejercicio 5

```python
import locale
from pathlib import Path

ruta = Path("enye.txt")
ruta.write_text("mañana", encoding="latin-1")

try:
    print(ruta.read_text(encoding="utf-8"))
except UnicodeDecodeError as e:
    print("UnicodeDecodeError:", e.reason)

print(ruta.read_text(encoding="latin-1"))
print("Encoding por omisión:", locale.getpreferredencoding(False))
```

### Ejercicio 6

```python
from pathlib import Path
from sys import getsizeof

ruta = Path("cien_mil.txt")
with open(ruta, "w", encoding="utf-8") as f:
    for i in range(100_000):
        f.write(f"{'x' * (i % 60 + 1)}\\n")

with open(ruta, encoding="utf-8") as f:
    todo = f.read()
mayor_a = max(todo.splitlines(), key=len)

with open(ruta, encoding="utf-8") as f:
    mayor_b = ""
    for linea in f:
        if len(linea) > len(mayor_b):
            mayor_b = linea

print("Iguales:", mayor_a == mayor_b.strip())
print("read():   variable más grande", f"{getsizeof(todo):,}", "bytes")
print("for:      variable más grande", f"{getsizeof(mayor_b):,}", "bytes")
```

### Ejercicio 7

```python
import csv
from pathlib import Path

ruta = Path("defensivo.csv")
ruta.write_text(
    'matricula,nombre,materia\\n'
    'A001,Ana Robles,COM102\\n'
    'A002,Luis Ferrer\\n'
    '"A003, provisional",Sofía Ines,COM101\\n', encoding="utf-8")

with open(ruta, newline="", encoding="utf-8") as f:
    lector = csv.DictReader(f)
    columnas = lector.fieldnames
    for numero, fila in enumerate(lector, start=2):
        faltan = [c for c in columnas if fila.get(c) is None]
        print(f"renglón {numero}: {len(fila)} campos",
              f"faltan {faltan}" if faltan else "completo")
```

### Ejercicio 8

```python
import csv
from pathlib import Path

filas = [{"matricula": "A001", "nota": 9.1},
         {"matricula": "A002", "nota": 6.4}]

ruta = Path("ida_vuelta.csv")
with open(ruta, "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=["matricula", "nota"])
    w.writeheader()
    w.writerows(filas)

with open(ruta, newline="", encoding="utf-8") as f:
    leidas = list(csv.DictReader(f))

print("Filas:", len(leidas) == len(filas))
print("Tipo al leer:", type(leidas[0]["nota"]).__name__)
convertidas = [{**r, "nota": float(r["nota"])} for r in leidas]
print("Tras convertir:", type(convertidas[0]["nota"]).__name__)

# Hace falta porque un CSV es un archivo de texto y no guarda tipos. Todo lo
# que sale de él es str, incluida la columna que se escribió como float.
```

### Ejercicio 9

```python
import csv
from pathlib import Path

COLUMNAS = ["matricula", "materia", "nota"]


def leer_capturas(ruta):
    \"\"\"Frontera de entrada: devuelve filas limpias y una lista de problemas.\"\"\"
    buenas, problemas = [], []
    try:
        with open(ruta, newline="", encoding="utf-8") as f:
            lector = csv.DictReader(f)
            if lector.fieldnames is None:
                return [], ["el archivo está vacío"]
            faltantes = [c for c in COLUMNAS if c not in lector.fieldnames]
            if faltantes:
                return [], [f"faltan columnas: {faltantes}"]
            for numero, fila in enumerate(lector, start=2):
                try:
                    buenas.append({"matricula": fila["matricula"],
                                   "materia": fila["materia"],
                                   "nota": float(fila["nota"])})
                except (TypeError, ValueError):
                    problemas.append(f"renglón {numero}: nota "
                                     f"{fila.get('nota')!r} no es un número")
    except FileNotFoundError:
        problemas.append(f"no existe {ruta}")
    return buenas, problemas


def promedios_por_materia(filas):
    agrupado = {}
    for f in filas:
        agrupado.setdefault(f["materia"], []).append(f["nota"])
    return {m: sum(n) / len(n) for m, n in sorted(agrupado.items())}


def lineas_del_reporte(promedios, problemas, total):
    lineas = [f"Capturas leídas: {total}", ""]
    for materia, promedio in promedios.items():
        lineas.append(f"{materia}: {promedio:.2f}")
    if problemas:
        lineas += ["", "Problemas:"] + [f"  {p}" for p in problemas]
    return lineas


def guardar(lineas, ruta):
    with open(ruta, "w", encoding="utf-8") as f:
        f.write("\\n".join(lineas) + "\\n")


if __name__ == "__main__":
    entrada = Path("capturas.csv")
    entrada.write_text(
        "matricula,materia,nota\\n"
        "A001,COM102,9.1\\n"
        "A002,COM102,6.4\\n"
        "A003,COM101,8.0\\n"
        "A004,COM101,siete\\n", encoding="utf-8")

    filas, problemas = leer_capturas(entrada)
    guardar(lineas_del_reporte(promedios_por_materia(filas), problemas, len(filas)),
            Path("reporte_final.txt"))
    print(Path("reporte_final.txt").read_text(encoding="utf-8"))

    filas, problemas = leer_capturas(Path("no_existe.csv"))
    print("Con un archivo que no está:", problemas)
```

Tres decisiones que vale la pena defender en la entrega.

**`leer_capturas` devuelve dos listas y no imprime nada.** Las filas buenas y los problemas salen juntos,
así que el reporte puede decir las dos cosas y la función se prueba con un CSV escrito a mano.

**El archivo vacío y la columna faltante se atienden antes del ciclo.** `fieldnames is None` es la
señal de que el archivo no traía ni encabezado, y comprobar las columnas una sola vez evita repetir la
misma revisión cien veces.

**Todo acceso a disco pasa por `with` y lleva `encoding`.** Las dos reglas del bloque 2, sin excepciones,
incluida la escritura del reporte.
"""),

]

write(OUT / "es" / "w12.ipynb", es)
print("wrote", OUT / "es" / "w12.ipynb")
