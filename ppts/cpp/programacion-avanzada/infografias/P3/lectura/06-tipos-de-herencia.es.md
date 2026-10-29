# Cuenta las bases directas y distingue los niveles

C++20 · En estos diagramas, la flecha apunta desde la derivada hacia su base.

## Simple

Una base directa.

```text
B → A
```

```cpp
class B : public A {};
```

## Múltiple

Dos o más bases directas.

```text
C → A y C → B
```

```cpp
class C : public A, public B {};
```

## Multinivel

Una derivada también actúa como base.

```text
C → B → A
```

```cpp
class B : public A {};
class C : public B {};
```

## Jerárquica

Varias derivadas comparten una base.

```text
B → A, C → A y D → A
```

```cpp
class B : public A {};
class C : public A {};
class D : public A {};
```

## Híbrida

Combina patrones de herencia. Un diamante combina varios niveles y bases múltiples.

```text
D → B y C; B → A; C → A.
```

## Diamante y base virtual

Sin virtual, D contiene dos subobjetos A: uno por cada rama. Con virtual en las dos ramas, comparte un solo A.

```cpp
struct A { int id{}; };
struct B : virtual public A {};
struct C : virtual public A {};
struct D : public B, public C {};
```

## No son categorías excluyentes

La forma de la jerarquía y el acceso de herencia son decisiones distintas. public, protected y private no significan simple o múltiple. La base virtual la inicializa la clase más derivada.

Los bloques son fragmentos didácticos. El ejemplo completo compilable está en `ejemplos/`.

Fuente: C++20: [class.derived], [class.mi], [class.base.init].
