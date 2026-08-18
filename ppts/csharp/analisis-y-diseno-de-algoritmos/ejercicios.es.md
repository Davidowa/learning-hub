# Ejercicios · Análisis y Diseño de Algoritmos · COM101

Este juego acompaña las diecisiete sesiones del curso y está pensado para el grupo de primer semestre de Ingeniería. Cada semana trae tres ejercicios: Reconocer se contesta leyendo código y prediciendo lo que imprime, Aplicar pide escribir un programa contra una especificación con datos concretos, e Integrar amarra el tema de la semana con lo que ya se vio antes. La dificultad sube dentro de la semana y también a lo largo del semestre, así que el Reconocer de la semana 12 pesa más que el Integrar de la semana 4. Todos los problemas viven en el mismo banco de pruebas: el transportador de rodillos de la estación EST-07, su tacómetro con banda nominal de 1480 a 1520 rpm, el tanque de refrigerante, los termopares y el dispositivo de inspección. Se entrega por Blackboard, con el código fuente y la salida real pegada, nunca descrita con palabras.

## Semana 01 · Encuadre y criterios de evaluación

### 01.1 · Reconocer
Escribe en tu cuaderno, antes de tocar el teclado, qué imprime cada una de estas tres líneas. Después córrelas sin cambiarles una letra y anota la salida real al lado de tu predicción.

```csharp
Console.WriteLine(10478 / 7);
Console.WriteLine(0.1 + 0.7);
Console.WriteLine(0.1 + 0.7 == 0.8);
```

El 10478 es la suma de las siete lecturas de rpm del turno y el 7 es el número de muestras. Explica en un renglón por qué la primera línea no imprime 1496.857142857143.

### 01.2 · Aplicar
Crea un proyecto nuevo con `dotnet new console -o est07` y edita el andamio para que imprima exactamente estas cuatro cosas, en este orden: la línea `BANCO DE PRUEBAS EST-07`, la línea `Canal A · transportador de rodillos`, la línea `Banda nominal: 1480 a 1520 rpm` y el valor de `Environment.Version`.

Córrelo con `dotnet run` desde una terminal, no desde el botón del IDE. Entrega la captura donde se vean el código y la salida, más el código de salida que reportó tu shell.

### 01.3 · Integrar
En el `est07.csproj` de tu proyecto cambia la propiedad `<ImplicitUsings>enable</ImplicitUsings>` por `<ImplicitUsings>disable</ImplicitUsings>` y no toques `Program.cs`. Intenta compilar.

Contesta por escrito tres cosas: el mensaje completo del compilador, con archivo, línea, columna y clave; cuántos archivos quedaron en `bin/Debug/net10.0` después del intento; y qué única línea hay que agregar arriba de `Program.cs` para que vuelva a compilar sin regresar la propiedad a `enable`. Comprueba las tres, no las supongas.

## Semana 02 · Tema 1 · Diseño de algoritmos

### 02.1 · Reconocer
El tanque de refrigerante del banco arranca con 12.0 litros y la bomba de llenado entrega 15.0 litros por pulso. Este es el pseudocódigo de la rutina de purga.

```text
INICIO
    nivel = 12.0
    ESCRIBIR "PURGA DE AIRE INICIADA"

    MIENTRAS nivel < 60.0
        nivel = nivel + 15.0
        ESCRIBIR "llenando tanque:", nivel, "L"

    SI nivel >= 60.0 ENTONCES
        ESCRIBIR "nivel alcanzado, abrir bomba de recirculacion"
    SI NO
        ESCRIBIR "ABORTAR: el tanque no alcanzo el nivel"

    ESCRIBIR "banco listo"
TERMINA
```

Escribe la traza completa: cuántos renglones imprime, con qué valor de nivel cada uno, y con cuánto líquido termina el tanque. Después contesta si el tanque quedó exactamente en 60.0 litros y por qué.

### 02.2 · Aplicar
Escribe en papel el algoritmo de la verificación previa al arranque del transportador. La secuencia revisa tres cosas en este orden: que la puerta de la guarda esté cerrada, que el paro de emergencia esté liberado y que el eje gire por debajo de 50 rpm. Si las tres se cumplen, arma la máquina. Si alguna falla, la nombra y deja la máquina enclavada.

Entrega el pseudocódigo con las siete palabras del curso y el diagrama de flujo correspondiente. Anexa la traza esperada para dos juegos de datos: puerta cerrada, paro liberado y 20 rpm; y puerta abierta, paro liberado y 20 rpm.

### 02.3 · Integrar
La instrucción de mantenimiento dice: «aprieta la tapa del reductor en cruz hasta que quede firme». Aplícale la prueba de las dos personas y explica en dos renglones cuál de las cinco propiedades de un algoritmo se rompe.

Después reescríbela como algoritmo. La tapa tiene cuatro tornillos, el apriete se hace en tres pasadas y el par de cada pasada es 8, 16 y 24 N·m. Escribe el pseudocódigo con dos PARA anidados y, antes de que nadie corra nada, escribe la traza esperada completa, renglón por renglón. La última línea tiene que decir cuántas operaciones de apriete se hicieron.

## Semana 03 · Tema 2 · Introducción a la programación

### 03.1 · Reconocer
Cinco fragmentos, cada uno en su propio archivo. Di para cada uno si compila y, cuando no, cuál es la clave del primer error y qué fue lo que el compilador leyó mal.

```csharp
// A
int parNominal = 24;
Console.WriteLine(parNominal)

// B
int 2sensor = 7;

// C
int parNominal = 24;
Console.writeline(parNominal);

// D
int parNominal = 24;
Console.WriteLine(ParNominal);

// E
int class = 7;
```

Uno de los cinco produce siete errores de un solo descuido. Di cuál y por qué el compilador ve tantos.

### 03.2 · Aplicar
Escribe un programa que declare tres variables enteras con el mismo nombre escrito con distinta caja, `parNominal`, `ParNominal` y `PARNOMINAL`, con los valores 24, 26 y 22 N·m. El programa tiene que imprimir los tres valores en un solo renglón, imprimir si las dos primeras son distintas, imprimir una cadena que contenga los caracteres `//` sin que se conviertan en comentario, e imprimir el resultado de comparar `"Console"` con `"console"`.

