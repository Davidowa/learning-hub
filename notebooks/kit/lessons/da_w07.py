"""notebooks/analisis-de-datos/{es,en}/w07.ipynb

Source deck: ppts/python/analisis-de-datos/{es,en}/w07.*.yaml
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from nbkit import md, code, write, REPO

OUT = REPO / "notebooks" / "analisis-de-datos"

es = [

md("""
# Análisis de Datos · Semana 7
## Selección anidada y operadores lógicos

**TIA502 · Facultad de Empresariales · Profesor David Escobar-Castillejos**

La sesión pasada fue una condición a la vez. Esta es cómo se juntan, y cuándo conviene anidar en
lugar de combinar.

Al terminar este cuaderno vas a poder:

1. Usar los tres operadores lógicos: `and` exige las dos, `or` se conforma con una, `not`
   invierte.
2. Leer una tabla de verdad y predecir el resultado de una condición compuesta sin ejecutarla.
3. Preguntar por pertenencia con `in` y `not in`, en lugar de encadenar comparaciones con `or`.
4. Distinguir `is` de `==`.
5. Decidir cuándo anidar, y reconocer el anidado que en realidad era un `and`.

### Cómo se usa este cuaderno

Ejecuta las celdas en orden. Cuatro fallan a propósito o dan un resultado inesperado a propósito,
y llevan un comentario que lo dice.

La regla práctica del final vale más que toda la teoría de arriba: **si las dos ramas del anidado
hacen lo mismo, era un `and` disfrazado.**
"""),

md("""
---
# Bloque 1 · Combinar condiciones

Tres operadores, y con ellos se arma cualquier regla por complicada que suene al decirla en voz
alta.

| Operador | Qué exige | Ejemplo |
|---|---|---|
| `and` | Que las dos condiciones sean verdaderas | `conversion >= 0.03 and clics > 1000` |
| `or` | Que al menos una sea verdadera | `canal == "Meta" or canal == "Google"` |
| `not` | Invierte el resultado de la condición | `not campana_activa` |

## La tabla de verdad, generada

| A | B | `A and B` | `A or B` |
|---|---|---|---|
| `True` | `True` | `True` | `True` |
| `True` | `False` | `False` | `True` |
| `False` | `True` | `False` | `True` |
| `False` | `False` | `False` | `False` |

En lugar de creérmela, constrúyela.
"""),

code("""
print(f"{'A':<7}{'B':<7}{'A and B':<10}{'A or B':<10}{'not A':<7}")
print("-" * 41)

for a in [True, False]:
    for b in [True, False]:
        print(f"{str(a):<7}{str(b):<7}{str(a and b):<10}{str(a or b):<10}{str(not a):<7}")
"""),

md("""
Cuatro renglones y ahí está todo. `and` solo es verdadero en el primero; `or` es falso solo en el
último.

## Una regla con dos condiciones
"""),

code("""
conversion = 0.0342
clics = 5074
canal = "Instagram"

if conversion >= 0.03 and clics > 1000:
    print("La campaña califica para más presupuesto.")
else:
    print("La campaña se mantiene igual.")
"""),

md("""
Con `and`, si una sola falla, la regla completa falla. No hay término medio.

**Por qué la segunda condición.** Una conversión alta sobre cien clics no significa nada: puede ser
casualidad. El volumen filtra el ruido, y por eso la política pide las dos cosas.

Cámbiale el `and` por un `or` y mira a quién aprueba.
"""),

code("""
CANDIDATAS = [
    ("Instagram", 0.0342, 5074),
    ("LinkedIn", 0.0205, 640),
    ("Boletín", 0.0810, 62),      # conversión altísima, casi sin volumen
    ("Display", 0.0021, 88400),   # volumen enorme, conversión pésima
]

print(f"{'Canal':<12}{'Conv.':>8}{'Clics':>9}   con and        con or")
print("-" * 58)

for canal, conv, clics in CANDIDATAS:
    con_and = "aprueba" if (conv >= 0.03 and clics > 1000) else "no"
    con_or = "aprueba" if (conv >= 0.03 or clics > 1000) else "no"
    print(f"{canal:<12}{conv:>8.2%}{clics:>9,}   {con_and:<14} {con_or}")
"""),

md("""
Con `or`, Display aprueba: ochenta y ocho mil clics y una conversión del 0.21 %. Es la campaña
que más dinero quema del grupo y la regla la premia.

Ese es el costo de cambiar una palabra.

## Evaluación corta

Si la primera condición de un `and` es falsa, Python **ni siquiera lee la segunda**. Ahorra
trabajo y, más importante, evita errores.
"""),

code("""
def revisar(nombre):
    \"\"\"Dice en voz alta que fue evaluada, para que se vea cuándo corre.\"\"\"
    print(f"  (evaluando {nombre})")
    return True


print("Con la primera falsa:")
resultado = False and revisar("segunda")
print("Resultado:", resultado)

print()
print("Con la primera verdadera:")
resultado = True and revisar("segunda")
print("Resultado:", resultado)
"""),

md("""
En el primer caso `revisar` nunca corrió. Eso no es una curiosidad: es lo que permite escribir
condiciones que serían un error al revés.
"""),

code("""
clics_reportados = 0

# El orden correcto: primero se revisa que no sea cero, después se divide.
if clics_reportados > 0 and 38500 / clics_reportados < 10:
    print("Costo por clic aceptable")
else:
    print("Sin clics suficientes para evaluar")
"""),

code("""
# FALLA A PROPÓSITO. El mismo par de condiciones, en el orden equivocado.
try:
    if 38500 / clics_reportados < 10 and clics_reportados > 0:
        print("Costo por clic aceptable")
except ZeroDivisionError as e:
    print("ZeroDivisionError:", e)
"""),

md("""
La misma regla, dos comportamientos. Con la guarda primero, la división nunca ocurre; al revés,
truena antes de llegar a la guarda.

