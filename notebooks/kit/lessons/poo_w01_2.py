"""notebooks/programacion-orientada-a-objetos/es/w01.2.ipynb

Source deck: ppts/python/programacion-orientada-a-objetos/es/w01.2.es.yaml
Source code:  docs/en/courses/python-course/01 - Basics/2nd Module/
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from nbkit import md, code, write, REPO

OUT = REPO / "notebooks" / "programacion-orientada-a-objetos"

es = [

md("""
# Programación Orientada a Objetos · Repaso 2 de 5
## Módulo 2 · Comparación, lógica y ciclos

**COM102 · Facultad de Ingeniería · Profesor David Escobar-Castillejos**

Comparar, decidir y repetir. Los cuatro grupos de operadores y las dos formas de ciclo.

Al terminar este cuaderno vas a poder:

1. Usar los seis operadores de comparación, y saber qué pasa al comparar cadenas.
2. Combinar condiciones con `and`, `or` y `not`, incluida la evaluación de cortocircuito.
3. Distinguir `in` de `is`.
4. Escribir `if`, `elif`, `else` y el ternario.
5. Elegir entre `for` y `while` por la pregunta que contestan.

### Cómo se usa este cuaderno

Ejecuta las celdas en orden. Seis fallan a propósito y llevan un comentario que lo dice.

El ciclo infinito va con un tope de seguridad: en un cuaderno, uno de verdad cuelga el kernel y hay
que reiniciarlo perdiendo todas las variables.
"""),

md("""
---
# Bloque 1 · Comparar

Toda decisión empieza por una pregunta cuya respuesta es verdadero o falso.

| Operador | Pregunta | Ejemplo | Resultado |
|---|---|---|---|
| `==` | ¿Son iguales? | `5 == 5` | `True` |
| `!=` | ¿Son distintos? | `5 != 5` | `False` |
| `>` | ¿Mayor que? | `5 > 3` | `True` |
| `<` | ¿Menor que? | `5 < 3` | `False` |
| `>=` | ¿Mayor o igual? | `5 >= 5` | `True` |
| `<=` | ¿Menor o igual? | `5 <= 5` | `True` |
"""),

code("""
for expresion, resultado in [("5 == 5", 5 == 5), ("5 != 5", 5 != 5), ("5 > 3", 5 > 3),
                             ("5 < 3", 5 < 3), ("5 >= 5", 5 >= 5), ("5 <= 5", 5 <= 5)]:
    print(f"{expresion:<8} -> {resultado}")
"""),

md("""
## Las cadenas se comparan letra por letra

Y esa comparación usa el valor numérico de cada carácter, no el alfabeto que tú tienes en la
cabeza.
"""),

code("""
print('"Python" == "python" ->', "Python" == "python")
print('"bag" > "apple"      ->', "bag" > "apple")
print('"Z" < "a"            ->', "Z" < "a", "<- las mayúsculas van antes")
print()
print("ord('b') =", ord("b"), "· ord('B') =", ord("B"), "· ord('Z') =", ord("Z"), "· ord('a') =", ord("a"))
"""),

md("""
`"Z" < "a"` es verdadero porque la Z mayúscula vale 90 y la a minúscula vale 97. Todas las
mayúsculas quedan antes que todas las minúsculas.

Eso muerde al ordenar una lista de nombres capturados a mano.
"""),

code("""
nombres = ["ana", "Beto", "carla", "Diego"]

print("Ordenados tal cual:", sorted(nombres))
print("Normalizando:      ", sorted(nombres, key=str.lower))
"""),

md("""
## Los tres que combinan

| Operador | Es verdadero cuando | Ejemplo | Resultado |
|---|---|---|---|
| `and` | Las dos partes son verdaderas | `True and False` | `False` |
| `or` | Al menos una es verdadera | `True or False` | `True` |
| `not` | La parte es falsa | `not True` | `False` |
"""),

code("""
print(f"{'A':<7}{'B':<7}{'A and B':<10}{'A or B':<10}{'not A':<7}")
print("-" * 41)
for a in [True, False]:
    for b in [True, False]:
        print(f"{str(a):<7}{str(b):<7}{str(a and b):<10}{str(a or b):<10}{str(not a):<7}")
"""),

md("""
## El cortocircuito

Con `and`, si la primera parte es falsa, Python ya sabe la respuesta y **no mira la segunda**. Con
`or` pasa lo contrario: si la primera es verdadera, se salta el resto.
"""),

code("""
def mira(nombre):
    print(f"  (evaluando {nombre})")
    return True


