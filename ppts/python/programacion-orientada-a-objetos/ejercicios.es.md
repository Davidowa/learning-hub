# Ejercicios · Programación Orientada a Objetos · COM102

Este cuadernillo acompaña las diecisiete sesiones del curso. Cada semana trae tres ejercicios: **Reconocer** se contesta leyendo código y prediciendo lo que imprime, **Aplicar** pide escribir contra una especificación con datos dados, e **Integrar** amarra el tema de la semana con lo de semanas anteriores. La dificultad sube dentro de la semana y a lo largo del semestre, así que el Reconocer de la semana 12 pesa más que el Integrar de la semana 4. Todos los problemas ocurren en la misma planta de bombeo: equipos con etiqueta ISA (B-101, C-310, M-204, V-12), instrumentos (TT-101, PT-205, FT-330), órdenes de trabajo, refacciones y bitácoras. Se entrega un archivo `.py` por ejercicio, por Blackboard, con el nombre `apellido_NN_M.py`.

## Semana 01 · Encuadre del curso

### 01.1 · Reconocer
Traza de tipos y ciclo.

El siguiente programa corre sin errores. Escribe, línea por línea, lo que imprime, y explica en un renglón por qué la tercera salida no es 4.

```python
tag = "B-101-BOMBA"
horas = "4820"

print(tag[0], tag[-1])
print(tag[0:5])
print(len(horas * 2))
print(horas + "0")

total = 0
for i in range(1, 4):
    total += i * 10
print(total)
```

### 01.2 · Aplicar
Clasificar una presión.

El manómetro PT-205 reporta presiones en bar. Escribe la función `clasificar_presion(bar)` que **devuelva** (no imprima) una de tres cadenas: `"baja"` si la presión es menor a 2.0, `"normal"` si está entre 2.0 y 8.0 con los dos extremos incluidos, y `"alta"` si pasa de 8.0.

Después recorre la lista `[1.4, 2.0, 6.7, 8.0, 9.3]` e imprime un renglón por lectura con este formato exacto, con un decimal:

```text
1.4 bar -> baja
```

Las fronteras importan: 2.0 y 8.0 son "normal", no "baja" ni "alta".

### 01.3 · Integrar
Lecturas que no siempre son números.

El registrador entrega las lecturas del turno como una lista de tuplas, y a veces el valor llega como texto porque el instrumento no respondió:

```python
lecturas = [
    ("TT-101", "74.5"),
    ("PT-205", "6.1"),
    ("TT-101", "s/d"),
    ("FT-330", "118.0"),
    ("PT-205", "6.4"),
    ("FT-330", "sin dato"),
]
```

Escribe tres funciones, cada una con retorno y sin `print` adentro:

1. `separar(registros)` devuelve dos cosas: la lista de tuplas donde el valor sí se pudo convertir a `float`, y cuántas se descartaron. La conversión va dentro de un `try` con el tipo de excepción nombrado.
2. `promedio(valores)` devuelve el promedio de una lista de números.
3. `etiquetas(registros)` devuelve las etiquetas sin repetir y en orden alfabético.

El programa principal imprime cuántas lecturas fueron válidas, cuántas se descartaron, el promedio con dos decimales y la lista de etiquetas.

## Semana 02 · Tema 1 · Introducción a la POO

### 02.1 · Reconocer
Listas paralelas que se desalinean.

El programa de abajo lleva el inventario de equipos en dos listas que se corresponden por posición. Alguien dio de baja la bomba B-102. Predice la salida y contesta: ¿a qué equipo pertenecen realmente las 1150 horas que se imprimen?

```python
tags = ["B-101", "B-102", "C-310"]
horas = [4820, 1150, 6300]

tags.remove("B-102")

for i in range(len(tags)):
    print(tags[i], horas[i])
```

Escribe además qué línea faltó y por qué Python no protestó.

### 02.2 · Aplicar
Qué pide clase y qué pide función.

Estos seis módulos aparecen en el sistema de mantenimiento de la planta. Clasifica cada uno como **clase** o **función**, con una línea de justificación que use el criterio de la sesión: si guarda algo entre una llamada y la siguiente, hay estado, y donde hay estado hay clase.

1. Convertir una lectura de presión de psi a bar.
2. Una bomba con horas de operación y estado actual.
3. Contar cuántos renglones de la bitácora dicen "falla".
4. Una orden de trabajo con folio, equipo asignado y avance.
5. Ordenar una lista de refacciones por clave.
6. Un inventario de refacciones que descuenta piezas conforme se surten.

De los que clasificaste como función, implementa el primero: `psi_a_bar(psi)` con el factor 0.0689476, e imprime el resultado para 120 psi y para 45 psi, con dos decimales y la unidad.

### 02.3 · Integrar
Del arreglo de listas al registro.

El sistema actual guarda cuatro listas paralelas:

```python
tags = ["B-101", "B-102", "C-310", "M-204"]
horas = [4820, 1150, 6300, 2210]
estados = ["operando", "detenido", "operando", "operando"]
revision = [1180, 40, 900, 310]
```

Reescríbelo con una sola lista de diccionarios, un diccionario por equipo con las llaves `tag`, `horas`, `estado` y `revision`. Escribe `a_registros(...)` que haga la conversión, `dar_de_baja(registros, tag)` que devuelva una lista nueva sin ese equipo, e `imprimir(registros)` que muestre un renglón por equipo.

Da de baja a B-102 e imprime lo que queda, más el total de equipos. Ningún dato debe quedar desalineado, y ninguna función debe modificar la lista que recibe.

## Semana 03 · Tema 2 · Elementos básicos

### 03.1 · Reconocer
La lista que comparten todas las bombas.

B-101 registró dos alarmas. B-102 no registró ninguna. Predice las tres salidas y explica en un renglón dónde vive la lista `alarmas`.

```python
class Bomba:
    alarmas = []

    def __init__(self, tag):
        self.tag = tag

    def alarmar(self, codigo):
        self.alarmas.append(codigo)


b1 = Bomba("B-101")
b2 = Bomba("B-102")

b1.alarmar("E12")
b1.alarmar("E07")

print(len(b2.alarmas))
print(b2.alarmas)
print(b1.alarmas is b2.alarmas)
```

Escribe también la corrección, que cabe en una línea.

### 03.2 · Aplicar
La bomba como clase.

