# Soluciones · Programación Avanzada · COM103

Documento del profesor. Trae la solución de los cincuenta y un ejercicios, la salida real de cada programa y la rúbrica de diez puntos con la que se califican. Todo el código se compiló y se corrió con `cl /EHsc /std:c++20` sobre Visual Studio Community 2026, toolset 14.51, x64. Las salidas están copiadas de esa corrida, no reconstruidas a mano. Los valores de punto flotante salen con la precisión que `cout` usa por omisión, que son seis cifras significativas: si un alumno entrega `2.9416667` en lugar de `2.94167` es porque tocó la precisión, no porque calculó distinto.

---

## Semana 01 · Unidad 1 · Elementos básicos de C++

### 01.1 · Reconocer

**Solución**

1. El programa imprime el total correcto y un promedio equivocado.
2. Con el punto de ruptura en la línea del promedio, Locales muestra `total` en 3743 y `promedio` con basura, porque el depurador se detiene antes de ejecutar la línea marcada, no después.
3. La línea `int promedio = total / 4;` divide entre cuatro cuando hay tres ventanas. Corregida a `total / 3` el programa imprime `Promedio: 1247`, que es la división entera de 3743 entre 3.

**Salida**

```
Total: 3743
Promedio: 935
```

Y con el divisor corregido:

```
Total: 3743
Promedio: 1247
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| Las dos líneas de salida, exactas | 3 |
| Locales con `total` en 3743 y `promedio` sin valor útil | 3 |
| Identifica la línea del divisor y da 1247 como resultado corregido | 4 |

**Error que más se ve**

Contestan que `promedio` vale cero al detenerse; lo delata que escriben "0" donde la ventana muestra un número grande y distinto en cada corrida.

### 01.2 · Aplicar

**Solución**

```cpp
#include <iostream>

int main()
{
    int lectura1 = 101;
    int lectura2 = 104;
    int lectura3 = 99;
    int lectura4 = 108;

    int suma = lectura1 + lectura2 + lectura3 + lectura4;
    int promedio = suma / 4;
    int rango = lectura4 - lectura3;

    std::cout << "Lecturas: " << lectura1 << " " << lectura2 << " "
              << lectura3 << " " << lectura4 << "\n";
    std::cout << "Suma: " << suma << "\n";
    std::cout << "Promedio entero: " << promedio << "\n";
    std::cout << "Rango: " << rango << "\n";
    return 0;
}
```

**Salida**

```
Lecturas: 101 104 99 108
Suma: 412
Promedio entero: 103
Rango: 9
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| Los cuatro valores en variables con nombre, no en la salida directa | 3 |
| Suma, promedio y rango correctos | 4 |
| La salida coincide carácter por carácter, incluidos los dos puntos y los espacios | 3 |

**Error que más se ve**

Escriben los números dentro del `cout` en lugar de usar las variables; lo delata que la línea de lecturas queda correcta pero la suma aparece como un 412 escrito a mano.

### 01.3 · Integrar

**Solución**

Falta el punto y coma al final de `int muestras = 240`. El compilador no se queja de esa línea sino de la siguiente, porque hasta ahí sigue leyendo lo que cree que es la misma declaración. En este toolchain el mensaje es `error C2144: syntax error: 'int' should be preceded by ';'` en el renglón 6, de la misma familia que el C2143 que se vio en la sesión. El estándar se fija en Propiedades del proyecto, C/C++, Lenguaje, Estándar de lenguaje de C++, y hay que ponerlo en las dos configuraciones. `__cplusplus` no sirve para comprobarlo porque MSVC la deja congelada en 199711 por compatibilidad, aunque el proyecto esté en C++20.

```cpp
#include <iostream>

int main()
{
    int muestras = 240;
    int frecuencia = 8;

    int duracion = muestras / frecuencia;

    std::cout << "Duracion: " << duracion << " s\n";
    std::cout << "Estandar: " << _MSVC_LANG << "\n";
    return 0;
}
```

**Salida**

```
Duracion: 30 s
Estandar: 202002
```

Y antes de corregir:

```
e01_3roto.cpp(6): error C2144: syntax error: 'int' should be preceded by ';'
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| Anticipa que el error se reporta en el renglón siguiente al de la falta | 3 |
| El programa corregido compila e imprime las dos líneas | 4 |
| Explica dónde se fija el estándar y por qué `__cplusplus` miente aquí | 3 |

**Error que más se ve**

Buscan el error en el renglón 6, donde el compilador señala, y borran o alteran esa línea; lo delata que el archivo entregado tiene `int frecuencia` modificado y la declaración de arriba sigue sin punto y coma.

---

## Semana 02 · Unidad 1 · Elementos básicos de C++

### 02.1 · Reconocer

**Solución**

`bloques` vale 6 después de la división entera de 1732 entre 250. `sobran` vale 232, que es el residuo. `enviados` recibe 6 porque el sufijo entrega el valor viejo, y en ese mismo instante `bloques` pasa a 7, que es lo que se imprime. `ocupacion` es 0 porque 232 entre 250 se calcula entre enteros y se trunca antes de que el `double` de la izquierda pueda hacer algo. Los dos que sorprenden son el 7 junto al 6 y el 0. La corrección es `double ocupacion = static_cast<double>(sobran) / BLOQUE;`, que da 0.928.

**Salida**

```
7 6
232 0
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| Las dos líneas exactas | 3 |
| Explica el sufijo: `enviados` con el valor viejo y `bloques` ya incrementado | 3 |
| Explica la división entera y corrige con `static_cast` sin cambiar los tipos de origen | 4 |

**Error que más se ve**

Corrigen la ocupación cambiando `BLOQUE` a 250.0; lo delata que el ejercicio prohíbe tocar esos tipos y la constante deja de ser el tamaño de bloque en muestras.

### 02.2 · Aplicar

**Solución**

```cpp
#include <iostream>

int main()
{
    const int CUENTA_MAX = 32768;
    const double FONDO_ESCALA_N = 5000.0;

    int cuenta = 26214;

    double fuerza = static_cast<double>(cuenta) / CUENTA_MAX * FONDO_ESCALA_N;
    double porcentaje = static_cast<double>(cuenta) / CUENTA_MAX * 100.0;

    std::cout << "Cuenta: " << cuenta << "\n";
    std::cout << "Fuerza: " << fuerza << " N\n";
    std::cout << "Fondo de escala: " << porcentaje << " %\n";
    return 0;
}
```

Sin el `static_cast`, `cuenta / CUENTA_MAX` da 0 y las dos salidas serían `0 N` y `0 %`.

**Salida**

```
Cuenta: 26214
Fuerza: 3999.94 N
Fondo de escala: 79.9988 %
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| Las dos constantes con `const` y nombres que dicen qué guardan | 2 |
| La conversión explícita antes de la división, no después | 4 |
| Los dos resultados correctos | 2 |
| El comentario dice que sin la conversión los dos salen en cero | 2 |

**Error que más se ve**

Escriben `double fuerza = cuenta / CUENTA_MAX * FONDO_ESCALA_N;` confiando en que el tipo del destino arregla la cuenta; lo delata que la fuerza sale exactamente 0 y el porcentaje también.

### 02.3 · Integrar

**Solución**

Con el programa original, `promedio` es un `int` que vale 119 y la desviación calcula 119 menos 119, así que imprime 0. Ese cero no dice que la última lectura sea la media, dice que la media perdió su fracción antes de la resta. El depurador lo muestra deteniéndose en la línea de la desviación con `promedio` en 119 y `suma` en 598.

```cpp
#include <iostream>

int main()
{
    const int N = 5;

    int m1 = 118;
    int m2 = 121;
    int m3 = 117;
    int m4 = 123;
    int m5 = 119;

    int suma = m1 + m2 + m3 + m4 + m5;
    int promedioEntero = suma / N;
    int residuo = suma % N;

    double promedioReal = static_cast<double>(suma) / N;
    double desviacion = m5 - promedioReal;

    std::cout << "Suma: " << suma << "\n";
    std::cout << "Promedio entero: " << promedioEntero << "\n";
    std::cout << "Residuo: " << residuo << "\n";
    std::cout << "Promedio real: " << promedioReal << "\n";
    std::cout << "Desviacion: " << desviacion << "\n";
    return 0;
}
```

**Salida**

```
Suma: 598
Promedio entero: 119
Residuo: 3
Promedio real: 119.6
Desviacion: -0.6
```

Y el programa original, antes de corregirlo:

```
Suma: 598
Promedio: 119
Desviacion: 0
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| Predice el 0 de la desviación y explica de dónde sale | 3 |
| El número de mediciones en una constante, usado en las tres cuentas | 2 |
| Las cinco líneas correctas, con el residuo en 3 y la desviación en -0.6 | 3 |
| Reporta el renglón donde se detuvo y el valor de `promedio` ahí | 2 |

**Error que más se ve**

Declaran `double promedio = suma / N;` y creen haberlo arreglado; lo delata que el promedio real sale 119 en lugar de 119.6 y la desviación vuelve a dar 0.

---

## Semana 03 · Unidad 2 · Tipos, espacios de nombres y string

### 03.1 · Reconocer

**Solución**

`substr(0, 5)` copia cinco caracteres desde el inicio y deja `TC-04`. `find("HORNO")` devuelve 6, la posición donde empieza el texto buscado. `length()` cuenta once caracteres. El contador da la vuelta: en un `unsigned short` de 16 bits, cero menos uno es 65535, y con `short` habría impreso -1 porque ese tipo sí admite negativos. `Midiendo` vale 2 porque los valores de un `enum class` empiezan en cero y suben de uno en uno; sin el `static_cast` el compilador rechaza la conversión, que es justo lo que `enum class` viene a impedir.

