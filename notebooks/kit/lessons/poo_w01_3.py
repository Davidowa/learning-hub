"""notebooks/programacion-orientada-a-objetos/es/w01.3.ipynb

Source deck: ppts/python/programacion-orientada-a-objetos/es/w01.3.es.yaml
Source code:  docs/en/courses/python-course/01 - Basics/3rd Module/
              Code010.py, Code011.py, Exercise002.py
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from nbkit import md, code, write, REPO

OUT = REPO / "notebooks" / "programacion-orientada-a-objetos"

es = [

md("""
# Programación Orientada a Objetos · Repaso 3 de 5
## Módulo 3 · Funciones

**COM102 · Facultad de Ingeniería · Profesor David Escobar-Castillejos**

Darle nombre a un pedazo de trabajo. Parámetros, retorno y dónde vive cada variable.

Este es el repaso que más pesa de los cinco. En tres semanas vas a escribir tu primera clase, y una
clase no es más que funciones que viven juntas y comparten datos. Todo lo que aquí se llama función,
parámetro y alcance ahí se va a llamar método, argumento y `self`, y va a funcionar igual.

Al terminar este cuaderno vas a poder:

1. Definir una función con `def` y distinguir definirla de llamarla.
2. Separar parámetro de argumento, y usar valores por defecto sin caer en la trampa de la lista.
3. Devolver un valor con `return`, y explicar qué entrega una función que no lo escribe.
4. Explicar el alcance de una variable, y por qué `NameError` y `UnboundLocalError` aparecen justo
   donde aparecen.
5. Escribir FizzBuzz completo y decir por qué el orden de sus condiciones no es negociable.

### Cómo se usa este cuaderno

Ejecuta las celdas en orden con **Shift + Enter**. Diez fallan a propósito y llevan un comentario
que lo dice.

Fíjate en cuáles de esas diez **no lanzan ningún error**. Son las peligrosas: el programa sigue
corriendo, entrega un resultado creíble, y está mal.
"""),

md("""
---
# Bloque 1 · Definir y llamar

Una función es un bloque de código con nombre que solo corre cuando alguien lo llama.

Sirve para tres cosas, y vale la pena tenerlas separadas en la cabeza. Para no repetir, porque el
código se escribe una vez y se usa muchas. Para poder probar una parte sin correr todo el programa.
Y para que lo que escribiste se lea como una lista de intenciones en lugar de un muro de
instrucciones.

**La regla del nombre: un verbo y un sustantivo.** `calcular_promedio`, `leer_archivo`, `es_par`.
Si no puedes nombrarla así, probablemente hace más de una cosa y conviene partirla.
"""),

code("""
def saludar():
    print("Hola desde una función")


saludar()                      # Hola desde una función


def saludar_a(nombre):
    print(f"Hola, {nombre}")


saludar_a("Ana")               # Hola, Ana
saludar_a("Beto")              # la misma función, otro argumento
"""),

md("""
Los dos puntos y la sangría son los que dicen qué pertenece a la función. Todo lo que está indentado
bajo el `def` es su cuerpo, y la primera línea que vuelve al margen ya está afuera.

## Definir no es llamar

El `def` solo crea la función y la guarda con ese nombre. Nada del cuerpo se ejecuta hasta que
alguien la llama.
"""),

code("""
# FALLA A PROPÓSITO, y esta es de las que no truenan.
def calcular_impuesto(monto):
    print(f"Impuesto: {monto * 0.16:.2f}")


print("El programa terminó sin imprimir ningún impuesto.")
"""),

md("""
Ni un error, ni una advertencia, ni una línea de salida. Python leyó el `def`, guardó la función y
siguió adelante.

Ese silencio es el problema. Un script que define veinte funciones y llama a dieciocho corre limpio
y entrega dos cosas de menos.
"""),

code("""
calcular_impuesto(1500)        # ahora sí corre el cuerpo
"""),

code("""
# FALLA A PROPÓSITO, y tampoco truena. Sin paréntesis no es una llamada.
print(calcular_impuesto)
print(type(calcular_impuesto))
print()
print("¿Es lo mismo que llamarla?", calcular_impuesto is calcular_impuesto)
"""),

md("""
Sin paréntesis, el nombre es solo el nombre. Python imprime la referencia a la función, con su
dirección en memoria, y no ejecuta nada.

Eso importa más de lo que parece: **una función es un valor** como un número o una cadena. Se puede
guardar en una variable, meter en una lista y pasar como argumento a otra función. Ahí es donde el
paréntesis deja de ser un adorno y se vuelve la diferencia entre entregar la receta y entregar el
platillo.
"""),

code("""
otra_forma = calcular_impuesto     # sin paréntesis: guarda la función
otra_forma(2000)                   # con paréntesis: la ejecuta

