"""notebooks/analisis-de-datos/es/w14.ipynb

Source deck: ppts/python/analisis-de-datos/es/w14.es.yaml
Source code:  06 - Advanced/A04 - Tabular Data/{read_with_csv_module,summarise_by_hand}.py
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from nbkit import md, code, write, bootstrap_cell, REPO

OUT = REPO / "notebooks" / "analisis-de-datos"

es = [

md("""
# Análisis de Datos · Semana 14
## Archivos de texto y CSV

**TIA502 · Facultad de Empresariales · Profesor David Escobar-Castillejos**

Aquí dejan de escribirse los datos a mano. Abrir un archivo, leerlo por columna, convertirlo y
volver a guardarlo.

El argumento de la sesión es que **un CSV no tiene tipos**. Ya se dijo en la semana 4; hoy lo vas
a ver pasar con un archivo real de 324 renglones, y ahí sí se queda.

Al terminar este cuaderno vas a poder:

1. Abrir un archivo con `with`, y explicar por qué esa forma lo cierra aunque el programa falle.
2. Reconocer los cuatro modos, y cuál de ellos borra lo que había.
3. Leer un CSV por nombre de columna con `DictReader`.
4. Convertir lo que llega del archivo, incluidas las celdas vacías.
5. Escribir un archivo de salida que otro programa pueda abrir.

### Sobre los archivos en Colab

Todo lo que este cuaderno escriba queda en la sesión, junto a los CSV que trae la celda de
preparación. Mientras la sesión esté abierta se pueden volver a leer; al cerrarla desaparecen.

Para bajarlos a tu máquina, el panel de archivos de la izquierda tiene la opción de descarga.

Seis celdas fallan a propósito y llevan un comentario que lo dice.
"""),

md("""
---
## Preparación
"""),

bootstrap_cell("es"),

md("""
---
# Bloque 1 · Abrir un archivo

Un archivo abierto es un recurso prestado. Hay que devolverlo, y hay una forma de que eso pase
solo.
"""),

code("""
with open("sales.csv", encoding="utf-8") as f:
    primera = f.readline()

print(primera.strip())
"""),

md("""
Tres cosas de esa línea.

**`with`.** Al salir del bloque el archivo se cierra solo, aunque una línea de adentro lance un
error. Es la razón por la que este curso nunca escribe `open` sin `with`.

**`encoding="utf-8"`.** Explícito. Sin él, un archivo con acentos se lee distinto en Windows y en
Mac, y el error aparece en el renglón 200 de un archivo que en tu máquina abría bien.

**Fuera del `with` el archivo ya está cerrado.**
"""),

code("""
# FALLA A PROPÓSITO. Leer después de que el with cerró el archivo.
with open("sales.csv", encoding="utf-8") as f:
    pass

try:
    f.readline()
except ValueError as e:
    print("ValueError:", e)
"""),

md("""
Y `with` cierra el archivo incluso cuando el bloque revienta, que es lo que lo hace valioso.
"""),

code("""
# FALLA A PROPÓSITO, y aun así el archivo queda cerrado.
try:
    with open("sales.csv", encoding="utf-8") as f:
        f.readline()
        raise RuntimeError("algo salió mal a la mitad")
except RuntimeError as e:
    print("RuntimeError:", e)

print("¿El archivo quedó cerrado?", f.closed)
"""),

md("""
Sin `with` habría que escribir un `try` con un `finally` de tres líneas para conseguir lo mismo.

## Las tres formas de leer

| Forma | Qué devuelve | Cuándo |
|---|---|---|
| `f.read()` | Todo el archivo como un texto | Archivos chicos |
| `f.readline()` | Un renglón | Cuando solo quieres el encabezado |
| `for linea in f` | Un renglón por vuelta | Siempre que sea grande |
"""),

code("""
with open("sales.csv", encoding="utf-8") as f:
    completo = f.read()

print("Caracteres:", len(completo))
print("Renglones: ", completo.count("\\n"))
print("Los primeros 120:")
print(completo[:120])
"""),

code("""
with open("sales.csv", encoding="utf-8") as f:
    for i, linea in enumerate(f):
        if i >= 3:
            break
        print(f"{i}: {linea.rstrip()}")
