"""notebooks/programacion-orientada-a-objetos/es/w01.5.ipynb

Source deck: ppts/python/programacion-orientada-a-objetos/es/w01.5.es.yaml
Source code:  docs/en/courses/python-course/01 - Basics/5th Module/Code028.py

Code028.py pide input siete veces y no corre headless. El cuaderno reproduce sus
bloques con valores asignados y deja una sola celda con input de verdad.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from nbkit import md, code, write, REPO

OUT = REPO / "notebooks" / "programacion-orientada-a-objetos"

es = [

md("""
# Programación Orientada a Objetos · Repaso 5 de 5
## Módulo 5 · Errores

**COM102 · Facultad de Ingeniería · Profesor David Escobar-Castillejos**

Leer un traceback, atrapar el error que esperabas y dejar pasar el que no.

Los cuatro repasos anteriores dejaron errores tirados por el camino: el `TypeError` de la anotación
mentida, el `ValueError` del desempaque, el `IndexError` de la lista corta, el `KeyError` de la beca
que no existe. Todos se atraparon con `try` para que el cuaderno siguiera corriendo, y hasta ahora
nadie explicó cómo funciona eso. Este cuaderno lo explica.

Al terminar vas a poder:

1. Leer un traceback de abajo hacia arriba y decir en qué línea empezó el problema.
2. Nombrar los siete errores que más vas a ver, y qué los provoca.
3. Escribir un `except` por tipo, y explicar qué esconde un `except` a secas.
4. Usar `else` y `finally`, y decir exactamente cuándo corre cada uno.
5. Decidir entre un `if` y un `try` con una sola pregunta.

### Cómo se usa este cuaderno

Ejecuta las celdas en orden con **Shift + Enter**. Este es el cuaderno donde casi todo falla a
propósito, así que la marca cambia de sentido: aquí lo que se señala es **el error que se cuela sin
que nadie lo note**.

Hay una sola celda que espera a que escribas algo. Está marcada y no bloquea un "Ejecutar todo".
"""),

md("""
---
# Bloque 1 · Leer el error

Python ya te dijo qué pasó y en qué línea. El problema casi nunca es el mensaje, es no leerlo.

La celda de abajo provoca un error de verdad y lo imprime completo, con `traceback.print_exc()`. Es
el mismo texto que verías si el programa se hubiera detenido, solo que aquí no se detiene.
"""),

code("""
import traceback


def dividir(a, b):
    return a / b


try:
    print(dividir(10, 0))
except ZeroDivisionError:
    traceback.print_exc()
"""),

md("""
Se lee **de abajo hacia arriba**, y ese es el único truco.

| Renglón | Qué te dice |
|---|---|
| El último | El tipo de error y el mensaje. Aquí empieza siempre. |
| El de arriba | El archivo, la línea y la función donde ocurrió |
| Los de más arriba | El camino que siguió el programa hasta llegar ahí |
| El primero | La llamada original, la que escribiste tú |

Con el tipo y la línea ya tienes casi todo. El resto del camino solo hace falta cuando el error viene
de una función lejana, y ahí sí vale su peso en oro.
"""),

code("""
def nivel_3(x):
    return 10 / x


def nivel_2(x):
    return nivel_3(x)


def nivel_1(x):
    return nivel_2(x)


try:
    nivel_1(0)
except ZeroDivisionError:
    traceback.print_exc()
"""),

md("""
Cuatro renglones de camino, y cada uno con su número de línea.

El de hasta abajo dice dónde reventó: en `nivel_3`, en la división. El de hasta arriba dice quién
empezó todo: la llamada `nivel_1(0)`. La corrección casi nunca va en el renglón de abajo, porque la
división está bien escrita. Va arriba, donde alguien pasó un cero.

Ese es el valor real del camino completo: **el error ocurre abajo y la culpa está arriba**.

## Los siete errores del semestre
"""),

code("""
ejemplos = [
    ("'5' + 1", lambda: '5' + 1),
    ("int('hola')", lambda: int("hola")),
    ("print(totl)", lambda: totl),                  # noqa: F821
    ("[1, 2][5]", lambda: [1, 2][5]),
    ("{'a': 1}['b']", lambda: {"a": 1}["b"]),
    ("10 / 0", lambda: 10 / 0),
    ("(1, 2).append(3)", lambda: (1, 2).append(3)),
]

