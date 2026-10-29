# El mismo recorrido calcula áreas de objetos distintos

C++20 · Shape, Circle, Rectangle y Square.

## La jerarquía del ejemplo

```text
Circle → Shape; Rectangle → Shape; Square → Rectangle.
```

Square tiene una base directa: Rectangle. La cadena hasta Shape es herencia multinivel, no múltiple.

## Todas comparten la operación

Shape declara:

```cpp
virtual double area() const = 0;
virtual ~Shape() = default;
```

Circle redefine: pi × radio × radio. Rectangle redefine: base × altura. Square redefine: lado × lado. Las tres implementaciones usan const override.

## Un solo recorrido

```cpp
Circle c{5.0};
Rectangle r{4.0, 6.0};
Square s{3.0};
Shape* figuras[]{&c, &r, &s};
for (const Shape* figura : figuras) {
    std::cout << figura->area() << '
';
}
```

## Salida con dos decimales

```text
78.54
```

```text
24.00
```

```text
9.00
```

Orden de salida: Circle, Rectangle, Square. El programa completo fija la precisión con std::fixed y std::setprecision(2).

## Límites del modelo

Esta jerarquía es didáctica. Si Rectangle permite cambiar base y altura por separado, derivar Square puede romper ese contrato. Revisa los invariantes antes de reutilizar esta relación en otro diseño.

## Durante la construcción

Una llamada virtual desde un constructor o destructor se resuelve en la clase que está construyéndose o destruyéndose; no salta a una parte derivada que todavía no está activa.

Los bloques son fragmentos didácticos. El ejemplo completo compilable está en `ejemplos/`.

Fuente: C++20: [class.virtual], [class.cdtor]. C++ Core Guidelines C.120.