El archivo lleva un comentario de línea y uno de bloque, y los nombres siguen la convención del curso. Entrega el `.cs` y la salida.

### 03.3 · Integrar
Rompe el andamio a propósito cuatro veces, una por archivo, y arma una tabla con lo que devuelve cada intento. Los cuatro descuidos son: quitarle el punto y coma a la llamada de `Console.WriteLine`, declarar `int 2sensor = 7;`, escribir `Console.writeline` con minúscula, y pedir `ParNominal` cuando la variable se llama `parNominal`.

De cada intento copia el primer mensaje completo, sin editarlo, con archivo, línea, columna y clave. Agrega un renglón por caso que diga qué leyó mal el compilador. Dos de los cuatro se quejan de un nombre y devuelven claves distintas: explica por qué.

## Semana 04 · Tema 3 · Datos, tipos y operaciones primitivas

### 04.1 · Reconocer
La banda del tacómetro se ensanchó a 1471 y 1533 rpm. Predice las cinco salidas antes de correr nada.

```csharp
int lo = 1471, hi = 1533;
Console.WriteLine(lo + hi / 2);
Console.WriteLine((lo + hi) / 2);
Console.WriteLine((lo + hi) / 2.0);
Console.WriteLine(hi % 100);
Console.WriteLine(7 / 2 * 2);
```

Una de las cinco imprime un número que ningún tacómetro del planeta puede leer. Señálala y di qué operador ganó la carrera.

### 04.2 · Aplicar
Escribe la tarjeta de identidad de un calibre del banco usando los cinco tipos, uno por dato: la estación es `EST-11`, el canal es la letra `C`, se tomaron 12 muestras, la cota medida es 24.972 mm y el canal está en línea. La cota nominal, 25.0 mm, va bajo `const` porque no debe moverse en toda la corrida.

El programa calcula la desviación contra la nominal, la imprime cruda y con tres decimales, e imprime si cabe dentro de una tolerancia de 0.05 mm. La revisión de tolerancia se hace con `Math.Abs`, nunca con un signo de igual.

### 04.3 · Integrar
Un solo programa, tres trampas, cero advertencias al compilar. Escríbelo y explica cada resultado en un renglón.

1. Un contador de piezas inspeccionadas declarado `byte` vale 250 y le sumas 10 con `+=`. Imprime el resultado.
2. Una ventana de muestreo declarada `short` vale 32000 y le sumas 1000 con `+=`. Imprime el resultado.
3. Cuatro desviaciones medidas valen 0.5, 1.5, 2.5 y 3.5 micras. Imprime tres sumas: la real, la que sale de redondear cada una con `Math.Round` a secas, y la que sale de redondear cada una con `MidpointRounding.AwayFromZero`.
4. Con `lo = 1471` y `hi = 1533`, imprime el punto medio de la banda con paréntesis y sin ellos.

Cierra con dos renglones: cuál de las dos reglas de redondeo usarías para reportar el desgaste acumulado de un lote de cien piezas, y por qué.

## Semana 05 · Tema 4 · Instrucciones, lectura y escritura

### 05.1 · Reconocer
Los límites de la banda son 1480 y 1520. Predice las cinco salidas.

```csharp
int lo = 1480, hi = 1520;
Console.WriteLine("rpm " + lo + hi);
Console.WriteLine("rpm " + (lo + hi));
Console.WriteLine(lo + hi + " rpm");
Console.WriteLine($"rpm {lo + hi}");
Console.WriteLine("desviaciones " + 2 + 3 + 4);
```

Ninguna de las cinco da error. Explica en dos renglones la regla que decide cuándo el signo de más suma y cuándo pega.

### 05.2 · Aplicar
Escribe el front end de captura del banco. Pide tres cosas con `Console.Write`, en este orden: la etiqueta de la estación, el número de muestras tomadas y la lectura en rpm. Guarda cada línea en una variable antes de convertirla.

Convierte las muestras con `int.TryParse` y la lectura con `double.TryParse`, y guarda el `bool` que devuelve cada una. Después imprime un bloque con la etiqueta, los dos `bool` con su valor convertido al lado, la lectura con tres decimales fijos y los ciclos del turno, 148230, con separador de miles.

Todavía no hay `if` en el curso, así que el `bool` se imprime, no se usa para decidir. Corre el programa con `EST-07`, `12` y `1496.857142857143`.

### 05.3 · Integrar
La lectura `480.50` viene de un equipo que reporta la carga permisible en kilonewtons. Escribe un programa que fije la cultura de la máquina a `es-MX`, convierta esa cadena con `double.TryParse` e imprima el `bool` y el valor; que después fije la cultura a `de-DE` y repita exactamente lo mismo; y que en cada cultura imprima además 1496.857142 con dos decimales, 148230 con separador de miles y 0.0342 como porcentaje con un decimal.

Al final, ya de regreso en `es-MX`, imprime la carga permisible cruda y con dos decimales, calculada como 480.50 entre un factor de seguridad de 1.10.

Contesta por escrito: en `de-DE` el guardia devolvió `True` y el valor quedó mal. Explica en dos renglones por qué revisar el `bool` no alcanza y qué habría que fijar además.

## Semana 06 · Tema 4.4 · Estructuras de selección

### 06.1 · Reconocer
El enclavamiento de refrigerante del reductor abre la derivación cuando la lectura pasa de 28.0 grados. Alguien le quitó las llaves al bloque.

```csharp
double refrig = 26.8;

if (refrig > 28.0)
    Console.WriteLine("alarma: refrigerante caliente");
    Console.WriteLine("valvula de derivacion abierta");

Console.WriteLine($"lectura {refrig} C registrada");
```

Predice cuántos renglones imprime y cuáles. Después contesta qué imprimiría con `refrig = 31.4` y, en un renglón, qué falla del banco provoca esta versión del programa cuando el refrigerante está frío.

### 06.2 · Aplicar
Escribe un programa que pida las rpm del eje con `Console.Write`, las lea con `int.TryParse` y las clasifique con una escalera de `else if` en cinco casos: lectura no numérica, lectura negativa (cable del tacómetro suelto), menor que 800 (en reposo), menor que 3000 (nominal) y el resto (sobrevelocidad, cortar par).

