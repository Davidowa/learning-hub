# Soluciones · Programación Orientada a Objetos · COM102

Cuadernillo del profesor. Cada ejercicio trae la solución corrida en Python 3.13, la salida real que produce, una rúbrica de diez puntos y el error que más aparece al calificar. Las soluciones de las semanas 14 y 15 que abren ventana están revisadas contra la documentación de PyQt6 pero no se ejecutaron aquí, y se marcan donde corresponde.

## Semana 01 · Encuadre del curso

### 01.1 · Reconocer
**Solución**
```text
Línea 4: tag[0] es 'B' y tag[-1] es 'A', la última letra de BOMBA.
Línea 5: el corte [0:5] entra en el 0 y no entra en el 5, así que da B-101.
Línea 6: horas es texto, no número. "4820" * 2 repite la cadena y queda
         "48204820", de ocho caracteres. Por eso imprime 8 y no 4.
Línea 7: el más entre dos cadenas concatena, no suma.
Línea 12: el ciclo acumula 10 + 20 + 30.
```
**Salida**
```text
B A
B-101
8
48200
60
```
**Rúbrica** (suma 10)
| Criterio | Puntos |
|---|---|
| Las cinco líneas de salida, exactas | 5 |
| Explica que horas es str y que el asterisco repite | 3 |
| Explica la regla del corte y el índice negativo | 2 |

**Error que más se ve**
Contestan 4 en la tercera línea porque leyeron 4820 como número: se delata en cuanto también contestan 9640 en la cuarta.

### 01.2 · Aplicar
**Solución**
```python
def clasificar_presion(bar: float) -> str:
    if bar < 2.0:
        return "baja"
    if bar <= 8.0:
        return "normal"
    return "alta"


lecturas = [1.4, 2.0, 6.7, 8.0, 9.3]

for lectura in lecturas:
    print(f"{lectura:.1f} bar -> {clasificar_presion(lectura)}")
```
**Salida**
```text
1.4 bar -> baja
2.0 bar -> normal
6.7 bar -> normal
8.0 bar -> normal
9.3 bar -> alta
```
**Rúbrica** (suma 10)
| Criterio | Puntos |
|---|---|
| La función devuelve la cadena en lugar de imprimirla | 4 |
| Las dos fronteras, 2.0 y 8.0, quedan en normal | 3 |
| El formato del renglón y el decimal con f-string | 3 |

**Error que más se ve**
Escriben `print` dentro de la función y `return` no aparece: el ciclo entonces imprime `None` al final de cada renglón.

### 01.3 · Integrar
**Solución**
```python
lecturas = [
    ("TT-101", "74.5"),
    ("PT-205", "6.1"),
    ("TT-101", "s/d"),
    ("FT-330", "118.0"),
    ("PT-205", "6.4"),
    ("FT-330", "sin dato"),
]


def separar(registros: list) -> tuple:
    validas = []
    descartadas = 0
    for tag, texto in registros:
        try:
            validas.append((tag, float(texto)))
        except ValueError:
            descartadas += 1
    return validas, descartadas


def promedio(valores: list) -> float:
    total = 0.0
    for valor in valores:
        total += valor
    return total / len(valores)


def etiquetas(registros: list) -> list:
    todas = []
    for tag, texto in registros:
        todas.append(tag)
    return sorted(set(todas))


validas, descartadas = separar(lecturas)

solo_numeros = []
for tag, valor in validas:
    solo_numeros.append(valor)

print(f"Validas: {len(validas)}")
print(f"Descartadas: {descartadas}")
print(f"Promedio: {promedio(solo_numeros):.2f}")
print(etiquetas(lecturas))
```
**Salida**
```text
Validas: 4
Descartadas: 2
Promedio: 51.25
['FT-330', 'PT-205', 'TT-101']
```
**Rúbrica** (suma 10)
| Criterio | Puntos |
|---|---|
| El try envuelve solo la conversión y nombra ValueError | 4 |
| Las tres funciones devuelven y ninguna imprime adentro | 3 |
| Las etiquetas sin repetir salen de un conjunto, no de un ciclo con if | 2 |
| El promedio sale con dos decimales | 1 |

**Error que más se ve**
Meten el ciclo completo dentro de un solo `try`: la primera lectura mala corta el recorrido y el promedio sale de dos valores en lugar de cuatro.

## Semana 02 · Tema 1 · Introducción a la POO

### 02.1 · Reconocer
**Solución**
```text
remove borró B-102 de tags y dejó horas intacta. El ciclo recorre las dos
posiciones que le quedan a tags y lee horas por la misma posición, así que
C-310 se lleva las 1150 horas que eran de B-102, y las 6300 suyas quedan
huérfanas al final de la lista.

Faltó horas.remove(1150), o mejor, borrar por índice en las dos listas a la
vez. Python no protesta porque no sabe que las dos listas van juntas: esa
relación existe solo en la cabeza de quien escribió el programa.
```
**Salida**
```text
B-101 4820
C-310 1150
```
**Rúbrica** (suma 10)
| Criterio | Puntos |
|---|---|
| Las dos líneas de salida | 4 |
| Dice que las 1150 horas eran de B-102 | 3 |
| Explica que la correspondencia entre listas no está en el código | 3 |

**Error que más se ve**
Contestan que el programa truena con `IndexError`: no truena, porque la lista corta es la que manda en el `range`.

### 02.2 · Aplicar
**Solución**
```text
1. Función. Entra un número, sale otro, no recuerda nada.
2. Clase. Las horas y el estado sobreviven entre una llamada y la siguiente.
3. Función. Recorre y cuenta; el resultado no se guarda en ningún lado.
4. Clase. Folio, equipo y avance solo tienen sentido juntos y cambian con el tiempo.
5. Función. Recibe una lista y devuelve otra.
6. Clase. Descontar piezas modifica algo que tiene que seguir ahí después.
```
```python
def psi_a_bar(psi: float) -> float:
    return psi * 0.0689476


print(f"{psi_a_bar(120):.2f} bar")
print(f"{psi_a_bar(45):.2f} bar")
```
**Salida**
```text
8.27 bar
3.10 bar
```
**Rúbrica** (suma 10)
| Criterio | Puntos |
|---|---|
| Los seis casos bien clasificados | 4 |
| Cada justificación menciona si hay estado o no | 3 |
| La función convierte y devuelve, con dos decimales | 3 |

**Error que más se ve**
Clasifican el punto 3 como clase porque dice "contar": el verbo no decide, decide si algo sobrevive a la llamada.

### 02.3 · Integrar
**Solución**
```python
tags = ["B-101", "B-102", "C-310", "M-204"]
horas = [4820, 1150, 6300, 2210]
estados = ["operando", "detenido", "operando", "operando"]
revision = [1180, 40, 900, 310]


def a_registros(tags: list, horas: list, estados: list, revision: list) -> list:
    registros = []
    for i in range(len(tags)):
        registros.append({
            "tag": tags[i],
            "horas": horas[i],
            "estado": estados[i],
            "revision": revision[i],
        })
    return registros


def dar_de_baja(registros: list, tag: str) -> list:
    quedan = []
    for equipo in registros:
        if equipo["tag"] != tag:
            quedan.append(equipo)
    return quedan


def imprimir(registros: list) -> None:
    for equipo in registros:
        print(equipo["tag"], equipo["horas"], equipo["estado"], equipo["revision"])


planta = a_registros(tags, horas, estados, revision)
planta = dar_de_baja(planta, "B-102")

imprimir(planta)
print(len(planta))
```
**Salida**
```text
B-101 4820 operando 1180
C-310 6300 operando 900
M-204 2210 operando 310
3
```
**Rúbrica** (suma 10)
| Criterio | Puntos |
|---|---|
| Un diccionario por equipo, con las cuatro llaves | 4 |
| dar_de_baja devuelve una lista nueva y no modifica la que recibe | 3 |
| C-310 conserva sus 6300 horas después de la baja | 2 |
| Las tres funciones tienen un solo trabajo cada una | 1 |

**Error que más se ve**
`dar_de_baja` borra mientras recorre la misma lista: el ciclo salta un elemento y el equipo siguiente al dado de baja se queda dentro.

## Semana 03 · Tema 2 · Elementos básicos

### 03.1 · Reconocer
**Solución**
```text
alarmas se declaró en el cuerpo de la clase, así que existe una sola lista
para todas las bombas. self.alarmas.append no crea nada nuevo: busca el
nombre en el objeto, no lo encuentra, lo encuentra en la clase y le agrega
ahí. B-102 ve las dos alarmas de B-101 y las dos etiquetas apuntan al mismo
objeto.
```
```python
    def __init__(self, tag):
        self.tag = tag
        self.alarmas = []
```
**Salida**
```text
2
['E12', 'E07']
True
```
**Rúbrica** (suma 10)
| Criterio | Puntos |
|---|---|
| Las tres salidas | 4 |
| Explica que la lista vive en la clase, no en el objeto | 3 |
| La corrección asigna la lista dentro de __init__ sobre self | 3 |

**Error que más se ve**
Contestan 0 y luego se sorprenden con el `True`: la tercera línea es la que no deja escaparse por "cada objeto tiene la suya".

### 03.2 · Aplicar
**Solución**
```python
class Bomba:
    def __init__(self, tag: str, caudal_l_s: float, horas: float) -> None:
        self.tag = tag
        self.caudal_l_s = caudal_l_s
        self.horas = horas

    def registrar_horas(self, corridas: float) -> None:
        self.horas = self.horas + corridas

    @property
    def caudal_m3_h(self) -> float:
        return self.caudal_l_s * 3.6

    @property
    def horas_para_servicio(self) -> float:
        return 5000 - self.horas


b101 = Bomba("B-101", 120.0, 4820.0)

print(f"{b101.tag}: {b101.caudal_m3_h:.1f} m3/h")
print(f"Faltan {b101.horas_para_servicio:.0f} h")

b101.registrar_horas(260)

print(f"Faltan {b101.horas_para_servicio:.0f} h")
```
**Salida**
```text
B-101: 432.0 m3/h
Faltan 180 h
Faltan -80 h
```
**Rúbrica** (suma 10)
| Criterio | Puntos |
|---|---|
| Constructor con los tres atributos sobre self | 3 |
| Las dos propiedades se leen sin paréntesis y calculan al vuelo | 4 |
| registrar_horas acumula en lugar de reemplazar | 2 |
| El segundo resultado sale en negativo y no se recorta a cero | 1 |

**Error que más se ve**
Guardan el caudal en m3/h como atributo dentro del constructor: al cambiar el caudal en litros, el otro dato se queda viejo, que es justo lo que la propiedad evita.

### 03.3 · Integrar
**Solución**
```python
class Sensor:
    def __init__(self, tag: str, unidad: str, minimo: float, maximo: float) -> None:
        self.tag = tag
        self.unidad = unidad
        self.minimo = minimo
        self.maximo = maximo

    def en_rango(self, valor: float) -> bool:
        return valor >= self.minimo and valor <= self.maximo

    @property
    def amplitud(self) -> float:
        return self.maximo - self.minimo


sensores = {
    "TT-101": Sensor("TT-101", "C", 0.0, 400.0),
    "PT-205": Sensor("PT-205", "bar", 0.0, 10.0),
    "FT-330": Sensor("FT-330", "L/s", 0.0, 200.0),
}

lecturas = [
    ("TT-101", 412.0),
    ("PT-205", 6.1),
    ("FT-330", 118.0),
    ("TT-101", 74.5),
    ("PT-205", 11.2),
]

fuera = 0
for tag, valor in lecturas:
    sensor = sensores[tag]
    if sensor.en_rango(valor):
        print(f"{tag} {valor} {sensor.unidad} dentro")
    else:
        print(f"{tag} {valor} {sensor.unidad} FUERA")
        fuera = fuera + 1

caudalimetro = sensores["FT-330"]

print(f"Fuera de rango: {fuera}")
print(f"Amplitud de FT-330: {caudalimetro.amplitud:.0f} L/s")
```
**Salida**
```text
TT-101 412.0 C FUERA
PT-205 6.1 bar dentro
FT-330 118.0 L/s dentro
TT-101 74.5 C dentro
PT-205 11.2 bar FUERA
Fuera de rango: 2
Amplitud de FT-330: 200 L/s
```
**Rúbrica** (suma 10)
| Criterio | Puntos |
|---|---|
| La clase Sensor con sus cuatro atributos y el método de rango | 3 |
| El sensor se busca por llave en un diccionario | 3 |
| La propiedad amplitud calcula, no se guarda | 2 |
| El conteo de lecturas fuera de rango y el formato de cada renglón | 2 |