**Cuando una condición protege a la otra, va primero.** No es estilo, es lo que hace que el
programa corra.

## `not`

Invierte. Se usa poco y cuando se usa, conviene que la variable ya se lea como una afirmación.
"""),

code("""
campana_activa = False

print("not campana_activa:", not campana_activa)

if not campana_activa:
    print("La campaña está pausada, no hay nada que evaluar.")
"""),

md("""
`if not campana_activa:` se lee casi como en español. Comparar con `if campana_activa == False:`
funciona igual y se lee peor.
"""),

md("""
---
# Bloque 2 · Pertenencia e identidad

Cuatro operadores más, y dos de ellos te van a ahorrar escribir la misma comparación cinco veces.

| Operador | Pregunta | Ejemplo | Resultado |
|---|---|---|---|
| `in` | ¿Está dentro? | `canal in ["Meta", "Google"]` | `False` |
| `not in` | ¿Está fuera? | `canal not in ["TikTok"]` | `True` |
| `is` | ¿Es el mismo objeto? | `costo is None` | `True` |
| `is not` | ¿Es otro objeto? | `costo is not None` | `False` |

## Cinco comparaciones, o una

Así se ve encadenando con `or`:

```python
if (canal == "Meta" or
    canal == "Google" or
    canal == "Instagram" or
    canal == "TikTok"):
    print("Canal digital")
```

Y así con `in`:
"""),

code("""
DIGITALES = ["Meta", "Google", "Instagram", "TikTok"]

canal = "Instagram"

if canal in DIGITALES:
    print("Canal digital")
else:
    print("Otro canal")
"""),

md("""
La segunda se lee de un vistazo y, sobre todo, **la lista se puede cambiar sin tocar la
condición**. Agregar un canal es agregar un elemento.
"""),

code("""
DIGITALES.append("LinkedIn")

for canal in ["Instagram", "LinkedIn", "Radio", "Espectacular"]:
    print(f"{canal:<14} {'digital' if canal in DIGITALES else 'tradicional'}")
"""),

md("""
`in` también funciona sobre texto, y ahí pregunta si una cadena está contenida en otra.
"""),

code("""
puesto = "Sales analyst"

print('"analyst" in puesto :', "analyst" in puesto)
print('"Analyst" in puesto :', "Analyst" in puesto, "<- distingue mayúsculas")
print('"analyst" in puesto.lower() :', "analyst" in puesto.lower())
"""),

md("""
Ese es el antecesor directo de `.str.contains("manager", case=False)` de la semana 15.2, aplicado
a un valor en vez de a una columna.

## `is` no es `==`

El que más se confunde. `==` pregunta si valen lo mismo; `is` pregunta si son **el mismo objeto**.
"""),

code("""
a = [1, 2, 3]
b = [1, 2, 3]

print("a == b :", a == b, "<- valen lo mismo")
print("a is b :", a is b, "<- y no son el mismo objeto")

c = a
print("c is a :", c is a, "<- c es otro nombre para el mismo objeto")
"""),

md("""
Dos listas con el mismo contenido son iguales y no son la misma. Es la diferencia entre dos hojas
con los mismos datos y dos pestañas que apuntan al mismo archivo.

**Para números y texto, usa siempre `==`.** `is` con valores da resultados que dependen de detalles
internos de Python y no se pueden predecir.
"""),

code("""
# FALLA A PROPÓSITO, y de la peor forma: a veces funciona.
x = 256
y = 256
print("256 is 256 :", x is y)

x = 1000
y = 1000
print("1000 is 1000 :", x is y, "<- el mismo código, otro resultado")

print()
print("Con == siempre es predecible:", 1000 == 1000)
"""),

md("""
El mismo código con otro número da otro resultado, porque Python guarda los enteros chicos en una
tabla y los reutiliza. Nada de eso es algo en lo que debas apoyarte.

`is` tiene un uso correcto y es este:
"""),

code("""
costo_por_clic = None

print("costo is None     :", costo_por_clic is None)
print("costo is not None :", costo_por_clic is not None)

costo_por_clic = 7.59
print("Ya medido, is not None:", costo_por_clic is not None)
"""),

md("""
`is None` y `is not None` son la forma correcta de preguntar por ausencia de dato, porque `None`
es un objeto único en todo el programa.
"""),

md("""
---
# Bloque 3 · Anidar una decisión

Una decisión dentro de otra. A veces es lo correcto, y a veces es un `and` escrito de la forma más
larga posible.

## Un anidado que sí gana algo
"""),

code("""
campana_activa = False
conversion = 0.061

if campana_activa:
    if conversion >= 0.05:
        accion = "Subir presupuesto"
    elif conversion >= 0.03:
        accion = "Mantener"
    else:
        accion = "Pausar y revisar"
else:
    accion = "Reactivar antes de evaluar"

print(accion)
"""),

md("""
Aquí el anidado gana algo real, por tres razones.

**La primera pregunta decide si sigues.** Si la campaña está apagada, su conversión no significa
nada: son datos de cuando estaba prendida. Preguntar por ella sería un error de negocio.

**Cada rama interna hace algo distinto.** Tres salidas, no dos iguales.

**El `else` de afuera** cubre el caso apagado completo, sin repetir las tres categorías.

La traza con una campaña apagada y conversión del 6 %:

| Paso | Condición | Resultado | `accion` |
|---|---|---|---|
| 1 | `campana_activa` | `False` | – |
| 2 | Todo el bloque interno | No se evalúa | – |
| 3 | `else` de afuera | Se ejecuta | `Reactivar antes de evaluar` |

La conversión del 6 % nunca se mira. El anidado la protege de una decisión que no tendría sentido
tomar.

## El anidado que era un `and`

Ahora el caso contrario. Léelo y busca qué le sobra.
"""),

code("""
def aprobar_anidado(conversion, clics):
    \"\"\"Tres niveles de sangría para una sola pregunta.\"\"\"
    if conversion >= 0.03:
        if clics > 1000:
            return "aprueba"
        else:
            return "no aprueba"
    else:
        return "no aprueba"


