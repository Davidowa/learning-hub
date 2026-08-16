"""notebooks/programacion-orientada-a-objetos/es/w13.ipynb

Source deck: ppts/python/programacion-orientada-a-objetos/es/w13.es.yaml
Source code:  docs/en/courses/python-course/03 - Paths and Files/7th Module/Code33.py
                  (json.dumps, json.loads, el archivo pixar_movies.json)
              docs/en/courses/python-course/03 - Paths and Files/7th Module/Code34.py
                  (zipfile: write, namelist, extractall)

Ninguno de los dos se corre desde el repositorio. Code34.py deja files.zip y una
carpeta extracted_files/ dentro de docs/, y Code33.py sobrescribe
pixar_movies.json. El cuaderno reproduce su código en el directorio de trabajo de
la sesión, que en Colab es /content.

Cosas medidas del repositorio que el cuaderno enseña como trampa, sin corregir:

  Code34.py línea 56 abre el zip con "with ZipFile(...) as zip", que tapa la
  función zip de Python para todo lo que venga después. Su propia anotación en el
  deck lo advierte. Medido: llamar a zip(a, b) después de esa línea da
  TypeError: 'ZipFile' object is not callable.

  Code34.py línea 15 guarda el archivo con la ruta relativa completa como nombre
  interno, así que extractall reconstruye el árbol de carpetas dentro de
  extracted_files/. No es un error, pero sorprende y conviene medirlo.

  Code33.py línea 56 escribe el JSON con write_text y sin encoding, así que usa
  el del sistema. Además json.dumps escapa los caracteres no ASCII por omisión,
  y por eso el archivo del repositorio se salva: no hay un solo acento adentro.
  En cuanto una película traiga uno, el archivo depende de la máquina.

  Code33.py línea 12 dice "JSON usually contains a collection of key-value pairs,
  in other words, a dictionary" y su línea 13 anuncia "Lets create a dictionary
  of Pixar movies". Lo que crea es una lista de diccionarios, que es otra cosa y
  es la que el resto del archivo usa.

La semana 12 cerró apuntando aquí: allá el cursor avanzó solo, un renglón a la
vez. Aquí se mueve a mano.

Las semanas 14 y 15 no llevan cuaderno: son PyQt6 y una ventana necesita
pantalla. El cierre de este cuaderno lo dice y el hilo se retoma en la semana 16.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from nbkit import md, code, write, REPO

OUT = REPO / "notebooks" / "programacion-orientada-a-objetos"

es = [

md("""
# Programación Orientada a Objetos · Semana 13
## Tema 5 · Archivos

**COM102 · Facultad de Ingeniería · Profesor David Escobar-Castillejos**

Los archivos que no se pueden abrir en un editor, la manera de saltar al registro que interesa sin leer
los anteriores, y el cierre de la unidad.

La semana pasada el cursor avanzó solo, un renglón a la vez, y nadie tuvo que pensar en él. Esta semana
se mueve a mano, y para eso hay que saber exactamente dónde está.

Al terminar vas a poder:

1. Elegir entre modo texto y modo binario por el contenido del archivo, no por su extensión.
2. Leer y escribir bytes con `rb` y `wb`, sabiendo que `read` cuenta bytes y no caracteres.
3. Calcular dónde empieza el registro n cuando todos los registros miden lo mismo.
4. Decir qué se rompe cuando los registros miden distinto, y por qué el acceso vuelve a ser secuencial.
5. Presentarte al segundo parcial con las unidades 4 y 5 practicadas escribiendo archivos.

### Cómo se usa este cuaderno

Ejecuta las celdas en orden con **Shift + Enter**. Nueve fallan a propósito y llevan un comentario que lo
dice.

Seis de las nueve **no lanzan ninguna excepción**. Dos de esas seis leen un archivo binario sin protestar
y devuelven un byte menos del que había, que es la manera exacta en que una imagen se corrompe sin que
nadie se entere.

Todo lo que este cuaderno escribe se queda en el directorio de trabajo de la sesión. No toca nada del
repositorio.
"""),

md("""
---
# Bloque 1 · Archivos binarios

Todo archivo es una fila de bytes. El modo texto le pone una capa encima que traduce esos bytes a letras
con un encoding y de paso arregla los saltos de línea.

El modo binario quita esa capa y entrega los bytes tal como salieron del disco.
"""),

code("""
from pathlib import Path

# Una imagen PNG de verdad empieza siempre con estos ocho bytes
CABECERA_PNG = bytes([0x89]) + b"PNG" + b"\\r\\n" + bytes([0x1A]) + b"\\n"
ruta = Path("logo.png")
ruta.write_bytes(CABECERA_PNG + b"\\x00\\x00\\x00\\rIHDR" + bytes(range(24)))

with open(ruta, "rb") as archivo:
    cabecera = archivo.read(8)

print("Los primeros ocho bytes:", cabecera)
print("Cuántos leyó:", len(cabecera), "bytes")
print("Tipo:", type(cabecera).__name__)
print()
print("Byte por byte, en decimal y en hexadecimal:")
for i, b in enumerate(cabecera):
    letra = chr(b) if 32 <= b < 127 else "."
    print(f"  {i}  {b:>3}  0x{b:02X}  {letra}")

print()
print("¿Es un PNG?", cabecera == CABECERA_PNG)
print("Tamaño del archivo:", ruta.stat().st_size, "bytes")
"""),

md("""
`read(8)` pidió ocho **bytes**, no ocho caracteres. En binario no existen los caracteres.

Lo que devuelve es un objeto `bytes`, que se parece a una cadena y no lo es: se indexa con enteros de 0 a
255 y no tiene idea de qué letra representa cada uno.

Esos ocho bytes son la firma de un PNG y están ahí a propósito. El tercero, cuarto y quinto son las
letras `PNG`; el primero es `0x89`, que es un byte imposible en un archivo de texto ASCII, y el
`\\r\\n` de en medio existe para detectar exactamente el error de las siguientes dos celdas.

## Abrir un binario en modo texto
"""),

code("""
# FALLA A PROPÓSITO. Un PNG leído como si fuera texto.
ruta = Path("logo.png")