for texto, disparar in ejemplos:
    try:
        disparar()
        print(f"{texto:<18}no falló")
    except Exception as e:
        print(f"{texto:<18}{type(e).__name__:<20}{e}")
"""),

md("""
Vale la pena leer los mensajes con calma, porque están redactados para decirte qué hacer.

`invalid literal for int() with base 10: 'hola'` te dice el valor exacto que no pudo convertir, que
es lo primero que ibas a preguntar. `can only concatenate str (not "int") to str` te dice cuál de los
dos operandos está bien y cuál sobra.

Dos parejas que se confunden seguido:

**`TypeError` contra `ValueError`.** El tipo está mal contra el valor está mal. `int([1, 2])` es
`TypeError` porque una lista no se convierte a entero de ninguna forma. `int("hola")` es `ValueError`
porque una cadena sí se convierte, solo que esa en particular no.

**`NameError` contra `AttributeError`.** El nombre no existe contra el objeto no tiene ese pedazo.
`totl` es un nombre que nadie definió; `append` sí existe en el mundo, pero no en una tupla, como
viste en el repaso 4.

## Los errores tienen familias
"""),

code("""
for excepcion in (ZeroDivisionError, ValueError, IndexError, KeyError,
                  TypeError, AttributeError, NameError):
    cadena, actual = [], excepcion
    while actual is not object:
        cadena.append(actual.__name__)
        actual = actual.__bases__[0]
    print(" <- ".join(cadena))
"""),

md("""
`IndexError` y `KeyError` son los dos hijos de `LookupError`, que es "buscaste algo y no estaba".
`ZeroDivisionError` cuelga de `ArithmeticError`. Y las siete terminan en `Exception`.

Eso no es trivia. Un `except` atrapa el tipo que nombres **y todos sus descendientes**, así que
`except LookupError` atrapa los dos casos de búsqueda fallida de un golpe, y `except Exception`
atrapa las siete. Esa herencia es la misma que vas a construir tú en la semana 7, con clases propias
en vez de excepciones.
"""),

code("""
def buscar(coleccion, donde):
    try:
        return coleccion[donde]
    except LookupError as e:
        return f"{type(e).__name__} atrapado por except LookupError"


print(buscar([1, 2, 3], 5))
print(buscar({"a": 1}, "b"))
print(buscar([1, 2, 3], 1), "<- este sí existe")
"""),

md("""
---
# Bloque 2 · Atrapar el error

`try` no arregla nada por sí solo. Decide qué pasa cuando algo falla.

La estructura completa tiene cuatro cláusulas y solo la primera es obligatoria.

| Cláusula | Cuándo corre | ¿Obligatoria? |
|---|---|---|
| `try` | Siempre. Es lo que se vigila. | Sí |
| `except` | Solo si ocurre ese tipo de error | Al menos uno, o un `finally` |
| `else` | Solo si el `try` terminó sin error | No |
| `finally` | Siempre, haya fallado o no | No |
"""),

code("""
def calcular_factor(edad_texto):
    \"\"\"La versión del Code028.py del curso, con el input ya resuelto.\"\"\"
    try:
        edad = int(edad_texto)
        factor = 10 / edad
    except ValueError:
        print("  Eso no es un número")
    except ZeroDivisionError:
        print("  La edad no puede ser 0")
    else:
        print("  Factor:", factor)
    finally:
        print("  Terminé de intentarlo")


for entrada in ["20", "cero", "0"]:
    print(f"Con {entrada!r}:")
    calcular_factor(entrada)
    print()
"""),

md("""
Tres entradas, tres caminos, y `finally` en las tres.

Con `"20"` no hubo excepción, así que corrió el `else` y no corrió ningún `except`. Con `"cero"` el
`int` lanzó `ValueError` antes de llegar a la división. Con `"0"` la conversión pasó sin problema y la
división fue la que reventó.

Ese orden importa. El `try` se abandona en la primera línea que falla, así que las líneas de abajo
nunca corren. Por eso `factor` no existe cuando hay excepción, y por eso imprimirlo tiene que ir en
el `else` y no al final del `try`.

## Por qué el `else` y no el final del `try`
"""),

code("""
# La versión sin else: el print queda dentro del bloque vigilado.
def sin_else(edad_texto):
    try:
        edad = int(edad_texto)
        factor = 10 / edad
        print("  Factor:", factor["mal"])     # error de dedo a propósito
    except ValueError:
        print("  Eso no es un número")
    except TypeError:
        print("  Eso no es un número")        # el mismo mensaje, mintiendo