def aprobar_combinado(conversion, clics):
    \"\"\"Lo mismo, en una línea.\"\"\"
    return "aprueba" if (conversion >= 0.03 and clics > 1000) else "no aprueba"


for conv, clics in [(0.0342, 5074), (0.081, 62), (0.0021, 88400), (0.02, 500)]:
    a = aprobar_anidado(conv, clics)
    b = aprobar_combinado(conv, clics)
    print(f"{conv:>7.2%}{clics:>8,}   {a:<12}{b:<12}{'iguales' if a == b else 'DISTINTOS'}"),
"""),

md("""
Idénticos en los cuatro casos, y uno ocupa nueve líneas y el otro una.

**La prueba: si las dos ramas internas hacen lo mismo, era un `and`.** En `aprobar_anidado`, el
`else` de adentro y el de afuera devuelven exactamente lo mismo, y eso es la señal.

Es la revisión más rentable que le puedes hacer a tu propio código. Convierte cuatro niveles de
sangría en una línea legible.

## La regla, dicha completa

Se anida cuando:

1. La segunda pregunta **solo tiene sentido** si la primera se cumplió.
2. Cada rama hace **algo distinto**.

Si las dos ramas internas terminan haciendo lo mismo, o si la segunda pregunta se puede hacer
siempre, entonces no era un anidado: era una sola condición unida con `and`.
"""),

md("""
---
## Cuatro trampas de las condiciones compuestas

### Escribir `and` cuando querías `or`

Léela en voz alta. "Las dos" es `and`, "cualquiera de las dos" es `or`. La mitad de los errores se
atrapan así.

### Comparar contra dos valores de golpe

**Predice antes de correr.** ¿Qué imprime, si el canal es Instagram?

- **A.** `No coincide`, porque no es ninguno de los dos.
- **B.** `Coincide`, porque un texto no vacío se evalúa como verdadero.
- **C.** Un error, porque falta una comparación.
- **D.** `Coincide`, porque Python compara con los dos.
"""),

code("""
# FALLA A PROPÓSITO, sin lanzar nada. Esta condición no hace lo que parece.
canal = "Instagram"

if canal == "Meta" or "Google":
    print("Coincide")
else:
    print("No coincide")
"""),

md("""
La respuesta es **B**, y es de las peores trampas del lenguaje.

Python lee eso como `(canal == "Meta") or ("Google")`. La primera parte es falsa, así que evalúa la
segunda: `"Google"` a secas, un texto no vacío, que cuenta como verdadero.

La condición es verdadera **siempre**, para cualquier canal.
"""),

code("""
for canal in ["Instagram", "Meta", "Radio", "cualquier cosa"]:
    resultado = canal == "Meta" or "Google"
    print(f"{canal:<16} -> {resultado!r}")
"""),

md("""
Ni siquiera devuelve `True`: devuelve el texto `"Google"`, que en un `if` cuenta como verdadero.

Las dos formas correctas:
"""),

code("""
canal = "Instagram"

print("Repitiendo la variable:", canal == "Meta" or canal == "Google")
print("Con in:                ", canal in ("Meta", "Google"))
"""),

md("""
### Usar `is` para comparar valores

Ya lo viste arriba. Para números y texto, siempre `==`.

### Anidar sin necesidad

Tres niveles de sangría casi siempre son dos condiciones unidas con `and` y una rama que sobra.

## Todo junto: una política real
"""),

code("""
DIGITALES = ["Meta", "Google", "Instagram", "TikTok", "LinkedIn"]

def decidir_presupuesto(canal, activa, conversion, clics):
    \"\"\"Política completa, con los tres operadores lógicos y pertenencia.\"\"\"
    if not activa:
        return "Reactivar antes de evaluar"

    if canal not in DIGITALES:
        return "Fuera de política, revisar a mano"

    if conversion >= 0.05 and clics > 1000:
        return "Subir presupuesto"
    elif conversion >= 0.03 or clics > 50000:
        return "Mantener"
    else:
        return "Pausar y revisar"


CASOS = [
    ("Instagram", True, 0.061, 5074),
    ("Instagram", False, 0.061, 5074),
    ("Radio", True, 0.061, 5074),
    ("Display", True, 0.0021, 88400),
    ("LinkedIn", True, 0.0205, 640),
]

for canal, activa, conv, clics in CASOS:
    estado = "activa" if activa else "pausada"
    print(f"{canal:<11}{estado:<10}{conv:>7.2%}{clics:>8,}   {decidir_presupuesto(canal, activa, conv, clics)}")
"""),

md("""
Tres guardas al principio y una decisión al final. Ninguna sangría pasa de dos niveles, y la
función se lee de arriba abajo como una lista de reglas.

Ese patrón, sacar los casos especiales primero y dejar la lógica principal al final, es lo que
evita el anidado profundo casi siempre.
"""),

md("""
---
# Ejercicios

Las soluciones están hasta abajo del cuaderno.

## Lógicos

### Ejercicio 1 · La tabla de verdad de `not` y de la combinación

Genera con un ciclo la tabla de verdad de `A and not B` y de `not (A or B)`. Cuatro renglones cada
una.

Después contesta en un comentario: ¿alguna de las dos da lo mismo que `not A or not B`?

### Ejercicio 2 · Leerla en voz alta

Para cada una de estas tres reglas, escribe la condición en Python y la frase en español que la
describe:

1. Aprobar si el cliente tiene más de dos años **y** su saldo es menor a 10 000.
2. Alertar si el pedido pasa de 100 000 **o** el cliente es nuevo.
3. Rechazar si **no** está en la lista de proveedores autorizados.

### Ejercicio 3 · La guarda que protege

Escribe una condición que calcule el costo por clic solo si hay clics, usando evaluación corta.
Pruébala con cero clics y con clics de verdad.