print("False and mira('segunda'):", False and mira("segunda"))
print()
print("True or mira('segunda'):", True or mira("segunda"))
print()
print("True and mira('segunda'):", True and mira("segunda"))
"""),

md("""
En los dos primeros casos `mira` nunca corrió.

Eso no es una curiosidad de rendimiento: **es lo que permite escribir guardas seguras.**
"""),

code("""
datos = []

# La guarda primero: el índice nunca llega a evaluarse.
if datos and datos[0] > 10:
    print("El primero es grande")
else:
    print("Lista vacía o el primero no pasa de diez")
"""),

code("""
# FALLA A PROPÓSITO. Las mismas dos condiciones, en el orden equivocado.
try:
    if datos[0] > 10 and datos:
        print("nunca llega aquí")
except IndexError as e:
    print("IndexError:", e)
"""),

md("""
**Cuando una condición protege a la otra, va primero.** No es estilo, es lo que hace que el programa
corra.

## Los cuatro que se confunden

| Operador | Pregunta | Ejemplo | Resultado |
|---|---|---|---|
| `in` | ¿Está dentro? | `"Pro" in "Programming"` | `True` |
| `not in` | ¿No está dentro? | `"swift" not in "Python"` | `True` |
| `is` | ¿Es el mismo objeto? | `a = [1]; b = a; a is b` | `True` |
| `is not` | ¿Es otro objeto? | `[1] is not [1]` | `True` |
"""),

code("""
print('"Pro" in "Programming"  ->', "Pro" in "Programming")
print('"swift" not in "Python" ->', "swift" not in "Python")
print('3 in [1, 2, 3]          ->', 3 in [1, 2, 3])
print('"a" in {"a": 1}         ->', "a" in {"a": 1}, "<- en un diccionario busca la llave")
"""),

md("""
## `is` no es `==`

El doble igual pregunta si dos cosas **valen** lo mismo. `is` pregunta si **son** exactamente el
mismo objeto en memoria.
"""),

code("""
a = [1, 2]
b = [1, 2]
c = a

print("a == b:", a == b, "<- valen lo mismo")
print("a is b:", a is b, "<- y no son la misma")
print("a is c:", a is c, "<- c es otro nombre para a")
"""),

code("""
# FALLA A PROPÓSITO, y de la peor forma: a veces funciona.
x = 256; y = 256
print("256 is 256  ->", x is y)

x = 1000; y = 1000
print("1000 is 1000 ->", x is y, "<- el mismo código, otro resultado")
"""),

md("""
Python guarda los enteros chicos en una tabla y los reutiliza. Nada de eso es algo en lo que
apoyarse.

**`is` solo se usa con `None`, `True` y `False`.** Para cualquier otra comparación, el doble igual
es lo que quieres.
"""),

code("""
resultado = None

print("resultado is None    ->", resultado is None)
print("resultado is not None->", resultado is not None)
"""),

md("""
El repaso 4 vuelve a esto con las copias de listas, y ahí es donde de verdad cuesta.
"""),

md("""
---
# Bloque 2 · Decidir

Una condición sin bloque no sirve de nada. **La indentación es la que dice qué se ejecuta.**
"""),

code("""
temperature = 20

if temperature > 30:
    print("Hace calor")
elif temperature > 20:
    print("Buen día")
elif temperature > 10:
    print("Hace algo de frío")
else:
    print("Hace frío")

print("Listo")
"""),

md("""
Con 20 grados entra la tercera rama, no la segunda. `temperature > 20` es falso porque 20 no es
mayor que 20.

**Ese es el error de la frontera**, y es el que más se cobra. Si el 20 debe contar como buen día, la
condición es `>=`.
"""),

code("""
def clasificar(t, incluir_limite):
    if t > 30:
        return "calor"
    elif (t >= 20 if incluir_limite else t > 20):
        return "buen día"
    elif t > 10:
        return "algo de frío"
    return "frío"


for t in [19, 20, 21, 30, 31]:
    print(f"{t:>3}°  con >  : {clasificar(t, False):<13} con >= : {clasificar(t, True)}")
"""),

md("""
Solo el renglón del 20 cambia. Una prueba que no incluya el valor exacto del límite no encuentra
nada.

## El orden manda