Escribe la clase `Bomba` con constructor que reciba `tag`, `caudal_l_s` y `horas`. Agrega:

- el método `registrar_horas(corridas)`, que suma las horas del turno a las acumuladas;
- la propiedad `caudal_m3_h`, que devuelve el caudal en metros cúbicos por hora (multiplica los litros por segundo por 3.6);
- la propiedad `horas_para_servicio`, que devuelve cuántas horas faltan para las 5000 del servicio mayor.

Construye B-101 con 120.0 L/s y 4820 horas. Imprime el caudal en m3/h con un decimal, imprime las horas que faltan, registra 260 horas más y vuelve a imprimirlas. El segundo número sale negativo, y así debe salir: el servicio ya se pasó.

### 03.3 · Integrar
Sensores con rango propio.

Escribe la clase `Sensor` con `tag`, `unidad`, `minimo` y `maximo`, el método `en_rango(valor)` que devuelva verdadero o falso, y la propiedad `amplitud` que devuelva el rango de la escala.

Arma un diccionario con tres sensores: TT-101 en grados C de 0.0 a 400.0, PT-205 en bar de 0.0 a 10.0 y FT-330 en L/s de 0.0 a 200.0. Recorre estas lecturas y por cada una imprime la etiqueta, el valor, la unidad y si quedó dentro o `FUERA`:

```python
lecturas = [
    ("TT-101", 412.0),
    ("PT-205", 6.1),
    ("FT-330", 118.0),
    ("TT-101", 74.5),
    ("PT-205", 11.2),
]
```

Al final imprime cuántas lecturas salieron de rango y la amplitud del FT-330. La búsqueda del sensor por etiqueta se hace con el diccionario, no recorriendo una lista.

## Semana 04 · Tema 2 · Elementos básicos

### 04.1 · Reconocer
Lo privado, el contador y el renombrado.

Predice las cuatro salidas. Dos de ellas sorprenden a la mitad del grupo.

```python
class Equipo:
    registrados = 0

    def __init__(self, tag):
        self.__tag = tag
        self.registrados += 1

    def etiqueta(self):
        return self.__tag


a = Equipo("B-101")
b = Equipo("C-310")

print(Equipo.registrados)
print(a.registrados)
print(a._Equipo__tag)
print(hasattr(a, "__tag"))
```

Explica en dos renglones por qué el contador de la clase se quedó donde se quedó, y qué línea lo arregla.

### 04.2 · Aplicar
Un manómetro que rechaza lo imposible.

Escribe la clase `Manometro` con `tag` público y la presión guardada en un atributo privado. La presión se expone como propiedad con setter, y el setter levanta `ValueError` si el valor sale del rango de 0.0 a 10.0 bar, con un mensaje que incluya el valor rechazado. El constructor asigna por la propiedad, no por el atributo privado.

Agrega el constructor alternativo `desde_psi(tag, psi)` como método de clase, con el factor 0.0689476.

Prueba así: construye PT-205 en 6.1 bar e imprímelo con dos decimales; súbelo a 9.0 e imprímelo; intenta ponerlo en 12.5 dentro de un `try` e imprime el mensaje del error; vuelve a imprimir la presión para demostrar que no cambió; construye PT-301 desde 120.0 psi e imprímelo.

### 04.3 · Integrar
Un tanque que no se desborda.

Escribe la clase `Tanque` con `tag` y `capacidad` públicos, el nivel en un atributo privado, y un atributo de clase `instalados` que cuente cuántos tanques se han construido. Expón `nivel` y `porcentaje` como propiedades de solo lectura. Los métodos `llenar(litros)` y `vaciar(litros)` levantan `ValueError` cuando la operación dejaría el tanque desbordado o en negativo.

Construye TQ-01 con capacidad 5000.0 L y nivel 1200.0, y TQ-02 con capacidad 2000.0 L y nivel 800.0. Llena TQ-01 con 2000 L e imprime su estado. Después intenta vaciarle 4000 L y llenarle 3000 L, cada intento dentro de su `try`, e imprime el mensaje que llegue. Vacíale 1200 L, imprime el estado de los dos tanques y el contador de la clase.

El formato de estado es `TQ-01: 3200 L (64.0 %)` y sale de una función aparte que recibe el tanque y devuelve la cadena.

## Semana 05 · Tema 2 · Elementos básicos

### 05.1 · Reconocer
Dos métodos con el mismo nombre.

Este archivo se llama `registrador.py`. Predice qué imprime la primera llamada, qué pasa con la segunda, y escribe el tipo de error completo.

```python
class Registrador:
    def registrar(self, tag, valor):
        print("dos datos:", tag, valor)

    def registrar(self, tag, valor, unidad):
        print("tres datos:", tag, valor, unidad)


r = Registrador()
r.registrar("TT-101", 74.5, "C")
r.registrar("PT-205", 6.1)
```

Reescribe la clase con un solo método que atienda los dos casos, sin `if` sobre la cantidad de argumentos.

### 05.2 · Aplicar
Existencias que se suman y se comparan.

Escribe la clase `Existencia` con `clave` y `piezas`, y tres métodos mágicos:

- `__str__` devuelve `BL-220 x12`;
- `__eq__` compara clave y piezas, no identidad;
- `__add__` devuelve una existencia nueva con la suma de piezas, y levanta `ValueError` si las claves no coinciden.

Con `almacen = Existencia("BL-220", 12)` y `llegada = Existencia("BL-220", 8)`, imprime el almacén, la suma de los dos, la comparación contra `Existencia("BL-220", 12)`, la comparación contra la llegada, y el mensaje del error al intentar sumarle `Existencia("SM-4471", 6)` dentro de un `try`.

### 05.3 · Integrar
Un inventario que recibe lo que sea.

Escribe el módulo `inventario.py` con la clase `Existencia` de 05.2 (solo `__str__`) y la clase `Inventario`, que guarda un diccionario privado de clave a piezas.

El método `recibir(*claves, **opciones)` acepta cuantas claves lleguen. La opción `piezas` dice cuántas de cada una, y vale 1 si no se pasa. La opción `avisar` imprime `2 claves recibidas en Almacén Norte` cuando es verdadera. El método `listado()` devuelve una lista de objetos `Existencia`, y `__str__` devuelve `Almacén Norte: 3 claves, 39 piezas`.