Después escríbela al revés y comprueba que truena.

## Pertenencia

### Ejercicio 4 · De cinco `or` a un `in`

Escribe una condición con cuatro `or` que revise si un mes es del último trimestre, y después la
misma con `in`. Pruébalas con seis meses distintos y comprueba que dan lo mismo.

### Ejercicio 5 · Buscar dentro de un texto

Con esta lista de puestos, imprime los que contengan la palabra "manager" sin importar mayúsculas,
y por separado los que contengan "analyst".

```python
PUESTOS = ["Sales analyst", "Brand Manager", "people manager",
           "Financial Analyst", "Recruiter", "Operations Manager"]
```

### Ejercicio 6 · `is` contra `==`

Crea dos diccionarios con el mismo contenido y compáralos con `==` y con `is`. Después asigna uno
al otro y vuelve a comparar.

Explica en un comentario en qué caso `is` sería la pregunta correcta.

## Anidar

### Ejercicio 7 · Colapsar un anidado

Este código tiene tres niveles de sangría y dos ramas que hacen lo mismo. Reescríbelo en una sola
condición.

```python
def puede_enviar(peso, destino, pagado):
    if pagado:
        if peso <= 20:
            if destino != "internacional":
                return "enviar"
            else:
                return "no enviar"
        else:
            return "no enviar"
    else:
        return "no enviar"
```

Comprueba con ocho combinaciones que las dos versiones dan lo mismo.

### Ejercicio 8 · Una política que necesita dos condiciones

Escribe una regla de tu área que dependa de al menos dos datos: aprobar un crédito por ingreso y
antigüedad, o priorizar un pedido por monto y por cliente. Que use `and`, `or` e `in` al menos una
vez cada uno.

Máximo dos niveles de sangría. Si necesitas tres, colapsa con `and`.

La prueba: léela en voz alta a un compañero. Si tiene que preguntar "¿y o o?", la condición está
mal escrita.
"""),

md("""
---
## Tres ideas para llevarse

**`and` exige las dos, `or` se conforma con una.** Leer la condición en voz alta atrapa la mitad de
los errores antes de correr el programa.

**`in` reemplaza una fila de `or`.** Y deja que la lista de valores válidos cambie sin tocar una
sola línea de la condición.

**Si las dos ramas hacen lo mismo, era un `and`.** La revisión más rentable que le puedes hacer a
tu código, y convierte cuatro niveles de sangría en uno.

La siguiente sesión es repetición, y el primer examen parcial.
"""),

md("""
---
# Soluciones

### Ejercicio 1

```python
print(f"{'A':<7}{'B':<7}{'A and not B':<14}{'not (A or B)':<15}{'not A or not B':<15}")
for a in [True, False]:
    for b in [True, False]:
        print(f"{str(a):<7}{str(b):<7}{str(a and not b):<14}"
              f"{str(not (a or b)):<15}{str(not a or not b):<15}")

# not (A or B) no coincide con not A or not B. La que sí coincide con
# not A or not B es not (A and B). Es una de las leyes de De Morgan: al negar
# una combinación, el and se vuelve or y cada parte se niega.
```

Vale la pena reconocer esa ley aunque no se llame por su nombre. Aparece cada vez que alguien
intenta negar una condición compuesta y lo hace a la mitad.

### Ejercicio 2

```python
antiguedad_anios = 3
saldo = 8500
monto_pedido = 128000
cliente_nuevo = False
AUTORIZADOS = ["Insumos SA", "Papelera del Norte", "Log Express"]
proveedor = "Otro Proveedor"

# 1. "Más de dos años Y saldo menor a diez mil"
print("Aprobar:", antiguedad_anios > 2 and saldo < 10000)

# 2. "Pedido de más de cien mil O cliente nuevo"
print("Alertar:", monto_pedido > 100000 or cliente_nuevo)

# 3. "NO está en la lista de autorizados"
print("Rechazar:", proveedor not in AUTORIZADOS)
```

La tercera se puede escribir `not (proveedor in AUTORIZADOS)` y da lo mismo. `not in` existe
precisamente porque se lee mejor.

### Ejercicio 3

```python
inversion = 38500

for clics in [0, 5074]:
    if clics > 0 and inversion / clics < 10:
        print(f"{clics:>6} clics -> costo por clic aceptable")
    else:
        print(f"{clics:>6} clics -> no evaluable o costo alto")

# Al revés truena:
try:
    clics = 0
    if inversion / clics < 10 and clics > 0:
        print("nunca llega aquí")
except ZeroDivisionError as e:
    print("ZeroDivisionError:", e)
```

La versión correcta no necesita un `if` extra ni un `try`. La guarda dentro del mismo `and` hace
todo el trabajo, y eso solo funciona por la evaluación corta.

### Ejercicio 4

```python
ULTIMO_TRIMESTRE = ["oct", "nov", "dic"]

for mes in ["ene", "jun", "sep", "oct", "nov", "dic"]:
    con_or = mes == "oct" or mes == "nov" or mes == "dic"
    con_in = mes in ULTIMO_TRIMESTRE
    print(f"{mes}   or: {str(con_or):<6} in: {str(con_in):<6} {'ok' if con_or == con_in else 'DIFIEREN'}")
```

Las dos dan lo mismo siempre. La de `in` gana cuando la política cambia: si el trimestre ahora
empieza en septiembre, se agrega un elemento a la lista y ninguna condición se toca.

### Ejercicio 5

```python
PUESTOS = ["Sales analyst", "Brand Manager", "people manager",
           "Financial Analyst", "Recruiter", "Operations Manager"]

print("Gerencias:")
for p in PUESTOS:
    if "manager" in p.lower():
        print("  ", p)

print("Analistas:")
for p in PUESTOS:
    if "analyst" in p.lower():
        print("  ", p)
```

