"""notebooks/programacion-orientada-a-objetos/es/w11.ipynb

Source deck: ppts/python/programacion-orientada-a-objetos/es/w11.es.yaml
Source code:  docs/en/courses/python-course/03 - Paths and Files/7th Module/Code035.py
                  (try/except con archivos, el except Exception del final)
              docs/en/courses/python-course/02 - POO/6th Module/Code026.py
                  (InvalidOperationError: la excepción propia del repositorio)
              docs/en/courses/python-course/07 - Activities/Projects/
                  01 - Login System/login_multiple_users.py
                  (los dos try del menú de edición)

Code035.py corre completo desde cualquier directorio y siempre imprime las dos
mismas líneas, comprobado. Sus dos rutas apuntan a archivos que no existen, así
que las dos ramas de error son las que corren.

Code026.py corre completo, comprobado. Ya salió en las semanas 7 y 8 por la
jerarquía y por ABC; aquí se cita solo por su excepción propia.

login_multiple_users.py no corre headless: cada menú llama a input() y a
os.system("cls"). Se citan dos de sus funciones, sin la plomería de consola, y
el cuaderno lo dice.

Bug del repositorio que este cuaderno enseña como trampa, medido:

  login_multiple_users.py, edit_user_by_index_menu, líneas 80 a 90. El índice se
  lee con int(input(...)) y se le resta uno, y el try solo atrapa IndexError.
  Teclear 0 deja index en -1, que es un índice válido en Python: la contraseña
  que se cambia es la del último usuario de la lista, no hay excepción, y el
  programa imprime "User edited". Comprobado.

La semana 10 cerró apuntando aquí: seis de sus celdas atraparon un error con try
y except sin explicar la sintaxis. Este cuaderno la explica y cierra apuntando a
los archivos de la semana 12.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from nbkit import md, code, write, REPO

OUT = REPO / "notebooks" / "programacion-orientada-a-objetos"

es = [

md("""
# Programación Orientada a Objetos · Semana 11
## Tema 4 · Funciones y estructuras avanzadas

**COM102 · Facultad de Ingeniería · Profesor David Escobar-Castillejos**

Qué hace un programa cuando algo sale mal, dónde se revisan los datos que entran, y cómo aguantar lo no
previsto.

La semana pasada, seis celdas atraparon un error con `try` y `except` sin explicar la sintaxis: el
`append` que recibía tres argumentos, el `pop` de la pila vacía y el `array` que no acepta cadenas,
entre otras. Aquí se explica qué era eso.

Al terminar vas a poder:

1. Leer un traceback completo, de abajo hacia arriba, y decir en qué línea empezó el problema.
2. Atrapar por tipo, con un `except` por cada error que sabes atender y ninguno que atrape lo que no
   esperabas.
3. Decir cuál de las cuatro cláusulas corre en cada caso y en qué orden.
4. Elegir dónde validar, y explicar por qué la frontera vale más que veinte revisiones repartidas.
5. Definir una excepción propia con el nombre del problema y un mensaje que diga qué corregir.

### Cómo se usa este cuaderno

Ejecuta las celdas en orden con **Shift + Enter**. Once fallan a propósito y llevan un comentario que lo
dice.

Nueve de las once **no lanzan ninguna excepción**, que en un cuaderno sobre excepciones es exactamente el
punto: las peores no truenan, se tragan la que sí importaba. Una de esas nueve es un bug real del
repositorio que lleva años sin dispararse.
"""),

md("""
---
# Bloque 1 · Manejo de excepciones

Una excepción es un objeto que Python crea cuando algo sale mal y lanza hacia arriba, buscando quién lo
atienda.

Si nadie lo atrapa en toda la cadena de llamadas, el programa termina e imprime el rastro de por dónde
pasó antes de rendirse. Ese rastro es el traceback, y leerlo bien es la mitad del trabajo.
"""),

code("""
import traceback
from pathlib import Path


def leer_promedio(texto):
    return promediar(partir(texto))


def partir(texto):
    return [float(x) for x in texto.split(",")]


def promediar(numeros):
    return sum(numeros) / len(numeros)


print("Con datos buenos:", leer_promedio("9.2, 7.8, 9.5"))
print()

try:
    leer_promedio("9.2, siete coma ocho, 9.5")
except ValueError as e:
    print(traceback.format_exc())
"""),

code("""
try:
    leer_promedio("9.2, siete coma ocho, 9.5")
except ValueError as e:
    marcos = traceback.extract_tb(e.__traceback__)
    tipo, mensaje = type(e).__name__, str(e)

print("Tipo:   ", tipo)
print("Mensaje:", mensaje)
print()
print("Los marcos, en el orden en que Python los imprime:")
for i, m in enumerate(marcos):
    print(f"  {i}  en {m.name:<16}{m.line}")

print()
print("El primero es dónde empezó la llamada:", marcos[0].name)
print("El último es dónde reventó:           ", marcos[-1].name, "->", marcos[-1].line)
"""),

md("""
Un traceback se lee **de abajo hacia arriba**.

La última línea trae el tipo y el mensaje, que es lo que de verdad estás buscando. El marco inmediato
anterior es la línea que falló. Los de más arriba son el camino que se recorrió para llegar ahí, y
sirven cuando la línea que falló es correcta y quien la llamó no lo era.

En esta cadena el error no está en `float`, que hizo su trabajo. Está en que alguien le dio a `partir`
un texto que no traía tres números, y eso solo se ve subiendo.

## Un `except` por tipo
"""),

code("""
# FALLA A PROPÓSITO. Dos errores distintos piden dos respuestas distintas.
def edad_a_factor(valor):
    try:
        edad = int(valor)
        return 10 / edad
    except ValueError:
        return "Eso no es un número entero"
    except ZeroDivisionError:
        return "La edad no puede ser cero"