Debajo, un bloque que solo corra cuando el archivo se ejecute y no cuando se importe: recibe BL-220 y SM-4471 con 4 piezas avisando, recibe EM-905 con 30 piezas, recibe BL-220 otra vez sin decir cuántas, imprime el listado renglón por renglón y luego el inventario.

## Semana 06 · Tema 3 · Propiedades fundamentales

### 06.1 · Reconocer
El getter que devolvió la lista de verdad.

La bitácora promete que toda entrada queda en mayúsculas. Predice las tres salidas y di si la promesa se cumplió.

```python
class Bitacora:
    def __init__(self):
        self.__entradas = []

    def registrar(self, texto):
        self.__entradas.append(texto.upper())

    def entradas(self):
        return self.__entradas


b = Bitacora()
b.registrar("falla en B-101")
b.entradas().append("todo bien")

print(len(b.entradas()))
print(b.entradas()[0])
print(b.entradas()[1])
```

El atributo tiene dos guiones bajos. Explica en un renglón por qué eso no bastó, y escribe la corrección de una línea.

### 06.2 · Aplicar
Contador de fallas con corchetes.

Escribe la clase `ContadorDeFallas` que guarde un diccionario privado de etiqueta a número de fallas. La única regla de la clase es que la etiqueta se normaliza a mayúsculas, y esa regla vive dentro de la clase y en ningún otro lado.

Expón tres cosas y nada más: `registrar(tag)`, el operador de corchetes para leer y escribir, y `len`. Pedir una etiqueta que nunca falló devuelve 0 en lugar de levantar `KeyError`.

Prueba registrando `"B-101"`, `"b-101"` y `"C-310"`, y luego imprime: la cuenta de B-101, la de b-101, la de V-12, el total de etiquetas, el resultado de asignar 5 a `contador["v-12"]`, y el total otra vez.

### 06.3 · Integrar
Estación armada por composición.

Escribe tres clases sin una sola herencia entre ellas:

- `Sensor` con `tag`, `minimo`, `maximo` y `en_rango(valor)`.
- `Bitacora` con lista privada, `registrar(texto)` que guarda en mayúsculas, `entradas()` que devuelve una copia y `__len__`.
- `Estacion`, que recibe en el constructor un diccionario de sensores y una bitácora, y les delega. Su método `medir(tag, valor)` pregunta al sensor si el valor está en rango y, si no lo está, le pide a la bitácora que registre `TT-101 fuera de rango con 412.0`. El método `historial()` devuelve lo que la bitácora entrega.

Arma la estación Planta Norte con TT-101 de 0.0 a 400.0 y PT-205 de 0.0 a 10.0. Mide 412.0 en TT-101, 6.1 en PT-205 y 11.2 en PT-205. Después intenta agregarle una entrada falsa al historial desde fuera, imprime el historial completo y su tamaño. La entrada falsa no debe aparecer.

## Semana 07 · Tema 3 · Propiedades fundamentales

### 07.1 · Reconocer
La subclase que olvidó a su padre.

El archivo se llama `equipos.py`. La primera línea imprime bien. Predice qué pasa con la segunda, con qué tipo de error y sobre qué atributo.

```python
class Equipo:
    def __init__(self, tag):
        self.tag = tag
        self.horas = 0.0


class Bomba(Equipo):
    def __init__(self, tag, caudal):
        self.caudal = caudal

    def ficha(self):
        return f"{self.tag}: {self.caudal} L/s"


b101 = Bomba("B-101", 120.0)
print(b101.caudal)
print(b101.ficha())
```

Escribe la línea que falta y en qué posición exacta del constructor va.

### 07.2 · Aplicar
Equipos con un padre común.

Escribe la clase `Equipo` con los atributos protegidos `_tag` y `_horas`, el método `resumen()` que devuelva `B-101 con 4820 h`, y `registrar_horas(corridas)`.

Cuelga dos hijas del mismo padre, cada una encadenando su constructor con `super`:

- `Bomba` agrega `caudal` y el método `arrancar()`, que devuelve `B-101 arranca a 120.0 L/s`;
- `Compresor` agrega `presion` y el método `purgar()`, que devuelve `C-310 purga a 8.5 bar`.

Los dos métodos nuevos leen `_tag` del padre. Construye B-101 con 4820.0 h y 120.0 L/s, y C-310 con 6300.0 h y 8.5 bar. Imprime el resumen y el método propio de la bomba, registra 40 horas al compresor, imprime su resumen y su método propio, y cierra con `isinstance` de la bomba contra `Equipo` y contra `Compresor`, más `issubclass` de `Compresor` contra `Equipo`.

### 07.3 · Integrar
Aplanar una jerarquía de seis niveles.

El proveedor entregó este árbol. Compila, corre, y nadie lo entiende.

```python
class Activo: ...
class EquipoRotativo(Activo): ...
class Bomba(EquipoRotativo): ...
class BombaDosificadora(Bomba): ...
class BombaConVariador(BombaDosificadora): ...
class Variador(BombaConVariador): ...
```

Aplánalo a dos niveles como máximo, aplicando la prueba de "es un" en voz alta a cada relación. Una de las seis clases no pasa la prueba de ninguna manera y tiene que salir del árbol y entrar por composición.

Entrega el código con `Activo` como padre, sus hijas directas, y la clase que quedó fuera recibida como parámetro del constructor con valor por omisión `None`. Prueba con B-101 sin esa pieza, B-102 con una pieza marca Danfoss a 45.0 Hz, y C-310 como compresor. Imprime el resumen de B-101, cómo arranca cada bomba, ajusta la pieza a 38.0 Hz, vuelve a imprimir cómo arranca B-102, el resumen de C-310, y dos `isinstance` que demuestren que la pieza compuesta no forma parte de la jerarquía. Agrega un renglón de justificación por cada relación que conservaste.

## Semana 08 · Tema 3 · Propiedades fundamentales

### 08.1 · Reconocer
Quién decide qué método corre.

`reporte` está escrito una sola vez, en la clase padre. Predice las cuatro salidas y di, para cada objeto, qué `consumo_kw` se ejecutó y por qué.