sin_else("20")
"""),

md("""
El programa dice "Eso no es un número" y el `20` era perfectamente un número.

El `print` con el error de dedo estaba dentro del `try`, así que su `TypeError` cayó en un `except`
que hablaba de otra cosa. Con el `print` en el `else`, ese error habría salido a la superficie con su
traceback y su número de línea.

**El `try` envuelve lo mínimo que puede fallar.** Dos o tres líneas adentro, y el `except` sabe
exactamente de qué está hablando.

## `finally` corre pase lo que pase
"""),

code("""
def con_finally(x, y):
    try:
        resultado = x / y
        return f"resultado {resultado}"
    except ZeroDivisionError:
        return "división por cero"
    finally:
        print("  finally corrió")


print(con_finally(10, 5))
print(con_finally(10, 0))
"""),

md("""
El `finally` se imprimió **antes** que el valor devuelto, en los dos casos. No es que corra después
del `return`: corre entre el `return` y la entrega, porque Python guarda el valor, ejecuta el
`finally` y hasta entonces sale de la función.

Ahí está su razón de ser. Lo que se abre hay que cerrarlo, falle o no falle: un archivo, una conexión
a base de datos, un cursor. En la semana 12 vas a ver que Python trae algo mejor para eso, el bloque
`with`, y `finally` es lo que hay por debajo.

## Predice antes de correr

¿Qué imprime este programa?

```python
try:
    numeros = [1, 2, 3]
    print(numeros[5])
except ValueError:
    print("valor")
except IndexError:
    print("indice")
finally:
    print("fin")
```

- **A.** `valor`, y luego `fin`.
- **B.** `indice`, y luego `fin`.
- **C.** Solo `fin`, porque ningún `except` aplica.
- **D.** El programa truena antes de llegar a `finally`.
"""),

code("""
try:
    numeros = [1, 2, 3]
    print(numeros[5])
except ValueError:
    print("valor")
except IndexError:
    print("indice")
finally:
    print("fin")
"""),

md("""
La respuesta es **B**.

| Paso | Qué pasa | Resultado |
|---|---|---|
| 1 | `numeros[5]` en una lista de 3 | levanta `IndexError` |
| 2 | `except ValueError` | no coincide, se salta |
| 3 | `except IndexError` | coincide, imprime `indice` |
| 4 | `finally` | corre siempre, imprime `fin` |

Los `except` se revisan **en orden** y solo entra el primero que coincide. Ese detalle del orden
tiene una consecuencia que muerde.
"""),

code("""
# FALLA A PROPÓSITO, y no truena. El segundo except no se alcanza nunca.
try:
    10 / 0
except Exception:
    print("entró aquí, en el genérico")
except ZeroDivisionError:
    print("y este renglón nunca se alcanza")
"""),

md("""
`ZeroDivisionError` desciende de `Exception`, así que el primer `except` ya coincidía y el segundo
quedó muerto. Python no se queja: no hay error de sintaxis ni advertencia.

Es exactamente el mismo problema que el orden de FizzBuzz en el repaso 3. La rama más general escrita
primero deja inalcanzables a todas las que vienen después. **Del más específico al más general,
siempre.**

## El `except` a secas, y por qué el deck lo marca como riesgo
"""),

code("""
# FALLA A PROPÓSITO, y no truena. El mensaje miente sobre lo que pasó.
notas = [8, 9, 10]

try:
    total = sum(notas)
    promedio = total / len(nota)      # error de dedo: nota, no notas
    print("Promedio:", promedio)
except:
    print("No se pudieron leer las calificaciones")
"""),

md("""
Las calificaciones se leyeron perfectamente. Lo que falló fue un nombre mal escrito, `nota` en lugar
de `notas`, y el `except` a secas lo convirtió en un mensaje sobre lectura de datos.

Un `NameError` es un error tuyo, de los que se arreglan en cinco segundos si te enteras. Ese `except`
lo enterró. Multiplicado por un programa de mil líneas, es la diferencia entre una tarde y una
semana.
"""),

code("""
# La misma celda con el tipo nombrado.
try:
    total = sum(notas)
    promedio = total / len(nota)      # el mismo error de dedo
    print("Promedio:", promedio)