**Salida**

```
TC-04
6
11
65535
2
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| Las cinco líneas exactas | 4 |
| Explica el 65535 y dice que con `short` habría dado -1 | 3 |
| Explica por qué `enum class` exige la conversión explícita | 3 |

**Error que más se ve**

Contestan 11 en la segunda línea y 5 en la tercera, cambiando `find` por `length`; lo delata que las dos respuestas están intercambiadas.

### 03.2 · Aplicar

**Solución**

```cpp
#include <iostream>
#include <string>

enum class Escala { Celsius, Kelvin };
using Temperatura = double;

int main()
{
    std::string canal = "TC";
    std::string id = "04";
    std::string zona = "HORNO";

    std::string etiqueta = canal + "-" + id + "-" + zona;

    Escala escala = Escala::Kelvin;
    Temperatura lectura = 373.15;

    std::cout << etiqueta << "\n";
    std::cout << etiqueta.length() << "\n";
    std::cout << etiqueta.substr(0, 2) << "\n";
    std::cout << etiqueta.find("-", 3) << "\n";
    std::cout << static_cast<int>(escala) << "\n";
    std::cout << lectura << "\n";
    return 0;
}
```

**Salida**

```
TC-04-HORNO
11
TC
5
1
373.15
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| La etiqueta se arma concatenando, no escribiéndola completa | 3 |
| `enum class` y el alias `using` declarados y usados | 3 |
| Las seis líneas correctas, con el 5 de la búsqueda desde el índice 3 | 4 |

**Error que más se ve**

Escriben `"TC" + "-" + "04"` sin ningún `std::string` de por medio y el compilador rechaza la suma de dos literales; lo delata el error de punteros en una línea que se ve inofensiva.

### 03.3 · Integrar

**Solución**

```cpp
#include <iostream>
#include <string>

int main()
{
    const int CUENTA_MAX = 4095;
    const double VREF = 3.3;
    const double V_CERO = 0.5;
    const double PENDIENTE = 0.01;

    int cuenta = 2867;

    double volts = static_cast<double>(cuenta) / CUENTA_MAX * VREF;
    double grados = (volts - V_CERO) / PENDIENTE;

    std::string reporte = "ADC-12 canal 3";

    std::cout << reporte << "\n";
    std::cout << reporte.substr(7, 5) << "\n";
    std::cout << volts << " V\n";
    std::cout << grados << " C\n";
    std::cout << sizeof(int) << " " << sizeof(double) << "\n";
    return 0;
}
```

**Salida**

```
ADC-12 canal 3
canal
2.3104 V
181.04 C
4 8
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| Las cuatro constantes con `const` | 2 |
| La conversión explícita y el voltaje correcto | 3 |
| La temperatura correcta a partir del voltaje, no de la cuenta | 3 |
| `substr` saca exactamente `canal` y los tamaños salen 4 y 8 | 2 |

**Error que más se ve**

Piden `substr(7, 11)` pensando que el segundo argumento es la posición final; lo delata que la salida arrastra el resto de la cadena en lugar de cortar en cinco caracteres.

---

## Semana 04 · Unidad 3 · Funciones definidas por el usuario I

### 04.1 · Reconocer

**Solución**

212 grados Fahrenheit son 100 Celsius, y en Kelvin 373.15. `margen` sigue valiendo 2.5 porque `duplicar` recibió una copia: el parámetro `x` nació al entrar, se duplicó y murió al salir, sin tocar la variable de `main`. Si se borra el prototipo de `kelvin`, el compilador reporta `C3861: identifier not found` en la línea de la llamada, más una cadena de errores derivados que desaparecen al corregir el primero. El parámetro `c` de `kelvin` y la variable `c` de `main` son dos variables distintas en dos alcances distintos que coinciden en el nombre y en el valor durante la llamada.

**Salida**

```
100 373.15
2.5
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| Las dos líneas exactas | 3 |
| Explica el paso por valor con la copia y el momento en que muere | 4 |
| Nombra el error C3861 y dice que los siguientes son consecuencia | 3 |

**Error que más se ve**

Contestan 5.0 en la segunda línea porque suponen que `duplicar` modificó el original; lo delata que ignoran que el valor de retorno no se guardó en ningún lado.

### 04.2 · Aplicar

**Solución**

```cpp
#include <iostream>

double cubo(double x);
double inercia(double b, double h);
double deflexion(double F, double L, double E, double I);
double aMilimetros(double metros);

int main()
{
    const double B = 0.04;
    const double H = 0.06;
    const double CARGA = 800.0;
    const double LARGO = 1.2;
    const double YOUNG = 200.0e9;

    double I = inercia(B, H);
    double d = deflexion(CARGA, LARGO, YOUNG, I);

    std::cout << "Inercia: " << I << " m4\n";
    std::cout << "Deflexion: " << d << " m\n";
    std::cout << "Deflexion: " << aMilimetros(d) << " mm\n";
    return 0;
}

double cubo(double x)
{
    return x * x * x;
}

double inercia(double b, double h)
{
    return b * cubo(h) / 12.0;
}

double deflexion(double F, double L, double E, double I)
{
    return F * cubo(L) / (3.0 * E * I);
}

double aMilimetros(double metros)
{
    return metros * 1000.0;
}
```

**Salida**

```
Inercia: 7.2e-07 m4
Deflexion: 0.0032 m
Deflexion: 3.2 mm
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| Cuatro prototipos antes de `main` y cuatro definiciones después | 3 |
| Cada función hace una sola cosa y `cubo` se reutiliza en dos lugares | 2 |
| Los tres valores correctos | 3 |
| `main` no calcula nada, solo llama e imprime | 2 |

**Error que más se ve**

Dividen entre `3 * E * I` con el 3 entero; aquí no cambia el resultado porque `E` es real, pero lo delata que el mismo hábito rompe la fórmula en cuanto los dos operandos son enteros.

### 04.3 · Integrar

**Solución**

```cpp
#include <iostream>
#include <string>

double volts(int cuenta, int cuentaMax, double vref);
double grados(double v, double vCero, double pendiente);
std::string etiqueta(std::string canal, std::string zona);

int main()
{
    const int CUENTA_MAX = 4095;
    const double VREF = 3.3;
    const double V_CERO = 0.5;
    const double PENDIENTE = 0.01;

    int cuenta = 2867;

    double v = volts(cuenta, CUENTA_MAX, VREF);
    double t = grados(v, V_CERO, PENDIENTE);
    std::string nombre = etiqueta("TC", "HORNO");

    std::cout << nombre << "\n";
    std::cout << nombre.length() << "\n";
    std::cout << v << " V\n";
    std::cout << t << " C\n";
    return 0;
}

double volts(int cuenta, int cuentaMax, double vref)
{
    return static_cast<double>(cuenta) / cuentaMax * vref;
}

double grados(double v, double vCero, double pendiente)
{
    return (v - vCero) / pendiente;
}

std::string etiqueta(std::string canal, std::string zona)
{
    return canal + "-" + zona;
}
```

**Salida**

```
TC-HORNO
8
2.3104 V
181.04 C
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| Las tres funciones con prototipo y con los tipos correctos | 3 |
| La conversión explícita vive dentro de `volts` | 2 |
| Los cuatro valores de salida correctos | 3 |
| Ninguna función imprime y `main` no calcula | 2 |

**Error que más se ve**

Meten el `cout` dentro de las funciones de conversión para no pasar el resultado; lo delata que `main` queda en dos líneas y las funciones ya no se pueden probar con otros valores.

---

## Semana 05 · Unidad 4 · Funciones definidas por el usuario II

### 05.1 · Reconocer

**Solución**

`llamadas` es `static`, así que su línea de inicialización corre una sola vez en todo el programa y el valor sobrevive entre llamadas: 1 y luego 2. `muestras` dentro de la función es una variable local nueva en cada llamada que además tapa a la global, así que nace en 100, sube a 101 y muere. La global nunca la toca nadie y termina en 0. `escalar` sí modifica su argumento porque lo recibe por referencia: 3.5 por 2 son 7, y 7 por 10 son 70.

**Salida**

```
1 101
2 101
70 0
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| Las tres líneas exactas | 3 |
| Explica que `static` cambia la vida de la variable y no su alcance | 4 |
| Explica que la local tapa a la global y que por eso la global sigue en 0 | 3 |

**Error que más se ve**

Contestan 102 en la segunda línea, sumando la local como si también fuera `static`; lo delata que aplican la misma regla a las dos variables cuando solo una lleva la palabra.

### 05.2 · Aplicar

**Solución**

```cpp
#include <iostream>
#include <string>

void resumen(const std::string& canal, double a, double b, double c,
             double& suma, double& media, std::string unidad = "mm/s");
void resumen(const std::string& canal, double a, double b, double c, double d,
             double& suma, double& media, std::string unidad = "mm/s");

int main()
{
    double suma = 0.0;
    double media = 0.0;

    resumen("VIB-02", 2.4, 3.1, 2.8, suma, media);
    std::cout << suma << " " << media << "\n";

    resumen("VIB-02", 2.4, 3.1, 2.8, 3.6, suma, media, "mm/s rms");
    std::cout << suma << " " << media << "\n";
    return 0;
}

void resumen(const std::string& canal, double a, double b, double c,
             double& suma, double& media, std::string unidad)
{
    suma = a + b + c;
    media = suma / 3.0;
    std::cout << canal << " 3 muestras " << unidad << "\n";
}