**Error que más se ve**
Recorren una lista de sensores buscando la etiqueta con un `for` adentro del `for` de lecturas: funciona con tres sensores y es lo que la semana 10 va a llamar "usar una lista para buscar".

## Semana 04 · Tema 2 · Elementos básicos

### 04.1 · Reconocer
**Solución**
```text
self.registrados += 1 lee el 0 de la clase, le suma uno y guarda el
resultado en el objeto. Cada equipo se queda con su propio 1 y la clase
nunca se entera, por eso Equipo.registrados sigue en 0 y a.registrados
vale 1. El atributo con dos guiones bajos existe, pero renombrado a
_Equipo__tag, así que hasattr con el nombre original contesta False.

La corrección es escribir Equipo.registrados += 1 dentro del constructor.
```
**Salida**
```text
0
1
B-101
False
```
**Rúbrica** (suma 10)
| Criterio | Puntos |
|---|---|
| Las cuatro salidas | 4 |
| Explica que la asignación creó un atributo de instancia | 3 |
| Nombra el renombrado y por qué hasattr da False | 2 |
| La corrección escribe sobre la clase | 1 |

**Error que más se ve**
Contestan 2 en la primera línea: es la respuesta correcta para el contador que sí funciona, y por eso no notan la diferencia hasta ver la segunda.

### 04.2 · Aplicar
**Solución**
```python
class Manometro:
    def __init__(self, tag: str, presion: float) -> None:
        self.tag = tag
        self.presion = presion

    @property
    def presion(self) -> float:
        return self.__presion

    @presion.setter
    def presion(self, valor: float) -> None:
        if valor < 0.0 or valor > 10.0:
            raise ValueError(f"{valor} bar queda fuera del rango 0 a 10")
        self.__presion = valor

    @classmethod
    def desde_psi(cls, tag: str, psi: float) -> "Manometro":
        return cls(tag, psi * 0.0689476)


pt205 = Manometro("PT-205", 6.1)
print(f"{pt205.tag}: {pt205.presion:.2f} bar")

pt205.presion = 9.0
print(f"{pt205.tag}: {pt205.presion:.2f} bar")

try:
    pt205.presion = 12.5
except ValueError as ex:
    print("Rechazado:", ex)

print(f"{pt205.tag}: {pt205.presion:.2f} bar")

pt301 = Manometro.desde_psi("PT-301", 120.0)
print(f"{pt301.tag}: {pt301.presion:.2f} bar")
```
**Salida**
```text
PT-205: 6.10 bar
PT-205: 9.00 bar
Rechazado: 12.5 bar queda fuera del rango 0 a 10
PT-205: 9.00 bar
PT-301: 8.27 bar
```
**Rúbrica** (suma 10)
| Criterio | Puntos |
|---|---|
| Propiedad con setter, y el setter es el único que asigna el privado | 4 |
| El constructor pasa por la propiedad, no por el atributo | 2 |
| El classmethod usa cls y devuelve un objeto ya validado | 2 |
| El ValueError trae el valor rechazado y el objeto no cambia | 2 |

**Error que más se ve**
Dentro del setter escriben `self.presion = valor`: la propiedad se llama a sí misma y el programa muere con `RecursionError` en la primera construcción.

### 04.3 · Integrar
**Solución**
```python
class Tanque:
    instalados = 0

    def __init__(self, tag: str, capacidad: float, nivel: float) -> None:
        self.tag = tag
        self.capacidad = capacidad
        self.__nivel = nivel
        Tanque.instalados += 1

    @property
    def nivel(self) -> float:
        return self.__nivel

    @property
    def porcentaje(self) -> float:
        return self.__nivel / self.capacidad * 100

    def llenar(self, litros: float) -> None:
        if self.__nivel + litros > self.capacidad:
            raise ValueError(f"{litros:.0f} L desbordan el {self.tag}")
        self.__nivel += litros

    def vaciar(self, litros: float) -> None:
        if litros > self.__nivel:
            raise ValueError(f"El {self.tag} solo tiene {self.__nivel:.0f} L")
        self.__nivel -= litros


def estado(tanque: Tanque) -> str:
    return f"{tanque.tag}: {tanque.nivel:.0f} L ({tanque.porcentaje:.1f} %)"


tq01 = Tanque("TQ-01", 5000.0, 1200.0)
tq02 = Tanque("TQ-02", 2000.0, 800.0)

tq01.llenar(2000)
print(estado(tq01))

try:
    tq01.vaciar(4000)
except ValueError as ex:
    print("Rechazado:", ex)

try:
    tq01.llenar(3000)
except ValueError as ex:
    print("Rechazado:", ex)

tq01.vaciar(1200)
print(estado(tq01))
print(estado(tq02))
print("Tanques instalados:", Tanque.instalados)
```
**Salida**
```text
TQ-01: 3200 L (64.0 %)
Rechazado: El TQ-01 solo tiene 3200 L
Rechazado: 3000 L desbordan el TQ-01
TQ-01: 2000 L (40.0 %)
TQ-02: 800 L (40.0 %)
Tanques instalados: 2
```
**Rúbrica** (suma 10)
| Criterio | Puntos |
|---|---|
| Nivel privado y las dos propiedades de solo lectura | 3 |
| Los dos métodos validan antes de mover el nivel | 3 |
| El contador se escribe sobre la clase y llega a 2 | 2 |
| Los dos rechazos se atrapan por tipo y el nivel queda intacto | 2 |

**Error que más se ve**
Validan después de sumar: el tanque se desborda, y solo entonces salta el error, con el nivel ya mal.

## Semana 05 · Tema 2 · Elementos básicos

### 05.1 · Reconocer
**Solución**
```text
El segundo def sobrescribe al primero, igual que asignar dos veces la misma
variable. Solo existe la versión de tres parámetros, así que la llamada con
tres datos corre y la de dos truena por el argumento que falta.
```
```python
class Registrador:
    def registrar(self, tag, valor, unidad="C"):
        print("registro:", tag, valor, unidad)
```
**Salida**
```text
tres datos: TT-101 74.5 C
Traceback (most recent call last):
  File "registrador.py", line 11, in <module>
    r.registrar("PT-205", 6.1)
    ~~~~~~~~~~~^^^^^^^^^^^^^^^
TypeError: Registrador.registrar() missing 1 required positional argument: 'unidad'
```
**Rúbrica** (suma 10)
| Criterio | Puntos |
|---|---|
| La primera llamada imprime la versión de tres | 3 |
| Nombra el TypeError y el argumento que falta | 3 |
| Explica que el nombre del método es una entrada que guarda un valor | 2 |
| La corrección usa un valor por omisión, sin if de conteo | 2 |

**Error que más se ve**
Contestan que Python elige el método según los argumentos: eso es Java, y aquí la primera definición ya no existe.

### 05.2 · Aplicar
**Solución**
```python
class Existencia:
    def __init__(self, clave: str, piezas: int) -> None:
        self.clave = clave
        self.piezas = piezas

    def __str__(self) -> str:
        return f"{self.clave} x{self.piezas}"

    def __eq__(self, otra) -> bool:
        return self.clave == otra.clave and self.piezas == otra.piezas

    def __add__(self, otra) -> "Existencia":
        if self.clave != otra.clave:
            raise ValueError("No se suman refacciones distintas")
        return Existencia(self.clave, self.piezas + otra.piezas)


almacen = Existencia("BL-220", 12)
llegada = Existencia("BL-220", 8)

print(almacen)
print(almacen + llegada)
print(almacen == Existencia("BL-220", 12))
print(almacen == llegada)

try:
    print(almacen + Existencia("SM-4471", 6))
except ValueError as ex:
    print("Rechazado:", ex)
```
**Salida**
```text
BL-220 x12
BL-220 x20
True
False
Rechazado: No se suman refacciones distintas
```
**Rúbrica** (suma 10)
| Criterio | Puntos |
|---|---|
| __str__ con el formato pedido | 2 |
| __eq__ compara los dos datos y no la identidad | 3 |
| __add__ devuelve un objeto nuevo sin tocar los operandos | 3 |
| Claves distintas levantan ValueError | 2 |

**Error que más se ve**
`__add__` hace `self.piezas += otra.piezas` y devuelve `self`: la suma modifica el almacén, y la línea que la imprime lo deja en 20 sin que nadie lo haya pedido.

### 05.3 · Integrar
**Solución**
```python
class Existencia:
    def __init__(self, clave: str, piezas: int) -> None:
        self.clave = clave
        self.piezas = piezas

    def __str__(self) -> str:
        return f"{self.clave} x{self.piezas}"


class Inventario:
    def __init__(self, almacen: str) -> None:
        self.almacen = almacen
        self.__existencias: dict[str, int] = {}

    def recibir(self, *claves: str, **opciones) -> None:
        piezas = opciones.get("piezas", 1)
        for clave in claves:
            actual = self.__existencias.get(clave, 0)
            self.__existencias[clave] = actual + piezas
        if opciones.get("avisar", False):
            print(f"{len(claves)} claves recibidas en {self.almacen}")

    def listado(self) -> list:
        renglones = []
        for clave, piezas in self.__existencias.items():
            renglones.append(Existencia(clave, piezas))
        return renglones

    def __str__(self) -> str:
        total = 0
        for clave, piezas in self.__existencias.items():
            total += piezas
        return f"{self.almacen}: {len(self.__existencias)} claves, {total} piezas"


if __name__ == "__main__":
    almacen = Inventario("Almacén Norte")

    almacen.recibir("BL-220", "SM-4471", piezas=4, avisar=True)
    almacen.recibir("EM-905", piezas=30)
    almacen.recibir("BL-220")

    for renglon in almacen.listado():
        print(renglon)

    print(almacen)
```
**Salida**
```text
2 claves recibidas en Almacén Norte
BL-220 x5
SM-4471 x4
EM-905 x30
Almacén Norte: 3 claves, 39 piezas
```
**Rúbrica** (suma 10)
| Criterio | Puntos |
|---|---|
| *claves recoge cuantas lleguen y **opciones lee piezas y avisar con get | 4 |
| BL-220 acumula 4 más 1 y queda en 5 | 2 |
| El diccionario es privado y solo se ve por listado y __str__ | 2 |
| El bloque de prueba no corre al importar el módulo | 2 |

**Error que más se ve**
Leen las opciones con corchetes en lugar de `get`: la segunda llamada, que no pasa `avisar`, muere con `KeyError`.

## Semana 06 · Tema 3 · Propiedades fundamentales

### 06.1 · Reconocer
**Solución**
```text
La promesa no se cumplió. El getter devolvió la lista misma, no una copia,
así que el append de fuera escribió directo en el atributo privado y se
saltó el upper. Los dos guiones bajos protegieron el nombre del atributo, no
el objeto que hay adentro.
```
```python
    def entradas(self):
        return list(self.__entradas)
```
**Salida**
```text
2
FALLA EN B-101
todo bien
```
**Rúbrica** (suma 10)
| Criterio | Puntos |
|---|---|
| Las tres salidas | 4 |
| Dice que la promesa de mayúsculas se rompió y en cuál entrada | 2 |
| Explica la diferencia entre cerrar el nombre y cerrar el objeto | 2 |
| La corrección devuelve una copia | 2 |

**Error que más se ve**
Contestan `AttributeError` porque vieron los dos guiones bajos: el método está dentro de la clase, así que ve el atributo sin problema.

