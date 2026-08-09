"""notebooks/programacion-orientada-a-objetos/{es,en}/w01.1.ipynb

Source deck: ppts/python/programacion-orientada-a-objetos/{es,en}/w01.1.*.yaml
Source code:  docs/en/courses/python-course/01 - Basics/1st Module/Code001-Code005.py
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from nbkit import md, code, write, REPO

OUT = REPO / "notebooks" / "programacion-orientada-a-objetos"

es = [

md("""
# Programación Orientada a Objetos · Repaso 1 de 5
## Módulo 1 · Datos y texto

**COM102 · Facultad de Ingeniería · Profesor David Escobar-Castillejos**

Primera de cinco sesiones de repaso, una por módulo de `01 - Basics`. Esta cubre el módulo 1
completo, de `Code001` a `Code005`.

No es material nuevo. Es el piso sobre el que se para todo lo que viene, y un par de cosas de aquí
van a reaparecer en la semana 3 con otro nombre: cuando veas que un atributo puede romper un
método, va a ser esto mismo.

Al terminar este cuaderno vas a poder:

1. Declarar variables de los cinco tipos básicos y saber cuál corresponde a cada dato.
2. Explicar el tipado dinámico: por qué el nombre no tiene tipo y el valor sí.
3. Cortar y componer texto con índices, rebanadas y f-strings.
4. Usar los siete operadores aritméticos y sus siete versiones cortas.
5. Convertir lo que llega de `input`, y reconocer el `TypeError` de no hacerlo.

### Cómo se usa este cuaderno

Ejecuta las celdas en orden con **Shift + Enter**. Seis fallan a propósito y llevan un comentario
que lo dice.

Hay **una sola celda con `input` de verdad**, marcada. En Colab abre un cuadro de texto y espera;
todo lo demás usa valores ya asignados para que "Ejecutar todo" no se quede detenido.
"""),

md("""
---
# Bloque 1 · Variables y tipos

Lo primero que hace cualquier programa es guardar algo y darle un nombre para volver a
encontrarlo.

Una variable es un nombre atado a un valor. **El nombre no tiene tipo; el valor sí.**

| Tipo | Qué guarda | Ejemplo | Su valor falso |
|---|---|---|---|
| `int` | Enteros, sin límite de tamaño | `student_count = 1000` | `0` |
| `float` | Decimales, con precisión limitada | `rating = 4.99` | `0.0` |
| `bool` | Verdadero o falso | `is_published = False` | `False` |
| `str` | Texto, entre comillas | `course = "Python"` | `""` vacía |
| `NoneType` | La ausencia de valor | `resultado = None` | `None` |
"""),

code("""
student_count = 1000          # int
rating = 4.99                 # float
is_published = False          # bool
course_name = "Python"        # str
resultado = None              # NoneType

print(type(student_count), type(rating), type(is_published))
print(type(course_name), type(resultado))
"""),

md("""
## Tipado dinámico

La misma variable puede guardar un número y después una cadena, sin que Python se queje.
"""),

code("""
student_count = 1000
print(student_count, type(student_count))

student_count = "1000"        # ahora es str
print(student_count, type(student_count))
"""),

md("""
**Ningún error avisa en ese momento.** El programa truena más adelante, cuando alguien intenta
operar con lo que ya dejó de ser un número.
"""),

code("""
# FALLA A PROPÓSITO. El error aparece lejos de donde está la causa.
student_count = 1000
student_count = "1000"        # <- aquí está la causa

print("El programa sigue...")

try:
    print(student_count + 500)
except TypeError as e:
    print("TypeError:", e)
"""),

md("""
Un nombre que a mitad del programa guarda otra cosa es la fuente de bugs más barata de evitar: se
evita no reasignándolo.

Esa idea vuelve en la semana 3. Un atributo de un objeto es exactamente una variable con otro
alcance, y reasignarle otro tipo rompe cualquier método que lo use.

## Asignación múltiple
"""),

code("""
x, y = 1, 2
print(x, y)

x, y = y, x                   # el intercambio, sin variable temporal
print(x, y)

a = b = c = 0                 # los tres al mismo valor
print(a, b, c)
"""),

md("""
## Los valores falsos