```python
class Equipo:
    def __init__(self, tag):
        self.tag = tag

    def consumo_kw(self):
        return 0.0

    def reporte(self):
        print(f"{self.tag}: {self.consumo_kw():.1f} kW")


class Motor(Equipo):
    def consumo_kw(self):
        return 45.0


class Compresor(Equipo):
    def consumo_kw(self):
        return 75.0

    def reporte(self):
        super().reporte()
        print(f"{self.tag}: revisar filtro")


for equipo in [Equipo("V-12"), Motor("M-204"), Compresor("C-310")]:
    equipo.reporte()
```

Contesta además qué cambiaría si `Compresor.reporte` llamara a `super().reporte()` al final en lugar de al principio.

### 08.2 · Aplicar
Instrumentos con contrato obligatorio.

Escribe la clase abstracta `Instrumento` que herede de `ABC`. Su constructor recibe `tag` y deja `calibrado` en falso. Trae el método concreto `calibrar()`, que pone `calibrado` en verdadero, y el método abstracto `leer()`.

Escribe tres hijas concretas: `Termopar` devuelve `TT-101: 74.5 C`, `Manometro` devuelve `PT-205: 6.1 bar` y `Caudalimetro` devuelve `FT-330: 118.0 L/s`.

Arma la lista `tablero` con un objeto de cada clase, recórrela calibrando e imprimiendo la lectura y el estado de calibración. El ciclo no puede preguntar de qué clase es cada objeto. Cierra intentando construir `Instrumento("XX-000")` dentro de un `try` e imprimiendo el mensaje del `TypeError`.

### 08.3 · Integrar
Planta completa, repaso del primer parcial.

Cierra las unidades 1, 2 y 3 en un solo archivo. Escribe la clase abstracta `Equipo(ABC)` con:

- el atributo de clase `censo`, que cuenta cuántos equipos se construyeron;
- `_tag` protegido y las horas en un atributo privado;
- las propiedades de solo lectura `tag` y `horas`;
- `registrar_horas(corridas)`, que levanta `ValueError` con horas negativas;
- el método abstracto `consumo_kw()`;
- el método concreto `reporte()`, que devuelve `B-101: 4820 h, 38.4 kW`.

`Bomba` recibe caudal y consume 0.32 kW por cada L/s. `Compresor` recibe presión, consume 8.0 kW por bar, y extiende `reporte()` agregando ` (aire)` al final con `super`. `Valvula` se declara heredando de `Equipo` y no implementa `consumo_kw`, a propósito.

Recorre una lista con B-101 (4820.0 h, 120.0 L/s) y C-310 (6300.0 h, 8.5 bar) imprimiendo cada reporte y acumulando el consumo total. Registra 180 horas a la bomba y vuelve a imprimir su reporte. Intenta registrarle 5 horas negativas y construir la válvula, cada intento en su `try`, e imprime los dos mensajes. Cierra con el censo.

## Semana 09 · Tema 4 · Funciones y estructuras avanzadas

### 09.1 · Reconocer
El historial que nadie pidió compartir.

Predice las cuatro salidas. La tercera y la cuarta son la razón del ejercicio.

```python
def registrar_falla(tag, historial=[]):
    historial.append(tag)
    return historial


print(registrar_falla("B-101"))
print(registrar_falla("C-310"))
print(registrar_falla("V-12", []))
print(registrar_falla("M-204"))
```

Explica en un renglón en qué momento exacto se creó la lista que comparten las llamadas, y escribe la firma corregida.

### 09.2 · Aplicar
Refacciones ordenadas por existencia.

El almacén entrega las refacciones como tuplas de clave, descripción y piezas:

```python
refacciones = [
    ("BL-220", "balero", 12),
    ("SM-4471", "sello mecánico", 6),
    ("EM-905", "empaque", 30),
    ("RT-118", "retén", 2),
]
```

Escribe tres funciones:

1. `por_existencia(refacciones)` devuelve una lista nueva ordenada de menos a más piezas, con `key` y una lambda, sin tocar la lista original.
2. `criticas(refacciones, minimo)` devuelve las claves con menos piezas que el mínimo. Devuelve, no imprime.
3. `imprimir(refacciones)` numera el listado ordenado con `enumerate` empezando en 1, con el formato `1. RT-118 retén: 2`.

Imprime el listado, las claves críticas con mínimo 5, y al final la clave de la primera tupla de la lista original, para demostrar que sigue intacta.

### 09.3 · Integrar
Contar piezas de una lista de materiales.

La lista de materiales de la bomba B-101 llega como diccionarios anidados. Cada nodo trae su nombre, cuántas piezas son y sus partes:

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
```

Escribe tres funciones recursivas, cada una con su caso base explícito:

1. `contar_piezas(nodo)` suma las piezas del nodo y de todo lo que cuelga de él. Para esta bomba da 15.
2. `profundidad(nodo)` devuelve cuántos niveles tiene el árbol contando el nodo recibido. Para esta bomba da 3.
3. `hojas(nodo)` devuelve la lista de nombres de las partes que ya no tienen partes, en el orden en que aparecen.

Ninguna de las tres imprime nada por dentro. La tercera acumula en una lista que no puede ser el valor por omisión del parámetro, por la razón que viste en 09.1.

## Semana 10 · Tema 4 · Funciones y estructuras avanzadas

### 10.1 · Reconocer
Alias, conjunto y acumulador.

Predice las cuatro salidas. Cuenta con cuidado la primera: hay una línea que modifica la lista por el otro nombre.

```python
lecturas = [74.5, 74.5, 118.0, 6.1, 118.0]
respaldo = lecturas

respaldo.append(6.1)
unicas = set(lecturas)

conteo = {}
for valor in lecturas:
    conteo[valor] = conteo.get(valor, 0) + 1

print(len(lecturas), len(unicas))
print(conteo[118.0], conteo[6.1])
print(respaldo is lecturas)
print(conteo.get(9.9, 0))
```

Explica en un renglón qué habría cambiado si la segunda línea fuera `respaldo = list(lecturas)`.

### 10.2 · Aplicar
Filtrar fallas y agruparlas.

Con estos datos del turno:

```python
fallas = [
    ("B-101", "vibración"),
    ("C-310", "sobrecalentamiento"),
    ("B-101", "fuga"),
    ("V-12", "fuga"),
    ("B-101", "vibración"),
]