except ZeroDivisionError:
    print("No hay calificaciones que promediar")
except NameError as e:
    print("Sale a la superficie:", type(e).__name__ + ":", e)
"""),

md("""
Ahora el mensaje dice la verdad y hasta el nombre de la variable.

En un programa de verdad ni siquiera pondrías ese segundo `except`: dejarías que el `NameError` se
propague con su traceback completo, que es justo lo que quieres ver.

## El `except` a secas atrapa más de lo que crees
"""),

code("""
# FALLA A PROPÓSITO, y no truena. Un except a secas atrapa hasta la salida del programa.
try:
    raise SystemExit(3)
except Exception as e:
    print("except Exception atrapó:", type(e).__name__)
except BaseException as e:
    print("solo BaseException lo atrapa:", type(e).__name__)
"""),

md("""
`SystemExit` no desciende de `Exception`, sino directamente de `BaseException`. Lo mismo pasa con
`KeyboardInterrupt`, el que se dispara con Control C.

Un `except:` a secas equivale a `except BaseException:`, así que se traga las dos. Un programa con un
ciclo así de protegido **no se puede detener con Control C**, y en Colab eso significa reiniciar el
entorno de ejecución.

Si de plano necesitas atrapar todo, escribe `except Exception`. Deja a `BaseException` en paz.
"""),

md("""
## El error más caro: atrapar y no hacer nada
"""),

code("""
# FALLA A PROPÓSITO, y no truena. El pass se come las entradas malas y el reporte miente.
ENTRADAS = ["8", "9", "diez", "7", ""]

validas = []
for entrada in ENTRADAS:
    try:
        validas.append(int(entrada))
    except Exception:
        pass

print("Promedio del grupo:", sum(validas) / len(validas))
print("Entradas capturadas:", len(ENTRADAS))
"""),

md("""
El promedio salió 8.0 y se calculó sobre tres de cinco. El reporte dice "promedio del grupo" y no es
del grupo.

`except Exception: pass` es la forma más rápida de que un programa deje de tronar y siga estando mal.
Nada avisa, y el número que sale es del tamaño correcto y del orden de magnitud correcto.

La versión honesta no cuesta más líneas.
"""),

code("""
validas, rechazadas = [], []
for entrada in ENTRADAS:
    try:
        validas.append(int(entrada))
    except ValueError:
        rechazadas.append(entrada)

print(f"Promedio: {sum(validas) / len(validas):.2f}")
print(f"Calculado sobre {len(validas)} de {len(ENTRADAS)} entradas")
print("Rechazadas:", rechazadas)
"""),

md("""
El promedio es el mismo. Lo que cambió es que ahora el reporte dice sobre cuántas entradas se calculó
y cuáles se fueron, y quien lo lea puede decidir si eso le sirve.

Esa distinción entre el resultado y su cobertura es la misma del repaso 3 con `None` contra cero, y
es lo que separa un número correcto de un número defendible.
"""),

md("""
## La celda que espera por ti
"""),

code("""
# ESTA CELDA ESPERA POR TI. En Colab abre un cuadro de texto arriba.
# El try de afuera es para que un "Ejecutar todo" sin teclado no se quede colgado.
try:
    texto = input("Escribe tu edad: ")
except Exception:
    texto = "cero"
    print("(sin teclado disponible, se usa 'cero' para ver el camino del error)")

try:
    edad = int(texto)
except ValueError as e:
    print("ValueError:", e)
    print("Lo que llegó fue", repr(texto), "y int() no sabe qué hacer con eso.")
else:
    print("Edad convertida:", edad, type(edad).__name__)
finally:
    print("La celda terminó, con edad o sin ella.")
"""),

md("""
`input` siempre devuelve texto, como viste en el repaso 1. Por eso la conversión es el único renglón
que de verdad puede fallar, y por eso es el único que va dentro del `try`.

La rúbrica de la tarea de esta semana pide exactamente eso en el criterio de "Alcance del try": el
`try` envuelve la conversión, no el programa entero.
"""),

md("""
---
# Bloque 3 · Cuándo no usar `try`

Envolver todo en un `try` no hace robusto a un programa. Lo hace mudo.

La regla se decide con una pregunta: **¿lo puedo comprobar con un `if` antes de intentarlo?**