for valor in ["abc", "0", "20", "  7 "]:
    print(f"  {valor!r:<8}-> {edad_a_factor(valor)}")

print()
print("Los dos errores heredan de Exception:")
for tipo in [ValueError, ZeroDivisionError]:
    print(f"  {tipo.__name__:<20}{[c.__name__ for c in tipo.__mro__[:-1]]}")
"""),

md("""
Cuatro entradas, tres caminos, y `"  7 "` con espacios entra igual porque `int` los recorta.

Corre el **primer** `except` cuyo tipo coincide, y los demás ni se revisan. Por eso el orden importa en
cuanto los tipos estén emparentados, que es la celda de más abajo.

Fíjate en el árbol de herencia impreso al final. `ZeroDivisionError` no cuelga directo de `Exception`:
pasa por `ArithmeticError`. Eso quiere decir que `except ArithmeticError` también lo atraparía, junto con
el desbordamiento y el error de punto flotante.

## Las cuatro cláusulas, y cuándo corre cada una
"""),

code("""
def intentar(valor):
    corrio = []
    try:
        corrio.append("try")
        numero = int(valor)
    except ValueError:
        corrio.append("except")
        numero = None
    else:
        corrio.append("else")
    finally:
        corrio.append("finally")
    return numero, corrio


print(f"{'entrada':<10}{'resultado':<12}{'cláusulas que corrieron'}")
for valor in ["7", "siete"]:
    numero, corrio = intentar(valor)
    print(f"{valor!r:<10}{str(numero):<12}{' -> '.join(corrio)}")

print()
print("El else corre solo cuando el try llegó al final sin tropezar.")
print("El finally corre en los dos casos.")
"""),

md("""
Dos entradas y la lista de lo que corrió en cada una.

`else` es el camino feliz. Va ahí lo que solo tiene sentido si el `try` salió bien, y la ventaja es que
deja el `try` con la línea riesgosa y nada más. Un `try` de una línea dice exactamente qué esperabas que
fallara.

`finally` corre siempre. Ahí va lo que hay que cerrar, pase lo que pase, y en la semana 12 va a ser el
lugar donde se cierra un archivo.

## Predice antes de correr

```python
def leer(valor):
    try:
        return int(valor)
    except ValueError:
        return 0
    finally:
        print("listo")


print(leer("7"))
```

- **A.** Primero `listo` y después `7`.
- **B.** Primero `7` y después `listo`.
- **C.** Solo `7`, porque el `return` se salta el `finally`.
- **D.** Solo `listo`, porque el `finally` descarta el `return`.
"""),

code("""
def leer(valor):
    try:
        print("  (el try calculó el valor de retorno)")
        return int(valor)
    except ValueError:
        return 0
    finally:
        print("  listo")


print("Llamando a leer('7'):")
resultado = leer("7")
print("Devolvió:", resultado)
"""),

md("""
La respuesta es **A**.

`return int(valor)` calcula el 7 y lo deja guardado, pero la función todavía no ha salido. `finally`
existe justamente para correr en ese hueco, entre "ya sé qué voy a devolver" y "ya salí". Por eso
`listo` aparece primero y el `7` se imprime después, cuando `print` de afuera recibe el valor.

Ese hueco tiene una consecuencia que casi nadie ve venir.

## El `finally` que se traga la excepción
"""),

code("""
# FALLA A PROPÓSITO, y no truena. Un return dentro del finally.
import warnings

FUENTE = '''
def guardar(dato):
    try:
        raise ValueError(f"{dato!r} no se pudo guardar")
    finally:
        return "guardado"
'''

with warnings.catch_warnings(record=True) as avisos:
    warnings.simplefilter("always")
    exec(compile(FUENTE, "<ejemplo>", "exec"), globals())

print("¿Esta versión de Python avisa al compilarlo?",
      "sí:" if avisos else "no", avisos[0].message if avisos else "")
print()
print("Lo que devuelve:", guardar("A001"))
print("Excepciones que llegaron a quien llamó: ninguna")
print()
print("Y el ValueError sí se levantó. Se puede ver quitando el return:")


def guardar_bien(dato):
    try:
        raise ValueError(f"{dato!r} no se pudo guardar")
    finally:
        print("  (el finally corrió igual)")


try:
    guardar_bien("A001")
except ValueError as e:
    print("  ValueError:", e)
"""),

md("""
La primera función levantó un `ValueError` y quien la llamó recibió la cadena `"guardado"`.

Un `return` dentro de `finally` **reemplaza lo que la función iba a hacer**, y lo que iba a hacer era
propagar la excepción. La excepción se levanta, el `finally` corre, el `return` gana, y el error
desaparece sin dejar rastro en ningún lado.

Es el error más silencioso de la sesión y el más difícil de encontrar después, porque el síntoma es que
un dato no se guardó y nadie tiene una sola línea de log que lo diga.

**En `finally` solo va lo que cierra recursos.** Ni `return`, ni `break`, ni `continue`.

## La variable que solo existe si no hubo error
"""),

code("""
# FALLA A PROPÓSITO. La variable se asigna dentro del try y se usa en el except.
def cargar(ruta):
    try:
        archivo = open(ruta, encoding="utf-8")
        return archivo.read()
    except FileNotFoundError:
        print("  No existe el archivo")
        return ""
    finally:
        archivo.close()          # archivo puede no haberse creado nunca


Path("existe.txt").write_text("hola", encoding="utf-8")
print("Con un archivo que existe:", repr(cargar("existe.txt")))

print()
print("Con uno que no existe:")
try:
    cargar("no_existe.txt")
except NameError as e:
    print("  NameError:", e)
    print("  <- y este error tapó al FileNotFoundError, que era el de verdad")
"""),

md("""
El archivo no existía, `open` lanzó `FileNotFoundError`, el `except` lo atendió, y el `finally` tumbó
todo con un `NameError` sobre una variable que nunca llegó a asignarse.

