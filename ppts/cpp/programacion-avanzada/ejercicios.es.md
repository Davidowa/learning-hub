# Ejercicios · Programación Avanzada · COM103

Cincuenta y un ejercicios para el grupo de segundo semestre de la Facultad de Ingeniería, tres por sesión y en el orden en que se ven los temas. Cada semana empieza con uno de lectura, en el que hay que predecir lo que imprime un programa antes de correrlo, sigue con uno de escritura contra una especificación cerrada, y cierra con uno que obliga a usar algo de las semanas anteriores. La dificultad sube dentro de la semana y a lo largo del semestre: el primero de la semana 12 pesa más que el tercero de la semana 4. Todos los problemas viven en el mismo laboratorio de instrumentación, con los mismos canales y las mismas vigas, así que los datos de una semana reaparecen en la siguiente. Se entrega un archivo `.cpp` por ejercicio, compilado en C++20 desde Visual Studio, comprimido sin la carpeta `x64` y subido a Blackboard antes de la sesión siguiente.

---

## Semana 01 · Unidad 1 · Elementos básicos de C++

### 01.1 · Reconocer

**Un caudalímetro que promedia mal**

El banco de pruebas cuenta los pulsos de un caudalímetro en tres ventanas de sesenta segundos y obtiene 1240, 1305 y 1198. Este programa compila y corre sin quejarse.

```cpp
#include <iostream>

int main()
{
    int pulsos1 = 1240;
    int pulsos2 = 1305;
    int pulsos3 = 1198;

    int total = pulsos1 + pulsos2 + pulsos3;
    int promedio = total / 4;

    std::cout << "Total: " << total << "\n";
    std::cout << "Promedio: " << promedio << "\n";
    return 0;
}
```

Conteste sin ejecutarlo:

1. Las dos líneas exactas que imprime.
2. Si pone un punto de ruptura con F9 en la línea del promedio y corre con F5, qué muestra la ventana Locales para `total` y para `promedio` en el instante en que el programa se detiene.
3. Qué línea está mal, y qué imprime el programa ya corregido.

### 01.2 · Aplicar

**Reporte de cuatro lecturas de presión**

El registrador guarda cuatro lecturas de un transductor de presión, en kilopascales enteros: 101, 104, 99 y 108. Escriba un programa que las declare en cuatro variables con nombre propio y que imprima exactamente estas cuatro líneas:

```
Lecturas: 101 104 99 108
Suma: 412
Promedio entero: 103
Rango: 9
```

El rango es la diferencia entre la lectura más alta y la más baja, que aquí se conocen de antemano. Todo va dentro de `main`, con variables de tipo `int`, sin funciones propias, sin `if` y sin ciclos, que llegan más adelante en el curso.

### 01.3 · Integrar

**El archivo que no compila y el estándar que sí importa**

Un compañero manda este archivo y dice que Visual Studio le tira una lista de errores.

```cpp
#include <iostream>

int main()
{
    int muestras = 240
    int frecuencia = 8;

    int duracion = muestras / frecuencia;

    std::cout << "Duracion: " << duracion << " s\n";
    std::cout << "Estandar: " << _MSVC_LANG << "\n";
    return 0;
}
```

1. Diga qué clave de error aparece primero y en qué renglón la reporta el compilador, antes de abrir el archivo en la máquina.
2. Corríjalo. El programa terminado tiene que imprimir `Duracion: 30 s` y `Estandar: 202002`.
3. Si la segunda línea imprime otra cosa, el proyecto no está en C++20. Diga en qué parte de las propiedades del proyecto se arregla y por qué la macro `__cplusplus` no sirve para comprobarlo en este compilador.

---

## Semana 02 · Unidad 1 · Elementos básicos de C++

### 02.1 · Reconocer

**Bloques de 250 muestras**

El adquisidor manda las muestras al disco en bloques de 250. En esta corrida acumuló 1732 muestras.

```cpp
#include <iostream>

int main()
{
    int muestras = 1732;
    const int BLOQUE = 250;

    int bloques = muestras / BLOQUE;
    int sobran = muestras % BLOQUE;

    int enviados = bloques++;
    double ocupacion = sobran / BLOQUE;

    std::cout << bloques << " " << enviados << "\n";
    std::cout << sobran << " " << ocupacion << "\n";
    return 0;
}
```

Escriba las dos líneas que imprime y, junto a cada número, la razón por la que vale eso. Dos de los cuatro valores sorprenden a la primera lectura: diga cuáles y por qué. Después corrija `ocupacion` para que muestre la fracción real del bloque que quedó ocupada, sin cambiar el tipo de `sobran` ni el de `BLOQUE`.

### 02.2 · Aplicar

**Celda de carga de 16 bits**

Una celda de carga entrega una cuenta digital de 0 a 32768, donde el fondo de escala corresponde a 5000 N. En la lectura de hoy la cuenta fue 26214.

Escriba un programa que declare `CUENTA_MAX` y `FONDO_ESCALA_N` como constantes con `const`, guarde la cuenta en una variable `int`, y calcule la fuerza en newtons y el porcentaje del fondo de escala. La conversión a real tiene que ser explícita, con `static_cast`, en el punto donde hace falta y no después. La salida esperada es:

```
Cuenta: 26214
Fuerza: 3999.94 N
Fondo de escala: 79.9988 %
```

Agregue un comentario de bloque de tres renglones que explique qué imprimiría el programa si la conversión se omitiera.

### 02.3 · Integrar

**Cinco resistencias y una desviación en cero**

Cinco mediciones de resistencia de contacto, en miliohms: 118, 121, 117, 123 y 119. El programa que las procesa quedó así.

```cpp
int suma = m1 + m2 + m3 + m4 + m5;
int promedio = suma / 5;
double desviacion = m5 - promedio;
```

1. Diga qué imprime la línea de la desviación tal como está, y por qué ese resultado no significa que la última medición sea la media.
2. Reescriba el programa con el número de mediciones en una constante, y que imprima la suma, el promedio entero, el residuo de la división entera, el promedio real y la desviación de la última lectura respecto de ese promedio real. La salida esperada:

```
Suma: 598
Promedio entero: 119
Residuo: 3
Promedio real: 119.6
Desviacion: -0.6
```

3. Localice el error original con el depurador, sin agregar líneas de impresión, y diga en qué renglón se detuvo y qué valor tenía `promedio` ahí.

---

## Semana 03 · Unidad 2 · Tipos, espacios de nombres y string

### 03.1 · Reconocer

**La etiqueta del termopar y un contador que da la vuelta**

