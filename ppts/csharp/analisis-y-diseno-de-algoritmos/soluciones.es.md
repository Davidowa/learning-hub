# Soluciones · Análisis y Diseño de Algoritmos · COM101

Documento del profesor. Cada solución se compiló y se corrió con el SDK 10.0.302 sobre `net10.0` antes de escribirse, y la salida que aparece aquí es la que produjo la máquina, no la que debería producir. Los códigos de salida se midieron en PowerShell 7 sobre Windows 11. La numeración es la misma del archivo de ejercicios.

## Semana 01 · Encuadre y criterios de evaluación

### 01.1 · Reconocer

**Solución**

```csharp
Console.WriteLine(10478 / 7);
Console.WriteLine(0.1 + 0.7);
Console.WriteLine(0.1 + 0.7 == 0.8);
```

Los dos operandos de la primera línea son enteros, así que la barra hace división entera y tira el residuo. La segunda y la tercera son el mismo hecho visto dos veces: 0.1 y 0.7 no tienen representación exacta en binario y su suma cae un poco abajo de 0.8.

**Salida**

```text
1496
0.7999999999999999
False
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| Las tres predicciones están escritas antes de la corrida | 3 |
| Las tres salidas reales están pegadas sin editar | 3 |
| Explica que la barra entre dos enteros trunca | 2 |
| Explica que la suma binaria no cae en 0.8 | 2 |

**Error que más se ve**

Escriben 1496.857142857143 en la primera predicción; se delata porque la misma hoja acepta después que el resultado fue 1496 sin explicar de dónde salió el cambio.

### 01.2 · Aplicar

**Solución**

```csharp
Console.WriteLine("BANCO DE PRUEBAS EST-07");
Console.WriteLine("Canal A · transportador de rodillos");
Console.WriteLine("Banda nominal: 1480 a 1520 rpm");
Console.WriteLine(Environment.Version);
```

**Salida**

```text
BANCO DE PRUEBAS EST-07
Canal A · transportador de rodillos
Banda nominal: 1480 a 1520 rpm
10.0.10
```

El código de salida fue 0. El último renglón depende de la máquina: `Environment.Version` reporta el runtime y `dotnet --version` reporta el SDK, y en este equipo son 10.0.10 y 10.0.302.

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| Los tres renglones de texto salen en el orden pedido | 3 |
| Aparece el valor de `Environment.Version` de su máquina | 3 |
| La corrida se hizo con `dotnet run` y se ve la terminal | 2 |
| Reporta el código de salida | 2 |

**Error que más se ve**

Copian el número de versión de la captura de un compañero; se delata porque el número no coincide con el `dotnet --version` que ellos mismos entregaron en la misma hoja.

### 01.3 · Integrar

**Solución**

Con `<ImplicitUsings>disable</ImplicitUsings>` el compilador ya no genera `obj/Debug/net10.0/est07.GlobalUsings.g.cs`, así que `Console` deja de existir en el contexto. La línea que lo arregla sin tocar el `csproj` es `using System;` arriba del archivo.

```csharp
using System;

Console.WriteLine("EST-07 en linea");
```

**Salida**

Con la propiedad apagada y sin el `using`:

```text
Program.cs(1,1): error CS0103: The name 'Console' does not exist in the current context

Build FAILED.
    0 Warning(s)
    1 Error(s)
```

La carpeta `bin/Debug/net10.0` queda con cero archivos. Con el `using` agregado la compilación pasa y el programa imprime `EST-07 en linea`.

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| Cita el mensaje completo con archivo, línea, columna y clave | 3 |
| Reporta que la carpeta de salida quedó vacía | 3 |
| Da la línea `using System;` y la comprueba corriendo | 3 |
| Distingue el archivo generado del `csproj` que lo pide | 1 |

**Error que más se ve**

Regresan la propiedad a `enable` y reportan que «ya funciona»; se delata porque el `csproj` que entregan no trae `disable` en ningún lado.

## Semana 02 · Tema 1 · Diseño de algoritmos

### 02.1 · Reconocer

**Solución**

La traza tiene siete renglones. El nivel arranca en 12.0 y sube de 15.0 en 15.0 hasta que la condición deja de cumplirse.

| Paso | nivel antes | nivel después | Lo que imprime |
|---|---|---|---|
| 0 | 12.0 | 12.0 | PURGA DE AIRE INICIADA |
| 1 | 12.0 | 27.0 | llenando tanque: 27.0 L |
| 2 | 27.0 | 42.0 | llenando tanque: 42.0 L |
| 3 | 42.0 | 57.0 | llenando tanque: 57.0 L |
| 4 | 57.0 | 72.0 | llenando tanque: 72.0 L |
| 5 | 72.0 | 72.0 | nivel alcanzado, abrir bomba de recirculacion |
| 6 | 72.0 | 72.0 | banco listo |

El tanque termina con 72.0 litros, no con 60.0. La condición se revisa antes de cada pulso y el último pulso entra completo, así que el nivel se pasa del setpoint por doce litros.

**Salida**

Corrida del pseudocódigo traducido a C#:

```text
PURGA DE AIRE INICIADA
llenando tanque: 27.0 L
llenando tanque: 42.0 L
llenando tanque: 57.0 L
llenando tanque: 72.0 L
nivel alcanzado, abrir bomba de recirculacion
banco listo
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| Los cuatro valores de nivel son 27.0, 42.0, 57.0 y 72.0 | 4 |
| Cuenta los siete renglones, con la cabecera y el cierre | 2 |
| Dice que el tanque termina en 72.0 y no en 60.0 | 2 |
| Explica que el pulso entra completo después de la revisión | 2 |

**Error que más se ve**

Escriben tres pulsos y dejan el tanque en 57.0, porque paran cuando el nivel «ya casi llega»; se delata porque su última línea dice ABORTAR aunque el nivel que escribieron es menor que el setpoint que ellos mismos copiaron.

### 02.2 · Aplicar

**Solución**

```text
INICIA
    LEER puerta, paro, rpm

    SI puerta = cerrada ENTONCES
        SI paro = liberado ENTONCES
            SI rpm < 50 ENTONCES
                ESCRIBIR "ARMADO"
            SI NO
                ESCRIBIR "ENCLAVADO: el eje todavia gira"
        SI NO
            ESCRIBIR "ENCLAVADO: paro de emergencia oprimido"
    SI NO
        ESCRIBIR "ENCLAVADO: puerta de guarda abierta"
TERMINA
```

El diagrama de flujo lleva tres rombos en cascada, cada uno con su salida por el NO hacia un rectángulo de mensaje distinto, y una sola salida por el SÍ que llega al rectángulo de ARMADO.

**Salida**

Traza esperada, escrita antes de correr nada:

```text
puerta cerrada, paro liberado, 20 rpm
ARMADO

puerta abierta, paro liberado, 20 rpm
ENCLAVADO: puerta de guarda abierta
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| Las tres condiciones se revisan en el orden pedido | 3 |
| Cada falla nombra su causa, no un mensaje genérico | 3 |
| El diagrama tiene los tres rombos con sus dos salidas | 2 |
| Las dos trazas esperadas están escritas antes de correr | 2 |

**Error que más se ve**

Un solo rombo con las tres condiciones pegadas y un solo mensaje de ENCLAVADO; se delata porque el segundo juego de datos no puede decir cuál de las tres falló.

### 02.3 · Integrar

**Solución**

La instrucción original rompe la precisión: «firme» lo decide quien lea, y dos técnicos van a apretar distinto. Rompe también lo finito, porque «hasta que quede firme» no dice en cuántos pasos termina.

```text
INICIA
    lineas = 0

    PARA pasada = 1 HASTA 3
        par = pasada * 8
        PARA tornillo = 1 HASTA 4
            ESCRIBIR "pasada", pasada, "tornillo", tornillo,
                     ": apretar a", par, "N·m"
            lineas = lineas + 1

    ESCRIBIR "apriete terminado en", lineas, "operaciones"
TERMINA
```

**Salida**

```text
pasada 1 tornillo 1: apretar a 8 N·m
pasada 1 tornillo 2: apretar a 8 N·m
pasada 1 tornillo 3: apretar a 8 N·m
pasada 1 tornillo 4: apretar a 8 N·m
pasada 2 tornillo 1: apretar a 16 N·m
pasada 2 tornillo 2: apretar a 16 N·m
pasada 2 tornillo 3: apretar a 16 N·m
pasada 2 tornillo 4: apretar a 16 N·m
pasada 3 tornillo 1: apretar a 24 N·m
pasada 3 tornillo 2: apretar a 24 N·m
pasada 3 tornillo 3: apretar a 24 N·m
pasada 3 tornillo 4: apretar a 24 N·m
apriete terminado en 12 operaciones
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| Nombra la propiedad que se rompe y la argumenta | 2 |
| Los dos PARA están anidados y el par sale de la pasada | 3 |
| La traza tiene los doce renglones en el orden correcto | 3 |
| La última línea reporta 12 operaciones | 2 |

**Error que más se ve**

Anidan al revés, con el tornillo afuera y la pasada adentro, y aprietan cada tornillo a 24 N·m antes de tocar el siguiente; se delata porque la traza que entregan sube el par de tres en tres dentro de un mismo tornillo, que es justo lo que el apriete en cruz existe para evitar.

## Semana 03 · Tema 2 · Introducción a la programación

### 03.1 · Reconocer

**Solución**

| Caso | Compila | Primer mensaje | Qué leyó mal |
|---|---|---|---|
| A | no | `Program.cs(2,30): error CS1002: ; expected` | La instrucción no terminó y sigue esperando |
| B | no | `Program.cs(2,5): error CS1001: Identifier expected` | Leyó `int`, esperaba nombre y encontró un dígito |
| C | no | `Program.cs(2,9): error CS0117: 'Console' does not contain a definition for 'writeline'` | El tipo existe, el miembro con esa caja no |
| D | no | `Program.cs(2,19): error CS0103: The name 'ParNominal' does not exist in the current context` | El nombre es del alumno y no existe en ningún lado |
| E | no | `Program.cs(1,5): error CS1001: Identifier expected` | `class` es palabra reservada y no puede ser nombre |

El caso E devuelve siete errores. Después del `int class` el analizador cree que empieza una declaración de tipo, y todo lo que sigue en la misma línea se vuelve un tropiezo nuevo: `CS1002`, otro `CS1001`, `CS1514`, `CS1513`, `CS8803` y `CS1525`.

**Salida**

```text
E · int class = 7;

Program.cs(1,5): error CS1001: Identifier expected
Program.cs(1,5): error CS1002: ; expected
Program.cs(1,11): error CS1001: Identifier expected
Program.cs(1,11): error CS1514: { expected
Program.cs(1,11): error CS1513: } expected
Program.cs(1,11): error CS8803: Top-level statements must precede namespace and type declarations.
Program.cs(1,11): error CS1525: Invalid expression term '='

Build FAILED.
    0 Warning(s)
    7 Error(s)
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| Las cinco claves están bien asignadas | 5 |
| Identifica el caso E como el de siete errores | 2 |
| Explica que C y D fallan por caja pero con claves distintas | 2 |
| Ninguno de los cinco se declara «compila» | 1 |

**Error que más se ve**

Dicen que C y D dan la misma clave porque «los dos son de mayúsculas»; se delata porque no pegan el mensaje, solo lo describen.

### 03.2 · Aplicar

**Solución**

```csharp
// Semana 3 · 3.2 · sensibilidad a mayúsculas y convenciones
int parNominal = 24;      // par de apriete nominal, en N·m
/* La misma palabra con otra caja
   es otra variable distinta. */
int ParNominal = 26;
int PARNOMINAL = 22;

Console.WriteLine($"parNominal={parNominal} ParNominal={ParNominal} PARNOMINAL={PARNOMINAL}");
Console.WriteLine("distintas: " + (parNominal != ParNominal));
Console.WriteLine("texto con // adentro: " + "revisar // antes del turno");
Console.WriteLine("Console vs console: " + ("Console" == "console"));
```

**Salida**

```text
parNominal=24 ParNominal=26 PARNOMINAL=22
distintas: True
texto con // adentro: revisar // antes del turno
Console vs console: False
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| Las tres variables conviven y se imprimen en un renglón | 3 |
| Los dos comentarios están y el `//` dentro del texto sobrevive | 3 |
| La comparación de las dos cadenas imprime `False` | 2 |
| Los nombres siguen camelCase y hay un comentario que dice la unidad | 2 |

**Error que más se ve**

Escriben `parnominal` en una de las tres impresiones y el programa deja de compilar con `CS0103`; se delata porque entregan el `.cs` sin salida y con una nota que dice «no me corrió».

### 03.3 · Integrar

**Solución**

Cuatro archivos, cuatro intentos, un mensaje cada uno.

```csharp
// A · falta el punto y coma
int parNominal = 24;
Console.WriteLine(parNominal)

// B · identificador que abre con dígito
int parNominal = 24;
int 2sensor = 7;
Console.WriteLine(parNominal);

// C · miembro con la caja equivocada
int parNominal = 24;
Console.writeline(parNominal);

// D · nombre propio con la caja equivocada
int parNominal = 24;
Console.WriteLine(ParNominal);
```

**Salida**

```text
A  Program.cs(2,30): error CS1002: ; expected
B  Program.cs(2,5): error CS1001: Identifier expected
C  Program.cs(2,9): error CS0117: 'Console' does not contain a definition for 'writeline'
D  Program.cs(2,19): error CS0103: The name 'ParNominal' does not exist in the current context
```

C y D nacen del mismo descuido y devuelven claves distintas porque el nombre de C pertenece al framework. `Console` sí existe, así que el compilador puede decir exactamente qué miembro le falta. `ParNominal` no existe en ningún lado, y lo único que puede contestar es que no lo conoce.

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| Los cuatro mensajes están copiados textual, con línea y columna | 4 |
| Cada caso trae un renglón que dice qué leyó mal el compilador | 3 |
| Explica la diferencia entre CS0117 y CS0103 | 2 |
| Los cuatro intentos se corrieron por separado | 1 |

**Error que más se ve**

Meten los cuatro descuidos en un solo archivo y reportan el primer mensaje del montón; se delata porque la clave que citan es `CS1003` y no aparece en ninguno de los cuatro casos por separado.

## Semana 04 · Tema 3 · Datos, tipos y operaciones primitivas

### 04.1 · Reconocer