Se evalúan de arriba abajo y se detiene en la primera verdadera. Al revés, una rama se vuelve
inalcanzable.
"""),

code("""
# FALLA A PROPÓSITO. Con el orden invertido, "calor" nunca se alcanza.
def clasificar_mal(t):
    if t > 10:
        return "algo de frío"
    elif t > 20:
        return "buen día"
    elif t > 30:
        return "calor"
    return "frío"


for t in [5, 15, 25, 35]:
    print(f"{t:>3}°  bien: {clasificar(t, False):<13} mal: {clasificar_mal(t)}")
"""),

md("""
Con el orden malo, cualquier temperatura arriba de diez cae en "algo de frío". Dos de las cuatro
ramas son inalcanzables y la función no lanza nada.

## El ternario

Cuando lo único que quieres es elegir entre dos valores, cabe en una línea.
"""),

code("""
edad = 20

estado = "mayor" if edad >= 18 else "menor"
print(estado)

# Lo mismo con if/else de cuatro líneas.
if edad >= 18:
    estado = "mayor"
else:
    estado = "menor"
print(estado)
"""),

md("""
El ternario se lee bien con dos opciones y se vuelve ilegible con tres. Ahí conviene el `if`/`elif`
normal.

## Un solo igual dentro de un `if`
"""),

code("""
# FALLA A PROPÓSITO. Un signo asigna, dos comparan.
try:
    compile("if temperature = 20:\\n    print('sí')", "<ejemplo>", "exec")
except SyntaxError as e:
    print("SyntaxError:", e.msg)
"""),

md("""
Python lo rechaza al leer el archivo, y eso te está salvando. En otros lenguajes esa línea compila,
asigna 20 y la condición siempre es verdadera.
"""),

md("""
---
# Bloque 3 · Repetir

Dos formas, y la pregunta que contestan es distinta.

| Ciclo | Cuándo se usa | La pregunta |
|---|---|---|
| `for` | Sabes cuántas vueltas, o tienes algo que recorrer | ¿Para cada uno de estos? |
| `while` | No sabes cuántas, solo cuándo parar | ¿Mientras se cumpla esto? |
"""),

code("""
contador = 0

while contador < 3:
    print("vuelta", contador)
    contador += 1        # sin esta línea, nunca termina

print("Salió con contador =", contador)
"""),

code("""
for n in range(10):
    if n == 3:
        continue         # salta a la siguiente vuelta
    if n == 6:
        break            # abandona el ciclo
    print(n, end=" ")
print()
"""),

md("""
`continue` se salta el resto del cuerpo y sigue con la vuelta siguiente. `break` sale del ciclo por
completo, sin evaluar la condición otra vez.

Por eso imprimió `0 1 2 4 5`: se saltó el 3 y se detuvo antes del 6.

## Las tres piezas de todo ciclo

Inicialización, condición de salida y avance. El `while` te obliga a escribirlas; el `for` las pone
solo, y por eso es más difícil equivocarse con él.
"""),

code("""
# Con while, las tres piezas visibles.
i = 0                    # inicialización
while i < 5:             # condición de salida
    print(i, end=" ")
    i += 1               # avance
print()

# Con for, las tres implícitas.
for i in range(5):
    print(i, end=" ")
print()
"""),

md("""
## El ciclo infinito

Quita el avance y la condición nunca cambia. Aquí va con tope, porque uno de verdad cuelga el
kernel del cuaderno.
"""),

code("""
# CICLO INFINITO A PROPÓSITO, con tope de seguridad.
contador = 0
vueltas = 0
TOPE = 500

while contador < 3:
    vueltas += 1
    # falta el contador += 1
    if vueltas >= TOPE:
        print(f"Detenido por el tope tras {vueltas} vueltas.")
        print(f"contador sigue en {contador} y la condición sigue siendo verdadera.")
        break
"""),

md("""
**La revisión de todo `while`**: señala con el dedo la línea del cuerpo que cambia la condición. Si
no la encuentras, el ciclo no termina.

## Predice antes de correr

¿Cuántas veces se imprime "hola"?

- **A.** Tres veces.
- **B.** Cinco veces.
- **C.** Seis veces.
- **D.** Nunca, el programa entra en bucle infinito.
"""),

code("""
contador = 0

while contador < 3:
    print("hola")
    contador += 1

for i in range(2):
    print("hola")
"""),

md("""
La respuesta es **B**, cinco.

| Paso | Instrucción | `contador` | `i` | Impresiones |
|---|---|---|---|---|
| 1 | `contador = 0` | 0 | – | 0 |
| 2 | `while 0 < 3` | 1 | – | 1 |
| 3 | `while 1 < 3` | 2 | – | 2 |
| 4 | `while 2 < 3` | 3 | – | 3 |
| 5 | `while 3 < 3` es falso | 3 | – | 3 |
| 6 | `for i in range(2)` | 3 | 0, 1 | 5 |