Es lo que la diapositiva anuncia como riesgo del `finally`, y tiene un agravante: **el error de la
limpieza sustituye al error original**. Quien lea el traceback va a ver un `NameError` sin ninguna
relación con la causa.

La corrección canónica es no escribir ese `finally`. El bloque `with` de la semana que entra cierra el
archivo solo, y solo si llegó a abrirse.

## El orden de los `except`
"""),

code("""
# FALLA A PROPÓSITO, y no truena. Un except general antes que el específico.
def leer_config(ruta):
    try:
        return Path(ruta).read_text(encoding="utf-8")
    except OSError:
        return "error de sistema operativo"
    except FileNotFoundError:
        return "el archivo no existe"


print("Ruta que no existe:", leer_config("no_existe.txt"))
print()
print("¿Por qué? Porque uno hereda del otro:")
print("  FileNotFoundError.__mro__:",
      [c.__name__ for c in FileNotFoundError.__mro__[:-1]])
print("  ¿FileNotFoundError es un OSError?",
      issubclass(FileNotFoundError, OSError))
print("  ¿IOError es el mismísimo objeto?", IOError is OSError)
print()


def leer_config_bien(ruta):
    try:
        return Path(ruta).read_text(encoding="utf-8")
    except FileNotFoundError:
        return "el archivo no existe"
    except OSError:
        return "error de sistema operativo"


print("Con el orden al derecho:", leer_config_bien("no_existe.txt"))
"""),

md("""
La segunda rama es inalcanzable y Python no dice nada.

`FileNotFoundError` hereda de `OSError`, así que el primer `except` coincide y el segundo nunca se
revisa. El mensaje que llega al usuario es el genérico, y el específico, que era el útil, quedó escrito
como decoración.

**Los `except` van de lo particular a lo general.** Es la misma regla del `elif`, y aquí no hay ninguna
advertencia que la recuerde.

`Code035.py`, en sus líneas 17 a 20, tiene el orden correcto: primero `FileNotFoundError` y después
`IOError`. Vale la pena saber que `IOError` **es** `OSError` desde Python 3.3, el mismo objeto con dos
nombres, y que por eso ese segundo `except` atrapa mucho más de lo que su nombre sugiere.
"""),

md("""
---
# Bloque 2 · Validación de errores

La diferencia entre un programa que se cae y uno que explica lo que hay que corregir cabe en dónde
pusiste la revisión.

Los cuatro errores de este bloque son los cuatro de la diapositiva, corridos.
"""),

code("""
# FALLA A PROPÓSITO, y no truena. Error 02: un except con pass adentro.
DATOS = [{"nombre": "Ana", "nota": "9.2"}, {"nombre": "Luis", "nota": "7,8"},
         {"nombre": "Sofía", "nota": "9.5"}]

notas = []
for fila in DATOS:
    try:
        notas.append(float(fila["nota"]))
    except Exception:
        pass

print("Filas de entrada:", len(DATOS))
print("Notas convertidas:", len(notas), notas)
print("Promedio:", round(sum(notas) / len(notas), 2))
print()
print("El promedio se ve razonable y le falta un alumno.")
print("Nadie sabe cuál, ni por qué, ni que faltó.")
print()

notas, rechazadas = [], []
for fila in DATOS:
    try:
        notas.append(float(fila["nota"]))
    except ValueError as e:
        rechazadas.append((fila["nombre"], fila["nota"], str(e)))

print("Con el except por tipo y sin pass:")
print("  convertidas:", len(notas))
for nombre, valor, motivo in rechazadas:
    print(f"  rechazada: {nombre} con {valor!r} -> {motivo}")
"""),

md("""
Tres filas entran, dos salen, y el promedio se calcula sobre las dos como si nada.

`except Exception: pass` es la instrucción de tirar el error a la basura. El programa sigue, el
resultado se ve plausible, y el dato que falta no aparece en ningún lado.

Fíjate en el arreglo: no basta con quitar el `pass`. Hay que **nombrar el tipo** y **guardar lo que se
rechazó**, porque una fila descartada es información, no ruido. La segunda mitad de la celda dice
exactamente qué fila se cayó y con qué valor, que es lo que alguien va a necesitar para corregir la
captura.

## El `except` que no dice de qué
"""),

code("""
# FALLA A PROPÓSITO, y no truena. Error 01: un except sin tipo se traga un typo.
def promediar(filas):
    try:
        total = 0
        for f in filas:
            total += float(f["nota"])
        return total / len(fillas)          # fillas, con dos eles
    except:                                  # noqa: E722
        return 0.0


print("Promedio:", promediar(DATOS[:1]))
print("El programa siguió con un promedio de cero y nadie escribió mal ningún dato.")
print()


def promediar_visible(filas):
    total = 0
    for f in filas:
        total += float(f["nota"])
    return total / len(fillas)


try:
    promediar_visible(DATOS[:1])
except NameError as e:
    print("Sin el except:", type(e).__name__ + ":", e)
"""),

md("""
El error no estaba en los datos. Estaba en el nombre de la variable, y el `except` sin tipo se lo tragó.

Un `except` desnudo atrapa **todo** lo que hereda de `BaseException`: los errores de programación como
este `NameError`, el `KeyboardInterrupt` de quien oprime Ctrl+C y el `SystemExit` de quien pide salir.
Ninguno de esos tres es un error que quisieras atender ahí.

Es el error 01 de la diapositiva, y su versión suave, `except Exception`, tiene el mismo problema con los
errores de programación: los convierte en un valor por omisión.

## Lo que un `except` desnudo atrapa de más
"""),

code("""
# FALLA A PROPÓSITO, y no truena. El except que impide salir del programa.
def salir_limpio():
    print("  cerrando...")
    raise SystemExit(0)


try:
    salir_limpio()
except:                                      # noqa: E722
    print("El except desnudo atrapó hasta la salida del programa.")