void resumen(const std::string& canal, double a, double b, double c, double d,
             double& suma, double& media, std::string unidad)
{
    suma = a + b + c + d;
    media = suma / 4.0;
    std::cout << canal << " 4 muestras " << unidad << "\n";
}
```

**Salida**

```
VIB-02 3 muestras mm/s
8.3 2.76667
VIB-02 4 muestras mm/s rms
11.9 2.975
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| Los dos resultados salen por parámetros de referencia, no por `return` | 3 |
| Las dos versiones sobrecargadas conviven y el compilador elige bien | 3 |
| El valor por omisión aparece una sola vez, en el prototipo | 2 |
| Los cuatro números correctos | 2 |

**Error que más se ve**

Repiten el valor por omisión en el prototipo y en la definición; lo delata el error del compilador que señala la definición, no la llamada.

### 05.3 · Integrar

**Solución**

```cpp
#include <iostream>

double cubo(double x);
double inercia(double b, double h);
int registrar();
void deflexion(double F, double L, double E, double I,
               double& metros, double& milimetros);
void deflexion(double F, double L, double E, double b, double h,
               double& metros, double& milimetros);

int main()
{
    const double CARGA = 800.0;
    const double LARGO = 1.2;
    const double YOUNG = 200.0e9;

    double metros = 0.0;
    double mm = 0.0;

    deflexion(CARGA, LARGO, YOUNG, 7.2e-7, metros, mm);
    std::cout << metros << " m " << mm << " mm\n";

    deflexion(CARGA, LARGO, YOUNG, 0.04, 0.06, metros, mm);
    std::cout << metros << " m " << mm << " mm\n";
    return 0;
}

double cubo(double x)
{
    return x * x * x;
}

double inercia(double b, double h)
{
    return b * cubo(h) / 12.0;
}

int registrar()
{
    static int veces = 0;
    veces = veces + 1;
    return veces;
}

void deflexion(double F, double L, double E, double I,
               double& metros, double& milimetros)
{
    metros = F * cubo(L) / (3.0 * E * I);
    milimetros = metros * 1000.0;
    std::cout << "calculo " << registrar() << "\n";
}

void deflexion(double F, double L, double E, double b, double h,
               double& metros, double& milimetros)
{
    deflexion(F, L, E, inercia(b, h), metros, milimetros);
}
```

El contador llega a 2 porque `registrar` solo se llama desde la versión que recibe el segundo momento de área. La versión que recibe base y altura no cuenta nada: calcula el momento y delega, así que su llamada pasa una sola vez por el contador.

**Salida**

```
calculo 1
0.0032 m 3.2 mm
calculo 2
0.0032 m 3.2 mm
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| Las dos versiones sobrecargadas, distinguidas por el número de parámetros | 3 |
| La segunda delega en la primera en lugar de repetir la fórmula | 2 |
| El contador `static` en su propia función y su valor correcto | 3 |
| La explicación del 2 en lugar del 3 | 2 |

**Error que más se ve**

Ponen la variable `static` dentro de las dos sobrecargas y entonces cada una lleva su propia cuenta; lo delata que la salida dice `calculo 1` las dos veces.

---

## Semana 06 · Unidad 5 · Clases y abstracción de datos

### 06.1 · Reconocer

**Solución**

El objeto nace con 250 kPa, que en bar son 2.5. Después el mutador lo deja en 101.3 kPa, que son 1.013 bar. La línea `s.kpa = 300.0;` no compila: `kpa` es privado y el compilador reporta `error C2248: cannot access private member declared in class 'SensorPresion'`. Aparece al compilar, antes de que el programa exista. La línea que hace lo mismo y sí compila es `s.setKpa(300.0);`, porque entra por la puerta que la clase dejó abierta.

**Salida**

```
PT-07
250
2.5
1.013
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| Las cuatro líneas exactas | 4 |
| Nombra C2248 y dice que ocurre en tiempo de compilación | 3 |
| Señala el mutador como la vía equivalente y legal | 3 |

**Error que más se ve**

Dicen que el acceso al privado "falla al correr"; lo delata que hablan de un mensaje en pantalla cuando el programa nunca llegó a generarse.

### 06.2 · Aplicar

**Solución**

```cpp
#include <iostream>
#include <string>

class Viga {
public:
    Viga(std::string id, double b, double h, double largo, double young)
    {
        clave = id;
        base = b;
        altura = h;
        L = largo;
        E = young;
    }

    std::string getClave() { return clave; }
    double inercia() { return base * altura * altura * altura / 12.0; }
    double deflexionM(double carga) { return carga * L * L * L / (3.0 * E * inercia()); }
    double deflexionMm(double carga) { return deflexionM(carga) * 1000.0; }

private:
    std::string clave;
    double base;
    double altura;
    double L;
    double E;
};

int main()
{
    Viga v1("VG-01", 0.04, 0.06, 1.2, 200.0e9);
    Viga v2("VG-02", 0.04, 0.08, 1.2, 200.0e9);

    std::cout << v1.getClave() << " " << v1.inercia() << " " << v1.deflexionMm(800.0) << "\n";
    std::cout << v2.getClave() << " " << v2.inercia() << " " << v2.deflexionMm(800.0) << "\n";
    return 0;
}
```

**Salida**

```
VG-01 7.2e-07 3.2
VG-02 1.70667e-06 1.35
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| Los cinco miembros de datos privados y el constructor que los deja completos | 3 |
| `deflexionMm` se apoya en las otras dos y no repite la fórmula | 2 |
| Los dos renglones con los valores correctos | 3 |
| `main` no hace ninguna cuenta | 2 |

**Error que más se ve**

Olvidan el punto y coma después de la llave que cierra la clase; lo delata que el error del compilador apunta a la línea de `int main`, donde no hay nada raro.

### 06.3 · Integrar

**Solución**

```cpp
class Viga {
public:
    Viga(std::string id, double b, double h, double largo, double young)
    {
        clave = id;
        base = b;
        altura = h;
        L = largo;
        E = young;
    }

    double inercia() { return base * altura * altura * altura / 12.0; }
    double deflexionMm(double carga = 800.0)
    {
        return carga * L * L * L / (3.0 * E * inercia()) * 1000.0;
    }

    void reportar(double& mm, double& segundoMomento, double carga = 800.0)
    {
        mm = deflexionMm(carga);
        segundoMomento = inercia();
        std::cout << clave << " con " << carga << " N\n";
    }

private:
    std::string clave;
    double base;
    double altura;
    double L;
    double E;
};
```

El segundo momento de área depende de la geometría de la sección y no de lo que se le cuelgue, así que las dos llamadas dan 7.2e-07. La deflexión es proporcional a la carga: con 1200 N en lugar de 800 sube en la misma proporción, de 3.2 a 4.8 mm.

**Salida**

```
VG-01 con 800 N
7.2e-07 m4 3.2 mm
VG-01 con 1200 N
7.2e-07 m4 4.8 mm
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| `reportar` entrega los dos resultados por referencia | 3 |
| El valor por omisión de la carga funciona en las dos llamadas | 3 |
| Los cuatro renglones correctos | 2 |
| La explicación distingue lo que depende de la geometría de lo que depende de la carga | 2 |

**Error que más se ve**

Ponen el parámetro con valor por omisión antes de los de referencia; lo delata el error del compilador, que exige que los parámetros con valor por omisión queden al final.

---

## Semana 07 · Unidad 6 · Estructuras de control I

### 07.1 · Reconocer

**Solución**

`if (alarmas = 1)` asigna en lugar de comparar, la condición vale 1 y siempre entra por el primer camino, de paso dejando `alarmas` en 1. La suma `0.1 + 0.2` no da exactamente 0.3 en binario, así que la igualdad es falsa y entra el `else`, aunque el número se imprima como 0.3. El `switch` entra en el caso 2 y, como ese caso no lleva `break`, cae al 3 y ejecuta los dos. Las correcciones mínimas son un segundo signo igual, una comparación contra una tolerancia y un `break` en el caso 2.

**Salida**

```
ADbarpsi
1 250
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| Las dos líneas exactas, con `barpsi` pegado | 4 |
| Explica las tres trampas | 3 |
| Da la corrección mínima de cada una | 3 |

**Error que más se ve**

Escriben `ADbar` porque suponen que el `switch` ejecuta un caso y sale; lo delata que el `psi` es justo lo que el ejercicio quiere ver reconocido.

### 07.2 · Aplicar

**Solución**

```cpp
std::string clasificar(double t)
{
    if (t < 0.0)
        return "bajo";
    else if (t <= 120.0)
        return "normal";
    else if (t <= 300.0)
        return "alto";
    else
        return "critico";
}

std::string unidad(int codigo)
{
    switch (codigo)
    {
    case 1:
        return "C";
    case 2:
        return "kPa";
    case 3:
        return "um/m";
    default:
        return "?";
    }
}

bool calibrado(double medido, double patron, double tolerancia)
{
    if (medido > patron - tolerancia && medido < patron + tolerancia)
        return true;
    return false;
}
```

**Salida**

```
normal
bajo
critico
C kPa ?
1 0
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| La cadena de `if-else` cubre los cuatro rangos sin huecos ni traslapes | 3 |
| El `switch` tiene caso por omisión y cada caso devuelve | 3 |
| `calibrado` compara contra una tolerancia y nunca con igualdad exacta | 3 |
| Los cinco renglones correctos | 1 |

**Error que más se ve**

Escriben `if (t < 0) ... if (t <= 120) ...` sin los `else`, y el valor -4.0 entra por dos ramas; lo delata que la clasificación de los negativos se imprime dos veces o se queda con la última.

### 07.3 · Integrar

**Solución**