try:
    contenido = ruta.read_text(encoding="utf-8")
except UnicodeDecodeError as e:
    print("UnicodeDecodeError")
    print("  motivo:  ", e.reason)
    print("  posición:", e.start)
    print("  el byte: ", hex(e.object[e.start]))

print()
print("El byte 0x89 no puede empezar un carácter de utf-8, y por eso truena")
print("antes de alcanzar a leer nada.")
"""),

md("""
`invalid start byte` en la posición 0.

`utf-8` tiene reglas sobre qué bytes pueden empezar un carácter, y `0x89` no es uno de ellos. La lectura
se detiene en el primer byte del archivo.

Este es el caso bueno. **La lectura truena antes de romper nada**, y el mensaje dice dónde. El caso malo
es el de la celda siguiente.

## Cuando el modo texto no protesta
"""),

code("""
# FALLA A PROPÓSITO, y no truena. El mismo PNG, con un encoding que acepta todo.
ruta = Path("logo.png")

crudos = ruta.read_bytes()
como_texto = ruta.read_text(encoding="latin-1")

print("Bytes en el disco:      ", len(crudos))
print("Caracteres que devolvió:", len(como_texto))
print("Diferencia:", len(crudos) - len(como_texto), "byte")
print()
print("Los primeros ocho, comparados:")
print("  del disco: ", list(crudos[:8]))
print("  del texto: ", [ord(c) for c in como_texto[:8]])
print()
print("El 13 desapareció. Es el \\\\r del \\\\r\\\\n de la firma:")
print("  el modo texto traduce \\\\r\\\\n a \\\\n y se come un byte")
print()
de_vuelta = como_texto.encode("latin-1")
Path("copia.png").write_bytes(de_vuelta)
print("Si guardas eso como imagen:")
print("  ¿mismo tamaño?", Path("copia.png").stat().st_size == ruta.stat().st_size)
print("  ¿sigue siendo un PNG?", de_vuelta[:8] == crudos[:8])
"""),

md("""
Ningún error, un byte menos, y una imagen que ya no abre.

`latin-1` asigna una letra a cada uno de los 256 bytes posibles, así que nunca falla al decodificar. Con
eso desaparece la protección de la celda anterior y aparece el problema de verdad: **el modo texto
también traduce los saltos de línea**.

Un `\\r\\n` dentro de un archivo se convierte en `\\n` al leerlo en modo texto, porque Python normaliza los
finales de línea de los tres sistemas. En un archivo de texto eso es lo que quieres. Adentro de un PNG,
de un ZIP o de un ejecutable, es un byte borrado en medio de los datos.

Es exactamente el riesgo que anuncia la diapositiva: *"o peor, lee basura sin quejarse"*.

## El mismo daño, en cuatro bytes
"""),

code("""
# FALLA A PROPÓSITO, y no truena. Ida y vuelta por el modo texto.
Path("crudo.bin").write_bytes(b"A\\r\\nB")

crudos = Path("crudo.bin").read_bytes()
texto = Path("crudo.bin").read_text(encoding="latin-1")

print("Escrito:  ", crudos, f"({len(crudos)} bytes)")
print("Leído en texto:", repr(texto), f"({len(texto)} caracteres)")
print()
print("¿Volvieron los mismos bytes?", texto.encode("latin-1") == crudos)
print()
print("Y en modo binario:")
print("  ", Path("crudo.bin").read_bytes() == crudos)
print()
print("Esto pasa en Windows, en Linux y en macOS por igual, porque la traducción")
print("de \\\\r\\\\n a \\\\n la hace Python al leer, no el sistema operativo.")
"""),

md("""
Cuatro bytes entran, tres caracteres salen, y ninguna excepción.

Es el mismo mecanismo de la celda anterior en su versión más pequeña posible. Vale la pena tenerlo
presente porque `\\r\\n` aparece por todos lados: en los CSV que escribió la semana pasada, en las
cabeceras de red, y dentro de cualquier archivo binario por pura casualidad estadística.

**La regla es de una línea: el modo se elige por el contenido del archivo, no por su extensión.** Un
`.dat` con texto adentro se abre en texto. Un `.txt` que en realidad trae bytes se abre en binario.

## Las cinco diferencias, medidas
"""),

code("""
Path("texto.txt").write_text("Ana,9.2\\nLuis,7.8\\n", encoding="utf-8")

with open("texto.txt", encoding="utf-8") as f:
    en_texto = f.read()
with open("texto.txt", "rb") as f:
    en_binario = f.read()

filas = [
    ("Cómo se abre", 'open(ruta, encoding="utf-8")', 'open(ruta, "rb")'),
    ("Qué devuelve read", type(en_texto).__name__, type(en_binario).__name__),
    ("Largo de lo leído", str(len(en_texto)), str(len(en_binario))),
    ("Qué es cada elemento", repr(en_texto[0]), repr(en_binario[0])),
    ("Encoding", "obligatorio en la práctica", "no aplica"),
]

print(f"{'Aspecto':<22}{'Modo texto':<30}{'Modo binario'}")
for aspecto, texto, binario in filas:
    print(f"{aspecto:<22}{texto:<30}{binario}")

print()
print("Un elemento de bytes es un entero:", en_binario[0], "que es la A")
print("Un elemento de str es un carácter:", repr(en_texto[0]))
print()
print("Y para pasar de uno a otro:")
print("  texto -> bytes:", repr("Ana".encode("utf-8")))
print("  bytes -> texto:", repr(b"Ana".decode("utf-8")))
"""),

md("""
El renglón que más sorprende es el cuarto. **Indexar un objeto `bytes` devuelve un entero, no un byte.**

`b"Ana"[0]` es `65`, no `b"A"`. Cortarlo sí devuelve bytes: `b"Ana"[0:1]` es `b"A"`. Esa asimetría es la
fuente de la mitad de los errores de quien empieza con binarios.

`encode` y `decode` son el puente entre los dos mundos, y las dos palabras dicen hacia dónde: **codificar
es de texto a bytes, decodificar es de bytes a texto**.