**Solución**

```csharp
int lo = 1471, hi = 1533;
Console.WriteLine(lo + hi / 2);
Console.WriteLine((lo + hi) / 2);
Console.WriteLine((lo + hi) / 2.0);
Console.WriteLine(hi % 100);
Console.WriteLine(7 / 2 * 2);
```

La división liga más fuerte que la suma, así que la primera línea calcula 1471 más 766. La tercera divide entre un literal real y por eso el resultado ya no trunca, aunque en este caso la suma sea par y el número coincida. La quinta agrupa de izquierda a derecha: primero 7 entre 2 da 3, luego 3 por 2 da 6.

**Salida**

```text
2237
1502
1502
33
6
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| Las cinco predicciones coinciden con la corrida | 5 |
| Señala la primera línea como la imposible de leer en un tacómetro | 2 |
| Nombra la precedencia como la causa | 2 |
| Explica el 6 de la última línea por asociatividad | 1 |

**Error que más se ve**

Predicen 3.5 en la última línea; se delata porque la misma hoja acepta que la barra entre enteros trunca dos renglones antes.

### 04.2 · Aplicar

**Solución**

```csharp
const double Nominal = 25.0;

string estacion = "EST-11";
char canal = 'C';
int muestras = 12;
double lectura = 24.972;
bool enLinea = true;

double desv = lectura - Nominal;
bool dentro = Math.Abs(desv) <= 0.05;

Console.WriteLine($"estacion {estacion} canal {canal}");
Console.WriteLine($"muestras {muestras}  en linea {enLinea}");
Console.WriteLine($"lectura  {lectura:F3} mm");
Console.WriteLine($"nominal  {Nominal:F3} mm");
Console.WriteLine($"desviacion cruda {desv}");
Console.WriteLine($"desviacion {desv:F3} mm");
Console.WriteLine($"dentro de +-0.05 -> {dentro}");
```

**Salida**

```text
estacion EST-11 canal C
muestras 12  en linea True
lectura  24.972 mm
nominal  25.000 mm
desviacion cruda -0.027999999999998693
desviacion -0.028 mm
dentro de +-0.05 -> True
```

La desviación cruda no es -0.028. La resta de dos números que ninguno cabe exacto en binario deja quince dígitos de ruido, y por eso la tolerancia se revisa con `Math.Abs` contra un margen y nunca con una igualdad.

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| Los cinco tipos están y cada uno guarda el dato que le toca | 3 |
| La cota nominal está bajo `const` | 2 |
| La desviación se imprime cruda y con tres decimales | 2 |
| La tolerancia se revisa con `Math.Abs` y no con `==` | 3 |

**Error que más se ve**

Declaran `int lectura = 24;` porque «el calibre da milímetros»; se delata porque su desviación imprime -1 y la tolerancia sale en `False` con una pieza que sí estaba buena.

### 04.3 · Integrar

**Solución**

```csharp
byte piezas = 250;
piezas += 10;
Console.WriteLine($"piezas inspeccionadas: {piezas}");

short ventana = 32000;
ventana += 1000;
Console.WriteLine($"ventana de muestreo:   {ventana}");

double real = 0.5 + 1.5 + 2.5 + 3.5;
double alPar = Math.Round(0.5) + Math.Round(1.5)
             + Math.Round(2.5) + Math.Round(3.5);
double lejos = Math.Round(0.5, MidpointRounding.AwayFromZero)
             + Math.Round(1.5, MidpointRounding.AwayFromZero)
             + Math.Round(2.5, MidpointRounding.AwayFromZero)
             + Math.Round(3.5, MidpointRounding.AwayFromZero);

Console.WriteLine($"suma real          {real}");
Console.WriteLine($"suma mitad al par  {alPar}");
Console.WriteLine($"suma mitad lejos   {lejos}");

int lo = 1471, hi = 1533;
Console.WriteLine($"sin parentesis {lo + hi / 2}");
Console.WriteLine($"con parentesis {(lo + hi) / 2}");
```

**Salida**

```text
piezas inspeccionadas: 4
ventana de muestreo:   -32536
suma real          8
suma mitad al par  8
suma mitad lejos   10
sin parentesis 2237
con parentesis 1502
```

El `+=` mete un cast que la forma larga no tiene, así que las dos primeras líneas compilan con cero advertencias y dan la vuelta en silencio. Para reportar el desgaste acumulado conviene la regla mitad al par, porque sobre muchos valores no arrastra el sesgo hacia arriba: sobre estas cuatro desviaciones da 8, el mismo total que la suma real, mientras que mitad lejos de cero da 10.

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| Los dos desbordamientos se reportan con su valor real | 3 |
| Las tres sumas de redondeo están y no coinciden entre sí | 3 |
| Las dos versiones del punto medio están corridas | 2 |
| Justifica la regla de redondeo con el sesgo, no con el gusto | 2 |

**Error que más se ve**

Reportan que el `byte` «da error»; se delata porque su captura muestra `Build succeeded` con cero advertencias arriba del 4.

## Semana 05 · Tema 4 · Instrucciones, lectura y escritura

### 05.1 · Reconocer

**Solución**

```csharp
int lo = 1480, hi = 1520;
Console.WriteLine("rpm " + lo + hi);
Console.WriteLine("rpm " + (lo + hi));
Console.WriteLine(lo + hi + " rpm");
Console.WriteLine($"rpm {lo + hi}");
Console.WriteLine("desviaciones " + 2 + 3 + 4);
```

Se lee de izquierda a derecha. Mientras los dos lados sean números, el más suma; en cuanto uno de los dos es texto, el más pega y todo lo que venga después ya se pega también.

**Salida**

```text
rpm 14801520
rpm 3000
3000 rpm
rpm 3000
desviaciones 234
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| Las cinco predicciones coinciden con la corrida | 5 |
| Explica la regla de izquierda a derecha | 3 |
| Señala que la tercera suma primero porque el texto va al final | 2 |

**Error que más se ve**

Predicen 3000 en la primera línea porque «los paréntesis se sobreentienden»; se delata porque la segunda línea, que sí los trae, la predicen igual.

### 05.2 · Aplicar

**Solución**

```csharp
Console.Write("Etiqueta de estacion: ");
string etiqueta = Console.ReadLine() ?? "";

Console.Write("Muestras tomadas: ");
string sMuestras = Console.ReadLine() ?? "";
bool okMuestras = int.TryParse(sMuestras, out int muestras);

Console.Write("Lectura en rpm: ");
string sLectura = Console.ReadLine() ?? "";
bool okLectura = double.TryParse(sLectura, out double lectura);

Console.WriteLine();
Console.WriteLine($"etiqueta        {etiqueta}");
Console.WriteLine($"muestras leidas {okMuestras}  valor {muestras}");
Console.WriteLine($"lectura leida   {okLectura}  valor {lectura:F3} rpm");
Console.WriteLine($"ciclos del turno {148230:N0}");
```

**Salida**

Con las entradas `EST-07`, `12` y `1496.857142857143`:

```text
Etiqueta de estacion: Muestras tomadas: Lectura en rpm: 
etiqueta        EST-07
muestras leidas True  valor 12
lectura leida   True  valor 1496.857 rpm
ciclos del turno 148,230
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| Los tres avisos usan `Console.Write` y no `WriteLine` | 2 |
| Cada línea se guarda en una variable antes de convertirla | 2 |
| Las dos conversiones son `TryParse` y su `bool` se imprime | 3 |
| La lectura sale con tres decimales y los ciclos con separador | 3 |

**Error que más se ve**

Usan `Convert.ToInt32` porque «es más corto»; se delata porque el programa truena con `FormatException` en cuanto el revisor teclea algo que no es número.

### 05.3 · Integrar

**Solución**

```csharp
using System.Globalization;

CultureInfo.CurrentCulture = new CultureInfo("es-MX");
bool okMx = double.TryParse("480.50", out double mx);
Console.WriteLine($"es-MX  TryParse -> {okMx}   valor {mx}");
Console.WriteLine($"es-MX  {1496.857142:F2} rpm");
Console.WriteLine($"es-MX  {148230:N0} ciclos");
Console.WriteLine($"es-MX  {0.0342:P1} fuera de banda");

CultureInfo.CurrentCulture = new CultureInfo("de-DE");
bool okDe = double.TryParse("480.50", out double de);
Console.WriteLine($"de-DE  TryParse -> {okDe}   valor {de}");
Console.WriteLine($"de-DE  {1496.857142:F2} rpm");
Console.WriteLine($"de-DE  {148230:N0} ciclos");
Console.WriteLine($"de-DE  {0.0342:P1} fuera de banda");

CultureInfo.CurrentCulture = new CultureInfo("es-MX");
double carga = 480.50 / 1.10;
Console.WriteLine($"cruda  {carga}");
Console.WriteLine($"a F2   {carga:F2} kN");
```

**Salida**

```text
es-MX  TryParse -> True   valor 480.5
es-MX  1496.86 rpm
es-MX  148,230 ciclos
es-MX  3.4% fuera de banda
de-DE  TryParse -> True   valor 48050
de-DE  1496,86 rpm
de-DE  148.230 ciclos
de-DE  3,4 % fuera de banda
cruda  436.81818181818176
a F2   436.82 kN
```

Bajo `de-DE` el punto es separador de miles, así que `480.50` se lee como cuarenta y ocho mil cincuenta y el guardia devuelve `True` de todos modos. Revisar el `bool` solo dice que el texto se pudo convertir, no que se haya convertido a lo que el operador quiso decir. Lo que falta es fijar la cultura de la conversión, con `CultureInfo.InvariantCulture` cuando el dato viene de un archivo o de un equipo.

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| Las dos conversiones están, cada una con su cultura fijada | 3 |
| Los tres especificadores aparecen en las dos culturas | 3 |
| El factor de seguridad se imprime crudo y con dos decimales | 2 |
| Explica por qué el `bool` en `True` no garantiza el valor | 2 |

**Error que más se ve**

Dejan la cultura en `de-DE` al final y reportan la carga como 436,82 sin notarlo; se delata porque el mismo documento afirma que la máquina está configurada en español de México.

## Semana 06 · Tema 4.4 · Estructuras de selección

### 06.1 · Reconocer

**Solución**

Sin llaves solo la línea que sigue al `if` pertenece a la decisión. La segunda corre siempre, aunque la sangría prometa otra cosa.

```csharp
double refrig = 26.8;

if (refrig > 28.0)
    Console.WriteLine("alarma: refrigerante caliente");
    Console.WriteLine("valvula de derivacion abierta");

Console.WriteLine($"lectura {refrig} C registrada");
```

**Salida**

```text
valvula de derivacion abierta
lectura 26.8 C registrada
```

Con `refrig = 31.4` imprime los tres renglones. La falla que provoca es la peor de las dos: con el refrigerante a 26.8 grados, que está frío, la derivación queda abierta y el reductor trabaja sin refrigerante en el circuito principal, sin que ninguna alarma lo diga.

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| Predice dos renglones y nombra cuáles | 4 |
| Predice tres renglones con la lectura de 31.4 | 2 |
| Explica que las llaves, no la sangría, marcan el bloque | 2 |
| Nombra la falla física que produce el descuido | 2 |

**Error que más se ve**

Predicen un solo renglón, el de la lectura registrada; se delata porque en su explicación dicen que «el `if` es falso, así que las dos líneas se saltan», que es exactamente la lectura que las llaves habrían hecho cierta.

### 06.2 · Aplicar

**Solución**

```csharp
Console.Write("rpm del eje: ");
string linea = Console.ReadLine() ?? "";
bool leido = int.TryParse(linea, out int rpm);

if (!leido)
{
    Console.WriteLine("lectura no numerica, canal descartado");
}
else if (rpm < 0)
{
    Console.WriteLine($"{rpm} rpm -> invalida, revisar cable del tacometro");
}
else if (rpm < 800)
{
    Console.WriteLine($"{rpm} rpm -> en reposo");
}
else if (rpm < 3000)
{
    Console.WriteLine($"{rpm} rpm -> nominal");
}
else
{
    Console.WriteLine($"{rpm} rpm -> sobrevelocidad, cortar par");
}
```

**Salida**

```text
rpm del eje: 800 rpm -> nominal
rpm del eje: -5 rpm -> invalida, revisar cable del tacometro
rpm del eje: 799 rpm -> en reposo
rpm del eje: 3000 rpm -> sobrevelocidad, cortar par
rpm del eje: lectura no numerica, canal descartado
```

El peldaño dice estrictamente menor que 800, así que 799 todavía cae en reposo y 800 ya pertenece a la banda de arriba. El valor del límite siempre es de la banda superior cuando la comparación es estricta.

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| El guardia de `TryParse` es el primer peldaño | 2 |
| Los cinco casos están y son excluyentes | 3 |
| Las cinco corridas están pegadas con su salida real | 3 |
| Explica a qué banda pertenece el valor del límite | 2 |

**Error que más se ve**

Ponen el peldaño de reposo arriba del de lectura negativa, y entonces el tacómetro desconectado se reporta como eje detenido; se delata porque su corrida con `-5` dice «en reposo» y compila sin una sola advertencia.

### 06.3 · Integrar

**Solución**

```csharp
const double LimiteC = 28.0;

Console.Write("temperatura del refrigerante en C: ");
string sTemp = Console.ReadLine() ?? "";
bool okTemp = double.TryParse(sTemp, out double temp);

Console.Write("rpm del eje: ");
string sRpm = Console.ReadLine() ?? "";
bool okRpm = int.TryParse(sRpm, out int rpm);

bool caliente = temp > LimiteC;
bool enElLimite = temp == LimiteC;

if (!okTemp)
{
    Console.WriteLine("temperatura no numerica, enclavamiento por falta de dato");
}
else if (!okRpm)
{
    Console.WriteLine("rpm no numerica, enclavamiento por falta de dato");
}
else if (caliente)
{
    Console.WriteLine($"lectura {temp:F1} C sobre {LimiteC:F1} C");
    Console.WriteLine("derivacion ABIERTA");
}
else
{
    Console.WriteLine($"lectura {temp:F1} C bajo o en {LimiteC:F1} C");
    Console.WriteLine("derivacion cerrada");
}

Console.WriteLine($"caliente {caliente}  en el limite {enElLimite}  rpm {rpm}");
```

**Salida**

```text
temperatura del refrigerante en C: rpm del eje: lectura 31.4 C sobre 28.0 C
derivacion ABIERTA
caliente True  en el limite False  rpm 1502