lecturas = [74.5, 118.0, 6.1, 203.0, 99.9, 118.0]
```

Resuelve cuatro consultas, cada una con el mecanismo que se indica:

1. Las etiquetas de los equipos con falla de tipo fuga, con una comprensión de lista.
2. Cuántas fallas tuvo cada equipo, con un diccionario acumulador y `get`.
3. Las lecturas mayores a 100, con una comprensión de lista.
4. Las etiquetas del punto 1 sin repetir y ordenadas.

Imprime los cuatro resultados, uno por renglón.

### 10.3 · Integrar
Un padrón con el contenedor correcto.

El padrón de la planta llega como una lista de diccionarios con `tag`, `tipo` y `horas`, con cinco equipos: B-101 bomba 4820.0, B-102 bomba 1150.0, C-310 compresor 6300.0, M-204 motor 2210.0 y V-12 válvula 300.0.

Escribe la clase `Padron`, que reciba esa lista en el constructor y guarde por dentro, en atributos privados, las estructuras que hagan falta. Expón cinco métodos, y cada uno tiene que usar el contenedor que contesta sin recorrer de más:

- `existe(tag)` contesta si la etiqueta está registrada;
- `horas(tag)` devuelve las horas de un equipo, o 0.0 si no existe;
- `ordenados()` devuelve las etiquetas en orden alfabético;
- `por_tipo()` devuelve un diccionario de tipo a cantidad;
- `vencidos(limite)` devuelve las etiquetas con más horas que el límite.

Imprime: si existe C-310 y si existe X-999 en el mismo renglón, las horas de B-101, la lista ordenada, el conteo por tipo y los vencidos con límite 5000. En la justificación escrita di, en un renglón por método, qué contenedor elegiste y por qué.

## Semana 11 · Tema 4 · Funciones y estructuras avanzadas

### 11.1 · Reconocer
El orden en que corre finally.

Predice la salida completa, en orden, con las seis líneas que aparecen.

```python
def leer(valor):
    try:
        return 100 / float(valor)
    except ValueError:
        return -1.0
    except ZeroDivisionError:
        return 0.0
    finally:
        print("intento", valor)


print(leer("4"))
print(leer("0"))
print(leer("s/d"))
```

Contesta también qué excepción levanta `float("s/d")` y por qué el segundo `except` nunca se revisa en esa llamada.

### 11.2 · Aplicar
Una excepción con nombre del problema.

Define `LecturaFueraDeRango` heredando de `Exception`. Escribe la clase `Sensor` con `tag`, `minimo` y `maximo` públicos, y el valor guardado en un atributo privado que arranca en el mínimo.

Expón el valor como propiedad con setter. El setter levanta `LecturaFueraDeRango` cuando la lectura sale del rango, con un mensaje que diga la etiqueta, el valor medido y el rango completo.

Construye TT-101 de 0.0 a 400.0 y recorre las lecturas 74.5, 412.0 y 180.0. Cada asignación va en su `try`. Cuando el valor se rechaza, imprime el nombre de la clase de la excepción y su mensaje. Cuando pasa, imprime la confirmación desde la cláusula `else`. Cierra imprimiendo el último valor que sí quedó guardado.

### 11.3 · Integrar
Ingesta de telemetría sucia.

El sistema de adquisición entrega esto, y ninguna de las siete tuplas se puede dar por buena:

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
```

Define tres excepciones propias: `LecturaInvalida` hereda de `Exception`, y `LecturaFueraDeRango` y `SensorDesconocido` heredan de la primera.

Escribe `validar(tag, texto)`, que valida en la frontera y devuelve un `float`. Rechaza la etiqueta que no esté en el diccionario `RANGOS` con TT-101 de 0.0 a 400.0, PT-205 de 0.0 a 10.0 y FT-330 de 0.0 a 200.0. Rechaza el dato ausente. Rechaza el texto que no convierte. Rechaza el valor fuera de rango. Cada rechazo lleva su tipo y un mensaje que diga qué corregir.

El programa principal recorre las tuplas con un `try` por vuelta y tres `except` en el orden que corresponde, del más específico al más general. Por cada rechazo imprime una etiqueta distinta según el tipo. Al final imprime cuántas se aceptaron, cuántas se rechazaron y el promedio de lo aceptado con dos decimales.

## Semana 12 · Tema 5 · Archivos

### 12.1 · Reconocer
El modo que borra al abrir.

El archivo `bitacora.txt` no existe cuando arranca el programa. Predice exactamente qué imprime, incluida la segunda línea.

```python
from pathlib import Path

ruta = Path("bitacora.txt")

with open(ruta, "w", encoding="utf-8") as f:
    f.write("08:00 B-101 arranca\n")

with open(ruta, "a", encoding="utf-8") as f:
    f.write("09:15 PT-205 en 6.1 bar\n")

with open(ruta, "w", encoding="utf-8") as f:
    f.write("11:40 C-310 alarma\n")

print(ruta.read_text(encoding="utf-8"))
print(len(ruta.read_text(encoding="utf-8")))
```

Di en qué instante desapareció el renglón de las 08:00, y cuál de las tres aperturas conservó lo que había.

### 12.2 · Aplicar
Telemetría que va y vuelve del CSV.

Escribe un programa que guarde estas cinco lecturas en `telemetria.csv` y después las vuelva a leer para promediarlas por instrumento:

```python
filas = [
    {"tag": "TT-101", "valor": 74.5},
    {"tag": "PT-205", "valor": 6.1},
    {"tag": "TT-101", "valor": 81.2},
    {"tag": "FT-330", "valor": 118.0},
    {"tag": "PT-205", "valor": 6.4},
]
```

La escritura usa `DictWriter` con encabezado, y la lectura usa `DictReader`, así que el programa no puede suponer el orden de las columnas. Los dos accesos van dentro de un `with`, con `newline=""` y `encoding="utf-8"` explícitos. El promedio se acumula con un diccionario de sumas y otro de conteos.

Imprime un renglón por instrumento con el formato `TT-101: 77.85 (n=2)`, en el orden en que aparecieron por primera vez.

### 12.3 · Integrar
Bitácora que sobrevive al programa.

Escribe la clase `Bitacora`, que recibe un `Path` en el constructor y guarda cada evento como un renglón de un CSV con las columnas `hora`, `tag` y `texto`.