print()
try:
    raise KeyboardInterrupt()
except:                                      # noqa: E722
    print("Y también el Ctrl+C de quien lo estaba usando.")

print()
print("Ninguno de los dos hereda de Exception:")
for tipo in [SystemExit, KeyboardInterrupt, ValueError]:
    print(f"  {tipo.__name__:<20}¿hereda de Exception? {issubclass(tipo, Exception)}")

print()
print("Por eso except Exception ya es mucho mejor que un except pelón.")
print("Y un except por tipo sigue siendo mejor que los dos.")
"""),

md("""
El programa pidió salir y el `except` se lo impidió.

Ese es el argumento técnico contra el `except` desnudo, y no es un tecnicismo: en un programa con un
ciclo, un `except` así dentro del ciclo hace que Ctrl+C no funcione. La única forma de cerrarlo es matar
el proceso.

`SystemExit` y `KeyboardInterrupt` cuelgan de `BaseException` y no de `Exception` precisamente para que
`except Exception` no los toque. Ese diseño solo sirve si nadie escribe el `except` pelón.

## El `try` de cuarenta líneas
"""),

code("""
# FALLA A PROPÓSITO, y no truena. Error 03: un try alrededor de todo el trabajo.
CRUDO = "A001,Ana Robles,9.2\\nA002,Luis Ferrer,siete\\nA003,Sofía Ines,9.5"

try:
    filas = CRUDO.split("\\n")
    partidas = [f.split(",") for f in filas]
    matriculas = [p[0] for p in partidas]
    nombres = [p[1] for p in partidas]
    notas = [float(p[2]) for p in partidas]
    promedio = sum(notas) / len(notas)
    reporte = f"{len(matriculas)} alumnos, promedio {promedio:.2f}"
except ValueError:
    reporte = "hubo un problema con los datos"

print(reporte)
print("¿Cuál de las siete líneas falló? El mensaje no lo dice.")
print()

notas, problemas = [], []
for numero, linea in enumerate(CRUDO.split("\\n"), start=1):
    matricula, nombre, cruda = linea.split(",")
    try:
        notas.append(float(cruda))
    except ValueError as e:
        problemas.append(f"renglón {numero} ({matricula}): {cruda!r} no es un número")

print("Con el try alrededor de la línea riesgosa y nada más:")
print("  convertidas:", len(notas))
for p in problemas:
    print("  ", p)
"""),

md("""
Siete líneas dentro del `try` y un mensaje que no sirve para nada.

`except ValueError` atrapó el error de `float`, pero también habría atrapado un error de
desempaquetado, uno de conversión de la matrícula, y cualquier otro `ValueError` de las siete líneas.
Cuando salta, no sabes cuál falló.

**El `try` envuelve la línea riesgosa y nada más.** La segunda mitad convierte el mismo problema en un
mensaje que dice el renglón, la matrícula y el valor exacto que no se pudo leer, y sigue procesando los
demás.

## Excepciones para lo que pasa siempre
"""),

code("""
# FALLA A PROPÓSITO, y no truena. Error 04: excepciones como flujo normal.
import time

INVENTARIO = {"teclado": 12, "monitor": 4}
CONSULTAS = ["teclado", "mouse", "monitor", "webcam", "cámara"] * 40_000

inicio = time.perf_counter()
encontrados = 0
for pieza in CONSULTAS:
    try:
        INVENTARIO[pieza]
        encontrados += 1
    except KeyError:
        pass
con_excepcion = time.perf_counter() - inicio

inicio = time.perf_counter()
encontrados_if = 0
for pieza in CONSULTAS:
    if pieza in INVENTARIO:
        encontrados_if += 1
con_if = time.perf_counter() - inicio

print("Los dos cuentan lo mismo:", encontrados == encontrados_if, f"({encontrados:,})")
print(f"Consultas: {len(CONSULTAS):,}, de las que fallan el "
      f"{1 - encontrados / len(CONSULTAS):.0%}")
print()
print(f"Con try/except: {con_excepcion:.4f} s")
print(f"Con if:         {con_if:.4f} s")
print(f"La versión con excepciones tardó {con_excepcion / con_if:.1f} veces más.")
"""),

md("""
El mismo conteo, y la versión con excepciones tarda bastante más.

Levantar una excepción cuesta: hay que construir el objeto, armar el traceback y desenrollar la pila.
Cuando el caso ocurre una vez cada mil, eso no se nota. Cuando ocurre el sesenta por ciento de las
veces, era un `if`.

Es el error 04 de la diapositiva, y el criterio se lee en el nombre: **las excepciones son para lo
excepcional**. Si puedes predecir con qué frecuencia va a ocurrir el caso, no era excepcional.

El costo, de todos modos, es el argumento chico. El argumento grande es de lectura: un `try` alrededor de
algo que pasa todo el tiempo le miente a quien lee el código sobre qué es lo raro.

## El bug que lleva años sin dispararse
"""),

code("""
# FALLA A PROPÓSITO, y no truena. login_multiple_users.py, líneas 80 a 90.
usernames = ["ana", "luis", "sofia"]
passws = ["clave-ana", "clave-luis", "clave-sofia"]


def editar_por_indice(usernames, passws, tecleado, nueva):
    \"\"\"Las líneas 80 a 90 del archivo, con el input() reemplazado por un parámetro.\"\"\"
    index = int(tecleado)
    index -= 1
    try:
        passws[index] = nueva
        return "User edited."
    except IndexError:
        return "Index not found."


print("Antes:", passws)
print()
print("Tecleando 2, que es lo que el menú espera:")
print(" ", editar_por_indice(usernames, passws, "2", "nueva-luis"))
print(" ", passws)