```cpp
class Termopar {
public:
    Termopar(std::string e)
    {
        etiqueta = e;
        celsius = 0.0;
        rechazos = 0;
    }

    void setCelsius(double c)
    {
        if (c < -200.0 || c > 1300.0)
        {
            rechazos++;
            std::cout << "rechazado " << c << "\n";
        }
        else
        {
            celsius = c;
        }
    }

    double getCelsius() { return celsius; }
    int getRechazos() { return rechazos; }

    char estado()
    {
        if (celsius < 0.0)
            return 'B';
        else if (celsius <= 120.0)
            return 'N';
        else if (celsius <= 300.0)
            return 'A';
        else
            return 'C';
    }

private:
    std::string etiqueta;
    double celsius;
    int rechazos;
};

void ejecutar(int opcion, Termopar& t)
{
    switch (opcion)
    {
    case 1:
        std::cout << t.getCelsius() << "\n";
        break;
    case 2:
        std::cout << t.estado() << "\n";
        break;
    case 3:
        std::cout << t.getRechazos() << "\n";
        break;
    default:
        std::cout << "opcion invalida\n";
    }
}
```

**Salida**

```
rechazado 1500
87.5
N
1
opcion invalida
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| La validación vive en el mutador y el dato no se toca cuando se rechaza | 4 |
| El contador de rechazos sube solo cuando corresponde | 2 |
| El `switch` con sus `break` y su caso por omisión | 2 |
| Los cinco renglones correctos | 2 |

**Error que más se ve**

Validan en `main` antes de llamar al mutador; lo delata que la clase sigue aceptando cualquier valor si alguien más la usa, que es exactamente lo que el encapsulamiento venía a evitar.

---

## Semana 08 · Unidad 6 · Estructuras de control II

### 08.1 · Reconocer

**Solución**

El ciclo interno arranca doce veces y en tres de ellas el `continue` salta antes de contar, así que el cuerpo útil corre nueve veces. La suma por fila es `fila * (1 + 2 + 4)`, o sea `7 * fila`, y sumando las tres filas da 42. El `do-while` ejecuta el cuerpo antes de revisar nada: `intentos` queda en 1 y `codigo` en 3, y la condición `3 > 5` es falsa. Un `while` con esa misma condición no habría entrado nunca, porque 5 no es mayor que 5, y habría dejado `intentos` en 0.

**Salida**

```
9 42
1 3
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| Las dos líneas exactas | 3 |
| Doce vueltas iniciadas, tres saltadas, nueve completas | 3 |
| Explica que el `while` equivalente no habría impreso nada | 4 |

**Error que más se ve**

Cuentan doce celdas porque leen el `continue` como si solo saltara la suma; lo delata que el 42 les sale bien y el conteo no.

### 08.2 · Aplicar

**Solución**

```cpp
#include <iostream>

int main()
{
    const double T_AMB = 100.0;
    const double TAU = 5.0;
    const double DT = 1.0;
    const double LIMITE = 90.0;
    const int MAX_PASOS = 20;

    double t = 20.0;
    int paso = 0;

    while (paso < MAX_PASOS)
    {
        paso++;
        t = t + (DT / TAU) * (T_AMB - t);
        std::cout << paso << " " << t << "\n";

        if (t > LIMITE)
            break;
    }

    std::cout << "pasos " << paso << "\n";
    return 0;
}
```

**Salida**

```
1 36
2 48.8
3 59.04
4 67.232
5 73.7856
6 79.0285
7 83.2228
8 86.5782
9 89.2626
10 91.4101
pasos 10
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| Las cinco constantes con nombre y ningún número suelto en el ciclo | 3 |
| La recurrencia bien escrita, con la temperatura anterior en los dos lados | 3 |
| El `break` corta en el primer paso que pasa de 90 | 2 |
| Los diez renglones y el conteo final | 2 |

**Error que más se ve**

Escriben `t = (DT / TAU) * (T_AMB - t);` sin sumar la temperatura anterior; lo delata que la primera línea sale 16 en lugar de 36 y la serie ya no converge a 100.

### 08.3 · Integrar

**Solución**

```cpp
double simular(int paso);

class Termopar {
public:
    Termopar(std::string e, double limite)
    {
        etiqueta = e;
        alarma = limite;
        alarmas = 0;
        suma = 0.0;
        n = 0;
    }

    void registrar(double c)
    {
        if (c < -200.0 || c > 1300.0)
        {
            std::cout << "fuera de rango " << c << "\n";
        }
        else
        {
            suma = suma + c;
            n++;

            if (c > alarma)
                alarmas++;
        }
    }

    std::string getEtiqueta() { return etiqueta; }
    double media() { return suma / n; }
    int getAlarmas() { return alarmas; }
    int getN() { return n; }

private:
    std::string etiqueta;
    double alarma;
    int alarmas;
    double suma;
    int n;
};

double simular(int paso)
{
    return 20.0 + 9.5 * paso;
}
```

**Salida**

```
1 29.5
2 39
3 48.5
4 58
5 67.5
6 77
7 86.5
8 96
fuera de rango 1500
TC-04
aceptadas 8
media 62.75
alarmas 2
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| La función de simulación separada, con prototipo | 2 |
| La clase acumula, cuenta y descarta sin que `main` intervenga | 3 |
| El `for` recorre los ocho pasos y el rechazo no altera los acumuladores | 2 |
| Media 62.75 y dos alarmas | 3 |

**Error que más se ve**

Suman la lectura rechazada al acumulador antes de revisar el rango; lo delata que la media pasa de 62.75 a más de doscientos, aunque el aviso de fuera de rango se imprima igual.

---

## Semana 09 · Unidad 7 · Herencia y composición

### 09.1 · Reconocer

**Solución**

`getEtiqueta` viene de la base y funciona sin escribirla otra vez. `describir` usa `etiqueta` directamente porque el miembro es `protected`, que es justo lo que abre la puerta a la clase hija y la deja cerrada para todo lo demás: si `main` escribe `t.etiqueta`, sale `error C2248`. `t.aUnidades(400)` corre la versión de `Termopar`, porque el objeto es un `Termopar` y esa función tapa a la de la base, así que da 100. El objeto `s` es un `Sensor` de verdad y usa la versión de la base, que da 400. Si se borra `Sensor(e)` de la lista de inicialización, el compilador busca un constructor sin argumentos en la base, no lo encuentra y rechaza la clase derivada.

**Salida**

```
TC-04
TC-04 tipo K
100
400
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| Las cuatro líneas exactas | 4 |
| Explica el nivel protegido y nombra C2248 para el acceso desde `main` | 3 |
| Explica qué falta cuando se quita la llamada al constructor de la base | 3 |

**Error que más se ve**

Contestan 400 en la tercera línea creyendo que la función de la base es la que corre; lo delata que aplican a un objeto concreto la regla que solo aparece con punteros y `virtual`, que es tema de la semana 12.

### 09.2 · Aplicar

**Solución**

```cpp
class Sensor {
public:
    Sensor(std::string e, std::string u) { etiqueta = e; unidad = u; }
    std::string getEtiqueta() { return etiqueta; }
    std::string getUnidad() { return unidad; }
protected:
    std::string etiqueta;
    std::string unidad;
};

class Termopar : public Sensor {
public:
    Termopar(std::string e, double p, double c) : Sensor(e, "C"), pendiente(p), cero(c) {}
    double convertir(double volts) { return (volts - cero) / pendiente; }
private:
    double pendiente;
    double cero;
};

class Extensometro : public Sensor {
public:
    Extensometro(std::string e, double f) : Sensor(e, "um/m"), factor(f) {}
    double convertir(double razon) { return razon / factor * 1000000.0; }
private:
    double factor;
};

class Canal {
public:
    Canal(int n, Termopar t) : numero(n), sensor(t) {}
    void reportar(double volts)
    {
        std::cout << numero << " " << sensor.getEtiqueta() << " "
                  << sensor.convertir(volts) << " " << sensor.getUnidad() << "\n";
    }
private:
    int numero;
    Termopar sensor;
};
```

Un termopar es un sensor y un extensómetro también, así que ahí la herencia describe algo real. Un canal no es un termopar: lo tiene, junto con un número y con lo que se le agregue después. Cambiar el sensor de un canal es cambiar un miembro, no rehacer una jerarquía.

**Salida**

```
TC-04 181 C
SG-11 100 um/m
3 TC-04 181 C
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| Las dos derivadas llaman al constructor de la base con su unidad | 3 |
| `Canal` contiene un `Termopar` y no hereda de él | 3 |
| Los tres renglones correctos | 2 |
| El comentario aplica la prueba de "es un" contra "tiene un" a las dos decisiones | 2 |

**Error que más se ve**

Hacen que `Canal` herede de `Termopar` para poder llamar a `convertir` sin escribir el miembro; lo delata que el canal termina exponiendo `getUnidad` como si él mismo fuera un sensor.

### 09.3 · Integrar

**Solución**

```cpp
class BancoDePruebas {
public:
    BancoDePruebas(std::string n, Termopar t, double lim) : nombre(n), sensor(t)
    {
        limite = lim;
        alarmas = 0;
        suma = 0.0;
        muestras = 0;
    }

    void medir(double volts)
    {
        double c = sensor.convertir(volts);
        suma += c;
        muestras++;

        if (c > limite)
        {
            alarmas++;
            std::cout << "ALARMA " << sensor.getEtiqueta() << " " << c << "\n";
        }
        else
        {
            std::cout << "ok " << sensor.getEtiqueta() << " " << c << "\n";
        }
    }

    double media() { return suma / muestras; }
    int getAlarmas() { return alarmas; }
    std::string getNombre() { return nombre; }

private:
    std::string nombre;
    Termopar sensor;
    double limite;
    int alarmas;
    double suma;
    int muestras;
};
```