- `registrar(hora, tag, texto)` abre en modo agregar y escribe el encabezado solo la primera vez, cuando el archivo todavía no existe.
- `entradas()` devuelve la lista de diccionarios, y devuelve una lista vacía si el archivo no está, atrapando `FileNotFoundError` por su nombre.
- `reporte(destino)` cuenta eventos por equipo y escribe un archivo de texto con el encabezado `Eventos por equipo` y un renglón por equipo.

Prueba registrando cuatro eventos: 08:00 B-101 arranque normal, 09:15 PT-205 lectura 6.1 bar, 11:40 C-310 alarma de temperatura y 13:05 B-101 paro por mantenimiento. Imprime cuántas entradas quedaron, las cuatro renglón por renglón, el contenido del reporte, y por último el tamaño de una bitácora apuntada a un archivo que no existe.

## Semana 13 · Tema 5 · Archivos

### 13.1 · Reconocer
El cursor, byte por byte.

Predice las cinco salidas. La última es la que separa a quien entendió el cursor de quien lo supuso.

```python
from pathlib import Path

ruta = Path("indice.bin")

with open(ruta, "wb") as f:
    f.write(b"B-101B-102C-310")

with open(ruta, "rb") as f:
    print(f.tell())
    f.seek(5)
    print(f.read(5))
    print(f.tell())
    f.seek(10)
    print(f.read(5))
    print(f.read(5))
```

Explica en un renglón por qué la última lectura devuelve lo que devuelve, y en qué posición quedó el cursor al terminar.

### 13.2 · Aplicar
Registros de tamaño fijo.

Escribe un programa que guarde las etiquetas `["B-101", "B-102", "C-310", "M-204"]` en `equipos.bin` como registros binarios de 32 bytes cada uno, rellenando con espacios a la derecha con el especificador de formato de las f-strings y codificando en UTF-8.

Escribe la función `leer_registro(ruta, numero)`, que abra el archivo en modo binario, salte directo al registro pedido sin leer los anteriores, lea sus 32 bytes y devuelva la etiqueta sin los espacios de relleno. La posición se calcula con el número de registro y el tamaño fijo.

Imprime cuántos bytes ocupa el archivo completo, y después los registros 2, 0 y 3 en ese orden.

### 13.3 · Integrar
Del CSV al índice binario.

Cierra las unidades 4 y 5. El programa escribe `telemetria.csv` con estas cinco filas y luego trabaja sobre el archivo, no sobre la lista:

```python
filas = [
    {"tag": "TT-101", "valor": "74.5"},
    {"tag": "PT-205", "valor": "6.1"},
    {"tag": "TT-101", "valor": "81.2"},
    {"tag": "FT-330", "valor": "118.0"},
    {"tag": "PT-205", "valor": "s/d"},
]
```

Escribe cuatro funciones:

1. `leer_lecturas(ruta)` devuelve la lista de diccionarios con `DictReader`, o una lista vacía si el archivo no existe.
2. `resumir(lecturas)` devuelve un diccionario de etiqueta a promedio. La fila que no convierte a número se descarta imprimiendo `Descartada: PT-205 envió s/d` y siguiendo con la vuelta siguiente.
3. `escribir_indice(ruta, promedios)` guarda un registro binario de 40 bytes por instrumento, con la etiqueta alineada a la izquierda en 10 posiciones y el promedio alineado a la derecha en 10 con dos decimales. Levanta la excepción propia `IndiceVacio` si no hay nada que indexar.
4. `leer_indice(ruta, numero)` salta al registro pedido y devuelve su contenido sin relleno. Levanta `IndexError` con un mensaje propio si el registro no existe.

Imprime cuántas filas se leyeron y cuántos instrumentos quedaron, los promedios con dos decimales, el registro 1 y el registro 0 del índice, y por último los mensajes de los dos errores: pedir el registro 9, y escribir un índice con un diccionario vacío. Cada intento va en su `try`.

## Semana 14 · Tema 6 · Interfaces gráficas

### 14.1 · Reconocer
El paréntesis que dispara el clic.

Esta ventana no llega a abrirse. Di qué se imprime, cuántas veces, en qué momento, y qué recibe `connect` como argumento.

```python
class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        boton = QPushButton("Consultar", self)
        boton.clicked.connect(self.al_consultar())

    def al_consultar(self):
        print("clic")
```

Escribe la corrección y explica en un renglón qué guarda `connect` cuando la corrección está bien hecha. Contesta también qué otro problema tendría esta ventana aunque el `connect` estuviera correcto, sabiendo que `boton` no se guardó sobre `self`.

### 14.2 · Aplicar
Una ventana que normaliza tags.

Escribe `VentanaTag`, que herede de `QMainWindow`, con el título `Normalizador de tags` y geometría 200, 200, 380, 140. Todos los controles cuelgan de un `QWidget` central y se colocan con coordenadas, porque los layouts llegan hasta la semana que entra.

- una `QLineEdit` con el texto de ayuda `b-101`, en 20, 20, 220, 28;
- un `QPushButton` con la leyenda `Normalizar`, en 250, 20, 110, 28;
- una `QLabel` que arranca en `Sin capturar`, en 20, 70, 340, 28.

El botón se conecta a un slot que no calcula nada: lee la caja, se lo pasa a la función suelta `normalizar(tag)` y pone el resultado en la etiqueta. La función quita espacios de orilla, pasa a mayúsculas y devuelve `Sin capturar` si no quedó nada. Los tres controles se guardan sobre `self`.

Entrega el archivo `.py` y una captura de la ventana después de escribir `  b-101 ` y oprimir el botón.

### 14.3 · Integrar
La ventana consulta, el tablero decide.

Escribe dos archivos. En `tablero.py` va la excepción `TagDesconocido` y la clase `Tablero`, con un diccionario privado de etiqueta a par de valor y unidad. Su método `registrar(tag, valor, unidad)` normaliza la etiqueta a mayúsculas, y `leer(tag)` quita espacios, normaliza, levanta `TagDesconocido` si la etiqueta no está registrada y devuelve `TT-101: 74.5 C` si sí lo está. Debajo, un bloque que solo corra al ejecutar el archivo y que pruebe la clase desde la consola con `tt-101`, con `  PT-205 ` y con `XX-999`.