### 06.2 · Aplicar
**Solución**
```python
class ContadorDeFallas:
    def __init__(self) -> None:
        self.__fallas: dict[str, int] = {}

    def registrar(self, tag: str) -> None:
        clave = tag.upper()
        actual = self.__fallas.get(clave, 0)
        self.__fallas[clave] = actual + 1

    def __getitem__(self, tag: str) -> int:
        return self.__fallas.get(tag.upper(), 0)

    def __setitem__(self, tag: str, cuenta: int) -> None:
        self.__fallas[tag.upper()] = cuenta

    def __len__(self) -> int:
        return len(self.__fallas)


contador = ContadorDeFallas()

contador.registrar("B-101")
contador.registrar("b-101")
contador.registrar("C-310")

print(contador["B-101"])
print(contador["b-101"])
print(contador["V-12"])
print(len(contador))

contador["v-12"] = 5
print(contador["V-12"])
print(len(contador))
```
**Salida**
```text
2
2
0
2
5
3
```
**Rúbrica** (suma 10)
| Criterio | Puntos |
|---|---|
| __getitem__, __setitem__ y __len__ funcionando | 4 |
| La normalización a mayúsculas está en un solo lugar, dentro de la clase | 3 |
| Una etiqueta sin fallas devuelve 0 en vez de KeyError | 2 |
| El diccionario no se puede alcanzar desde fuera | 1 |

**Error que más se ve**
Normalizan en `registrar` y se les olvida en `__getitem__`: `contador["b-101"]` devuelve 0 aunque la falla esté guardada.

### 06.3 · Integrar
**Solución**
```python
class Sensor:
    def __init__(self, tag: str, minimo: float, maximo: float) -> None:
        self.tag = tag
        self.minimo = minimo
        self.maximo = maximo

    def en_rango(self, valor: float) -> bool:
        return valor >= self.minimo and valor <= self.maximo


class Bitacora:
    def __init__(self) -> None:
        self.__entradas: list[str] = []

    def registrar(self, texto: str) -> None:
        self.__entradas.append(texto.upper())

    def entradas(self) -> list:
        return list(self.__entradas)

    def __len__(self) -> int:
        return len(self.__entradas)


class Estacion:
    def __init__(self, nombre: str, sensores: dict, bitacora: Bitacora) -> None:
        self.nombre = nombre
        self.__sensores = sensores
        self.__bitacora = bitacora

    def medir(self, tag: str, valor: float) -> None:
        sensor = self.__sensores[tag]
        if not sensor.en_rango(valor):
            self.__bitacora.registrar(f"{tag} fuera de rango con {valor}")

    def historial(self) -> list:
        return self.__bitacora.entradas()


sensores = {
    "TT-101": Sensor("TT-101", 0.0, 400.0),
    "PT-205": Sensor("PT-205", 0.0, 10.0),
}

norte = Estacion("Planta Norte", sensores, Bitacora())

norte.medir("TT-101", 412.0)
norte.medir("PT-205", 6.1)
norte.medir("PT-205", 11.2)

norte.historial().append("entrada falsa")

for entrada in norte.historial():
    print(entrada)

print(len(norte.historial()))
```
**Salida**
```text
TT-101 FUERA DE RANGO CON 412.0
PT-205 FUERA DE RANGO CON 11.2
2
```
**Rúbrica** (suma 10)
| Criterio | Puntos |
|---|---|
| Estación recibe sus piezas y les delega, sin heredar de ninguna | 4 |
| La entrada falsa no entra, porque el historial devuelve copia | 3 |
| Solo se registra lo que quedó fuera de rango | 2 |
| Las tres clases se pueden probar por separado | 1 |

**Error que más se ve**
Hacen que `Estacion` herede de `Bitacora` para reusar `registrar`: la frase "una estación es una bitácora" no se sostiene, y la prueba de "es un" la tumba en voz alta.

## Semana 07 · Tema 3 · Propiedades fundamentales

### 07.1 · Reconocer
**Solución**
```text
Definir __init__ en la hija reemplaza al del padre. Como nadie llamó a
super().__init__(tag), Animal nunca corrió y el objeto nació sin tag ni
horas. caudal sí existe, por eso la primera línea imprime. La segunda muere
al leer self.tag.

La línea que falta es super().__init__(tag), y va como primera instrucción
del constructor de Bomba, antes de asignar caudal.
```
**Salida**
```text
120.0
Traceback (most recent call last):
  File "equipos.py", line 17, in <module>
    print(b101.ficha())
          ~~~~~~~~~~^^
  File "equipos.py", line 12, in ficha
    return f"{self.tag}: {self.caudal} L/s"
              ^^^^^^^^
AttributeError: 'Bomba' object has no attribute 'tag'
```
**Rúbrica** (suma 10)
| Criterio | Puntos |
|---|---|
| La primera línea imprime y la segunda truena | 3 |
| Nombra AttributeError y el atributo tag | 3 |
| Explica que el constructor de la hija reemplaza al del padre | 2 |
| Coloca super().__init__ al principio del constructor | 2 |

**Error que más se ve**
Contestan que el error es `TypeError` por argumentos: el constructor recibió los dos que pedía, el problema aparece después, al leer un atributo que nunca se creó.

### 07.2 · Aplicar
**Solución**
```python
class Equipo:
    def __init__(self, tag: str, horas: float) -> None:
        self._tag = tag
        self._horas = horas

    def resumen(self) -> str:
        return f"{self._tag} con {self._horas:.0f} h"

    def registrar_horas(self, corridas: float) -> None:
        self._horas += corridas


class Bomba(Equipo):
    def __init__(self, tag: str, horas: float, caudal: float) -> None:
        super().__init__(tag, horas)
        self.caudal = caudal

    def arrancar(self) -> str:
        return f"{self._tag} arranca a {self.caudal} L/s"


class Compresor(Equipo):
    def __init__(self, tag: str, horas: float, presion: float) -> None:
        super().__init__(tag, horas)
        self.presion = presion

    def purgar(self) -> str:
        return f"{self._tag} purga a {self.presion} bar"


b101 = Bomba("B-101", 4820.0, 120.0)
c310 = Compresor("C-310", 6300.0, 8.5)

print(b101.resumen())
print(b101.arrancar())

c310.registrar_horas(40)
print(c310.resumen())
print(c310.purgar())

print(isinstance(b101, Equipo), isinstance(b101, Compresor))
print(issubclass(Compresor, Equipo))
```
**Salida**
```text
B-101 con 4820 h
B-101 arranca a 120.0 L/s
C-310 con 6340 h
C-310 purga a 8.5 bar
True False
True
```
**Rúbrica** (suma 10)
| Criterio | Puntos |
|---|---|
| Las dos hijas cuelgan del mismo padre, no una de la otra | 3 |
| Los dos constructores encadenan con super | 3 |
| Los métodos propios leen el atributo protegido del padre | 2 |
| isinstance e issubclass contestan lo esperado | 2 |

**Error que más se ve**
Vuelven a asignar `self._tag` en la hija después de llamar a `super`: no rompe nada hoy, y esconde que el padre ya lo había hecho.

### 07.3 · Integrar
**Solución**
```text
La cadena de seis niveles se aplana así. Activo queda como padre, Bomba y
Compresor cuelgan de él, y Variador sale del árbol porque "un variador es
una bomba con variador" no se sostiene de ninguna manera: la bomba usa un
variador, no es uno. Eso es composición.

Activo -> Bomba: una bomba es un activo de la planta. Se sostiene.
Activo -> Compresor: un compresor es un activo de la planta. Se sostiene.
Bomba recibe un Variador: relación de uso, resuelta con un parámetro.
```
```python
class Variador:
    def __init__(self, marca: str, hz: float) -> None:
        self.marca = marca
        self.hz = hz

    def ajustar(self, hz: float) -> None:
        self.hz = hz


class Activo:
    def __init__(self, tag: str, horas: float) -> None:
        self._tag = tag
        self._horas = horas

    def resumen(self) -> str:
        return f"{self._tag} con {self._horas:.0f} h"


class Bomba(Activo):
    def __init__(self, tag: str, horas: float, caudal: float, variador=None) -> None:
        super().__init__(tag, horas)
        self.caudal = caudal
        self.variador = variador

    def arrancar(self) -> str:
        if self.variador is None:
            return f"{self._tag} arranca directo"
        return f"{self._tag} arranca a {self.variador.hz} Hz"


class Compresor(Activo):
    def __init__(self, tag: str, horas: float, presion: float) -> None:
        super().__init__(tag, horas)
        self.presion = presion


b101 = Bomba("B-101", 4820.0, 120.0)
b102 = Bomba("B-102", 1150.0, 120.0, Variador("Danfoss", 45.0))
c310 = Compresor("C-310", 6300.0, 8.5)

print(b101.resumen())
print(b101.arrancar())
print(b102.arrancar())

b102.variador.ajustar(38.0)
print(b102.arrancar())

print(c310.resumen())
print(isinstance(b102, Activo), isinstance(b102.variador, Activo))
```
**Salida**
```text
B-101 con 4820 h
B-101 arranca directo
B-102 arranca a 45.0 Hz
B-102 arranca a 38.0 Hz
C-310 con 6300 h
True False
```
**Rúbrica** (suma 10)
| Criterio | Puntos |
|---|---|
| Ninguna rama pasa de dos niveles | 3 |
| Variador sale del árbol y entra por el constructor | 3 |
| Una justificación por relación conservada, con la frase de tipo | 2 |
| El caso sin variador funciona y no truena con None | 2 |

**Error que más se ve**
Dejan `BombaDosificadora` colgando de `Bomba` "porque sí es una bomba": la relación se sostiene, pero el enunciado pide dos niveles, y la dosificación cabe como un atributo.

## Semana 08 · Tema 3 · Propiedades fundamentales

### 08.1 · Reconocer
**Solución**
```text
reporte está escrito en Equipo, pero self conserva la clase real del objeto.
Python busca consumo_kw empezando por esa clase, no por la clase donde se
escribió el método. V-12 se queda con la versión del padre, M-204 usa la de
Motor y C-310 la de Compresor. Compresor además sobrescribe reporte y lo
extiende: super().reporte() imprime la línea del padre y después agrega la
suya.

Si la llamada a super fuera al final, primero saldría "revisar filtro" y
después el renglón con los kW.
```
**Salida**
```text
V-12: 0.0 kW
M-204: 45.0 kW
C-310: 75.0 kW
C-310: revisar filtro
```
**Rúbrica** (suma 10)
| Criterio | Puntos |
|---|---|
| Las cuatro líneas, en orden | 4 |
| Dice que self manda sobre dónde está escrito el método | 3 |
| Explica qué hace super dentro de un método sobrescrito | 2 |
| Contesta bien el cambio de orden | 1 |

**Error que más se ve**
Contestan 0.0 kW para los tres porque `reporte` vive en `Equipo`: es exactamente la confusión que el ejercicio busca.

### 08.2 · Aplicar
**Solución**
```python
from abc import ABC, abstractmethod


class Instrumento(ABC):
    def __init__(self, tag: str) -> None:
        self.tag = tag
        self.calibrado = False

    def calibrar(self) -> None:
        self.calibrado = True

    @abstractmethod
    def leer(self) -> str:
        ...


class Termopar(Instrumento):
    def leer(self) -> str:
        return f"{self.tag}: 74.5 C"


class Manometro(Instrumento):
    def leer(self) -> str:
        return f"{self.tag}: 6.1 bar"


class Caudalimetro(Instrumento):
    def leer(self) -> str:
        return f"{self.tag}: 118.0 L/s"


tablero = [Termopar("TT-101"), Manometro("PT-205"), Caudalimetro("FT-330")]

for instrumento in tablero:
    instrumento.calibrar()
    print(instrumento.leer(), instrumento.calibrado)

try:
    suelto = Instrumento("XX-000")
except TypeError as ex:
    print("Rechazado:", ex)
```
**Salida**
```text
TT-101: 74.5 C True
PT-205: 6.1 bar True
FT-330: 118.0 L/s True
Rechazado: Can't instantiate abstract class Instrumento without an implementation for abstract method 'leer'
```
**Rúbrica** (suma 10)
| Criterio | Puntos |
|---|---|
| ABC y @abstractmethod juntos, no uno solo | 3 |
| Las tres hijas implementan leer y heredan calibrar | 3 |
| El ciclo no pregunta el tipo de ningún objeto | 2 |
| La clase abstracta no se deja construir | 2 |

**Error que más se ve**
Ponen `@abstractmethod` sin heredar de `ABC`: la clase se construye como si nada y el `try` del final no imprime nunca.