temperatura del refrigerante en C: rpm del eje: lectura 28.0 C bajo o en 28.0 C
derivacion cerrada
caliente False  en el limite True  rpm 1502

temperatura del refrigerante en C: rpm del eje: temperatura no numerica, enclavamiento por falta de dato
caliente False  en el limite False  rpm 1502
```

Con `>=` en lugar de `>`, el segundo juego habría abierto la derivación. La lectura de 28.0 cae exactamente sobre la raya y lo único que decide de qué lado queda es el carácter de más en el operador.

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| El límite está bajo `const` y las dos capturas usan `TryParse` | 3 |
| La escalera revisa los guardias antes que las bandas | 2 |
| La última línea corre en los cuatro caminos | 2 |
| Las tres corridas están pegadas | 2 |
| Explica el cambio que produce `>=` sobre la lectura de 28.0 | 1 |

**Error que más se ve**

Meten la última línea dentro del `else` final, y entonces las corridas con captura inválida no imprimen los `bool`; se delata porque su tercera corrida tiene dos renglones y las otras tres.

## Semana 07 · Tema 4.4 · Selección, profundización

### 07.1 · Reconocer

**Solución**

```csharp
int suma = 0, cuenta = 0;

if (cuenta > 0 && suma / cuenta > 1500)
    Console.WriteLine("media alta");
Console.WriteLine("A: con && la ventana vacia sobrevive");

double c = -3.0;
string dijo = "(nada)";
if (c > 0)
    if (c > 10)
        dijo = "sobre el limite";
    else
        dijo = "bajo el limite";
Console.WriteLine($"B: con c = {c} -> {dijo}");

double lectura = 0.1 + 0.2;
Console.WriteLine($"C: 0.1 + 0.2 == 0.3 -> {lectura == 0.3}");
Console.WriteLine($"D: |dif| < 1e-9     -> {Math.Abs(lectura - 0.3) < 1e-9}");
```

**Salida**

```text
A: con && la ventana vacia sobrevive
B: con c = -3 -> (nada)
C: 0.1 + 0.2 == 0.3 -> False
D: |dif| < 1e-9     -> True
```

Con un solo `&` el corto circuito desaparece, los dos lados se evalúan y la división entre cero mata el programa con `DivideByZeroException` antes de imprimir nada. El `else` del segundo bloque se ligó al `if` interno, el de `c > 10`, y no al externo como promete la sangría. Por eso una lectura de -3 grados, que es el termopar desconectado, no imprime absolutamente nada sobre sí misma.

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| Los cuatro renglones predichos coinciden | 4 |
| Dice que con `&` el programa truena y nombra la excepción | 3 |
| Identifica a cuál `if` se ligó el `else` | 3 |

**Error que más se ve**

Predicen `bajo el limite` en el renglón B, leyendo la sangría; se delata porque el mismo alumno afirma después que el `else` pertenece al `if` externo, que es justo lo contrario de lo que hace el compilador.

### 07.2 · Aplicar

**Solución**

```csharp
const double Nominal = 25.00;
const double Tolerancia = 0.05;

Console.Write("cota medida en mm: ");
bool okCota = double.TryParse(Console.ReadLine(), out double medida);

Console.Write("temperatura del refrigerante en C: ");
bool okTemp = double.TryParse(Console.ReadLine(), out double temp);

if (!okCota || !okTemp)
{
    Console.WriteLine("captura invalida, la pieza no se dictamina");
}
else
{
    double desvio = Math.Abs(medida - Nominal);
    bool dentro = desvio <= Tolerancia;

    string dictamen = dentro switch
    {
        true => "acepta",
        false => "rechaza"
    };

    string banda = temp switch
    {
        < 0.0 => "sensor desconectado",
        < 20.0 => "frio",
        <= 28.0 => "nominal",
        < 90.0 => "caliente, derivacion abierta",
        _ => "paro por sobretemperatura"
    };

    Console.WriteLine($"cota    {medida:F2} mm   desvio {desvio:F4} mm");
    Console.WriteLine($"cota    {dictamen}");
    Console.WriteLine($"refrig  {temp:F1} C -> {banda}");
}
```

**Salida**

```text
cota medida en mm: temperatura del refrigerante en C: cota    25.06 mm   desvio 0.0600 mm
cota    rechaza
refrig  31.4 C -> caliente, derivacion abierta

cota medida en mm: temperatura del refrigerante en C: cota    24.97 mm   desvio 0.0300 mm
cota    acepta
refrig  28.0 C -> nominal

cota medida en mm: temperatura del refrigerante en C: cota    25.00 mm   desvio 0.0000 mm
cota    acepta
refrig  -3.0 C -> sensor desconectado

cota medida en mm: temperatura del refrigerante en C: captura invalida, la pieza no se dictamina
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| El guardia de captura va primero y corta el resto del cálculo | 2 |
| La tolerancia se decide con `Math.Abs` contra un margen declarado | 3 |
| La expresión `switch` tiene sus brazos en orden y su descarte | 3 |
| Las cuatro corridas están pegadas, incluida la de captura mala | 2 |

**Error que más se ve**

Ordenan los brazos con `< 90.0` arriba de `< 20.0`; se delata porque el compilador contesta `CS8510: The pattern is unreachable` y el archivo que entregan no compila.

### 07.3 · Integrar

**Solución**

```csharp
Console.Write("presion en bar: ");
bool okP = double.TryParse(Console.ReadLine(), out double presion);

Console.Write("puerta cerrada (1 = si, 0 = no): ");
bool okD = int.TryParse(Console.ReadLine(), out int puertaNum);

Console.Write("modo (0 paro, 1 automatico, 2 jog): ");
bool okM = int.TryParse(Console.ReadLine(), out int modo);

if (!okP || !okD || !okM)
{
    Console.WriteLine("captura invalida, la maquina queda enclavada");
}
else
{
    bool puerta = puertaNum == 1;
    bool presionOk = presion >= 3.5 && presion <= 5.0;
    bool arrancar = presionOk && puerta && modo == 1;

    string estadoModo = modo switch
    {
        0 => "paro",
        1 => "automatico",
        2 => "jog",
        _ => "modo desconocido"
    };

    Console.WriteLine($"presion {presion:F2} bar en rango -> {presionOk}");
    Console.WriteLine($"puerta cerrada            -> {puerta}");
    Console.WriteLine($"modo {modo}                    -> {estadoModo}");
    Console.WriteLine($"arrancar                  -> {arrancar}");

    if (!arrancar)
    {
        if (!presionOk)
        {
            Console.WriteLine("causa: presion fuera de 3.5 a 5.0 bar");
        }
        else if (!puerta)
        {
            Console.WriteLine("causa: puerta abierta");
        }
        else
        {
            Console.WriteLine("causa: la maquina no esta en automatico");
        }
    }
}
```

**Salida**

Las cuatro corridas, en el orden `4.2 1 1`, `4.2 0 1`, `0.5 1 1` y `4.2 1 2`. Los tres avisos
salen con `Console.Write`, así que la primera línea de cada corrida los trae pegados:

```text
presion en bar: puerta cerrada (1 = si, 0 = no): modo (0 paro, 1 automatico, 2 jog): presion 4.20 bar en rango -> True
puerta cerrada            -> True
modo 1                    -> automatico
arrancar                  -> True

presion en bar: puerta cerrada (1 = si, 0 = no): modo (0 paro, 1 automatico, 2 jog): presion 4.20 bar en rango -> True
puerta cerrada            -> False
modo 1                    -> automatico
arrancar                  -> False
causa: puerta abierta

presion en bar: puerta cerrada (1 = si, 0 = no): modo (0 paro, 1 automatico, 2 jog): presion 0.50 bar en rango -> False
puerta cerrada            -> True
modo 1                    -> automatico
arrancar                  -> False
causa: presion fuera de 3.5 a 5.0 bar

presion en bar: puerta cerrada (1 = si, 0 = no): modo (0 paro, 1 automatico, 2 jog): presion 4.20 bar en rango -> True
puerta cerrada            -> True
modo 2                    -> jog
arrancar                  -> False
causa: la maquina no esta en automatico
```

El `&&` exige las tres condiciones, así que basta con que un enclavamiento falle para que el arranque quede en `False`. Con `||` en su lugar, la fila `4.2 0 1` arrancaría la máquina con la puerta de la guarda abierta, nada más porque la presión es correcta.

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| Las tres capturas se leen con `TryParse` y hay guardia | 2 |
| `presionOk` son dos comparaciones unidas y `arrancar` las tres | 3 |
| La escalera anidada lleva llaves y nombra la primera causa | 2 |
| Las cuatro filas de la tabla de verdad están corridas | 2 |
| Explica qué arrancaría con `||` | 1 |

**Error que más se ve**

Escriben `presion >= 3.5 || presion <= 5.0`, que es cierto para cualquier presión; se delata porque su fila de `0.5` reporta la presión en rango.

## Semana 08 · Tema 4.5 · Repetición · Primer parcial

### 08.1 · Reconocer

**Solución**

```csharp
int[] par = { 22, 24, 25, 19, 24, 31, 23 };

int i = 0, revisadas = 0, saltadas = 0, suma = 0, corte = -1;

while (i < par.Length)
{
    revisadas++;
    if (par[i] > 30) { corte = i; break; }
    if (par[i] < 20) { saltadas++; i++; continue; }
    suma += par[i];
    i++;
}
```

La línea que vuelve falsa la condición es `i++`, y aparece dos veces: al final del cuerpo y también dentro de la rama del `continue`. Si borras la del `continue`, el tornillo de 19 N·m se revisa para siempre y la terminal se queda corriendo hasta que la cortes.

**Salida**

```text
tornillos revisados  6
saltados por flojos  1
suma en tolerancia   95
indice del corte     5
nunca se revisaron   1
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| Los cinco números coinciden con la corrida | 5 |
| Señala `i++` como el cuarto tiempo | 2 |
| Explica que hay dos `i++` y por qué el del `continue` es obligatorio | 3 |

**Error que más se ve**

Contestan 7 en tornillos revisados porque «el arreglo tiene siete»; se delata porque su última línea también dice 0 en los que nunca se revisaron, y las dos cuentas no pueden ser ciertas al mismo tiempo con un `break` de por medio.

### 08.2 · Aplicar

**Solución**

```csharp
int intentos = 0;
double temp;
bool ok;

do
{
    intentos++;
    Console.Write("temperatura del refrigerante en C (10 a 95): ");
    string linea = Console.ReadLine() ?? "";
    bool leido = double.TryParse(linea, out temp);
    ok = leido && temp >= 10.0 && temp <= 95.0;
    if (!ok)
    {
        Console.WriteLine($"  rechazada '{linea}'");
    }
} while (!ok && intentos < 4);

if (ok)
{
    Console.WriteLine($"aceptada {temp:F1} C en {intentos} intentos");
}
else
{
    Console.WriteLine("ENCLAVADO: cuatro capturas invalidas, reposicion manual");
}
```

**Salida**

```text
temperatura del refrigerante en C (10 a 95):   rechazada 'abc'
temperatura del refrigerante en C (10 a 95):   rechazada '120'
temperatura del refrigerante en C (10 a 95):   rechazada '-5'
temperatura del refrigerante en C (10 a 95): aceptada 31.4 C en 4 intentos

temperatura del refrigerante en C (10 a 95):   rechazada 'a'
temperatura del refrigerante en C (10 a 95):   rechazada 'b'
temperatura del refrigerante en C (10 a 95):   rechazada 'c'
temperatura del refrigerante en C (10 a 95):   rechazada 'd'
ENCLAVADO: cuatro capturas invalidas, reposicion manual
```

Va `do-while` porque hay que pedir la muestra antes de poder juzgarla. Con `while` habría que revisar una variable que todavía nadie llenó, y eso obliga a inventar un valor inicial falso que después nadie recuerda por qué está ahí. El cuerpo tiene que correr al menos una vez, y esa es exactamente la garantía que `do-while` da y `while` no.

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| Es `do-while` y el ciclo depende de `ok` | 3 |
| Los dos guardias van en orden: formato primero, rango después | 2 |
| El mensaje de rechazo muestra entre comillas lo que se tecleó | 2 |
| El tope de cuatro intentos corta y enclava | 2 |
| El párrafo justifica `do-while` con la pasada mínima | 1 |

**Error que más se ve**

El `while` final revisa `intentos < 4` y se olvida de `ok`, así que el programa pide cuatro temperaturas aunque la primera sirva; se delata porque su corrida buena tiene cuatro avisos y una sola línea de aceptación al final.

### 08.3 · Integrar

**Solución**

```csharp
const int Minimo = 1480;
const int Maximo = 1520;

int intentos = 0, rpm;
bool ok;
do
{
    intentos++;
    Console.Write($"muestra de cierre en rpm ({Minimo}-{Maximo}): ");
    string linea = Console.ReadLine() ?? "";
    bool leido = int.TryParse(linea, out rpm);
    ok = leido && rpm >= Minimo && rpm <= Maximo;
    if (!ok) Console.WriteLine($"  rechazada '{linea}'");
} while (!ok && intentos < 3);

if (!ok)
{
    Console.WriteLine("ENCLAVADO: tres capturas invalidas");
}
else
{
    Console.WriteLine($"aceptada {rpm} rpm en {intentos} intentos");

    if (rpm < 1490) Console.WriteLine("banda baja");
    else if (rpm < 1510) Console.WriteLine("banda central");
    else Console.WriteLine("banda alta");

    bool puerta = true, paro = true;
    bool armado = puerta && paro && rpm >= Minimo;
    Console.WriteLine($"armado -> {armado}");

    int[] corrida = { 1480, 1502, 1495, 1533, 1471, 1509, 1488 };
    int i = 0, suma = 0, fuera = 0;
    while (i < corrida.Length)
    {
        suma += corrida[i];
        if (corrida[i] < Minimo || corrida[i] > Maximo) fuera++;
        i++;
    }

    Console.WriteLine($"suma        {suma}");
    Console.WriteLine($"media int   {suma / corrida.Length}");
    Console.WriteLine($"media real  {(double)suma / corrida.Length:F3}");
    Console.WriteLine($"fuera       {fuera} de {corrida.Length}");
}
```

**Salida**

```text
muestra de cierre en rpm (1480-1520):   rechazada 'abc'
muestra de cierre en rpm (1480-1520): aceptada 1502 rpm en 2 intentos
banda central
armado -> True
suma        10478
media int   1496
media real  1496.857
fuera       2 de 7
```

La media entera divide dos enteros y tira el residuo. La media real castea la suma a `double` antes de dividir, así que el residuo sobrevive. Sobre estas siete lecturas la diferencia es 0.857 rpm, que sobre un tacómetro no suena a nada y sobre un reporte de tendencia acumulado durante un mes sí.

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| Los límites bajo `const` y la captura defendida con tope | 2 |
| La escalera clasifica en tres bandas excluyentes | 2 |
| El enclavamiento une tres condiciones con `&&` | 2 |
| El `while` acumula suma y cuenta fuera de banda con la regla escrita | 2 |
| Explica la diferencia entre media entera y media real | 2 |

**Error que más se ve**

Declaran `suma` dentro del `while` y el total termina siendo la última lectura; se delata porque su suma imprime 1488 y su media imprime 212.

## Semana 09 · Tema 4.5 · Repetición, profundización

### 09.1 · Reconocer

**Solución**

```csharp
int externas = 0, internas = 0, pares = 0;

