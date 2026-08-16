"""notebooks/programacion-orientada-a-objetos/es/w09.ipynb

Source deck: ppts/python/programacion-orientada-a-objetos/es/w09.es.yaml
Source code:  docs/en/courses/python-course/01 - Basics/3rd Module/  (funciones)
              docs/en/courses/python-course/07 - Activities/Projects/02 - Hanoi Tower/
                  hanoi_tower.py

hanoi_tower.py no se puede correr tal cual en un cuaderno: pide el número de
discos con input(), llama a os.system("cls") dos veces y termina con otro
input(). El algoritmo, que son las dos funciones de en medio, se cita completo y
sin tocar; la plomería de consola se deja fuera y el cuaderno lo dice.

El repaso 3 (w01.3) ya cubrió lo básico de funciones, incluida la lista por
omisión. Aquí no se repite: se retoma con __defaults__ enfrente y se sigue con
lo que falta.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from nbkit import md, code, write, REPO

OUT = REPO / "notebooks" / "programacion-orientada-a-objetos"

es = [

md("""
# Programación Orientada a Objetos · Semana 09
## Tema 4 · Funciones y estructuras avanzadas

**COM102 · Facultad de Ingeniería · Profesor David Escobar-Castillejos**

Empieza la unidad de aplicación. Funciones que se prueban solas, código repartido en piezas, y
funciones que se llaman a sí mismas.

Nada de esto es sintaxis nueva. Lo avanzado son tres decisiones: qué recibe una función, qué devuelve, y
qué deja modificado fuera de sí misma. La tercera es la que casi nadie mira y la que decide si el código
se puede probar.

Al terminar vas a poder:

1. Diseñar la firma de una función, decidiendo qué va posicional, qué lleva valor por omisión y qué
   conviene exigir por nombre.
2. Pasar una función como argumento y escribir un criterio de orden con `lambda`.
3. Partir un script en funciones que hagan una sola cosa cada una.
4. Escribir una función recursiva con un caso base que corte y una llamada que se acerque a él.
5. Decir cuánto cuesta una recursión antes de correrla.

### Cómo se usa este cuaderno

Ejecuta las celdas en orden con **Shift + Enter**. Diez fallan a propósito y llevan un comentario que lo
dice.

Ocho de las diez **no lanzan ninguna excepción**. Dos de esas ocho son las que más caro cobran fuera
de clase: el valor por omisión que se evalúa una sola vez, y la `lambda` dentro de un ciclo que se lleva
la variable y no su valor.
"""),

md("""
---
# Bloque 1 · Funciones avanzadas

## Tres maneras de llamar a la misma función
"""),

code("""
def registrar(nombre: str, carrera: str = "Sin definir", activo: bool = True) -> None:
    print(f"  {nombre:<8}{carrera:<16}activo={activo}")


registrar("Ana")
registrar("Luis", "Mecatrónica")
registrar("Sofía", activo=False)
registrar(carrera="Industrial", nombre="Marco")

print()
print("Valores por omisión:", registrar.__defaults__)
print("Parámetros:", registrar.__code__.co_varnames[:registrar.__code__.co_argcount])
"""),

md("""
Cuatro llamadas, una sola firma.

Pasar `activo` por nombre deja que `carrera` se quede con su valor por omisión, y ese es el punto
entero de los argumentos con nombre: **saltarse los de en medio sin repetirlos**.

La última llamada invierte el orden y funciona igual, porque con nombre la posición deja de importar.
"""),

code("""
# FALLA A PROPÓSITO. Los parámetros con omisión van al final, sin excepción.
FUENTE = "def f(a=1, b):\\n    return a + b"

try:
    compile(FUENTE, "<ejemplo>", "exec")
except SyntaxError as e:
    print("SyntaxError:", e.msg)
    print("En la línea:", e.text.strip())

print()
print("Y al revés sí compila:", bool(compile("def f(b, a=1):\\n    return a + b",
                                             "<ejemplo>", "exec")))
"""),

md("""
`parameter without a default follows parameter with a default`.

La razón es de lectura, no de capricho: si `a` tuviera omisión y `b` no, `f(5)` sería ambiguo. ¿El cinco
es `a` o es `b`? Poniendo los que tienen omisión al final, los posicionales siempre se llenan de
izquierda a derecha y no hay nada que adivinar.

Este es de los pocos errores del cuaderno que se ven al escribir. Los que siguen no.

## El valor por omisión se evalúa una sola vez
"""),

code("""
# FALLA A PROPÓSITO, y no truena. La lista por omisión, con la prueba enfrente.
def agregar_tarea(tarea, lista=[]):
    lista.append(tarea)
    return lista


print(agregar_tarea("comprar café"))
print(agregar_tarea("mandar correo"))
print(agregar_tarea("revisar tareas"))