print()
print("Tecleando 0, que el menú no espera:")
print(" ", editar_por_indice(usernames, passws, "0", "INTRUSA"))
print(" ", passws)
print()
print("¿A quién le cambió la contraseña?", usernames[-1])
print("¿Hubo IndexError?", "no, porque passws[-1] es un índice perfectamente válido")
"""),

md("""
Teclear `0` cambió la contraseña de `sofia`, que es la última de la lista, y el programa contestó
`User edited.`

La función resta uno para convertir la opción del menú en índice, y el `try` solo atrapa `IndexError`.
Pero `-1` **no** produce `IndexError`: en Python es el último elemento. El único índice fuera de rango
que el `except` llega a ver es el que se pasa por arriba.

Es el error 04 de este bloque al revés: no es que la excepción sobre, es que **el `except` está
esperando un error que en este caso no ocurre**. Atrapar por tipo no sirve de nada si el caso malo no
levanta nada.

La corrección no es otro `except`. Es una validación antes:

```python
if not 1 <= opcion <= len(usernames):
    return "Index not found."
```

**Un rango se valida con un `if`, no con un `except`.** Eso es exactamente lo que dice la diapositiva de
este bloque: valida en la frontera, y de ahí hacia adentro confía.

## Dónde va la revisión
"""),

code("""
class Cuenta:
    \"\"\"La revisión vive en el constructor y en el setter. En ningún otro lado.\"\"\"

    def __init__(self, titular: str, saldo: float = 0.0) -> None:
        if not titular.strip():
            raise ValueError("el titular no puede ir vacío")
        self._titular = titular.strip()
        self.saldo = saldo                    # pasa por el setter

    @property
    def saldo(self) -> float:
        return self._saldo

    @saldo.setter
    def saldo(self, valor: float) -> None:
        if valor < 0:
            raise ValueError(f"el saldo no puede ser negativo, llegó {valor}")
        self._saldo = float(valor)

    def depositar(self, monto: float) -> None:
        self.saldo = self.saldo + monto       # vuelve a pasar por el setter

    def __repr__(self) -> str:
        return f"Cuenta({self._titular!r}, {self._saldo:,.2f})"


c = Cuenta("Ana Robles", 1500)
c.depositar(500)
print(c)

for intento in [lambda: Cuenta("   "), lambda: Cuenta("Luis", -10),
                lambda: c.depositar(-3000)]:
    try:
        intento()
    except ValueError as e:
        print("  ValueError:", e)

print()
print("El objeto nunca quedó en un estado imposible:", c)
"""),

md("""
Tres intentos de meter un dato malo y tres mensajes que dicen qué corregir.

La revisión vive en dos lugares: el constructor y el `setter`. `depositar` no revisa nada, porque asigna
a `self.saldo` y eso pasa por el `setter`. Esa es la propiedad de la semana 5 cobrando su primer interés
de verdad.

Lo que se gana es que **el resto del programa se escribe suponiendo datos correctos**. Ninguna función
que reciba una `Cuenta` tiene que preguntarse si el saldo es negativo, porque no hay manera de construir
una así.

Lo que se pierde si la regla se rompe: si cada función revisa por su cuenta, la regla vive en veinte
lugares y tarde o temprano dos de ellos dicen cosas distintas.
"""),

md("""
---
# Bloque 3 · Robustez del software

Un error con nombre propio y un mensaje que dice qué corregir valen más que veinte líneas de defensas
repartidas.
"""),

code("""
# Code026.py, líneas 7 a 37: las dos versiones que el archivo escribe seguidas
class StreamGenerico:
    def __init__(self) -> None:
        self.opened = False

    def open(self) -> None:
        if self.opened:
            raise Exception("Stream already opened.")
        self.opened = True


class InvalidOperationError(Exception):
    pass


class Stream:
    def __init__(self) -> None:
        self.opened = False

    def open(self) -> None:
        if self.opened:
            raise InvalidOperationError("Stream already opened.")
        self.opened = True

    def close(self) -> None:
        if not self.opened:
            raise InvalidOperationError("Stream already closed.")
        self.opened = False


s = Stream()
s.open()
print("Con la excepción propia:")
for accion in [s.open, s.close, s.close]:
    try:
        accion()
        print(f"  {accion.__name__}() -> ok, opened={s.opened}")
    except InvalidOperationError as e:
        print(f"  {accion.__name__}() -> InvalidOperationError: {e}")

print()
print("Con la genérica, quien llama no puede distinguirla de nada más:")
g = StreamGenerico()
g.open()
try:
    g.open()
except InvalidOperationError:
    print("  atrapada por tipo")
except Exception as e:
    print("  hubo que atrapar Exception entera:", e)
"""),

md("""
`Code026.py` escribe la clase dos veces, y la segunda solo cambia una palabra: `Exception` por
`InvalidOperationError`.

El archivo lo justifica en su línea 16 con *"But we dont want a generic Exception. We want a specific
Exception"*, y esa es toda la razón. Una excepción propia es una clase que hereda de `Exception`, con
`pass` adentro, y con eso ya está completa.

Lo que compra es poder atraparla sola. Con `Exception` genérica no hay manera de escribir un `except`
que atienda "el stream ya estaba abierto" sin atrapar de paso todos los demás errores del programa.

## Lo que pasa cuando la excepción propia hereda de donde no debe
"""),

code("""
# FALLA A PROPÓSITO, y no truena. Una excepción propia colgada de BaseException.
class SaldoInsuficiente(BaseException):      # <- debería ser Exception
    pass


def retirar(saldo, monto):
    if monto > saldo:
        raise SaldoInsuficiente(f"faltan {monto - saldo:,.2f}")
    return saldo - monto


print("¿Hereda de Exception?", issubclass(SaldoInsuficiente, Exception))
print("Cadena:", [c.__name__ for c in SaldoInsuficiente.__mro__])
print()

try:
    try:
        retirar(100, 150)
    except Exception as e:
        print("La red de seguridad la atrapó:", e)
except SaldoInsuficiente as e:
    print("Se pasó de largo por el except Exception:", e)

print()