Si la respuesta es sí, va un `if`. Si depende de algo que no controlas, va un `try`.

| Situación | Va con |
|---|---|
| La lista puede estar vacía | `if` |
| El divisor puede ser cero | `if` |
| La llave puede no estar | `if` con `in`, o `get` |
| El usuario escribe cualquier cosa | `try` |
| El archivo puede no existir | `try` |
| La red se puede caer | `try` |

Las tres de arriba las puedes revisar tú mismo con los datos que ya tienes en la mano. Las tres de
abajo dependen del mundo, y entre revisar y usar puede cambiar.
"""),

code("""
def promedio_con_if(notas):
    if not notas:
        return None
    return sum(notas) / len(notas)


def promedio_con_try(notas):
    try:
        return sum(notas) / len(notas)
    except ZeroDivisionError:
        return None


for grupo in [[8, 9, 10], []]:
    print(f"{str(grupo):<12} if: {promedio_con_if(grupo)}  "
          f"try: {promedio_con_try(grupo)}")
"""),

md("""
Las dos dan el mismo resultado, y la del `if` se lee mejor porque dice la condición con sus palabras:
"si no hay notas". La del `try` obliga a reconstruir mentalmente que una lista vacía hace que `len`
sea cero y que eso provoca la división.

## Cuánto cuesta una excepción

`Code028.py` mide esto con `timeit` y llega a una conclusión razonable. Vale la pena medirlo otra vez,
porque la conclusión completa es más interesante que la del archivo.
"""),

code("""
import timeit

CON_RAISE = '''
def factor(edad):
    if edad <= 0:
        raise ValueError("La edad no puede ser 0 o menos.")
    return 10 / edad

try:
    factor(-1)
except ValueError:
    pass
'''

CON_IF = '''
def factor(edad):
    if edad <= 0:
        return None
    return 10 / edad

if factor(-1) is None:
    pass
'''

t_raise = timeit.timeit(CON_RAISE, number=10000)
t_if = timeit.timeit(CON_IF, number=10000)

print("Cuando el error SÍ ocurre, 10,000 veces:")
print(f"  con raise/except: {t_raise * 1000:7.1f} ms")
print(f"  con if/None:      {t_if * 1000:7.1f} ms")
print(f"  la excepción costó {t_raise / t_if:.1f} veces más")
"""),

code("""
FELIZ_TRY = '''
d = {"a": 1}
try:
    x = d["a"]
except KeyError:
    x = None
'''

FELIZ_IF = '''
d = {"a": 1}
if "a" in d:
    x = d["a"]
else:
    x = None
'''

t_try = timeit.timeit(FELIZ_TRY, number=200000)
t_if2 = timeit.timeit(FELIZ_IF, number=200000)

print("Cuando el error NO ocurre, 200,000 veces:")
print(f"  con try/except: {t_try * 1000:7.1f} ms")
print(f"  con if:         {t_if2 * 1000:7.1f} ms")
"""),

md("""
Las dos celdas dicen cosas distintas y las dos son ciertas.

**Levantar una excepción cuesta.** Construir el objeto, armar el traceback y desenrollar la pila es
trabajo real, y con el error ocurriendo cada vez el `raise` sale varias veces más caro.

**Entrar a un `try` que no falla no cuesta.** El `try` en el camino feliz sale igual o más rápido que
el `if`, porque el `if` evalúa una condición en cada vuelta y el `try` no evalúa nada mientras no
haya excepción.

Los números exactos cambian con la máquina, y la conclusión no: las excepciones son caras cuando
ocurren seguido, y gratis cuando son la excepción. De ahí el nombre.

El criterio no es de velocidad, de todos modos. Es de legibilidad, y en ese terreno gana el `if` para
lo previsible y el `try` para lo que viene de afuera.

## Levantar tus propias excepciones
"""),

code("""
def calcular_factor(edad):
    if edad <= 0:
        raise ValueError("La edad no puede ser 0 o menos.")
    return 10 / edad


try:
    calcular_factor(-1)
except ValueError as error:
    print("ValueError:", error)

print("Con una edad válida:", calcular_factor(25))
"""),

md("""
`raise` levanta una excepción a propósito, con el mensaje que tú escribas.

Sirve cuando una función detecta que sus argumentos no tienen sentido y no le toca a ella decidir qué
hacer al respecto. `calcular_factor` sabe que una edad negativa está mal, pero no sabe si el programa
debe pedirle otra al usuario, escribirlo en la bitácora o abortar. Levanta la excepción y quien la
llamó decide.