operaciones = [saludar, calcular_impuesto]
print("Guardadas en una lista:", len(operaciones))
operaciones[0]()                   # llama a saludar desde la lista
"""),

md("""
## Cuatro palabras que se confunden

| Término | Qué es | Dónde aparece | Ejemplo |
|---|---|---|---|
| Parámetro | El hueco que declaras | En el `def` | `def saludar_a(nombre)` |
| Argumento | El valor que pasas | En la llamada | `saludar_a("Ana")` |
| Retorno | Lo que la función entrega | En el `return` | `return total / n` |
| Llamada | La orden de ejecutarla | Donde la uses | `saludar_a("Ana")` |

La confusión más común es entre las dos primeras. El parámetro se escribe una vez, al definir. El
argumento cambia en cada llamada.
"""),

code("""
def describir(producto, cantidad):     # producto y cantidad son parámetros
    print(f"{cantidad} x {producto}")


describir("café", 3)                   # "café" y 3 son argumentos
describir("filtro", 12)                # otros argumentos, mismos parámetros
describir(cantidad=5, producto="taza")  # por nombre, en cualquier orden
"""),

md("""
La última llamada usa **argumentos por nombre**. Al escribir el nombre del parámetro en la llamada,
el orden deja de importar y la línea se lee sola.

Compara `increment(2, 1)` con `increment(number=2, by=1)`. La primera obliga a ir a buscar la
definición para saber cuál es cuál.

## Valores por defecto

Un parámetro con valor por defecto se vuelve opcional. Si la llamada no lo trae, se usa el valor
que quedó escrito en el `def`.
"""),

code("""
def presentar(nombre, apellido, saludo="Hola"):
    print(f"{saludo}, {nombre} {apellido}")


presentar("Ana", "López")                     # usa el valor por defecto
presentar("Ana", "López", "Buenos días")      # lo reemplaza
presentar(apellido="López", nombre="Ana")     # por nombre, sin orden
"""),

md("""
## Los que tienen valor van al final

Y no es una convención de estilo. Es un error de sintaxis, porque con el orden invertido Python no
tendría forma de saber cuál argumento se omitió.
"""),

code("""
# FALLA A PROPÓSITO. Un parámetro sin valor no puede ir después de uno con valor.
try:
    compile("def presentar(saludo='Hola', nombre):\\n    pass", "<ejemplo>", "exec")
except SyntaxError as e:
    print("SyntaxError:", e.msg)
"""),

md("""
Python lo rechaza al leer el archivo, antes de ejecutar una sola línea. Es el mismo tipo de rechazo
temprano que viste en el repaso 2 con el `if` de un solo igual, y en los dos casos te está evitando
un bug que sería mucho más caro encontrar después.

## Las anotaciones de tipo documentan, no obligan

Puedes escribir de qué tipo esperas cada parámetro y qué tipo devuelve la función. Python **no lo
revisa al ejecutar**.
"""),

code("""
def imprimir_edad(edad: int) -> None:
    print("Edad:", edad)


def area_rectangulo(base: float, altura: float) -> float:
    return base * altura


imprimir_edad(20)
print("Área:", area_rectangulo(2, 3))
"""),

code("""
# FALLA A PROPÓSITO, y no truena. La anotación dice int y le pasamos una cadena.
imprimir_edad("veinte")
imprimir_edad([1, 2, 3])

print()
print("La anotación sigue ahí, sin haber servido de nada:")
print(imprimir_edad.__annotations__)
"""),

md("""
Las tres llamadas funcionaron. La anotación quedó guardada en `__annotations__` y ningún mecanismo
la consultó.

Entonces para qué se escriben. Por dos razones que no tienen que ver con la ejecución: el editor
autocompleta mejor, y una herramienta como `mypy` o el propio VS Code marca el error mientras
escribes, no cuando el programa ya está corriendo en producción.

## La trampa de la lista por defecto

Esta es la más famosa del lenguaje, y la única del módulo que produce datos incorrectos sin decir
nada.
"""),

code("""
# FALLA A PROPÓSITO, y no truena. La lista por defecto se crea UNA vez.
def agregar_nota(nota, notas=[]):
    notas.append(nota)
    return notas


print("Primera llamada: ", agregar_nota(8))
print("Segunda llamada: ", agregar_nota(9))
print("Tercera llamada: ", agregar_nota(10))
print()
print("La lista guardada en la definición:", agregar_nota.__defaults__)
"""),

md("""
La tercera llamada devolvió tres notas, y solo se le pasó una.

El valor por defecto se evalúa **una sola vez**, cuando Python lee el `def`. Esa lista vive pegada a
la función, en `__defaults__`, y cada llamada que no trae argumento le agrega encima. Un servidor
que corre semanas con esa función acumula ahí todo lo que pasó por ella.