```cpp
#include <iostream>
#include <string>

enum class Estado { Inactivo, Calibrando, Midiendo };

int main()
{
    std::string etiqueta = "TC-04-HORNO";

    unsigned short contador = 0;
    contador = static_cast<unsigned short>(contador - 1);

    Estado e = Estado::Midiendo;

    std::cout << etiqueta.substr(0, 5) << "\n";
    std::cout << etiqueta.find("HORNO") << "\n";
    std::cout << etiqueta.length() << "\n";
    std::cout << contador << "\n";
    std::cout << static_cast<int>(e) << "\n";
    return 0;
}
```

Escriba las cinco líneas de salida. Para la cuarta, explique de dónde sale ese número y qué habría impreso si `contador` fuera `short` en lugar de `unsigned short`. Para la quinta, diga por qué hace falta el `static_cast` y qué error da si se quita.

### 03.2 · Aplicar

**Armar la etiqueta de un canal**

El sistema nombra sus canales pegando tres pedazos: el tipo de sensor, el número de canal y la zona. Para el termopar cuatro del horno los pedazos son `"TC"`, `"04"` y `"HORNO"`.

Escriba un programa que:

- guarde los tres pedazos en variables `std::string` separadas y arme la etiqueta completa con guiones de por medio,
- declare `enum class Escala { Celsius, Kelvin }` y un alias `using Temperatura = double;`,
- guarde 373.15 en una variable del tipo `Temperatura`,
- imprima la etiqueta, su longitud, sus dos primeros caracteres, la posición del segundo guion buscando a partir del índice 3, el valor entero de `Escala::Kelvin` y la temperatura.

Salida esperada, en ese orden: `TC-04-HORNO`, `11`, `TC`, `5`, `1`, `373.15`.

### 03.3 · Integrar

**Del ADC a grados, con la ficha del canal**

El convertidor analógico digital es de 12 bits, así que su cuenta va de 0 a 4095, y su referencia es de 3.3 V. El sensor entrega 0.5 V a cero grados y sube 0.01 V por cada grado. La cuenta que llegó es 2867.

Escriba un programa que calcule el voltaje y la temperatura, con las cuatro constantes declaradas con `const` y con la conversión de tipos explícita donde haga falta. Además, guarde la ficha del canal en un `std::string` con el texto `ADC-12 canal 3` e imprima de él solo la palabra `canal`, sacada con `substr`. Cierre imprimiendo cuántos bytes ocupan un `int` y un `double` en esta plataforma. La salida esperada:

```
ADC-12 canal 3
canal
2.3104 V
181.04 C
4 8
```

---

## Semana 04 · Unidad 3 · Funciones definidas por el usuario I

### 04.1 · Reconocer

**Tres funciones de conversión y un parámetro que no cambia**

```cpp
#include <iostream>

double celsius(double f);
double kelvin(double c);
double duplicar(double x);

int main()
{
    double lecturaF = 212.0;

    double c = celsius(lecturaF);
    double k = kelvin(c);

    double margen = 2.5;
    duplicar(margen);

    std::cout << c << " " << k << "\n";
    std::cout << margen << "\n";
    return 0;
}

double celsius(double f)
{
    return (f - 32.0) * 5.0 / 9.0;
}

double kelvin(double c)
{
    return c + 273.15;
}

double duplicar(double x)
{
    x = x * 2.0;
    return x;
}
```

Escriba las dos líneas de salida. Después conteste: por qué `margen` vale lo que vale después de la llamada, qué error reporta el compilador si se borra el prototipo de `kelvin` de la línea 4, y en qué se distingue el parámetro `c` de la función `kelvin` de la variable `c` que está en `main`.

### 04.2 · Aplicar

**Deflexión de una viga en voladizo**

Una viga en voladizo de sección rectangular tiene base 0.04 m y altura 0.06 m, mide 1.2 m de largo y es de acero, con módulo de Young de 200 GPa. Se le cuelga una carga de 800 N en la punta. La deflexión en el extremo es `F L³ / (3 E I)`, y el segundo momento de área de la sección rectangular es `b h³ / 12`.

Escriba el programa con cuatro funciones, cada una con su prototipo antes de `main` y su definición después: una que eleve al cubo, una que calcule el segundo momento de área, una que calcule la deflexión en metros y una que convierta metros a milímetros. `main` no hace ninguna cuenta, solo llama e imprime.

```
Inercia: 7.2e-07 m4
Deflexion: 0.0032 m
Deflexion: 3.2 mm
```

### 04.3 · Integrar

**Cadena de conversión del canal 3**

Retome los datos del ejercicio 03.3, ahora repartidos en funciones. Escriba tres funciones con prototipo: una que reciba la cuenta, la cuenta máxima y el voltaje de referencia y devuelva el voltaje; otra que reciba el voltaje, el voltaje a cero grados y la pendiente y devuelva la temperatura; y otra que reciba dos `std::string` y devuelva la etiqueta unida con un guion.

Con cuenta 2867, cuenta máxima 4095, referencia 3.3 V, cero en 0.5 V y pendiente de 0.01 V por grado, y con los pedazos `"TC"` y `"HORNO"`, la salida es:

```
TC-HORNO
8
2.3104 V
181.04 C
```

Ninguna de las tres funciones puede imprimir nada, y `main` no puede calcular nada.

---

## Semana 05 · Unidad 4 · Funciones definidas por el usuario II

### 05.1 · Reconocer

**Un contador que sobrevive y una global tapada**

```cpp
#include <iostream>

int muestras = 0;

void registrar(double v)
{
    static int llamadas = 0;
    int muestras = 100;

    llamadas = llamadas + 1;
    muestras = muestras + 1;

    std::cout << llamadas << " " << muestras << "\n";
}

void escalar(double& v, double factor = 2.0)
{
    v = v * factor;
}

int main()
{
    double lectura = 3.5;

    registrar(lectura);
    registrar(lectura);

    escalar(lectura);
    escalar(lectura, 10.0);

    std::cout << lectura << " " << muestras << "\n";
    return 0;
}
```

Escriba las tres líneas de salida. Explique por qué la segunda columna repite el mismo número en las dos primeras líneas mientras la primera columna avanza, y por qué la variable global `muestras` termina como empezó aunque dentro de `registrar` haya una línea que la suma.

### 05.2 · Aplicar

**Resumen de vibración por referencia**

El canal VIB-02 mide velocidad de vibración en mm/s. En la primera tanda entregó 2.4, 3.1 y 2.8. En la segunda entregó esas tres y una cuarta de 3.6.

Escriba una función `void` que reciba el nombre del canal por referencia constante, las tres lecturas por valor, y devuelva la suma y la media en dos parámetros por referencia. Agregue un último parámetro con valor por omisión `"mm/s"` para la unidad. La función imprime una línea con el canal, cuántas muestras procesó y la unidad, y nada más. Sobrecárguela con una segunda versión que acepte cuatro lecturas.