for (int a = 0; a < 4; a++)
{
    externas++;
    for (int b = a + 1; b < 4; b++)
    {
        internas++;
        if (b == 3) break;
        pares++;
    }
}
```

El `break` sale del ciclo interno y nada más. El externo da sus cuatro vueltas completas, y por eso el conteo de externas es 4 aunque tres de esas vueltas terminen cortadas por dentro.

**Salida**

```text
pasadas externas 4
pasadas internas 6
pares contados   3
```

Después del ciclo, `Console.WriteLine(a);` no compila: `error CS0103: The name 'a' does not exist in the current context`. La variable de control nace y muere en el encabezado del `for`.

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| Los tres números coinciden con la corrida | 5 |
| Dice que el `break` termina el ciclo interno | 2 |
| Cita `CS0103` para el uso de `a` fuera del ciclo | 3 |

**Error que más se ve**

Contestan 12 en pasadas internas, multiplicando 4 por 3; se delata porque su cuenta ignora que el interno arranca en `a + 1` y que el `break` corta.

### 09.2 · Aplicar

**Solución**

```csharp
int[] rpm = { 1480, 1502, 1495, 1533, 1471, 1509, 1488 };

int suma = 0, fuera = 0;
int maxIdx = 0, minIdx = 0;

for (int i = 0; i < rpm.Length; i++)
{
    suma += rpm[i];
    if (rpm[i] < 1480 || rpm[i] > 1520) fuera++;
    if (rpm[i] > rpm[maxIdx]) maxIdx = i;
    if (rpm[i] < rpm[minIdx]) minIdx = i;
}

int cuenta = 0;
int sumaForeach = 0;
foreach (int lectura in rpm)
{
    sumaForeach += lectura;
    cuenta++;
}

Console.WriteLine($"lecturas    {cuenta}");
Console.WriteLine($"suma        {suma}  (foreach {sumaForeach})");
Console.WriteLine($"media int   {suma / rpm.Length}");
Console.WriteLine($"media real  {(double)suma / rpm.Length}");
Console.WriteLine($"media a F3  {(double)suma / rpm.Length:F3}");
Console.WriteLine($"fuera       {fuera} de {rpm.Length}");
Console.WriteLine($"maximo      {rpm[maxIdx]} en el indice {maxIdx}");
Console.WriteLine($"minimo      {rpm[minIdx]} en el indice {minIdx}");
Console.WriteLine($"rango       {rpm[maxIdx] - rpm[minIdx]}");
```

**Salida**

```text
lecturas    7
suma        10478  (foreach 10478)
media int   1496
media real  1496.857142857143
media a F3  1496.857
fuera       2 de 7
maximo      1533 en el indice 3
minimo      1471 en el indice 4
rango       62
```

Los índices del máximo y del mínimo no se pueden llevar con `foreach`, porque ese ciclo entrega el valor y no la posición. En cuanto la pregunta pasa de cuál es el máximo a dónde está el máximo, hay que volver al `for`. Y el índice es justo lo que le sirve al técnico para saber qué muestra ir a revisar.

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| Los cuatro acumuladores se declaran antes del ciclo | 3 |
| Un solo `for` los llena todos | 2 |
| El `foreach` reproduce suma y conteo | 2 |
| Los nueve renglones salen con los valores medidos | 2 |
| Identifica el acumulador que exige índice y lo explica | 1 |

**Error que más se ve**

Arrancan `minIdx` en el índice del último elemento «para que empiece grande»; se delata porque su mínimo imprime 1488 en lugar de 1471 y su rango sale en 45.

### 09.3 · Integrar

**Solución**

```csharp
int[] rpm = { 1480, 1502, 1495, 1533, 1471, 1509, 1488 };

int fuera = 0;
for (int i = 0; i < rpm.Length; i++)
    if (rpm[i] < 1480 || rpm[i] > 1520) fuera++;

Console.WriteLine($"fuera            {fuera} de {rpm.Length}");
Console.WriteLine($"pct entero       {fuera * 100 / rpm.Length}");
Console.WriteLine($"pct real         {fuera * 100.0 / rpm.Length}");
Console.WriteLine($"pct a F1         {fuera * 100.0 / rpm.Length:F1}");

int malla = 0, triangular = 0;
for (int a = 0; a < rpm.Length; a++)
{
    for (int b = 0; b < rpm.Length; b++) malla++;
    for (int b = a + 1; b < rpm.Length; b++) triangular++;
}
Console.WriteLine($"malla completa   {malla}");
Console.WriteLine($"pares distintos  {triangular}");

int ciclos = int.MaxValue - 2;
for (int k = 0; k < 3; k++)
{
    ciclos++;
    Console.WriteLine($"+1 ciclo en int  {ciclos}");
}
long ciclosL = int.MaxValue - 2;
for (int k = 0; k < 3; k++) ciclosL++;
Console.WriteLine($"el mismo en long {ciclosL}");
Console.WriteLine($"a 25 ciclos/s    {int.MaxValue / 25.0 / 3600.0 / 24.0:F1} dias");
```

**Salida**

```text
fuera            2 de 7
pct entero       28
pct real         28.571428571428573
pct a F1         28.6
malla completa   49
pares distintos  21
+1 ciclo en int  2147483646
+1 ciclo en int  2147483647
+1 ciclo en int  -2147483648
el mismo en long 2147483648
a 25 ciclos/s    994.2 dias
```

Al jefe de mantenimiento se le reporta 28.6, porque el 28 se comió medio punto sin avisar y el número de diecisiete dígitos no lo va a leer nadie. La mañana en que el contador se dio la vuelta, el sistema reportó menos dos mil ciento cuarenta y siete millones de ciclos, un número que a nadie le suena a error de tipo y que sí parece un sensor descompuesto. Se detecta sin cambiar el tipo comparando el valor nuevo contra el anterior: si el contador bajó cuando nadie lo reinició, se dio la vuelta.

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| Los cuatro porcentajes están y elige el que se reporta | 3 |
| Los dos conteos de pares están y no coinciden | 2 |
| El contador `int` se ve pasar a negativo, y el `long` no | 3 |
| Los días de corrida continua salen con un decimal | 1 |
| Da una forma de detectar la vuelta sin cambiar el tipo | 1 |

**Error que más se ve**

Esperan una excepción en el desbordamiento; se delata porque su reporte dice «aquí truena» y la corrida que pegan sigue imprimiendo renglones después del número negativo.

## Semana 10 · Tema 5.1 · Funciones definidas por el usuario

### 10.1 · Reconocer

**Solución**

| Archivo | Compila | Qué contesta | Qué imprime |
|---|---|---|---|
| A | sí | `warning CS8321: The local function 'ImprimirEncabezado' is declared but never used` | nada |
| B | no | `error CS0029: Cannot implicitly convert type 'void' to 'double'` | nada |
| C | no | `error CS8421: A static local function cannot contain a reference to 'limiteC'` | nada |

El archivo A compila, corre y sale con 0 sin imprimir una sola línea, porque declarar un método no lo ejecuta. El compilador lo avisa con `CS8321`, que es una advertencia y no un error.

En el archivo C hay que quitar `static`. Al quitarla el método puede leer `limiteC` y compila, pero se pierde el aislamiento: ya no se puede probar la pieza sola, porque su resultado depende de una variable que el llamador no le pasó.

**Salida**

```text
A  Build succeeded con 1 advertencia, dotnet run no imprime nada, exit 0
B  Program.cs(1,12): error CS0029: Cannot implicitly convert type 'void' to 'double'
C  Program.cs(6,22): error CS8421: A static local function cannot contain a reference to 'limiteC'.
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| Los tres desenlaces están bien clasificados | 4 |
| Cita `CS8321` y explica que A no imprime nada | 2 |
| Cita `CS0029` y distingue devolver de imprimir | 2 |
| Dice qué se pierde al quitar `static` en C | 2 |

**Error que más se ve**

Dicen que A no compila porque «falta llamarlo»; se delata porque no pegan el `Build succeeded` que su propia máquina imprimió.

### 10.2 · Aplicar

**Solución**

```csharp
int[] rpm = { 1480, 1502, 1495, 1533, 1471, 1509, 1488 };

Console.WriteLine($"suma       {Suma(rpm)}");
Console.WriteLine($"media      {Media(rpm):F3}");
Console.WriteLine($"fuera      {FueraDeBanda(rpm, 1480, 1520)} de {rpm.Length}");
int idx = IndiceDelMaximo(rpm);
Console.WriteLine($"maximo     {rpm[idx]} en el indice {idx}");

static int Suma(int[] v)
{
    int total = 0;
    foreach (int x in v) total += x;
    return total;
}

static double Media(int[] v)
{
    return (double)Suma(v) / v.Length;
}

static int FueraDeBanda(int[] v, int lo, int hi)
{
    int cuenta = 0;
    foreach (int x in v)
        if (x < lo || x > hi) cuenta++;
    return cuenta;
}

static int IndiceDelMaximo(int[] v)
{
    int idx = 0;
    for (int i = 1; i < v.Length; i++)
        if (v[i] > v[idx]) idx = i;
    return idx;
}
```

**Salida**

```text
suma       10478
media      1496.857
fuera      2 de 7
maximo     1533 en el indice 3
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| Los cuatro métodos existen, con `static` y su firma completa | 3 |
| Ninguno imprime por su cuenta, todos devuelven | 3 |
| `Media` se apoya en `Suma` y castea antes de dividir | 2 |
| Los límites entran como parámetros, no escritos adentro | 2 |

**Error que más se ve**

`Media` devuelve `int` y el resultado sale en 1496; se delata porque el `:F3` de la impresión muestra 1496.000, que es un promedio sin residuo sobre siete números que no se dividen exacto.

### 10.3 · Integrar

**Solución**

```csharp
int[] rpm = { 1480, 1502, 1495, 1533, 1471, 1509, 1488 };

PonerACero(rpm);
Console.WriteLine($"tras PonerACero    rpm[0] = {rpm[0]}");

Reemplazar(rpm);
Console.WriteLine($"tras Reemplazar    rpm[0] = {rpm[0]}");

ReemplazarRef(ref rpm);
Console.WriteLine($"tras ReemplazarRef rpm[0] = {rpm[0]}");

int[] original = { 1480, 1502, 1495, 1533, 1471, 1509, 1488 };
int[] ventana = Ventana(original, 2, 3);
ventana[0] = 0;
Console.WriteLine($"ventana recortada  {ventana[0]} {ventana[1]} {ventana[2]}");
Console.WriteLine($"original intacto   original[2] = {original[2]}");

Console.WriteLine($"media de 2         {Media(1480, 1502):F3}");
Console.WriteLine($"media de 7         {Media(original):F3}");
Console.WriteLine($"media de ninguna   {Media()}");

static void PonerACero(int[] v) { v[0] = 0; }

static void Reemplazar(int[] v) { v = new int[] { -1, -1, -1 }; }

static void ReemplazarRef(ref int[] v) { v = new int[] { -1, -1, -1 }; }

static int[] Ventana(int[] v, int inicio, int cuenta)
{
    int[] w = new int[cuenta];
    for (int i = 0; i < cuenta; i++) w[i] = v[inicio + i];
    return w;
}

static double Media(params int[] muestras)
{
    if (muestras.Length == 0) return double.NaN;
    int total = 0;
    foreach (int m in muestras) total += m;
    return (double)total / muestras.Length;
}
```

**Salida**

```text
tras PonerACero    rpm[0] = 0
tras Reemplazar    rpm[0] = 0
tras ReemplazarRef rpm[0] = -1
ventana recortada  0 1533 1471
original intacto   original[2] = 1495
media de 2         1491.000
media de 7         1496.857
media de ninguna   NaN
```

El punto 1 le llega al llamador porque la variable del parámetro es una copia de la referencia, y esa copia apunta al mismo arreglo. El punto 2 no le llega porque asignar un arreglo nuevo cambia la copia de la referencia, no la del llamador. La palabra que cambia el desenlace del punto 3 es `ref`, que entrega la variable misma en lugar de una copia de ella.

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| Los tres primeros métodos existen y se ve la diferencia | 3 |
| `Ventana` devuelve un arreglo nuevo y el original no se toca | 2 |
| `Media` con `params` atiende dos, siete y ninguna muestra | 2 |
| Devuelve `NaN` con cero muestras en lugar de tronar | 1 |
| Los tres renglones de explicación distinguen elemento de reemplazo | 2 |

**Error que más se ve**

Escriben `Ventana` copiando la referencia en vez de crear un arreglo nuevo, y entonces escribir en la ventana cambia el original; se delata porque su renglón de original intacto imprime 0 en lugar de 1495.

## Semana 11 · Tema 5.3 · Paso de parámetros por referencia

### 11.1 · Reconocer

**Solución**

Los dos cuerpos son idénticos y hacen lo correcto. Lo que cambia es sobre qué trabajan: el primero sobre copias que se destruyen al salir, el segundo sobre las variables del llamador.

**Salida**

```text
por valor      1, 2
por referencia 2, 1
TryParse       False, guardado = 0
```

Si quitas los dos `ref` del sitio de llamada y dejas la firma como está, el compilador contesta `error CS1620: Argument 1 must be passed with the 'ref' keyword` y otro igual para el argumento 2. La palabra va en los dos lados o no va en ninguno.

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| Los tres renglones predichos coinciden | 5 |
| Explica que el cuerpo del primero está bien escrito | 2 |
| Cita `CS1620` para la llamada sin la palabra | 3 |

**Error que más se ve**

Predicen `guardado = 999` porque «si falló, no la tocó»; se delata porque el mismo alumno escribe que `TryParse` devuelve `False`, y esa falla es justamente cuando la sobrescribe con 0.

### 11.2 · Aplicar

**Solución**

```csharp
double[] termopares = { 21.0, 39.5, 22.4 };