"""),

md("""
Recorrer el archivo con un `for` lee un renglón a la vez y no carga los 324 en memoria. Con este
archivo da igual; con uno de dos millones de renglones es la diferencia entre correr y no correr.

Ese `.rstrip()` quita el salto de línea que cada renglón trae pegado al final.

## Los cuatro modos

| Modo | Qué hace | Si el archivo existe |
|---|---|---|
| `r` | Leer, y es el modo por omisión | Lo abre |
| `w` | Escribir desde cero | **Borra todo su contenido** |
| `a` | Agregar al final | Conserva lo que había |
| `x` | Crear uno nuevo | Falla con `FileExistsError` |

**Predice antes de correr.** ¿Qué pasa con el archivo al correr esto?

- **A.** Lee el contenido y lo guarda en la variable.
- **B.** Borra el archivo al abrirlo y luego falla al leer.
- **C.** Falla porque el archivo ya existe.
- **D.** Agrega una línea vacía al final.
"""),

code("""
# FALLA A PROPÓSITO, y destruye. Lo hago sobre una copia desechable.
with open("desechable.txt", "w", encoding="utf-8") as f:
    f.write("contenido original que vale oro\\n")

print("Antes:", open("desechable.txt", encoding="utf-8").read().strip())

try:
    with open("desechable.txt", "w", encoding="utf-8") as f:
        contenido = f.read()
except Exception as e:
    print(f"{type(e).__name__}: {e}")

print("Después:", repr(open("desechable.txt", encoding="utf-8").read()))
"""),

md("""
La respuesta es **B**. El modo `w` **borra el contenido en el instante en que abre**, antes de que
llegues a leer nada. El archivo quedó vacío y encima el `read` falló.

Ese es el error más caro de la sesión, porque no hay deshacer. Si `desechable.txt` hubiera sido el
archivo de tu proyecto, se acabó.

Los otros tres modos, con el mismo archivo:
"""),

code("""
with open("desechable.txt", "w", encoding="utf-8") as f:
    f.write("primera línea\\n")

with open("desechable.txt", "a", encoding="utf-8") as f:
    f.write("segunda línea, agregada\\n")

print(open("desechable.txt", encoding="utf-8").read())

# FALLA A PROPÓSITO. El modo x se niega a pisar un archivo existente.
try:
    with open("desechable.txt", "x", encoding="utf-8") as f:
        f.write("esto nunca se escribe")
except FileExistsError as e:
    print("FileExistsError:", e)
"""),

md("""
El modo `x` es la red de seguridad: cuando escribir sobre algo existente sería un desastre, `x`
falla en lugar de borrar.

## Rutas
"""),

code("""
from pathlib import Path

aqui = Path.cwd()
print("Estamos en:", aqui)
print("Archivos aquí:", sorted(p.name for p in aqui.glob("*.csv")))
print()
print("¿Existe sales.csv?", Path("sales.csv").exists())
print("Tamaño:", Path("sales.csv").stat().st_size, "bytes")
"""),

md("""
`pathlib` arma rutas que funcionan en Windows, Mac y Linux sin cambiarles nada. Escribir
`C:\\Users\\tu_nombre\\datos.csv` a mano no corre en ninguna otra máquina, incluida la del salón.

En un script de verdad la ruta se arma desde la ubicación del propio archivo:

```python
DATOS = Path(__file__).resolve().parent / "data"
```

En un cuaderno no hay `__file__`, así que los archivos viven en el directorio de trabajo y se
nombran directo.
"""),

md("""
---
# Bloque 2 · Leer un CSV

El formato que exporta cualquier hoja de cálculo y lee cualquier herramienta. Texto plano,
separado por comas.

Se podría partir a mano, y no se debe.
"""),

code("""
# FALLA A PROPÓSITO en cuanto un campo trae una coma dentro.
linea = '2025-12-08,South,Online,"Bean, subscription",15,"$ 1,690.00"'