`main` llama a las dos y luego imprime la suma y la media de cada una. La primera llamada deja que la unidad tome su valor por omisión y la segunda le pasa `"mm/s rms"`.

```
VIB-02 3 muestras mm/s
8.3 2.76667
VIB-02 4 muestras mm/s rms
11.9 2.975
```

### 05.3 · Integrar

**La viga, ahora con referencias y sobrecarga**

Tome el programa de la viga del ejercicio 04.2 y cámbielo por completo a esta forma:

- una función `void` que reciba carga, largo, módulo y segundo momento de área, y entregue la deflexión en metros y en milímetros por dos parámetros de referencia,
- una segunda versión sobrecargada que reciba base y altura en lugar del segundo momento de área, lo calcule y delegue en la primera,
- una función aparte con una variable `static` que lleve la cuenta de cuántos cálculos se han pedido, y que la primera versión llama para imprimir el número de cálculo.

`main` llama primero a la versión que recibe `7.2e-7` directo y luego a la que recibe 0.04 y 0.06, y con carga de 800 N, largo de 1.2 m y 200 GPa las dos dan lo mismo:

```
calculo 1
0.0032 m 3.2 mm
calculo 2
0.0032 m 3.2 mm
```

Explique en tres renglones por qué el contador llega a 2 y no a 3, aunque la segunda llamada pase por las dos funciones.

---

## Semana 06 · Unidad 5 · Clases y abstracción de datos

### 06.1 · Reconocer

**Un sensor de presión con datos privados**

```cpp
class SensorPresion {
public:
    SensorPresion(std::string e, double k) { etiqueta = e; kpa = k; }
    std::string getEtiqueta() { return etiqueta; }
    double getKpa() { return kpa; }
    double enBar() { return kpa / 100.0; }
    void setKpa(double k) { kpa = k; }
private:
    std::string etiqueta;
    double kpa;
};

int main()
{
    SensorPresion s("PT-07", 250.0);

    std::cout << s.getEtiqueta() << "\n";
    std::cout << s.getKpa() << "\n";
    std::cout << s.enBar() << "\n";

    s.setKpa(101.3);
    std::cout << s.enBar() << "\n";
    return 0;
}
```

Escriba las cuatro líneas de salida. Después diga qué pasa si en `main` se agrega la línea `s.kpa = 300.0;`, con la clave de error exacta y en qué momento aparece, y qué otra línea del programa hace lo mismo que esa pero sí compila.

### 06.2 · Aplicar

**La viga convertida en clase**

Escriba una clase `Viga` que guarde como miembros privados la clave, la base, la altura, el largo y el módulo de Young. El constructor recibe los cinco valores. La clase expone tres funciones miembro públicas: la clave, el segundo momento de área y la deflexión en milímetros para una carga que se recibe como argumento.

`main` crea dos vigas de la misma sección de base pero distinta altura, VG-01 con 0.04 por 0.06 y VG-02 con 0.04 por 0.08, las dos de 1.2 m y 200 GPa, y pide la deflexión de las dos con 800 N.

```
VG-01 7.2e-07 3.2
VG-02 1.70667e-06 1.35
```

Ningún miembro de datos puede ser público y `main` no puede hacer ninguna cuenta. Sin `if` y sin ciclos.

### 06.3 · Integrar

**La viga que reporta dos resultados**

Amplíe la clase de 06.2 con una función miembro `reportar` que reciba dos parámetros por referencia, uno para la deflexión en milímetros y otro para el segundo momento de área, y un tercer parámetro con valor por omisión de 800.0 para la carga. La función imprime una sola línea con la clave y la carga usada, y deja los dos resultados en los parámetros de referencia.

`main` declara la viga VG-01 con 0.04, 0.06, 1.2 y 200 GPa, llama a `reportar` sin dar carga, imprime lo que recibió, y vuelve a llamar con 1200 N.

```
VG-01 con 800 N
7.2e-07 m4 3.2 mm
VG-01 con 1200 N
7.2e-07 m4 4.8 mm
```

Explique en dos renglones por qué el segundo momento de área no cambió entre las dos llamadas y la deflexión sí.

---

## Semana 07 · Unidad 6 · Estructuras de control I

### 07.1 · Reconocer

**Cuatro trampas en una sola corrida**

```cpp
int main()
{
    double presion = 250.0;
    int codigo = 2;
    int alarmas = 0;

    if (alarmas = 1)
        std::cout << "A";
    else
        std::cout << "B";

    double suma = 0.1 + 0.2;

    if (suma == 0.3)
        std::cout << "C";
    else
        std::cout << "D";

    switch (codigo)
    {
    case 1: std::cout << "kPa";
    case 2: std::cout << "bar";
    case 3: std::cout << "psi"; break;
    default: std::cout << "?";
    }

    std::cout << "\n" << alarmas << " " << presion << "\n";
    return 0;
}
```

Escriba las dos líneas de salida, carácter por carácter. Después señale las tres decisiones que no hicieron lo que aparentan y, para cada una, la corrección mínima: una letra en la primera, una comparación distinta en la segunda y una palabra en la tercera.

### 07.2 · Aplicar

**Clasificador de temperatura y tabla de unidades**

Escriba tres funciones:

- `clasificar` recibe una temperatura en grados Celsius y devuelve un `std::string`: `bajo` abajo de cero, `normal` hasta 120 inclusive, `alto` hasta 300 inclusive y `critico` arriba de eso. Se resuelve con un `if-else` encadenado.
- `unidad` recibe un código entero y devuelve la unidad con un `switch`: 1 es `C`, 2 es `kPa`, 3 es `um/m` y cualquier otro es `?`.
- `calibrado` recibe la lectura, el patrón y una tolerancia, y devuelve `bool`. Está calibrado si la lectura cae dentro de la tolerancia alrededor del patrón, sin comparar reales con igualdad exacta.

`main` prueba `clasificar` con 87.5, -4.0 y 310.0, `unidad` con 1, 2 y 9, y `calibrado` con 99.97 y con 100.2 contra un patrón de 100.0 y tolerancia de 0.05.

```
normal
bajo
critico
C kPa ?
1 0
```

### 07.3 · Integrar

**El termopar que se defiende**

Escriba una clase `Termopar` con etiqueta, temperatura en grados Celsius y un contador de rechazos, los tres privados. El mutador acepta valores entre -200 y 1300 grados; fuera de ese rango no toca el dato, suma un rechazo e imprime `rechazado` seguido del valor. Agregue una función miembro `estado` que devuelva un `char`: `B` abajo de cero, `N` hasta 120, `A` hasta 300 y `C` arriba.