En `ventana.py` va `VentanaTablero`, que recibe el tablero armado en el constructor, lo guarda, y arma caja, botón y etiqueta como en 14.2. El slot llama a `tablero.leer` dentro de un `try` y pone en la etiqueta el resultado o el mensaje de la excepción.

`tablero.py` no puede importar PyQt6. Entrega los dos archivos, la salida de consola del primero y una captura de la ventana consultando una etiqueta que no existe.

## Semana 15 · Tema 6 · Interfaces gráficas

### 15.1 · Reconocer
Dónde cae el botón en la rejilla.

La rejilla recibe cinco controles del tablero de la planta. Dibuja la cuadrícula resultante y di qué celdas ocupa cada uno.

```python
rejilla = QGridLayout(central)

rejilla.addWidget(QLabel("B-101"), 0, 0)
rejilla.addWidget(QLabel("C-310"), 1, 0)
rejilla.addWidget(QLabel("M-204"), 2, 0)
rejilla.addWidget(boton_paro, 0, 1, 2, 1)
rejilla.addWidget(boton_arranque, 2, 1, 1, 2)
```

Contesta tres cosas: qué significan cada uno de los cuatro números de `addWidget`, cuál de los dos botones es más alto y cuál más ancho, y qué pasaría si alguien agregara otra etiqueta en la posición 0, 1.

### 15.2 · Aplicar
Formulario de alta con layouts.

Rehaz la captura de órdenes de trabajo sin una sola coordenada. La ventana hereda de `QMainWindow`, con el título `Alta de órdenes de trabajo` y geometría 200, 200, 460, 320.

Sobre el widget central va un `QVBoxLayout`, y dentro de él, en este orden:

1. un `QFormLayout` con cuatro renglones etiquetados `Folio`, `Equipo`, `Prioridad` y `Descripción`, cada uno con su `QLineEdit`;
2. un `QHBoxLayout` con los botones `Guardar` y `Limpiar`;
3. una `QLabel` de aviso que arranca en `Captura una orden`;
4. un `QListWidget` donde se acumula lo capturado.

Guardar agrega a la lista un renglón con folio, equipo y prioridad, actualiza el aviso con el total capturado y limpia los cuatro campos. Limpiar solo vacía los campos. Cada botón se conecta a su propio slot.

Entrega el archivo y dos capturas: la ventana en su tamaño original y la misma ventana estirada al doble de ancho, para demostrar que nada se encima.

### 15.3 · Integrar
El dominio que no sabe de Qt.

Parte la ventana de 15.2 en dos archivos.

En `registro.py` va la excepción `DatoInvalido`, la clase `OrdenDeTrabajo` con `folio`, `tag`, `prioridad`, `descripcion` y un `__str__` que devuelva `OT-1042 B-101 P1: Cambio de sello mecánico`, y la clase `Registro` con una lista privada de órdenes. Su método `alta(folio, tag, prioridad, descripcion)` recibe los cuatro campos como texto, los valida en ese orden y levanta `DatoInvalido` con el mensaje que corresponda:

- el folio lleva al menos seis caracteres;
- la etiqueta lleva al menos tres;
- la prioridad tiene que convertir a entero y quedar entre 1 y 3;
- la descripción no puede ir vacía.

Si todo pasa, construye la orden con la etiqueta en mayúsculas, la guarda y la devuelve. Agrega `listado()` y `__len__`. Debajo, un bloque que solo corra al ejecutar el archivo, que dé de alta OT-1042 en b-101 con prioridad 1 y OT-1043 en C-310 con prioridad 3, y que después intente tres altas malas: folio corto, prioridad 9 y una prioridad escrita con letra. Imprime las dos órdenes buenas, los tres mensajes de rechazo y el total.

En `ventana.py` va la misma ventana de 15.2, pero el slot de guardar llama a `registro.alta` dentro de un `try`. Si la excepción llega, el mensaje se muestra en la etiqueta de aviso y no se agrega nada a la lista. `registro.py` no puede importar PyQt6, y el slot no puede validar nada por su cuenta.

## Semana 16 · Tema 7 · Bases de datos y proyecto

### 16.1 · Reconocer
La conexión que se cerró sin confirmar.

El archivo `refacciones.db` no existe cuando arranca el programa. Predice las dos salidas.

```python
import sqlite3
from pathlib import Path

ruta = Path("refacciones.db")

conexion = sqlite3.connect(ruta)
conexion.execute(
    "CREATE TABLE IF NOT EXISTS Refacciones (clave TEXT PRIMARY KEY, piezas INTEGER)")
conexion.commit()
conexion.close()

conexion = sqlite3.connect(ruta)
conexion.execute("INSERT INTO Refacciones VALUES ('BL-220', 12)")
conexion.close()

conexion = sqlite3.connect(ruta)
cursor = conexion.execute("SELECT COUNT(*) FROM Refacciones")
print(cursor.fetchone())

conexion.execute("INSERT INTO Refacciones VALUES ('SM-4471', 6)")
conexion.commit()
conexion.close()

conexion = sqlite3.connect(ruta)
cursor = conexion.execute("SELECT COUNT(*) FROM Refacciones")
print(cursor.fetchone())
conexion.close()
```

Explica por qué el balero no llegó al disco y el sello sí, y por qué `fetchone` devuelve lo que devuelve en lugar de un número pelón.

### 16.2 · Aplicar
Refacciones en una tabla.

Escribe un programa que cree `almacen.db` con la tabla `Refacciones`, de columnas `clave` como llave primaria, `descripcion` obligatoria y `piezas` obligatoria. Inserta estas cuatro con un ciclo, una llamada a `execute` por refacción, pasando los valores como parámetros:

```python
refacciones = [
    ("BL-220", "balero", 12),
    ("SM-4471", "sello mecánico", 6),
    ("EM-905", "empaque", 30),
    ("RT-118", "retén", 2),
]
```

Después consulta tres cosas, siempre con marcadores y nunca pegando el valor dentro de la cadena: las claves y piezas de lo que tenga menos de 10 piezas ordenado por piezas, la descripción de la clave EM-905, y el total de renglones. Imprime lo que devuelva cada consulta tal como llega.

Todo va dentro de bloques `with`, con `commit` explícito después de las inserciones. Anota en un comentario qué hay que hacer antes de volver a correr el programa y por qué.

### 16.3 · Integrar
Objetos que van y vienen de la base.