print()
print("Lo que guarda la función:", agregar_tarea.__defaults__)
print("¿Es la misma lista de las tres llamadas?",
      agregar_tarea.__defaults__[0] is agregar_tarea("cuarta"))
"""),

md("""
Tres llamadas independientes y una lista que crece.

Ya lo viste en el repaso 3 y en la semana 5. Lo que agrega esta celda es la prueba: `__defaults__` es una
tupla que vive **en la función**, se llenó una sola vez cuando Python leyó el `def`, y contiene esa
lista. No hay tres listas, hay una.

La regla, ahora con el porqué: **el valor por omisión se evalúa al definir la función, no al llamarla.**

Eso vale para cualquier expresión, no solo para las listas.
"""),

code("""
# FALLA A PROPÓSITO, y no truena. Una omisión que se calcula una vez y se congela.
import itertools

siguiente_folio = itertools.count(1000).__next__


def emitir(concepto, folio=siguiente_folio()):
    return f"folio {folio}: {concepto}"


print(emitir("consultoría"))
print(emitir("capacitación"))
print(emitir("mantenimiento"))

print()
print("El folio congelado:", emitir.__defaults__)
print("¿Los tres folios son el mismo?",
      len({emitir(c).split(":")[0] for c in ["a", "b", "c"]}) == 1)
print()


def emitir_bien(concepto, folio=None):
    if folio is None:
        folio = siguiente_folio()
    return f"folio {folio}: {concepto}"


for concepto in ["consultoría", "capacitación", "mantenimiento"]:
    print(emitir_bien(concepto))
"""),

md("""
Tres facturas con el mismo folio, y ninguna advertencia.

`siguiente_folio()` corrió una sola vez, mientras Python leía el `def`, y ese número quedó guardado en
`__defaults__` para siempre. Con la lista el síntoma era que crecía; aquí el síntoma es que no cambia
nunca, y las dos cosas salen del mismo mecanismo.

La corrección es la misma de siempre: **`None` por omisión, y el valor de verdad se calcula adentro**.

Este error es más traicionero que el de la lista porque suele aparecer con fechas.
`def registrar(evento, cuando=datetime.now())` sella todos los eventos con la hora en que se importó el
módulo.

## Cinco formas de recibir un dato

| Forma | Cómo se ve | Qué recibe |
|---|---|---|
| Posicional | `def f(a, b)` | En el orden en que se pasan |
| Con omisión | `def f(a, b=0)` | El valor dado, o el de omisión |
| Por nombre | `f(b=3)` | Sin importar la posición |
| Variable | `def f(*args)` | Una tupla con lo que llegue |
| Nombrada variable | `def f(**kw)` | Un diccionario con lo nombrado |

Los dos últimos ya salieron en la semana 5, con el carrito. Aquí falta una que ordena mucho una firma
larga.
"""),

code("""
def transferir(monto, *, origen, destino, notificar=False):
    \"\"\"El asterisco solo obliga a que todo lo de después vaya por nombre.\"\"\"
    aviso = " (con aviso)" if notificar else ""
    return f"${monto:,.2f} de {origen} a {destino}{aviso}"


print(transferir(1500, origen="ahorro", destino="nómina"))
print(transferir(2000, origen="nómina", destino="ahorro", notificar=True))

try:
    transferir(1500, "ahorro", "nómina")
except TypeError as e:
    print()
    print("TypeError:", e)
"""),

md("""
El asterisco suelto en la firma no recoge nada: **marca dónde terminan los posicionales**.

Aquí eso importa porque `origen` y `destino` son dos cadenas del mismo tipo, y confundirlas manda el
dinero al revés sin ningún error. Obligar a escribir el nombre convierte una transferencia invertida en
un `TypeError`.

Ese mismo problema, sin el asterisco, se ve así.
"""),

code("""
# FALLA A PROPÓSITO, y no truena. Booleanos posicionales en la llamada.
def enviar_reporte(destinatario, incluir_detalle, mandar_copia, comprimir):
    partes = []
    if incluir_detalle:
        partes.append("con detalle")
    if mandar_copia:
        partes.append("con copia")
    if comprimir:
        partes.append("comprimido")
    return f"{destinatario}: " + (", ".join(partes) if partes else "básico")


print(enviar_reporte("ana@up.edu.mx", True, False, True))
print(enviar_reporte("ana@up.edu.mx", True, True, False))     # ¿cuál es cuál?
print()
print("Las dos llamadas son legales y hacen cosas distintas.")
print("Leyendo solo la llamada, no hay manera de saber cuál es cuál.")
print()
print("Con nombre:")
print(enviar_reporte("ana@up.edu.mx", incluir_detalle=True,
                     mandar_copia=True, comprimir=False))
"""),

md("""
`f(True, False, True)` no dice absolutamente nada al leerlo, y las dos primeras llamadas de la celda
podrían estar invertidas sin que nadie lo notara en una revisión de código.