class SaldoInsuficienteBien(Exception):
    pass


try:
    raise SaldoInsuficienteBien("faltan 50.00")
except Exception as e:
    print("Colgada de Exception, la red la atrapa:", type(e).__name__, "-", e)
"""),

md("""
La excepción se saltó el `except Exception` de la capa de arriba y siguió subiendo.

Un programa serio suele tener, en el punto más alto, un `except Exception` que registra el error y
mantiene el programa vivo. Una excepción que cuelga de `BaseException` se salta esa red, y el programa se
cae con un traceback en la cara del usuario.

**Una excepción propia hereda de `Exception`, nunca de `BaseException`.** `BaseException` está reservada
para lo que no es un error del programa: la salida y la interrupción del teclado, que son las dos de la
celda del `except` pelón.

## El mensaje que dice qué corregir
"""),

code("""
class SaldoInsuficiente(Exception):
    def __init__(self, saldo, monto):
        self.saldo = saldo
        self.monto = monto
        self.faltante = monto - saldo
        super().__init__(f"faltan ${self.faltante:,.2f} para retirar ${monto:,.2f} "
                         f"de un saldo de ${saldo:,.2f}")


class Cuenta2:
    def __init__(self, saldo):
        self.saldo = saldo

    def retirar(self, monto):
        if monto > self.saldo:
            raise SaldoInsuficiente(self.saldo, monto)
        self.saldo -= monto


cuenta = Cuenta2(100)

try:
    cuenta.retirar(150)
except SaldoInsuficiente as e:
    print("Tipo:    ", type(e).__name__)
    print("Mensaje: ", e)
    print("Y además el dato, sin tener que leer el texto:")
    print("   faltante:", e.faltante)
    print("   se puede sugerir:", f"retira hasta ${e.saldo:,.2f}")

print()
print("El saldo no se movió:", cuenta.saldo)
"""),

md("""
Tres cosas llegan juntas: el tipo, el mensaje y los datos.

El mensaje dice **qué corregir**, no solo que algo salió mal. Comparado con `"Error"` o con
`"Operación inválida"`, la diferencia es que quien lo lee sabe qué teclear en el siguiente intento.

Los atributos son la otra mitad. Guardar `saldo`, `monto` y `faltante` en la excepción deja que quien la
atrape use los números sin tener que sacarlos del texto con `split`, que es lo que la gente termina
haciendo cuando la excepción solo trae una cadena.

Fíjate en la última línea: **el objeto no cambió de estado**. La validación corre antes de tocar nada, y
por eso una excepción no deja la cuenta a medio retirar.

## `raise ... from`, para no perder la causa
"""),

code("""
class ErrorDeCaptura(Exception):
    pass


def leer_nota(texto):
    try:
        return float(texto)
    except ValueError as e:
        raise ErrorDeCaptura(f"la nota {texto!r} no es un número") from e


try:
    leer_nota("siete coma ocho")
except ErrorDeCaptura as e:
    print("Lo que ve quien llama:", type(e).__name__ + ":", e)
    print("La causa original:    ", type(e.__cause__).__name__ + ":", e.__cause__)

print()
import traceback
try:
    leer_nota("siete coma ocho")
except ErrorDeCaptura as e:
    print(traceback.format_exc())
"""),

md("""
Dos excepciones en un solo traceback, unidas por la línea *"The above exception was the direct cause of
the following exception"*.

`raise ... from e` traduce un error técnico a uno del dominio **sin borrar el original**. Quien llama
atrapa `ErrorDeCaptura`, que es lo que le importa; quien depura sigue viendo el `ValueError` de `float`
que lo causó.

Sin el `from`, Python encadena de todos modos, pero con la frase *"During handling of the above
exception, another exception occurred"*, que dice algo distinto: que el segundo error ocurrió **mientras**
se atendía el primero, no que sea su traducción.

## El archivo del repositorio, corrido
"""),

code("""
# Code035.py, líneas 10 a 47, con las rutas cambiadas al directorio de trabajo
from pathlib import Path

try:
    file_path = Path("x.txt")
    with open(file_path, 'r') as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print(f"The file at {file_path} was not found.")
except IOError:
    print(f"An error occurred while reading the file at {file_path}.")

try:
    with open("app.py") as file:
        print("File opened")
except Exception as ex:
    print("Could not open the file")

print()
print("El archivo original imprime estas dos mismas líneas, desde cualquier directorio,")
print("porque sus dos rutas apuntan a archivos que no existen.")
"""),

md("""
`Code035.py` corre completo y siempre por la rama de error. Sus dos rutas apuntan a archivos que no
existen, así que el camino feliz del archivo nunca se ha visto.

Dos cosas que hoy escribiríamos distinto, y ninguna es un error de sintaxis.

**`file_path` se asigna dentro del `try`.** Aquí no truena porque construir un `Path` no puede fallar,
pero es el patrón exacto de la celda del `NameError`. La asignación va afuera.

**`except Exception as ex` atrapa todo y no usa `ex`.** El nombre se captura y se descarta, así que el
mensaje que se imprime es el mismo si el archivo no existe, si no hay permisos o si alguien escribió mal
el nombre de una variable tres líneas arriba.

Lo que el archivo sí hace bien, y conviene copiar: pone `FileNotFoundError` **antes** que `IOError`.
"""),

md("""
---
## Cuatro errores de esta sesión

**Un `except` sin tipo.** Atrapa el `NameError` de un typo, el Ctrl+C y la salida del programa. Nombra el
tipo que de verdad esperas.

**Un `except` con `pass` adentro.** El error desaparece sin dejar rastro y el defecto reaparece tres
pantallas más adelante, convertido en un promedio que no cuadra.

**Un `try` alrededor de cuarenta líneas.** Cuando salta no sabes cuál de las cuarenta falló. Envuelve
solo la línea riesgosa.