El `.lower()` va sobre el puesto, no sobre la palabra buscada. Es el orden que importa: normalizas
el dato y comparas contra un valor que ya escribiste en minúsculas.

### Ejercicio 6

```python
uno = {"canal": "Instagram", "clics": 5074}
dos = {"canal": "Instagram", "clics": 5074}

print("uno == dos :", uno == dos)
print("uno is dos :", uno is dos)

tres = uno
print("tres is uno:", tres is uno)

tres["clics"] = 9999
print("uno después de tocar tres:", uno)

# is sería la pregunta correcta cuando lo que quieres saber es si dos nombres
# apuntan al mismo objeto, porque entonces modificar uno modifica al otro. La
# última línea lo demuestra: tocar tres cambió uno, y eso solo pasa cuando is
# da verdadero.
```

Ese comportamiento es la razón de fondo por la que `.copy()` existe en pandas, y por la que la
semana 15.2 empieza haciendo `ventas.copy()` antes de la demostración.

### Ejercicio 7

```python
def puede_enviar(peso, destino, pagado):
    return "enviar" if (pagado and peso <= 20 and destino != "internacional") else "no enviar"


CASOS = [(15, "nacional", True), (15, "nacional", False),
         (25, "nacional", True), (25, "nacional", False),
         (15, "internacional", True), (15, "internacional", False),
         (25, "internacional", True), (20, "local", True)]

for peso, destino, pagado in CASOS:
    print(f"{peso:>3} kg {destino:<15} {'pagado' if pagado else 'sin pagar':<10} -> {puede_enviar(peso, destino, pagado)}")
```

Nueve líneas y tres niveles de sangría se volvieron una. La señal estaba a la vista: los tres
`else` devolvían exactamente lo mismo.

### Ejercicio 8

No hay solución publicada porque la política es distinta para cada quien. Se califica sobre cuatro
cosas: que use los tres operadores, que la sangría no pase de dos niveles, que los cuatro casos de
la tabla de verdad estén probados, y que la condición se pueda leer en voz alta sin ambigüedad.
"""),

]

write(OUT / "es" / "w07.ipynb", es)
print("wrote", OUT / "es" / "w07.ipynb")


en = [

md("""
# Data Analysis · Week 7
## Nested selection and logical operators

**TIA502 · School of Business · Instructor David Escobar-Castillejos**

Last session was one condition at a time. This one is how they join up, and when nesting beats
combining.

By the end of this notebook you will be able to:

1. Use the three logical operators: `and` demands both, `or` settles for one, `not` inverts.
2. Read a truth table and predict the result of a compound condition without running it.
3. Ask about membership with `in` and `not in`, instead of chaining comparisons with `or`.
4. Tell `is` from `==`.
5. Decide when to nest, and recognise the nesting that was really an `and`.

### How to use this notebook

Run the cells in order. Four fail on purpose or give a deliberately surprising result, and carry a
comment saying so.

The practical rule at the end is worth more than all the theory above it: **if both branches of
the nesting do the same thing, it was an `and` in disguise.**
"""),

md("""
---
# Block 1 · Combining conditions

Three operators, and any rule can be built from them however complicated it sounds said out loud.

| Operator | What it demands | Example |
|---|---|---|
| `and` | That both conditions are true | `conversion >= 0.03 and clicks > 1000` |
| `or` | That at least one is true | `channel == "Meta" or channel == "Google"` |
| `not` | Inverts the result of the condition | `not campaign_active` |

## The truth table, generated

| A | B | `A and B` | `A or B` |
|---|---|---|---|
| `True` | `True` | `True` | `True` |
| `True` | `False` | `False` | `True` |
| `False` | `True` | `False` | `True` |
| `False` | `False` | `False` | `False` |

Rather than taking my word for it, build it.
"""),

code("""
print(f"{'A':<7}{'B':<7}{'A and B':<10}{'A or B':<10}{'not A':<7}")
print("-" * 41)

for a in [True, False]:
    for b in [True, False]:
        print(f"{str(a):<7}{str(b):<7}{str(a and b):<10}{str(a or b):<10}{str(not a):<7}")
"""),

md("""
Four rows and that is all of it. `and` is only true on the first; `or` is false only on the last.

## A rule with two conditions
"""),

code("""
conversion = 0.0342
clicks = 5074
channel = "Instagram"

if conversion >= 0.03 and clicks > 1000:
    print("The campaign qualifies for more budget.")
else:
    print("The campaign stays as it is.")
"""),

md("""
With `and`, if a single one fails, the whole rule fails. There is no middle ground.

**Why the second condition.** A high conversion over a hundred clicks means nothing: it could be
chance. Volume filters the noise, which is why the policy asks for both.

Swap the `and` for an `or` and look at who it approves.
"""),

code("""
CANDIDATES = [
    ("Instagram", 0.0342, 5074),
    ("LinkedIn", 0.0205, 640),
    ("Newsletter", 0.0810, 62),   # sky-high conversion, almost no volume
    ("Display", 0.0021, 88400),   # enormous volume, dreadful conversion
]

print(f"{'Channel':<12}{'Conv.':>8}{'Clicks':>9}   with and       with or")
print("-" * 58)

for channel, conv, clicks in CANDIDATES:
    with_and = "approves" if (conv >= 0.03 and clicks > 1000) else "no"
    with_or = "approves" if (conv >= 0.03 or clicks > 1000) else "no"
    print(f"{channel:<12}{conv:>8.2%}{clicks:>9,}   {with_and:<15}{with_or}")
"""),

md("""
With `or`, Display approves: eighty-eight thousand clicks and a conversion of 0.21 %. It is the
campaign burning the most money in the group and the rule rewards it.

That is the cost of changing one word.

## Short-circuit evaluation

If the first condition of an `and` is false, Python **does not even read the second**. It saves
work and, more importantly, prevents errors.
"""),

code("""
def check(name):
    \"\"\"Announces itself, so you can see when it runs.\"\"\"
    print(f"  (evaluating {name})")
    return True