Es el error 04 de la diapositiva. La corrección tiene dos niveles: escribir los nombres en la llamada, o
mejor, ponerle un `*` a la firma para que el lenguaje los exija.

## Una función que se le pasa a otra función
"""),

code("""
productos = [("Teclado", 890), ("Monitor", 4200), ("Mouse", 350), ("Webcam", 890)]

por_defecto = sorted(productos)
por_precio = sorted(productos, key=lambda p: p[1])
por_precio_desc = sorted(productos, key=lambda p: p[1], reverse=True)
por_nombre_largo = sorted(productos, key=lambda p: len(p[0]))

print("Sin key:        ", [p[0] for p in por_defecto])
print("Por precio:     ", [p[0] for p in por_precio])
print("Por precio desc:", [p[0] for p in por_precio_desc])
print("Por largo:      ", [p[0] for p in por_nombre_largo])
print()
print("El más barato:", por_precio[0])
print("¿Los dos de 890 conservaron su orden original?",
      [p[0] for p in por_precio if p[1] == 890] == ["Teclado", "Webcam"])
"""),

md("""
`key` recibe **una función**, no un valor. `sorted` la llama una vez por elemento y ordena por lo que
devuelva.

Sin `key`, `sorted` compara las tuplas completas de izquierda a derecha, así que ordena por nombre. Con
`key=lambda p: p[1]` compara solo el precio.

La última línea comprueba algo que se usa más de lo que se nombra: el orden de Python es **estable**. Dos
elementos con la misma clave conservan el orden en el que venían, y por eso se puede ordenar por un
criterio y luego por otro para tener desempates.

`lambda` es una función anónima de una sola expresión. No trae nada que `def` no tenga, y cuando el
cálculo no cabe cómodo en una línea, `def` con un nombre propio se lee mejor.
"""),

code("""
# FALLA A PROPÓSITO, y no truena. Ordenar sin decir por cuál campo.
alumnos = [("Robles", 9.2), ("Ferrer", 7.8), ("Ines", 9.5), ("Duarte", 6.4)]

ranking_malo = sorted(alumnos, reverse=True)
ranking_bueno = sorted(alumnos, key=lambda a: a[1], reverse=True)

print("Ranking sin key:", [a[0] for a in ranking_malo])
print("Ranking con key:", [a[0] for a in ranking_bueno])
print()
print("Primer lugar según el primero:", ranking_malo[0])
print("Primer lugar según el segundo:", ranking_bueno[0])
print("¿Coinciden los dos rankings?", ranking_malo == ranking_bueno)
"""),

md("""
El primer lugar del ranking sin `key` es Robles, que tiene 9.2, y el verdadero es Ines con 9.5.

`sorted` ordenó por apellido descendente y el resultado se ve como un ranking perfectamente
respetable: cuatro alumnos, en orden, sin errores. Solo está mal.

Es el mismo error de las listas paralelas de la semana 2 y del `sort` del cuaderno de la semana 2: **una
salida ordenada no es una salida correcta**.

## La `lambda` que se lleva la variable y no su valor
"""),

code("""
# FALLA A PROPÓSITO, y no truena. Tres funciones que resultaron ser la misma.
multiplicadores = []
for factor in [2, 3, 10]:
    multiplicadores.append(lambda x: x * factor)

print("Esperábamos 5*2, 5*3 y 5*10:")
print(" ", [f(5) for f in multiplicadores])
print()
print("Valor final de factor:", factor)
print()

buenos = []
for factor in [2, 3, 10]:
    buenos.append(lambda x, f=factor: x * f)      # el valor se captura al definir

print("Capturando el valor:")
print(" ", [f(5) for f in buenos])
"""),

md("""
Tres funciones que deberían multiplicar por 2, por 3 y por 10, y las tres multiplican por 10.

Una `lambda` definida dentro de un ciclo **no se guarda el valor de la variable, se guarda la variable**.
Cuando alguien las llama, el ciclo ya terminó y `factor` vale lo último que valió.

Es el alcance del repaso 3 visto desde el otro lado: ahí el problema era que asignar dentro de una
función creaba una variable local; aquí el problema es que **no** hay variable local y la lambda alcanza
la de afuera.

La corrección de la segunda mitad usa el mecanismo de hace tres celdas, y esta vez a favor: un parámetro
con valor por omisión se evalúa al definir la función, así que `f=factor` captura el valor de ese
momento.

El mismo error aparece con `key`, con los manejadores de eventos de la semana 14 y con cualquier función
que se guarde para llamarla después.
"""),

md("""
---
# Bloque 2 · Modularidad

Una función hace una sola cosa y su nombre la describe entera.

**La prueba del nombre.** Si no puedes nombrarla sin decir la palabra "y", todavía hace de más.