### 08.3 · Integrar
**Solución**
```python
from abc import ABC, abstractmethod


class Equipo(ABC):
    censo = 0

    def __init__(self, tag: str, horas: float) -> None:
        self._tag = tag
        self.__horas = horas
        Equipo.censo += 1

    @property
    def tag(self) -> str:
        return self._tag

    @property
    def horas(self) -> float:
        return self.__horas

    def registrar_horas(self, corridas: float) -> None:
        if corridas < 0:
            raise ValueError("Las horas corridas no pueden ser negativas")
        self.__horas += corridas

    @abstractmethod
    def consumo_kw(self) -> float:
        ...

    def reporte(self) -> str:
        return f"{self._tag}: {self.horas:.0f} h, {self.consumo_kw():.1f} kW"


class Bomba(Equipo):
    def __init__(self, tag: str, horas: float, caudal: float) -> None:
        super().__init__(tag, horas)
        self.caudal = caudal

    def consumo_kw(self) -> float:
        return self.caudal * 0.32


class Compresor(Equipo):
    def __init__(self, tag: str, horas: float, presion: float) -> None:
        super().__init__(tag, horas)
        self.presion = presion

    def consumo_kw(self) -> float:
        return self.presion * 8.0

    def reporte(self) -> str:
        return super().reporte() + " (aire)"


class Valvula(Equipo):
    def __init__(self, tag: str, horas: float) -> None:
        super().__init__(tag, horas)


planta = [Bomba("B-101", 4820.0, 120.0), Compresor("C-310", 6300.0, 8.5)]

total = 0.0
for equipo in planta:
    print(equipo.reporte())
    total += equipo.consumo_kw()

print(f"Consumo total: {total:.1f} kW")

planta[0].registrar_horas(180)
print(planta[0].reporte())

try:
    planta[0].registrar_horas(-5)
except ValueError as ex:
    print("Rechazado:", ex)

try:
    v12 = Valvula("V-12", 300.0)
except TypeError as ex:
    print("Rechazado:", ex)

print("Equipos construidos:", Equipo.censo)
```
**Salida**
```text
B-101: 4820 h, 38.4 kW
C-310: 6300 h, 68.0 kW (aire)
Consumo total: 106.4 kW
B-101: 5000 h, 38.4 kW
Rechazado: Las horas corridas no pueden ser negativas
Rechazado: Can't instantiate abstract class Valvula without an implementation for abstract method 'consumo_kw'
Equipos construidos: 2
```
**Rúbrica** (suma 10)
| Criterio | Puntos |
|---|---|
| Abstracta con método abstracto y método concreto que lo usa | 3 |
| Horas privadas, propiedades de solo lectura y validación en el método | 3 |
| El ciclo suma consumos sin preguntar tipos | 2 |
| Compresor extiende reporte con super, y la válvula no se deja construir | 2 |

**Error que más se ve**
La válvula sí se construye porque le pusieron un `consumo_kw` que devuelve 0: el censo entonces marca 3 y el contrato dejó de servir para lo que servía.

## Semana 09 · Tema 4 · Funciones y estructuras avanzadas

### 09.1 · Reconocer
**Solución**
```text
La lista del valor por omisión se creó una sola vez, en el momento de
ejecutar el def, y todas las llamadas que no pasan historial escriben en
ella. La tercera llamada recibe una lista propia y por eso sale sola. La
cuarta vuelve a la compartida, que ya traía dos etiquetas.
```
```python
def registrar_falla(tag, historial=None):
    if historial is None:
        historial = []
    historial.append(tag)
    return historial
```
**Salida**
```text
['B-101']
['B-101', 'C-310']
['V-12']
['B-101', 'C-310', 'M-204']
```
**Rúbrica** (suma 10)
| Criterio | Puntos |
|---|---|
| Las cuatro salidas | 4 |
| Dice que la lista se creó al definir la función | 3 |
| La corrección usa None y crea la lista adentro | 3 |

**Error que más se ve**
Contestan que la cuarta línea trae una etiqueta sola porque la tercera "reinició" la lista: la tercera nunca tocó la compartida.

### 09.2 · Aplicar
**Solución**
```python
refacciones = [
    ("BL-220", "balero", 12),
    ("SM-4471", "sello mecánico", 6),
    ("EM-905", "empaque", 30),
    ("RT-118", "retén", 2),
]


def por_existencia(refacciones: list) -> list:
    copia = list(refacciones)
    copia.sort(key=lambda r: r[2])
    return copia


def criticas(refacciones: list, minimo: int) -> list:
    claves = []
    for clave, descripcion, piezas in refacciones:
        if piezas < minimo:
            claves.append(clave)
    return claves


def imprimir(refacciones: list) -> None:
    for numero, refaccion in enumerate(por_existencia(refacciones), start=1):
        clave, descripcion, piezas = refaccion
        print(f"{numero}. {clave} {descripcion}: {piezas}")


imprimir(refacciones)
print(criticas(refacciones, 5))
print(refacciones[0][0])
```
**Salida**
```text
1. RT-118 retén: 2
2. SM-4471 sello mecánico: 6
3. BL-220 balero: 12
4. EM-905 empaque: 30
['RT-118']
BL-220
```
**Rúbrica** (suma 10)
| Criterio | Puntos |
|---|---|
| sort con key y lambda sobre el tercer elemento | 3 |
| La lista original queda intacta, y la última línea lo demuestra | 3 |
| criticas devuelve y no imprime | 2 |
| enumerate numera desde 1 | 2 |

**Error que más se ve**
Escriben `copia = refacciones.sort(...)`: `sort` devuelve `None`, la variable queda en `None` y el `enumerate` truena.

### 09.3 · Integrar
**Solución**
```python
BOMBA = {
    "nombre": "B-101",
    "piezas": 1,
    "partes": [
        {
            "nombre": "conjunto rotor",
            "piezas": 1,
            "partes": [
                {"nombre": "impulsor", "piezas": 1, "partes": []},
                {"nombre": "balero BL-220", "piezas": 2, "partes": []},
            ],
        },
        {"nombre": "sello SM-4471", "piezas": 2, "partes": []},
        {"nombre": "tornillo", "piezas": 8, "partes": []},
    ],
}


def contar_piezas(nodo: dict) -> int:
    total = nodo["piezas"]
    for parte in nodo["partes"]:
        total += contar_piezas(parte)
    return total


def profundidad(nodo: dict) -> int:
    mayor = 0
    for parte in nodo["partes"]:
        nivel = profundidad(parte)
        if nivel > mayor:
            mayor = nivel
    return mayor + 1


def hojas(nodo: dict, encontradas: list = None) -> list:
    if encontradas is None:
        encontradas = []
    if len(nodo["partes"]) == 0:
        encontradas.append(nodo["nombre"])
    for parte in nodo["partes"]:
        hojas(parte, encontradas)
    return encontradas


print(contar_piezas(BOMBA))
print(profundidad(BOMBA))
print(hojas(BOMBA))
```
**Salida**
```text
15
3
['impulsor', 'balero BL-220', 'sello SM-4471', 'tornillo']
```
**Rúbrica** (suma 10)
| Criterio | Puntos |
|---|---|
| Las tres funciones son recursivas y cada una tiene caso base | 4 |
| contar_piezas da 15 y profundidad da 3 | 3 |
| hojas devuelve las cuatro en orden y sin repetir el nodo raíz | 2 |
| El acumulador no es el valor por omisión del parámetro | 1 |

**Error que más se ve**
`profundidad` devuelve 2 porque cuenta solo el primer nivel de partes: se delata en cuanto se prueba con un árbol de un solo nodo, donde debe dar 1.

## Semana 10 · Tema 4 · Funciones y estructuras avanzadas

### 10.1 · Reconocer
**Solución**
```text
respaldo y lecturas son dos nombres para la misma lista, así que el append
deja seis elementos en las dos. El conjunto descarta repetidos y queda con
74.5, 118.0 y 6.1. El acumulador cuenta dos veces el 118.0 y dos veces el
6.1, porque el segundo 6.1 entró con el append. Con list(lecturas) habría
dos listas: el append tocaría solo el respaldo, lecturas seguiría en cinco
y el conteo del 6.1 sería 1.
```
**Salida**
```text
6 3
2 2
True
0
```
**Rúbrica** (suma 10)
| Criterio | Puntos |
|---|---|
| Las cuatro salidas | 4 |
| Explica por qué len(lecturas) es 6 y no 5 | 3 |
| Dice qué cambiaría con list(lecturas) | 2 |
| Menciona que get devuelve el valor por omisión sin levantar KeyError | 1 |

**Error que más se ve**
Contestan `5 3` en la primera línea: se les fue que el append entró por el otro nombre.

### 10.2 · Aplicar
**Solución**
```python
fallas = [
    ("B-101", "vibración"),
    ("C-310", "sobrecalentamiento"),
    ("B-101", "fuga"),
    ("V-12", "fuga"),
    ("B-101", "vibración"),
]

lecturas = [74.5, 118.0, 6.1, 203.0, 99.9, 118.0]

fugas = [tag for tag, tipo in fallas if tipo == "fuga"]

conteo = {}
for tag, tipo in fallas:
    conteo[tag] = conteo.get(tag, 0) + 1

altas = [valor for valor in lecturas if valor > 100]

print(fugas)
print(conteo)
print(altas)
print(sorted(set(fugas)))
```
**Salida**
```text
['B-101', 'V-12']
{'B-101': 3, 'C-310': 1, 'V-12': 1}
[118.0, 203.0, 118.0]
['B-101', 'V-12']
```
**Rúbrica** (suma 10)
| Criterio | Puntos |
|---|---|
| Las dos comprensiones con su condición | 4 |
| El acumulador usa get con valor por omisión 0 | 3 |
| El 118.0 repetido aparece dos veces en las altas | 2 |
| Las etiquetas sin repetir salen de un conjunto ordenado | 1 |

**Error que más se ve**
Escriben la comprensión con `if` y `else` para el conteo: la comprensión filtra, y contar por llave pide el diccionario acumulador.

### 10.3 · Integrar
**Solución**
```python
class Padron:
    def __init__(self, equipos: list) -> None:
        self.__equipos = list(equipos)
        self.__por_tag = {}
        etiquetas = []
        for equipo in equipos:
            self.__por_tag[equipo["tag"]] = equipo
            etiquetas.append(equipo["tag"])
        self.__tags = set(etiquetas)

    def existe(self, tag: str) -> bool:
        return tag in self.__tags

    def horas(self, tag: str) -> float:
        equipo = self.__por_tag.get(tag)
        if equipo is None:
            return 0.0
        return equipo["horas"]

    def ordenados(self) -> list:
        return sorted([e["tag"] for e in self.__equipos])

    def por_tipo(self) -> dict:
        conteo = {}
        for equipo in self.__equipos:
            conteo[equipo["tipo"]] = conteo.get(equipo["tipo"], 0) + 1
        return conteo

    def vencidos(self, limite: float) -> list:
        return [e["tag"] for e in self.__equipos if e["horas"] > limite]


equipos = [
    {"tag": "B-101", "tipo": "bomba", "horas": 4820.0},
    {"tag": "B-102", "tipo": "bomba", "horas": 1150.0},
    {"tag": "C-310", "tipo": "compresor", "horas": 6300.0},
    {"tag": "M-204", "tipo": "motor", "horas": 2210.0},
    {"tag": "V-12", "tipo": "válvula", "horas": 300.0},
]

padron = Padron(equipos)

print(padron.existe("C-310"), padron.existe("X-999"))
print(padron.horas("B-101"))
print(padron.ordenados())
print(padron.por_tipo())
print(padron.vencidos(5000))
```
**Salida**
```text
True False
4820.0
['B-101', 'B-102', 'C-310', 'M-204', 'V-12']
{'bomba': 2, 'compresor': 1, 'motor': 1, 'válvula': 1}
['C-310']
```
**Rúbrica** (suma 10)
| Criterio | Puntos |
|---|---|
| Conjunto para pertenencia y diccionario para búsqueda por llave | 4 |
| Las estructuras son privadas y se arman una sola vez en el constructor | 2 |
| horas devuelve 0.0 sin levantar KeyError | 2 |
| La justificación nombra el contenedor y la razón, método por método | 2 |

**Error que más se ve**
`existe` recorre la lista con un `for` y un `return True` adentro: contesta bien y es justo la consulta que el conjunto resuelve sin recorrer nada.

## Semana 11 · Tema 4 · Funciones y estructuras avanzadas