La solución es usar `None` como valor por defecto y crear la lista dentro.
"""),

code("""
def agregar_nota_bien(nota, notas=None):
    if notas is None:
        notas = []          # una lista nueva en cada llamada
    notas.append(nota)
    return notas


print("Primera llamada: ", agregar_nota_bien(8))
print("Segunda llamada: ", agregar_nota_bien(9))
print("Tercera llamada: ", agregar_nota_bien(10))
"""),

md("""
Aquí es donde el `is None` del repaso 2 encuentra su primer uso de verdad. No se compara con `==`
porque una lista vacía también daría falso en un `if`, y entonces `notas=[]` explícita se
confundiría con "no me pasaron nada".

Guarda esta celda. En la semana 6, cuando dos objetos de la misma clase compartan una lista sin que
nadie entienda por qué, va a ser exactamente este mecanismo con otro disfraz.

## Redefinir una función la reemplaza en silencio
"""),

code("""
# FALLA A PROPÓSITO, y no truena. Dos funciones con el mismo nombre.
def imprimir_nombre(nombre, apellido="Doe"):
    print(nombre, apellido)


imprimir_nombre("Juan")            # funciona, usa el valor por defecto


def imprimir_nombre(nombre, apellido):     # el mismo nombre, otra firma
    print(nombre, apellido)


try:
    imprimir_nombre("Juan")        # la misma llamada de arriba
except TypeError as e:
    print("TypeError:", e)
"""),

md("""
La llamada no cambió. Lo que cambió es a qué función apunta el nombre.

Un `def` es una asignación: crea la función y la ata a ese nombre, igual que `x = 5`. Si más abajo
en el archivo hay otro `def` con el mismo nombre, el segundo pisa al primero y nadie avisa.

Esto no es un ejemplo inventado. `Code010.py` del curso define `print_name` en la línea 82 y la
vuelve a definir en la línea 144 con otra firma. El archivo corre limpio porque todas las llamadas
están antes de la segunda definición, pero cualquiera que agregue una línea al final se lleva la
sorpresa.
"""),

md("""
---
# Bloque 2 · Devolver

Imprimir y devolver no son lo mismo, y confundirlos rompe la mitad de los ejercicios del curso.

`print` escribe en la consola y no deja nada aprovechable. `return` le entrega un valor a quien
llamó, para que pueda guardarlo, sumarlo o pasárselo a otra función.
"""),

code("""
def promedio_imprime(notas):
    print(sum(notas) / len(notas))


def promedio_devuelve(notas):
    return sum(notas) / len(notas)


a = promedio_imprime([8, 9, 10])
b = promedio_devuelve([8, 9, 10])

print("a vale", a, "y es", type(a).__name__)
print("b vale", b, "y es", type(b).__name__)
"""),

md("""
Las dos funciones calcularon lo mismo. Solo una lo entregó.

**Una función sin `return` devuelve `None`.** Siempre, sin excepción, y sin avisar. Por eso `a`
quedó en `None` aunque en la pantalla apareciera el 9.0: ese nueve lo escribió el `print` de adentro
y se perdió ahí mismo.
"""),

code("""
# FALLA A PROPÓSITO. Operar con lo que devolvió una función que solo imprime.
try:
    print("El promedio por diez es", a * 10)
except TypeError as e:
    print("TypeError:", e)

print("Con la que devuelve:", b * 10)
"""),

md("""
El `TypeError` aparece en la línea de la multiplicación, que es donde no está el problema. El
problema está en la función, varias líneas arriba, y ahí no truena nada.

Ese patrón de "el error aparece lejos de su causa" es el mismo del repaso 1 con el tipado dinámico.
Vas a verlo una y otra vez.

## `return` también termina la función
"""),

code("""
def revisar(edad):
    if edad < 0:
        return "edad inválida"     # sale aquí mismo
    print("Esta línea solo corre si la edad es válida")
    return "edad aceptada"


print(revisar(-5))
print()
print(revisar(30))
"""),

md("""
Con `-5` nunca se imprimió la línea de en medio. El `return` entregó el valor y abandonó la función
en ese punto.

Puede haber varios `return` en una función, pero **solo uno se ejecuta**. Ese es el patrón de la
salida temprana, y es lo que evita el `if`/`else` anidado de seis niveles.
"""),

code("""
def clasificar_edad(edad):
    if edad < 0:
        return "inválida"
    if edad < 18:
        return "menor"
    if edad < 65:
        return "adulta"
    return "adulta mayor"


for edad in [-1, 10, 30, 70]:
    print(f"{edad:>3} -> {clasificar_edad(edad)}")
"""),

md("""
## Devolver varias cosas a la vez
"""),

code("""
def cuadrado_y_cubo(numero):
    return numero * numero, numero * numero * numero


resultado = cuadrado_y_cubo(2)
print("Devuelve:", resultado, "de tipo", type(resultado).__name__)