**La prueba del tamaño.** Si no cabe en una pantalla sin bajar, hay algo adentro que quiere salir.

**La prueba del retorno.** Una función que devuelve un valor y además imprime está haciendo dos
trabajos.
"""),

code("""
# FALLA A PROPÓSITO, y no truena. La función que calcula e imprime.
def procesar(alumnos):
    total = 0
    for a in alumnos:
        total += a["nota"]
    print(f"Promedio: {total / len(alumnos):.2f}")


GRUPO = [{"nombre": "Ana", "nota": 9.2}, {"nombre": "Luis", "nota": 7.8},
         {"nombre": "Sofía", "nota": 9.5}]

resultado = procesar(GRUPO)

print()
print("Lo que devolvió:", resultado)
print("Tipo:", type(resultado).__name__)
print()
print("¿Se puede comparar contra el promedio esperado?")
try:
    print("  ", round(resultado, 2) == 8.83)
except TypeError as e:
    print("   TypeError:", e)
"""),

md("""
El promedio salió bien en la pantalla y la función devolvió `None`.

Esa es toda la diferencia entre calcular e imprimir. Un número que solo existe en la consola no se puede
comparar, no se puede sumar, no se puede escribir en un archivo y no se puede probar. Es la frase que
lleva desde el repaso 3 apareciendo, y aquí llega a su forma final: **una función que imprime sirve una
vez; una que devuelve sirve en cualquier parte.**
"""),

code("""
def promedio(notas):
    return sum(notas) / len(notas)


def notas_de(alumnos):
    return [a["nota"] for a in alumnos]


def aprobados(alumnos, minimo=8.0):
    return [a for a in alumnos if a["nota"] >= minimo]


def linea_de_reporte(alumnos):
    return (f"{len(alumnos)} alumnos · promedio {promedio(notas_de(alumnos)):.2f} · "
            f"{len(aprobados(alumnos))} aprobados")


print(linea_de_reporte(GRUPO))
print()
print("Y ahora sí se puede probar sin mirar la pantalla:")
print("  promedio correcto:", abs(promedio(notas_de(GRUPO)) - 8.833333) < 0.001)
print("  aprobados correctos:", [a["nombre"] for a in aprobados(GRUPO)])
print("  con otro mínimo:   ", [a["nombre"] for a in aprobados(GRUPO, 7.0)])
print()
PRUEBAS = [(promedio, [1, 2, 3]), (notas_de, GRUPO), (aprobados, GRUPO),
           (linea_de_reporte, GRUPO)]
for f, argumento in PRUEBAS:
    devuelve_algo = f(argumento) is not None
    lleva_y = "_y_" in f.__name__
    print(f"  {f.__name__:<18}devuelve un valor: {devuelve_algo}   "
          f"el nombre lleva 'y': {lleva_y}")
"""),

md("""
Cuatro funciones, ninguna con la palabra "y" en el nombre, y las tres primeras devuelven sin imprimir.

`linea_de_reporte` sí arma texto, y aun así devuelve en lugar de imprimir. Esa decisión es la que permite
que mañana el reporte se escriba en un archivo sin tocar nada.

Fíjate en `aprobados(alumnos, minimo=8.0)`. El mínimo salió a la firma con un valor por omisión, así que
la función sirve para la regla de hoy y para la que ponga la coordinación el semestre que viene.

## La variable global que comunica funciones
"""),

code("""
# FALLA A PROPÓSITO, y no truena. Dos funciones que se hablan por una global.
total_acumulado = 0


def sumar_ventas(montos):
    global total_acumulado
    for m in montos:
        total_acumulado += m


def aplicar_descuento(porcentaje):
    global total_acumulado
    total_acumulado *= (1 - porcentaje / 100)


sumar_ventas([100, 200, 300])
aplicar_descuento(10)
sumar_ventas([400])

print("Total:", round(total_acumulado, 2))

total_acumulado = 0
sumar_ventas([100, 200, 300])
sumar_ventas([400])
aplicar_descuento(10)

print("Los mismos datos, otro orden:", round(total_acumulado, 2))
print()
print("¿Da lo mismo?", round(940.0, 2) == round(900.0, 2))
"""),

md("""
Los mismos datos, las mismas operaciones, dos resultados.

Cuando dos funciones se comunican por una variable global, el resultado depende del orden en que
alguien las llamó, y ese orden no aparece en ninguna firma. Para saber qué hace `aplicar_descuento` hay
que saber quién tocó `total_acumulado` antes, y eso está repartido por todo el archivo.

Es el error 02 de la diapositiva, y es el mismo problema del estado compartido de la semana 6 sin
siquiera la ventaja de tener una clase que lo agrupe.

La corrección: **que los datos entren por parámetros y salgan por el `return`**.
"""),

code("""
def total_de(montos):
    return sum(montos)


def con_descuento(total, porcentaje):
    return total * (1 - porcentaje / 100)