**Salida**

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

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| El banco contiene el sensor y delega la conversión en él | 3 |
| El ciclo genera los cinco voltajes y no los escribe uno por uno | 2 |
| Las cinco líneas de medición con su etiqueta correcta | 3 |
| Media 130 y tres alarmas | 2 |

**Error que más se ve**

Guardan el `Termopar` como copia pero convierten en `main` y le pasan al banco el resultado ya convertido; lo delata que el banco deja de necesitar al sensor y su miembro queda sin usarse.

---

## Semana 10 · Unidad 8 · Arreglos y cadenas

### 10.1 · Reconocer

**Solución**

`sizeof` del arreglo entre `sizeof` de un elemento da 6. La suma de las seis lecturas es 728. `lecturas[n - 1]` es la última casilla válida y vale 130. La etiqueta tiene dos guiones. Con `lecturas[n]` el programa imprimiría lo que hubiera en la memoria de junto, un número distinto en cada corrida, y no fallaría: nadie revisa el índice. Dentro de una función que recibe el arreglo, el parámetro es una dirección y `sizeof` mide esa dirección, así que la cuenta daría 8 entre 4, o sea 2, sin importar cuántos elementos haya.

**Salida**

```
6 728
130 2
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| Las dos líneas exactas | 3 |
| Dice que el acceso fuera de rango imprime basura y no interrumpe el programa | 4 |
| Explica por qué `sizeof` deja de servir dentro de una función | 3 |

**Error que más se ve**

Contestan que el programa "truena" al leer `lecturas[n]`; lo delata que el ejercicio pide precisamente reconocer el error que no avisa.

### 10.2 · Aplicar

**Solución**

```cpp
int lecturas[8] = {118, 121, 117, 123, 119, 130, 112, 126};
int n = sizeof(lecturas) / sizeof(lecturas[0]);

int suma = 0;
int mayor = lecturas[0];
int menor = lecturas[0];

for (int i = 0; i < n; i++)
{
    suma = suma + lecturas[i];

    if (lecturas[i] > mayor)
        mayor = lecturas[i];

    if (lecturas[i] < menor)
        menor = lecturas[i];
}

double media = static_cast<double>(suma) / n;

int arriba = 0;
for (int i = 0; i < n; i++)
    if (lecturas[i] > media)
        arriba++;
```

**Salida**

```
n 8
media 120.75
mayor 130
menor 112
rango 18
arriba 4
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| El tamaño se calcula con `sizeof` y ningún ciclo lleva el 8 escrito | 3 |
| Mayor y menor arrancan con el primer elemento, no con cero | 3 |
| La media es real, con conversión explícita | 2 |
| Los seis renglones correctos | 2 |

**Error que más se ve**

Inicializan `mayor` en 0 y `menor` en 0; el mayor sale bien de casualidad y el menor sale 0, lo delata que el valor reportado no está en el arreglo.

### 10.3 · Integrar

**Solución**

```cpp
double media(const int datos[], int n)
{
    int suma = 0;
    for (int i = 0; i < n; i++)
        suma = suma + datos[i];
    return static_cast<double>(suma) / n;
}

void extremos(const int datos[], int n, int& mayor, int& menor)
{
    mayor = datos[0];
    menor = datos[0];

    for (int i = 1; i < n; i++)
    {
        if (datos[i] > mayor)
            mayor = datos[i];
        if (datos[i] < menor)
            menor = datos[i];
    }
}

int contarSobre(const int datos[], int n, double umbral)
{
    int cuantos = 0;
    for (int i = 0; i < n; i++)
        if (datos[i] > umbral)
            cuantos++;
    return cuantos;
}

int contarDigitos(const std::string& s)
{
    int cuantos = 0;
    for (int i = 0; i < static_cast<int>(s.length()); i++)
        if (s.at(i) >= '0' && s.at(i) <= '9')
            cuantos++;
    return cuantos;
}
```

El tamaño va como parámetro porque dentro de la función el arreglo ya no es un arreglo, es la dirección de su primera casilla, y de ahí no se puede recuperar cuántos elementos tenía.

**Salida**

```
SG-11-VIGA-A3 13 3
media 120.75
mayor 130 menor 112
sobre la media 4
sobre 125 2
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| Las cuatro funciones con el arreglo recibido como `const` | 3 |
| `extremos` entrega sus dos resultados por referencia | 2 |
| `contarSobre` sirve para los dos umbrales sin cambiar una línea | 2 |
| Los cinco renglones correctos y la explicación del tamaño como parámetro | 3 |

**Error que más se ve**

Escriben `contarDigitos` comparando contra los números 0 y 9 en lugar de los caracteres `'0'` y `'9'`; lo delata que el conteo sale en cero, porque ningún carácter imprimible tiene un código tan bajo.

---

## Semana 11 · Unidad 9 · Registros

### 11.1 · Reconocer

**Solución**

`Muestra b = a;` copia campo por campo, así que cambiar `b.valor` no toca a `a`. `tabla[1]` recibió esa copia y conserva la marca de tiempo 100. La suma de los campos es 4 más 8, o sea 12, pero `sizeof(Muestra)` da 16: el compilador mete cuatro bytes de relleno después del `int` para que el `double` quede alineado a ocho. El arreglo de tres ocupa 48 por la misma razón. Antes de las dos asignaciones, los dos campos de `tabla[2]` traen basura, porque declarar el arreglo no inicializa nada.

**Salida**

```
2.5 9.9
100 1.25
16 48
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| Las tres líneas exactas | 3 |
| Explica que la asignación copia y que desde ahí son dos registros independientes | 3 |
| Explica el relleno: suma 12, ocupa 16, y el arreglo 48 | 4 |

**Error que más se ve**

Contestan 12 y 36 en la tercera línea sumando los campos a mano; lo delata que el número cuadra con la aritmética y no con lo que el programa imprime.

### 11.2 · Aplicar

**Solución**

```cpp
struct Muestra {
    int t_ms;
    double valor;
};

Muestra crear(int t, double v)
{
    Muestra m;
    m.t_ms = t;
    m.valor = v;
    return m;
}

int main()
{
    Muestra tabla[6];

    tabla[0] = crear(0, 2.41);
    tabla[1] = crear(100, 2.65);
    tabla[2] = crear(200, 3.12);
    tabla[3] = crear(300, 2.98);
    tabla[4] = crear(400, 3.44);
    tabla[5] = crear(500, 3.05);

    int n = sizeof(tabla) / sizeof(tabla[0]);

    double suma = 0.0;
    int iMax = 0;

    for (int i = 0; i < n; i++)
    {
        suma += tabla[i].valor;

        if (tabla[i].valor > tabla[iMax].valor)
            iMax = i;
    }

    std::cout << "t_ms\tvalor\n";
    for (int i = 0; i < n; i++)
        std::cout << tabla[i].t_ms << "\t" << tabla[i].valor << "\n";

    std::cout << "media " << suma / n << "\n";
    std::cout << "maximo " << tabla[iMax].valor << " en " << tabla[iMax].t_ms << " ms\n";
    return 0;
}
```

**Salida**

```
t_ms	valor
0	2.41
100	2.65
200	3.12
300	2.98
400	3.44
500	3.05
media 2.94167
maximo 3.44 en 400 ms
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| El registro con sus dos campos y la función que lo arma y lo devuelve | 3 |
| Un solo recorrido calcula la suma y el índice del máximo | 3 |
| Guarda el índice y no el valor, y por eso puede reportar la marca de tiempo | 2 |
| La tabla, la media y el máximo correctos | 2 |

**Error que más se ve**

Guardan el valor máximo en una variable suelta y después no saben a qué tiempo corresponde; lo delata que agregan un segundo recorrido para buscar en qué posición estaba.

### 11.3 · Integrar

**Solución**

```cpp
bool valida(const Muestra& m)
{
    if (m.t_ms < 0 || m.valor <= 0.0)
        return false;
    return true;
}

double mediaValidas(const Muestra tabla[], int n, int& usadas)
{
    double suma = 0.0;
    usadas = 0;

    for (int i = 0; i < n; i++)
    {
        if (valida(tabla[i]))
        {
            suma += tabla[i].valor;
            usadas++;
        }
        else
        {
            std::cout << "descartado " << tabla[i].t_ms << " ms\n";
        }
    }

    return suma / usadas;
}

void extremos(const Muestra tabla[], int n, int& iMax, int& iMin)
{
    iMax = -1;
    iMin = -1;

    for (int i = 0; i < n; i++)
    {
        if (valida(tabla[i]))
        {
            if (iMax < 0 || tabla[i].valor > tabla[iMax].valor)
                iMax = i;
            if (iMin < 0 || tabla[i].valor < tabla[iMin].valor)
                iMin = i;
        }
    }
}
```

Un registro se pasa por referencia constante porque copiarlo duplica todos sus campos en cada llamada, y `const` promete que la función no lo va a modificar. Con dieciséis bytes la diferencia no se nota; con un registro de cien campos, sí.

**Salida**

```
descartado 200 ms
registros 6 validos 5
media 2.906
maximo 3.44 en 400 ms
minimo 2.41 en 0 ms
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| `valida` recibe por referencia constante y decide con una sola condición | 2 |
| La media se calcula solo sobre las válidas y el conteo sale por referencia | 3 |
| `extremos` ignora la inválida y arranca sin suponer que la primera sirve | 3 |
| Los cinco renglones correctos | 2 |

**Error que más se ve**

Arrancan `iMin` en el índice 0 sin revisar si esa muestra es válida, y cuando la inválida es la primera el mínimo reportado es la que se descartó; lo delata que el mínimo impreso aparece también en la línea de descartados.

---