**Excepciones para el flujo normal.** Si el caso ocurre la mitad de las veces, era un `if`. Y un rango se
valida con un `if` aunque el `except` esté escrito, como en el menú del sistema de login.
"""),

md("""
---
# Ejercicios

El laboratorio de esta semana es endurecer un lector de calificaciones. Los ejercicios construyen hacia
eso.

Las soluciones están hasta abajo del cuaderno.

### Ejercicio 1 · Leer el traceback

Escribe tres funciones que se llamen en cadena y haz que la última falle. Atrapa la excepción e imprime
los marcos con `traceback.extract_tb`.

Di en un comentario cuál de los tres marcos contiene el error de verdad y por qué no es el último.

### Ejercicio 2 · Un `except` por tipo

Escribe una función que convierta un texto a número y divida diez entre él. Atiende por separado el texto
que no es número y el cero.

Pruébala con cinco entradas distintas e imprime qué devolvió cada una.

### Ejercicio 3 · Las cuatro cláusulas

Escribe una función con `try`, `except`, `else` y `finally` que vaya guardando en una lista qué cláusula
corrió. Llámala con una entrada buena y una mala e imprime las dos listas.

### Ejercicio 4 · El `finally` que se traga

Escribe una función que levante un `ValueError` dentro del `try` y tenga un `return` en el `finally`.
Muestra que quien la llama no recibe ninguna excepción.

Quita el `return` y comprueba que ahora sí sube.

### Ejercicio 5 · El orden importa

Escribe dos versiones de la misma función, una con `except OSError` antes de `except FileNotFoundError` y
otra al revés. Llama a las dos con una ruta que no existe y muestra que devuelven cosas distintas.

Imprime el `__mro__` de `FileNotFoundError` para explicar por qué.

### Ejercicio 6 · Sin `pass`

Toma una lista de diez capturas donde tres traigan la nota mal escrita. Conviértelas guardando aparte las
que fallaron, con el nombre y el motivo.

Imprime cuántas entraron, cuántas se rechazaron, y comprueba que las dos sumen diez.

### Ejercicio 7 · Validar en la frontera

Escribe una clase `Alumno` con matrícula y promedio. La matrícula no puede ir vacía y el promedio tiene
que estar entre cero y diez. Las dos revisiones van en el constructor y en el `setter`.

Intenta construir tres objetos inválidos y atrapa los tres `ValueError`.

### Ejercicio 8 · Una excepción del dominio

Define `NotaFueraDeRango(Exception)` que guarde el valor recibido y el rango permitido, y arme su mensaje
con los dos. Lánzala desde el `setter` del ejercicio anterior.

Atrápala e imprime el mensaje y los atributos por separado.

### Ejercicio 9 · El laboratorio

Te entregan un script que lee calificaciones desde la consola y truena con cualquier entrada rara.
Hazlo sobrevivir a texto, a números fuera de rango y a un archivo que no existe.

Restricciones: ningún `except` sin tipo, ninguno vacío, y el `try` envuelve solo la línea riesgosa.

El criterio es que cada mensaje le diga a quien lo lee qué tiene que corregir para seguir.
"""),

md("""
---
## Tres ideas para llevarse

**Un `except` por tipo, y con nombre.** `except Exception` atrapa lo que no esperabas y esconde justo el
error que sí importaba. El `except` pelón además se lleva el Ctrl+C.

**La validación vive en la frontera.** Se revisa donde el dato entra, en el constructor y en el `setter`,
y de ahí hacia adentro el resto del programa ya confía. Un rango se valida con un `if`, no esperando un
`IndexError` que a veces no llega.

**`finally` corre siempre.** Con error, sin error y con un `return` esperando su turno. Es donde se cierra
lo que se abrió, y es lo único que debe ir ahí.

La semana 12 abre la unidad de archivos: rutas que sirven en cualquier sistema, el bloque `with` que
cierra solo, y el CSV de siempre. Una celda de este cuaderno abrió un archivo a mano y tuvo que escribir
el `finally` que lo cerrara, y se cayó en el intento; el `with` de la semana que entra es lo que hace que
ese `finally` deje de escribirse.
"""),

md("""
---
# Soluciones

### Ejercicio 1

```python
import traceback


def nivel_1(texto):
    return nivel_2(texto)


def nivel_2(texto):
    return nivel_3(texto)


def nivel_3(texto):
    return float(texto)


try:
    nivel_1("no soy un número")
except ValueError as e:
    for m in traceback.extract_tb(e.__traceback__):
        print(f"línea {m.lineno:>3}  {m.name:<10}{m.line}")

# El último marco es float(texto), que hizo su trabajo bien: le dieron un texto
# que no era un número. El error de verdad está en el marco de arriba, en quien
# llamó con ese texto sin revisarlo antes.
```

### Ejercicio 2

```python
def dividir(texto):
    try:
        return 10 / int(texto)
    except ValueError:
        return "no es un entero"
    except ZeroDivisionError:
        return "no puede ser cero"


for entrada in ["5", "0", "abc", "  2  ", "3.5"]:
    print(f"{entrada!r:<10}{dividir(entrada)}")
```

### Ejercicio 3

```python
def intentar(valor):
    corrio = []
    try:
        corrio.append("try")
        n = int(valor)
    except ValueError:
        corrio.append("except")
        n = None
    else:
        corrio.append("else")
    finally:
        corrio.append("finally")
    return n, corrio


print(intentar("7"))
print(intentar("siete"))
```

### Ejercicio 4

```python
FUENTE = '''
def guardar():
    try:
        raise ValueError("no se guardó")
    finally:
        return "ok"
'''
exec(compile(FUENTE, "<ej>", "exec"), globals())
print("Devuelve:", guardar())


def guardar_bien():
    try:
        raise ValueError("no se guardó")
    finally:
        print("el finally corrió")


try:
    guardar_bien()
except ValueError as e:
    print("Ahora sí subió:", e)
```