## Un binario tratado como carpeta
"""),

code("""
# Code34.py, líneas 8 a 16 y 56 a 64, en el directorio de trabajo
from zipfile import ZipFile

carpeta = Path("datos")
carpeta.mkdir(exist_ok=True)
(carpeta / "alumnos.csv").write_text("matricula,nota\\nA001,9.2\\n", encoding="utf-8")
(carpeta / "materias.csv").write_text("clave,nombre\\nCOM102,POO\\n", encoding="utf-8")
(carpeta / "notas.txt").write_text("apuntes", encoding="utf-8")

with ZipFile("entrega.zip", "w") as paquete:
    for archivo in carpeta.rglob("*.csv"):
        paquete.write(archivo)

print("Tamaño del zip:", Path("entrega.zip").stat().st_size, "bytes")
print()
with ZipFile("entrega.zip") as paquete:
    print("Lo que trae adentro:", paquete.namelist())
    for info in paquete.infolist():
        print(f"  {info.filename:<22}{info.file_size:>4} bytes ->"
              f" {info.compress_size:>4} comprimidos")

print()
with ZipFile("entrega.zip") as paquete:
    paquete.extractall("extraidos")

print("Lo que quedó en el disco:")
for p in sorted(Path("extraidos").rglob("*")):
    print("  ", p)
"""),

md("""
Un zip es un archivo binario y `zipfile` lo trata como si fuera una carpeta. Nunca hay que tocar un byte.

Fíjate en `namelist()`. Los nombres de adentro traen la ruta **relativa completa** con la que se
agregaron, así que `extractall` reconstruye el árbol de carpetas. `Code34.py` guarda
`03 - Paths and Files/7th Module/test.txt`, y al extraerlo recrea esas dos carpetas. Si quieres que
adentro solo esté el nombre, hay que decirlo: `paquete.write(archivo, arcname=archivo.name)`.

`rglob` recorre también las subcarpetas; `glob` se queda en el nivel de arriba y nada más. Y `notas.txt`
no entró al zip porque el patrón pedía `*.csv`.

## La variable que tapó una función de Python
"""),

code("""
# FALLA A PROPÓSITO. Code34.py, línea 56, con su nombre de variable tal cual.
from zipfile import ZipFile

nombres = ["Ana", "Luis", "Sofía"]
notas = [9.2, 7.8, 9.5]

print("Antes:", list(zip(nombres, notas)))
print()

with ZipFile("entrega.zip", "r") as zip:
    print(zip.namelist())

print()
try:
    list(zip(nombres, notas))
except TypeError as e:
    print("Después:", type(e).__name__ + ":", e)

print()
del zip
print("Recuperada:", list(zip(nombres, notas)))
"""),

md("""
`'ZipFile' object is not callable`, y la línea que falló no tenía nada que ver con archivos.

`with ... as zip` asigna a `zip` como cualquier otra asignación, y esa asignación **sobrevive al bloque**.
De ahí en adelante, `zip` en ese módulo es el archivo comprimido y no la función de Python.

Es el mismo error que el `sum` de la semana 10 y la anotación del deck lo dice con todas sus letras: *"No
le pongas zip a la variable, porque tapa la función zip que trae Python"*. Aquí duele más porque `zip` y
`ZipFile` se usan en el mismo tipo de programa.

En `Code34.py` no se nota porque el archivo termina dos líneas después. En un programa de verdad, el
error aparece donde alguien quiera recorrer dos listas en paralelo.

## JSON: texto que se ve como un diccionario
"""),

code("""
# Code33.py, líneas 15 a 63, con tres películas en lugar de veintiséis
import json

pixar_movies = [
    {"id": 1, "title": "Toy Story", "year": 1995},
    {"id": 19, "title": "Coco", "year": 2017},
    {"id": 25, "title": "Turning Red", "year": 2022},
]

print("Lo que el archivo llama 'a dictionary of Pixar movies' es de tipo:",
      type(pixar_movies).__name__)
print("Y cada elemento sí es un:", type(pixar_movies[0]).__name__)
print()

json_string = json.dumps(pixar_movies)
print("Como texto:", json_string)
print("Tipo:", type(json_string).__name__)
print()

file_path = Path("pixar_movies.json")
file_path.write_text(json_string, encoding="utf-8")

data = file_path.read_text(encoding="utf-8")
read_pixar_movies = json.loads(data)

print("De vuelta en Python:", type(read_pixar_movies).__name__,
      "con", len(read_pixar_movies), "elementos")
print("¿Sobrevivió el viaje completo?", read_pixar_movies == pixar_movies)
print("El año sigue siendo un número:", type(read_pixar_movies[0]["year"]).__name__)
"""),

md("""
El viaje de ida y vuelta salió intacto, y el año volvió como número.

Esa es la diferencia grande con el CSV de la semana pasada. **Un CSV no tiene tipos y un JSON sí**: el
formato distingue números, cadenas, booleanos, nulos, listas y objetos, así que `json.loads` devuelve las
estructuras de Python que le corresponden sin que nadie convierta nada.

`Code33.py` llama diccionario a lo que crea, y lo que crea es una **lista de diccionarios**. La distinción
importa porque el resto del archivo la recorre con un `for`, que es lo que se hace con una lista, y
porque en la semana 16 esa lista se convierte en una tabla donde cada elemento es un renglón.

## El acento que todavía no ha llegado
"""),

code("""
# FALLA A PROPÓSITO, y no truena. Code33.py, línea 56: write_text sin encoding.
import json
import locale

con_acento = [{"id": 27, "title": "El Niño y la Garza", "year": 2023}]

sin_ensure = json.dumps(con_acento)
print("json.dumps por omisión:", sin_ensure)
print("  <- la ñ se escapó como \\\\u00f1, así que el archivo sale en ASCII puro")
print()
print("Y por eso escribirlo sin encoding funciona en cualquier máquina:")
Path("escapado.json").write_text(sin_ensure)
print("  bytes en disco:", Path("escapado.json").read_bytes()[:44], "...")
print("  encoding por omisión de esta máquina:",
      locale.getpreferredencoding(False))