Cada rama imprime un solo renglón que incluye la lectura. Corre el programa cinco veces, con `800`, `-5`, `799`, `3000` y `abc`, y pega las cinco salidas. Explica en un renglón por qué 799 y 800 caen en bandas distintas.

### 06.3 · Integrar
Escribe la consola de enclavamiento del reductor. Pide dos datos, la temperatura del refrigerante en grados y las rpm del eje, y convierte los dos con `TryParse` guardando su `bool`. El límite de 28.0 grados va bajo `const`.

Guarda en dos variables `bool` con nombre si la lectura está caliente y si cae exactamente sobre el límite. La escalera decide, en este orden: temperatura no numérica, rpm no numérica, caliente (derivación abierta) y el resto (derivación cerrada). Las ramas que sí tienen dato imprimen la lectura con un decimal junto al límite.

La última línea del programa imprime siempre los dos `bool` y las rpm leídas, pase lo que pase. Corre el programa con tres juegos de datos: `31.4` y `1502`, `28.0` y `1502`, y `abc` y `1502`. Explica en dos renglones qué habría cambiado en el segundo juego si la comparación fuera `>=` en lugar de `>`.

## Semana 07 · Tema 4.4 · Selección, profundización

### 07.1 · Reconocer
Cuatro renglones de salida, y ninguna línea de este programa da error. Predícelos.

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

Después contesta dos cosas por escrito. Qué pasaría si el `&&` de la primera condición fuera un solo `&`, y a qué `if` se ligó el `else` del segundo bloque.

### 07.2 · Aplicar
Escribe el inspector de piezas del banco. Pide dos datos, la cota medida en milímetros y la temperatura del refrigerante en grados, y lee los dos con `double.TryParse`. La cota nominal, 25.00 mm, y la tolerancia, 0.05 mm, van bajo `const`.

Si cualquiera de las dos capturas falla, el programa imprime un solo renglón diciendo que la pieza no se dictamina y no calcula nada más. Si las dos sirven, calcula la desviación absoluta con `Math.Abs`, decide con una expresión `switch` sobre el `bool` si la pieza se acepta o se rechaza, y clasifica la temperatura con otra expresión `switch` de cinco brazos: negativa (sensor desconectado), menor que 20.0 (frío), menor o igual que 28.0 (nominal), menor que 90.0 (caliente, derivación abierta) y el brazo de descarte (paro por sobretemperatura).

Corre el programa con cuatro juegos: `25.06` y `31.4`, `24.97` y `28.0`, `25.00` y `-3.0`, y `abc` y `28.0`.

### 07.3 · Integrar
Escribe la matriz de enclavamiento de la máquina. Pide tres datos: la presión en bar, si la puerta está cerrada (1 o 0) y el modo (0 paro, 1 automático, 2 jog). Los tres se leen con `TryParse` y si alguno falla el programa imprime un renglón y deja la máquina enclavada.

La presión está en rango entre 3.5 y 5.0 bar, las dos comparaciones unidas por `&&`. La máquina arranca solo si la presión está en rango, la puerta está cerrada y el modo es automático. Una expresión `switch` con brazo de descarte traduce el número de modo a su nombre.

El programa imprime cuatro renglones con los `bool` intermedios y el resultado de `arrancar`. Cuando `arrancar` es falso, una escalera anidada con llaves nombra la primera causa, en el orden presión, puerta, modo.

Entrega la tabla de verdad con estas cuatro filas y las cuatro corridas al lado: `4.2 1 1`, `4.2 0 1`, `0.5 1 1` y `4.2 1 2`. Agrega dos renglones que expliquen por qué el `&&` es el que protege esta matriz y qué arrancaría con `||` en su lugar.

## Semana 08 · Tema 4.5 · Repetición · Primer parcial

Los tres ejercicios de esta semana repasan las unidades 1 a 4 y la repetición al nivel en que se enseñó hoy. El `for`, el anidamiento y el costo contado son de la semana 9 y no entran aquí.

### 08.1 · Reconocer
Siete tornillos de la tapa del reductor se midieron con torquímetro. Predice los cinco números que imprime este programa.

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

Console.WriteLine($"tornillos revisados  {revisadas}");
Console.WriteLine($"saltados por flojos  {saltadas}");
Console.WriteLine($"suma en tolerancia   {suma}");
Console.WriteLine($"indice del corte     {corte}");
Console.WriteLine($"nunca se revisaron   {par.Length - revisadas}");
```

Señala con el dedo la línea que vuelve falsa la condición del `while` y di qué pasa si borras el `i++` que está antes del `continue`.

### 08.2 · Aplicar
Escribe la captura defendida de la temperatura del refrigerante. El programa pide un valor con `Console.Write`, lo lee con `double.TryParse` y solo lo acepta si cae entre 10.0 y 95.0 grados. Mientras no lo acepte, vuelve a pedirlo e imprime un renglón sangrado que muestre entre comillas exactamente lo que se tecleó.

El ciclo se corta a los cuatro intentos y deja el banco enclavado. Al aceptar, imprime la temperatura con un decimal y cuántos intentos costó.

Corre el programa dos veces. La primera con `abc`, `120`, `-5` y `31.4`. La segunda con cuatro capturas basura seguidas. Justifica en un párrafo por qué aquí va `do-while` y no `while`.

### 08.3 · Integrar
Escribe la consola de cierre de turno. Cruza lo que llevas del semestre en un solo archivo, en este orden.

1. Los límites de la banda, 1480 y 1520, van bajo `const`.
2. Un `do-while` pide la muestra de cierre en rpm, la lee con `int.TryParse` y la acepta solo dentro de la banda. Tres intentos y enclava.
3. Si aceptó, una escalera de `else if` la clasifica en banda baja (menor que 1490), central (menor que 1510) o alta.
4. Tres enclavamientos unidos con `&&` deciden si la máquina queda armada: puerta cerrada, paro liberado y la muestra dentro de la banda.
5. Un `while` recorre la corrida `{ 1480, 1502, 1495, 1533, 1471, 1509, 1488 }` acumulando la suma y contando las lecturas fuera de banda con la regla `r < 1480 || r > 1520`.
6. Imprime suma, media entera, media real con tres decimales y el conteo de fuera de banda.

Corre el programa con `abc` y luego `1502`. Explica en dos renglones por qué la media entera y la media real no son el mismo número.

## Semana 09 · Tema 4.5 · Repetición, profundización

### 09.1 · Reconocer
Cuatro sensores del banco se comparan por pares. Predice los tres números.

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

Console.WriteLine($"pasadas externas {externas}");
Console.WriteLine($"pasadas internas {internas}");
Console.WriteLine($"pares contados   {pares}");
```