MinMax(termopares, out double frio, out double caliente);
Console.WriteLine($"minimo {frio:F1} C   maximo {caliente:F1} C");

double tanque = 40.0;

Llenar(ref tanque, 15.0);
Console.WriteLine($"tanque {tanque:F1} L");

Llenar(ref tanque, 10.0);
Console.WriteLine($"tanque {tanque:F1} L");

Vaciar(ref tanque, 20.0);
Console.WriteLine($"tanque {tanque:F1} L");

Vaciar(ref tanque, 40.0);
Console.WriteLine($"tanque {tanque:F1} L");

static void MinMax(double[] v, out double lo, out double hi)
{
    lo = v[0];
    hi = v[0];
    foreach (double x in v)
    {
        if (x < lo) lo = x;
        if (x > hi) hi = x;
    }
}

static void Llenar(ref double litros, double agrega)
{
    if (litros + agrega > 60.0)
    {
        Console.WriteLine($"  rechazado: {litros + agrega:F1} L pasa el tope de 60.0 L");
        return;
    }
    litros += agrega;
}

static void Vaciar(ref double litros, double saca)
{
    if (litros - saca < 5.0)
    {
        Console.WriteLine($"  rechazado: dejaria {litros - saca:F1} L y el minimo es 5.0 L");
        return;
    }
    litros -= saca;
}
```

**Salida**

```text
minimo 21.0 C   maximo 39.5 C
tanque 55.0 L
  rechazado: 65.0 L pasa el tope de 60.0 L
tanque 55.0 L
tanque 35.0 L
  rechazado: dejaria -5.0 L y el minimo es 5.0 L
tanque 35.0 L
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| Los dos `out` se llenan en todos los caminos de `MinMax` | 3 |
| `Llenar` y `Vaciar` reciben el nivel por `ref` | 2 |
| Las dos guardas rechazan y el mensaje dice el número que habría quedado | 3 |
| Las cuatro operaciones encadenadas están corridas | 2 |

**Error que más se ve**

`Vaciar` resta primero y revisa después, y el tanque queda en menos cinco litros; se delata porque el mensaje de rechazo aparece y el nivel de la línea siguiente ya bajó.

### 11.3 · Integrar

**Solución**

```csharp
double[] banco = { 21.0, 39.5, 22.4 };
double[] alias = banco;

alias[0] = 99.9;
Console.WriteLine($"banco[0] tras tocar el alias  {banco[0]}");
Console.WriteLine($"son el mismo arreglo          {ReferenceEquals(banco, alias)}");

banco[0] = 21.0;

int intentos = 0;
double ajuste;
bool ok;
do
{
    intentos++;
    Console.Write("ajuste de calibracion en C (-5 a 5): ");
    string linea = Console.ReadLine() ?? "";
    bool leido = double.TryParse(linea, out ajuste);
    ok = leido && ajuste >= -5.0 && ajuste <= 5.0;
    if (!ok) Console.WriteLine($"  rechazado '{linea}'");
} while (!ok && intentos < 3);

if (!ok)
{
    Console.WriteLine("calibracion cancelada, el banco queda sin tocar");
}
else
{
    Aplicar(ref banco[1], ajuste);
    Recortar(ref banco[1], 30.0);

    MinMax(banco, out double frio, out double caliente);

    Console.WriteLine($"canal 1 tras calibrar  {banco[1]:F1} C");
    Console.WriteLine($"minimo {frio:F1} C   maximo {caliente:F1} C");
}

static void Aplicar(ref double lectura, double ajuste)
{
    lectura += ajuste;
}

static void Recortar(ref double lectura, double limite)
{
    if (lectura > limite)
    {
        Console.WriteLine($"  recortada de {lectura:F1} a {limite:F1} C");
        lectura = limite;
    }
}

static void MinMax(double[] v, out double lo, out double hi)
{
    lo = v[0];
    hi = v[0];
    foreach (double x in v)
    {
        if (x < lo) lo = x;
        if (x > hi) hi = x;
    }
}
```

**Salida**

Con las entradas `abc` y `-2.5`:

```text
banco[0] tras tocar el alias  99.9
son el mismo arreglo          True
ajuste de calibracion en C (-5 a 5):   rechazado 'abc'
ajuste de calibracion en C (-5 a 5):   recortada de 37.0 a 30.0 C
canal 1 tras calibrar  30.0 C
minimo 21.0 C   maximo 30.0 C
```

El arreglo del punto 1 se comparte porque la variable no lleva los tres números, lleva una referencia a ellos, y asignarla copia la referencia. El punto 3 sí necesita `ref` porque `banco[1]` es un `double`, un valor suelto, y sin la palabra el método recibiría una copia del número y la calibración se quedaría adentro.

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| El alias queda demostrado con `ReferenceEquals` | 2 |
| El `do-while` valida el ajuste y deja el banco sin tocar al fallar | 3 |
| `Aplicar` y `Recortar` reciben el elemento del arreglo por `ref` | 3 |
| `MinMax` reporta con dos `out` después de calibrar | 1 |
| Explica por qué uno comparte sin la palabra y el otro la necesita | 1 |

**Error que más se ve**

Pasan `banco[1]` sin `ref` y la calibración no aparece; se delata porque su renglón final imprime 39.5 y el mensaje de recorte nunca sale.

## Semana 12 · Tema 5.4 · Funciones predefinidas

### 12.1 · Reconocer

**Solución**

`NaN` es el único valor del lenguaje que no es igual a sí mismo, por eso la comparación con doble igual contesta `False` y la única forma de preguntarlo es `double.IsNaN`. El seno de pi no da cero porque `Math.PI` es una aproximación de pi con diecisiete dígitos, y el seno de ese número aproximado es un número muy pequeño, no cero.

**Salida**

```text
Program.cs(4,45): warning CS1718: Comparison made to same variable; did you mean to compare something else?

Math.Sqrt(-1)          NaN
nan == nan             False
double.IsNaN(nan)      True
Math.Sin(Math.PI)      1.2246467991473532E-16
|sin(pi)| < 1e-9       True
Math.Round(2.5)        2
Round(2.5) lejos de 0  3
1.0 / 0                ∞
Math.Clamp(39.5,0,30)  30
Math.Pow(2, 10)        1024
```

La advertencia sale de la línea 4, la que compara `nan` contra sí mismo. `int capacidad = Math.Pow(2, 10);` devuelve `error CS0266: Cannot implicitly convert type 'double' to 'int'`, porque la firma de `Math.Pow` promete un `double` aunque el resultado se vea entero. `Math.Sqrt("9")` devuelve `error CS1503: Argument 1: cannot convert from 'string' to 'double'`.

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| Los diez renglones predichos coinciden | 4 |
| Ubica la advertencia `CS1718` en la línea correcta | 2 |
| Explica por qué `nan == nan` es `False` | 2 |
| Cita `CS0266` para `Math.Pow` y `CS1503` para `Math.Sqrt` con texto | 2 |

**Error que más se ve**

Predicen 0 en el seno de pi; se delata porque en la línea siguiente aceptan que la comparación por tolerancia contesta `True`, y las dos cosas no pueden ser ciertas a la vez si el valor fuera cero exacto.

### 12.2 · Aplicar

**Solución**

```csharp
double[] v = { 0.42, -0.31, 0.55, -0.48, 0.12, -0.27, 0.61 };

double sumaCuadrados = 0;
double pico = 0;
foreach (double x in v)
{
    sumaCuadrados += Math.Pow(x, 2);
    pico = Math.Max(pico, Math.Abs(x));
}

double rms = Math.Sqrt(sumaCuadrados / v.Length);
double cresta = pico / rms;
double alarma = Math.Clamp(rms, 0.0, 0.4500);

Console.WriteLine($"RMS crudo      {rms}");
Console.WriteLine($"RMS a F4       {rms:F4} mm/s");
Console.WriteLine($"pico           {pico:F4} mm/s");
Console.WriteLine($"factor cresta  {cresta:F4}");
Console.WriteLine($"RMS recortado  {alarma:F4} mm/s");
Console.WriteLine($"sobre 0.4500   {rms > 0.4500}");
```

**Salida**

```text
RMS crudo      0.42507142257003616
RMS a F4       0.4251 mm/s
pico           0.6100 mm/s
factor cresta  1.4351
RMS recortado  0.4251 mm/s
sobre 0.4500   False
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| La suma de cuadrados y la raíz están bien encadenadas | 3 |
| El pico usa `Math.Abs` y `Math.Max`, no un `if` escrito a mano | 2 |
| El recorte usa `Math.Clamp` con sus tres argumentos | 2 |
| El RMS se imprime crudo y con cuatro decimales | 2 |
| El factor de cresta sale del pico entre el RMS | 1 |

**Error que más se ve**

Suman los valores absolutos en lugar de los cuadrados y llaman RMS al resultado; se delata porque su número da 0.3943 y el factor de cresta les sale por debajo de 1, que es imposible.

### 12.3 · Integrar

**Solución**

```csharp
const int Semilla = 2026;

Random r = new Random(Semilla);

int[] sim = new int[20];
for (int i = 0; i < sim.Length; i++)
    sim[i] = r.Next(1400, 1601);

int suma = 0, fuera = 0, maxIdx = 0;
for (int i = 0; i < sim.Length; i++)
{
    suma += sim[i];
    if (sim[i] < 1480 || sim[i] > 1520) fuera++;
    if (sim[i] > sim[maxIdx]) maxIdx = i;
}

Console.WriteLine($"semilla        {Semilla}");
Console.WriteLine($"primeras cinco {sim[0]} {sim[1]} {sim[2]} {sim[3]} {sim[4]}");
Console.WriteLine($"suma           {suma}");
Console.WriteLine($"media          {(double)suma / sim.Length:F3} rpm");
Console.WriteLine($"fuera de banda {fuera} de {sim.Length}");
Console.WriteLine($"pico           {sim[maxIdx]} rpm en el indice {maxIdx}");

int palabra = 0;
if (fuera > 0) palabra += 1;
if (sim[maxIdx] > 1520) palabra += 2;
if (suma / sim.Length > 1500) palabra += 4;

Console.WriteLine($"palabra estado {palabra} = {Convert.ToString(palabra, 2)} en binario");
Console.WriteLine($"en hexadecimal {Convert.ToString(palabra, 16)}");
```

**Salida**

Las dos corridas seguidas dan exactamente lo mismo:

```text
semilla        2026
primeras cinco 1432 1456 1584 1599 1584
suma           30052
media          1502.600 rpm
fuera de banda 16 de 20
pico           1599 rpm en el indice 3
palabra estado 7 = 111 en binario
en hexadecimal 7
```

Con el generador construido dentro del ciclo, las veinte muestras serían el mismo número repetido veinte veces. Una semilla es el punto de partida de una secuencia, así que resembrar en cada pasada vuelve a leer su primer valor.

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| La semilla está bajo `const` y aparece en la salida | 2 |
| El generador se construye una sola vez, fuera del ciclo | 3 |
| Los acumuladores reproducen suma, media, fuera de banda y pico | 2 |
| La palabra de estado sale en decimal, binario y hexadecimal | 2 |
| Las dos corridas pegadas son idénticas | 1 |

**Error que más se ve**

Escriben `new Random(Semilla)` dentro del `for`; se delata porque sus veinte muestras son el mismo número y su conteo de fuera de banda es 0 o 20, nunca algo intermedio.

## Semana 13 · Tema 6.1 · Arreglos y cadenas · Segundo parcial

### 13.1 · Reconocer

**Solución**

Asignar un arreglo crea un segundo nombre para el mismo arreglo. `Clone` sí produce uno independiente. Una cadena no se puede editar, así que `ToUpper` y `Trim` devuelven otra cadena y dejan la tuya quieta.

**Salida**

```text
src[0] 99   src[1] 1502
alias es el mismo True
copia es el mismo False
tag        sensor-07
ToUpper()  SENSOR-07
tag.Length 9
vacia dentro True
campos de la vacia 1
Substring(9) []
```

`tag.Substring(10)` lanza `ArgumentOutOfRangeException`, mientras que `tag.Substring(9)` sobre una cadena de largo 9 devuelve la cadena vacía sin quejarse. `tag[9]` lanza `IndexOutOfRangeException` con el mensaje `Index was outside the bounds of the array`. Dos llamadas de la misma biblioteca, dos fronteras distintas.

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| Los nueve renglones predichos coinciden | 4 |
| Distingue alias de copia con los dos `ReferenceEquals` | 2 |
| Explica que `tag.ToUpper();` en su propia línea no hace nada | 2 |
| Reporta las dos excepciones de frontera y su diferencia | 2 |

**Error que más se ve**

Predicen `SENSOR-07` en el renglón de `tag`; se delata porque escriben la línea `tag.ToUpper();` como si guardara el resultado en algún lado.

### 13.2 · Aplicar

**Solución**

```csharp
using System.Globalization;

string linea = "  EST-07:1480.0,1502.5,1495.0,1533.5  ";

string[] partes = linea.Trim().Split(':');
string etiqueta = partes[0];
string[] campos = partes[1].Split(',');

double[] lecturas = new double[campos.Length];
for (int i = 0; i < campos.Length; i++)
    lecturas[i] = double.Parse(campos[i], CultureInfo.InvariantCulture);

double suma = 0;
foreach (double x in lecturas) suma += x;

Console.WriteLine($"etiqueta   {etiqueta}");
Console.WriteLine($"campos     {campos.Length}");
Console.WriteLine($"media      {suma / lecturas.Length:F3} rpm");
Console.WriteLine($"primera    {lecturas[0]:F1}   ultima {lecturas[lecturas.Length - 1]:F1}");

string[] pruebas = { "SNS-4471-A", "  SNS-4471-A  ", "sns-4471-b", "SNS-44X1-A", "" };
foreach (string p in pruebas)
    Console.WriteLine($"[{p}] -> {IdValido(p)}");