cuadrado, cubo = cuadrado_y_cubo(3)     # desempaque
print("Cuadrado:", cuadrado, "· cubo:", cubo)
"""),

md("""
La coma en el `return` construye una tupla. No hay una sintaxis especial para devolver dos valores,
solo hay una tupla que se desempaca del otro lado.

Las tuplas son el tema del repaso 4. Por ahora basta con saber que el número de nombres a la
izquierda tiene que coincidir con el número de valores.
"""),

code("""
# FALLA A PROPÓSITO. Tres nombres para dos valores.
try:
    a1, a2, a3 = cuadrado_y_cubo(4)
except ValueError as e:
    print("ValueError:", e)
"""),

md("""
## El riesgo que la diapositiva señala

`calcular_promedio` divide entre `len(calificaciones)`. Con una lista vacía, eso es una división
entre cero.
"""),

code("""
def calcular_promedio(calificaciones: list) -> float:
    total = 0
    for nota in calificaciones:
        total += nota
    return total / len(calificaciones)


print("Con datos:", calcular_promedio([8, 9, 10]))

# FALLA A PROPÓSITO. La lista vacía no tiene nada que promediar.
try:
    print(calcular_promedio([]))
except ZeroDivisionError as e:
    print("ZeroDivisionError:", e)
"""),

md("""
Una lista vacía no es un caso raro. Es lo que llega cuando un filtro no encontró nada, cuando el
archivo venía sin renglones, o cuando el grupo todavía no tiene calificaciones capturadas.

El repaso 5 lo atrapa con `try`. Por ahora, la versión defensiva es decidir qué significa el
promedio de nada y escribirlo.
"""),

code("""
def calcular_promedio_seguro(calificaciones):
    if not calificaciones:          # la lista vacía cuenta como falsa
        return None                 # "no hay promedio" no es lo mismo que "cero"
    return sum(calificaciones) / len(calificaciones)


for grupo in [[8, 9, 10], [], [7]]:
    print(f"{str(grupo):<12} -> {calcular_promedio_seguro(grupo)}")
"""),

md("""
Devolver `None` y no `0` es una decisión, no un detalle. Un promedio de cero dice que el grupo
reprobó. `None` dice que no hay con qué calcular, que es lo que de verdad pasó.
"""),

md("""
---
# Bloque 3 · Alcance

Dónde vive una variable y cuánto dura.

Una variable declarada dentro de una función solo existe mientras la función corre. Fuera de ella
Python no conoce el nombre.
"""),

code("""
def mi_funcion():
    mensaje = "Hola mundo"      # local: nace y muere con la llamada
    print("Dentro:", mensaje)


mi_funcion()

# FALLA A PROPÓSITO. Afuera, ese nombre no existe.
try:
    print(mensaje)
except NameError as e:
    print("NameError:", e)
"""),

code("""
# FALLA A PROPÓSITO. Los parámetros también son locales.
def mi_funcion2(frase):
    print("Dentro:", frase)


mi_funcion2("una frase")

try:
    print(frase)
except NameError as e:
    print("NameError:", e)
"""),

md("""
## La regla de búsqueda

Cuando Python encuentra un nombre dentro de una función, lo busca en este orden:

1. En el alcance local de la función.
2. Si no está, afuera, en el alcance global.
3. Si tampoco está, levanta `NameError`.

Leer una global desde adentro funciona sin ceremonia.
"""),

code("""
IVA = 0.16          # global, en MAYÚSCULAS por convención de constante


def con_impuesto(monto):
    return monto * (1 + IVA)      # lee la global sin declarar nada


print(con_impuesto(1000))
"""),

md("""
## Asignar adentro es otra historia
"""),

code("""
mensaje = "global"


def cambiar():
    mensaje = "local"       # NO modifica la de afuera: crea una nueva
    print("Dentro:", mensaje)


cambiar()
print("Afuera:", mensaje)
"""),

md("""
Adentro imprimió `local` y afuera sigue diciendo `global`. Son dos variables distintas que comparten
el nombre y no se conocen entre sí.

**Si asignas a un nombre dentro de una función, Python lo trata como local.** Aunque exista una
global que se llame igual, aunque la asignación esté en la última línea.

Para modificar la global de verdad hace falta declararlo.
"""),

code("""
mensaje = "global"


def cambiar_de_verdad():
    global mensaje          # ahora sí es la de afuera
    mensaje = "cambiada desde adentro"


cambiar_de_verdad()
print("Afuera:", mensaje)
"""),

md("""
Funciona, y aun así casi nunca es lo que quieres.

Una función que modifica globales no se puede leer sola: para saber qué hace hay que revisar quién
más toca esa variable en todo el archivo. Tampoco se puede probar de forma aislada, porque su
resultado depende de lo que haya pasado antes.