print("Descuento al final:", round(con_descuento(total_de([100, 200, 300, 400]), 10), 2))
print("Descuento a la mitad:",
      round(total_de([400]) + con_descuento(total_de([100, 200, 300]), 10), 2))
print()
print("Los dos resultados siguen siendo distintos, y ahora la línea dice por qué.")
"""),

md("""
Las dos cuentas siguen dando distinto, porque de verdad son cuentas distintas. La diferencia es que
ahora se ve en la línea que las escribe, y no hay que buscar en el archivo quién tocó qué.

**Una función que solo depende de sus parámetros se puede leer sin leer nada más.** Ese es el criterio
completo de este bloque.
"""),

md("""
---
# Bloque 3 · Recursividad

Una función que se llama a sí misma con un problema más chico, hasta que el problema es tan chico que ya
no hay nada que hacer.

Toda recursión necesita dos piezas: **el caso base** que corta, y **la llamada que se acerca a él**.
"""),

code("""
import sys


def factorial(n: int) -> int:
    if n <= 1:                   # caso base
        return 1
    return n * factorial(n - 1)  # se acerca al caso base


for n in [0, 1, 4, 10]:
    print(f"  factorial({n:>2}) = {factorial(n)}")

print()
print("Límite de llamadas de esta sesión:", sys.getrecursionlimit())
"""),

code("""
# FALLA A PROPÓSITO. Sin caso base, la pila se acaba.
def sin_freno(n):
    return n + sin_freno(n - 1)      # nunca deja de llamarse


try:
    sin_freno(10)
except RecursionError as e:
    print("RecursionError:", str(e)[:60])

print()


def con_freno_mal(n):
    if n == 0:
        return 0
    return n + con_freno_mal(n - 2)  # de dos en dos, desde un impar


print("Con n par:", con_freno_mal(10))
try:
    con_freno_mal(9)
except RecursionError as e:
    print("Con n impar:", type(e).__name__)
"""),

md("""
Los dos casos son el mismo error con distinta cara.

El primero no tiene caso base. El segundo lo tiene y **nunca lo alcanza** cuando arranca en un número
impar, porque baja de dos en dos y pasa de largo por el cero.

Escribir `if n <= 0` en lugar de `if n == 0` habría cerrado ese hueco. **El caso base tiene que atrapar
todo lo que quede por debajo, no un valor exacto.**

## Predice antes de correr

```python
def cuenta(n):
    if n == 0:
        return 0
    return n + cuenta(n - 1)


print(cuenta(3))
```

- **A.** 6, porque suma 3 más 2 más 1 más 0.
- **B.** 3, porque solo cuenta la primera llamada.
- **C.** 0, porque el caso base devuelve cero.
- **D.** `RecursionError`, la función no tiene caso base.
"""),

code("""
PROFUNDIDAD = []


def cuenta(n, nivel=0):
    PROFUNDIDAD.append(nivel)
    print(f"{'  ' * nivel}cuenta({n}) llamada, marcos abiertos: {nivel + 1}")
    if n == 0:
        print(f"{'  ' * nivel}cuenta(0) devuelve 0")
        return 0
    resultado = n + cuenta(n - 1, nivel + 1)
    print(f"{'  ' * nivel}cuenta({n}) devuelve {resultado}")
    return resultado


print("Resultado:", cuenta(3))
print()
print("Marcos que llegaron a estar abiertos a la vez:", max(PROFUNDIDAD) + 1)
print("Llamadas en total:", len(PROFUNDIDAD))
"""),

md("""
La respuesta es **A**.

La sangría de la salida es la pila. Baja hasta el caso base abriendo un marco por llamada, y ahí se da
la vuelta: el cero se devuelve primero, después el uno, después el tres y al final el seis.

Ninguna llamada de en medio conoce el resultado final. Cada una sabe hacer una sola cosa: sumarle `n` a
lo que le devuelva la siguiente.

## Lo que cuesta una recursión mal armada
"""),

code("""
# FALLA A PROPÓSITO, y no truena. La recursión que recalcula lo que ya sabía.
LLAMADAS = {"ingenua": 0, "con_memoria": 0}


def fib(n):
    LLAMADAS["ingenua"] += 1
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)


def fib_memo(n, memoria={}):
    LLAMADAS["con_memoria"] += 1
    if n < 2:
        return n
    if n not in memoria:
        memoria[n] = fib_memo(n - 1, memoria) + fib_memo(n - 2, memoria)
    return memoria[n]


for n in [10, 20, 25]:
    LLAMADAS["ingenua"] = LLAMADAS["con_memoria"] = 0
    a, b = fib(n), fib_memo(n, {})
    print(f"  fib({n}) = {a:<7} ingenua: {LLAMADAS['ingenua']:>7} llamadas   "
          f"con memoria: {LLAMADAS['con_memoria']:>3}")