print()

legible = json.dumps(con_acento, ensure_ascii=False)
print("Con ensure_ascii=False:", legible)
Path("legible.json").write_text(legible, encoding="utf-8")
print("  bytes en disco:", Path("legible.json").read_bytes()[:44], "...")
print()
print("Las dos versiones cargan al mismo objeto:",
      json.loads(sin_ensure) == json.loads(legible))
"""),

md("""
`Code033.py` escribe el JSON sin `encoding` y se salva por un pelo.

`json.dumps` escapa todo lo que no sea ASCII por omisión: la eñe sale como `\\u00f1`. El archivo resultante
solo tiene bytes por debajo de 128, y esos significan lo mismo en todos los encodings del mundo, así que
`write_text` sin `encoding` produce el mismo archivo en cualquier máquina.

El día que alguien escriba `ensure_ascii=False` para que el archivo se lea mejor, esa protección
desaparece y el archivo pasa a depender del encoding del sistema. La versión correcta lleva las dos
cosas: `ensure_ascii=False` para que sea legible y `encoding="utf-8"` para que no dependa de nadie.

Las veintiséis películas del repositorio no traen un solo acento. Ese es el único motivo por el que
`Code33.py` funciona.
"""),

md("""
---
# Bloque 2 · Acceso secuencial y aleatorio

Todo archivo abierto tiene un cursor. Leer lo empuja hacia adelante, y hay una manera de moverlo a donde
quieras.
"""),

code("""
Path("registros.bin").write_bytes(bytes(range(256)) * 2)

with open("registros.bin", "rb") as f:
    print("Al abrir, el cursor está en:", f.tell())
    f.seek(64)
    print("Después de seek(64):       ", f.tell())
    datos = f.read(32)
    print("Después de read(32):       ", f.tell())
    print("  y leyó", len(datos), "bytes:", datos[:8], "...")
    f.seek(0)
    print("Después de seek(0):        ", f.tell())
    f.seek(-16, 2)
    print("Después de seek(-16, 2):   ", f.tell(), "<- 2 quiere decir 'desde el final'")
    print("  los últimos 16 bytes:", f.read())
"""),

md("""
`tell()` devuelve la posición actual del cursor, contada en **bytes desde el principio**.

Leer lo empuja: después de `read(32)` el cursor avanzó exactamente 32. `seek` lo pone donde le digas sin
leer nada en el camino, que es la diferencia entera entre acceso secuencial y acceso aleatorio.

El segundo argumento de `seek` dice desde dónde se cuenta: `0` desde el principio, que es lo de siempre,
`1` desde la posición actual, y `2` desde el final. `seek(-16, 2)` es la manera de leer la cola de un
archivo sin recorrerlo.

## Predice antes de correr

```python
with open("datos.bin", "wb") as f:
    f.write(b"ABCDEFGH")

with open("datos.bin", "rb") as f:
    f.seek(3)
    print(f.read(2))
```

- **A.** `b'DE'`, porque el cursor queda antes de la cuarta letra.
- **B.** `b'CD'`, porque `seek` empieza a contar en uno.
- **C.** `b'ABCDEFGH'`, porque `seek` no afecta lo que lee `read`.
- **D.** Un error, `seek` no funciona en modo binario.
"""),

code("""
with open("datos.bin", "wb") as f:
    f.write(b"ABCDEFGH")

print("El archivo, con sus posiciones:")
print("  posición:", "".join(f"{i:>4}" for i in range(8)))
print("  byte:    ", "".join(f"{chr(b):>4}" for b in b"ABCDEFGH"))
print()

with open("datos.bin", "rb") as f:
    print("Cursor al abrir:  ", f.tell())
    f.seek(3)
    print("Cursor tras seek: ", f.tell())
    leido = f.read(2)
    print("read(2) devolvió: ", leido)
    print("Cursor tras read: ", f.tell())
"""),

md("""
La respuesta es **A**.

Las posiciones se cuentan desde cero, igual que los índices de una lista. La posición 3 no está *sobre* la
cuarta letra: está **justo antes** de ella, en la ranura entre la `C` y la `D`. `read(2)` toma esa y la
siguiente.

La tabla de arriba lo dice mejor que cualquier explicación: la posición es la ranura, no la casilla.

## Saltar al registro n
"""),

code("""
import time

TAM = 32
N = 200_000

with open("padron.bin", "wb") as f:
    for i in range(N):
        matricula = f"A{i:06d}".encode("ascii")
        nombre = f"alumno-{i}".encode("ascii")
        f.write(matricula.ljust(8) + nombre.ljust(24))

print("Registros:", f"{N:,}", " tamaño del archivo:",
      f"{Path('padron.bin').stat().st_size:,}", "bytes")
print("¿Cuadra con N * TAM?", Path("padron.bin").stat().st_size == N * TAM)
print()

print(f"{'registro':>10}{'con seek':>14}{'secuencial':>14}{'¿el mismo?':>14}")
with open("padron.bin", "rb") as f:
    for buscado in [1_000, 50_000, 150_000]:
        inicio = time.perf_counter()
        f.seek(buscado * TAM)
        con_seek = f.read(TAM)
        costo_seek = time.perf_counter() - inicio

        inicio = time.perf_counter()
        f.seek(0)
        for _ in range(buscado):
            f.read(TAM)
        secuencial = f.read(TAM)
        costo_secuencial = time.perf_counter() - inicio

        print(f"{buscado:>10,}{costo_seek:>14.6f}{costo_secuencial:>14.6f}"
              f"{str(con_seek == secuencial):>14}")

print()
print("La columna del seek no crece. La del recorrido se multiplica con el número")
print("de registro, porque de verdad los está leyendo todos.")
"""),

md("""
El mismo registro por los dos caminos, y una de las dos columnas no se mueve.

La cuenta es toda la idea: **si todos los registros miden lo mismo, el registro `n` empieza en
`n * TAM`**. `seek` va directo a ese byte, así que leer el registro mil cuesta exactamente lo mismo que
leer el ciento cincuenta mil. El recorrido secuencial no: cada registro que hay antes se lee de verdad, y
por eso su columna crece con el número que busques.