Cada tipo tiene un valor que cuenta como falso en una condición. Todos los demás cuentan como
verdaderos.
"""),

code("""
for valor in [0, 0.0, False, "", None, [], {}]:
    print(f"{str(valor)!r:<8} -> {bool(valor)}")
"""),

code("""
# FALLA A PROPÓSITO en la intuición. Cualquier cadena no vacía es verdadera.
print('bool("0")  ->', bool("0"), "<- sorprende")
print('bool(" ")  ->', bool(" "), "<- un espacio también")
print('bool("")   ->', bool(""))
print('bool("False") ->', bool("False"), "<- incluso esta")
"""),

md("""
`bool("0")` es verdadero porque `"0"` es una cadena con un carácter dentro. Lo que Python mira es
si está vacía, no qué dice.

Ese es el error que produce validaciones que dejan pasar todo.
"""),

md("""
---
# Bloque 2 · Texto

Una cadena es una secuencia de caracteres, y casi todo lo que aprendas de ella sirve después para
las listas.
"""),

code("""
course = "Python Programming"

print("Largo:        ", len(course))
print("El primero:   ", course[0])
print("El último:    ", course[-1])
print("Del 0 al 2:   ", course[0:3])
print("Desde el 7:   ", course[7:])
print("Hasta el 6:   ", course[:6])
print("Al revés:     ", course[::-1])
"""),

md("""
El primer índice entra, el segundo no. Por eso `course[0:3]` devuelve tres caracteres, y por eso
`course[0:3] + course[3:]` reconstruye la cadena completa.
"""),

code("""
print(course[0:3] + course[3:] == course)
"""),

md("""
## Los métodos devuelven copias

Una cadena **no se puede modificar**. Todo método de cadena devuelve algo nuevo.
"""),

code("""
# FALLA A PROPÓSITO. Una cadena es inmutable.
try:
    course[0] = "J"
except TypeError as e:
    print("TypeError:", e)
"""),

code("""
# FALLA A PROPÓSITO. Llamar al método y no guardar lo que devuelve.
course = "Python Programming"
course.upper()

print("Después de course.upper():", course, "<- sin cambios")

course = course.upper()
print("Guardando el resultado:   ", course)
"""),

md("""
Ese es el tercer error del módulo, y es el mismo patrón que vas a ver con `sort` en el repaso 4:
algunas cosas devuelven y otras modifican, y confundirlas hace que el programa corra sin hacer
nada.
"""),

code("""
course = "Python Programming"

print("upper:      ", course.upper())
print("lower:      ", course.lower())
print("title:      ", course.title())
print("strip:      ", repr("  hola  ".strip()))
print("replace:    ", course.replace("Python", "Java"))
print("split:      ", course.split())
print("find:       ", course.find("Pro"))
print("startswith: ", course.startswith("Py"))
print("in:         ", "Program" in course)
print()
print("Y el original sigue:", course)
"""),

md("""
## f-strings
"""),

code("""
nombre = "Ana"
edad = 21
promedio = 9.4567

print(f"{nombre} tiene {edad} años")
print(f"Su promedio es {promedio:.2f}")
print(f"Dentro de cinco años tendrá {edad + 5}")
print(f"En mayúsculas: {nombre.upper()}")
print(f"Alineado: [{nombre:>10}] [{nombre:<10}]")
"""),

md("""
Dentro de las llaves puede ir una variable, una expresión o una llamada. Después de los dos puntos
va el formato, y no cambia el valor guardado.
"""),

md("""
---
# Bloque 3 · Operadores

Los siete aritméticos, completos.