Devolver `None` también es una opción, y la diferencia está en si ignorar el problema es fácil. El
`None` se puede ignorar; la excepción no. Cuando el dato malo tiene que detener el proceso, `raise`.

En la semana 11 esto se retoma en serio, con excepciones propias que heredan de `Exception` y con
validación en la frontera del programa.
"""),

md("""
---
## Cuatro errores de este módulo

**`except` a secas.** Atrapa todo, incluidos tus errores de dedo, y los convierte en un mensaje que
miente. También atrapa `KeyboardInterrupt`, así que el programa deja de responder a Control C.

**Un `try` de treinta líneas.** Cuando salta, nadie sabe cuál de las treinta falló. Envuelve solo lo
que puede tronar y saca lo demás al `else`.

**Atrapar y no hacer nada.** Un `except` con solo `pass` esconde el problema y lo deja para después,
normalmente para cuando el número ya se reportó.

**Usar `try` donde bastaba un `if`.** Comprobar que la lista no está vacía es un `if`. Que el archivo
exista, un `try`.

Los cuatro corrieron arriba, y ninguno lanzó nada.
"""),

md("""
---
# Ejercicios

Las soluciones están hasta abajo del cuaderno.

### Ejercicio 1 · Leer el traceback

Escribe tres funciones encadenadas donde la última convierta a entero un texto que no lo es. Llama a
la primera dentro de un `try` e imprime el traceback completo con `traceback.print_exc()`.

Di en un comentario qué línea tiene el error y qué línea tiene la culpa.

### Ejercicio 2 · Los siete errores

Escribe una expresión que dispare cada uno de los siete errores de la tabla, y atrápalas todas en un
ciclo que imprima el tipo y el mensaje. No repitas ninguno.

### Ejercicio 3 · Del más específico al más general

Escribe un bloque con tres `except`: `ZeroDivisionError`, `ArithmeticError` y `Exception`, en ese
orden. Compruébalo con una división entre cero.

Después invierte el orden y demuestra que ahora entra otro. Explica en un comentario por qué Python
no marca ningún error en la versión invertida.

### Ejercicio 4 · El mensaje que miente

Escribe un bloque con un `except` a secas donde el error real sea un `NameError` por un nombre mal
escrito. Imprime un mensaje que hable de otra cosa.

Después arréglalo nombrando el tipo, y muestra el mensaje verdadero.

### Ejercicio 5 · `else` y `finally`

Escribe una función `dividir_reportando(a, b)` con las cuatro cláusulas. Que el `try` tenga solo la
división, el `else` imprima el resultado y el `finally` imprima una línea de cierre.

Llámala con `(10, 2)`, `(10, 0)` y `(10, "x")`. Explica en un comentario cuántas veces corrió el
`finally`.

### Ejercicio 6 · `if` o `try`

Para cada una de estas seis situaciones, escribe la solución con `if` o con `try`, la que
corresponda, y di en un comentario por qué:

1. Sacar el primer elemento de una lista que puede estar vacía.
2. Convertir a entero lo que escribió el usuario.
3. Dividir entre una variable que puede valer cero.
4. Leer la llave `"beca"` de un diccionario de alumno.
5. Abrir un archivo cuyo nombre te dieron por consola.
6. Sacar la raíz cuadrada de un número que puede ser negativo.

### Ejercicio 7 · El promedio honesto

Toma la lista `["8", "9", "diez", "7", "", "10"]` y calcula el promedio de las entradas que sí son
números. Reporta el promedio, sobre cuántas entradas se calculó, y cuáles se rechazaron.

Hazlo primero con `except Exception: pass` y muestra qué reporta. Después con el tipo nombrado y la
lista de rechazos.

### Ejercicio 8 · Tu propia excepción

Escribe `retirar(saldo, monto)` que levante `ValueError` con un mensaje distinto según si el monto es
negativo o si excede el saldo, y que devuelva el saldo nuevo cuando todo esté bien.

Pruébala con tres casos y atrapa el error imprimiendo el mensaje.

### Ejercicio 9 · La tarea

Escribe un programa que pida cinco calificaciones, calcule el promedio con una función y no truene
con nada de lo que el usuario escriba.