Fíjate en el `ljust`. Cada campo se rellena hasta su ancho fijo, y por eso la cuenta funciona. Ese relleno
es el precio del acceso aleatorio: el archivo ocupa más de lo que necesita a cambio de que la posición se
pueda calcular.

## Cuando los registros miden distinto
"""),

code("""
# FALLA A PROPÓSITO, y no truena. La misma cuenta sobre registros de largo variable.
NOMBRES = ["Ana", "Luis", "Sofía", "Marco", "Paula Elena", "Rubén"]

with open("variable.bin", "wb") as f:
    for i, nombre in enumerate(NOMBRES):
        f.write(f"A{i:03d}{nombre}\\n".encode("utf-8"))

print("Contenido:", Path("variable.bin").read_bytes())
print("Tamaño:", Path("variable.bin").stat().st_size, "bytes")
print()

TAM_SUPUESTO = 10
for buscado in [0, 2, 4]:
    with open("variable.bin", "rb") as f:
        f.seek(buscado * TAM_SUPUESTO)
        print(f"  registro {buscado} 'según la cuenta':", f.read(TAM_SUPUESTO))

print()
print("Lo que de verdad hay en cada posición:")
with open("variable.bin", "rb") as f:
    for i, linea in enumerate(f):
        print(f"  registro {i}: {linea!r}")
"""),

md("""
Tres saltos, tres pedazos de registro cortados por la mitad, y ninguna excepción.

Cuando cada registro mide distinto, no hay multiplicación que dé la posición. La cuenta sigue
funcionando, sigue devolviendo bytes, y esos bytes son basura: media matrícula de uno y medio nombre del
siguiente.

Es el error 02 de la diapositiva. **El acceso aleatorio exige registros del mismo tamaño**, y cuando no
los hay, o se recorre el archivo desde el principio, o se guarda aparte un índice que diga en qué byte
empieza cada registro. Eso segundo es, en dos frases, lo que hace una base de datos, y es a donde va la
semana 16.

## El registro más corto que el anterior
"""),

code("""
# FALLA A PROPÓSITO, y no truena. Sobrescribir sin rellenar hasta el tamaño fijo.
TAM = 8

with open("fijo.bin", "wb") as f:
    for nombre in [b"ANA00000", b"LUIS0000", b"SOFIA000"]:
        f.write(nombre)

print("Antes: ", Path("fijo.bin").read_bytes())

with open("fijo.bin", "r+b") as f:
    f.seek(1 * TAM)
    f.write(b"ED")                     # el registro nuevo mide dos, no ocho

print("Después:", Path("fijo.bin").read_bytes())
print()
with open("fijo.bin", "rb") as f:
    for i in range(3):
        f.seek(i * TAM)
        print(f"  registro {i}: {f.read(TAM)}")

print()
print("Con el relleno que hacía falta:")
with open("fijo.bin", "r+b") as f:
    f.seek(1 * TAM)
    f.write(b"ED".ljust(TAM, b"0"))

with open("fijo.bin", "rb") as f:
    for i in range(3):
        f.seek(i * TAM)
        print(f"  registro {i}: {f.read(TAM)}")
"""),

md("""
El registro nuevo midió dos bytes y los otros seis del anterior se quedaron ahí.

Escribir en medio de un archivo **sobrescribe** exactamente los bytes que escribas y no toca ni uno más.
No hay ningún concepto de "borrar el registro": si el nuevo es más corto, lo que sobra del viejo sigue en
el disco y el siguiente `read(TAM)` lo devuelve pegado.

Es el error 03 de la diapositiva. La corrección es `ljust` hasta el tamaño fijo, que es la misma
disciplina del padrón de hace dos celdas.

Fíjate en el modo `r+b`. `wb` habría vaciado el archivo al abrirlo, que es el error de la semana pasada;
`r+b` abre para leer y escribir **conservando** lo que había, y es el modo que pide el acceso aleatorio.

## Saltar más allá del final
"""),

code("""
# FALLA A PROPÓSITO, y no truena. seek más allá del final y escribir.
with open("hueco.bin", "wb") as f:
    f.write(b"INICIO")
    print("Cursor tras escribir:", f.tell())
    f.seek(20)
    print("Cursor tras seek(20):", f.tell())
    f.write(b"FINAL")

crudos = Path("hueco.bin").read_bytes()
print()
print("Bytes en disco:", crudos)
print("Tamaño:", len(crudos))
print()
print("Lo que hay entre la posición 6 y la 20:", crudos[6:20])
print("Todos ceros:", crudos[6:20] == bytes(14))
print()
print("Y leído como texto, esos ceros son caracteres perfectamente válidos:")
print(" ", repr(crudos.decode("latin-1")))
"""),

md("""
Catorce bytes en cero aparecieron en medio del archivo, y nadie dijo nada.

Es el error 04 de la diapositiva. `seek` no comprueba nada: acepta cualquier posición, incluidas las que
están más allá del final. Escribir ahí obliga al sistema a rellenar el hueco, y lo rellena con ceros.

Ese relleno cuenta como contenido. El archivo mide 25 bytes, se lee sin problemas, y quien lo procese
después va a encontrar catorce bytes nulos que nadie escribió. En un archivo de registros fijos, eso son
casi dos registros fantasma.

**Antes de un `seek` calculado, la posición se compara contra el tamaño del archivo.** Una línea:
`if posicion > ruta.stat().st_size: ...`

## `seek` en modo texto
"""),

code("""
# FALLA A PROPÓSITO. Un salto que cae a media letra.
ruta = Path("acentos.txt")
ruta.write_text("niño y más", encoding="utf-8")

print("Como texto: ", ruta.read_text(encoding="utf-8"))
print("Como bytes: ", ruta.read_bytes())
print("Caracteres:", len(ruta.read_text(encoding='utf-8')),
      " bytes:", len(ruta.read_bytes()))