static bool IdValido(string crudo)
{
    string id = crudo.Trim();
    if (id.Length != 10) return false;

    StringComparison ci = StringComparison.OrdinalIgnoreCase;
    if (!id.StartsWith("SNS-", ci)) return false;
    if (!id.EndsWith("-A", ci) && !id.EndsWith("-B", ci)) return false;

    for (int i = 4; i < 8; i++)
        if (!char.IsDigit(id[i])) return false;

    return true;
}
```

**Salida**

```text
etiqueta   EST-07
campos     4
media      1502.750 rpm
primera    1480.0   ultima 1533.5
[SNS-4471-A] -> True
[  SNS-4471-A  ] -> True
[sns-4471-b] -> True
[SNS-44X1-A] -> False
[] -> False
```

La tercera entrada es la que separa un validador con una política de uno con dos. Si el sufijo se compara sin `OrdinalIgnoreCase` y el prefijo sí, `sns-4471-b` devuelve `False` y el defecto vive a dos líneas de distancia de su propia contradicción.

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| `Trim` antes de `Split`, y los dos cortes en el orden correcto | 2 |
| La cultura se fija en la conversión, no se deja a la máquina | 3 |
| El validador revisa largo, prefijo, sufijo y dígitos | 3 |
| Una sola política de comparación en las dos revisiones de texto | 2 |

**Error que más se ve**

Convierten con `double.Parse` sin cultura y el archivo corre bien en el salón; se delata cuando el revisor lo corre en una máquina configurada en alemán y la media salta a seis cifras.

### 13.3 · Integrar

**Solución**

```csharp
string captura = "1480,1502,1495,abc,1533,1471,1509,1488";

string[] campos = captura.Split(',');
int[] rpm = new int[campos.Length];
int n = 0, rechazadas = 0;

foreach (string campo in campos)
{
    bool ok = int.TryParse(campo.Trim(), out int valor);
    if (ok) { rpm[n] = valor; n++; }
    else { rechazadas++; }
}

int[] validas = new int[n];
for (int i = 0; i < n; i++) validas[i] = rpm[i];

Console.WriteLine($"campos     {campos.Length}");
Console.WriteLine($"leidas     {n}");
Console.WriteLine($"rechazadas {rechazadas}");
Console.WriteLine($"suma       {Suma(validas)}");
Console.WriteLine($"media int  {Suma(validas) / validas.Length}");
Console.WriteLine($"media real {Media(validas):F3}");
Console.WriteLine($"fuera      {FueraDeBanda(validas, 1480, 1520)} de {validas.Length}");

int[] ordenadas = (int[])validas.Clone();
Array.Sort(ordenadas);

Console.WriteLine($"mediana    {ordenadas[ordenadas.Length / 2]}");
Console.WriteLine($"original intacto: validas[0] = {validas[0]}");

Console.WriteLine();
Console.WriteLine("canal    rpm  estado");
for (int i = 0; i < validas.Length; i++)
{
    string estado = "ok";
    if (validas[i] < 1480 || validas[i] > 1520) estado = "fuera";
    Console.WriteLine($"{i,-5}{validas[i],7}  {estado}");
}

static int Suma(int[] v)
{
    int total = 0;
    foreach (int x in v) total += x;
    return total;
}

static double Media(int[] v) => (double)Suma(v) / v.Length;

static int FueraDeBanda(int[] v, int lo, int hi)
{
    int c = 0;
    foreach (int x in v) if (x < lo || x > hi) c++;
    return c;
}
```

**Salida**

```text
campos     8
leidas     7
rechazadas 1
suma       10478
media int  1496
media real 1496.857
fuera      2 de 7
mediana    1495
original intacto: validas[0] = 1480

canal    rpm  estado
0       1480  ok
1       1502  ok
2       1495  ok
3       1533  fuera
4       1471  fuera
5       1509  ok
6       1488  ok
```

Con `Convert.ToInt32` en lugar de `TryParse`, el programa muere en el cuarto campo con `FormatException` y no llega a imprimir un solo renglón del reporte. El caso peor no es ese: `Convert.ToInt32` sobre `null` devuelve 0 en silencio, y ese cero entra al banco como una lectura que nadie tomó.

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| El parseo defendido cuenta buenas y malas por separado | 2 |
| Los tres métodos existen, con `static` y sin imprimir adentro | 3 |
| `Clone` y `Array.Sort` dejan el original intacto y se comprueba | 2 |
| El reporte sale alineado en tres columnas | 2 |
| Explica qué pasaría con `Convert.ToInt32` | 1 |

**Error que más se ve**

Calculan la media sobre el arreglo de ocho lugares en vez de sobre las siete lecturas buenas, y el promedio les baja a 1309; se delata porque su renglón de leídas dice 7 y su divisor es 8.

## Semana 14 · Tema 6.2–6.3 · Rejillas, ordenación y búsqueda

### 14.1 · Reconocer

**Solución**

Sobre entrada sin ordenar la búsqueda binaria no falla, contesta mal y sigue corriendo. Los cinco valores están en el arreglo y solo dos regresan con su posición verdadera.

**Salida**

```text
busca 1533 -> 2
busca 1502 -> 0
busca 1471 -> -1
busca 1495 -> -1
busca 1500 -> -5
punto de insercion -> 4
```

Las que devuelven el mismo número son `1471` y `1495`: las dos regresan menos uno aunque una viva en el índice 1 y la otra en el 4. De las cuatro contestaron bien dos, 1533 y 1502, y por suerte. No se lanzó ninguna excepción para ninguna de las cuatro. La precondición que hay que escribir junto a cualquier llamada es que el arreglo tenga que estar ordenado, porque el algoritmo no la revisa.

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| Los seis renglones predichos coinciden | 4 |
| Señala las dos búsquedas que devuelven el mismo número | 2 |
| Dice que no hubo excepción en ningún caso | 2 |
| Enuncia la precondición del arreglo ordenado | 2 |

**Error que más se ve**

Esperan una excepción por recibir un arreglo sin ordenar; se delata porque su predicción no tiene números para las cuatro primeras líneas, solo la palabra error.

### 14.2 · Aplicar

**Solución**

```csharp
double[,] desv = {
    { -0.012,  0.004,  0.021, -0.003 },
    {  0.008, -0.031,  0.015,  0.002 },
    { -0.005,  0.011, -0.047,  0.009 }
};

int filas = desv.GetLength(0);
int cols = desv.GetLength(1);

Console.WriteLine($"posiciones {filas}   puntos {cols}   celdas {desv.Length}");
Console.WriteLine($"Rank {desv.Rank}");
Console.WriteLine();

for (int f = 0; f < filas; f++)
{
    double suma = 0;
    for (int c = 0; c < cols; c++) suma += desv[f, c];
    Console.WriteLine($"posicion {f}  promedio {suma / cols,9:F4} mm");
}

Console.WriteLine();

for (int c = 0; c < cols; c++)
{
    double suma = 0;
    for (int f = 0; f < filas; f++) suma += desv[f, c];
    Console.WriteLine($"punto    {c}  promedio {suma / filas,9:F4} mm");
}

int peorF = 0, peorC = 0;
for (int f = 0; f < filas; f++)
    for (int c = 0; c < cols; c++)
        if (Math.Abs(desv[f, c]) > Math.Abs(desv[peorF, peorC]))
        {
            peorF = f;
            peorC = c;
        }

Console.WriteLine();
Console.WriteLine($"peor celda [{peorF},{peorC}] con {desv[peorF, peorC]:F4} mm");
Console.WriteLine($"fuera de +-0.030 mm -> {Math.Abs(desv[peorF, peorC]) > 0.030}");
```

**Salida**

```text
posiciones 3   puntos 4   celdas 12
Rank 2

posicion 0  promedio    0.0025 mm
posicion 1  promedio   -0.0015 mm
posicion 2  promedio   -0.0080 mm

punto    0  promedio   -0.0030 mm
punto    1  promedio   -0.0053 mm
punto    2  promedio   -0.0037 mm
punto    3  promedio    0.0027 mm

peor celda [2,2] con -0.0470 mm
fuera de +-0.030 mm -> True
```

Al agregar una quinta columna a la rejilla el programa sigue corriendo sin tocar un solo ciclo, porque los dos límites salen de `GetLength` y no de un número escrito a mano.

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| La rejilla se declara con dos índices y se reportan `Length` y `Rank` | 2 |
| Los promedios por posición y por punto están y son correctos | 3 |
| La peor celda se elige por valor absoluto y reporta sus dos índices | 3 |
| Los límites salen de `GetLength` y la prueba de la columna extra pasa | 2 |

**Error que más se ve**

Eligen la peor celda por el valor con signo y reportan la de más 0.021 en lugar de la de menos 0.047; se delata porque su celda «peor» no rebasa la tolerancia y su propio renglón siguiente dice que sí.

### 14.3 · Integrar

**Solución**

```csharp
int[] corrida = { 1480, 1502, 1495, 1533, 1471, 1509, 1488 };
int[] ordenada = { 1471, 1480, 1488, 1495, 1502, 1509, 1533 };
int[] invertida = { 1533, 1509, 1502, 1495, 1488, 1480, 1471 };

Console.WriteLine("entrada      burbuja cmp/mov   insercion cmp/mov");
Reportar("corrida  ", corrida);
Reportar("ordenada ", ordenada);
Reportar("invertida", invertida);

Console.WriteLine();
int[] destino = (int[])corrida.Clone();
Array.Sort(destino);
Console.WriteLine($"secuencial 1533 -> {Secuencial(destino, 1533)} comparaciones");
Console.WriteLine($"binaria    1533 -> {Binaria(destino, 1533)} comparaciones");
Console.WriteLine($"secuencial 1471 -> {Secuencial(destino, 1471)} comparaciones");
Console.WriteLine($"binaria    1471 -> {Binaria(destino, 1471)} comparaciones");

static void Reportar(string nombre, int[] fuente)
{
    int[] a = (int[])fuente.Clone();
    int[] b = (int[])fuente.Clone();
    Burbuja(a, out int bc, out int bm);
    Insercion(b, out int ic, out int im);
    Console.WriteLine($"{nombre}        {bc,3} / {bm,-3}          {ic,3} / {im}");
}

static void Burbuja(int[] a, out int cmp, out int mov)
{
    cmp = 0;
    mov = 0;
    for (int i = 0; i < a.Length - 1; i++)
    {
        bool hubo = false;
        for (int j = 0; j < a.Length - 1 - i; j++)
        {
            cmp++;
            if (a[j] > a[j + 1])
            {
                int t = a[j];
                a[j] = a[j + 1];
                a[j + 1] = t;
                mov++;
                hubo = true;
            }
        }
        if (!hubo) break;
    }
}

static void Insercion(int[] a, out int cmp, out int mov)
{
    cmp = 0;
    mov = 0;
    for (int i = 1; i < a.Length; i++)
    {
        int clave = a[i], j = i;
        while (j >= 1)
        {
            cmp++;
            if (a[j - 1] <= clave) break;
            a[j] = a[j - 1];
            j--;
            mov++;
        }
        a[j] = clave;
    }
}

static int Secuencial(int[] a, int clave)
{
    int c = 0;
    for (int i = 0; i < a.Length; i++)
    {
        c++;
        if (a[i] == clave) return c;
    }
    return c;
}

static int Binaria(int[] a, int clave)
{
    int lo = 0, hi = a.Length - 1, c = 0;
    while (lo <= hi)
    {
        c++;
        int mid = lo + (hi - lo) / 2;
        if (a[mid] == clave) return c;
        if (a[mid] < clave) lo = mid + 1; else hi = mid - 1;
    }
    return c;
}
```

**Salida**

```text
entrada      burbuja cmp/mov   insercion cmp/mov
corrida           20 / 10            15 / 10
ordenada           6 / 0              6 / 0
invertida         21 / 21            21 / 21

secuencial 1533 -> 7 comparaciones
binaria    1533 -> 3 comparaciones
secuencial 1471 -> 1 comparaciones
binaria    1471 -> 3 comparaciones
```

A los dos les conviene la entrada ya ordenada, donde la bandera de burbuja y la salida temprana de inserción bajan las dos cuentas a 6. Ninguno de los dos deja de moverse con la entrada invertida, y ahí los dos llegan a 21. La selección es la que nunca cambia su cuenta, porque mira todo pase lo que pase, y por eso no aparece en esta tabla con tres números distintos. La búsqueda secuencial le gana a la binaria al buscar 1471, que quedó en la posición 0 del arreglo ordenado: una comparación contra tres.

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| Los contadores viven dentro del algoritmo, con dos `out` | 3 |
| Las tres entradas corren sobre `Clone` y no se contaminan | 2 |
| Los seis pares de conteos coinciden con la medición | 3 |
| Las dos búsquedas devuelven comparaciones y no la posición | 1 |
| Explica el caso en que la secuencial gana | 1 |

**Error que más se ve**

Cuentan los intercambios de burbuja como tres movimientos cada uno, porque el intercambio son tres asignaciones; se delata porque su cuenta de movimientos triplica la de la clase y su definición de movimiento no aparece escrita en ningún lado.

## Semana 15 · Tema 7.1 · Registros y enumeraciones

### 15.1 · Reconocer

**Solución**

Un `struct` se llena solo antes que tú: los campos numéricos arrancan en 0 y el campo de enumeración arranca en el nombre que valga 0, que aquí es `Ok`. Copiar un `struct` copia campo por campo, y cuando un campo es una referencia lo que se copia es la referencia.

**Salida**

```text
warning CS0649: Field 'Muestra.SensorId' is never assigned to, and will always have its default value 0
warning CS0649: Field 'Muestra.Celsius' is never assigned to, and will always have its default value 0
warning CS0649: Field 'Muestra.Estado' is never assigned to, and will always have its default value