print("Partiendo con split:", linea.split(","))
print()
print("Salieron", len(linea.split(",")), "campos y deberían ser 6.")
"""),

md("""
El módulo `csv` conoce las reglas: comillas, comas dentro de comillas, saltos de línea dentro de
un campo. Partir con `split` funciona hasta que un producto se llama "Café, tostado".
"""),

code("""
import csv, io

lector = csv.reader(io.StringIO(linea))
print("Con el módulo csv:", next(lector))
"""),

md("""
## Por posición, o por nombre
"""),

code("""
# Por posición: se rompe en cuanto alguien inserta una columna.
with open("sales.csv", encoding="utf-8") as f:
    lector = csv.reader(f)
    encabezado = next(lector)
    primera = next(lector)

print("Encabezado:", encabezado)
print("Región por posición:", primera[1])
"""),

code("""
# Por nombre: usa el encabezado, y sobrevive a un archivo reordenado.
with open("sales.csv", encoding="utf-8") as f:
    filas = list(csv.DictReader(f))

print("Renglones:", len(filas))
print("El primero:", filas[0])
print()
print("Región por nombre:", filas[0]["region"])
"""),

md("""
`DictReader` convierte cada renglón en un diccionario, con las llaves del encabezado. Es la semana
13 aplicada a un archivo.

El `list(...)` importa: sin él solo puedes recorrer una vez, porque el lector avanza y no
regresa.
"""),

code("""
# FALLA A PROPÓSITO. Sin list, el segundo recorrido no encuentra nada.
with open("sales.csv", encoding="utf-8") as f:
    lector = csv.DictReader(f)
    primera_vuelta = sum(1 for _ in lector)
    segunda_vuelta = sum(1 for _ in lector)

print("Primera vuelta:", primera_vuelta)
print("Segunda vuelta:", segunda_vuelta, "<- el lector ya llegó al final")
"""),

md("""
## Lo que el archivo entrega
"""),

code("""
print("El valor:", filas[0]["units"])
print("Su tipo: ", type(filas[0]["units"]))
print()
for campo, valor in filas[0].items():
    print(f"  {campo:<12} {valor!r:<22} {type(valor).__name__}")
"""),

md("""
**Todo es texto.** La fecha, la región, las unidades y el precio. El archivo no guarda tipos
porque un CSV no tiene dónde guardarlos.

Es exactamente lo que la semana 4 anunció, ahora con 324 renglones de verdad.
"""),

code("""
# FALLA A PROPÓSITO. Sumar texto concatena.
total_mal = ""
for fila in filas[:5]:
    total_mal += fila["units"]

print("Sumando sin convertir:", total_mal)
print("Convertido:", sum(int(f["units"]) for f in filas[:5]))
"""),

md("""
## La suciedad del archivo real
"""),

code("""
regiones = [f["region"] for f in filas]
vacias = sum(1 for f in filas if f["units"].strip() == "")

print("Regiones distintas:", len(set(regiones)), "y la empresa tiene cuatro")
print(sorted(set(regiones)))
print()
print("Celdas de units vacías:", vacias)
"""),

md("""
Ocho regiones donde hay cuatro, y once celdas vacías. El archivo real siempre viene sucio, y eso
no es un defecto de este archivo: es lo normal.
"""),

md("""
---
# Bloque 3 · Convertir y guardar

El archivo entrega texto. Decidir qué era cada cosa, y qué hacer con lo que falta, es trabajo
tuyo.
"""),

code("""
def a_entero(texto):
    \"\"\"Convierte a entero. Una celda vacía cuenta como cero.\"\"\"
    texto = texto.strip()
    return int(texto) if texto else 0


def a_decimal(texto):
    \"\"\"Convierte un precio con formato de moneda a decimal.\"\"\"
    limpio = texto.replace("$", "").replace(",", "")
    return float(limpio.strip())


def limpiar_region(texto):
    \"\"\"Quita espacios y normaliza mayúsculas, para que North y north sean uno.\"\"\"
    return texto.strip().title()


print(a_entero("15"), a_entero(""), a_entero("  22  "))
print(a_decimal("$ 2,082.50"), a_decimal("690.00"))
print(limpiar_region(" NORTH "), limpiar_region("north"))
"""),

md("""
Cada regla de limpieza en su propia función, con su docstring. Así se prueba sola y se reusa en
todo el archivo, que es exactamente el argumento de la semana 10.