print("  <- la ñ y la á ocupan dos bytes cada una")
print()

with open(ruta, encoding="utf-8") as f:
    f.seek(3)
    try:
        print("Desde la posición 3:", repr(f.read()))
    except UnicodeDecodeError as e:
        print("UnicodeDecodeError:", e.reason)
        print("  la posición 3 cae en medio de los dos bytes de la ñ")

print()
with open(ruta, encoding="utf-8") as f:
    posicion = f.tell()
    f.read(3)
    guardada = f.tell()
    f.seek(guardada)
    print("Con una posición devuelta por tell():", repr(f.read()))
"""),

md("""
En modo texto, las posiciones no son bytes ni son caracteres. Son valores opacos que solo `tell()` sabe
producir.

La celda lo enseña con una eñe: ocupa dos bytes en `utf-8`, así que `seek(3)` cae entre los dos y el
decodificador se queda sin manera de armar el carácter.

Es el error 01 de la diapositiva. **En modo texto, `seek` solo acepta las posiciones que devolvió
`tell()`**, y el `0` del principio. Cualquier otra cosa es apostar.

Si necesitas saltar a un byte concreto, el archivo se abre en binario y se decodifica a mano el pedazo
que leíste. Esa es la razón técnica por la que los archivos de registros fijos se guardan en binario y no
en texto.
"""),

md("""
---
# Bloque 3 · Segundo parcial

Cierra las unidades 4 y 5. Todo lo que entra se practicó en un laboratorio, con el archivo escribiéndose
en disco.

| Unidad | Qué entra |
|---|---|
| U4 | Parámetros, modularidad, recursividad, colecciones, arreglos dinámicos y manejo de excepciones |
| U5 | Rutas, modos de apertura, texto, CSV, binarios y acceso secuencial y aleatorio |
| Base | El modelado de las unidades 1 a 3, porque el examen pide clases que lean y escriban archivos |
| Fuera | Interfaces gráficas y bases de datos, que se evalúan en el proyecto y en el examen final |

**Cómo se estudia.** Cada pregunta de la unidad 5 se contesta escribiendo un archivo y volviéndolo a
leer. Si no lo practicaste corriendo el código, no lo practicaste.

La celda de abajo es un simulacro corto. Corre las nueve preguntas, se califica sola, y las que falles te
dicen a qué semana volver.
"""),

code("""
from pathlib import Path

PREGUNTAS = []


def pregunta(enunciado, semana, obtenido, esperado):
    PREGUNTAS.append((enunciado, semana, obtenido, esperado))


# 1. El valor por omisión mutable (semana 09)
def agregar(x, lista=[]):
    lista.append(x)
    return lista


agregar("a")
pregunta("Una lista por omisión, tras dos llamadas", 9, len(agregar("b")), 2)

# 2. El alias (semana 10)
a = [1, 2, 3]
b = a
b.append(4)
pregunta("copia = lista y después append", 10, len(a), 4)

# 3. Borrar mientras se recorre (semana 10)
nums = [2, 4, 6, 8]
for n in nums:
    if n % 2 == 0:
        nums.remove(n)
pregunta("Borrar pares dentro del for", 10, nums, [4, 8])

# 4. zip corta con la más corta (semana 10)
pregunta("zip de 5 y 3 elementos", 10, len(list(zip(range(5), range(3)))), 3)

# 5. finally corre con un return pendiente (semana 11)
orden = []


def leer():
    try:
        return "valor"
    finally:
        orden.append("finally")


leer()
pregunta("¿Corrió el finally con un return esperando?", 11, orden, ["finally"])

# 6. El orden de los except (semana 11)
def clasificar(ruta):
    try:
        return Path(ruta).read_text(encoding="utf-8")
    except OSError:
        return "general"
    except FileNotFoundError:
        return "específico"


pregunta("except OSError antes que FileNotFoundError", 11,
         clasificar("no_existe_jamas.txt"), "general")

# 7. El modo w vacía al abrir (semana 12)
p = Path("parcial.txt")
p.write_text("primera", encoding="utf-8")
f = open(p, "w", encoding="utf-8")
pregunta("Bytes tras abrir en w, antes de escribir", 12, p.stat().st_size, 0)
f.close()

# 8. Un CSV no tiene tipos (semana 12)
import csv
p = Path("parcial.csv")
p.write_text("nombre,nota\\nAna,9.1\\n", encoding="utf-8")
with open(p, newline="", encoding="utf-8") as f:
    fila = next(csv.DictReader(f))
pregunta("Tipo de la columna nota al leerla", 12, type(fila["nota"]).__name__, "str")

# 9. Las posiciones arrancan en cero (semana 13)
Path("parcial.bin").write_bytes(b"ABCDEFGH")
with open("parcial.bin", "rb") as f:
    f.seek(3)
    leido = f.read(2)
pregunta("seek(3) y read(2) sobre ABCDEFGH", 13, leido, b"DE")

aciertos = 0
print(f"{'#':<3}{'sem':<6}{'pregunta':<48}{'resultado'}")
for i, (enunciado, semana, obtenido, esperado) in enumerate(PREGUNTAS, start=1):
    ok = obtenido == esperado
    aciertos += ok
    print(f"{i:<3}{semana:<6}{enunciado:<48}{obtenido!r}"
          f"{'' if ok else f'  <- se esperaba {esperado!r}'}")

print()
print(f"Predicciones que coincidieron: {aciertos} de {len(PREGUNTAS)}")
print("Si alguna te sorprendió, la columna 'sem' dice a qué cuaderno volver.")
"""),

md("""
Las nueve son comportamientos, no definiciones, y las nueve aparecen en el examen convertidas en código
que hay que escribir.

Ninguna se contesta releyendo una diapositiva. Se contestan tecleando, que es lo que la celda acaba de
hacer.

**Lo que hay que revisar antes del parcial:** los modos de apertura y qué hace cada uno cuando el archivo
ya existía. Es de lo poco que hay que saber de memoria, porque equivocarse ahí borra el archivo de
entrada.