print()
print("Las dos versiones dan el mismo número. Lo que cambia es cuántas veces lo calculan.")
"""),

md("""
Para `fib(25)` la versión ingenua hace más de doscientas mil llamadas y la que recuerda hace menos de
cincuenta.

Las dos son correctas. Ninguna truena. La diferencia es que la primera vuelve a calcular `fib(20)` miles
de veces, porque cada rama del árbol de llamadas ignora lo que descubrieron las otras.

Fíjate en la firma de `fib_memo`: usa un diccionario como valor por omisión, que es exactamente el error
del bloque 1. Aquí está a propósito y por eso las llamadas de arriba le pasan un diccionario nuevo cada
vez; si no lo hicieran, la memoria se compartiría entre llamadas y los conteos saldrían mal. Un valor por
omisión mutable como caché es de los poquísimos casos donde alguien lo usa a sabiendas, y aun así conviene
escribirlo con `None` y una línea más.

## Las torres de Hanói

El proyecto `07 - Activities/Projects/02 - Hanoi Tower/hanoi_tower.py` resuelve el rompecabezas con seis
líneas de recursión. El archivo completo no corre en un cuaderno porque pide el número de discos con
`input()` y limpia la consola con `os.system("cls")`; el algoritmo, que son sus dos funciones de en
medio, va aquí tal cual.
"""),

code("""
MOVIMIENTOS = []


def mover_disco(n, origen, destino):
    disco = "*" * n
    MOVIMIENTOS.append((n, origen, destino))
    print(f"  Mueve el disco {disco:<4} de {origen} a {destino}")


def hanoi(n, origen, destino, auxiliar):
    if n == 0:                                   # caso base: nada que mover
        return
    hanoi(n - 1, origen, auxiliar, destino)
    mover_disco(n, origen, destino)
    hanoi(n - 1, auxiliar, destino, origen)


hanoi(3, "A", "C", "B")

print()
print("Movimientos con 3 discos:", len(MOVIMIENTOS))
print("2**3 - 1 =", 2 ** 3 - 1)
"""),

code("""
def mover_disco(n, origen, destino):              # ahora solo cuenta, sin imprimir
    MOVIMIENTOS.append((n, origen, destino))


print(f"{'discos':>7}{'movimientos':>14}{'2^n - 1':>10}{'iguales':>10}")
for n in range(1, 11):
    MOVIMIENTOS.clear()
    hanoi(n, "A", "C", "B")
    print(f"{n:>7}{len(MOVIMIENTOS):>14}{2 ** n - 1:>10}"
          f"{str(len(MOVIMIENTOS) == 2 ** n - 1):>10}")

print()
print("Con 20 discos serían", f"{2 ** 20 - 1:,}", "movimientos.")
print("Con 64, que es la leyenda original:", f"{2 ** 64 - 1:,}")
"""),

md("""
Tres discos son siete movimientos, diez discos son mil veintitrés, y la fórmula es exactamente
`2**n - 1`.

Eso no es una casualidad del código, sale de la estructura de la recursión: resolver `n` discos cuesta
dos veces resolver `n - 1` más un movimiento. `T(n) = 2·T(n-1) + 1`, y esa relación da `2**n - 1`.

La leyenda dice que unos monjes mueven sesenta y cuatro discos a razón de uno por segundo. Con el número
de arriba, eso son más de quinientos mil millones de años.

**Lo que hay que llevarse: una recursión con dos llamadas por nivel duplica el trabajo en cada nivel.**
Saber contar eso antes de correr el programa es la mitad de lo que esta semana enseña.
"""),

md("""
---
## Cuatro errores de esta sesión

**El valor por omisión mutable.** Se crea una sola vez, al leer el `def`, y todas las llamadas escriben
en él. Vale para listas, diccionarios, fechas y cualquier llamada a función que pongas ahí.

**La `lambda` dentro de un ciclo.** Se lleva la variable, no su valor, y todas terminan viendo el último.
Se arregla con un parámetro con valor por omisión.

**`global` para comunicar funciones.** El resultado depende del orden de las llamadas y ese orden no
aparece en ninguna firma.

**Ordenar sin decir por cuál campo.** `sorted` sobre tuplas ordena por el primer elemento, y el resultado
se ve como un ranking correcto.
"""),

md("""
---
# Ejercicios

El laboratorio de esta semana es partir un script de cincuenta líneas en funciones. Los ejercicios
construyen hacia eso.

Las soluciones están hasta abajo del cuaderno.

### Ejercicio 1 · La firma

Escribe una función con un parámetro posicional, uno con valor por omisión y uno que se exija por nombre
con `*`. Llámala de cuatro maneras distintas y atrapa el `TypeError` de la quinta.

Imprime `__defaults__` y explica en un comentario qué contiene.

### Ejercicio 2 · La lista que crece