Escriba aparte una función libre que reciba un número de opción y el termopar por referencia, y que con un `switch` de cuatro casos imprima la temperatura, el estado, el número de rechazos o el aviso de opción inválida.

`main` asigna 87.5, luego intenta asignar 1500.0, y llama a la función con las opciones 1, 2, 3 y 7.

```
rechazado 1500
87.5
N
1
opcion invalida
```

La validación tiene que vivir dentro de la clase. Si `main` revisa el rango antes de llamar al mutador, el ejercicio no cuenta.

---

## Semana 08 · Unidad 6 · Estructuras de control II

### 08.1 · Reconocer

**Rejilla de 3 por 4 con un continue**

```cpp
int main()
{
    int celdas = 0;
    int suma = 0;

    for (int fila = 1; fila <= 3; fila++)
    {
        for (int col = 1; col <= 4; col++)
        {
            if (col == 3)
                continue;
            celdas++;
            suma = suma + fila * col;
        }
    }

    int intentos = 0;
    int codigo = 5;

    do
    {
        intentos++;
        codigo = codigo - 2;
    } while (codigo > 5);

    std::cout << celdas << " " << suma << "\n";
    std::cout << intentos << " " << codigo << "\n";
    return 0;
}
```

Escriba las dos líneas de salida y, junto a la primera, cuántas veces corrió el cuerpo del ciclo interno en total y cuántas se saltó. Para la segunda, diga cuántas veces habría impreso el mismo bloque escrito como `while` con esa misma condición, y por qué.

### 08.2 · Aplicar

**Calentamiento de primer orden, paso a paso**

Una termorresistencia arranca a 20 °C y se mete a un horno que está a 100 °C. Su respuesta es de primer orden con constante de tiempo de 5 s. Con paso de 1 s, la temperatura del siguiente instante se calcula como `T = T + (dt / tau) * (Tamb - T)`.

Escriba un programa con un `while` que avance paso por paso, imprima el número de paso y la temperatura de cada uno, se detenga con `break` en cuanto la temperatura pase de 90 °C, y no pase de veinte pasos en ningún caso. Al final imprime cuántos pasos hicieron falta.

Las tres primeras líneas y la última son:

```
1 36
2 48.8
3 59.04
...
pasos 10
```

El valor 100.0, el 5.0, el 1.0 y el 90.0 van en constantes con nombre. Ningún número suelto dentro del ciclo.

### 08.3 · Integrar

**Repaso del primer parcial: ocho pasos y una lectura imposible**

Este ejercicio cruza todo lo que entra al primer parcial, de la unidad 1 a la unidad 6, y no trae material nuevo.

El banco simula la temperatura del paso `k` con la fórmula `20.0 + 9.5 * k`, para `k` de 1 a 8. Escriba:

- una función que reciba el número de paso y devuelva esa temperatura,
- una clase `Termopar` con etiqueta y límite de alarma en el constructor, y con una función miembro `registrar` que descarte cualquier valor fuera del rango de -200 a 1300 grados imprimiendo `fuera de rango` y el valor, y que en caso contrario acumule la suma, aumente el conteo y sume una alarma si el valor pasa del límite,
- accesores para el conteo, la media, el número de alarmas y la etiqueta.

`main` recorre los ocho pasos con un `for`, imprime el paso y la lectura de cada uno, después intenta registrar 1500.0, y cierra con el resumen. Con TC-04 y límite de 80 grados:

```
1 29.5
...
8 96
fuera de rango 1500
TC-04
aceptadas 8
media 62.75
alarmas 2
```

---

## Semana 09 · Unidad 7 · Herencia y composición

### 09.1 · Reconocer

**Termopar que hereda de Sensor**

```cpp
class Sensor {
public:
    Sensor(std::string e) { etiqueta = e; }
    std::string getEtiqueta() { return etiqueta; }
    double aUnidades(int cuenta) { return cuenta * 1.0; }
protected:
    std::string etiqueta;
};

class Termopar : public Sensor {
public:
    Termopar(std::string e, double p) : Sensor(e), pendiente(p) {}
    double aUnidades(int cuenta) { return cuenta * pendiente; }
    std::string describir() { return etiqueta + " tipo K"; }
private:
    double pendiente;
};

int main()
{
    Termopar t("TC-04", 0.25);

    std::cout << t.getEtiqueta() << "\n";
    std::cout << t.describir() << "\n";
    std::cout << t.aUnidades(400) << "\n";

    Sensor s("PT-07");
    std::cout << s.aUnidades(400) << "\n";
    return 0;
}
```

Escriba las cuatro líneas de salida. Conteste además: por qué `describir` puede usar `etiqueta` sin ningún accesor, qué error da si `main` escribe `t.etiqueta`, y qué pasa si se borra `Sensor(e)` de la lista de inicialización del constructor de `Termopar`.

### 09.2 · Aplicar

**Dos sensores que heredan y un canal que compone**

Escriba una clase base `Sensor` con etiqueta y unidad protegidas y accesores públicos. De ella derive dos clases:

- `Termopar`, que guarda pendiente y voltaje a cero grados, tiene unidad `C`, y convierte volts a grados con `(volts - cero) / pendiente`,
- `Extensometro`, que guarda el factor de galga, tiene unidad `um/m`, y convierte una razón de deformación a micrómetros por metro con `razon / factor * 1000000.0`.

Escriba después una clase `Canal` que no herede de nadie y que tenga un `Termopar` como miembro, más un número de canal, y una función miembro que reciba el voltaje e imprima el número, la etiqueta, el valor convertido y la unidad.

`main` crea el termopar TC-04 con pendiente 0.01 y cero en 0.5, el extensómetro SG-11 con factor 2.05, y el canal 3 con el termopar adentro.

```
TC-04 181 C
SG-11 100 um/m
3 TC-04 181 C
```

Cierre con un comentario de tres renglones que aplique la prueba de la frase a las dos decisiones: por qué `Termopar` hereda y por qué `Canal` no.

### 09.3 · Integrar

**Banco de pruebas con un termopar adentro**

Escriba una clase `BancoDePruebas` que tenga como miembros un nombre, un `Termopar` por composición y un límite de alarma, más los acumuladores que necesite. Su función miembro `medir` recibe el voltaje, lo convierte con el sensor que trae adentro, acumula, y imprime `ALARMA` con la etiqueta y el valor si pasa del límite, o `ok` con los mismos datos si no.

`main` arma el termopar TC-04 con pendiente 0.01 y cero en 0.5, crea el banco `Horno 2` con límite de 120 grados, y recorre con un `for` cinco voltajes generados como `1.0 + 0.4 * k` con `k` de 0 a 4. Al final imprime el nombre del banco, la media de todo lo medido y el número de alarmas.