**Lo que no vale la pena memorizar:** los métodos de `Path`. Están a un tabulador de distancia dentro del
editor y el examen se presenta con el repositorio del curso abierto.
"""),

md("""
---
## Cuatro errores de esta sesión

**Mezclar `seek` con modo texto.** En texto, `seek` solo acepta las posiciones que devolvió `tell`.
Cualquier otra cae a media letra.

**Registros de tamaño variable.** Si cada renglón mide distinto no hay cuenta que dé la posición, y el
acceso vuelve a ser secuencial.

**Escribir un registro más corto.** Lo que sobra del anterior se queda ahí. Hay que rellenar hasta el
tamaño fijo.

**Creer que `seek` avisa.** Saltar más allá del final y escribir deja ceros en medio del archivo, sin
ningún error.
"""),

md("""
---
# Ejercicios

El laboratorio de esta semana es un simulacro del segundo parcial en parejas. Los ejercicios construyen
hacia eso.

Las soluciones están hasta abajo del cuaderno.

### Ejercicio 1 · La firma de un archivo

Escribe a mano los primeros bytes de un PNG, un ZIP y un PDF, y una función que abra un archivo en
binario, lea los primeros ocho bytes y adivine de cuál se trata.

Pruébala con un archivo de texto y comprueba que dice que no lo reconoce.

### Ejercicio 2 · El byte que se pierde

Escribe un archivo binario que contenga `\\r\\n` en medio. Léelo en binario y en texto con `latin-1`, y
compara los largos.

Explica en un comentario quién se comió el byte.

### Ejercicio 3 · De texto a bytes y de vuelta

Toma una cadena con acentos. Conviértela a bytes con `utf-8` y con `latin-1`, imprime los dos y compara
los largos.

Después intenta decodificar los bytes de `utf-8` como `latin-1` e imprime lo que sale.

### Ejercicio 4 · El zip

Crea tres archivos, mételos en un zip con `rglob`, imprime `namelist()` y `infolist()`, y extráelos a
otra carpeta.

Repite el ejercicio pasando `arcname` para que adentro solo esté el nombre del archivo.

### Ejercicio 5 · El cursor

Escribe un archivo de veintiséis bytes con el abecedario. Imprime `tell()` después de cada operación de
una secuencia de al menos seis `seek` y `read`, incluyendo uno con `whence=2`.

### Ejercicio 6 · Registros fijos

Guarda diez alumnos con matrícula de ocho bytes y nombre de veinticuatro, rellenando con `ljust`. Lee el
séptimo con una sola llamada a `seek` y comprueba que el tamaño del archivo es diez por treinta y dos.

### Ejercicio 7 · Registros variables

Guarda los mismos diez alumnos sin rellenar. Intenta leer el séptimo con la misma cuenta y muestra la
basura que sale.

Explica en un comentario qué haría falta para poder saltar.

### Ejercicio 8 · El hueco

Escribe cinco bytes, salta a la posición cincuenta y escribe cinco más. Imprime el tamaño del archivo y
lo que hay en medio.

Agrega la comprobación de una línea que lo habría evitado.

### Ejercicio 9 · El laboratorio

En parejas, cada quien escribe un enunciado corto que exija leer un CSV, calcular algo y escribir un
archivo nuevo. Lo intercambian con la otra pareja y resuelven el que les tocó.

Restricciones: el enunciado cabe en cinco renglones y admite una sola interpretación posible.

Entregan el enunciado propio, la solución del ajeno y una nota de qué quedó ambiguo. El criterio es que
la solución corra con el archivo de prueba sin tener que editar ninguna ruta.
"""),

md("""
---
## Tres ideas para llevarse

**El modo binario no traduce nada.** Ni saltos de línea ni acentos. Lo que está en el disco es exactamente
lo que llega a memoria, y el modo texto no siempre avisa cuando cambió algo.

**El acceso aleatorio pide registros iguales.** Si cada registro mide distinto no hay multiplicación que
dé la posición, y toca leer todo o guardar un índice aparte.

**Las posiciones se cuentan desde cero.** `seek(3)` deja el cursor antes del cuarto byte, con la misma
lógica que un índice de lista, y no comprueba absolutamente nada.

Con esto cierra la unidad de archivos. Las semanas 14 y 15 son interfaces gráficas con PyQt6 y no llevan
cuaderno, porque una ventana necesita una pantalla y Colab no la tiene: se trabajan en clase, sobre el
editor. El hilo se retoma en la semana 16, donde este mismo problema de guardar y recuperar datos se
resuelve otra vez, y donde el índice que hoy habría que escribir a mano viene incluido.
"""),

md("""
---
# Soluciones

### Ejercicio 1

```python
from pathlib import Path

FIRMAS = {
    bytes([0x89]) + b"PNG\\r\\n\\x1a\\n": "PNG",
    b"PK\\x03\\x04": "ZIP",
    b"%PDF-": "PDF",
}


def reconocer(ruta):
    with open(ruta, "rb") as f:
        cabecera = f.read(8)
    for firma, nombre in FIRMAS.items():
        if cabecera.startswith(firma):
            return nombre
    return "no reconocido"


Path("a.png").write_bytes(bytes([0x89]) + b"PNG\\r\\n\\x1a\\n" + b"resto")
Path("a.txt").write_text("hola", encoding="utf-8")

print(reconocer("a.png"))
print(reconocer("a.txt"))
```

### Ejercicio 2

```python
from pathlib import Path

Path("x.bin").write_bytes(b"12\\r\\n34")
crudos = Path("x.bin").read_bytes()
texto = Path("x.bin").read_text(encoding="latin-1")

print(crudos, len(crudos))
print(repr(texto), len(texto))

# Se lo comió el modo texto de Python, no el sistema operativo. Al leer en
# texto, Python normaliza \\r\\n y \\r a \\n, así que dos bytes se vuelven uno.
```

### Ejercicio 3