Escribe una función con una lista como valor por omisión y llámala tres veces. Demuestra con `is` que las
tres llamadas comparten la lista de `__defaults__`.

Arréglala con `None` y repite las tres llamadas.

### Ejercicio 3 · La omisión congelada

Escribe una función cuyo valor por omisión sea el resultado de otra función, por ejemplo un contador o la
hora. Llámala tres veces y muestra que el valor no cambia.

Explica en un comentario en qué momento se calculó.

### Ejercicio 4 · Ordenar por lo que toca

Toma una lista de tuplas con nombre y calificación. Ordénala sin `key` y con `key`, e imprime los dos
primeros lugares de cada versión.

Después ordénala por dos criterios, primero por calificación y luego por nombre para los empates.

### Ejercicio 5 · La lambda del ciclo

Crea tres funciones dentro de un ciclo con `lambda`, guárdalas en una lista y llámalas después.
Demuestra que las tres hacen lo mismo, y arréglalo.

### Ejercicio 6 · Calcular contra imprimir

Escribe una función que calcule un promedio e imprima el resultado, y guarda lo que devuelve en una
variable. Muestra que es `None`.

Sepárala en dos y comprueba el número con una comparación.

### Ejercicio 7 · Sin globales

Escribe dos funciones que se comuniquen por una variable global y muestra que el resultado cambia si
inviertes el orden de las llamadas. Reescríbelas pasando y devolviendo los datos.

### Ejercicio 8 · Recursión con caso base

Escribe una función recursiva que sume los dígitos de un número. Prueba con cero, con un dígito y con
seis dígitos.

Después escribe a propósito una versión cuyo caso base no se alcance y atrapa el `RecursionError`.

### Ejercicio 9 · El laboratorio

Te entregan un script de cincuenta líneas que lee notas, saca el promedio, cuenta aprobados e imprime un
reporte, todo seguido. Pártelo en funciones con un solo trabajo cada una.

Ninguna función pasa de quince líneas, y ninguna calcula e imprime al mismo tiempo. Entrega un archivo
`.py` con las funciones y un bloque principal que las llama en orden.

El criterio es que el nombre de cada función se pueda decir completo sin usar la palabra "y".
"""),

md("""
---
## Tres ideas para llevarse

**El valor por omisión se evalúa al definir la función.** Una sola vez, cuando Python lee el `def`. Por
eso la lista crece, el folio se congela y la fecha se queda en la hora del arranque.

**Una función, una razón para cambiar.** Si el nombre necesita una conjunción, adentro hay dos funciones
esperando a que las separen. Y si calcula e imprime, ya son dos.

**Toda recursión necesita un caso base y una llamada que se acerque a él.** El caso base atrapa todo lo
que quede por debajo, no un valor exacto, y conviene saber cuánto va a costar antes de correrla.

La semana 10 sigue con colecciones: cuatro maneras de guardar varias cosas en una variable, cómo crece
una lista por dentro, y qué se puede hacer sin tocar el disco.
"""),

md("""
---
# Soluciones

### Ejercicio 1

```python
def inscribir(matricula, grupo="01", *, activo=True, beca=False):
    return f"{matricula} grupo {grupo} activo={activo} beca={beca}"


print(inscribir("A001"))
print(inscribir("A002", "02"))
print(inscribir("A003", activo=False))
print(inscribir("A004", "03", beca=True))

try:
    inscribir("A005", "04", False)
except TypeError as e:
    print("TypeError:", e)

print(inscribir.__defaults__)
print(inscribir.__kwdefaults__)

# __defaults__ trae solo los de los parámetros posicionales, en este caso ("01",).
# Los que van después del asterisco viven aparte, en __kwdefaults__.
```

### Ejercicio 2

```python
def apuntar(nombre, lista=[]):
    lista.append(nombre)
    return lista


print(apuntar("Ana"))
print(apuntar("Luis"))
print(apuntar("Sofía"))
print("La lista de la firma:", apuntar.__defaults__[0])
print("¿La misma?", apuntar.__defaults__[0] is apuntar("Marco"))


def apuntar_bien(nombre, lista=None):
    lista = [] if lista is None else list(lista)
    lista.append(nombre)
    return lista


print(apuntar_bien("Ana"))
print(apuntar_bien("Luis"))
print(apuntar_bien("Sofía"))
```

### Ejercicio 3

```python
CONTADOR = [0]


def siguiente():
    CONTADOR[0] += 1
    return CONTADOR[0]


def etiquetar(texto, numero=siguiente()):
    return f"#{numero} {texto}"


print(etiquetar("uno"))
print(etiquetar("dos"))
print(etiquetar("tres"))
print("Veces que corrió siguiente():", CONTADOR[0])

# Se calculó una sola vez, mientras Python leía el def, antes de la primera
# llamada. El contador quedó en 1 y las tres etiquetas comparten ese número.
```