```
ok TC-04 50
ok TC-04 90
ALARMA TC-04 130
ALARMA TC-04 170
ALARMA TC-04 210
Horno 2
media 130
alarmas 3
```

---

## Semana 10 · Unidad 8 · Arreglos y cadenas

### 10.1 · Reconocer

**Seis lecturas, dos guiones y un tamaño calculado**

```cpp
int main()
{
    int lecturas[6] = {118, 121, 117, 123, 119, 130};
    int n = sizeof(lecturas) / sizeof(lecturas[0]);

    int suma = 0;
    for (int i = 0; i < n; i++)
        suma = suma + lecturas[i];

    std::string etiqueta = "SG-11-VIGA";
    int guiones = 0;
    for (int i = 0; i < static_cast<int>(etiqueta.length()); i++)
        if (etiqueta.at(i) == '-')
            guiones++;

    std::cout << n << " " << suma << "\n";
    std::cout << lecturas[n - 1] << " " << guiones << "\n";
    return 0;
}
```

Escriba las dos líneas de salida. Después conteste: qué imprimiría la segunda línea si dijera `lecturas[n]` en lugar de `lecturas[n - 1]`, si el programa fallaría al correr, y qué pasa con `n` si ese mismo cálculo de `sizeof` se hace dentro de una función que recibe el arreglo como parámetro.

### 10.2 · Aplicar

**Estadísticas de ocho deformaciones**

Un extensómetro sobre la viga entregó ocho lecturas de deformación, en micrómetros por metro: 118, 121, 117, 123, 119, 130, 112 y 126.

Escriba un programa que guarde las ocho en un arreglo, calcule el número de elementos con `sizeof`, y con un solo recorrido obtenga la suma, la lectura mayor y la menor. Después, con un segundo recorrido, cuente cuántas están arriba de la media.

```
n 8
media 120.75
mayor 130
menor 112
rango 18
arriba 4
```

Ningún ciclo puede llevar el número 8 escrito a mano. Cambiar el arreglo a nueve lecturas no debe obligar a tocar ninguna otra línea.

### 10.3 · Integrar

**Las mismas ocho lecturas, repartidas en funciones**

Reescriba 10.2 con cuatro funciones y un `main` que solo llame e imprima:

- `media` recibe el arreglo como `const int datos[]` y su tamaño, y devuelve un `double`,
- `extremos` recibe lo mismo y entrega el mayor y el menor por dos parámetros de referencia,
- `contarSobre` recibe el arreglo, el tamaño y un umbral, y devuelve cuántos lo pasan,
- `contarDigitos` recibe un `const std::string&` y devuelve cuántos de sus caracteres son dígitos.

Con las mismas ocho lecturas y la etiqueta `SG-11-VIGA-A3`:

```
SG-11-VIGA-A3 13 3
media 120.75
mayor 130 menor 112
sobre la media 4
sobre 125 2
```

Explique en dos renglones por qué las funciones reciben el tamaño como parámetro en lugar de calcularlo adentro.

---

## Semana 11 · Unidad 9 · Registros

### 11.1 · Reconocer

**Copiar un registro y medir cuánto ocupa**

```cpp
struct Muestra {
    int t_ms;
    double valor;
};

int main()
{
    Muestra a;
    a.t_ms = 100;
    a.valor = 2.5;

    Muestra b = a;
    b.valor = 9.9;

    Muestra tabla[3];
    tabla[0] = a;
    tabla[1] = b;
    tabla[2].t_ms = 300;
    tabla[2].valor = 1.25;

    std::cout << a.valor << " " << b.valor << "\n";
    std::cout << tabla[1].t_ms << " " << tabla[2].valor << "\n";
    std::cout << sizeof(Muestra) << " " << sizeof(tabla) << "\n";
    return 0;
}
```

Escriba las tres líneas de salida. La tercera tiene un número que no es la suma de los tamaños de los campos: diga cuál es la suma, cuál se imprime y por qué el compilador decidió eso. Diga también qué campo de `tabla[2]` quedó con basura si se imprimiera antes de las dos asignaciones.

### 11.2 · Aplicar

**Seis muestras con marca de tiempo**

El adquisidor guarda pares de tiempo y voltaje. La corrida de hoy dejó estos seis: (0, 2.41), (100, 2.65), (200, 3.12), (300, 2.98), (400, 3.44) y (500, 3.05), con el tiempo en milisegundos.

Escriba un `struct Muestra` con los dos campos, una función `crear` que reciba los dos valores y devuelva la muestra armada, y un `main` que llene un arreglo de seis llamando a esa función. Con un solo recorrido calcule la suma y el índice de la muestra de mayor valor. Imprima la tabla completa separada con tabuladores, la media y el máximo con su marca de tiempo.

```
t_ms	valor
0	2.41
...
500	3.05
media 2.94167
maximo 3.44 en 400 ms
```

### 11.3 · Integrar

**La tabla con una muestra inválida**

Repita la tabla de 11.2, pero la muestra de los 200 ms llegó como -1.00, que es imposible en este canal. Escriba:

- `valida`, que recibe un `const Muestra&` y devuelve `false` si el tiempo es negativo o el valor no es mayor que cero,
- `mediaValidas`, que recibe la tabla como `const Muestra tabla[]`, el tamaño y un parámetro de referencia donde deja cuántas usó, imprime `descartado` con la marca de tiempo de cada rechazo, y devuelve la media de las que sobrevivieron,
- `extremos`, que deja en dos parámetros de referencia los índices de la mayor y la menor entre las válidas.

```
descartado 200 ms
registros 6 validos 5
media 2.906
maximo 3.44 en 400 ms
minimo 2.41 en 0 ms
```

Explique en dos renglones por qué las funciones reciben la tabla por referencia constante y no por valor.

---

## Semana 12 · Unidad 10 · Punteros, virtuales y abstractas

### 12.1 · Reconocer

**Un puntero, una virtual y una que no lo es**

```cpp
class Sensor {
public:
    virtual double convertir(int cuenta) { return cuenta * 1.0; }
    double escala() { return 1.0; }
    virtual ~Sensor() {}
};

class Termopar : public Sensor {
public:
    double convertir(int cuenta) override { return cuenta * 0.25; }
    double escala() { return 0.25; }
};

int main()
{
    int cuenta = 400;
    int* p = &cuenta;

    *p = 800;

    Termopar t;
    Sensor* s = &t;

    std::cout << cuenta << " " << (p == &cuenta) << "\n";
    std::cout << s->convertir(cuenta) << " " << s->escala() << "\n";

    Sensor* d = new Termopar();
    std::cout << d->convertir(100) << "\n";
    delete d;
    return 0;
}
```