Contesta además dos preguntas. De cuál de los dos ciclos sale el `break`, y qué contesta el compilador si después del ciclo externo escribes `Console.WriteLine(a);`.

### 09.2 · Aplicar
Sobre la corrida `{ 1480, 1502, 1495, 1533, 1471, 1509, 1488 }`, escribe un programa con un solo `for` que llene cuatro acumuladores: la suma, el conteo de lecturas fuera de la banda 1480 a 1520 con la regla `r < 1480 || r > 1520`, el índice del máximo y el índice del mínimo. Las cuatro variables se declaran antes del ciclo.

Agrega después un `foreach` que vuelva a sumar y a contar las lecturas, para comprobar que da lo mismo. El programa imprime nueve renglones: lecturas, suma con la suma del `foreach` entre paréntesis, media entera, media real cruda, media con tres decimales, conteo de fuera de banda, máximo con su índice, mínimo con su índice y el rango.

Explica en un renglón cuál de los cuatro acumuladores no se puede escribir con `foreach` y por qué.

### 09.3 · Integrar
Escribe el reporte de fatiga del banco. Un solo archivo con tres bloques y sus salidas.

1. Sobre las siete lecturas de la corrida, cuenta las que quedan fuera de banda e imprime el porcentaje de cuatro maneras: `fuera * 100 / 7`, `fuera * 100.0 / 7`, ese mismo valor con un decimal, y el conteo crudo. Explica cuál de los tres números reportarías al jefe de mantenimiento.
2. Con dos ciclos anidados cuenta cuántas comparaciones hace la malla completa de los siete sensores contra todos, y cuántas hace la versión que arranca el ciclo interno en `a + 1`. Imprime los dos conteos.
3. Un contador de ciclos declarado `int` arranca en `int.MaxValue - 2` y sube tres veces dentro de un `for`, imprimiendo su valor en cada vuelta. El mismo conteo repetido en `long` se imprime al final. Cierra con cuántos días de corrida continua a 25 ciclos por segundo tardaría el contador `int` en llegar a su tope, con un decimal.

Escribe al final dos renglones: qué habría reportado el sistema de mantenimiento la mañana en que el contador `int` se dio la vuelta, y cómo se detecta ese caso sin cambiar el tipo.

## Semana 10 · Tema 5.1 · Funciones definidas por el usuario

### 10.1 · Reconocer
Tres archivos distintos. Di para cada uno si compila, qué clave devuelve el compilador y qué imprime al correr.

```csharp
// A
static void ImprimirEncabezado()
{
    Console.WriteLine("BANCO EST-07 - CIERRE DE TURNO");
}

// B
double m = MostrarMedia(21.0, 39.5);
Console.WriteLine(m);

static void MostrarMedia(double a, double b)
{
    Console.WriteLine((a + b) / 2);
}

// C
int limiteC = 30;
Console.WriteLine(SobreLimite(39));

static int SobreLimite(int lectura)
{
    return lectura - limiteC;
}
```

El archivo A compila. Explica en un renglón por qué no imprime nada y qué le está avisando el compilador. Del C, di qué palabra hay que quitar para que compile y qué se pierde al quitarla.

### 10.2 · Aplicar
Toma el barrido de acumuladores de la semana 9 y pártelo en cuatro métodos con nombre, todos marcados `static`.

- `Suma` recibe el arreglo de lecturas y devuelve el total.
- `Media` recibe el arreglo y devuelve el promedio real, apoyándose en `Suma`.
- `FueraDeBanda` recibe el arreglo y los dos límites, y devuelve cuántas lecturas quedan fuera.
- `IndiceDelMaximo` recibe el arreglo y devuelve la posición de la lectura más alta.

El código de nivel superior solo llama a los cuatro y arma cuatro renglones de salida sobre la corrida `{ 1480, 1502, 1495, 1533, 1471, 1509, 1488 }` con los límites 1480 y 1520. La media se imprime con tres decimales. Ninguno de los cuatro métodos imprime nada por su cuenta.

### 10.3 · Integrar
Escribe el programa que mide qué le llega al llamador cuando un arreglo cruza la frontera de un método. Sobre la corrida de siete lecturas, en este orden:

1. `PonerACero` recibe el arreglo y le escribe un 0 en la posición 0. Imprime `rpm[0]` después de llamarlo.
2. `Reemplazar` recibe el arreglo y le asigna adentro un arreglo nuevo de tres elementos en menos uno. Imprime `rpm[0]` después de llamarlo.
3. `ReemplazarRef` hace exactamente lo mismo, pero el parámetro va con `ref`. Imprime `rpm[0]` después de llamarlo.
4. `Ventana` recibe el arreglo, un índice de inicio y un conteo, y devuelve un arreglo nuevo con esa ventana. Recorta la ventana que empieza en 2 y mide 3, escríbele un 0 en su primera posición e imprime la ventana y también `original[2]`.
5. `Media` está declarado con `params int[] muestras` y devuelve `double.NaN` cuando no recibe ninguna. Llámalo con dos muestras, con la corrida completa y sin argumentos.

Explica en tres renglones por qué el punto 1 le llega al llamador, el punto 2 no, y qué palabra cambia el desenlace del punto 3.

## Semana 11 · Tema 5.3 · Paso de parámetros por referencia

### 11.1 · Reconocer
Predice los tres renglones. El cuerpo de los dos métodos de intercambio es idéntico.