print("With the first one false:")
result = False and check("second")
print("Result:", result)

print()
print("With the first one true:")
result = True and check("second")
print("Result:", result)
"""),

md("""
In the first case `check` never ran. That is not a curiosity: it is what lets you write conditions
that would be an error the other way round.
"""),

code("""
reported_clicks = 0

# The right order: check it is not zero first, divide afterwards.
if reported_clicks > 0 and 38500 / reported_clicks < 10:
    print("Cost per click acceptable")
else:
    print("Not enough clicks to evaluate")
"""),

code("""
# FAILS ON PURPOSE. The same pair of conditions, in the wrong order.
try:
    if 38500 / reported_clicks < 10 and reported_clicks > 0:
        print("Cost per click acceptable")
except ZeroDivisionError as e:
    print("ZeroDivisionError:", e)
"""),

md("""
The same rule, two behaviours. With the guard first, the division never happens; the other way
round, it blows up before reaching the guard.

**When one condition protects the other, it goes first.** That is not style, it is what makes the
program run.

## `not`

It inverts. It gets used rarely, and when it does, the variable should already read as a
statement.
"""),

code("""
campaign_active = False

print("not campaign_active:", not campaign_active)

if not campaign_active:
    print("The campaign is paused, there is nothing to evaluate.")
"""),

md("""
`if not campaign_active:` reads almost like English. Comparing with `if campaign_active == False:`
works the same and reads worse.
"""),

md("""
---
# Block 2 · Membership and identity

Four more operators, and two of them will save you writing the same comparison five times.

| Operator | Question | Example | Result |
|---|---|---|---|
| `in` | Is it inside? | `channel in ["Meta", "Google"]` | `False` |
| `not in` | Is it outside? | `channel not in ["TikTok"]` | `True` |
| `is` | Is it the same object? | `cost is None` | `True` |
| `is not` | Is it another object? | `cost is not None` | `False` |

## Five comparisons, or one

Chained with `or` it looks like this:

```python
if (channel == "Meta" or
    channel == "Google" or
    channel == "Instagram" or
    channel == "TikTok"):
    print("Digital channel")
```

And with `in`:
"""),

code("""
DIGITAL = ["Meta", "Google", "Instagram", "TikTok"]

channel = "Instagram"

if channel in DIGITAL:
    print("Digital channel")
else:
    print("Another channel")
"""),

md("""
The second reads at a glance and, above all, **the list can change without touching the
condition**. Adding a channel is adding an element.
"""),

code("""
DIGITAL.append("LinkedIn")

for channel in ["Instagram", "LinkedIn", "Radio", "Billboard"]:
    print(f"{channel:<12} {'digital' if channel in DIGITAL else 'traditional'}")
"""),

md("""
`in` also works on text, where it asks whether one string is contained in another.
"""),

code("""
title = "Sales analyst"

print('"analyst" in title :', "analyst" in title)
print('"Analyst" in title :', "Analyst" in title, "<- capitals matter")
print('"analyst" in title.lower() :', "analyst" in title.lower())
"""),

md("""
That is the direct ancestor of `.str.contains("manager", case=False)` from week 15.2, applied to a
single value instead of a column.

## `is` is not `==`

The most confused pair. `==` asks whether they are worth the same; `is` asks whether they are
**the same object**.
"""),

code("""
a = [1, 2, 3]
b = [1, 2, 3]

print("a == b :", a == b, "<- worth the same")
print("a is b :", a is b, "<- and not the same object")

c = a
print("c is a :", c is a, "<- c is another name for the same object")
"""),

md("""
Two lists with the same contents are equal and are not the same. It is the difference between two
sheets holding the same data and two tabs pointing at the same file.

**For numbers and text, always use `==`.** `is` on values gives results that depend on Python's
internal details and cannot be predicted.
"""),

code("""
# FAILS ON PURPOSE, in the worst way: it sometimes works.
x = 256
y = 256
print("256 is 256 :", x is y)

x = 1000
y = 1000
print("1000 is 1000 :", x is y, "<- same code, different result")

print()
print("With == it is always predictable:", 1000 == 1000)
"""),

md("""
The same code with a different number gives a different result, because Python keeps small
integers in a table and reuses them. None of that is anything you should lean on.

`is` has one correct use and this is it:
"""),

code("""
cost_per_click = None

print("cost is None     :", cost_per_click is None)
print("cost is not None :", cost_per_click is not None)

cost_per_click = 7.59
print("Now measured, is not None:", cost_per_click is not None)
"""),

md("""
`is None` and `is not None` are the correct way to ask about a missing value, because `None` is a
single unique object across the whole program.
"""),

md("""
---
# Block 3 · Nesting a decision

A decision inside another. Sometimes it is right, and sometimes it is an `and` written in the
longest possible way.

## A nesting that earns its place
"""),

code("""
campaign_active = False
conversion = 0.061

if campaign_active:
    if conversion >= 0.05:
        action = "Raise the budget"
    elif conversion >= 0.03:
        action = "Hold"
    else:
        action = "Pause and review"
else:
    action = "Reactivate before evaluating"

print(action)
"""),

md("""
Here the nesting earns something real, for three reasons.

**The first question decides whether you continue.** If the campaign is off, its conversion means
nothing: it is data from when it was on. Asking about it would be a business error.

**Each inner branch does something different.** Three outcomes, not two identical ones.

**The outer `else`** covers the whole off case without repeating the three categories.

The trace with a paused campaign at 6 % conversion:

| Step | Condition | Result | `action` |
|---|---|---|---|
| 1 | `campaign_active` | `False` | – |
| 2 | The whole inner block | Not evaluated | – |
| 3 | The outer `else` | Runs | `Reactivate before evaluating` |

The 6 % conversion is never looked at. The nesting protects it from a decision that would make no
sense to take.

## The nesting that was an `and`