Escriba las tres líneas de salida. La segunda tiene dos números que salen de dos funciones casi idénticas de la misma clase: explique quién decide cuál corre en cada caso y en qué momento se toma esa decisión. Diga también qué se fuga si se borra la línea del `delete`, y qué se fuga distinto si en lugar de eso se le quita el `virtual` al destructor.

### 12.2 · Aplicar

**Tres canales por un arreglo de punteros**

Escriba una clase abstracta `Sensor` con etiqueta protegida, dos funciones virtuales puras, una que convierta una cuenta a unidades de ingeniería y otra que devuelva la unidad, un accesor para la etiqueta y destructor virtual. Derive `Termopar`, que multiplica la cuenta por su pendiente y reporta `C`, y `Extensometro`, que divide la cuenta entre su factor y reporta `um/m`.

`main` declara un arreglo de tres punteros a `Sensor`, los llena con `new` con TC-04 de pendiente 0.25, SG-11 de factor 2.05 y TC-05 de pendiente 0.50, y recorre con un solo ciclo las cuentas 400, 410 y 300, imprimiendo etiqueta, valor y unidad, y contando cuántos pasan de 120. Al final libera los tres.

```
TC-04 100 C
SG-11 200 um/m
TC-05 150 C
sobre 120: 2
```

Ni un solo `if` que pregunte de qué tipo es cada objeto. Si aparece uno, falta un `virtual`.

### 12.3 · Integrar

**Los mismos canales sin un solo delete**

Reescriba 12.2 con dos cambios. El arreglo de punteros crudos se vuelve un arreglo de `std::unique_ptr<Sensor>` construidos con `std::make_unique`, y las muestras dejan de estar sueltas: use un `struct Muestra` con marca de tiempo y cuenta, reservado con `new Muestra[4]` y liberado con `delete[]`, lleno en un ciclo con tiempos de 0 a 300 ms de cien en cien y cuentas de 400 a 460 de veinte en veinte.

Para cada uno de los dos canales, TC-04 con pendiente 0.25 y SG-11 con factor 2.05, imprima la media de las cuatro muestras convertidas.

```
TC-04 media 107.5 C
SG-11 media 209.756 um/m
```

Termine imprimiendo cuántos `new` quedaron sin su pareja, y explique en tres renglones qué líneas de la versión anterior desaparecieron al cambiar a `unique_ptr`.

---

## Semana 13 · Unidad 11 · Entrada y salida

### 13.1 · Reconocer

**El ciclo con eof y el archivo que no está**

```cpp
std::ofstream out("bitacora.txt");
out << "TC-04 100 2.41\n";
out << "TC-04 200 2.65\n";
out << "TC-04 300 3.12\n";
out.close();

std::ifstream in("bitacora.txt");
std::string etiqueta;
int t = 0;
double v = 0.0;
int lineas = 0;

while (!in.eof())
{
    in >> etiqueta >> t >> v;
    std::cout << t << " " << v << "\n";
    lineas++;
}
in.close();

std::cout << "lineas " << lineas << "\n";

std::ifstream falta("no_existe.txt");
int n = 7;
falta >> n;

std::cout << falta.is_open() << " " << n << "\n";
```

El archivo tiene tres renglones. Escriba todo lo que imprime el programa, que son seis líneas. Explique por qué el conteo no da 3, de dónde salen los valores de la línea repetida, y por qué la lectura del archivo inexistente deja a `n` como estaba en lugar de ponerlo en cero. Escriba la condición del ciclo que arregla el primer problema.

### 13.2 · Aplicar

**Bitácora del horno, escrita y leída**

Escriba un programa que cree el archivo `horno.txt` con seis renglones, cada uno con la etiqueta `TC-04`, la marca de tiempo en milisegundos y la temperatura: (0, 21.5), (100, 48.2), (200, 76.9), (300, 98.4), (400, 121.7) y (500, 133.0). Ciérrelo, vuelva a abrirlo para lectura y recórralo completo sin saber de antemano cuántos registros trae, usando la lectura misma como condición del ciclo.

El programa revisa `is_open` después de abrir, tanto al escribir como al leer, y si falla imprime un aviso y termina con código 1. Al final reporta cuántos registros leyó, la media de las temperaturas y cuántas pasaron de 100 grados.

```
registros 6
media 83.2833
sobre 100 C 2
```

### 13.3 · Integrar

**Repaso del segundo parcial: del archivo al reporte**

Este ejercicio cruza lo que entra al segundo parcial, de la unidad 1 a la unidad 11, y no trae material nuevo.

Escriba un programa que genere `banco.txt` con seis renglones de etiqueta, tiempo y temperatura, donde el tercero trae 9999.0 porque el canal se desconectó. Después:

- declare un `struct Registro` con los tres campos y un arreglo de diez,
- lea el archivo dentro de un ciclo que se detenga por el fin del archivo o por llenar el arreglo, lo que ocurra primero, revisando `is_open` antes,
- pase cada registro a una clase `Canal` que descarte lo que caiga fuera del rango de -200 a 1300 grados, acumule lo demás y cuente las alarmas arriba de 100 grados,
- imprima el resumen.

```
TC-04
leidos 6
aceptados 5
descartados 1
media 84.56
alarmas 2
```

La clase no lee el archivo y `main` no valida rangos. Cada quien hace una cosa.

---

## Semana 14 · Unidad 12 · Sobrecarga y plantillas

### 14.1 · Reconocer

**Suma de fuerzas y dos versiones de una plantilla**

```cpp
class Fuerza {
public:
    Fuerza(double a, double b) : x(a), y(b) {}
    Fuerza operator+(Fuerza o) { return Fuerza(x + o.x, y + o.y); }
    bool operator==(Fuerza o) { return x == o.x && y == o.y; }
    double x;
    double y;
};

template <typename T>
T mayor(T a, T b)
{
    if (a > b)
        return a;
    return b;
}

int main()
{
    Fuerza f1(120.0, 45.0);
    Fuerza f2(30.5, 15.0);

    Fuerza suma = f1 + f2;

    std::cout << suma.x << " " << suma.y << "\n";
    std::cout << (suma == Fuerza(150.5, 60.0)) << "\n";
    std::cout << mayor(3, 9) << " " << mayor(2.5, 1.5) << "\n";
    return 0;
}
```

Escriba las tres líneas de salida. Diga cuántas funciones concretas genera el compilador a partir de la plantilla en este programa y con qué tipos, qué queda de la plantilla en el ejecutable, y qué error aparece si alguien agrega la llamada `mayor(f1, f2)`.

### 14.2 · Aplicar

**Una medición que se suma, se compara y se imprime**

Escriba una clase `Medicion` con un valor `double` y una unidad `std::string`, las dos privadas. Sobrecargue como funciones miembro la suma, que devuelve una medición nueva con la unidad de la izquierda, la igualdad, que compara valor y unidad, y el mayor que, que compara solo el valor. Sobrecargue además el operador de salida como función libre, para que `cout` imprima el valor y la unidad separados por un espacio.