**Y ahí hay una decisión de negocio escrita.** `a_entero("")` devuelve cero: alguien decidió que
una celda vacía significa cero unidades. Podría haber sido descartar el renglón, y también sería
defendible.

Lo que no se vale es no decidir.
"""),

code("""
# FALLA A PROPÓSITO. Sin la decisión, int de una cadena vacía truena.
try:
    int("")
except ValueError as e:
    print("ValueError:", e)
"""),

md("""
## Construir los registros limpios
"""),

code("""
registros = []
for fila in filas:
    unidades = a_entero(fila["units"])
    precio = a_decimal(fila["unit_price"])
    registros.append({
        "date": fila["date"],
        "region": limpiar_region(fila["region"]),
        "channel": fila["channel"],
        "product": fila["product"],
        "units": unidades,
        "unit_price": precio,
        "amount": unidades * precio,
    })

print("Registros:", len(registros))
print("Regiones ahora:", sorted({r["region"] for r in registros}))
print("El primero:", registros[0])
"""),

md("""
Ocho regiones se volvieron cuatro con una función de una línea.

## Los duplicados
"""),

code("""
vistos = set()
unicos = []
for r in registros:
    llave = tuple(r.values())
    if llave not in vistos:
        vistos.add(llave)
        unicos.append(r)

print("Antes: ", len(registros))
print("Después:", len(unicos))
print("Duplicados quitados:", len(registros) - len(unicos))
"""),

md("""
Ahí está el conjunto de la semana pasada haciendo el trabajo. Un registro cuenta como duplicado
cuando **todos** sus campos coinciden con otro, y por eso la llave es la tupla de todos sus
valores.

Una tupla, no una lista, porque una lista no puede vivir en un conjunto.
"""),

code("""
total_con = sum(r["amount"] for r in registros)
total_sin = sum(r["amount"] for r in unicos)

print(f"Total con duplicados: {total_con:>16,.2f}")
print(f"Total sin duplicados: {total_sin:>16,.2f}")
print(f"Diferencia:           {total_con - total_sin:>16,.2f}")
"""),

md("""
Doscientos setenta y tres mil pesos de diferencia por siete renglones repetidos. Nadie que lea
el total sabría que está inflado, porque un total no dice sobre cuántos registros se calculó.

## El resumen por región
"""),

code("""
from collections import defaultdict

por_region = defaultdict(float)
unidades_region = defaultdict(int)

for r in unicos:
    por_region[r["region"]] += r["amount"]
    unidades_region[r["region"]] += r["units"]

total = sum(por_region.values())

print(f"{'Región':<10}{'Monto':>16}{'Unidades':>10}{'Parte':>9}")
print("-" * 45)
for region in sorted(por_region, key=por_region.get, reverse=True):
    print(f"{region:<10}{por_region[region]:>16,.2f}"
          f"{unidades_region[region]:>10}{por_region[region] / total:>9.1%}")
print("-" * 45)
print(f"{'Total':<10}{total:>16,.2f}")
"""),

md("""
`defaultdict(float)` es un diccionario donde una llave que no se ha visto empieza en 0.0, así que
no hace falta el `get(r, 0)` de la semana pasada.

Esas veinte líneas son una tabla dinámica hecha a mano. **La semana que entra son ocho**, y dan
exactamente los mismos cuatro totales hasta el centavo.

## Escribir el resultado
"""),

code("""
with open("resumen_por_region.csv", "w", newline="", encoding="utf-8") as f:
    escritor = csv.writer(f)
    escritor.writerow(["region", "amount", "units", "share"])
    for region in sorted(por_region, key=por_region.get, reverse=True):
        escritor.writerow([
            region,
            round(por_region[region], 2),
            unidades_region[region],
            round(por_region[region] / total, 4),
        ])

print("Escrito. Contenido:")
print(open("resumen_por_region.csv", encoding="utf-8").read())
"""),

md("""
Ese `newline=""` no es opcional. **Sin él, en Windows el archivo sale con un renglón en blanco
entre cada dato**, porque el módulo `csv` ya pone su propio salto de línea y el sistema agrega
otro.