### 11.1 · Reconocer
**Solución**
```text
finally corre siempre, incluso cuando ya hay un return esperando turno. El
valor se guarda, el bloque imprime, y solo entonces la función devuelve. Por
eso "intento" aparece antes que el número en las tres llamadas.

float("s/d") levanta ValueError, que es el primer except y el único que se
revisa: en cuanto uno coincide, los demás ni se miran.
```
**Salida**
```text
intento 4
25.0
intento 0
0.0
intento s/d
-1.0
```
**Rúbrica** (suma 10)
| Criterio | Puntos |
|---|---|
| Las seis líneas en el orden correcto | 5 |
| Explica que finally corre antes de devolver | 3 |
| Nombra ValueError y dice por qué el segundo except no se revisa | 2 |

**Error que más se ve**
Ponen el número antes del "intento" en cada par: el `return` parece salir primero al leerlo, y `finally` se cuela en medio.

### 11.2 · Aplicar
**Solución**
```python
class LecturaFueraDeRango(Exception):
    pass


class Sensor:
    def __init__(self, tag: str, minimo: float, maximo: float) -> None:
        self.tag = tag
        self.minimo = minimo
        self.maximo = maximo
        self.__valor = minimo

    @property
    def valor(self) -> float:
        return self.__valor

    @valor.setter
    def valor(self, lectura: float) -> None:
        if lectura < self.minimo or lectura > self.maximo:
            raise LecturaFueraDeRango(
                f"{self.tag} midió {lectura} y su rango es {self.minimo} a {self.maximo}")
        self.__valor = lectura


tt101 = Sensor("TT-101", 0.0, 400.0)

for lectura in [74.5, 412.0, 180.0]:
    try:
        tt101.valor = lectura
    except LecturaFueraDeRango as ex:
        print(type(ex).__name__)
        print(ex)
    else:
        print(f"{tt101.tag} aceptado: {tt101.valor}")

print(f"Último valor guardado: {tt101.valor}")
```
**Salida**
```text
TT-101 aceptado: 74.5
LecturaFueraDeRango
TT-101 midió 412.0 y su rango es 0.0 a 400.0
TT-101 aceptado: 180.0
Último valor guardado: 180.0
```
**Rúbrica** (suma 10)
| Criterio | Puntos |
|---|---|
| La excepción propia hereda de Exception y se atrapa por su nombre | 3 |
| La validación vive en el setter, no en el ciclo que llama | 3 |
| El else imprime solo cuando la asignación pasó | 2 |
| El valor rechazado no queda guardado | 2 |

**Error que más se ve**
Validan en el ciclo con un `if` antes de asignar: funciona en esta prueba y deja el sensor abierto para cualquier otro archivo que le escriba directo.

### 11.3 · Integrar
**Solución**
```python
crudas = [
    ("TT-101", "74.5"),
    ("PT-205", "6.1"),
    ("TT-101", "412.0"),
    ("XX-999", "12.0"),
    ("FT-330", "s/d"),
    ("PT-205", None),
    ("FT-330", "118.0"),
]


class LecturaInvalida(Exception):
    pass


class LecturaFueraDeRango(LecturaInvalida):
    pass


class SensorDesconocido(LecturaInvalida):
    pass


RANGOS = {
    "TT-101": (0.0, 400.0),
    "PT-205": (0.0, 10.0),
    "FT-330": (0.0, 200.0),
}


def validar(tag: str, texto) -> float:
    if tag not in RANGOS:
        raise SensorDesconocido(f"{tag} no está en el tablero")
    if texto is None:
        raise LecturaInvalida(f"{tag} no envió nada")
    try:
        valor = float(texto)
    except ValueError:
        raise LecturaInvalida(f"{tag} envió {texto} y no es un número")
    minimo, maximo = RANGOS[tag]
    if valor < minimo or valor > maximo:
        raise LecturaFueraDeRango(f"{tag} midió {valor} fuera de {minimo} a {maximo}")
    return valor


aceptadas = []
rechazadas = 0

for tag, texto in crudas:
    try:
        aceptadas.append((tag, validar(tag, texto)))
    except LecturaFueraDeRango as ex:
        rechazadas += 1
        print("Fuera de rango:", ex)
    except SensorDesconocido as ex:
        rechazadas += 1
        print("Sin registrar:", ex)
    except LecturaInvalida as ex:
        rechazadas += 1
        print("Dato malo:", ex)

print(f"Aceptadas: {len(aceptadas)}  Rechazadas: {rechazadas}")

suma = 0.0
for tag, valor in aceptadas:
    suma += valor

print(f"Promedio de lo aceptado: {suma / len(aceptadas):.2f}")
```
**Salida**
```text
Fuera de rango: TT-101 midió 412.0 fuera de 0.0 a 400.0
Sin registrar: XX-999 no está en el tablero
Dato malo: FT-330 envió s/d y no es un número
Dato malo: PT-205 no envió nada
Aceptadas: 3  Rechazadas: 4
Promedio de lo aceptado: 66.20
```
**Rúbrica** (suma 10)
| Criterio | Puntos |
|---|---|
| Las tres excepciones propias, con la jerarquía que permite atraparlas juntas | 3 |
| Los except van del más específico al más general | 3 |
| Toda la validación está en una función, en la frontera | 2 |
| Cada mensaje dice qué corregir, y el conteo final cuadra | 2 |

**Error que más se ve**
Ponen `except LecturaInvalida` arriba de los otros dos: atrapa todo y los mensajes específicos nunca se imprimen, porque las dos hijas son también la madre.

## Semana 12 · Tema 5 · Archivos

### 12.1 · Reconocer
**Solución**
```text
El modo w vacía el archivo en el instante de abrirlo, antes de escribir un
solo carácter. La tercera apertura borró los dos renglones anteriores. La
única que conservó lo que había fue la segunda, con modo a.

Lo que queda son 19 caracteres: los 18 del renglón más el salto de línea.
El print del contenido agrega su propio salto, por eso aparece un renglón
en blanco antes del número.
```
**Salida**
```text
11:40 C-310 alarma

19
```
**Rúbrica** (suma 10)
| Criterio | Puntos |
|---|---|
| Solo queda el renglón de las 11:40 | 4 |
| Dice que el borrado ocurre al abrir, no al escribir | 3 |
| El 19 cuenta el salto de línea | 2 |
| Identifica el modo a como el único que conservó | 1 |

**Error que más se ve**
Contestan 18 porque cuentan las letras a mano: el `\n` del final también es un carácter.

### 12.2 · Aplicar
**Solución**
```python
import csv
from pathlib import Path

ruta = Path("telemetria.csv")

filas = [
    {"tag": "TT-101", "valor": 74.5},
    {"tag": "PT-205", "valor": 6.1},
    {"tag": "TT-101", "valor": 81.2},
    {"tag": "FT-330", "valor": 118.0},
    {"tag": "PT-205", "valor": 6.4},
]

with open(ruta, "w", newline="", encoding="utf-8") as archivo:
    escritor = csv.DictWriter(archivo, fieldnames=["tag", "valor"])
    escritor.writeheader()
    escritor.writerows(filas)

sumas = {}
cuentas = {}

with open(ruta, newline="", encoding="utf-8") as archivo:
    lector = csv.DictReader(archivo)
    for fila in lector:
        tag = fila["tag"]
        sumas[tag] = sumas.get(tag, 0.0) + float(fila["valor"])
        cuentas[tag] = cuentas.get(tag, 0) + 1

for tag, suma in sumas.items():
    print(f"{tag}: {suma / cuentas[tag]:.2f} (n={cuentas[tag]})")
```
**Salida**
```text
TT-101: 77.85 (n=2)
PT-205: 6.25 (n=2)
FT-330: 118.00 (n=1)
```
**Rúbrica** (suma 10)
| Criterio | Puntos |
|---|---|
| DictWriter con encabezado y DictReader por nombre de columna | 3 |
| Los dos accesos con with, newline vacío y encoding explícito | 3 |
| Dos acumuladores, sumas y conteos, con get | 2 |
| La conversión a float ocurre al leer, porque el CSV entrega texto | 2 |

**Error que más se ve**
Suman `fila["valor"]` sin convertir: el CSV devuelve cadenas, así que la suma concatena y el promedio truena al dividir.

### 12.3 · Integrar
**Solución**
```python
import csv
from pathlib import Path


class Bitacora:
    CAMPOS = ["hora", "tag", "texto"]

    def __init__(self, ruta: Path) -> None:
        self.ruta = ruta

    def registrar(self, hora: str, tag: str, texto: str) -> None:
        nuevo = not self.ruta.exists()
        with open(self.ruta, "a", newline="", encoding="utf-8") as archivo:
            escritor = csv.DictWriter(archivo, fieldnames=Bitacora.CAMPOS)
            if nuevo:
                escritor.writeheader()
            escritor.writerow({"hora": hora, "tag": tag, "texto": texto})

    def entradas(self) -> list:
        try:
            with open(self.ruta, newline="", encoding="utf-8") as archivo:
                return list(csv.DictReader(archivo))
        except FileNotFoundError:
            return []

    def reporte(self, destino: Path) -> None:
        conteo = {}
        for entrada in self.entradas():
            conteo[entrada["tag"]] = conteo.get(entrada["tag"], 0) + 1
        with open(destino, "w", encoding="utf-8") as archivo:
            archivo.write("Eventos por equipo\n")
            for tag, veces in conteo.items():
                archivo.write(f"{tag}: {veces}\n")


bitacora = Bitacora(Path("bitacora.csv"))

bitacora.registrar("08:00", "B-101", "arranque normal")
bitacora.registrar("09:15", "PT-205", "lectura 6.1 bar")
bitacora.registrar("11:40", "C-310", "alarma de temperatura")
bitacora.registrar("13:05", "B-101", "paro por mantenimiento")

print(len(bitacora.entradas()))
for entrada in bitacora.entradas():
    print(entrada["hora"], entrada["tag"], entrada["texto"])

destino = Path("reporte.txt")
bitacora.reporte(destino)
print(destino.read_text(encoding="utf-8"))

perdida = Bitacora(Path("no-existe.csv"))
print(len(perdida.entradas()))
```
**Salida**
```text
4
08:00 B-101 arranque normal
09:15 PT-205 lectura 6.1 bar
11:40 C-310 alarma de temperatura
13:05 B-101 paro por mantenimiento
Eventos por equipo
B-101: 2
PT-205: 1
C-310: 1

0
```
**Rúbrica** (suma 10)
| Criterio | Puntos |
|---|---|
| Modo a para agregar, con el encabezado escrito una sola vez | 3 |
| FileNotFoundError atrapado por su nombre y lista vacía de vuelta | 3 |
| El reporte agrupa por equipo y sale a un archivo nuevo | 2 |
| Todas las rutas son Path y todas las aperturas llevan encoding | 2 |

**Error que más se ve**
Escriben el encabezado en cada llamada a `registrar`: el CSV queda con cuatro renglones de encabezado y `DictReader` los lee como si fueran eventos.

## Semana 13 · Tema 5 · Archivos

### 13.1 · Reconocer
**Solución**
```text
El archivo tiene 15 bytes y las posiciones se cuentan desde cero. Al abrir,
el cursor está en 0. seek(5) lo deja justo antes de la sexta letra, y read(5)
devuelve B-102 y deja el cursor en 10. seek(10) y read(5) devuelven C-310 y
dejan el cursor en 15, que es el final. La última lectura no encuentra nada
y devuelve una cadena de bytes vacía, sin levantar ningún error.
```
**Salida**
```text
0
b'B-102'
10
b'C-310'
b''
```
**Rúbrica** (suma 10)
| Criterio | Puntos |
|---|---|
| Las cinco salidas, con la b de bytes | 5 |
| Explica que leer avanza el cursor y seek lo coloca | 3 |
| Dice que al final se devuelve vacío en lugar de un error | 2 |

**Error que más se ve**
Escriben `'B-102'` sin la `b`: en modo binario lo que llega son bytes, y esa letra es la mitad del punto de la sesión.