Now the opposite case. Read it and look for what is redundant.
"""),

code("""
def approve_nested(conversion, clicks):
    \"\"\"Three levels of indentation for a single question.\"\"\"
    if conversion >= 0.03:
        if clicks > 1000:
            return "approves"
        else:
            return "does not approve"
    else:
        return "does not approve"


def approve_combined(conversion, clicks):
    \"\"\"The same thing, on one line.\"\"\"
    return "approves" if (conversion >= 0.03 and clicks > 1000) else "does not approve"


for conv, clicks in [(0.0342, 5074), (0.081, 62), (0.0021, 88400), (0.02, 500)]:
    a = approve_nested(conv, clicks)
    b = approve_combined(conv, clicks)
    print(f"{conv:>7.2%}{clicks:>8,}   {a:<20}{b:<20}{'same' if a == b else 'DIFFERENT'}")
"""),

md("""
Identical in all four cases, and one takes nine lines and the other one.

**The test: if both inner branches do the same thing, it was an `and`.** In `approve_nested`, the
inner `else` and the outer `else` return exactly the same thing, and that is the signal.

It is the most profitable review you can give your own code. It turns four levels of indentation
into one readable line.

## The rule, stated in full

You nest when:

1. The second question **only makes sense** if the first one held.
2. Each branch does **something different**.

If both inner branches end up doing the same thing, or if the second question can always be asked,
then it was not a nesting: it was a single condition joined with `and`.
"""),

md("""
---
## Four traps in compound conditions

### Writing `and` when you meant `or`

Read it out loud. "Both" is `and`, "either of the two" is `or`. Half the errors get caught that
way.

### Comparing against two values at once

**Predict before you run.** What does this print, if the channel is Instagram?

- **A.** `No match`, because it is neither of the two.
- **B.** `Match`, because a non-empty string evaluates as true.
- **C.** An error, because a comparison is missing.
- **D.** `Match`, because Python compares against both.
"""),

code("""
# FAILS ON PURPOSE, raising nothing. This condition does not do what it looks like.
channel = "Instagram"

if channel == "Meta" or "Google":
    print("Match")
else:
    print("No match")
"""),

md("""
The answer is **B**, and it is one of the language's nastiest traps.

Python reads that as `(channel == "Meta") or ("Google")`. The first part is false, so it evaluates
the second: bare `"Google"`, a non-empty string, which counts as true.

The condition is true **always**, for any channel.
"""),

code("""
for channel in ["Instagram", "Meta", "Radio", "anything at all"]:
    result = channel == "Meta" or "Google"
    print(f"{channel:<18} -> {result!r}")
"""),

md("""
It does not even return `True`: it returns the string `"Google"`, which inside an `if` counts as
true.

The two correct forms:
"""),

code("""
channel = "Instagram"

print("Repeating the variable:", channel == "Meta" or channel == "Google")
print("With in:               ", channel in ("Meta", "Google"))
"""),

md("""
### Using `is` to compare values

You saw it above. For numbers and text, always `==`.

### Nesting without needing to

Three levels of indentation are almost always two conditions joined with `and` and one redundant
branch.

## All together: a real policy
"""),

code("""
DIGITAL = ["Meta", "Google", "Instagram", "TikTok", "LinkedIn"]

def budget_decision(channel, active, conversion, clicks):
    \"\"\"The full policy, with all three logical operators and membership.\"\"\"
    if not active:
        return "Reactivate before evaluating"

    if channel not in DIGITAL:
        return "Outside policy, review by hand"

    if conversion >= 0.05 and clicks > 1000:
        return "Raise the budget"
    elif conversion >= 0.03 or clicks > 50000:
        return "Hold"
    else:
        return "Pause and review"


CASES = [
    ("Instagram", True, 0.061, 5074),
    ("Instagram", False, 0.061, 5074),
    ("Radio", True, 0.061, 5074),
    ("Display", True, 0.0021, 88400),
    ("LinkedIn", True, 0.0205, 640),
]

for channel, active, conv, clicks in CASES:
    state = "active" if active else "paused"
    print(f"{channel:<11}{state:<9}{conv:>7.2%}{clicks:>8,}   {budget_decision(channel, active, conv, clicks)}")
"""),

md("""
Three guards at the top and one decision at the bottom. No indentation goes past two levels, and
the function reads top to bottom like a list of rules.

That pattern, pulling the special cases out first and leaving the main logic at the end, is what
avoids deep nesting nearly every time.
"""),

md("""
---
# Exercises

The solutions sit at the very bottom of the notebook.

## Logical

### Exercise 1 · The truth table of `not` and of the combination

Generate with a loop the truth table for `A and not B` and for `not (A or B)`. Four rows each.

Then answer in a comment: does either of them match `not A or not B`?

### Exercise 2 · Reading it out loud

For each of these three rules, write the Python condition and the English sentence describing it:

1. Approve if the customer has more than two years **and** their balance is under 10,000.
2. Alert if the order exceeds 100,000 **or** the customer is new.
3. Reject if it is **not** on the authorised supplier list.

### Exercise 3 · The guard that protects

Write a condition that computes the cost per click only if there are clicks, using short-circuit
evaluation. Test it with zero clicks and with real clicks.

Then write it the other way round and confirm it blows up.

## Membership

### Exercise 4 · From five `or` to one `in`

Write a condition with four `or` clauses checking whether a month is in the last quarter, then the
same with `in`. Test both with six different months and check they agree.

### Exercise 5 · Searching inside text

With this list of job titles, print the ones containing the word "manager" ignoring capitals, and
separately the ones containing "analyst".

```python
TITLES = ["Sales analyst", "Brand Manager", "people manager",
          "Financial Analyst", "Recruiter", "Operations Manager"]
```

### Exercise 6 · `is` against `==`

Create two dictionaries with the same contents and compare them with `==` and with `is`. Then
assign one to the other and compare again.

Explain in a comment in which case `is` would be the right question.