```csharp
int canalA = 1, canalB = 2;

IntercambiarPorValor(canalA, canalB);
Console.WriteLine($"por valor      {canalA}, {canalB}");

IntercambiarPorRef(ref canalA, ref canalB);
Console.WriteLine($"por referencia {canalA}, {canalB}");

int guardado = 999;
bool ok = int.TryParse("abc", out guardado);
Console.WriteLine($"TryParse       {ok}, guardado = {guardado}");

static void IntercambiarPorValor(int a, int b)
{
    int t = a; a = b; b = t;
}

static void IntercambiarPorRef(ref int a, ref int b)
{
    int t = a; a = b; b = t;
}
```

Contesta además qué contesta el compilador si en la segunda llamada quitas los dos `ref` del sitio de llamada y dejas la firma como está.

### 11.2 · Aplicar
Escribe dos piezas del banco en un solo archivo.

`MinMax` recibe el arreglo de termopares `{ 21.0, 39.5, 22.4 }` y dos parámetros `out`, y deja en ellos la lectura más fría y la más caliente. El llamador imprime las dos con un decimal.

`Llenar` y `Vaciar` reciben el nivel del tanque de refrigerante por `ref` y una cantidad en litros. `Llenar` rechaza cualquier operación que pase de 60.0 litros y `Vaciar` rechaza cualquiera que deje el tanque por debajo de 5.0 litros. El mensaje de rechazo dice el número que habría quedado, no solo que no se pudo.

Arranca el tanque en 40.0 litros y encadena cuatro operaciones: llenar 15.0, llenar 10.0, vaciar 20.0 y vaciar 40.0. Imprime el nivel después de cada una.

### 11.3 · Integrar
Escribe la rutina de calibración de un canal del banco. En este orden:

1. Declara `banco = { 21.0, 39.5, 22.4 }` y un segundo nombre `alias` asignado a partir del primero. Escribe 99.9 en `alias[0]` e imprime `banco[0]` y el resultado de `ReferenceEquals`. Regresa `banco[0]` a 21.0.
2. Un `do-while` pide el ajuste de calibración en grados y lo lee con `double.TryParse`. Solo acepta valores entre -5.0 y 5.0, se corta a los tres intentos y en ese caso deja el banco sin tocar.
3. Si aceptó, `Aplicar` suma el ajuste al canal 1 recibiendo el elemento del arreglo por `ref`, y `Recortar` deja ese mismo elemento en 30.0 si lo pasó, avisando de cuánto a cuánto lo recortó.
4. `MinMax` con dos `out` reporta el nuevo mínimo y máximo del banco.

Corre el programa con `abc` y luego `-2.5`. Explica en tres renglones por qué el arreglo del punto 1 se comparte sin que nadie escriba `ref`, y por qué el punto 3 sí necesita la palabra.

## Semana 12 · Tema 5.4 · Funciones predefinidas

### 12.1 · Reconocer
Diez renglones de salida y una advertencia del compilador. Predice los diez y di de qué línea sale la advertencia.

```csharp
double nan = Math.Sqrt(-1);

Console.WriteLine($"Math.Sqrt(-1)          {nan}");
Console.WriteLine($"nan == nan             {nan == nan}");
Console.WriteLine($"double.IsNaN(nan)      {double.IsNaN(nan)}");
Console.WriteLine($"Math.Sin(Math.PI)      {Math.Sin(Math.PI)}");
Console.WriteLine($"|sin(pi)| < 1e-9       {Math.Abs(Math.Sin(Math.PI)) < 1e-9}");
Console.WriteLine($"Math.Round(2.5)        {Math.Round(2.5)}");
Console.WriteLine($"Round(2.5) lejos de 0  {Math.Round(2.5, MidpointRounding.AwayFromZero)}");
Console.WriteLine($"1.0 / 0                {1.0 / 0}");
Console.WriteLine($"Math.Clamp(39.5,0,30)  {Math.Clamp(39.5, 0.0, 30.0)}");
Console.WriteLine($"Math.Pow(2, 10)        {Math.Pow(2, 10)}");
```

Contesta tres cosas más. Por qué la segunda línea no imprime `True`. Qué clave devuelve el compilador si escribes `int capacidad = Math.Pow(2, 10);`. Y qué devuelve `Math.Sqrt("9")`.

### 12.2 · Aplicar
La ventana de vibración del reductor trae siete muestras en mm/s: `{ 0.42, -0.31, 0.55, -0.48, 0.12, -0.27, 0.61 }`. Escribe el programa que calcula el valor RMS.

Recorre la ventana con `foreach`, acumula el cuadrado de cada muestra con `Math.Pow` y lleva el pico con `Math.Max` sobre `Math.Abs`. El RMS es la raíz cuadrada del promedio de los cuadrados, con `Math.Sqrt`. Calcula además el factor de cresta, que es el pico entre el RMS, y el RMS recortado al umbral de alarma de 0.4500 mm/s con `Math.Clamp`.

Imprime seis renglones: el RMS crudo con todos sus dígitos, el RMS con cuatro decimales y unidad, el pico, el factor de cresta, el RMS recortado y si el RMS pasó el umbral.

### 12.3 · Integrar
El banco está desarmado y hay que probar los acumuladores sin él. Escribe el programa que simula veinte muestras de rpm y las pasa por el barrido de la semana 9.

La semilla, 2026, va bajo `const` y el generador se construye una sola vez, fuera del ciclo. Cada muestra sale de `Next(1400, 1601)`. Un `for` llena el arreglo y otro acumula la suma, cuenta las lecturas fuera de la banda 1480 a 1520 y lleva el índice de la más alta.

El programa imprime la semilla, las primeras cinco muestras, la suma, la media con tres decimales, el conteo de fuera de banda y el pico con su índice. Cierra armando una palabra de estado: suma 1 si hubo lecturas fuera de banda, suma 2 si el pico pasó de 1520 y suma 4 si la media entera pasó de 1500. Imprime esa palabra en decimal, en binario y en hexadecimal con `Convert.ToString`.

Corre el programa dos veces seguidas y pega las dos salidas. Explica en dos renglones qué habría cambiado si el generador se construyera dentro del ciclo.

## Semana 13 · Tema 6.1 · Arreglos y cadenas · Segundo parcial