## Semana 12 · Unidad 10 · Punteros, virtuales y abstractas

### 12.1 · Reconocer

**Solución**

`*p = 800;` escribe a través del puntero, así que `cuenta` cambia sin que su nombre aparezca en la línea, y `p == &cuenta` es verdadero, que se imprime como 1. `convertir` es virtual: la decisión de cuál corre la toma el objeto real al ejecutar, y como el objeto es un `Termopar`, 800 por 0.25 da 200. `escala` no es virtual: la decisión la toma el compilador con el tipo del puntero, que es `Sensor*`, y da 1. Si se borra el `delete`, se fuga el objeto reservado con `new`. Si en lugar de eso se le quita el `virtual` al destructor, el `delete` sí libera memoria pero solo destruye la parte de la base, y lo que la hija hubiera reservado se queda.

**Salida**

```
800 1
200 1
25
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| Las tres líneas exactas | 3 |
| Explica quién decide y cuándo, con el par 200 y 1 como evidencia | 4 |
| Distingue la fuga por `delete` faltante de la fuga por destructor no virtual | 3 |

**Error que más se ve**

Contestan `200 0.25` en la segunda línea, aplicando el despacho dinámico a las dos funciones; lo delata que ignoran la única palabra que separa una línea de la otra.

### 12.2 · Aplicar

**Solución**

```cpp
class Sensor {
public:
    Sensor(std::string e) : etiqueta(e) {}
    virtual double convertir(int cuenta) = 0;
    virtual std::string unidad() = 0;
    std::string getEtiqueta() { return etiqueta; }
    virtual ~Sensor() {}
protected:
    std::string etiqueta;
};

class Termopar : public Sensor {
public:
    Termopar(std::string e, double p) : Sensor(e), pendiente(p) {}
    double convertir(int cuenta) override { return cuenta * pendiente; }
    std::string unidad() override { return "C"; }
private:
    double pendiente;
};

class Extensometro : public Sensor {
public:
    Extensometro(std::string e, double f) : Sensor(e), factor(f) {}
    double convertir(int cuenta) override { return cuenta / factor; }
    std::string unidad() override { return "um/m"; }
private:
    double factor;
};

int main()
{
    Sensor* canales[3];
    canales[0] = new Termopar("TC-04", 0.25);
    canales[1] = new Extensometro("SG-11", 2.05);
    canales[2] = new Termopar("TC-05", 0.50);

    int cuentas[3] = {400, 410, 300};
    int sobre = 0;

    for (int i = 0; i < 3; i++)
    {
        double v = canales[i]->convertir(cuentas[i]);

        if (v > 120.0)
            sobre++;

        std::cout << canales[i]->getEtiqueta() << " " << v << " "
                  << canales[i]->unidad() << "\n";
    }

    std::cout << "sobre 120: " << sobre << "\n";

    for (int i = 0; i < 3; i++)
        delete canales[i];

    return 0;
}
```

**Salida**

```
TC-04 100 C
SG-11 200 um/m
TC-05 150 C
sobre 120: 2
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| Clase abstracta con dos funciones virtuales puras y destructor virtual | 3 |
| Un solo ciclo recorre los tres sin preguntar de qué tipo son | 3 |
| Los tres `new` tienen su `delete` | 2 |
| Los cuatro renglones correctos | 2 |

**Error que más se ve**

Declaran el arreglo como `Sensor canales[3]` en lugar de punteros y el compilador rechaza el programa porque la clase es abstracta; lo delata que el error habla de instanciar un tipo abstracto y no de la conversión.

### 12.3 · Integrar

**Solución**

```cpp
std::unique_ptr<Sensor> canales[2];
canales[0] = std::make_unique<Termopar>("TC-04", 0.25);
canales[1] = std::make_unique<Extensometro>("SG-11", 2.05);

const int N = 4;
Muestra* tabla = new Muestra[N];

for (int i = 0; i < N; i++)
{
    tabla[i].t_ms = i * 100;
    tabla[i].cuenta = 400.0 + 20.0 * i;
}

for (int c = 0; c < 2; c++)
{
    double suma = 0.0;

    for (int i = 0; i < N; i++)
        suma += canales[c]->convertir(tabla[i].cuenta);

    std::cout << canales[c]->getEtiqueta() << " media "
              << suma / N << " " << canales[c]->unidad() << "\n";
}

delete[] tabla;
```

Lo que desapareció es el ciclo final que borraba los sensores uno por uno, y con él la posibilidad de olvidarlo o de que una salida temprana lo saltara. El `unique_ptr` libera en su destructor, así que la liberación ocurre aunque el programa salga por otro camino. La tabla sigue pidiendo `delete[]` porque se reservó con `new[]`.

**Salida**

```
TC-04 media 107.5 C
SG-11 media 209.756 um/m
new sin pareja: 0
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| Los sensores en `unique_ptr` creados con `make_unique` | 3 |
| La tabla con `new[]` y su `delete[]`, no con `delete` a secas | 3 |
| Las dos medias correctas | 2 |
| La explicación de qué líneas se fueron y por qué | 2 |

**Error que más se ve**

Liberan la tabla con `delete tabla;` sin corchetes; el programa muchas veces corre igual, y lo delata que el mismo error en un arreglo de objetos con destructor deja de llamar a todos menos al primero.

---

## Semana 13 · Unidad 11 · Entrada y salida

### 13.1 · Reconocer

**Solución**

La bandera de fin de archivo se enciende después de una lectura que falla, no antes, así que el ciclo entra una cuarta vez, la lectura no consigue nada y el cuerpo imprime otra vez lo que había quedado en `t` y en `v` de la vuelta anterior. El conteo llega a 4. En el archivo que no existe, la extracción ni siquiera se intenta porque el flujo ya está en estado de fallo, y por eso `n` conserva el 7 con el que se declaró. La condición que arregla el ciclo es la lectura misma: `while (in >> etiqueta >> t >> v)`.

**Salida**

```
100 2.41
200 2.65
300 3.12
300 3.12
lineas 4
0 7
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| Las seis líneas exactas, con el renglón repetido | 4 |
| Explica que `eof` se enciende después de fallar | 3 |
| Escribe la condición correcta y explica el 7 que sobrevive | 3 |

**Error que más se ve**

Predicen `0 0` en la línea repetida suponiendo que la lectura fallida limpia las variables; lo delata que en este toolchain el flujo ya venía en fallo y no las tocó.

### 13.2 · Aplicar

**Solución**

```cpp
std::ofstream out("horno.txt");

if (!out.is_open())
{
    std::cout << "no se pudo escribir\n";
    return 1;
}

out << "TC-04 0 21.5\n";
out << "TC-04 100 48.2\n";
out << "TC-04 200 76.9\n";
out << "TC-04 300 98.4\n";
out << "TC-04 400 121.7\n";
out << "TC-04 500 133.0\n";
out.close();

std::ifstream in("horno.txt");

if (!in.is_open())
{
    std::cout << "no se pudo abrir horno.txt\n";
    return 1;
}

std::string etiqueta;
int t = 0;
double c = 0.0;

int n = 0;
double suma = 0.0;
int sobre = 0;

while (in >> etiqueta >> t >> c)
{
    n++;
    suma += c;

    if (c > 100.0)
        sobre++;
}
in.close();
```

**Salida**

```
registros 6
media 83.2833
sobre 100 C 2
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| `is_open` revisado en la escritura y en la lectura | 3 |
| El ciclo se controla con la lectura y no con un contador ni con `eof` | 3 |
| Los dos archivos se cierran | 2 |
| Los tres renglones correctos | 2 |

**Error que más se ve**

Recorren el archivo con un `for` de seis vueltas porque saben cuántos renglones escribieron; lo delata que el programa deja de servir en cuanto el archivo lo genera otro.

### 13.3 · Integrar

**Solución**

```cpp
struct Registro {
    std::string etiqueta;
    int t_ms;
    double celsius;
};

class Canal {
public:
    Canal(std::string e, double lim)
    {
        etiqueta = e;
        limite = lim;
        suma = 0.0;
        n = 0;
        alarmas = 0;
        descartados = 0;
    }

    void agregar(const Registro& r)
    {
        if (r.celsius < -200.0 || r.celsius > 1300.0)
        {
            descartados++;
        }
        else
        {
            suma += r.celsius;
            n++;

            if (r.celsius > limite)
                alarmas++;
        }
    }

    double media() { return suma / n; }
    int getN() { return n; }
    int getAlarmas() { return alarmas; }
    int getDescartados() { return descartados; }
    std::string getEtiqueta() { return etiqueta; }

private:
    std::string etiqueta;
    double limite;
    double suma;
    int n;
    int alarmas;
    int descartados;
};
```

La lectura del archivo se detiene por lo que ocurra primero:

```cpp
while (leidos < 10 && in >> tabla[leidos].etiqueta >> tabla[leidos].t_ms >> tabla[leidos].celsius)
    leidos++;
```

La media de las cinco aceptadas es 422.8 entre 5, o sea 84.56.

**Salida**

```
TC-04
leidos 6
aceptados 5
descartados 1
media 84.56
alarmas 2
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| `is_open` revisado antes de leer, con salida limpia si falla | 2 |
| El ciclo se detiene por fin de archivo o por capacidad, lo que llegue primero | 3 |
| La clase valida y acumula, `main` solo coordina | 3 |
| Los seis renglones correctos | 2 |

**Error que más se ve**

Ponen la condición de capacidad después de la lectura, así que el registro número once se lee sobre el final del arreglo antes de que nadie revise; lo delata que con archivos largos el programa escribe fuera del arreglo sin ningún aviso.

---

## Semana 14 · Unidad 12 · Sobrecarga y plantillas