**La alternativa es devolver el valor.** La función queda con una sola entrada y una sola salida.
"""),

code("""
def cambiar_devolviendo(actual):
    return actual.upper() + " (procesada)"


mensaje = "global"
mensaje = cambiar_devolviendo(mensaje)
print(mensaje)
"""),

md("""
En la semana 3 esto cambia de forma. Un objeto tiene sus propios datos, y un método los modifica
escribiendo `self.mensaje = ...` sin necesitar `global` ni devolver nada. Eso es lo que las clases
vinieron a resolver: darle a un grupo de funciones un lugar compartido donde guardar cosas, sin
ensuciar el alcance global.

## Predice antes de correr

¿Qué imprime la última línea?

- **A.** 5, porque `total` valía 0 y le sumó 5.
- **B.** `UnboundLocalError`, porque `total` es local y se lee antes de asignarla.
- **C.** 0, porque la global no cambió.
- **D.** `None`, porque la función no devuelve nada.
"""),

code("""
# FALLA A PROPÓSITO. La respuesta del quiz, atrapada para que el cuaderno siga.
total = 0


def sumar(n):
    total = total + n
    return total


try:
    print(sumar(5))
except UnboundLocalError as e:
    print("UnboundLocalError:", e)
"""),

md("""
La respuesta es **B**.

| Paso | Qué ve Python | Decisión |
|---|---|---|
| 1 | `total = 0` fuera de la función | es global |
| 2 | dentro hay una asignación a `total` | la trata como local en toda la función |
| 3 | el lado derecho lee `total` | la local todavía no existe |
| 4 | levanta `UnboundLocalError` | antes de sumar nada |

Lo que descoloca es que la decisión se toma **antes de ejecutar una sola línea**. Python revisa el
cuerpo completo al compilar la función: si encuentra una asignación a `total` en cualquier línea, el
nombre es local en todas, incluida la línea que lo lee primero.

Las dos salidas, y solo una es buena.
"""),

code("""
# La limpia: recibir y devolver.
def sumar_bien(total, n):
    return total + n


total = 0
total = sumar_bien(total, 5)
print("Con parámetro y retorno:", total)


# La que funciona pero ata la función a esa variable.
total = 0


def sumar_global(n):
    global total
    total = total + n
    return total


print("Con global:            ", sumar_global(5))
"""),

md("""
La primera versión se puede llamar con cualquier par de números y probar sin montar nada alrededor.
La segunda solo sirve si existe una variable llamada `total`, y devuelve algo distinto según cuántas
veces se haya llamado antes.

## Cada llamada estrena locales
"""),

code("""
def contar():
    n = 0           # se crea al entrar
    n += 1
    return n        # y se destruye al salir


print([contar() for _ in range(5)])
"""),

md("""
Cinco llamadas y cinco unos. La `n` de una llamada no sabe nada de la `n` de la anterior, porque cada
una vivió en su propia ejecución.

Esa es justamente la carencia que resuelve un objeto. Cuando en la semana 3 escribas `self.n += 1`,
el valor sí va a sobrevivir entre llamadas, porque no vive en la función sino en el objeto.
"""),

md("""
---
# FizzBuzz, el ejercicio que junta todo lo anterior

Imprimir los números del 1 al 100, cambiando los múltiplos de tres por `Fizz`, los de cinco por
`Buzz`, y los de ambos por `FizzBuzz`.

Cabe en diez líneas y repasa función, ciclo, residuo, condicional encadenado y `else` por defecto.
Es pregunta de entrevista desde hace veinte años, y la razón es que el orden de las condiciones
separa a quien entendió `elif` de quien lo memorizó.
"""),

code("""
def fizz_buzz(hasta=100):
    \"\"\"Imprime del 1 a hasta, con las sustituciones de FizzBuzz.\"\"\"
    for numero in range(1, hasta + 1):
        if numero % 3 == 0 and numero % 5 == 0:
            print("FizzBuzz")
        elif numero % 3 == 0:
            print("Fizz")
        elif numero % 5 == 0:
            print("Buzz")
        else:
            print(numero)


fizz_buzz(15)      # los primeros quince, para no llenar la pantalla
"""),

md("""
Con quince ya se ven los cuatro casos: el 3 salió `Fizz`, el 5 salió `Buzz`, el 15 salió `FizzBuzz`
y el resto salió como número.

## Por qué la condición doble va primero

Porque `elif` se detiene en la primera rama verdadera. Si `numero % 3 == 0` se evalúa antes, el 15
entra ahí y nunca llega a la rama de `FizzBuzz`.