Separa el dominio del acceso a datos en un solo archivo, con la regla de que `Refaccion` no puede importar `sqlite3`.

`Refaccion` tiene `clave`, `descripcion` y `piezas`, el método `surtir(cuantas)` que levanta `ValueError` si no alcanzan las piezas, y un `__str__` que devuelva `BL-220 (balero): 12`.

`AlmacenSQLite` recibe la ruta, crea la tabla si no existe en el constructor, y expone tres métodos, con todo el SQL del programa viviendo ahí adentro: `guardar(refaccion)`, `cargar(clave)` que devuelve un objeto `Refaccion` o levanta la excepción propia `RefaccionNoEncontrada`, y `bajo_minimo(minimo)` que devuelve una lista de objetos ordenada por piezas.

Guarda BL-220 balero 12, SM-4471 sello mecánico 6 y RT-118 retén 2. Carga BL-220, súrtele 9 piezas e imprime el objeto. En seguida vuelve a cargar BL-220 de la base e imprímelo también. Los dos números son distintos: explica en un párrafo por qué, y qué método habría que agregarle a la clase de acceso para que dejaran de serlo.

Cierra imprimiendo lo que esté bajo el mínimo de 10, y los mensajes de cargar XX-999 y de surtir 100 piezas al objeto, cada intento en su `try`.

## Semana 17 · Evaluación final

### 17.1 · Reconocer
Cuatro reglas en una sola traza.

Predice las cuatro salidas. Cada una depende de una regla distinta del semestre.

```python
class Activo:
    censo = 0

    def __init__(self, tag):
        self.__tag = tag
        Activo.censo += 1

    @property
    def tag(self):
        return self.__tag

    def clase(self):
        return "activo"

    def ficha(self):
        return f"{self.tag}/{self.clase()}"


class Rotativo(Activo):
    def clase(self):
        return "rotativo"


class Bomba(Rotativo):
    def __init__(self, tag, caudal):
        super().__init__(tag)
        self.caudal = caudal

    def clase(self):
        return "bomba " + super().clase()


b101 = Bomba("B-101", 120.0)

print(b101.ficha())
print(Activo.censo)
print(hasattr(b101, "_Activo__tag"), hasattr(b101, "__tag"))

try:
    b101.tag = "B-999"
except AttributeError:
    print("la propiedad no tiene setter")
```

Nombra las cuatro reglas: por qué `ficha`, que está escrito en la clase de más arriba, termina llamando al método de la nieta; por qué el censo vale lo que vale; qué le pasó al nombre del atributo privado; y qué le falta a la propiedad.

### 17.2 · Aplicar
Contrato, validación y exportación.

Escribe la clase abstracta `Equipo(ABC)` cuyo constructor valide y levante la excepción propia `DatoInvalido`: la etiqueta lleva al menos tres caracteres, y las horas no pueden ser negativas. La etiqueta se guarda limpia y en mayúsculas en un atributo protegido, y las horas en uno privado. Expón `tag` y `horas` como propiedades de solo lectura. Declara abstractos `consumo_kw()` y `tipo()`, y escribe el método concreto `fila()`, que devuelva un diccionario con las llaves `tag`, `tipo`, `horas` sin decimales y `kw` con uno.

`Bomba` recibe caudal y consume 0.32 kW por cada L/s. `Compresor` recibe presión y consume 8.0 kW por bar.

Escribe la función `exportar(equipos, ruta)`, que guarde un CSV con `DictWriter` y encabezado, dentro de un `with`, con `newline` vacío y `encoding` explícito.

Construye la planta con `b-101` de 4820.0 h y 120.0 L/s, `B-102` de 1150.0 h y 95.0 L/s, y `c-310` de 6300.0 h y 8.5 bar. Después intenta agregar dos equipos malos, `XX` con 100.0 h y `B-103` con horas negativas, cada uno en su `try`, e imprime los mensajes. Exporta a `equipos.csv`, imprime el contenido del archivo y el total de equipos que sí entraron.

### 17.3 · Integrar
De la telemetría al reporte.

El examen final es integrador: una sola pregunta toca modelado, colecciones, errores, archivos y persistencia. Este ejercicio tiene esa forma.

Escribe un programa que reciba la telemetría cruda, la valide contra el tablero de instrumentos, guarde lo aceptado en SQLite y produzca un reporte en texto.

- `Instrumento(ABC)` recibe etiqueta, mínimo y máximo, expone `tag` como propiedad, declara abstracto `unidad()`, y trae el método concreto `validar(texto)`, que convierte a `float` y levanta `LecturaInvalida` cuando el texto no es número o cuando el valor sale del rango. El mensaje del rango incluye la unidad. Las hijas son `Termopar` en C, `Manometro` en bar y `Caudalimetro` en L/s.
- `Historico` recibe la ruta de la base, crea en el constructor la tabla `Lecturas` con `id` como llave primaria, `tag` y `valor`, y expone `guardar(tag, valor)` y `valores(tag)`. Todo el SQL vive en esta clase y usa marcadores.
- `cargar_crudas(ruta)` lee el CSV con `DictReader` y devuelve lista vacía si el archivo no existe.
- `escribir_reporte(ruta, resumen, descartadas)` escribe el encabezado `Reporte de telemetría`, un renglón por instrumento con dos decimales, el conteo de descartadas y una línea con sangría por cada motivo.

El tablero tiene TT-101 de 0.0 a 400.0, PT-205 de 0.0 a 10.0 y FT-330 de 0.0 a 200.0. El programa escribe primero `crudas.csv` con estas siete filas y a partir de ahí trabaja sobre el archivo, no sobre la lista:

```python
crudas = [
    {"tag": "TT-101", "valor": "74.5"},
    {"tag": "PT-205", "valor": "6.1"},
    {"tag": "TT-101", "valor": "81.2"},
    {"tag": "FT-330", "valor": "118.0"},
    {"tag": "PT-205", "valor": "s/d"},
    {"tag": "TT-101", "valor": "412.0"},
    {"tag": "XX-999", "valor": "3.0"},
]
```

La etiqueta que no está en el tablero se descarta con una comprobación previa, sin excepción. El resto se valida en un `try` con el tipo nombrado. El promedio de cada instrumento se calcula sobre lo que devolvió la base, no sobre la lista en memoria. Al final imprime el reporte completo y los valores guardados de TT-101.