### Ejercicio 4

```python
alumnos = [("Robles", 9.2), ("Ferrer", 7.8), ("Ines", 9.5), ("Duarte", 9.2)]

sin_key = sorted(alumnos, reverse=True)
con_key = sorted(alumnos, key=lambda a: a[1], reverse=True)

print("Sin key:", sin_key[:2])
print("Con key:", con_key[:2])

dos_criterios = sorted(alumnos, key=lambda a: (-a[1], a[0]))
print("Por nota y desempate por nombre:", dos_criterios)

# El menos delante de la nota la ordena de mayor a menor sin invertir el nombre,
# que es el truco de siempre para mezclar dos direcciones en una sola clave.
```

### Ejercicio 5

```python
funciones = []
for etiqueta in ["a", "b", "c"]:
    funciones.append(lambda: etiqueta)

print([f() for f in funciones])

buenas = []
for etiqueta in ["a", "b", "c"]:
    buenas.append(lambda e=etiqueta: e)

print([f() for f in buenas])
```

### Ejercicio 6

```python
def reportar(notas):
    print(f"Promedio: {sum(notas) / len(notas):.2f}")


devuelto = reportar([9.2, 7.8, 9.5])
print("Devolvió:", devuelto)


def promedio(notas):
    return sum(notas) / len(notas)


valor = promedio([9.2, 7.8, 9.5])
print(f"Promedio: {valor:.2f}")
print("¿Es el esperado?", abs(valor - 8.8333) < 0.001)
```

### Ejercicio 7

```python
saldo = 0


def depositar(monto):
    global saldo
    saldo += monto


def cobrar_comision(pesos):
    global saldo
    saldo -= pesos


depositar(1000)
cobrar_comision(50)
depositar(500)
print("Orden A:", saldo)

saldo = 0
depositar(1000)
depositar(500)
cobrar_comision(50)
print("Orden B:", saldo)


def con_deposito(saldo, monto):
    return saldo + monto


def con_comision(saldo, pesos):
    return saldo - pesos


print("Sin globales:", con_comision(con_deposito(con_deposito(0, 1000), 500), 50))
```

### Ejercicio 8

```python
def suma_digitos(n):
    if n < 10:
        return n
    return n % 10 + suma_digitos(n // 10)


for n in [0, 7, 942817]:
    print(f"suma_digitos({n}) = {suma_digitos(n)}")


def suma_rota(n):
    if n == 0:
        return 0
    return n % 10 + suma_rota(n // 10 - 1)     # se pasa del cero


try:
    suma_rota(942817)
except RecursionError as e:
    print("RecursionError:", str(e)[:50])
```

### Ejercicio 9

```python
def leer_notas(texto):
    \"\"\"Del texto crudo a una lista de pares.\"\"\"
    alumnos = []
    for linea in texto.strip().splitlines():
        nombre, nota = linea.split(",")
        alumnos.append((nombre.strip(), float(nota)))
    return alumnos


def promedio(notas):
    return sum(notas) / len(notas)


def aprobados(alumnos, minimo=8.0):
    return [a for a in alumnos if a[1] >= minimo]


def mejor(alumnos):
    return max(alumnos, key=lambda a: a[1])


def lineas_del_reporte(alumnos, minimo=8.0):
    notas = [a[1] for a in alumnos]
    return [
        f"Alumnos: {len(alumnos)}",
        f"Promedio: {promedio(notas):.2f}",
        f"Aprobados: {len(aprobados(alumnos, minimo))} de {len(alumnos)}",
        f"Mejor nota: {mejor(alumnos)[0]} con {mejor(alumnos)[1]}",
    ]


def imprimir(lineas):
    for linea in lineas:
        print(linea)


CRUDO = \"\"\"
Ana Robles, 9.2
Luis Ferrer, 7.8
Sofia Ines, 9.5
Marco Duarte, 6.4
\"\"\"

if __name__ == "__main__":
    grupo = leer_notas(CRUDO)
    imprimir(lineas_del_reporte(grupo))
```

Tres decisiones que vale la pena defender en la entrega.

**`leer_notas` devuelve datos y no imprime nada.** Con eso el reporte se puede probar con una lista
escrita a mano, sin archivo y sin consola.

**`lineas_del_reporte` devuelve una lista de textos y no los imprime.** Imprimir es trabajo de
`imprimir`, y por eso el mismo reporte puede irse a un archivo la semana 12 sin tocar una línea.

**Ninguno de los nombres necesita la palabra "y".** `leer_notas`, `promedio`, `aprobados`, `mejor`,
`lineas_del_reporte`, `imprimir`. Si alguno hubiera quedado como `leer_y_promediar`, ahí había dos
funciones.
"""),

]

write(OUT / "es" / "w09.ipynb", es)
print("wrote", OUT / "es" / "w09.ipynb")