El promedio se calcula en una función con parámetro y retorno. El `try` envuelve solo la conversión,
no el programa entero. Cada `except` nombra su tipo. Y el reporte final dice sobre cuántas de las
cinco se calculó.
"""),

md("""
---
## Tres ideas para llevarse

**El traceback se lee de abajo hacia arriba.** La última línea dice qué pasó, la de arriba dice
dónde, y el camino completo dice quién lo provocó. El error ocurre abajo y la culpa suele estar
arriba.

**Nombrar la excepción es lo que ayuda.** Un `except` a secas convierte un error tuyo en un mensaje
que miente, y de paso se traga el Control C. Del más específico al más general, siempre.

**Si lo puedes comprobar con un `if`, no uses `try`.** `try` es para lo que viene de afuera y no
puedes prever: el teclado, un archivo, una conexión.

Con esto se cierra el repaso de los cinco módulos. La semana 2 no trae código nuevo: trae la pregunta
de por qué existe la programación orientada a objetos y qué problema vino a resolver. Todo lo que
repasaste en estos cinco cuadernos es el material con el que ese problema se explica, y de la semana
3 en adelante empieza a tener nombre propio.
"""),

md("""
---
# Soluciones

### Ejercicio 1

```python
import traceback


def convertir(texto):
    return int(texto)


def procesar(texto):
    return convertir(texto)


def principal(texto):
    return procesar(texto)


try:
    principal("veinte")
except ValueError:
    traceback.print_exc()

# El error está en convertir, en la línea del int(). La culpa está en la llamada
# principal("veinte"), hasta arriba, porque convertir hace bien su trabajo: le
# entregaron un texto que no es un número. La corrección va donde nace el dato.
```

### Ejercicio 2

```python
casos = [
    ("TypeError", lambda: "5" + 1),
    ("ValueError", lambda: int("hola")),
    ("NameError", lambda: variable_que_no_existe),   # noqa: F821
    ("IndexError", lambda: [1, 2][5]),
    ("KeyError", lambda: {"a": 1}["b"]),
    ("ZeroDivisionError", lambda: 10 / 0),
    ("AttributeError", lambda: (1, 2).append(3)),
]

for esperado, disparar in casos:
    try:
        disparar()
        print(f"{esperado:<20}no falló")
    except Exception as e:
        marca = "ok" if type(e).__name__ == esperado else "OTRO"
        print(f"{esperado:<20}{type(e).__name__:<20}{marca}  {e}")
```

La columna de la derecha comprueba que cada expresión disparó el error que se esperaba, en vez de
darlo por hecho.

### Ejercicio 3

```python
print("Del específico al general:")
try:
    10 / 0
except ZeroDivisionError:
    print("  ZeroDivisionError")
except ArithmeticError:
    print("  ArithmeticError")
except Exception:
    print("  Exception")

print("Al revés:")
try:
    10 / 0
except Exception:
    print("  Exception")
except ArithmeticError:
    print("  ArithmeticError")
except ZeroDivisionError:
    print("  ZeroDivisionError")

# Python no marca nada porque un except con un tipo general es sintaxis
# perfectamente válida: nadie puede saber al leer el archivo qué excepciones va
# a levantar el try. Solo al ejecutar se descubre que los dos de abajo nunca
# entran, y para descubrirlo hace falta que alguien note que su mensaje jamás
# aparece.
```

### Ejercicio 4

```python
datos = [1, 2, 3]

try:
    total = sum(dato)          # error de dedo: dato, no datos
    print(total)
except:
    print("No se pudo leer el archivo de datos")

try:
    total = sum(dato)
    print(total)
except NameError as e:
    print("NameError:", e)
```

El primer mensaje habla de un archivo que nunca se abrió. El segundo dice el nombre exacto que falta,
que es lo que necesitas para arreglarlo.

### Ejercicio 5

```python
def dividir_reportando(a, b):
    try:
        resultado = a / b
    except ZeroDivisionError:
        print("  no se puede dividir entre cero")
    except TypeError as e:
        print("  tipos incompatibles:", e)
    else:
        print("  resultado:", resultado)
    finally:
        print("  ---")


for a, b in [(10, 2), (10, 0), (10, "x")]:
    print(f"dividir_reportando({a}, {b!r}):")
    dividir_reportando(a, b)

# El finally corrió tres veces, una por llamada. No le importa si hubo
# excepción, si se atrapó ni cuál se atrapó.
```