```python
palabra = "cañón"

en_utf8 = palabra.encode("utf-8")
en_latin = palabra.encode("latin-1")

print(en_utf8, len(en_utf8))
print(en_latin, len(en_latin))

print(repr(en_utf8.decode("latin-1")))

# La ñ y la ó ocupan dos bytes en utf-8 y uno en latin-1, así que la misma
# palabra de cinco letras mide siete bytes en uno y cinco en el otro.
# Decodificar los bytes de utf-8 como latin-1 no truena y devuelve basura.
```

### Ejercicio 4

```python
from pathlib import Path
from zipfile import ZipFile

carpeta = Path("entrega")
carpeta.mkdir(exist_ok=True)
for n in range(3):
    (carpeta / f"archivo{n}.txt").write_text(f"contenido {n}", encoding="utf-8")

with ZipFile("con_ruta.zip", "w") as paquete:
    for p in carpeta.rglob("*.txt"):
        paquete.write(p)

with ZipFile("sin_ruta.zip", "w") as paquete:
    for p in carpeta.rglob("*.txt"):
        paquete.write(p, arcname=p.name)

for nombre in ["con_ruta.zip", "sin_ruta.zip"]:
    with ZipFile(nombre) as paquete:
        print(nombre, paquete.namelist())
```

### Ejercicio 5

```python
from pathlib import Path
import string

Path("abc.bin").write_bytes(string.ascii_uppercase.encode("ascii"))

with open("abc.bin", "rb") as f:
    print("abrir      ", f.tell())
    print("read(5)    ", f.read(5), f.tell())
    f.seek(10)
    print("seek(10)   ", f.tell())
    print("read(3)    ", f.read(3), f.tell())
    f.seek(-4, 2)
    print("seek(-4, 2)", f.tell())
    print("read()     ", f.read(), f.tell())
```

### Ejercicio 6

```python
from pathlib import Path

TAM_MATRICULA, TAM_NOMBRE = 8, 24
TAM = TAM_MATRICULA + TAM_NOMBRE

with open("alumnos.bin", "wb") as f:
    for i in range(10):
        f.write(f"A{i:06d}".encode("ascii").ljust(TAM_MATRICULA))
        f.write(f"alumno-{i}".encode("ascii").ljust(TAM_NOMBRE))

with open("alumnos.bin", "rb") as f:
    f.seek(6 * TAM)
    registro = f.read(TAM)

print(registro[:TAM_MATRICULA].strip(), registro[TAM_MATRICULA:].strip())
print("Tamaño:", Path("alumnos.bin").stat().st_size == 10 * TAM)
```

### Ejercicio 7

```python
from pathlib import Path

with open("variable.bin", "wb") as f:
    for i in range(10):
        f.write(f"A{i:06d}alumno-{i}\\n".encode("utf-8"))

with open("variable.bin", "rb") as f:
    f.seek(6 * 32)
    print("Con la cuenta:", f.read(32))

with open("variable.bin", "rb") as f:
    for i, linea in enumerate(f):
        if i == 6:
            print("De verdad:    ", linea)

# Para poder saltar harían falta dos cosas: o rellenar cada registro hasta un
# tamaño fijo, o guardar aparte una lista con el byte en el que empieza cada
# uno. Lo segundo es un índice, y es lo que hace una base de datos.
```

### Ejercicio 8

```python
from pathlib import Path

with open("hueco.bin", "wb") as f:
    f.write(b"AAAAA")
    f.seek(50)
    f.write(b"BBBBB")

crudos = Path("hueco.bin").read_bytes()
print("Tamaño:", len(crudos))
print("En medio:", crudos[5:50])
print("Todos ceros:", crudos[5:50] == bytes(45))

# La comprobación que lo evita
POSICION = 50
tam = Path("hueco.bin").stat().st_size
if POSICION > tam:
    print(f"la posición {POSICION} está más allá del final ({tam} bytes)")
```

### Ejercicio 9

```python
# Enunciado propio, en cinco renglones:
#
#   El archivo capturas.csv trae las columnas matricula, materia y nota.
#   Escribe un programa que lea el archivo, cuente cuántos alumnos aprobaron
#   cada materia con nota mayor o igual a 7, y escriba un archivo nuevo
#   llamado aprobados.csv con las columnas materia y aprobados, una fila por
#   materia y ordenado por clave de materia.

import csv
from pathlib import Path

ENTRADA = Path("capturas.csv")
SALIDA = Path("aprobados.csv")
MINIMO = 7.0


def leer(ruta):
    with open(ruta, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def contar_aprobados(filas, minimo=MINIMO):
    conteo = {}
    for fila in filas:
        materia = fila["materia"]
        conteo.setdefault(materia, 0)
        if float(fila["nota"]) >= minimo:
            conteo[materia] += 1
    return conteo


def guardar(conteo, ruta):
    with open(ruta, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["materia", "aprobados"])
        w.writeheader()
        for materia in sorted(conteo):
            w.writerow({"materia": materia, "aprobados": conteo[materia]})


if __name__ == "__main__":
    ENTRADA.write_text(
        "matricula,materia,nota\\n"
        "A001,COM102,9.1\\nA002,COM102,6.4\\n"
        "A003,COM101,8.0\\nA004,COM101,5.5\\nA005,COM102,7.0\\n",
        encoding="utf-8")

    guardar(contar_aprobados(leer(ENTRADA)), SALIDA)
    print(SALIDA.read_text(encoding="utf-8"))
```

Tres decisiones que vale la pena defender en la entrega.

**El enunciado dice el nombre del archivo de salida y sus columnas.** Sin eso, dos personas resuelven dos
cosas distintas y las dos tienen razón. La ambigüedad más común en estos enunciados es no decir qué pasa
con una materia sin aprobados; aquí se resuelve con el `setdefault`, que la deja en cero en lugar de
desaparecerla.

**Las tres funciones se pueden probar por separado.** `contar_aprobados` recibe una lista y devuelve un
diccionario, así que se prueba sin archivo y sin disco.

**Las rutas son constantes del módulo y relativas al directorio de trabajo.** Quien lo corra no tiene que
editar ninguna, que es el criterio del laboratorio.
"""),

]

write(OUT / "es" / "w13.ipynb", es)
print("wrote", OUT / "es" / "w13.ipynb")