Los tres ejercicios repasan la unidad 5 completa y la unidad 6 hasta el subtema 6.1.3. Las rejillas de dos índices y los algoritmos de ordenación y de búsqueda son de la semana 14 y no entran aquí. La llamada `Array.Sort` sí entra, porque el deck de hoy la usa para sacar una mediana.

### 13.1 · Reconocer
Once renglones de salida. Predícelos todos.

```csharp
int[] src = { 1480, 1502, 1495 };
int[] alias = src;
int[] copia = (int[])src.Clone();

alias[0] = 99;
copia[1] = 77;

Console.WriteLine($"src[0] {src[0]}   src[1] {src[1]}");
Console.WriteLine($"alias es el mismo {ReferenceEquals(src, alias)}");
Console.WriteLine($"copia es el mismo {ReferenceEquals(src, copia)}");

string tag = "sensor-07";
tag.ToUpper();
Console.WriteLine($"tag        {tag}");
Console.WriteLine($"ToUpper()  {tag.ToUpper()}");
Console.WriteLine($"tag.Length {tag.Length}");
Console.WriteLine($"vacia dentro {tag.Contains("")}");
Console.WriteLine($"campos de la vacia {"".Split(';').Length}");
Console.WriteLine($"Substring(9) [{tag.Substring(9)}]");
```

Contesta además qué pasa si cambias `tag.Substring(9)` por `tag.Substring(10)`, y qué pasa con `tag[9]`. Los dos índices están fuera del texto y no fallan igual.

### 13.2 · Aplicar
El registrador entrega esta línea, con espacios a los lados: `  EST-07:1480.0,1502.5,1495.0,1533.5  `.

Escribe el programa que la parte en etiqueta y lecturas. Recorta primero con `Trim`, corta por dos puntos y después por comas, y convierte cada campo con `double.Parse` fijando `CultureInfo.InvariantCulture`. Imprime la etiqueta, cuántos campos salieron, la media con tres decimales y la primera y la última lectura con un decimal.

En el mismo archivo escribe `IdValido`, que recibe un identificador de parte y devuelve `bool`. Las reglas son: recortar lo que llega, largo exactamente 10, prefijo `SNS-`, sufijo `-A` o `-B`, y las posiciones 4 a 7 tienen que ser dígitos. Las dos comparaciones de texto usan la misma política, `StringComparison.OrdinalIgnoreCase`.

Pruébalo con cinco entradas: `SNS-4471-A`, `  SNS-4471-A  `, `sns-4471-b`, `SNS-44X1-A` y la cadena vacía. La tercera es la que delata si tu validador tiene una sola política o dos.

### 13.3 · Integrar
La captura del turno llegó con un campo echado a perder: `1480,1502,1495,abc,1533,1471,1509,1488`. Escribe el programa que la procesa entero.

1. Corta por comas y convierte cada campo con `int.TryParse`. Las buenas se guardan y las malas se cuentan. Copia las buenas a un arreglo del tamaño exacto.
2. Tres métodos `static` calculan lo demás: `Suma`, `Media` apoyada en `Suma`, y `FueraDeBanda` con los dos límites como parámetros.
3. Saca una copia con `Clone`, ordénala con `Array.Sort` y reporta la mediana. Imprime después el primer elemento del arreglo original para comprobar que la copia no lo tocó.
4. Cierra con un reporte alineado de tres columnas, canal, rpm y estado, donde el estado dice `fuera` cuando la lectura sale de la banda 1480 a 1520.

Imprime también cuántos campos venían, cuántos se leyeron, cuántos se rechazaron, la suma, la media entera y la media real con tres decimales. Explica en dos renglones qué habría pasado con `Convert.ToInt32` en lugar de `TryParse`.

## Semana 14 · Tema 6.2–6.3 · Rejillas, ordenación y búsqueda

### 14.1 · Reconocer
El arreglo de identificadores de muestra no está ordenado y los cinco valores sí están adentro. Predice los seis renglones.

```csharp
int[] sinOrdenar = { 1502, 1471, 1533, 1480, 1495 };

Console.WriteLine($"busca 1533 -> {Array.BinarySearch(sinOrdenar, 1533)}");
Console.WriteLine($"busca 1502 -> {Array.BinarySearch(sinOrdenar, 1502)}");
Console.WriteLine($"busca 1471 -> {Array.BinarySearch(sinOrdenar, 1471)}");
Console.WriteLine($"busca 1495 -> {Array.BinarySearch(sinOrdenar, 1495)}");

int[] ordenadas = { 1471, 1480, 1488, 1495, 1502, 1509, 1533 };
int falta = Array.BinarySearch(ordenadas, 1500);
Console.WriteLine($"busca 1500 -> {falta}");
Console.WriteLine($"punto de insercion -> {~falta}");
```

Dos de las cuatro primeras búsquedas devuelven el mismo número aunque los valores estén en posiciones distintas. Señálalas. Después contesta cuántas de las cuatro contestaron bien, si se lanzó alguna excepción, y qué precondición hay que escribir junto a cualquier llamada a esta biblioteca.

### 14.2 · Aplicar
El dispositivo de inspección mide cuatro puntos por cada una de las tres posiciones de la pieza. Las desviaciones en milímetros son:

```text
posicion 0:  -0.012   0.004   0.021  -0.003
posicion 1:   0.008  -0.031   0.015   0.002
posicion 2:  -0.005   0.011  -0.047   0.009
```

Escribe el programa que carga esa rejilla en un arreglo de dos índices, imprime cuántas posiciones, cuántos puntos, cuántas celdas y qué `Rank` tiene, y después imprime el promedio de cada posición y el promedio de cada punto, con cuatro decimales alineados a la derecha.

Cierra reportando la peor celda por desviación absoluta con sus dos índices y si pasa la tolerancia de 0.030 mm. Los límites de todos los ciclos salen de `GetLength`, no de un 3 ni de un 4 escritos a mano. Agrega una quinta columna a la rejilla y comprueba que el programa sigue corriendo sin tocar un solo ciclo.

### 14.3 · Integrar
Instrumenta dos ordenamientos y dos búsquedas sobre las mismas lecturas, y reporta los conteos.