### 13.2 · Aplicar
**Solución**
```python
from pathlib import Path

TAM = 32
ruta = Path("equipos.bin")

equipos = ["B-101", "B-102", "C-310", "M-204"]

with open(ruta, "wb") as archivo:
    for tag in equipos:
        archivo.write(f"{tag:<32}".encode("utf-8"))


def leer_registro(ruta: Path, numero: int) -> str:
    with open(ruta, "rb") as archivo:
        archivo.seek(numero * TAM)
        crudo = archivo.read(TAM)
    return crudo.decode("utf-8").strip()


print(len(equipos) * TAM)
print(leer_registro(ruta, 2))
print(leer_registro(ruta, 0))
print(leer_registro(ruta, 3))
```
**Salida**
```text
128
C-310
B-101
M-204
```
**Rúbrica** (suma 10)
| Criterio | Puntos |
|---|---|
| Cada registro mide exactamente 32 bytes | 3 |
| La posición se calcula con número por tamaño, y se salta con seek | 3 |
| Codificar al escribir y decodificar al leer, en UTF-8 | 2 |
| El relleno se quita al devolver la etiqueta | 2 |

**Error que más se ve**
Escriben sin rellenar y los registros quedan de cinco bytes: la multiplicación por 32 apunta a media etiqueta y todo lo que sale después está corrido.

### 13.3 · Integrar
**Solución**
```python
import csv
from pathlib import Path

TAM = 40


class IndiceVacio(Exception):
    pass


def leer_lecturas(ruta: Path) -> list:
    try:
        with open(ruta, newline="", encoding="utf-8") as archivo:
            return list(csv.DictReader(archivo))
    except FileNotFoundError:
        return []


def resumir(lecturas: list) -> dict:
    sumas = {}
    cuentas = {}
    for fila in lecturas:
        tag = fila["tag"]
        try:
            valor = float(fila["valor"])
        except ValueError:
            print(f"Descartada: {tag} envió {fila['valor']}")
            continue
        sumas[tag] = sumas.get(tag, 0.0) + valor
        cuentas[tag] = cuentas.get(tag, 0) + 1
    promedios = {}
    for tag, suma in sumas.items():
        promedios[tag] = suma / cuentas[tag]
    return promedios


def escribir_indice(ruta: Path, promedios: dict) -> None:
    if len(promedios) == 0:
        raise IndiceVacio("No hay promedios que indexar")
    with open(ruta, "wb") as archivo:
        for tag, promedio in promedios.items():
            registro = f"{tag:<10}{promedio:>10.2f}"
            archivo.write(f"{registro:<40}".encode("utf-8"))


def leer_indice(ruta: Path, numero: int) -> str:
    with open(ruta, "rb") as archivo:
        archivo.seek(numero * TAM)
        crudo = archivo.read(TAM)
    if len(crudo) < TAM:
        raise IndexError(f"No existe el registro {numero}")
    return crudo.decode("utf-8").strip()


filas = [
    {"tag": "TT-101", "valor": "74.5"},
    {"tag": "PT-205", "valor": "6.1"},
    {"tag": "TT-101", "valor": "81.2"},
    {"tag": "FT-330", "valor": "118.0"},
    {"tag": "PT-205", "valor": "s/d"},
]

origen = Path("telemetria.csv")
with open(origen, "w", newline="", encoding="utf-8") as archivo:
    escritor = csv.DictWriter(archivo, fieldnames=["tag", "valor"])
    escritor.writeheader()
    escritor.writerows(filas)

lecturas = leer_lecturas(origen)
promedios = resumir(lecturas)

print(len(lecturas), len(promedios))
for tag, promedio in promedios.items():
    print(f"{tag}: {promedio:.2f}")

indice = Path("promedios.bin")
escribir_indice(indice, promedios)

print(leer_indice(indice, 1))
print(leer_indice(indice, 0))

try:
    print(leer_indice(indice, 9))
except IndexError as ex:
    print("Rechazado:", ex)

try:
    escribir_indice(Path("vacio.bin"), {})
except IndiceVacio as ex:
    print("Rechazado:", ex)
```
**Salida**
```text
Descartada: PT-205 envió s/d
5 3
TT-101: 77.85
PT-205: 6.10
FT-330: 118.00
PT-205          6.10
TT-101         77.85
Rechazado: No existe el registro 9
Rechazado: No hay promedios que indexar
```
**Rúbrica** (suma 10)
| Criterio | Puntos |
|---|---|
| El CSV se lee con DictReader y el archivo faltante devuelve lista vacía | 2 |
| El promedio descarta la fila mala sin cortar el recorrido, y avisa | 3 |
| Los registros del índice miden 40 bytes y se leen con seek | 3 |
| Las dos excepciones, la propia y la de índice, con mensaje propio | 2 |

**Error que más se ve**
Calculan el promedio sobre la lista en memoria y escriben el índice sin verificar el tamaño: pedir el registro 9 devuelve una cadena vacía en lugar de un error, y nadie se entera de que la consulta falló.

## Semana 14 · Tema 6 · Interfaces gráficas

Las soluciones 14.2 y 14.3 abren ventana y no se ejecutaron en la máquina de revisión. Están escritas contra la API de PyQt6 y revisadas línea por línea; la parte de dominio de 14.3 sí corre y su salida es real.

### 14.1 · Reconocer
**Solución**
```text
Los paréntesis llaman al método en ese momento, durante la construcción de
la ventana. Por eso "clic" se imprime una sola vez y antes de que aparezca
nada en pantalla. El método no devuelve nada, así que connect recibe None y
la construcción falla con TypeError, porque None no se puede llamar después.

Aunque el connect estuviera bien, el botón es una variable local del
constructor: al terminar __init__ nadie lo referencia y Python lo recolecta,
así que la ventana abre vacía. Los controles se guardan sobre self.
```
```python
        self.boton = QPushButton("Consultar", self)
        self.boton.clicked.connect(self.al_consultar)
```
**Salida**
```text
clic
```
Después de esa línea la construcción termina con `TypeError`, porque `connect` recibió `None` en lugar de algo que se pueda llamar.

**Rúbrica** (suma 10)
| Criterio | Puntos |
|---|---|
| "clic" se imprime una vez, al construir | 3 |
| connect recibe None y la construcción falla | 3 |
| La corrección quita los paréntesis | 2 |
| Detecta que el botón no se guardó sobre self | 2 |

**Error que más se ve**
Contestan que se imprime en cada clic: es lo que dice la intención del código, no lo que dice el paréntesis.

### 14.2 · Aplicar
**Solución**
```python
import sys

from PyQt6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
                             QPushButton, QWidget)


def normalizar(tag: str) -> str:
    limpio = tag.strip().upper()
    if len(limpio) == 0:
        return "Sin capturar"
    return limpio


class VentanaTag(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Normalizador de tags")
        self.setGeometry(200, 200, 380, 140)

        central = QWidget(self)
        self.setCentralWidget(central)

        self.caja = QLineEdit(central)
        self.caja.setPlaceholderText("b-101")
        self.caja.setGeometry(20, 20, 220, 28)

        self.boton = QPushButton("Normalizar", central)
        self.boton.setGeometry(250, 20, 110, 28)

        self.resultado = QLabel("Sin capturar", central)
        self.resultado.setGeometry(20, 70, 340, 28)

        self.boton.clicked.connect(self.al_normalizar)

    def al_normalizar(self) -> None:
        self.resultado.setText(normalizar(self.caja.text()))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaTag()
    ventana.show()
    sys.exit(app.exec())
```
**Salida**
```text
La ventana abre con la caja vacía y la etiqueta en "Sin capturar".
Al escribir "  b-101 " y oprimir Normalizar, la etiqueta muestra B-101.
Con la caja vacía, la etiqueta vuelve a "Sin capturar".
```
**Rúbrica** (suma 10)
| Criterio | Puntos |
|---|---|
| La ventana es una clase que hereda de QMainWindow y encadena super | 3 |
| Los tres controles se guardan sobre self y cuelgan del widget central | 3 |
| connect sin paréntesis, a un método de la ventana | 2 |
| El slot no calcula: llama a normalizar y muestra el resultado | 2 |

**Error que más se ve**
Leen `self.caja.text()` dentro del constructor y guardan el resultado: en ese momento la caja está vacía, así que la etiqueta nunca cambia por más clics que reciba.

### 14.3 · Integrar
**Solución**
```python
class TagDesconocido(Exception):
    pass


class Tablero:
    def __init__(self) -> None:
        self.__lecturas = {}

    def registrar(self, tag: str, valor: float, unidad: str) -> None:
        self.__lecturas[tag.upper()] = (valor, unidad)

    def leer(self, tag: str) -> str:
        clave = tag.strip().upper()
        if clave not in self.__lecturas:
            raise TagDesconocido(f"{clave} no está en el tablero")
        valor, unidad = self.__lecturas[clave]
        return f"{clave}: {valor} {unidad}"


if __name__ == "__main__":
    tablero = Tablero()
    tablero.registrar("TT-101", 74.5, "C")
    tablero.registrar("PT-205", 6.1, "bar")

    print(tablero.leer("tt-101"))
    print(tablero.leer("  PT-205 "))

    try:
        print(tablero.leer("XX-999"))
    except TagDesconocido as ex:
        print("Rechazado:", ex)
```
```python
import sys

from PyQt6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
                             QPushButton, QWidget)

from tablero import Tablero, TagDesconocido


class VentanaTablero(QMainWindow):
    def __init__(self, tablero: Tablero) -> None:
        super().__init__()
        self.tablero = tablero

        self.setWindowTitle("Consulta de tablero")
        self.setGeometry(200, 200, 400, 140)

        central = QWidget(self)
        self.setCentralWidget(central)

        self.caja = QLineEdit(central)
        self.caja.setPlaceholderText("tt-101")
        self.caja.setGeometry(20, 20, 240, 28)

        self.boton = QPushButton("Consultar", central)
        self.boton.setGeometry(270, 20, 110, 28)

        self.resultado = QLabel("Escribe un tag", central)
        self.resultado.setGeometry(20, 70, 360, 28)

        self.boton.clicked.connect(self.al_consultar)

    def al_consultar(self) -> None:
        try:
            self.resultado.setText(self.tablero.leer(self.caja.text()))
        except TagDesconocido as ex:
            self.resultado.setText(str(ex))


if __name__ == "__main__":
    tablero = Tablero()
    tablero.registrar("TT-101", 74.5, "C")
    tablero.registrar("PT-205", 6.1, "bar")
    tablero.registrar("FT-330", 118.0, "L/s")

    app = QApplication(sys.argv)
    ventana = VentanaTablero(tablero)
    ventana.show()
    sys.exit(app.exec())
```
**Salida**
```text
TT-101: 74.5 C
PT-205: 6.1 bar
Rechazado: XX-999 no está en el tablero
```
Esa es la salida de correr `tablero.py` desde la terminal. En la ventana, consultar `xx-999` deja en la etiqueta el texto `XX-999 no está en el tablero`.

**Rúbrica** (suma 10)
| Criterio | Puntos |
|---|---|
| tablero.py no importa PyQt6 y corre desde la terminal | 4 |
| La ventana recibe el tablero armado y lo guarda | 2 |
| El slot atrapa la excepción propia y la muestra en la etiqueta | 3 |
| La normalización de la etiqueta vive en el dominio, no en el slot | 1 |

**Error que más se ve**
Ponen el `strip().upper()` en el slot: la ventana queda con una regla de negocio adentro, y la misma clase deja de servir para el script de consola.

## Semana 15 · Tema 6 · Interfaces gráficas

Igual que la semana anterior: el código de ventana está revisado contra la API de PyQt6 y no se ejecutó aquí. La clase de dominio de 15.3 sí corre, y su salida es real.

### 15.1 · Reconocer
**Solución**
```text
Los cuatro números de addWidget son fila, columna, cuántas filas abarca y
cuántas columnas abarca. Los dos primeros empiezan en cero, igual que los
índices de una lista. Cuando se omiten los dos últimos, el control ocupa
una sola celda.

           columna 0     columna 1        columna 2
fila 0     B-101         boton_paro       (vacía)
fila 1     C-310         boton_paro       (vacía)
fila 2     M-204         boton_arranque   boton_arranque

boton_paro es el más alto: abarca dos filas y una columna.
boton_arranque es el más ancho: abarca una fila y dos columnas.

Una etiqueta más en la posición 0, 1 caería encima del botón de paro. La
rejilla no avisa: los dos quedan en la misma celda y el problema se ve al
correr la ventana, no al escribirla.
```
**Salida**
```text
Este ejercicio no imprime. Se califica el dibujo de la cuadrícula y las
tres respuestas.
```
**Rúbrica** (suma 10)
| Criterio | Puntos |
|---|---|
| La cuadrícula ubica los cinco controles en las celdas correctas | 4 |
| Explica los cuatro números de addWidget | 3 |
| Identifica cuál botón es más alto y cuál más ancho | 2 |
| Dice que dos controles en la misma celda se encinan sin error | 1 |