Compruébalo.
"""),

code("""
# FALLA A PROPÓSITO. Escribir un CSV sin newline vacío.
with open("con_renglones_de_mas.csv", "w", encoding="utf-8") as f:
    escritor = csv.writer(f)
    escritor.writerow(["a", "b"])
    escritor.writerow(["1", "2"])

crudo = open("con_renglones_de_mas.csv", newline="", encoding="utf-8").read()
print("Sin newline='':", repr(crudo))

with open("bien.csv", "w", newline="", encoding="utf-8") as f:
    escritor = csv.writer(f)
    escritor.writerow(["a", "b"])
    escritor.writerow(["1", "2"])

print("Con newline='':", repr(open("bien.csv", newline="", encoding="utf-8").read()))
"""),

md("""
En Colab, que corre Linux, los dos salen iguales. En Windows el primero trae `\\r\\r\\n` y se ve
como renglones en blanco al abrirlo en Excel.

Como no sabes en qué máquina va a correr tu programa, `newline=""` va siempre.

## Y con `DictWriter`, por nombre
"""),

code("""
with open("registros_limpios.csv", "w", newline="", encoding="utf-8") as f:
    campos = ["date", "region", "channel", "product", "units", "unit_price", "amount"]
    escritor = csv.DictWriter(f, fieldnames=campos)
    escritor.writeheader()
    escritor.writerows(unicos)

print("Escritos", len(unicos), "registros limpios")
print(open("registros_limpios.csv", encoding="utf-8").readline().strip())
print(open("registros_limpios.csv", encoding="utf-8").readlines()[1].strip())
"""),

md("""
`DictWriter` es la contraparte de `DictReader`: recibe diccionarios y usa `fieldnames` para decidir
el orden de las columnas.

Con eso el ciclo se cierra: leíste un archivo sucio, lo limpiaste, lo resumiste, y escribiste dos
archivos que cualquiera puede abrir.

## Cuatro errores con archivos

**Abrir en modo `w` para leer.** Borra el contenido en el instante en que abre.

**Rutas escritas a mano.** No corren en ninguna otra máquina.

**Sumar sin convertir.** Concatena y el total sale absurdo sin lanzar error.

**Olvidar `newline` al escribir.** Un renglón en blanco entre cada dato, en Windows.

Los cuatro los viste correr.
"""),

md("""
---
# Ejercicios

Las soluciones están hasta abajo del cuaderno.

## Abrir y leer

### Ejercicio 1 · Las tres formas

Lee `regions.csv` de las tres formas: entero con `read`, el encabezado con `readline`, y renglón
por renglón con un `for`. Imprime algo distinto en cada caso.

### Ejercicio 2 · El modo que destruye

Crea un archivo con tres líneas, ábrelo en modo `a` y agrégale una cuarta, y después demuestra con
`x` que no puedes crearlo de nuevo.

No uses el modo `w` sobre un archivo que te importe.

### Ejercicio 3 · El archivo que no existe

Provoca un `FileNotFoundError` y escribe una función `leer_seguro(ruta)` que devuelva una lista
vacía en lugar de tronar, y avise por pantalla.

## CSV

### Ejercicio 4 · Por nombre

Lee `employees.csv` con `DictReader` e imprime cuántos renglones tiene, los nombres de las
columnas, y el primer registro completo.

### Ejercicio 5 · Los tipos que llegan

Para el primer registro de `employees.csv`, imprime cada campo con su tipo. Después convierte los
dos que son numéricos y vuelve a imprimirlos con su tipo nuevo.

### Ejercicio 6 · Tu propia función de limpieza

Escribe `a_entero_o_none(texto)` que devuelva `None` en lugar de cero cuando la celda esté vacía.
Después calcula el promedio de unidades de las dos formas, con cero y con `None` descartado, y di
cuál reportarías.

Es la misma decisión de la semana 15.2, tomada a mano.

## Resumir y escribir

### Ejercicio 7 · Resumen por canal