El `while` corre tres veces y el `for` dos.

## Cuatro errores de este módulo

**Comparar con un solo igual.** `SyntaxError`. Un signo asigna, dos comparan.

**Fallar en la frontera.** "Mayor que 20" excluye al 20.

**Ciclo infinito.** La variable de control nunca se modifica dentro del cuerpo.

**Usar `is` en lugar de `==`.** `is` compara identidad. Solo con `None`, `True` y `False`.

Los cuatro corrieron arriba.
"""),

md("""
---
# Ejercicios

Las soluciones están hasta abajo del cuaderno.

### Ejercicio 1 · Los seis, con cadenas

Compara `"Python"` contra `"python"`, `"Java"` y `"Python "` con los seis operadores. Explica en un
comentario por qué la tercera no es igual.

### Ejercicio 2 · La tabla de verdad completa

Genera con un ciclo la tabla de `A and not B`, `not (A and B)` y `not A or not B`. Di en un
comentario cuáles dos coinciden.

### Ejercicio 3 · La guarda que protege

Escribe una función `primero_grande(datos)` que devuelva verdadero si el primer elemento pasa de
diez, y que no truene con una lista vacía. Usa cortocircuito, sin `if` anidado.

Pruébala con lista vacía, con `[5]` y con `[50]`.

### Ejercicio 4 · `is` contra `==`

Demuestra con cuatro casos la diferencia: dos listas iguales, dos nombres de la misma lista, dos
enteros chicos y dos enteros grandes.

### Ejercicio 5 · La frontera

Escribe `calificar(puntos)` con cuatro rangos, y prueba los tres valores alrededor de cada límite.
Son nueve pruebas.

Di en un comentario, por cada límite, si el valor exacto sube o baja de categoría y por qué.

### Ejercicio 6 · La rama inalcanzable

Escribe a propósito una versión de `calificar` con los rangos al revés, y demuestra con código que
una categoría nunca se alcanza recorriendo todos los puntajes posibles.

### Ejercicio 7 · Los dos ciclos

Resuelve lo mismo dos veces, con `for` y con `while`: sumar los números del 1 al 100 que sean
múltiplos de tres. Compara cuál se lee mejor.

### Ejercicio 8 · La tarea

Escribe un programa que pida números hasta que el usuario escriba cero, y al final diga cuántos
fueron pares y cuántos impares.

Como `input` detiene el cuaderno, escríbelo primero con una lista de respuestas simuladas, y
después en una celda nueva al final con `input` de verdad.
"""),

md("""
---
## Tres ideas para llevarse

**El orden de las condiciones importa.** Se detiene en la primera verdadera, así que la más
específica va arriba. Al revés, una rama se vuelve inalcanzable sin lanzar nada.

**El cortocircuito no es un detalle.** Es lo que permite escribir guardas que no truenan con datos
vacíos, y cambiar el orden de las dos condiciones rompe el programa.

**Todo ciclo necesita tres piezas.** Inicialización, condición de salida y avance, aunque el `for`
las ponga solo.

El siguiente repaso son funciones con parámetros, retorno y alcance.
"""),

md("""
---
# Soluciones

### Ejercicio 1

```python
base = "Python"
for otro in ["python", "Java", "Python "]:
    print(f"{otro!r:<10} == {base == otro}  != {base != otro}  "
          f"> {base > otro}  < {base < otro}  >= {base >= otro}  <= {base <= otro}")

# "Python " no es igual porque tiene un espacio al final, y un espacio es un
# carácter como cualquier otro. len() lo delata: siete contra seis. Es el mismo
# problema que las regiones sucias de un archivo capturado a mano.
```

### Ejercicio 2

```python
print(f"{'A':<7}{'B':<7}{'A and not B':<14}{'not (A and B)':<16}{'not A or not B':<15}")
for a in [True, False]:
    for b in [True, False]:
        print(f"{str(a):<7}{str(b):<7}{str(a and not b):<14}"
              f"{str(not (a and b)):<16}{str(not a or not b):<15}")

# Coinciden not (A and B) y not A or not B. Es una de las leyes de De Morgan: al
# negar una combinación, el and se vuelve or y cada parte se niega.
```

Esa ley aparece cada vez que alguien intenta negar una condición compuesta y lo hace a la mitad.