Escriba dos plantillas: `mayor`, que devuelve el mayor de dos valores de cualquier tipo, y `promedio`, que recibe un arreglo de cualquier tipo y su tamaño y devuelve un `double`.

`main` usa las mediciones de 120.5 kPa y 98.3 kPa, el arreglo de presiones {120.5, 98.3, 105.0, 111.4} y el de cuentas {400, 410, 300}.

```
218.8 kPa
0 1
120.5 kPa
7 9.75
108.8
370
```

### 14.3 · Integrar

**Un búfer que sirve para cualquier tipo**

Escriba una plantilla de clase `Buffer` con capacidad fija de 5, declarada en una constante global. Guarda los elementos en un arreglo interno, lleva la cuenta de cuántos tiene, y expone tres funciones: agregar, que imprime `buffer lleno` y no guarda nada cuando ya no cabe; obtener por índice; y tamaño.

Pruébela dos veces. Primero con `Buffer<double>` y los voltajes 2.41, 2.65 y 3.12, imprimiendo cuántos guardó y su media. Después con `Buffer<Muestra>`, donde `Muestra` es el registro de la semana 11 con marca de tiempo y valor, metiendo seis muestras generadas con tiempos de cien en cien y valores `2.41 + 0.25 * i`. Sobrecargue el operador de salida para `Muestra` y recorra el búfer imprimiendo cada una.

```
volts 3 media 2.72667
buffer lleno
registro 5
0 ms 2.41
...
400 ms 3.41
```

Explique en dos renglones por qué el mensaje de búfer lleno aparece antes que el conteo del registro.

---

## Semana 15 · Unidad 13 · Manejo de excepciones

### 15.1 · Reconocer

**En qué orden imprime y quién atrapa qué**

```cpp
double razon(double a, double b)
{
    if (b == 0.0)
        throw std::invalid_argument("divisor cero");
    return a / b;
}

int main()
{
    std::string etiqueta = "TC-04";

    try
    {
        std::cout << "A";
        std::cout << razon(10.0, 4.0) << " ";
        std::cout << etiqueta.at(9) << " ";
        std::cout << "B";
    }
    catch (const std::out_of_range&)
    {
        std::cout << "C";
    }
    catch (const std::exception&)
    {
        std::cout << "D";
    }

    std::cout << "E\n";

    try
    {
        std::cout << razon(10.0, 0.0) << "\n";
    }
    catch (const std::exception& e)
    {
        std::cout << e.what() << "\n";
    }
}
```

Escriba las dos líneas de salida, carácter por carácter. Explique qué pasó con la `B`, cuál de los dos `catch` atrapó el problema del primer bloque y por qué el otro no, y por qué el segundo bloque sí atrapa una `invalid_argument` con un `catch` que dice `exception`.

### 15.2 · Aplicar

**La calibración que se niega a existir mal**

Escriba una clase `Calibracion` con etiqueta, pendiente y voltaje a cero grados. Si el constructor recibe pendiente cero, lanza `std::invalid_argument` con un mensaje que incluya la etiqueta, porque una pendiente de cero no define ninguna conversión. Agregue la función miembro que convierte volts a grados.

Escriba aparte una función libre `resistencia` que reciba volts y amperes y lance `std::runtime_error` si la corriente es cero.

`main` hace tres intentos, cada uno en su propio bloque `try`: crea la calibración buena TC-04 con pendiente 0.01 y cero en 0.5 y convierte 2.31 V; intenta crear TC-09 con pendiente 0.0; y calcula la resistencia con 12 V a 0.5 A y luego con 12 V a 0 A. El programa nunca termina de golpe.

```
TC-04 181 C
error: pendiente cero en TC-09
24 ohm
error: corriente cero, no hay resistencia que medir
el programa sigue
```

Todos los `catch` reciben por referencia constante. La clase detecta y `main` decide.

### 15.3 · Integrar

**Un lote con una línea corta**

El archivo `lote.txt` trae cuatro renglones con etiqueta y temperatura. La etiqueta normal lleva la zona en la posición 6, como en `TC-04-A`, pero el tercer renglón se grabó como `TC-04`, sin zona. El programa escribe ese archivo antes de leerlo, con los renglones `TC-04-A 21.5`, `TC-04-B 48.2`, `TC-04 76.9` y `TC-04-C 98.4`.

Escriba una función que reciba un `std::ifstream&` por referencia y una ruta, abra el archivo y lance `std::runtime_error` si no se pudo abrir. En `main`, recorra el archivo con la lectura como condición y, dentro del ciclo, saque la zona con `at`. La línea corta lanza `std::out_of_range`, que se atrapa dentro del mismo ciclo, se reporta y no detiene la lectura del resto. Al final, un segundo bloque intenta abrir `no_existe.txt` para ver la otra excepción.

La media que se reporta al final es la de las tres temperaturas que sí se pudieron leer:

```
zona A 21.5
zona B 48.2
linea mal formada: TC-04
zona C 98.4
buenas 3 malas 1
media 56.0333
error: no se pudo abrir no_existe.txt
```

---

## Semana 16 · Unidad 14 · Recursión y concurrencia

### 16.1 · Reconocer

**Tres recursiones y una que no termina**

```cpp
int suma(int n)
{
    if (n <= 0)
        return 0;
    return n + suma(n - 1);
}

int pasos(int n)
{
    if (n <= 1)
        return 0;
    return 1 + pasos(n / 2);
}

double potencia(double base, int exp)
{
    if (exp == 0)
        return 1.0;
    return base * potencia(base, exp - 1);
}

int main()
{
    std::cout << suma(5) << "\n";
    std::cout << pasos(64) << "\n";
    std::cout << potencia(2.0, 10) << "\n";
    return 0;
}
```

Escriba las tres líneas de salida. Para `pasos(64)`, dibuje la cadena de llamadas con el valor de `n` en cada una y diga cuántos marcos llegan a estar vivos al mismo tiempo. Después conteste qué le ocurre a `potencia` si se llama con exponente -1, y por qué eso no se cuelga como un ciclo infinito sino que termina el programa.

### 16.2 · Aplicar

**Búsqueda binaria recursiva y un contador con candado**

La tabla de calibración del ADC está ordenada: 512, 1024, 1536, 2048, 2560, 3072, 3584 y 4095.

Escriba una función recursiva que reciba el arreglo, el índice izquierdo, el derecho y el valor buscado, y devuelva el índice donde está o -1 si no está. Escriba también una función recursiva que sume un arreglo de `double` sin usar ningún ciclo. Pruébelas buscando 2560, buscando 2600, y sumando los voltajes 2.41, 2.65, 3.12, 2.98 y 3.44.