**Error que más se ve**
Leen los dos primeros números como columna y fila: el botón les queda acostado, y el dibujo sale transpuesto.

### 15.2 · Aplicar
**Solución**
```python
import sys

from PyQt6.QtWidgets import (QApplication, QFormLayout, QHBoxLayout, QLabel,
                             QLineEdit, QListWidget, QMainWindow, QPushButton,
                             QVBoxLayout, QWidget)


class VentanaOrden(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Alta de órdenes de trabajo")
        self.setGeometry(200, 200, 460, 320)

        central = QWidget(self)
        columna = QVBoxLayout(central)

        formulario = QFormLayout()
        self.folio = QLineEdit()
        self.tag = QLineEdit()
        self.prioridad = QLineEdit()
        self.descripcion = QLineEdit()

        formulario.addRow("Folio", self.folio)
        formulario.addRow("Equipo", self.tag)
        formulario.addRow("Prioridad", self.prioridad)
        formulario.addRow("Descripción", self.descripcion)
        columna.addLayout(formulario)

        botones = QHBoxLayout()
        self.boton_guardar = QPushButton("Guardar")
        self.boton_limpiar = QPushButton("Limpiar")
        botones.addWidget(self.boton_guardar)
        botones.addWidget(self.boton_limpiar)
        columna.addLayout(botones)

        self.aviso = QLabel("Captura una orden")
        columna.addWidget(self.aviso)

        self.lista = QListWidget()
        columna.addWidget(self.lista)

        self.setCentralWidget(central)

        self.boton_guardar.clicked.connect(self.al_guardar)
        self.boton_limpiar.clicked.connect(self.al_limpiar)

    def al_guardar(self) -> None:
        renglon = f"{self.folio.text()} {self.tag.text()} P{self.prioridad.text()}"
        self.lista.addItem(renglon)
        self.aviso.setText(f"Órdenes capturadas: {self.lista.count()}")
        self.al_limpiar()

    def al_limpiar(self) -> None:
        self.folio.clear()
        self.tag.clear()
        self.prioridad.clear()
        self.descripcion.clear()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaOrden()
    ventana.show()
    sys.exit(app.exec())
```
**Salida**
```text
La ventana abre con los cuatro campos vacíos y el aviso en "Captura una
orden". Al capturar OT-1042, B-101 y 1 y oprimir Guardar, la lista muestra
"OT-1042 B-101 P1", el aviso pasa a "Órdenes capturadas: 1" y los campos
quedan vacíos. Al estirar la ventana, el formulario y la lista crecen con
ella y nada se encima.
```
**Rúbrica** (suma 10)
| Criterio | Puntos |
|---|---|
| Ninguna coordenada fija en toda la ventana | 3 |
| El formulario y la fila de botones van anidados dentro del layout vertical | 3 |
| Cada botón conectado a su propio slot, sin paréntesis | 2 |
| Guardar limpia los campos reusando el otro slot | 2 |

**Error que más se ve**
Meten el `QFormLayout` con `addWidget` en lugar de `addLayout`: un layout no es un widget, y la ventana abre sin el formulario.

### 15.3 · Integrar
**Solución**
```python
class DatoInvalido(Exception):
    pass


class OrdenDeTrabajo:
    def __init__(self, folio: str, tag: str, prioridad: int, descripcion: str) -> None:
        self.folio = folio
        self.tag = tag
        self.prioridad = prioridad
        self.descripcion = descripcion

    def __str__(self) -> str:
        return f"{self.folio} {self.tag} P{self.prioridad}: {self.descripcion}"


class Registro:
    def __init__(self) -> None:
        self.__ordenes = []

    def alta(self, folio: str, tag: str, prioridad: str, descripcion: str) -> OrdenDeTrabajo:
        if len(folio.strip()) < 6:
            raise DatoInvalido("El folio lleva al menos seis caracteres")
        if len(tag.strip()) < 3:
            raise DatoInvalido("El tag lleva al menos tres caracteres")
        try:
            nivel = int(prioridad)
        except ValueError:
            raise DatoInvalido("La prioridad es un número del 1 al 3")
        if nivel < 1 or nivel > 3:
            raise DatoInvalido("La prioridad va del 1 al 3")
        if len(descripcion.strip()) == 0:
            raise DatoInvalido("La descripción no puede ir vacía")
        orden = OrdenDeTrabajo(folio.strip(), tag.strip().upper(), nivel, descripcion.strip())
        self.__ordenes.append(orden)
        return orden

    def listado(self) -> list:
        return list(self.__ordenes)

    def __len__(self) -> int:
        return len(self.__ordenes)


if __name__ == "__main__":
    registro = Registro()

    print(registro.alta("OT-1042", "b-101", "1", "Cambio de sello mecánico"))
    print(registro.alta("OT-1043", "C-310", "3", "Limpieza de filtro"))

    for datos in [("OT-1", "B-101", "1", "x"), ("OT-1044", "V-12", "9", "Ajuste"),
                  ("OT-1045", "V-12", "dos", "Ajuste")]:
        try:
            registro.alta(datos[0], datos[1], datos[2], datos[3])
        except DatoInvalido as ex:
            print("Rechazado:", ex)

    print(len(registro))
```
La ventana es la misma de 15.2, con un solo cambio en el slot de guardar:
```python
    def al_guardar(self) -> None:
        try:
            orden = self.registro.alta(
                self.folio.text(),
                self.tag.text(),
                self.prioridad.text(),
                self.descripcion.text())
        except DatoInvalido as ex:
            self.aviso.setText(str(ex))
            return
        self.lista.addItem(str(orden))
        self.aviso.setText(f"Órdenes capturadas: {len(self.registro)}")
        self.al_limpiar()
```
**Salida**
```text
OT-1042 B-101 P1: Cambio de sello mecánico
OT-1043 C-310 P3: Limpieza de filtro
Rechazado: El folio lleva al menos seis caracteres
Rechazado: La prioridad va del 1 al 3
Rechazado: La prioridad es un número del 1 al 3
2
```
Esa es la salida de correr `registro.py` desde la terminal. En la ventana, capturar la prioridad 9 deja el aviso en `La prioridad va del 1 al 3` y no agrega nada a la lista.

**Rúbrica** (suma 10)
| Criterio | Puntos |
|---|---|
| registro.py no importa PyQt6 y corre desde la terminal | 3 |
| Las cuatro validaciones en orden, cada una con su mensaje | 3 |
| El slot solo traduce: lee, llama, atrapa y muestra | 2 |
| Cuando el alta se rechaza, la lista no crece | 2 |

**Error que más se ve**
Validan la longitud del folio dentro del slot para no llamar en balde: la regla queda repartida entre la ventana y el registro, y las dos versiones se contradicen en cuanto una cambia.

## Semana 16 · Tema 7 · Bases de datos y proyecto

### 16.1 · Reconocer
**Solución**
```text
El primer bloque crea la tabla y la confirma, así que la estructura queda en
disco. El segundo inserta el balero y cierra la conexión sin confirmar: la
transacción se descarta y el renglón nunca llega al archivo, sin un solo
mensaje de error. Por eso el primer COUNT devuelve 0.

El tercer bloque inserta el sello y sí llama a commit antes de cerrar, así
que el segundo COUNT devuelve 1.

fetchone devuelve la fila completa, y una fila siempre llega como tupla,
aunque traiga una sola columna. De ahí la coma dentro del paréntesis.
```
**Salida**
```text
(0,)
(1,)
```
**Rúbrica** (suma 10)
| Criterio | Puntos |
|---|---|
| Las dos salidas, con la forma de tupla | 4 |
| Explica que cerrar sin confirmar descarta lo insertado | 3 |
| Dice que no hay error ni aviso cuando eso pasa | 2 |
| Explica por qué fetchone devuelve una tupla | 1 |

**Error que más se ve**
Contestan `(1,)` y `(2,)` porque suponen que cada INSERT se guarda solo: el motor lo tiene pendiente hasta que alguien confirma.

### 16.2 · Aplicar
**Solución**
```python
import sqlite3
from pathlib import Path

# Antes de volver a correr esto hay que borrar almacen.db: las claves son
# llave primaria, así que un segundo INSERT de BL-220 falla por duplicado.
ruta = Path("almacen.db")

refacciones = [
    ("BL-220", "balero", 12),
    ("SM-4471", "sello mecánico", 6),
    ("EM-905", "empaque", 30),
    ("RT-118", "retén", 2),
]

with sqlite3.connect(ruta) as conexion:
    conexion.execute(
        "CREATE TABLE IF NOT EXISTS Refacciones ("
        "clave TEXT PRIMARY KEY, descripcion TEXT NOT NULL, piezas INTEGER NOT NULL)")
    for clave, descripcion, piezas in refacciones:
        conexion.execute(
            "INSERT INTO Refacciones VALUES (?, ?, ?)", (clave, descripcion, piezas))
    conexion.commit()

with sqlite3.connect(ruta) as conexion:
    cursor = conexion.execute(
        "SELECT clave, piezas FROM Refacciones WHERE piezas < ? ORDER BY piezas", (10,))
    for fila in cursor:
        print(fila)

    cursor = conexion.execute(
        "SELECT descripcion FROM Refacciones WHERE clave = ?", ("EM-905",))
    print(cursor.fetchone())

    cursor = conexion.execute("SELECT COUNT(*) FROM Refacciones")
    print(cursor.fetchone())
```
**Salida**
```text
('RT-118', 2)
('SM-4471', 6)
('empaque',)
(4,)
```
**Rúbrica** (suma 10)
| Criterio | Puntos |
|---|---|
| La tabla con llave primaria y las dos columnas obligatorias | 2 |
| Los valores viajan como parámetros, nunca pegados en la cadena | 4 |
| commit explícito después de las inserciones | 2 |
| El ORDER BY va en la consulta y no en Python | 2 |

**Error que más se ve**
Arman la consulta con una f-string "porque es solo un número": es el mismo hueco que con un texto, y basta una comilla en el dato para que la consulta cambie de forma.

### 16.3 · Integrar
**Solución**
```python
import sqlite3
from pathlib import Path


class RefaccionNoEncontrada(Exception):
    pass


class Refaccion:
    def __init__(self, clave: str, descripcion: str, piezas: int) -> None:
        self.clave = clave
        self.descripcion = descripcion
        self.piezas = piezas

    def surtir(self, cuantas: int) -> None:
        if cuantas > self.piezas:
            raise ValueError(f"{self.clave} solo tiene {self.piezas} piezas")
        self.piezas -= cuantas

    def __str__(self) -> str:
        return f"{self.clave} ({self.descripcion}): {self.piezas}"


class AlmacenSQLite:
    def __init__(self, ruta: Path) -> None:
        self.ruta = ruta
        with sqlite3.connect(self.ruta) as conexion:
            conexion.execute(
                "CREATE TABLE IF NOT EXISTS Refacciones ("
                "clave TEXT PRIMARY KEY, descripcion TEXT NOT NULL, piezas INTEGER NOT NULL)")
            conexion.commit()

    def guardar(self, refaccion: Refaccion) -> None:
        with sqlite3.connect(self.ruta) as conexion:
            conexion.execute(
                "INSERT INTO Refacciones VALUES (?, ?, ?)",
                (refaccion.clave, refaccion.descripcion, refaccion.piezas))
            conexion.commit()

    def cargar(self, clave: str) -> Refaccion:
        with sqlite3.connect(self.ruta) as conexion:
            cursor = conexion.execute(
                "SELECT clave, descripcion, piezas FROM Refacciones WHERE clave = ?",
                (clave,))
            fila = cursor.fetchone()
        if fila is None:
            raise RefaccionNoEncontrada(f"{clave} no está en el almacén")
        return Refaccion(fila[0], fila[1], fila[2])

    def bajo_minimo(self, minimo: int) -> list:
        with sqlite3.connect(self.ruta) as conexion:
            cursor = conexion.execute(
                "SELECT clave, descripcion, piezas FROM Refacciones "
                "WHERE piezas < ? ORDER BY piezas", (minimo,))
            filas = cursor.fetchall()
        return [Refaccion(f[0], f[1], f[2]) for f in filas]


almacen = AlmacenSQLite(Path("planta.db"))

almacen.guardar(Refaccion("BL-220", "balero", 12))
almacen.guardar(Refaccion("SM-4471", "sello mecánico", 6))
almacen.guardar(Refaccion("RT-118", "retén", 2))

balero = almacen.cargar("BL-220")
balero.surtir(9)
print(balero)
print(almacen.cargar("BL-220"))

for refaccion in almacen.bajo_minimo(10):
    print(refaccion)

try:
    almacen.cargar("XX-999")
except RefaccionNoEncontrada as ex:
    print("Rechazado:", ex)

try:
    balero.surtir(100)
except ValueError as ex:
    print("Rechazado:", ex)
```
**Salida**
```text
BL-220 (balero): 3
BL-220 (balero): 12
RT-118 (retén): 2
SM-4471 (sello mecánico): 6
Rechazado: XX-999 no está en el almacén
Rechazado: BL-220 solo tiene 3 piezas
```
Los dos números son distintos porque `cargar` construye un objeto nuevo con lo que había en la tabla en ese momento. Surtir nueve piezas modificó el objeto que vive en memoria y nadie le avisó a la base. Para que dejaran de ser distintos habría que agregarle a `AlmacenSQLite` un método `actualizar(refaccion)` con un `UPDATE`, y llamarlo después de surtir.