SensorId 0
Celsius  0
Estado   Ok
parece sano -> True
c1.Nombre      CORRIDA-A
c1.Lecturas[0] 99.9
```

El campo de texto no se movió porque una cadena no se puede editar en su lugar: asignarle otra cosa a `c2.Nombre` cambia la referencia de `c2` y deja la de `c1` donde estaba. El campo de arreglo sí se movió porque `c2.Lecturas[0] = 99.9` no cambia la referencia, escribe dentro del arreglo al que las dos apuntan.

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| Predice las tres `CS0649` y las nombra por campo | 3 |
| Los seis renglones predichos coinciden | 3 |
| Explica por qué `Estado` sale en `Ok` sin que nadie lo asigne | 2 |
| Distingue el campo de texto del campo de arreglo | 2 |

**Error que más se ve**

Predicen `CORRIDA-B` y 99.9, tratando el `struct` como si fuera una clase; se delata porque el renglón del nombre les sale mal y el del arreglo les sale bien por la razón equivocada.

### 15.2 · Aplicar

**Solución**

```csharp
Muestra[] banco = new Muestra[3];

banco[0] = new Muestra { SensorId = 1, Celsius = 20.0, Estado = Estado.Ok };
banco[1] = new Muestra { SensorId = 2, Celsius = 99.9, Estado = Estado.Falla };

Console.WriteLine("sensor  celsius  estado");
foreach (Muestra m in banco)
    Console.WriteLine($"{m.SensorId,-8}{m.Celsius,7:F1}  {m.Estado}");

Muestra caliente = MasCaliente(banco);
Console.WriteLine();
Console.WriteLine($"mas caliente: sensor {caliente.SensorId} a {caliente.Celsius:F1} C");

Console.WriteLine($"lugar 2 sin llenar: {banco[2].SensorId}, {banco[2].Celsius}, {banco[2].Estado}");
Console.WriteLine($"y reporta sano -> {banco[2].Estado == Estado.Ok}");

for (int i = 0; i < banco.Length; i++)
    banco[i].Celsius = banco[i].Celsius + 1.0;

Muestra copia = banco[0];
copia.Celsius = 0.0;

Console.WriteLine();
Console.WriteLine($"tras el for   banco[0].Celsius = {banco[0].Celsius:F1}");
Console.WriteLine($"tras la copia banco[0].Celsius = {banco[0].Celsius:F1}");
Console.WriteLine($"la copia vale                   {copia.Celsius:F1}");

static Muestra MasCaliente(Muestra[] b)
{
    int idx = 0;
    for (int i = 1; i < b.Length; i++)
        if (b[i].Celsius > b[idx].Celsius) idx = i;
    return b[idx];
}

enum Estado { Ok, Alerta, Falla }

struct Muestra
{
    public int SensorId;
    public double Celsius;
    public Estado Estado;
}
```

**Salida**

```text
sensor  celsius  estado
1          20.0  Ok
2          99.9  Falla
0           0.0  Ok

mas caliente: sensor 2 a 99.9 C
lugar 2 sin llenar: 0, 0, Ok
y reporta sano -> True

tras el for   banco[0].Celsius = 21.0
tras la copia banco[0].Celsius = 21.0
la copia vale                   0.0
```

El `for` escribió en el banco porque `banco[i]` es el `struct` mismo, no una copia de él. La variable local sí es una copia, hecha en el momento de la asignación, y escribirle un campo no llega a ningún lado.

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| El registro y la enumeración están declarados al final del archivo | 2 |
| La tabla sale alineada con las tres muestras, incluida la vacía | 2 |
| `MasCaliente` recibe el arreglo y devuelve un registro | 2 |
| El lugar sin llenar se reporta con sus tres campos y su comparación | 2 |
| El `for` escribe y la copia no, y las dos salidas lo demuestran | 2 |

**Error que más se ve**

Usan `foreach` para subir el grado y el compilador contesta `CS1654: Cannot modify members of 'm' because it is a 'foreach iteration variable'`; se delata porque entregan el `.cs` sin salida.

### 15.3 · Integrar

**Solución**

```csharp
Canal[] banco = new Canal[3];

banco[0] = new Canal
{
    Id = 1,
    Lecturas = new double[] { 1480, 1502, 1495 },
    Estado = Estado.Desconocido
};
banco[1] = new Canal
{
    Id = 2,
    Lecturas = new double[] { 1533, 1471, 1509 },
    Estado = Estado.Desconocido
};
banco[2] = new Canal
{
    Id = 3,
    Lecturas = new double[] { 1488, 1496, 1501 },
    Estado = Estado.Desconocido
};

for (int i = 0; i < banco.Length; i++)
{
    int fuera = 0;
    foreach (double r in banco[i].Lecturas)
        if (r < 1480 || r > 1520) fuera++;

    if (fuera == 0) banco[i].Estado = Estado.Ok;
    else if (fuera == 1) banco[i].Estado = Estado.Alerta;
    else banco[i].Estado = Estado.Falla;
}

Console.WriteLine("canal   media  estado   dictamen");
foreach (Canal c in banco)
{
    double suma = 0;
    foreach (double r in c.Lecturas) suma += r;
    double media = suma / c.Lecturas.Length;

    string dictamen = c.Estado switch
    {
        Estado.Ok => "sigue en linea",
        Estado.Alerta => "revisar al cierre de turno",
        Estado.Falla => "sacar de servicio",
        _ => "sin clasificar"
    };

    Console.WriteLine($"{c.Id,-6}{media,8:F2}  {c.Estado,-8} {dictamen}");
}

Console.WriteLine();
Console.WriteLine($"Estado.Desconocido vale {(int)Estado.Desconocido}");
Console.WriteLine($"Estado.Falla vale       {(int)Estado.Falla}");
Console.WriteLine($"(Estado)9 definido      {Enum.IsDefined((Estado)9)}");

Canal copia = banco[0];
copia.Id = 99;
copia.Lecturas[0] = 0;

Console.WriteLine();
Console.WriteLine($"banco[0].Id           {banco[0].Id}");
Console.WriteLine($"banco[0].Lecturas[0]  {banco[0].Lecturas[0]}");

enum Estado { Desconocido = 0, Ok = 1, Alerta = 2, Falla = 3 }

struct Canal
{
    public int Id;
    public double[] Lecturas;
    public Estado Estado;
}
```

**Salida**

```text
canal   media  estado   dictamen
1      1492.33  Ok       sigue en linea
2      1504.33  Falla    sacar de servicio
3      1495.00  Ok       sigue en linea

Estado.Desconocido vale 0
Estado.Falla vale       3
(Estado)9 definido      False

banco[0].Id           1
banco[0].Lecturas[0]  0
```

El canal 2 tiene la media más alta de los tres y es el único que sale de servicio: la media esconde que dos de sus tres lecturas se salieron de banda en direcciones opuestas. Al copiar el registro, el identificador no se movió porque es un valor suelto, y la primera lectura sí se movió porque el arreglo lo comparten los dos registros.

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| La enumeración reserva el cero para lo no clasificado | 2 |
| Los tres canales se llenan y se clasifican con un `for` | 2 |
| El reporte usa `foreach` y una expresión `switch` con descarte | 2 |
| Las tres comprobaciones de la enumeración están corridas | 2 |
| La copia demuestra que el arreglo se comparte y el `int` no | 2 |

**Error que más se ve**

Dejan `Ok = 0` y clasifican con el valor por omisión, así que un canal que nadie alcanzó a clasificar aparece en línea; se delata porque su tabla no tiene ningún canal en `Desconocido` aunque el arreglo tenga lugares que el ciclo no tocó.

## Semana 16 · Tema 7 · Integración y proyecto final

### 16.1 · Reconocer

**Solución**

El contador `cuenta` llega a 3, que ya es un lugar que no existe en un arreglo de tres. La escritura de la cuarta muestra revienta y la línea de `fin` nunca corre.

**Salida**

```text
registrada en el lugar 0
registrada en el lugar 1
registrada en el lugar 2
Unhandled exception. System.IndexOutOfRangeException: Index was outside the bounds of the array.
   at Program.<Main>$(String[] args) in Program.cs:line 6
```

Códigos de salida medidos con el mismo binario: PowerShell 7 reporta -532462766 y Git Bash reporta 127, porque los shells POSIX recortan el estado a ocho bits.

La versión de `LeerOpcion` con `Convert.ToInt32` truena con `FormatException` cuando el operador teclea una letra, truena igual con `3.7`, y truena también con la entrada vacía. Solo con `null`, que es lo que llega cuando la consola se cierra, devuelve 0 en silencio, y ese cero se lee como la opción de salir.

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| Predice tres renglones y la excepción, sin `fin` | 3 |
| Reporta los dos códigos de salida y dice que son del shell | 3 |
| Clasifica las cuatro entradas de `LeerOpcion` | 3 |
| Señala el caso `null` como el más peligroso de los cuatro | 1 |

**Error que más se ve**

Reportan un solo código de salida sin decir en qué shell lo midieron; se delata porque el número que citan no coincide con el de la captura de al lado.

### 16.2 · Aplicar

**Solución**

```csharp
Muestra[] banco = new Muestra[3];
int cuenta = 0;
bool corriendo = true;

while (corriendo)
{
    Console.WriteLine("1 registrar  2 listar  3 estadisticas  0 salir");
    Console.Write("opcion: ");
    switch (LeerOpcion())
    {
        case 1: Registrar(banco, ref cuenta); break;
        case 2: Listar(banco, cuenta); break;
        case 3: Estadisticas(banco, cuenta); break;
        case 0: corriendo = false; break;
        default: Console.WriteLine("opcion no valida"); break;
    }
}

Console.WriteLine("fin");

static int LeerOpcion()
{
    string? linea = Console.ReadLine();
    if (linea == null) return 0;
    if (int.TryParse(linea, out int v)) return v;
    return -1;
}

static void Registrar(Muestra[] b, ref int cuenta)
{
    if (cuenta >= b.Length)
    {
        Console.WriteLine("banco lleno, rechazada");
        return;
    }
    b[cuenta].SensorId = cuenta + 1;
    b[cuenta].Celsius = 20.0 + cuenta;
    b[cuenta].Estado = Estado.Ok;
    cuenta++;
    Console.WriteLine($"registrada en el lugar {cuenta - 1}");
}

static void Listar(Muestra[] b, int cuenta)
{
    if (cuenta == 0)
    {
        Console.WriteLine("sin muestras");
        return;
    }
    for (int i = 0; i < cuenta; i++)
        Console.WriteLine($"{b[i].SensorId,-4}{b[i].Celsius,7:F1}  {b[i].Estado}");
}

static void Estadisticas(Muestra[] b, int cuenta)
{
    if (cuenta == 0)
    {
        Console.WriteLine("sin muestras, sin datos");
        return;
    }
    double suma = 0;
    for (int i = 0; i < cuenta; i++) suma += b[i].Celsius;
    Console.WriteLine($"n = {cuenta}   media = {suma / cuenta:F2} C");
}

enum Estado { Desconocido = 0, Ok = 1, Alerta = 2, Falla = 3 }

struct Muestra
{
    public int SensorId;
    public double Celsius;
    public Estado Estado;
}
```

**Salida**

Con la secuencia `3, 1, 1, 1, 1, x, 2, 3, 0`, y `Build succeeded` con cero advertencias:

```text
1 registrar  2 listar  3 estadisticas  0 salir
opcion: sin muestras, sin datos
1 registrar  2 listar  3 estadisticas  0 salir
opcion: registrada en el lugar 0
1 registrar  2 listar  3 estadisticas  0 salir
opcion: registrada en el lugar 1
1 registrar  2 listar  3 estadisticas  0 salir
opcion: registrada en el lugar 2
1 registrar  2 listar  3 estadisticas  0 salir
opcion: banco lleno, rechazada
1 registrar  2 listar  3 estadisticas  0 salir
opcion: opcion no valida
1 registrar  2 listar  3 estadisticas  0 salir
opcion: 1      20.0  Ok
2      21.0  Ok
3      22.0  Ok
1 registrar  2 listar  3 estadisticas  0 salir
opcion: n = 3   media = 21.00 C
1 registrar  2 listar  3 estadisticas  0 salir
opcion: fin
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| El menú tiene salida probada: `corriendo` solo cambia en `case 0` | 2 |
| `LeerOpcion` distingue vacío, número y basura sin lanzar nada | 2 |
| `Registrar` recibe el contador por `ref` y trae la guarda de capacidad | 3 |
| `Estadisticas` corta antes de dividir cuando no hay muestras | 2 |
| La compilación reporta cero advertencias | 1 |

**Error que más se ve**

`Registrar` recibe el contador por valor, así que el banco siempre escribe en el lugar 0; se delata porque su corrida imprime tres veces «registrada en el lugar 0» y la estadística reporta n igual a 0.

### 16.3 · Integrar

**Solución**

```csharp
using System.Globalization;

const int Minimo = 1480;
const int Maximo = 1520;
const string Estacion = "EST-07";

string captura = "1480,1502,1495,abc,1533,1471,1509,1488";

int intentos = 0;
double umbral;
bool ok;
do
{
    intentos++;
    Console.Write("umbral de alerta en rpm (5 a 60): ");
    string linea = Console.ReadLine() ?? "";
    bool leido = double.TryParse(linea, NumberStyles.Float,
                                 CultureInfo.InvariantCulture, out umbral);
    ok = leido && umbral >= 5.0 && umbral <= 60.0;
    if (!ok) Console.WriteLine($"  rechazado '{linea}'");
    if (intentos == 3) break;
} while (!ok);

if (!ok)
{
    Console.WriteLine("ENCLAVADO: tres capturas invalidas, consola detenida");
}
else
{
    string[] campos = captura.Split(',');
    int[] validas = new int[campos.Length];
    int n = 0, rechazadas = 0;
    foreach (string campo in campos)
    {
        if (int.TryParse(campo.Trim(), out int valor)) { validas[n] = valor; n++; }
        else rechazadas++;
    }

    Muestra[] banco = new Muestra[n];
    for (int i = 0; i < n; i++)
    {
        banco[i].Canal = i;
        banco[i].Rpm = validas[i];
        banco[i].Estado = Clasificar(validas[i], Minimo, Maximo, umbral);
    }

    int suma = 0, fuera = 0;
    foreach (Muestra m in banco)
    {
        suma += m.Rpm;
        if (m.Estado != Estado.Ok) fuera++;
    }
    MinMax(banco, out int menor, out int mayor);

    Console.WriteLine();
    Console.WriteLine($"estacion   {Estacion.ToUpper()}  umbral {umbral:F1} rpm");
    Console.WriteLine($"campos {campos.Length}  leidas {n}  rechazadas {rechazadas}");
    Console.WriteLine($"media entera  {suma / n}");
    Console.WriteLine($"media real    {(double)suma / n:F3} rpm");
    Console.WriteLine($"punto medio   {(Minimo + Maximo) / 2} rpm");
    Console.WriteLine($"rango         {mayor - menor} rpm  ({menor} a {mayor})");
    Console.WriteLine($"desviacion max {Math.Abs(mayor - (Minimo + Maximo) / 2.0):F1} rpm");
    Console.WriteLine($"fuera de Ok   {fuera} de {n}");

    Console.WriteLine();
    Console.WriteLine("canal    rpm  estado   dictamen");
    foreach (Muestra m in banco)
    {
        string dictamen = m.Estado switch
        {
            Estado.Ok => "en linea",
            Estado.Alerta => "revisar al cierre",
            Estado.Falla => "sacar de servicio",
            _ => "sin clasificar"
        };
        Console.WriteLine($"{m.Canal,-5}{m.Rpm,7}  {m.Estado,-8} {dictamen}");
    }
}

static Estado Clasificar(int rpm, int lo, int hi, double umbral)
{
    if (rpm >= lo && rpm <= hi) return Estado.Ok;
    double exceso = Math.Max(lo - rpm, rpm - hi);
    if (exceso <= umbral) return Estado.Alerta;
    return Estado.Falla;
}

static void MinMax(Muestra[] b, out int menor, out int mayor)
{
    menor = b[0].Rpm;
    mayor = b[0].Rpm;
    foreach (Muestra m in b)
    {
        if (m.Rpm < menor) menor = m.Rpm;
        if (m.Rpm > mayor) mayor = m.Rpm;
    }
}

enum Estado { Desconocido = 0, Ok = 1, Alerta = 2, Falla = 3 }

struct Muestra
{
    public int Canal;
    public int Rpm;
    public Estado Estado;
}
```