Escribe `Burbuja` con bandera de salida temprana y `Insercion`, las dos con dos parámetros `out` que devuelvan comparaciones y movimientos. Una comparación de burbuja es cada evaluación de `a[j] > a[j + 1]`, y una de inserción es cada evaluación de la clave contra `a[j - 1]`.

Córrelos sobre tres entradas de siete lecturas: la corrida registrada `{ 1480, 1502, 1495, 1533, 1471, 1509, 1488 }`, la misma ya ordenada y la misma invertida. Cada corrida trabaja sobre un `Clone`, para que las tres arranquen del mismo lugar. Arma una tabla con los seis pares de conteos.

Después escribe `Secuencial` y `Binaria`, las dos con la firma `static int Buscar(int[] a, int clave)`, que devuelven cuántas comparaciones costó llegar. Búscales 1533 y 1471 sobre el arreglo ya ordenado y reporta los cuatro números.

Cierra con tres renglones: qué entrada le conviene a cada ordenamiento, cuál de los dos nunca cambia su cuenta y por qué la búsqueda secuencial le gana a la binaria en uno de los cuatro casos que mediste.

## Semana 15 · Tema 7.1 · Registros y enumeraciones

### 15.1 · Reconocer
Este programa compila con tres advertencias e imprime seis renglones. Predice las tres advertencias y los seis renglones.

```csharp
Muestra vacia = new Muestra();
Console.WriteLine($"SensorId {vacia.SensorId}");
Console.WriteLine($"Celsius  {vacia.Celsius}");
Console.WriteLine($"Estado   {vacia.Estado}");
Console.WriteLine($"parece sano -> {vacia.Estado == Estado.Ok}");

Corrida c1 = new Corrida();
c1.Nombre = "CORRIDA-A";
c1.Lecturas = new double[] { 20.0, 21.0 };

Corrida c2 = c1;
c2.Nombre = "CORRIDA-B";
c2.Lecturas[0] = 99.9;

Console.WriteLine($"c1.Nombre      {c1.Nombre}");
Console.WriteLine($"c1.Lecturas[0] {c1.Lecturas[0]}");

enum Estado { Ok, Alerta, Falla }

struct Muestra
{
    public int SensorId;
    public double Celsius;
    public Estado Estado;
}

struct Corrida
{
    public string Nombre;
    public double[] Lecturas;
}
```

Explica en dos renglones por qué el campo de texto no se movió y el campo de arreglo sí, cuando la copia fue campo por campo en los dos casos.

### 15.2 · Aplicar
Declara `Muestra` con tres campos, el identificador del sensor, la lectura en grados y el estado, y una enumeración `Estado` con `Ok`, `Alerta` y `Falla`. Crea un arreglo de tres muestras y llena solo las dos primeras: sensor 1 a 20.0 grados en `Ok` y sensor 2 a 99.9 grados en `Falla`.

El programa imprime la tabla completa de las tres muestras alineada en tres columnas, reporta con un método `MasCaliente` cuál sensor trae la lectura más alta, e imprime los tres campos del lugar que nunca se llenó junto con el resultado de compararlo contra `Estado.Ok`.

Después sube un grado a las tres muestras con un `for`, saca una copia de la primera a una variable local, ponle 0.0 a la copia y vuelve a imprimir la primera muestra del arreglo y la copia. Explica en dos renglones por qué el `for` escribió en el banco y la copia no.

### 15.3 · Integrar
Diseña el registro del banco de canales y córrelo. `Canal` tiene tres campos: el identificador, un arreglo de lecturas y el estado. La enumeración `Estado` vale `Desconocido = 0`, `Ok = 1`, `Alerta = 2` y `Falla = 3`, con el cero reservado para lo que nadie clasificó.

Llena tres canales, cada uno con tres lecturas: el canal 1 con `1480, 1502, 1495`, el canal 2 con `1533, 1471, 1509` y el canal 3 con `1488, 1496, 1501`. Todos nacen en `Desconocido`.

Un `for` clasifica cada canal contando sus lecturas fuera de la banda 1480 a 1520: cero fuera es `Ok`, una es `Alerta` y dos o más es `Falla`. Un `foreach` recorre después el banco para imprimir el reporte alineado con el identificador, la media con dos decimales, el estado y un dictamen sacado de una expresión `switch` con brazo de descarte.

Cierra con tres comprobaciones: el valor entero de `Desconocido` y de `Falla`, lo que contesta `Enum.IsDefined` sobre `(Estado)9`, y qué le pasa al canal 1 cuando copias su registro a otra variable, le cambias el identificador y le escribes un 0 a la primera lectura de la copia.

## Semana 16 · Tema 7 · Integración y proyecto final

### 16.1 · Reconocer
Este es el registro del banco sin la guarda, con capacidad para tres muestras y cuatro que registrar.

```csharp
Muestra[] banco = new Muestra[3];
int cuenta = 0;

for (int i = 0; i < 4; i++)
{
    banco[cuenta].SensorId = i + 1;
    banco[cuenta].Celsius = 20.0 + i;
    cuenta++;
    Console.WriteLine($"registrada en el lugar {cuenta - 1}");
}

Console.WriteLine("fin");
```

Predice cuántos renglones alcanza a imprimir, con qué excepción muere y si llega a imprimir `fin`. Después córrelo en PowerShell y en Git Bash y reporta el código de salida de cada uno.

Contesta además qué hace esta versión de la lectura de la opción del menú cuando el operador teclea una letra, cuando teclea `3.7` y cuando la entrada viene vacía:

```csharp
static int LeerOpcion()
{
    string linea = Console.ReadLine();
    return Convert.ToInt32(linea);
}
```

### 16.2 · Aplicar
Arma el esqueleto de referencia del proyecto, el que compila y corre antes de tener una sola funcionalidad adentro.

El menú es un `while` con cuatro opciones: 1 registrar, 2 listar, 3 estadísticas y 0 salir, resuelto con un `switch` que tiene brazo `default`. `LeerOpcion` devuelve 0 cuando la entrada viene vacía, el número cuando `int.TryParse` lo logra, y menos uno en cualquier otro caso.

`Registrar` recibe el arreglo y el contador por `ref`, y antes de escribir revisa si el banco está lleno. `Listar` y `Estadisticas` reciben el contador por valor y avisan cuando no hay muestras, para que la división entre cero nunca ocurra.