**Rúbrica** (suma 10)
| Criterio | Puntos |
|---|---|
| Refaccion no importa sqlite3 y todo el SQL vive en la otra clase | 4 |
| cargar devuelve un objeto, no una tupla, y levanta la excepción propia | 2 |
| El párrafo explica que el objeto en memoria y la fila en disco son dos cosas | 3 |
| bajo_minimo consulta con parámetro y ORDER BY | 1 |

**Error que más se ve**
Le meten un `import sqlite3` y un `guardar()` a la clase `Refaccion`: la clase deja de poder probarse sin base de datos, y el SQL termina repartido en dos lugares.

## Semana 17 · Evaluación final

### 17.1 · Reconocer
**Solución**
```text
Regla 1. ficha está escrito en Activo, pero self conserva la clase real del
objeto, que es Bomba. Python busca clase empezando por ahí: corre la versión
de Bomba, que a su vez llama con super a la de Rotativo. De ahí sale
"bomba rotativo".

Regla 2. El censo se incrementa sobre la clase, con Activo.censo += 1, así
que sí queda en la clase. Se construyó un solo objeto, y vale 1.

Regla 3. El atributo con dos guiones bajos se renombró a _Activo__tag dentro
del intérprete. El primer hasattr lo encuentra con ese nombre y el segundo
no lo encuentra con el original.

Regla 4. La propiedad tag solo tiene getter. Asignarle algo levanta
AttributeError, porque no hay setter que reciba el valor.
```
**Salida**
```text
B-101/bomba rotativo
1
True False
la propiedad no tiene setter
```
**Rúbrica** (suma 10)
| Criterio | Puntos |
|---|---|
| Las cuatro salidas | 4 |
| Explica la búsqueda de métodos desde la clase real del objeto | 2 |
| Explica el renombrado del atributo privado | 2 |
| Explica por qué el censo vale 1 y por qué la propiedad rechaza la asignación | 2 |

**Error que más se ve**
Contestan "B-101/activo" porque `ficha` está escrito en `Activo`: es el mismo error de la semana 8, y en el examen final vale el doble.

### 17.2 · Aplicar
**Solución**
```python
import csv
from abc import ABC, abstractmethod
from pathlib import Path


class DatoInvalido(Exception):
    pass


class Equipo(ABC):
    def __init__(self, tag: str, horas: float) -> None:
        if len(tag.strip()) < 3:
            raise DatoInvalido(f"Tag inválido: {tag}")
        if horas < 0:
            raise DatoInvalido(f"{tag} no puede tener {horas} horas")
        self._tag = tag.strip().upper()
        self.__horas = horas

    @property
    def tag(self) -> str:
        return self._tag

    @property
    def horas(self) -> float:
        return self.__horas

    @abstractmethod
    def consumo_kw(self) -> float:
        ...

    @abstractmethod
    def tipo(self) -> str:
        ...

    def fila(self) -> dict:
        return {
            "tag": self.tag,
            "tipo": self.tipo(),
            "horas": f"{self.horas:.0f}",
            "kw": f"{self.consumo_kw():.1f}",
        }


class Bomba(Equipo):
    def __init__(self, tag: str, horas: float, caudal: float) -> None:
        super().__init__(tag, horas)
        self.caudal = caudal

    def consumo_kw(self) -> float:
        return self.caudal * 0.32

    def tipo(self) -> str:
        return "bomba"


class Compresor(Equipo):
    def __init__(self, tag: str, horas: float, presion: float) -> None:
        super().__init__(tag, horas)
        self.presion = presion

    def consumo_kw(self) -> float:
        return self.presion * 8.0

    def tipo(self) -> str:
        return "compresor"


def exportar(equipos: list, ruta: Path) -> None:
    campos = ["tag", "tipo", "horas", "kw"]
    with open(ruta, "w", newline="", encoding="utf-8") as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=campos)
        escritor.writeheader()
        for equipo in equipos:
            escritor.writerow(equipo.fila())


planta = [
    Bomba("b-101", 4820.0, 120.0),
    Bomba("B-102", 1150.0, 95.0),
    Compresor("c-310", 6300.0, 8.5),
]

for datos in [("XX", 100.0, 50.0), ("B-103", -20.0, 80.0)]:
    try:
        planta.append(Bomba(datos[0], datos[1], datos[2]))
    except DatoInvalido as ex:
        print("Rechazado:", ex)

ruta = Path("equipos.csv")
exportar(planta, ruta)

print(ruta.read_text(encoding="utf-8"))
print(len(planta))
```
**Salida**
```text
Rechazado: Tag inválido: XX
Rechazado: B-103 no puede tener -20.0 horas
tag,tipo,horas,kw
B-101,bomba,4820,38.4
B-102,bomba,1150,30.4
C-310,compresor,6300,68.0

3
```
**Rúbrica** (suma 10)
| Criterio | Puntos |
|---|---|
| La validación vive en el constructor de la abstracta y levanta DatoInvalido | 3 |
| Los dos métodos abstractos implementados en las dos hijas | 2 |
| Las etiquetas quedan limpias y en mayúsculas en el CSV | 2 |
| Exportación con DictWriter, encabezado, with y encoding | 3 |

**Error que más se ve**
Repiten la validación en cada hija en lugar de encadenar con `super`: el día que cambie la regla del tag hay que tocar tres constructores, y uno se queda atrás.

### 17.3 · Integrar
**Solución**
```python
import csv
import sqlite3
from abc import ABC, abstractmethod
from pathlib import Path


class LecturaInvalida(Exception):
    pass


class Instrumento(ABC):
    def __init__(self, tag: str, minimo: float, maximo: float) -> None:
        self._tag = tag
        self._minimo = minimo
        self._maximo = maximo

    @property
    def tag(self) -> str:
        return self._tag

    @abstractmethod
    def unidad(self) -> str:
        ...

    def validar(self, texto: str) -> float:
        try:
            valor = float(texto)
        except ValueError:
            raise LecturaInvalida(f"{self._tag} envió {texto} y no es un número")
        if valor < self._minimo or valor > self._maximo:
            raise LecturaInvalida(
                f"{self._tag} midió {valor} {self.unidad()} fuera de "
                f"{self._minimo} a {self._maximo}")
        return valor


class Termopar(Instrumento):
    def unidad(self) -> str:
        return "C"


class Manometro(Instrumento):
    def unidad(self) -> str:
        return "bar"


class Caudalimetro(Instrumento):
    def unidad(self) -> str:
        return "L/s"


class Historico:
    def __init__(self, ruta: Path) -> None:
        self.ruta = ruta
        with sqlite3.connect(self.ruta) as conexion:
            conexion.execute(
                "CREATE TABLE IF NOT EXISTS Lecturas ("
                "id INTEGER PRIMARY KEY, tag TEXT NOT NULL, valor REAL NOT NULL)")
            conexion.commit()

    def guardar(self, tag: str, valor: float) -> None:
        with sqlite3.connect(self.ruta) as conexion:
            conexion.execute(
                "INSERT INTO Lecturas (tag, valor) VALUES (?, ?)", (tag, valor))
            conexion.commit()

    def valores(self, tag: str) -> list:
        with sqlite3.connect(self.ruta) as conexion:
            cursor = conexion.execute(
                "SELECT valor FROM Lecturas WHERE tag = ? ORDER BY id", (tag,))
            return [fila[0] for fila in cursor.fetchall()]


def cargar_crudas(ruta: Path) -> list:
    try:
        with open(ruta, newline="", encoding="utf-8") as archivo:
            return list(csv.DictReader(archivo))
    except FileNotFoundError:
        return []


def escribir_reporte(ruta: Path, resumen: dict, descartadas: list) -> None:
    with open(ruta, "w", encoding="utf-8") as archivo:
        archivo.write("Reporte de telemetría\n")
        for tag, promedio in resumen.items():
            archivo.write(f"{tag}: {promedio:.2f}\n")
        archivo.write(f"Descartadas: {len(descartadas)}\n")
        for motivo in descartadas:
            archivo.write(f"  {motivo}\n")


tablero = {
    "TT-101": Termopar("TT-101", 0.0, 400.0),
    "PT-205": Manometro("PT-205", 0.0, 10.0),
    "FT-330": Caudalimetro("FT-330", 0.0, 200.0),
}

crudas = [
    {"tag": "TT-101", "valor": "74.5"},
    {"tag": "PT-205", "valor": "6.1"},
    {"tag": "TT-101", "valor": "81.2"},
    {"tag": "FT-330", "valor": "118.0"},
    {"tag": "PT-205", "valor": "s/d"},
    {"tag": "TT-101", "valor": "412.0"},
    {"tag": "XX-999", "valor": "3.0"},
]

origen = Path("crudas.csv")
with open(origen, "w", newline="", encoding="utf-8") as archivo:
    escritor = csv.DictWriter(archivo, fieldnames=["tag", "valor"])
    escritor.writeheader()
    escritor.writerows(crudas)

# La base se rehace en cada corrida, o las lecturas se acumularían.
ruta_base = Path("historico.db")
ruta_base.unlink(missing_ok=True)

historico = Historico(ruta_base)
descartadas = []

for fila in cargar_crudas(origen):
    tag = fila["tag"]
    instrumento = tablero.get(tag)
    if instrumento is None:
        descartadas.append(f"{tag} no está en el tablero")
        continue
    try:
        historico.guardar(tag, instrumento.validar(fila["valor"]))
    except LecturaInvalida as ex:
        descartadas.append(str(ex))

resumen = {}
for tag, instrumento in tablero.items():
    valores = historico.valores(tag)
    if len(valores) == 0:
        continue
    suma = 0.0
    for valor in valores:
        suma += valor
    resumen[tag] = suma / len(valores)

destino = Path("reporte.txt")
escribir_reporte(destino, resumen, descartadas)

print(destino.read_text(encoding="utf-8"))
print(historico.valores("TT-101"))
```
**Salida**
```text
Reporte de telemetría
TT-101: 77.85
PT-205: 6.10
FT-330: 118.00
Descartadas: 3
  PT-205 envió s/d y no es un número
  TT-101 midió 412.0 C fuera de 0.0 a 400.0
  XX-999 no está en el tablero

[74.5, 81.2]
```
**Rúbrica** (suma 10)
| Criterio | Puntos |
|---|---|
| Instrumento abstracto, con validar concreto que usa el método abstracto | 2 |
| El CSV se lee con DictReader y el archivo faltante no truena | 2 |
| Todo el SQL vive en Historico y usa marcadores | 2 |
| La etiqueta desconocida se comprueba con if y el resto se valida con try | 2 |
| El reporte sale con los promedios calculados desde la base | 2 |

**Error que más se ve**
Calculan el promedio sobre la lista cruda en memoria: el 412.0 rechazado se cuela en la cuenta de TT-101, que sube de 77.85 a 189.23 sin que el reporte lo note.