En lugar de afirmarlo, cuéntalo.
"""),

code("""
def contar_fizz_buzz(orden_correcto):
    \"\"\"Cuenta cuántos de 1 a 100 caen en cada categoría.\"\"\"
    cuentas = {"FizzBuzz": 0, "Fizz": 0, "Buzz": 0, "número": 0}
    for numero in range(1, 101):
        if orden_correcto and numero % 3 == 0 and numero % 5 == 0:
            cuentas["FizzBuzz"] += 1
        elif numero % 3 == 0:
            cuentas["Fizz"] += 1
        elif numero % 5 == 0:
            cuentas["Buzz"] += 1
        elif numero % 3 == 0 and numero % 5 == 0:
            cuentas["FizzBuzz"] += 1        # inalcanzable con el orden malo
        else:
            cuentas["número"] += 1
    return cuentas


# FALLA A PROPÓSITO, y no truena. Compara los dos órdenes.
bien = contar_fizz_buzz(True)
mal = contar_fizz_buzz(False)

print(f"{'Categoría':<12}{'Orden bueno':>12}{'Orden malo':>12}")
for clave in bien:
    print(f"{clave:<12}{bien[clave]:>12}{mal[clave]:>12}")
"""),

md("""
Con el orden malo, `FizzBuzz` sale en cero y `Fizz` sube de 27 a 33. Los seis que faltan son el 15,
30, 45, 60, 75 y 90, y se fueron todos a `Fizz`.

Ninguna de las cien líneas lanzó un error. El programa corre, imprime cien renglones y seis están
mal. Una categoría con cero casos después de recorrer todo el rango es la firma de una rama
inalcanzable, la misma del repaso 2.
"""),

code("""
print("Los seis que cambian de categoría:",
      [n for n in range(1, 101) if n % 3 == 0 and n % 5 == 0])
"""),

md("""
## La versión que devuelve

`fizz_buzz` imprime, y por eso no se puede probar sin leer la pantalla. Una función que **devuelve**
la etiqueta se puede verificar con una comparación.
"""),

code("""
def evaluar_fizz_buzz(numero: int) -> str:
    \"\"\"Devuelve la etiqueta que le toca a un número.\"\"\"
    if numero % 3 == 0 and numero % 5 == 0:
        return "FizzBuzz"
    if numero % 3 == 0:
        return "Fizz"
    if numero % 5 == 0:
        return "Buzz"
    return str(numero)


ESPERADO = {1: "1", 3: "Fizz", 5: "Buzz", 9: "Fizz", 10: "Buzz", 15: "FizzBuzz",
            30: "FizzBuzz", 98: "98"}

for numero, esperado in ESPERADO.items():
    obtenido = evaluar_fizz_buzz(numero)
    marca = "ok" if obtenido == esperado else "FALLA"
    print(f"{numero:>3} -> {obtenido:<9} esperado {esperado:<9} {marca}")
"""),

md("""
Fíjate en que ya no hace falta un `else` final: como cada `return` sale de la función, la última
línea solo se alcanza si ninguna condición se cumplió.

Y ahora imprimir es asunto de quien llama, no de la función.
"""),

code("""
for numero in range(1, 16):
    print(evaluar_fizz_buzz(numero), end="  ")
print()
"""),

md("""
## Cuatro errores de este módulo

**Definir y no llamar.** El `def` solo crea la función. Sin la llamada con paréntesis, nunca corre y
nada avisa.

**Imprimir en vez de devolver.** La función muestra el resultado y entrega `None`, así que quien la
llamó se queda con las manos vacías.

**Esperar que la local cambie la global.** Asignar adentro crea una variable nueva. Para modificar la
de afuera, devuélvela.

**Lista como valor por defecto.** `def f(x=[])` comparte la misma lista entre todas las llamadas.
Usa `None` y créala adentro.

Los cuatro corrieron arriba, y tres de ellos sin lanzar un solo error.
"""),

md("""
---
# Ejercicios

Las soluciones están hasta abajo del cuaderno.

### Ejercicio 1 · La más pequeña

Escribe una función `presentarse` que no reciba nada e imprima tu nombre y tu carrera. Llámala tres
veces. Después escribe una línea que la mencione **sin** paréntesis e imprime lo que sale.

### Ejercicio 2 · Parámetro contra argumento

Escribe `calcular_total(precio, cantidad, descuento=0)` que imprima el total. Llámala de cuatro
formas: por posición, por nombre, mezclando las dos, y omitiendo el descuento.

Di en un comentario cuál de las cuatro se lee mejor y por qué.

### Ejercicio 3 · Imprimir contra devolver

Escribe dos versiones de una función que calcule el área de un círculo, una que imprima y otra que
devuelva. Intenta usar el resultado de las dos para calcular el área de tres círculos sumadas.

Atrapa el error de la primera e imprímelo.

### Ejercicio 4 · Salida temprana

Escribe `clasificar_imc(peso, estatura)` que devuelva la categoría según el índice de masa corporal:
menos de 18.5 bajo peso, menos de 25 normal, menos de 30 sobrepeso, y de ahí para arriba obesidad.