## Nesting

### Exercise 7 · Collapsing a nesting

This code has three levels of indentation and two branches doing the same thing. Rewrite it as a
single condition.

```python
def can_ship(weight, destination, paid):
    if paid:
        if weight <= 20:
            if destination != "international":
                return "ship"
            else:
                return "do not ship"
        else:
            return "do not ship"
    else:
        return "do not ship"
```

Check with eight combinations that both versions agree.

### Exercise 8 · A policy that needs two conditions

Write a rule from your field that depends on at least two values: approving credit by income and
tenure, or prioritising an order by amount and by customer. Use `and`, `or` and `in` at least once
each.

Two levels of indentation maximum. If you need three, collapse with `and`.

The test: read it out loud to a classmate. If they have to ask "and or or?", the condition is badly
written.
"""),

md("""
---
## Three ideas to take away

**`and` demands both, `or` settles for one.** Reading the condition out loud catches half the
errors before the program runs.

**`in` replaces a row of `or` clauses.** And it lets the list of valid values change without
touching a single line of the condition.

**If both branches do the same thing, it was an `and`.** The most profitable review you can give
your code, and it turns four levels of indentation into one.

Next session is repetition, and the first midterm.
"""),

md("""
---
# Solutions

### Exercise 1

```python
print(f"{'A':<7}{'B':<7}{'A and not B':<14}{'not (A or B)':<15}{'not A or not B':<15}")
for a in [True, False]:
    for b in [True, False]:
        print(f"{str(a):<7}{str(b):<7}{str(a and not b):<14}"
              f"{str(not (a or b)):<15}{str(not a or not b):<15}")

# not (A or B) does not match not A or not B. The one that matches
# not A or not B is not (A and B). It is one of De Morgan's laws: negating a
# combination turns the and into an or and negates each part.
```

That law is worth recognising even without naming it. It turns up every time somebody tries to
negate a compound condition and only does half the job.

### Exercise 2

```python
tenure_years = 3
balance = 8500
order_amount = 128000
new_customer = False
AUTHORISED = ["Insumos SA", "Papelera del Norte", "Log Express"]
supplier = "Some Other Supplier"

# 1. "More than two years AND balance under ten thousand"
print("Approve:", tenure_years > 2 and balance < 10000)

# 2. "Order over a hundred thousand OR new customer"
print("Alert:", order_amount > 100000 or new_customer)

# 3. "NOT on the authorised list"
print("Reject:", supplier not in AUTHORISED)
```

The third can be written `not (supplier in AUTHORISED)` and means the same. `not in` exists
precisely because it reads better.

### Exercise 3

```python
spend = 38500

for clicks in [0, 5074]:
    if clicks > 0 and spend / clicks < 10:
        print(f"{clicks:>6} clicks -> cost per click acceptable")
    else:
        print(f"{clicks:>6} clicks -> not evaluable or cost too high")

# The other way round it blows up:
try:
    clicks = 0
    if spend / clicks < 10 and clicks > 0:
        print("never gets here")
except ZeroDivisionError as e:
    print("ZeroDivisionError:", e)
```

The correct version needs no extra `if` and no `try`. The guard inside the same `and` does all the
work, and that only functions because of short-circuit evaluation.

### Exercise 4

```python
LAST_QUARTER = ["oct", "nov", "dec"]

for month in ["jan", "jun", "sep", "oct", "nov", "dec"]:
    with_or = month == "oct" or month == "nov" or month == "dec"
    with_in = month in LAST_QUARTER
    print(f"{month}   or: {str(with_or):<6} in: {str(with_in):<6} {'ok' if with_or == with_in else 'DIFFER'}")
```

Both always agree. The `in` version wins when the policy changes: if the quarter now starts in
September, one element gets added to the list and no condition is touched.

### Exercise 5

```python
TITLES = ["Sales analyst", "Brand Manager", "people manager",
          "Financial Analyst", "Recruiter", "Operations Manager"]

print("Management:")
for t in TITLES:
    if "manager" in t.lower():
        print("  ", t)

print("Analysts:")
for t in TITLES:
    if "analyst" in t.lower():
        print("  ", t)
```

The `.lower()` goes on the title, not on the word being searched for. The order is what matters:
you normalise the data and compare against a value you already wrote in lowercase.

### Exercise 6

```python
one = {"channel": "Instagram", "clicks": 5074}
two = {"channel": "Instagram", "clicks": 5074}

print("one == two :", one == two)
print("one is two :", one is two)

three = one
print("three is one:", three is one)

three["clicks"] = 9999
print("one after touching three:", one)

# is would be the right question when what you want to know is whether two names
# point at the same object, because then modifying one modifies the other. The
# last line proves it: touching three changed one, and that only happens when is
# comes back true.
```

That behaviour is the underlying reason `.copy()` exists in pandas, and why week 15.2 starts by
calling `sales.copy()` before the demonstration.

### Exercise 7

```python
def can_ship(weight, destination, paid):
    return "ship" if (paid and weight <= 20 and destination != "international") else "do not ship"


CASES = [(15, "national", True), (15, "national", False),
         (25, "national", True), (25, "national", False),
         (15, "international", True), (15, "international", False),
         (25, "international", True), (20, "local", True)]

for weight, destination, paid in CASES:
    print(f"{weight:>3} kg {destination:<15} {'paid' if paid else 'unpaid':<8} -> {can_ship(weight, destination, paid)}")
```

Nine lines and three levels of indentation became one. The signal was in plain sight: all three
`else` clauses returned exactly the same thing.

### Exercise 8

There is no published solution, because the policy is different for everyone. It is graded on four
things: that all three operators are used, that indentation does not go past two levels, that all
four rows of the truth table are tested, and that the condition can be read out loud without
ambiguity.
"""),

]

write(OUT / "en" / "w07.ipynb", en)
print("wrote", OUT / "en" / "w07.ipynb")