### Ejercicio 6

```python
lista, texto, divisor = [], "42", 0
alumno = {"nombre": "Ana"}

# 1. if. La lista la tengo aquí y puedo preguntarle su longitud.
print(lista[0] if lista else "lista vacía")

# 2. try. Lo escribió una persona y puede ser cualquier cosa.
try:
    print(int(texto))
except ValueError:
    print("no es un número")

# 3. if. El valor del divisor está en mis manos antes de dividir.
print(10 / divisor if divisor != 0 else "divisor en cero")

# 4. if con get. La llave está o no está, y lo puedo consultar.
print(alumno.get("beca", "sin beca"))

# 5. try. Entre comprobar que existe y abrirlo, el archivo puede desaparecer.
try:
    with open("no_existe.txt") as f:
        print(f.read())
except FileNotFoundError as e:
    print("FileNotFoundError:", e.filename)

# 6. if. El signo del número se revisa con una comparación.
numero = -9
print(numero ** 0.5 if numero >= 0 else "raíz de un negativo")
```

El quinto es el más interesante. Preguntar si el archivo existe y después abrirlo deja una rendija
entre las dos líneas donde otro programa lo puede borrar. Por eso los archivos van con `try` aunque
parezca que se pueden comprobar antes.

### Ejercicio 7

```python
ENTRADAS = ["8", "9", "diez", "7", "", "10"]

# La versión que esconde.
validas = []
for entrada in ENTRADAS:
    try:
        validas.append(int(entrada))
    except Exception:
        pass
print("Con pass -> promedio", sum(validas) / len(validas))

# La versión que reporta.
validas, rechazadas = [], []
for entrada in ENTRADAS:
    try:
        validas.append(int(entrada))
    except ValueError:
        rechazadas.append(entrada)

print(f"Promedio: {sum(validas) / len(validas):.2f}")
print(f"Sobre {len(validas)} de {len(ENTRADAS)} entradas")
print("Rechazadas:", rechazadas)
```

Las dos imprimen el mismo promedio. Solo una dice que dos de las seis entradas no entraron en la
cuenta.

### Ejercicio 8

```python
def retirar(saldo, monto):
    if monto <= 0:
        raise ValueError(f"El monto tiene que ser positivo, llegó {monto}")
    if monto > saldo:
        raise ValueError(f"Saldo insuficiente: hay {saldo} y se piden {monto}")
    return saldo - monto


for monto in [500, -100, 5000]:
    try:
        print(f"Retirar {monto}: queda {retirar(1000, monto)}")
    except ValueError as e:
        print(f"Retirar {monto}: ValueError: {e}")
```

Los dos mensajes traen los números del caso concreto. Un mensaje que dice solo "monto inválido"
obliga a ir a leer el código para saber cuál de las dos reglas se rompió.

### Ejercicio 9

```python
ENTRADAS = ["8", "nueve", "10", "", "7"]     # simula lo que se teclea


def calcular_promedio(calificaciones):
    if not calificaciones:
        return None
    return sum(calificaciones) / len(calificaciones)


validas, rechazadas = [], []
for entrada in ENTRADAS:
    try:
        validas.append(float(entrada))
    except ValueError:
        rechazadas.append(entrada)

promedio = calcular_promedio(validas)

if promedio is None:
    print("No se capturó ninguna calificación válida.")
else:
    print(f"Promedio: {promedio:.2f}")
    print(f"Calculado sobre {len(validas)} de {len(ENTRADAS)} calificaciones")

if rechazadas:
    print("Se rechazaron:", rechazadas)
```

Las tres cosas de la rúbrica están separadas a propósito. El `try` envuelve una sola línea, la
conversión. El promedio vive en una función que recibe y devuelve, sin imprimir nada. Y el `except`
nombra `ValueError`, que es lo único que `float` puede lanzar con un texto.

Con `input` de verdad, la única línea que cambia es la que llena `ENTRADAS`:

```python
ENTRADAS = [input(f"Calificación {i + 1}: ") for i in range(5)]
```

El resto del programa no se entera de dónde vinieron los datos, y eso es justamente lo que permite
probarlo sin teclado.
"""),

]

write(OUT / "es" / "w01.5.ipynb", es)
print("wrote", OUT / "es" / "w01.5.ipynb")