El banco tiene tres lugares y guarda un `struct Muestra` con identificador, grados y un `Estado`. Corre la secuencia `3, 1, 1, 1, 1, x, 2, 3, 0` y pega la salida. La compilación tiene que reportar cero advertencias.

### 16.3 · Integrar
Escribe la consola de inspección del banco EST-07. Es el proyecto integrador en miniatura y tiene que cumplir los renglones de la lista de verificación que se enumeran abajo, en un solo archivo, con cero advertencias.

1. La estación, el mínimo y el máximo de la banda van bajo `const`.
2. Un `do-while` pide el umbral de alerta en rpm, lo lee con `double.TryParse` fijando `InvariantCulture` y solo acepta entre 5.0 y 60.0. Se corta con un `break` justificado a los tres intentos.
3. La línea del registrador `1480,1502,1495,abc,1533,1471,1509,1488` se corta por comas y se convierte con `int.TryParse`, contando las que se rechazan.
4. Un arreglo de `Muestra` guarda canal, rpm y `Estado`, con la enumeración en `Desconocido = 0`, `Ok = 1`, `Alerta = 2` y `Falla = 3`.
5. Un método `Clasificar` decide el estado: dentro de la banda es `Ok`; fuera pero con un exceso menor o igual al umbral es `Alerta`; más allá es `Falla`. El exceso se calcula con `Math.Max`.
6. Un método `MinMax` con dos parámetros `out` reporta la lectura menor y la mayor.
7. Un `foreach` acumula la suma y cuenta las muestras que no quedaron en `Ok`.
8. El reporte imprime la etiqueta en mayúsculas con `ToUpper`, el conteo de campos, la media entera, la media real con tres decimales, el punto medio de la banda con paréntesis, el rango, la desviación máxima con `Math.Abs`, y la tabla alineada de canal, rpm, estado y dictamen sacado de una expresión `switch`.

Corre el programa con `abc` y luego `10`. Entrega el código, la salida y un párrafo con la alternativa de diseño que consideraste y descartaste.

## Semana 17 · Todas las unidades · Repaso y examen final

Los tres ejercicios repasan el semestre completo. No hay material nuevo aquí.

### 17.1 · Reconocer
Ocho renglones numerados. Predícelos todos y di de qué semana viene cada trampa.

```csharp
int suma = 10478, n = 7;
Console.WriteLine($"1  {suma / n}");
Console.WriteLine($"2  {(double)suma / n:F3}");

double lectura = 0.1 + 0.2;
Console.WriteLine($"3  {lectura == 0.3}");
Console.WriteLine($"4  {Math.Abs(lectura - 0.3) < 1e-9}");

string? nada = null;
Console.WriteLine($"5  {Convert.ToInt32(nada)}");

Muestra s1 = new Muestra { SensorId = 1, Celsius = 20.0 };
Muestra s2 = s1;
s2.Celsius = 99.9;
Console.WriteLine($"6  {s1.Celsius}");

int[] src = { 20, 21, 22 };
int[] alias = src;
alias[0] = 99;
Console.WriteLine($"7  {src[0]}");

int ciclos = int.MaxValue;
ciclos++;
Console.WriteLine($"8  {ciclos}");

struct Muestra
{
    public int SensorId;
    public double Celsius;
}
```

De los ocho, el número 5 es el más peligroso en un programa real. Explica por qué en dos renglones. Después di qué contesta el compilador ante este otro archivo y en qué columna apunta:

```csharp
for (int i = 0; i < 3; i++)
{
    Console.WriteLine(i);
}
Console.WriteLine(i);
```

### 17.2 · Aplicar
Escribe el programa de repaso que atraviesa los siete temas del curso. La entrada es la línea del registrador `  EST-07:1480,1502,1495,abc,1533,1471,1509,1488  `, con espacios a los lados.

1. Recorta, corta por dos puntos, separa la etiqueta y corta las lecturas por comas.
2. Convierte cada campo con `int.TryParse` fijando `InvariantCulture`, guardando las buenas y contando las malas.
3. Llena un arreglo de `Muestra` con canal, rpm y `Estado`, clasificando con la regla `r < 1480 || r > 1520` y contando las fuera de banda.
4. Copia con `Array.Copy`, ordena con `Array.Sort` y reporta la mediana.
5. Busca 1495 y 1500 con `Array.BinarySearch` e imprime el retorno de cada una, más el punto de inserción del que no está, decodificado con el complemento a bits.
6. Cierra con el reporte alineado de canal, rpm y estado.

Imprime también la etiqueta, cuántas se leyeron, cuántas se rechazaron, el conteo de fuera de banda, la media entera y la media real con tres decimales. La compilación tiene que reportar cero advertencias.

### 17.3 · Integrar
Cierre de semestre del banco EST-07. Un solo archivo, cero advertencias, cuatro bloques.

1. Carga la rejilla de desviaciones de tres posiciones por cuatro puntos de la semana 14. Un método `PeorDeLaFila` con dos parámetros `out` devuelve la columna y el valor de la peor celda de una fila, comparando por valor absoluto y sacando la cota de `GetLength`.
2. Un método `Registrar` recibe un arreglo de `Posicion` con capacidad para tres y el contador por `ref`, y antes de escribir revisa si hay lugar. Clasifica cada posición en `Ok` si la desviación absoluta cabe en media tolerancia, `Alerta` si cabe en la tolerancia de 0.030 mm y `Falla` si la pasa. Registra las tres posiciones de la rejilla y después intenta registrar una cuarta, para que se vea la guarda trabajando.
3. Copia la fila 2 a un arreglo de una dimensión, sácale un `Clone` y ordénalo con `Insercion` instrumentada con dos `out`. Imprime la fila original, la ordenada y los dos conteos. Busca después el valor 0.011 en la fila ordenada con `Array.BinarySearch`.
4. Un contador de ciclos declarado `int` y otro declarado `long` arrancan los dos en `int.MaxValue - 1` y suben tres veces dentro del mismo `for`. Imprime los dos y si coinciden.

Entrega el código, la salida completa y una tabla de dos columnas que asocie cada bloque del programa con las semanas del curso que lo hicieron posible.