### 14.1 · Reconocer

**Solución**

La suma de fuerzas opera componente por componente: 150.5 y 60. La comparación con `Fuerza(150.5, 60.0)` es verdadera y se imprime como 1. La plantilla genera dos funciones concretas, una con `T` igual a `int` y otra con `T` igual a `double`, y en el ejecutable solo quedan esas dos: la plantilla misma no llega, es una receta. `mayor(f1, f2)` no compila porque el cuerpo pide `a > b` y `Fuerza` no define el operador mayor que. El error aparece en la primera llamada, no donde se escribió la plantilla.

**Salida**

```
150.5 60
1
9 2.5
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| Las tres líneas exactas | 3 |
| Dos instanciaciones, con los tipos correctos, y la plantilla fuera del ejecutable | 4 |
| Explica que el error de `mayor(f1, f2)` sale en la llamada y por qué | 3 |

**Error que más se ve**

Contestan que la plantilla genera una sola función que sirve para los dos tipos; lo delata que confunden el mecanismo con el de un lenguaje que resuelve tipos al ejecutar.

### 14.2 · Aplicar

**Solución**

```cpp
class Medicion {
public:
    Medicion(double v, std::string u) : valor(v), unidad(u) {}

    Medicion operator+(const Medicion& o) { return Medicion(valor + o.valor, unidad); }
    bool operator==(Medicion o) { return valor == o.valor && unidad == o.unidad; }
    bool operator>(const Medicion& o) { return valor > o.valor; }

    double getValor() { return valor; }
    std::string getUnidad() { return unidad; }

private:
    double valor;
    std::string unidad;
};

std::ostream& operator<<(std::ostream& os, Medicion m)
{
    os << m.getValor() << " " << m.getUnidad();
    return os;
}

template <typename T>
T mayor(T a, T b)
{
    if (a > b)
        return a;
    return b;
}

template <typename T>
double promedio(const T datos[], int n)
{
    double suma = 0.0;

    for (int i = 0; i < n; i++)
        suma += datos[i];

    return suma / n;
}
```

**Salida**

```
218.8 kPa
0 1
120.5 kPa
7 9.75
108.8
370
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| Suma, igualdad y mayor que sobrecargados como funciones miembro | 3 |
| El operador de salida como función libre que devuelve el flujo | 2 |
| Las dos plantillas funcionan con los tipos pedidos sin una línea específica de `Medicion` | 3 |
| Los seis renglones correctos | 2 |

**Error que más se ve**

Declaran `bool operator==(const Medicion& o)` sin marcarlo `const` y el compilador de C++20 rechaza la comparación con `error C2666`, porque el lenguaje sintetiza también la versión invertida y las dos empatan; se sale del paso recibiendo el operando por valor.

### 14.3 · Integrar

**Solución**

```cpp
const int CAPACIDAD = 5;

struct Muestra {
    int t_ms;
    double valor;
};

std::ostream& operator<<(std::ostream& os, Muestra m)
{
    os << m.t_ms << " ms " << m.valor;
    return os;
}

template <typename T>
class Buffer {
public:
    Buffer() { n = 0; }

    void agregar(T v)
    {
        if (n < CAPACIDAD)
        {
            datos[n] = v;
            n++;
        }
        else
        {
            std::cout << "buffer lleno\n";
        }
    }

    T obtener(int i) { return datos[i]; }
    int tamano() { return n; }

private:
    T datos[CAPACIDAD];
    int n;
};
```

El aviso de búfer lleno se imprime durante el llenado, en la sexta llamada a `agregar`, y el conteo se imprime después, cuando el ciclo ya terminó. Por eso el mensaje aparece arriba aunque hable del final del arreglo.

**Salida**

```
volts 3 media 2.72667
buffer lleno
registro 5
0 ms 2.41
100 ms 2.66
200 ms 2.91
300 ms 3.16
400 ms 3.41
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| La plantilla de clase sirve para `double` y para `Muestra` sin cambios | 3 |
| El rechazo por capacidad no escribe fuera del arreglo | 3 |
| El operador de salida de `Muestra` imprime en el formato pedido | 2 |
| Los renglones correctos y la explicación del orden | 2 |

**Error que más se ve**

Definen las funciones de la plantilla en un `.cpp` aparte y el enlazador no encuentra la versión concreta; lo delata que el error es LNK2019 y no un error de compilación.

---

## Semana 15 · Unidad 13 · Manejo de excepciones

### 15.1 · Reconocer

**Solución**

Se imprime la `A`, después `2.5` con su espacio, y en ese punto `at(9)` lanza `std::out_of_range` porque la cadena tiene cinco caracteres. El `throw` abandona el bloque y no vuelve, así que la `B` no se ejecuta nunca. El primer `catch` es el que corresponde al tipo lanzado y se imprime la `C`; el segundo no se toca, porque en cuanto uno atrapa, los demás se saltan. El programa sigue después del bloque y termina la línea con `E`. En el segundo bloque el `catch` de `exception` sí atrapa una `invalid_argument`, porque `invalid_argument` desciende de `exception`, y `what()` devuelve el mensaje con el que se construyó.

**Salida**

```
A2.5 CE
divisor cero
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| Las dos líneas exactas | 4 |
| Explica que el `throw` no regresa al bloque y por eso no hay `B` | 3 |
| Explica la herencia entre `invalid_argument` y `exception` | 3 |

**Error que más se ve**

Escriben `ACBD` porque suponen que el programa retoma el `try` después del `catch`; lo delata que meten la `B` en una salida donde el bloque ya se había abandonado.

### 15.2 · Aplicar

**Solución**

```cpp
class Calibracion {
public:
    Calibracion(std::string e, double p, double c)
    {
        if (p == 0.0)
            throw std::invalid_argument("pendiente cero en " + e);

        etiqueta = e;
        pendiente = p;
        cero = c;
    }

    double convertir(double volts) { return (volts - cero) / pendiente; }
    std::string getEtiqueta() { return etiqueta; }

private:
    std::string etiqueta;
    double pendiente;
    double cero;
};

double resistencia(double volts, double amperes)
{
    if (amperes == 0.0)
        throw std::runtime_error("corriente cero, no hay resistencia que medir");

    return volts / amperes;
}
```

**Salida**

```
TC-04 181 C
error: pendiente cero en TC-09
24 ohm
error: corriente cero, no hay resistencia que medir
el programa sigue
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| El constructor lanza antes de dejar el objeto a medio armar | 3 |
| Los tipos lanzados son los de `stdexcept` y no cadenas sueltas | 2 |
| Todos los `catch` reciben por referencia constante | 2 |
| Las cinco líneas correctas y el programa termina normal | 3 |

**Error que más se ve**

Asignan los miembros y luego revisan la pendiente, así que el objeto alcanza a existir mal antes de que la excepción salga; lo delata que la validación aparece en el renglón siguiente a las asignaciones.

### 15.3 · Integrar

**Solución**

```cpp
void abrir(std::ifstream& in, const std::string& ruta)
{
    in.open(ruta);

    if (!in.is_open())
        throw std::runtime_error("no se pudo abrir " + ruta);
}
```

El `try` interior vive dentro del ciclo, que es lo que permite reportar la línea corta y seguir leyendo:

```cpp
while (in >> etiqueta >> celsius)
{
    try
    {
        char zona = etiqueta.at(6);
        suma += celsius;
        buenas++;
        std::cout << "zona " << zona << " " << celsius << "\n";
    }
    catch (const std::out_of_range&)
    {
        malas++;
        std::cout << "linea mal formada: " << etiqueta << "\n";
    }
}
```

La media es 168.1 entre 3, o sea 56.0333, porque la línea descartada tampoco entra en la suma.

**Salida**

```
zona A 21.5
zona B 48.2
linea mal formada: TC-04
zona C 98.4
buenas 3 malas 1
media 56.0333
error: no se pudo abrir no_existe.txt
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| La función de apertura lanza `runtime_error` con la ruta en el mensaje | 3 |
| El `try` de la línea corta está dentro del ciclo y la lectura continúa | 3 |
| La suma no incluye la línea rechazada | 2 |
| Los siete renglones correctos | 2 |

**Error que más se ve**

Ponen el `try` alrededor del ciclo completo y la primera línea mal formada detiene la lectura; lo delata que la salida termina en la línea rechazada y las que faltaban nunca se procesan.

---

## Semana 16 · Unidad 14 · Recursión y concurrencia

### 16.1 · Reconocer

**Solución**

`suma(5)` baja hasta el caso base y arma el resultado de regreso: 15. `pasos(64)` divide entre dos en cada llamada, con `n` valiendo 64, 32, 16, 8, 4, 2 y 1, o sea seis llamadas que suman uno más la de abajo, y llegan a estar vivos siete marcos al mismo tiempo, incluido el del caso base. `potencia(2.0, 10)` da 1024. Con exponente -1 el caso base compara contra cero exacto, el argumento se aleja en cada llamada y nunca lo alcanza: el programa consume la pila y muere de golpe. No se cuelga como un ciclo infinito porque la pila tiene un tamaño fijo y se agota.

**Salida**

```
15
6
1024
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| Las tres líneas exactas | 3 |
| La cadena de `pasos(64)` con sus valores y el número de marcos vivos | 4 |
| Explica el caso base inalcanzable y por qué termina en lugar de colgarse | 3 |

**Error que más se ve**

Cuentan seis marcos porque olvidan el de la llamada que devuelve cero; lo delata que la cadena que dibujan sí llega a 1 pero el conteo no lo incluye.

### 16.2 · Aplicar

**Solución**

```cpp
int buscar(const int tabla[], int izq, int der, int objetivo)
{
    if (izq > der)
        return -1;

    int medio = (izq + der) / 2;

    if (tabla[medio] == objetivo)
        return medio;

    if (tabla[medio] < objetivo)
        return buscar(tabla, medio + 1, der, objetivo);

    return buscar(tabla, izq, medio - 1, objetivo);
}

