# Inicializa los miembros antes de ejecutar el cuerpo

C++20 · La lista construye subobjetos; el cuerpo opera sobre ellos.

## Declaraciones relevantes

```cpp
class Circle : public Shape {
    double radio;
protected:
    double factorEscala;
public:
    Circle(unsigned id, double r);
};
```

## Lista de inicialización

```cpp
Circle::Circle(unsigned id, double r)
    : Shape(id, "Círculo"),
      radio(r > 0.0 ? r : 1.0),
      factorEscala(1.0) {
    // Aquí empieza el cuerpo.
}
```

## Orden real en este ejemplo

```text
1. Shape(id, "Círculo")
```

```text
2. radio
```

```text
3. factorEscala
```

```text
4. Cuerpo del constructor
```

Los miembros siguen su orden de declaración, aunque cambies el orden escrito en la lista. Las bases se construyen antes que los miembros.

## Asignar en el cuerpo es distinto

```cpp
Circle::Circle(unsigned id, double r)
    : Shape(id, "Círculo") {
    radio = r > 0.0 ? r : 1.0;
    factorEscala = 1.0;
}
```

Aquí los double sin inicializador previo reciben su valor mediante asignación. No deben leerse antes de ella. Un miembro string o vector ya habría sido construido antes de entrar al cuerpo.

## Cuándo hace falta inicializar

Las referencias deben enlazarse al construirse. Los miembros const necesitan inicialización y pueden tener un inicializador en su declaración. Para pasar argumentos al constructor de la base, usa la lista.

Los bloques son fragmentos didácticos. El ejemplo completo compilable está en `ejemplos/`.

Fuente: C++20: [class.base.init], [dcl.init].