Usa varios `return` en lugar de `if`/`elif` anidados. Pruébala con los valores exactos de cada
frontera.

### Ejercicio 5 · Devolver varias cosas

Escribe `estadisticas(numeros)` que devuelva el mínimo, el máximo y el promedio en un solo `return`.
Desempácalo en tres variables al llamarla.

Después intenta desempacarlo en dos y atrapa el `ValueError`.

### Ejercicio 6 · La trampa de la lista

Reproduce el error de la lista por defecto con una función `registrar_asistencia(alumno, lista=[])`.
Llámala cuatro veces con alumnos distintos y muestra qué devuelve cada llamada.

Después arréglala con `None` y demuestra con las mismas cuatro llamadas que ahora sí funciona.

### Ejercicio 7 · Alcance

Escribe una función que intente modificar una variable global de tres formas: asignando directo,
usando `global`, y devolviendo el valor. Muestra qué vale la global después de cada una.

Di en un comentario cuál de las tres usarías en un programa de verdad.

### Ejercicio 8 · El contador que no cuenta

Escribe una función `siguiente_folio()` que quieras que devuelva 1, 2, 3 en llamadas sucesivas.
Hazla primero con una variable local y demuestra que siempre devuelve 1.

Después arréglala con `global` y explica en un comentario por qué esa solución no escala a dos
contadores independientes.

### Ejercicio 9 · La tarea

Escribe tres funciones que reciban una lista de calificaciones y devuelvan el promedio, la más alta,
y cuántas aprobaron con 7 o más.

Las tres devuelven con `return` y ninguna imprime desde adentro. Las tres reciben la lista como
parámetro y ninguna lee una variable global. Cada nombre es un verbo y un sustantivo.

Pruébalas con una lista normal y con una vacía.
"""),

md("""
---
## Tres ideas para llevarse

**Una función es una responsabilidad con nombre.** En tres semanas eso mismo se va a llamar método y
va a vivir dentro de una clase, con las mismas reglas de parámetros y retorno que acabas de ver.

**`return` entrega, `print` solo muestra.** Una función de cálculo que imprime deja al que la llamó
con `None` en las manos, y el `TypeError` aparece varias líneas después.

**Asignar adentro crea una variable local.** Aunque exista una global con el mismo nombre, y aunque
la asignación esté en la última línea de la función.

El siguiente repaso son las cuatro colecciones y cuándo usar cada una. Ahí vuelve la lista por
defecto de este cuaderno, con el nombre de alias, y es la que en la semana 6 explica por qué dos
objetos comparten estado.
"""),

md("""
---
# Soluciones

### Ejercicio 1

```python
def presentarse():
    print("David Escobar, Ingeniería en Sistemas")


presentarse()
presentarse()
presentarse()

print(presentarse)      # sin paréntesis: la referencia, no la ejecución
```

La última línea imprime algo como `<function presentarse at 0x7f...>`. La dirección cambia en cada
sesión, y no significa nada útil salvo que ahí hay una función y no un resultado.

### Ejercicio 2

```python
def calcular_total(precio, cantidad, descuento=0):
    total = precio * cantidad * (1 - descuento)
    print(f"Total: {total:,.2f}")


calcular_total(150, 3, 0.10)                              # posición
calcular_total(precio=150, cantidad=3, descuento=0.10)    # nombre
calcular_total(150, cantidad=3, descuento=0.10)           # mezcla
calcular_total(150, 3)                                    # sin descuento

# La segunda se lee mejor. En la primera, el 0.10 no dice si es un descuento,
# un impuesto o una comisión, y hay que ir a buscar la definición para saberlo.
# El costo de escribir los nombres se paga una vez; el de ir a buscar la firma
# se paga cada vez que alguien lee esa línea.
```

### Ejercicio 3

```python
import math


def area_circulo_imprime(radio):
    print(math.pi * radio ** 2)


def area_circulo_devuelve(radio):
    return math.pi * radio ** 2


try:
    suma = (area_circulo_imprime(1) + area_circulo_imprime(2)
            + area_circulo_imprime(3))
except TypeError as e:
    print("TypeError:", e)

suma = (area_circulo_devuelve(1) + area_circulo_devuelve(2)
        + area_circulo_devuelve(3))
print(f"Suma de las tres áreas: {suma:.4f}")
```

La primera versión imprime los tres números y después truena al intentar sumar tres `None`. Los
números aparecieron en pantalla, que es lo que engaña: parece que la función funcionó.

### Ejercicio 4