double sumaRec(const double datos[], int n)
{
    if (n <= 0)
        return 0.0;
    return datos[n - 1] + sumaRec(datos, n - 1);
}

std::mutex candado;
long long total = 0;

void sumar(int veces)
{
    for (int i = 0; i < veces; i++)
    {
        std::lock_guard<std::mutex> cerrojo(candado);
        total = total + 1;
    }
}
```

Los dos `jthread` se declaran dentro de un bloque y se unen solos al salir de él, así que la impresión de después ve el total completo. Sin el candado, `total = total + 1` son tres pasos, leer, sumar y escribir, y dos hilos que los entrelazan pierden incrementos: el total sale abajo de 200000 y distinto en cada corrida. Con el candado, solo un hilo tiene el objeto a la vez y ningún incremento se pierde.

**Salida**

```
4
-1
14.6
200000
```

La corrida sin `lock_guard` en esta máquina dio 175983, 100000 y 100567 en tres intentos seguidos. El segundo número es el que más enseña: cien mil exactos quiere decir que un hilo pisó por completo el trabajo del otro. Cualquier resultado abajo de 200000 vale para el ejercicio, y no se le puede pedir a nadie que reproduzca los mismos tres.

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| La búsqueda es recursiva de verdad, con caso base para el fracaso | 3 |
| La suma recursiva no usa ningún ciclo | 2 |
| El candado se toma con `lock_guard` y los hilos se unen antes de imprimir | 3 |
| Los cuatro valores y los tres totales sin candado anotados | 2 |

**Error que más se ve**

Imprimen el total dentro del mismo bloque donde viven los `jthread`, así que leen la variable antes de que los hilos terminen; lo delata que el número impreso es menor que 200000 aun con el candado puesto.

### 16.3 · Integrar

**Solución**

```cpp
int mayorRec(const int datos[], int n)
{
    if (n == 1)
        return datos[0];

    int resto = mayorRec(datos, n - 1);

    if (datos[n - 1] > resto)
        return datos[n - 1];

    return resto;
}

void leer(const std::string& ruta, Registro tabla[], int capacidad, int& leidos)
{
    std::ifstream in(ruta);

    if (!in.is_open())
        throw std::runtime_error("no se pudo abrir " + ruta);

    leidos = 0;

    while (leidos < capacidad &&
           in >> tabla[leidos].etiqueta >> tabla[leidos].t_ms >> tabla[leidos].cuenta)
        leidos++;

    in.close();
}
```

La media de las cuatro cuentas es 448. Convertida con el termopar de pendiente 0.25 da 112 grados, y con el extensómetro de factor 2.05 da 218.537 micrómetros por metro.

**Salida**

```
registros 4
cuenta maxima 512
TC-04 media 112 C
SG-11 media 218.537 um/m
error: no se pudo abrir no_existe.txt
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| El registro, la lectura con `is_open` y la excepción con la ruta en el mensaje | 3 |
| La jerarquía abstracta recorrida por un solo ciclo, sobre `unique_ptr` | 3 |
| La función recursiva del máximo, sin ciclos | 2 |
| Los cinco renglones correctos | 2 |

**Error que más se ve**

Escriben `mayorRec` con caso base en `n == 0` y devuelven cero, así que un arreglo de cuentas negativas reportaría cero como máximo; lo delata que el caso base inventa un valor que no está en los datos.

---

## Semana 17 · Cierre · Proyecto integrador

### 17.1 · Reconocer

**Solución**

Los cuatro defectos, uno por criterio de la rúbrica:

1. Correctitud: `procesar` no revisa `is_open`, el archivo no existe, el ciclo no da ni una vuelta y `n` queda en cero. La división entre cero en punto flotante no truena, produce un valor que no es número, y el programa lo reporta como si fuera un resultado.
2. Diseño: `procesar` lee el archivo, imprime cada registro, calcula la media y además la imprime. Son al menos dos funciones pegadas.
3. Eficiencia y memoria: hay dos `new` y un solo `delete`. El objeto `respaldo` se fuga completo. Y el `delete principal` tampoco hace todo su trabajo, porque el destructor de la base no es virtual, así que solo corre `~Sensor` y la parte de `Termopar` nunca se destruye. La salida lo enseña: aparece `cierra Sensor` y no aparece `cierra Termopar`.
4. Documentación: el programa no dice en ningún momento que el archivo no se pudo abrir, así que quien lea la salida no tiene manera de saber qué pasó.

**Salida**

```
100
200
media -nan(ind)
resultado -nan(ind)
cierra Sensor
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| Las cinco líneas, incluida la forma en que este compilador imprime el no número | 3 |
| Los cuatro defectos, cada uno con su línea y su criterio | 4 |
| Cuenta dos `new` contra un `delete` y explica el destructor no virtual | 3 |

**Error que más se ve**

Reportan una sola fuga, la del puntero sin `delete`, y dan por buena la línea que sí libera; lo delata que la salida solo trae una de las dos líneas de destructor y nadie se pregunta por la que falta.

### 17.2 · Aplicar

**Solución**

```cpp
class Sensor {
public:
    Sensor(std::string e) : etiqueta(e) {}
    virtual double convertir(int cuenta) = 0;
    std::string getEtiqueta() { return etiqueta; }
    virtual ~Sensor() { std::cout << "cierra Sensor\n"; }
protected:
    std::string etiqueta;
};

class Termopar : public Sensor {
public:
    Termopar(std::string e, double p) : Sensor(e), pendiente(p) {}
    double convertir(int cuenta) override { return cuenta * pendiente; }
    ~Termopar() override { std::cout << "cierra Termopar\n"; }
private:
    double pendiente;
};

bool leer(const std::string& ruta, int cuentas[], int capacidad, int& leidos)
{
    std::ifstream in(ruta);

    if (!in.is_open())
        return false;

    std::string etiqueta;
    leidos = 0;

    while (leidos < capacidad && in >> etiqueta >> cuentas[leidos])
        leidos++;

    in.close();
    return true;
}

double media(const int datos[], int n)
{
    double suma = 0.0;

    for (int i = 0; i < n; i++)
        suma += datos[i];

    return suma / n;
}
```

Las cuatro últimas líneas aparecen porque ahora el destructor de la base es virtual y porque los dos objetos se destruyen. Cada uno imprime primero el de la clase derivada y luego el de la base, que es el orden en que se desarma un objeto. Los dos `unique_ptr` viven en `main` y se destruyen en orden inverso al de su declaración, así que primero se cierra `respaldo` y después `principal`.

**Salida**

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

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| Destructor virtual en la base y conversión virtual pura | 3 |
| Los dos punteros crudos reemplazados por `unique_ptr` con `make_unique` | 2 |
| La lectura separada del cálculo, y el aviso claro cuando el archivo no abre | 3 |
| Las diez líneas correctas y la explicación del orden de destrucción | 2 |

**Error que más se ve**

Cambian a `unique_ptr` pero dejan el destructor de la base sin `virtual`; lo delata que la fuga sigue ahí y la salida solo imprime `cierra Sensor` dos veces.

### 17.3 · Integrar

**Solución**

```cpp
struct Lectura {
    std::string etiqueta;
    int t_ms;
    int cuenta;
};

std::ostream& operator<<(std::ostream& os, Lectura l)
{
    os << l.etiqueta << " " << l.t_ms << " ms " << l.cuenta;
    return os;
}

template <typename T>
double promedio(const T datos[], int n)
{
    double suma = 0.0;

    for (int i = 0; i < n; i++)
        suma += datos[i];

    return suma / n;
}

int maxRec(const int datos[], int n)
{
    if (n == 1)
        return datos[0];

    int resto = maxRec(datos, n - 1);

    if (datos[n - 1] > resto)
        return datos[n - 1];

    return resto;
}

bool valida(const Lectura& l)
{
    if (l.cuenta < 0 || l.cuenta > 4095)
        return false;
    return true;
}

void leer(const std::string& ruta, Lectura tabla[], int capacidad, int& leidos)
{
    std::ifstream in(ruta);

    if (!in.is_open())
        throw std::runtime_error("no se pudo abrir " + ruta);

    leidos = 0;

    while (leidos < capacidad &&
           in >> tabla[leidos].etiqueta >> tabla[leidos].t_ms >> tabla[leidos].cuenta)
        leidos++;

    in.close();
}
```

`main` separa las válidas en un arreglo aparte, con lo que la estadística nunca toca la lectura de 5000, y la jerarquía se recorre con un solo ciclo sobre los `unique_ptr`. Las cuatro cuentas válidas promedian 448 y su máximo es 512.

**Salida**

```
descartada TC-04 200 ms 5000
leidas 5 validas 4
media de cuentas 448
cuenta maxima 512
TC-04 112 C
SG-11 218.537 um/m
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| Lectura con excepción, validación de rango y separación de las válidas | 3 |
| La plantilla y la función recursiva funcionan sobre el arreglo filtrado | 2 |
| La jerarquía abstracta sobre `unique_ptr`, recorrida sin preguntar tipos | 2 |
| El operador de salida de `Lectura` y los seis renglones correctos | 2 |
| Ningún `new` sin pareja y ninguna función que haga dos cosas | 1 |

**Error que más se ve**

Filtran las inválidas pero calculan la media sobre las cinco lecturas originales; lo delata que la media sale 1358.4 en lugar de 448, aunque la línea de descarte se imprima correctamente.
