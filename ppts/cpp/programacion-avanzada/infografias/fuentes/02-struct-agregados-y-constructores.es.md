# Las llaves pueden inicializar un agregado o llamar un constructor

C++20 · La definición del tipo determina qué ocurre.

## Caso 1 · inicialización de agregado

```cpp
struct Punto {
    double x;
    double y;
};
Punto p{3.0, 5.0};
```

Los valores inicializan x y y en su orden de declaración. Este tipo es un agregado.

## Caso 2 · llamada a un constructor

```cpp
struct PuntoConConstructor {
    double x;
    double y;
    PuntoConConstructor(double a, double b)
        : x(a), y(b) {}
};
PuntoConConstructor q{3.0, 5.0};
```

Las llaves seleccionan el constructor. Ese constructor inicializa los miembros mediante su lista.

## ¿cuándo es un agregado?

Para una clase en C++20: no hay constructores declarados por el usuario ni heredados; no hay datos de instancia directos private o protected; no hay funciones virtuales; las bases no son virtuales, private ni protected.

## Una distinción útil

Que un struct no declare constructor no basta para llamarlo agregado. Una class con miembros public también puede ser un agregado.

## Compruébalo en código

```cpp
std::is_aggregate_v<Punto>                 // true
std::is_aggregate_v<PuntoConConstructor>   // false
```

Los bloques son fragmentos didácticos. El ejemplo completo compilable está en `ejemplos/`.

Fuente: C++20: [dcl.init.aggr], [dcl.init.list].