**Salida**

Compilación con `0 Warning(s)` y `0 Error(s)`. Con las entradas `abc` y luego `10`:

```text
umbral de alerta en rpm (5 a 60):   rechazado 'abc'
umbral de alerta en rpm (5 a 60): 
estacion   EST-07  umbral 10.0 rpm
campos 8  leidas 7  rechazadas 1
media entera  1496
media real    1496.857 rpm
punto medio   1500 rpm
rango         62 rpm  (1471 a 1533)
desviacion max 33.0 rpm
fuera de Ok   2 de 7

canal    rpm  estado   dictamen
0       1480  Ok       en linea
1       1502  Ok       en linea
2       1495  Ok       en linea
3       1533  Falla    sacar de servicio
4       1471  Alerta   revisar al cierre
5       1509  Ok       en linea
6       1488  Ok       en linea
```

Con un umbral de 10 rpm, la muestra de 1471 queda nueve rpm por debajo del mínimo y clasifica como alerta, mientras que la de 1533 se pasa trece por arriba y clasifica como falla. La alternativa que se descartó fue clasificar solo en dos estados, dentro y fuera de banda: con esa versión las dos muestras se reportan igual, y el técnico no sabe a cuál de las dos ir primero.

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| Los ocho renglones de la lista aparecen en el archivo | 3 |
| El `do-while` valida con cultura fijada y corta con `break` | 2 |
| `Clasificar` y `MinMax` son métodos, uno con dos `out` | 2 |
| El reporte sale alineado con dictamen sacado de un `switch` | 2 |
| La compilación reporta cero advertencias | 1 |

**Error que más se ve**

Recorren el banco entero para las estadísticas y no solo las lecturas válidas, y el promedio baja de golpe; se delata porque su reporte imprime un renglón de más con canal 7 en 0 rpm y estado `Desconocido`.

## Semana 17 · Todas las unidades · Repaso y examen final

### 17.1 · Reconocer

**Solución**

| Renglón | De qué semana viene | Por qué |
|---|---|---|
| 1 y 2 | semana 4 | la barra entre dos enteros trunca y el cast va antes de dividir |
| 3 y 4 | semanas 4 y 7 | dos lecturas nunca se comparan con igual, se comparan por tolerancia |
| 5 | semanas 5 y 16 | `Convert.ToInt32` sobre `null` devuelve 0 sin decir nada |
| 6 | semana 15 | un `struct` se copia campo por campo |
| 7 | semanas 11 y 13 | un arreglo es una referencia y asignarlo crea un segundo nombre |
| 8 | semanas 4 y 9 | el `int` se da la vuelta sin error y sin advertencia |

**Salida**

```text
1  1496
2  1496.857
3  False
4  True
5  0
6  20
7  99
8  -2147483648
```

El renglón 5 es el más peligroso porque no truena. Un cero que nadie tecleó entra al banco como si fuera una lectura tomada, baja el promedio y no deja rastro en ningún log. Los otros siete o dan un número visiblemente raro o dan `False`, y ese cero se ve exactamente igual que un dato bueno.

El archivo del alcance no compila: `Program.cs(5,19): error CS0103: The name 'i' does not exist in the current context`. La variable de control nace y muere en el encabezado del `for`, y la columna 19 apunta a la `i` dentro del paréntesis.

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| Los ocho renglones predichos coinciden | 4 |
| Cada trampa queda asociada a la semana que la enseñó | 3 |
| Argumenta por qué el renglón 5 es el más peligroso | 2 |
| Cita `CS0103` con su columna | 1 |

**Error que más se ve**

Predicen `99.9` en el renglón 6 y `20` en el 7, invirtiendo las dos reglas; se delata porque su explicación llama copia a lo que se compartió y compartido a lo que se copió.

### 17.2 · Aplicar

**Solución**

```csharp
using System.Globalization;

string captura = "  EST-07:1480,1502,1495,abc,1533,1471,1509,1488  ";

string[] partes = captura.Trim().Split(':');
string etiqueta = partes[0];
string[] campos = partes[1].Split(',');

int[] rpm = new int[campos.Length];
int n = 0, rechazadas = 0;
foreach (string campo in campos)
{
    bool ok = int.TryParse(campo.Trim(), NumberStyles.Integer,
                           CultureInfo.InvariantCulture, out int valor);
    if (ok) { rpm[n] = valor; n++; }
    else rechazadas++;
}

Muestra[] banco = new Muestra[n];
int suma = 0, fuera = 0;
for (int i = 0; i < n; i++)
{
    bool malo = rpm[i] < 1480 || rpm[i] > 1520;
    banco[i].Canal = i;
    banco[i].Rpm = rpm[i];
    if (malo) { banco[i].Estado = Estado.Falla; fuera++; }
    else banco[i].Estado = Estado.Ok;
    suma += rpm[i];
}

int[] ordenadas = new int[n];
Array.Copy(rpm, ordenadas, n);
Array.Sort(ordenadas);

Console.WriteLine($"etiqueta      {etiqueta}");
Console.WriteLine($"leidas {n}, rechazadas {rechazadas}");
Console.WriteLine($"fuera de banda {fuera} de {n}");
Console.WriteLine($"media entera  {suma / n}");
Console.WriteLine($"media real    {(double)suma / n:F3}");
Console.WriteLine($"mediana       {ordenadas[n / 2]}");

int hay = Array.BinarySearch(ordenadas, 1495);
int noHay = Array.BinarySearch(ordenadas, 1500);
Console.WriteLine($"binaria 1495 -> {hay}");
Console.WriteLine($"binaria 1500 -> {noHay}, insertaria en {~noHay}");

Console.WriteLine();
Console.WriteLine("canal    rpm  estado");
foreach (Muestra m in banco)
    Console.WriteLine($"{m.Canal,-5}{m.Rpm,7}  {m.Estado}");

enum Estado { Desconocido = 0, Ok = 1, Alerta = 2, Falla = 3 }

struct Muestra
{
    public int Canal;
    public int Rpm;
    public Estado Estado;
}
```

**Salida**

Compilación con `0 Warning(s)` y `0 Error(s)`.

```text
etiqueta      EST-07
leidas 7, rechazadas 1
fuera de banda 2 de 7
media entera  1496
media real    1496.857
mediana       1495
binaria 1495 -> 3
binaria 1500 -> -5, insertaria en 4

canal    rpm  estado
0       1480  Ok
1       1502  Ok
2       1495  Ok
3       1533  Falla
4       1471  Falla
5       1509  Ok
6       1488  Ok
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| El corte por dos puntos y por comas separa etiqueta de lecturas | 2 |
| `TryParse` con cultura fijada cuenta buenas y malas | 2 |
| El banco de registros clasifica y acumula en un solo recorrido | 2 |
| El orden se hace sobre una copia y la mediana sale de ahí | 2 |
| Las dos búsquedas están y el negativo se decodifica | 2 |

**Error que más se ve**

Ordenan el arreglo original y después imprimen el reporte por canal, así que el canal 0 ya no es la primera lectura del turno; se delata porque su tabla sale en orden creciente y su mediana coincide con el renglón de en medio de la tabla.

### 17.3 · Integrar

**Solución**

```csharp
const double Tolerancia = 0.030;
const int Capacidad = 3;

double[,] rejilla = {
    { -0.012,  0.004,  0.021, -0.003 },
    {  0.008, -0.031,  0.015,  0.002 },
    { -0.005,  0.011, -0.047,  0.009 }
};

int filas = rejilla.GetLength(0);
int cols = rejilla.GetLength(1);

Posicion[] tablero = new Posicion[Capacidad];
int registradas = 0;

for (int f = 0; f < filas; f++)
{
    PeorDeLaFila(rejilla, f, out int col, out double peor);
    Registrar(tablero, ref registradas, f, col, peor, Tolerancia);
}

Console.WriteLine("pos  punto   desviacion  estado");
for (int i = 0; i < registradas; i++)
{
    Posicion p = tablero[i];
    Console.WriteLine($"{p.Fila,-5}{p.Columna,-7}{p.Desviacion,10:F4}  {p.Estado}");
}

Registrar(tablero, ref registradas, 3, 0, 0.001, Tolerancia);

double[] fila2 = new double[cols];
for (int c = 0; c < cols; c++) fila2[c] = rejilla[2, c];

double[] copia = (double[])fila2.Clone();
Insercion(copia, out int cmp, out int mov);

Console.WriteLine();
Console.WriteLine($"fila 2 original  {fila2[0]:F3} {fila2[1]:F3} {fila2[2]:F3} {fila2[3]:F3}");
Console.WriteLine($"fila 2 ordenada  {copia[0]:F3} {copia[1]:F3} {copia[2]:F3} {copia[3]:F3}");
Console.WriteLine($"insercion        {cmp} comparaciones, {mov} desplazamientos");

int pos = Array.BinarySearch(copia, 0.011);
Console.WriteLine($"binaria 0.011 -> {pos}");

int enInt = int.MaxValue - 1;
long enLong = int.MaxValue - 1;
for (int k = 0; k < 3; k++) { enInt++; enLong++; }

Console.WriteLine();
Console.WriteLine($"ciclos en int   {enInt}");
Console.WriteLine($"ciclos en long  {enLong}");
Console.WriteLine($"coinciden       {enInt == enLong}");

static void PeorDeLaFila(double[,] r, int fila, out int columna, out double peor)
{
    columna = 0;
    peor = r[fila, 0];
    for (int c = 1; c < r.GetLength(1); c++)
        if (Math.Abs(r[fila, c]) > Math.Abs(peor))
        {
            peor = r[fila, c];
            columna = c;
        }
}

static void Registrar(Posicion[] t, ref int cuenta, int fila, int columna,
                      double desviacion, double tolerancia)
{
    if (cuenta >= t.Length)
    {
        Console.WriteLine($"tablero lleno, posicion {fila} rechazada");
        return;
    }
    t[cuenta].Fila = fila;
    t[cuenta].Columna = columna;
    t[cuenta].Desviacion = desviacion;
    if (Math.Abs(desviacion) <= tolerancia * 0.5) t[cuenta].Estado = Estado.Ok;
    else if (Math.Abs(desviacion) <= tolerancia) t[cuenta].Estado = Estado.Alerta;
    else t[cuenta].Estado = Estado.Falla;
    cuenta++;
}

static void Insercion(double[] a, out int cmp, out int mov)
{
    cmp = 0;
    mov = 0;
    for (int i = 1; i < a.Length; i++)
    {
        double clave = a[i];
        int j = i;
        while (j >= 1)
        {
            cmp++;
            if (a[j - 1] <= clave) break;
            a[j] = a[j - 1];
            j--;
            mov++;
        }
        a[j] = clave;
    }
}

enum Estado { Desconocido = 0, Ok = 1, Alerta = 2, Falla = 3 }

struct Posicion
{
    public int Fila;
    public int Columna;
    public double Desviacion;
    public Estado Estado;
}
```

**Salida**

Compilación con `0 Warning(s)` y `0 Error(s)`.

```text
pos  punto   desviacion  estado
0    2          0.0210  Alerta
1    1         -0.0310  Falla
2    2         -0.0470  Falla
tablero lleno, posicion 3 rechazada

fila 2 original  -0.005 0.011 -0.047 0.009
fila 2 ordenada  -0.047 -0.005 0.009 0.011
insercion        5 comparaciones, 3 desplazamientos
binaria 0.011 -> 3

ciclos en int   -2147483647
ciclos en long  2147483649
coinciden       False
```

Tabla de correspondencia entre los bloques y las semanas:

| Bloque | Semanas que lo hicieron posible |
|---|---|
| Rejilla y peor celda con dos `out` | 11, 14 |
| Registro con guarda y contador por `ref` | 11, 15, 16 |
| Clasificación por tolerancia y enumeración sin cero engañoso | 4, 7, 15 |
| Inserción instrumentada y búsqueda binaria | 9, 10, 14 |
| Contador de ciclos en `int` contra `long` | 4, 9 |
| Reporte alineado | 5, 13 |

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| `PeorDeLaFila` usa dos `out` y saca la cota de `GetLength` | 2 |
| `Registrar` trae la guarda y el contador por `ref`, y la cuarta se rechaza | 2 |
| La inserción está instrumentada y trabaja sobre un `Clone` | 2 |
| El contador `int` se da la vuelta y el `long` no, y se compara | 2 |
| La tabla de correspondencia con las semanas está completa | 1 |
| La compilación reporta cero advertencias | 1 |

**Error que más se ve**

Ordenan `fila2` en lugar de su `Clone` y después imprimen «la fila original» ya ordenada; se delata porque sus dos renglones de la fila 2 son idénticos y la comparación entre antes y después deja de decir nada.