Con los registros limpios, arma un resumen por canal en lugar de por región, con monto, unidades y
participación. Escríbelo a `resumen_por_canal.csv`.

Comprueba que la suma de los tres canales da el mismo total que la de las cuatro regiones.

### Ejercicio 8 · El cruce

Arma un resumen por región **y** canal a la vez, usando una tupla como llave del diccionario.
Imprímelo como tabla con las regiones en renglones y los canales en columnas.

Es el ciclo anidado de la semana 9 y la llave compuesta de la semana 13, juntos.

### Ejercicio 9 · Tu propio archivo, de principio a fin

Toma el CSV que trajiste en la semana 1, léelo con `DictReader`, convierte al menos dos columnas al
tipo correcto, y produce un resumen por categoría escrito en un archivo nuevo.

Ninguna ruta absoluta. Y bórrale un valor a una celda: tu programa tiene que seguir corriendo y
decir qué hizo con ella.
"""),

md("""
---
## Tres ideas para llevarse

**Un archivo guarda texto.** Los tipos los pones tú. Es la misma lección de la semana 4, ahora con
un archivo de 324 renglones y siete duplicados que valen ciento noventa mil pesos.

**Lee por nombre de columna.** Contar posiciones se rompe en cuanto alguien inserta una columna, y
nadie te va a avisar.

**Qué hacer con lo que falta es tu decisión.** Descartar, rellenar o ignorar dan tres respuestas
distintas, y las tres se tienen que poder defender.

La siguiente sesión es pandas. Todo lo que hiciste hoy a mano, en ocho líneas.
"""),

md("""
---
# Soluciones

### Ejercicio 1

```python
with open("regions.csv", encoding="utf-8") as f:
    completo = f.read()
print("Caracteres:", len(completo))

with open("regions.csv", encoding="utf-8") as f:
    print("Encabezado:", f.readline().strip())

with open("regions.csv", encoding="utf-8") as f:
    next(f)
    for linea in f:
        print("  ", linea.strip().split(",")[0])
```

El `next(f)` de la tercera salta el encabezado sin necesidad de un contador. Un archivo abierto se
comporta como una secuencia de renglones, y `next` toma el siguiente.

### Ejercicio 2

```python
with open("prueba.txt", "w", encoding="utf-8") as f:
    f.write("una\\ndos\\ntres\\n")

with open("prueba.txt", "a", encoding="utf-8") as f:
    f.write("cuatro\\n")

print(open("prueba.txt", encoding="utf-8").read())

try:
    with open("prueba.txt", "x", encoding="utf-8") as f:
        f.write("nunca")
except FileExistsError as e:
    print("FileExistsError:", e)
```

El modo `a` conservó las tres líneas y agregó la cuarta. El modo `x` se negó, que es justo lo que
quieres cuando escribir sobre algo existente sería un accidente.

### Ejercicio 3

```python
try:
    open("no_existe.csv", encoding="utf-8")
except FileNotFoundError as e:
    print("FileNotFoundError:", e)


def leer_seguro(ruta):
    \"\"\"Devuelve los renglones del CSV, o una lista vacía si el archivo no está.\"\"\"
    try:
        with open(ruta, encoding="utf-8") as f:
            return list(csv.DictReader(f))
    except FileNotFoundError:
        print(f"Aviso: no encontré {ruta}, sigo con una lista vacía")
        return []


print(len(leer_seguro("sales.csv")), "renglones")
print(len(leer_seguro("no_existe.csv")), "renglones")
```

Devolver una lista vacía en lugar de tronar es una decisión, no una comodidad. Sirve cuando el
archivo es opcional; cuando es obligatorio, dejar que truene es lo correcto.

### Ejercicio 4

```python
with open("employees.csv", encoding="utf-8") as f:
    empleados = list(csv.DictReader(f))

print("Renglones:", len(empleados))
print("Columnas: ", list(empleados[0].keys()))
print("El primero:", empleados[0])
```

Ciento veinte renglones y seis columnas. `list(empleados[0].keys())` da los nombres del encabezado,
que es lo mismo que `DictReader` usó para armar las llaves.

### Ejercicio 5