Cierre con la parte de concurrencia: una variable global `long long`, un `std::mutex`, y una función que la incremente cien mil veces tomando el candado con `std::lock_guard` en cada vuelta. Lance dos `std::jthread` sobre esa función dentro de un bloque, y al salir del bloque imprima el total.

```
4
-1
14.6
200000
```

Corra después la misma prueba quitando el `lock_guard`, tres veces seguidas, y anote los tres totales que le salieron. Explique en tres renglones por qué ninguno coincide con el otro y por qué la versión con candado siempre da el mismo número.

### 16.3 · Integrar

**Repaso del tercer parcial: ensayo completo**

El tercer parcial cubre el curso entero, de la unidad 1 a la 14. Este ejercicio junta lo esencial de todos los bloques en un solo programa.

Escriba un programa que genere `ensayo.txt` con cuatro renglones de etiqueta, tiempo y cuenta: (0, 400), (100, 420), (200, 460) y (300, 512). Después:

- un `struct Registro` con los tres campos,
- una función `leer` que reciba la ruta, el arreglo, su capacidad y un parámetro de referencia para el conteo, y que lance `std::runtime_error` si el archivo no abre,
- una clase abstracta `Sensor` con conversión y unidad virtuales puras, y las dos derivadas de siempre, guardadas en un arreglo de `std::unique_ptr`,
- una función recursiva que devuelva la cuenta más alta del arreglo, sin ciclos.

`main` lee el archivo dentro de un `try`, imprime cuántos registros trae y la cuenta máxima, recorre los dos canales imprimiendo la media convertida de cada uno, y termina intentando leer un archivo que no existe para mostrar el mensaje de la excepción.

```
registros 4
cuenta maxima 512
TC-04 media 112 C
SG-11 media 218.537 um/m
error: no se pudo abrir no_existe.txt
```

---

## Semana 17 · Cierre · Proyecto integrador

### 17.1 · Reconocer

**Cuatro defectos con el programa funcionando**

Este programa compila, corre y no falla. Es la clase de entrega que pierde la mitad de la rúbrica sin que nadie vea un error en pantalla.

```cpp
class Sensor {
public:
    Sensor(std::string e) : etiqueta(e) {}
    virtual double convertir(int cuenta) { return cuenta * 1.0; }
    ~Sensor() { std::cout << "cierra Sensor\n"; }
protected:
    std::string etiqueta;
};

class Termopar : public Sensor {
public:
    Termopar(std::string e, double p) : Sensor(e), pendiente(p) {}
    double convertir(int cuenta) override { return cuenta * pendiente; }
    ~Termopar() { std::cout << "cierra Termopar\n"; }
private:
    double pendiente;
};

double procesar(const std::string& ruta)
{
    std::ifstream in(ruta);
    std::string etiqueta;
    int cuenta = 0;
    double suma = 0.0;
    int n = 0;

    while (in >> etiqueta >> cuenta)
    {
        suma += cuenta;
        n++;
        std::cout << etiqueta << " " << cuenta << "\n";
    }

    std::cout << "media " << suma / n << "\n";
    return suma / n;
}

int main()
{
    Sensor* principal = new Termopar("TC-04", 0.25);
    Sensor* respaldo = new Termopar("TC-05", 0.50);

    std::cout << principal->convertir(400) << "\n";
    std::cout << respaldo->convertir(400) << "\n";

    double m = procesar("no_existe.txt");
    std::cout << "resultado " << m << "\n";

    delete principal;
    return 0;
}
```

1. Escriba las cinco líneas que imprime, con el archivo `no_existe.txt` ausente.
2. Señale cuatro defectos, uno por cada criterio de la rúbrica del proyecto, y diga en qué línea está cada uno y qué evidencia lo delata en la salida.
3. Cuente los `new` y los `delete`, diga cuánta memoria queda sin liberar y por qué la línea del `delete` que sí está tampoco hace todo su trabajo.

### 17.2 · Aplicar

**El mismo programa, sin fugas y con aviso**

Reescriba 17.1 con cuatro correcciones y nada más:

- el destructor de la base pasa a ser virtual y la conversión pasa a ser virtual pura,
- los dos punteros crudos se vuelven `std::unique_ptr` creados con `std::make_unique`,
- la función que procesaba se parte en dos: una que lee el archivo a un arreglo de cuentas y devuelve `bool` según haya abierto, y otra que calcula la media,
- `main` avisa con un mensaje claro cuando el archivo no abre, en lugar de imprimir un resultado que no significa nada.

El programa genera `ensayo17.txt` con cuatro renglones de etiqueta y cuenta, 400, 420, 460 y 512, intenta primero leer un archivo inexistente y después el bueno.

```
100
200
no se pudo abrir no_existe.txt
registros 4
media de cuentas 448
media en TC-04 112 C
cierra Termopar
cierra Sensor
cierra Termopar
cierra Sensor
```

Explique en tres renglones por qué las cuatro últimas líneas aparecen ahora y en el programa anterior no, y en qué orden se destruyen los dos objetos.

### 17.3 · Integrar

**Del archivo de instrumentación al reporte final**

Ejercicio de cierre. Es el tamaño y la forma de lo que se espera del proyecto, en una sola pieza.

Escriba un programa que genere `ensayo17b.txt` con cinco renglones de etiqueta, tiempo y cuenta: (0, 400), (100, 420), (200, 5000), (300, 460) y (400, 512). La tercera cuenta no cabe en un convertidor de 12 bits y hay que descartarla. Después:

- `struct Lectura` con los tres campos, y el operador de salida sobrecargado para imprimirla en una línea,
- `leer`, que lanza `std::runtime_error` si el archivo no abre,
- `valida`, que rechaza cuentas fuera del rango de 0 a 4095,
- una plantilla `promedio` que sirva para cualquier tipo de arreglo numérico,
- una función recursiva que devuelva la cuenta máxima,
- una clase abstracta `Sensor` con dos derivadas, guardadas en un arreglo de `std::unique_ptr`, con TC-04 de pendiente 0.25 y SG-11 de factor 2.05.

`main` lee dentro de un `try`, separa las válidas de las descartadas imprimiendo cada rechazo con el operador de salida, y cierra con el reporte.

```
descartada TC-04 200 ms 5000
leidas 5 validas 4
media de cuentas 448
cuenta maxima 512
TC-04 112 C
SG-11 218.537 um/m
```

Al terminar, corra sobre su propio programa la revisión del bloque 1 de la sesión: cuente los `new` contra los `delete`, busque la función más larga y decida si son dos, y pruebe qué imprime si borra el archivo antes de correrlo.