```python
def clasificar_imc(peso, estatura):
    imc = peso / estatura ** 2
    if imc < 18.5:
        return "bajo peso"
    if imc < 25:
        return "normal"
    if imc < 30:
        return "sobrepeso"
    return "obesidad"


# Los valores exactos de cada frontera, con estatura 1.70 para despejar la cuenta.
for imc_objetivo in [18.4, 18.5, 24.9, 25.0, 29.9, 30.0]:
    peso = imc_objetivo * 1.70 ** 2
    print(f"IMC {imc_objetivo:>5} (peso {peso:>6.2f}) -> {clasificar_imc(peso, 1.70)}")
```

En los tres límites el valor exacto sube de categoría, porque las condiciones usan `<`. Un IMC de
exactamente 25 sale `normal` con `<=` y `sobrepeso` con `<`, y la definición médica dice que 25 ya
es sobrepeso. La frontera la decide la definición, no la comodidad del código.

### Ejercicio 5

```python
def estadisticas(numeros):
    return min(numeros), max(numeros), sum(numeros) / len(numeros)


datos = [8, 3, 10, 6, 9]

minimo, maximo, promedio = estadisticas(datos)
print(f"Mínimo {minimo} · máximo {maximo} · promedio {promedio}")

try:
    a, b = estadisticas(datos)
except ValueError as e:
    print("ValueError:", e)
```

El mensaje del `ValueError` dice cuántos valores llegaron y cuántos nombres había. Es de los pocos
errores de Python que te da el diagnóstico completo en una línea.

### Ejercicio 6

```python
def registrar_asistencia(alumno, lista=[]):
    lista.append(alumno)
    return lista


for alumno in ["Ana", "Beto", "Carla", "Diego"]:
    print(f"{alumno:<7} -> {registrar_asistencia(alumno)}")

print()


def registrar_asistencia_bien(alumno, lista=None):
    if lista is None:
        lista = []
    lista.append(alumno)
    return lista


for alumno in ["Ana", "Beto", "Carla", "Diego"]:
    print(f"{alumno:<7} -> {registrar_asistencia_bien(alumno)}")
```

La primera versión llega a cuatro alumnos en la última llamada y ninguno de ellos fue registrado en
esa llamada. La segunda devuelve una lista de uno cada vez, que es lo que dice el nombre de la
función.

### Ejercicio 7

```python
contador = 10


def asignar_directo():
    contador = 99


def con_global():
    global contador
    contador = 99


def devolviendo(actual):
    return actual + 89


asignar_directo()
print("Después de asignar directo:", contador)

con_global()
print("Después de global:        ", contador)

contador = 10
contador = devolviendo(contador)
print("Después de devolver:      ", contador)

# En un programa de verdad, la tercera. La función no depende de que exista una
# variable llamada contador, se puede probar con cualquier número, y leyendo la
# línea de la llamada ya se sabe qué cambió. Con global hay que buscar en todo el
# archivo quién más la toca antes de poder afirmar nada.
```

### Ejercicio 8

```python
def siguiente_folio_local():
    folio = 0
    folio += 1
    return folio


print("Con local: ", [siguiente_folio_local() for _ in range(3)])

folio_global = 0


def siguiente_folio_global():
    global folio_global
    folio_global += 1
    return folio_global


print("Con global:", [siguiente_folio_global() for _ in range(3)])

# La versión con global no escala porque el nombre de la variable está escrito
# dentro de la función. Para llevar dos contadores independientes, uno de facturas
# y otro de notas de crédito, harían falta dos variables globales y dos funciones
# casi idénticas. Eso es exactamente el problema que resuelve una clase: cada
# objeto trae su propio contador y la función se escribe una sola vez.
```

### Ejercicio 9

```python
def calcular_promedio(calificaciones):
    if not calificaciones:
        return None
    return sum(calificaciones) / len(calificaciones)


def obtener_maxima(calificaciones):
    if not calificaciones:
        return None
    return max(calificaciones)


def contar_aprobados(calificaciones, minima=7):
    return sum(1 for nota in calificaciones if nota >= minima)


GRUPO = [8, 5, 10, 6.5, 9, 7, 4, 8.5]

print(f"Promedio: {calcular_promedio(GRUPO):.2f}")
print(f"Máxima:   {obtener_maxima(GRUPO)}")
print(f"Aprobados: {contar_aprobados(GRUPO)} de {len(GRUPO)}")

print()
print("Con lista vacía:", calcular_promedio([]), obtener_maxima([]),
      contar_aprobados([]))
```

`contar_aprobados` sí puede devolver cero con lista vacía, y ahí el cero es la respuesta correcta:
nadie aprobó porque no hay nadie. Las otras dos devuelven `None`, porque el promedio y el máximo de
un conjunto vacío no existen.

Esa distinción entre "el resultado es cero" y "no hay resultado" es la que hace que un reporte diga
la verdad. `max([])` de hecho lanza `ValueError` por la misma razón, y el repaso 5 lo va a atrapar.
"""),

]

write(OUT / "es" / "w01.3.ipynb", es)
print("wrote", OUT / "es" / "w01.3.ipynb")