| Operador | Qué hace | Ejemplo | Resultado |
|---|---|---|---|
| `+` | Suma | `10 + 3` | `13` |
| `-` | Resta | `10 - 3` | `7` |
| `*` | Producto | `10 * 3` | `30` |
| `/` | División decimal | `10 / 3` | `3.333…` |
| `//` | División entera | `10 // 3` | `3` |
| `%` | Residuo | `10 % 3` | `1` |
| `**` | Potencia | `10 ** 3` | `1000` |
"""),

code("""
for op, resultado in [("10 + 3", 10 + 3), ("10 - 3", 10 - 3), ("10 * 3", 10 * 3),
                      ("10 / 3", 10 / 3), ("10 // 3", 10 // 3),
                      ("10 % 3", 10 % 3), ("10 ** 3", 10 ** 3)]:
    print(f"{op:<10} = {resultado}")
"""),

md("""
## Las dos divisiones no dan lo mismo

La barra sencilla **siempre** devuelve un `float`, aunque la división sea exacta. La barra doble
descarta la parte decimal.
"""),

code("""
print("10 / 5  =", 10 / 5, type(10 / 5).__name__, "<- float aunque sea exacta")
print("10 // 5 =", 10 // 5, type(10 // 5).__name__)
print()
print("10 / 4  =", 10 / 4)
print("10 // 4 =", 10 // 4)
print("10 % 4  =", 10 % 4)
print()
print("El cociente y el residuo reconstruyen el original:", 10 // 4 * 4 + 10 % 4)
"""),

md("""
El residuo contesta otra pregunta: qué sobró después de repartir.
"""),

code("""
for n in range(1, 11):
    print(f"{n:>3} es par: {n % 2 == 0:<6} múltiplo de 3: {n % 3 == 0}")
"""),

md("""
`n % 2 == 0` es la prueba de par y `n % 3 == 0` la de múltiplo de tres. Eso es exactamente lo que
pide FizzBuzz en el repaso 3.

## Los siete, en versión corta

| Operador | Equivale a | Partiendo de `x = 10` | `x` queda en |
|---|---|---|---|
| `+=` | `x = x + 3` | `x += 3` | `13` |
| `-=` | `x = x - 3` | `x -= 3` | `7` |
| `*=` | `x = x * 3` | `x *= 3` | `30` |
| `/=` | `x = x / 3` | `x /= 3` | `3.333…` |
| `//=` | `x = x // 3` | `x //= 3` | `3` |
| `%=` | `x = x % 3` | `x %= 3` | `1` |
| `**=` | `x = x ** 3` | `x **= 3` | `1000` |
"""),

code("""
for etiqueta, operacion in [("+=", lambda x: x + 3), ("-=", lambda x: x - 3),
                            ("*=", lambda x: x * 3), ("/=", lambda x: x / 3),
                            ("//=", lambda x: x // 3), ("%=", lambda x: x % 3),
                            ("**=", lambda x: x ** 3)]:
    x = 10
    x = operacion(x)
    print(f"x = 10; x {etiqueta:<4} 3  ->  {x}")
"""),

md("""
Ojo con `/=`: convierte un entero en decimal, y `//=` no. Esa diferencia se cuela en reportes donde
de pronto todo se imprime con `.0` al final.
"""),

md("""
---
# Bloque 4 · Entrada por consola

`input` **siempre** devuelve texto. Sin excepción.

Esta es la única celda del cuaderno que espera por ti.
"""),

code("""
# ESTA CELDA ESPERA POR TI. En Colab abre un cuadro de texto arriba.
# El try es para que un "Ejecutar todo" sin teclado no se quede colgado.
try:
    x = input("Escribe un número: ")
except Exception:
    x = "5"
    print("(sin teclado disponible, se usa 5)")

print("Lo que llegó:", repr(x), type(x))
print("Convertido:  ", int(x), type(int(x)))
"""),

md("""
De aquí en adelante todo usa valores ya asignados. Pero conviene ver qué pasa sin convertir.

**Predice antes de correr.** ¿Qué imprime la última línea?

- **A.** 3, porque 200 tiene tres dígitos.
- **B.** 6, porque repitió el texto "100" dos veces.
- **C.** Error, no se puede multiplicar texto.
- **D.** 2, porque `total` vale 200 y `len` cuenta dos cosas.
"""),

code("""
precio = "100"

total = precio * 2

print(total)
print(len(total))
"""),

md("""
La respuesta es **B**, seis.

| Paso | Instrucción | `precio` | `total` | Tipo de `total` |
|---|---|---|---|---|
| 1 | `precio = "100"` | `"100"` | – | `str` |
| 2 | `total = precio * 2` | `"100"` | `"100100"` | `str` |
| 3 | `len(total)` | `"100"` | `"100100"` | `6` |

Multiplicar una cadena por un entero **la repite**. Para operar con números hace falta
`int(precio)` primero.

Y no lanzó ningún error, que es lo peligroso.
"""),

code("""
precio = "100"

print("Sin convertir:", precio * 2)
print("Convertido:   ", int(precio) * 2)
"""),

code("""
# FALLA A PROPÓSITO. Sumar texto y número sí lanza.
try:
    print("100" + 2)
except TypeError as e:
    print("TypeError:", e)
"""),

md("""
Multiplicar texto por entero funciona y sumarlos no. Esa inconsistencia es la que hace que el error
aparezca a veces sí y a veces no.

## Las conversiones
"""),

code("""
for valor in ["100", "4.99", "abc", "", "  7  "]:
    for conv in (int, float):
        try:
            print(f"{conv.__name__}({valor!r:<8}) -> {conv(valor)}")
        except ValueError as e:
            print(f"{conv.__name__}({valor!r:<8}) -> ValueError")
"""),

md("""
`int("4.99")` falla y `float("4.99")` funciona: `int` no redondea texto con punto decimal.

## Cuatro errores de este módulo

**Operar con lo que llegó de `input`.** `TypeError`, porque `input` devuelve `str`.

**Creer que `bool("0")` es `False`.** Cualquier cadena no vacía es verdadera.

**Llamar a un método y no guardarlo.** `course.upper()` no cambia `course`.

**Confundir la barra sencilla con la doble.** La sencilla siempre da `float`.

Los cuatro corrieron arriba.
"""),

md("""
---
# Ejercicios

Las soluciones están hasta abajo del cuaderno.

### Ejercicio 1 · Los cinco tipos

Declara una variable de cada uno de los cinco tipos, con nombres que digan qué guardan, e imprime
cada una con su `type` y con su valor de verdad.

### Ejercicio 2 · El tipo que cambia

Escribe un programa de cinco líneas donde una variable empiece siendo un número, se vuelva texto a
la mitad, y truene tres líneas después al operar con ella. Atrapa el error e imprímelo.

### Ejercicio 3 · Rebanadas

Con `curso = "Programación Orientada a Objetos"`, extrae: la primera palabra, la última, los
primeros diez caracteres, los últimos siete, y la cadena al revés.

Comprueba que la original no cambió.

### Ejercicio 4 · Los métodos que no guardas

Toma una cadena y aplícale cinco métodos sin guardar el resultado. Imprime la cadena después de
cada uno para comprobar que sigue igual. Después hazlo bien.

### Ejercicio 5 · Los siete operadores

Con `a = 17` y `b = 5`, imprime los siete resultados con su etiqueta. Después comprueba que
`a // b * b + a % b` reconstruye `a`.

### Ejercicio 6 · Par, impar y múltiplo

Escribe un programa que recorra del 1 al 20 e imprima, por cada número, si es par y si es múltiplo
de cinco. Usa solo el residuo.

### Ejercicio 7 · La conversión que hace falta

Estos valores llegaron como texto. Calcula el total y el promedio, y maneja el que no se puede
convertir sin que el programa se detenga.

```python
ENTRADAS = ["100", "250", "no capturado", "75", "300"]
```

### Ejercicio 8 · La tarea

Escribe un programa que pida nombre y edad por teclado, y salude con una f-string diciendo en qué
año cumplió esa edad.

Escríbelo en una celda nueva al final y córrelo tú, a mano.
"""),

md("""
---
## Tres ideas para llevarse

**El nombre no tiene tipo, el valor sí.** En tres semanas eso mismo va a explicar por qué un
atributo puede romper un método.

**Las cadenas no se modifican, se copian.** Todo método de cadena devuelve algo nuevo, así que hay
que guardarlo.

**`input` devuelve texto, siempre.** Convertir es tu responsabilidad, y olvidarlo es el `TypeError`
más común del curso.

El siguiente repaso son comparación, lógica y los dos tipos de ciclo.
"""),

md("""
---
# Soluciones

### Ejercicio 1

```python
alumnos_inscritos = 42
promedio_grupo = 8.73
esta_publicado = False
nombre_curso = "Programación Orientada a Objetos"
fecha_cierre = None

for nombre, valor in [("alumnos_inscritos", alumnos_inscritos),
                      ("promedio_grupo", promedio_grupo),
                      ("esta_publicado", esta_publicado),
                      ("nombre_curso", nombre_curso),
                      ("fecha_cierre", fecha_cierre)]:
    print(f"{nombre:<20} {str(valor):<34} {type(valor).__name__:<9} {bool(valor)}")
```

`esta_publicado` y `fecha_cierre` son los dos falsos, por razones distintas: uno porque vale
`False` y el otro porque vale `None`.

### Ejercicio 2

```python
matricula = 20240315
print("Es un número:", matricula, type(matricula).__name__)

matricula = "20240315"
print("Ahora es texto:", matricula, type(matricula).__name__)

try:
    print(matricula + 1)
except TypeError as e:
    print("TypeError:", e)
```

Una matrícula es justo el caso donde esto pasa de verdad: se lee de un archivo como texto, alguien
la convierte a número para compararla, y pierde los ceros de la izquierda.

### Ejercicio 3

```python
curso = "Programación Orientada a Objetos"

print("Primera palabra:", curso[:13])
print("Última palabra: ", curso[-7:])
print("Primeros diez:  ", curso[:10])
print("Últimos siete:  ", curso[-7:])
print("Al revés:       ", curso[::-1])
print("Sin cambios:    ", curso)
```

La primera palabra también se puede sacar con `curso.split()[0]`, que no depende de contar
caracteres. Esa versión sobrevive a que cambie el nombre del curso, y la de la rebanada no.

### Ejercicio 4

```python
texto = "  Python Programming  "

texto.strip()
texto.upper()
texto.replace("Python", "Java")
texto.lower()
texto.title()
print("Después de cinco métodos:", repr(texto))

limpio = texto.strip().upper()
print("Guardando el resultado:  ", repr(limpio))
```

Los cinco corrieron y ninguno cambió nada, porque nadie guardó lo que devolvieron. El encadenado
de la última línea funciona porque cada método devuelve una cadena nueva sobre la que se puede
llamar al siguiente.

### Ejercicio 5

```python
a, b = 17, 5

print(f"a + b  = {a + b}")
print(f"a - b  = {a - b}")
print(f"a * b  = {a * b}")
print(f"a / b  = {a / b}")
print(f"a // b = {a // b}")
print(f"a % b  = {a % b}")
print(f"a ** b = {a ** b}")
print()
print("a // b * b + a % b =", a // b * b + a % b, "· ¿es a?", a // b * b + a % b == a)
```

Esa identidad vale para cualquier par de enteros positivos, y es la razón por la que `//` y `%`
suelen aparecer juntos.

### Ejercicio 6

```python
for n in range(1, 21):
    par = "par" if n % 2 == 0 else "impar"
    cinco = "sí" if n % 5 == 0 else "no"
    print(f"{n:>3}  {par:<6} múltiplo de 5: {cinco}")
```

Sin un solo `if` anidado y sin listas auxiliares. El residuo contesta las dos preguntas.

### Ejercicio 7

```python
ENTRADAS = ["100", "250", "no capturado", "75", "300"]

validos = []
rechazados = []

for entrada in ENTRADAS:
    try:
        validos.append(int(entrada))
    except ValueError:
        rechazados.append(entrada)

print("Total:   ", sum(validos))
print("Promedio:", round(sum(validos) / len(validos), 2))
print("Sobre",  len(validos), "de", len(ENTRADAS), "entradas")
print("Rechazados:", rechazados)
```

El promedio se calcula sobre cuatro, no sobre cinco, y el programa lo dice. Reportar 145 sin
mencionar que una entrada se descartó es lo que vuelve indefendible un número correcto.

### Ejercicio 8

```python
nombre = input("¿Cómo te llamas? ")
edad = int(input("¿Cuántos años tienes? "))

anio_actual = 2026
print(f"Hola {nombre}, cumpliste {edad} en {anio_actual - 0}")
print(f"O sea que naciste alrededor de {anio_actual - edad}")
```

El detalle que casi todos fallan: `int()` va envolviendo al `input`, no al resultado de la resta.
Sin eso, `anio_actual - edad` lanza `TypeError` porque `edad` sigue siendo texto.
"""),

]

write(OUT / "es" / "w01.1.ipynb", es)
print("wrote", OUT / "es" / "w01.1.ipynb")