```python
primero = empleados[0]

for campo, valor in primero.items():
    print(f"{campo:<16} {valor!r:<20} {type(valor).__name__}")

print()
meses = int(primero["tenure_months"])
sueldo = int(primero["monthly_salary"])
print(f"tenure_months    {meses!r:<20} {type(meses).__name__}")
print(f"monthly_salary   {sueldo!r:<20} {type(sueldo).__name__}")
```

Los seis llegan como `str`, incluido `employee_id`, que **debe** quedarse como texto: es un
identificador con ceros a la izquierda, y convertirlo perdería el formato. La lección de la semana
4, otra vez.

### Ejercicio 6

```python
def a_entero_o_none(texto):
    \"\"\"Entero, o None si la celda está vacía.\"\"\"
    texto = texto.strip()
    return int(texto) if texto else None


con_cero = [a_entero(f["units"]) for f in filas]
con_none = [a_entero_o_none(f["units"]) for f in filas]
medidos = [u for u in con_none if u is not None]

print(f"Tratando vacío como cero: {sum(con_cero) / len(con_cero):>8.2f} sobre {len(con_cero)}")
print(f"Descartando los vacíos:   {sum(medidos) / len(medidos):>8.2f} sobre {len(medidos)}")

# Reportaría el segundo, diciendo que cubre 313 de 324 registros. Tratar el vacío
# como cero afirma que once ventas movieron cero unidades, y eso es falso: no se
# capturaron. La diferencia es de medio punto en el promedio, que parece poco hasta
# que alguien lo usa para proyectar el año.
```

Es exactamente la decisión que `dropna` contra `fillna(0)` toma en la semana 15.2, tomada aquí a
mano y con las mismas consecuencias.

### Ejercicio 7

```python
por_canal = defaultdict(float)
unidades_canal = defaultdict(int)

for r in unicos:
    por_canal[r["channel"]] += r["amount"]
    unidades_canal[r["channel"]] += r["units"]

total_canal = sum(por_canal.values())

with open("resumen_por_canal.csv", "w", newline="", encoding="utf-8") as f:
    escritor = csv.writer(f)
    escritor.writerow(["channel", "amount", "units", "share"])
    for canal in sorted(por_canal, key=por_canal.get, reverse=True):
        escritor.writerow([canal, round(por_canal[canal], 2),
                           unidades_canal[canal],
                           round(por_canal[canal] / total_canal, 4)])

print(open("resumen_por_canal.csv", encoding="utf-8").read())
print("¿Mismo total que por región?", round(total_canal, 2) == round(total, 2))
```

Los dos totales coinciden porque los dos resúmenes reparten exactamente los mismos registros, solo
que agrupados por otra columna. Si no coincidieran, algún registro se habría quedado fuera de uno
de los dos.

Esa comprobación es gratis y vale la pena dejarla puesta.

### Ejercicio 8

```python
cruce = defaultdict(float)
for r in unicos:
    cruce[(r["region"], r["channel"])] += r["amount"]

regiones_ord = sorted({r for r, _ in cruce})
canales_ord = sorted({c for _, c in cruce})

print(f"{'Región':<10}" + "".join(f"{c:>16}" for c in canales_ord) + f"{'Total':>16}")
for region in regiones_ord:
    fila = [cruce[(region, c)] for c in canales_ord]
    print(f"{region:<10}" + "".join(f"{v:>16,.2f}" for v in fila) + f"{sum(fila):>16,.2f}")
```

La llave compuesta es una tupla, y las dos comprensiones de conjunto sacan las regiones y los
canales distintos sin repetir.

Esas doce líneas son la rejilla que `pivot_table` produce en una instrucción en la semana 15.3, y
los números salen idénticos.

### Ejercicio 9

No hay solución publicada porque el archivo es distinto para cada quien. Se califica sobre cuatro
cosas: que use `DictReader` y no posiciones, que las conversiones estén en funciones con docstring,
que no haya ninguna ruta absoluta, y que al borrar un valor el programa siga corriendo y diga qué
decidió sobre esa celda.
"""),

]

write(OUT / "es" / "w14.ipynb", es)
print("wrote", OUT / "es" / "w14.ipynb")