### Ejercicio 5

```python
from pathlib import Path


def general_primero(ruta):
    try:
        return Path(ruta).read_text()
    except OSError:
        return "error de sistema"
    except FileNotFoundError:
        return "no existe"


def especifico_primero(ruta):
    try:
        return Path(ruta).read_text()
    except FileNotFoundError:
        return "no existe"
    except OSError:
        return "error de sistema"


print(general_primero("nada.txt"))
print(especifico_primero("nada.txt"))
print([c.__name__ for c in FileNotFoundError.__mro__])

# FileNotFoundError hereda de OSError, así que el except general coincide
# primero y el específico queda inalcanzable.
```

### Ejercicio 6

```python
CAPTURAS = [("Ana", "9.2"), ("Luis", "7,8"), ("Sofía", "9.5"), ("Marco", "6.4"),
            ("Paula", ""), ("Rubén", "8.1"), ("Elena", "9,0"), ("Iván", "7.7"),
            ("Óscar", "8.8"), ("Sara", "6.9")]

buenas, rechazadas = [], []
for nombre, cruda in CAPTURAS:
    try:
        buenas.append((nombre, float(cruda)))
    except ValueError as e:
        rechazadas.append((nombre, cruda, str(e)))

print("Entraron:", len(buenas))
print("Rechazadas:", len(rechazadas))
for nombre, cruda, motivo in rechazadas:
    print(f"  {nombre}: {cruda!r} -> {motivo}")
print("¿Suman diez?", len(buenas) + len(rechazadas) == len(CAPTURAS))
```

### Ejercicio 7

```python
class Alumno:
    def __init__(self, matricula, promedio):
        if not matricula.strip():
            raise ValueError("la matrícula no puede ir vacía")
        self._matricula = matricula.strip()
        self.promedio = promedio

    @property
    def promedio(self):
        return self._promedio

    @promedio.setter
    def promedio(self, valor):
        if not 0 <= valor <= 10:
            raise ValueError(f"el promedio debe ir de 0 a 10, llegó {valor}")
        self._promedio = float(valor)


for intento in [lambda: Alumno("", 9.0), lambda: Alumno("A001", 11),
                lambda: Alumno("A002", -1)]:
    try:
        intento()
    except ValueError as e:
        print("ValueError:", e)
```

### Ejercicio 8

```python
class NotaFueraDeRango(Exception):
    def __init__(self, valor, minimo=0, maximo=10):
        self.valor = valor
        self.minimo = minimo
        self.maximo = maximo
        super().__init__(f"{valor} está fuera del rango permitido "
                         f"[{minimo}, {maximo}]")


class Alumno2:
    def __init__(self, matricula, promedio):
        self._matricula = matricula
        self.promedio = promedio

    @property
    def promedio(self):
        return self._promedio

    @promedio.setter
    def promedio(self, valor):
        if not 0 <= valor <= 10:
            raise NotaFueraDeRango(valor)
        self._promedio = float(valor)


try:
    Alumno2("A001", 11.5)
except NotaFueraDeRango as e:
    print("Mensaje:", e)
    print("Valor:", e.valor, " rango:", e.minimo, "a", e.maximo)
```

### Ejercicio 9

```python
from pathlib import Path


class CalificacionInvalida(Exception):
    def __init__(self, cruda, motivo):
        self.cruda = cruda
        self.motivo = motivo
        super().__init__(f"{cruda!r}: {motivo}")


def a_calificacion(cruda):
    \"\"\"Frontera de entrada. Todo lo que salga de aquí ya sirve.\"\"\"
    texto = cruda.strip()
    try:
        valor = float(texto)
    except ValueError:
        raise CalificacionInvalida(texto, "no es un número") from None
    if not 0 <= valor <= 10:
        raise CalificacionInvalida(texto, "está fuera del rango 0 a 10")
    return valor


def leer_lineas(ruta):
    try:
        return Path(ruta).read_text(encoding="utf-8").splitlines()
    except FileNotFoundError:
        print(f"No existe {ruta}. Revisa el nombre y vuelve a intentar.")
        return []


def procesar(lineas):
    buenas, malas = [], []
    for numero, linea in enumerate(lineas, start=1):
        if not linea.strip():
            continue
        try:
            buenas.append(a_calificacion(linea))
        except CalificacionInvalida as e:
            malas.append(f"renglón {numero}: {e}")
    return buenas, malas


def reportar(buenas, malas):
    if buenas:
        print(f"{len(buenas)} calificaciones, promedio "
              f"{sum(buenas) / len(buenas):.2f}")
    else:
        print("No entró ninguna calificación válida.")
    for m in malas:
        print("  ", m)


if __name__ == "__main__":
    ENTRADAS = ["9.2", "siete", "11", "8.0", "-1", "", "  7.5  "]
    Path("notas.txt").write_text("\\n".join(ENTRADAS), encoding="utf-8")

    buenas, malas = procesar(leer_lineas("notas.txt"))
    reportar(buenas, malas)

    procesar(leer_lineas("no_existe.txt"))
```

Tres decisiones que vale la pena defender en la entrega.

**`a_calificacion` es la única frontera.** Convierte y valida en el mismo lugar, y de ahí para adentro
nadie vuelve a preguntar si el número sirve. `reportar` recibe una lista de flotantes y se escribe sin
una sola defensa.

**Cada `except` nombra un tipo y ninguno lleva `pass`.** El `ValueError` de `float` se traduce a
`CalificacionInvalida`, que es el nombre del problema en el lenguaje del profesor, no en el de Python.

**El `from None` es deliberado.** Aquí el `ValueError` de `float` no aporta nada: ya lo dice el mensaje
propio. Cuando la causa técnica sí importa, se escribe `from e` y el traceback las encadena.
"""),

]

write(OUT / "es" / "w11.ipynb", es)
print("wrote", OUT / "es" / "w11.ipynb")