### Ejercicio 3

```python
def primero_grande(datos):
    \"\"\"Verdadero si el primer elemento pasa de diez. Falso con lista vacía.\"\"\"
    return bool(datos) and datos[0] > 10


for caso in [[], [5], [50]]:
    print(f"{str(caso):<8} -> {primero_grande(caso)}")
```

El `bool(datos)` de la izquierda protege al índice de la derecha. Sin cortocircuito haría falta un
`if` anidado de cuatro líneas.

El `bool(...)` alrededor no es obligatorio, y sin él la función devolvería la lista vacía en lugar
de `False`. Las dos cuentan como falsas en un `if`, y devolver un booleano de verdad es más
honesto.

### Ejercicio 4

```python
print("[1,2] == [1,2] :", [1, 2] == [1, 2])
print("[1,2] is [1,2] :", [1, 2] is [1, 2])

a = [1, 2]; b = a
print("b is a         :", b is a)

x = 256; y = 256
print("256 is 256     :", x is y)
x = 1000; y = 1000
print("1000 is 1000   :", x is y)
```

Los dos últimos dan resultados distintos con el mismo código, y esa es toda la razón para no usar
`is` con números.

### Ejercicio 5

```python
def calificar(puntos):
    if puntos >= 90:
        return "excelente"
    elif puntos >= 80:
        return "bueno"
    elif puntos >= 70:
        return "suficiente"
    return "insuficiente"


for limite in [70, 80, 90]:
    for p in [limite - 1, limite, limite + 1]:
        print(f"{p:>4} -> {calificar(p)}")
    print()

# En los tres límites el valor exacto sube de categoría, porque usé >=. Para
# calificaciones me parece lo correcto: una política que dice "80 o más es bueno"
# incluye al 80. Si dijera "más de 80", habría que usar > y el 80 caería en
# suficiente. La frase de la política decide, no la comodidad del código.
```

### Ejercicio 6

```python
def calificar_mal(puntos):
    if puntos >= 70:
        return "suficiente"
    elif puntos >= 80:
        return "bueno"
    elif puntos >= 90:
        return "excelente"
    return "insuficiente"


conteo_bien = {}
conteo_mal = {}
for p in range(0, 101):
    conteo_bien[calificar(p)] = conteo_bien.get(calificar(p), 0) + 1
    conteo_mal[calificar_mal(p)] = conteo_mal.get(calificar_mal(p), 0) + 1

print("Con el orden bueno:", conteo_bien)
print("Con el orden malo: ", conteo_mal)
```

Con el orden malo, `bueno` y `excelente` salen en cero sobre 101 puntajes probados. Una categoría
con cero casos después de recorrer todo el rango es la firma de una rama inalcanzable.

### Ejercicio 7

```python
total = 0
for n in range(1, 101):
    if n % 3 == 0:
        total += n
print("Con for:  ", total)

total = 0
n = 1
while n <= 100:
    if n % 3 == 0:
        total += n
    n += 1
print("Con while:", total)

print("Y en una línea:", sum(n for n in range(1, 101) if n % 3 == 0))
```

Los tres dan 1683. La versión con `while` tiene dos líneas más y ninguna es sobre el problema: son
sobre llevar la cuenta.

Aquí el `for` es lo correcto porque sabes cuántas vueltas hay antes de empezar.

### Ejercicio 8

```python
# Primero con respuestas simuladas, para que corra sin detenerse.
RESPUESTAS = ["4", "7", "12", "9", "0"]

pares = impares = 0
for escrito in RESPUESTAS:
    n = int(escrito)
    if n == 0:
        break
    if n % 2 == 0:
        pares += 1
    else:
        impares += 1

print(f"Pares: {pares} · impares: {impares}")

# Y con input de verdad, en una celda nueva al final del cuaderno:
#
# pares = impares = 0
# while True:
#     n = int(input("Número (0 para terminar): "))
#     if n == 0:
#         break
#     if n % 2 == 0:
#         pares += 1
#     else:
#         impares += 1
# print(f"Pares: {pares} · impares: {impares}")
```

Nota que el cero **no se cuenta**: el `break` va antes de la clasificación. Si fuera después, el
cero contaría como par y el conteo saldría con uno de más.

Ese detalle de dónde poner el `break` es el que decide si el centinela entra o no en el resultado.
"""),

]

write(OUT / "es" / "w01.2.ipynb", es)
print("wrote", OUT / "es" / "w01.2.ipynb")
