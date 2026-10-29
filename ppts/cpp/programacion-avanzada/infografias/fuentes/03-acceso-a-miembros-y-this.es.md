# this apunta al objeto que ejecuta el método

C++20 · El acceso depende del miembro, no de escribir class o struct.

## Acceso directo a un miembro público

```cpp
struct Registro {
    std::string nombre;
};
Registro r{"Ana"};
r.nombre = "Luis";
```

## Interfaz de una clase

```cpp
class Estudiante {
    std::string nombre;
public:
    explicit Estudiante(std::string n)
        : nombre(std::move(n)) {}
    void fijarNombre(std::string nombre) {
        this->nombre = std::move(nombre);
    }
    const std::string& verNombre() const {
        return nombre;
    }
};
```

## Desde fuera del objeto

```cpp
Estudiante e{"Ana"};
e.fijarNombre("Luis");
// e.nombre = "Luis";  // Error: privado.
```

## Dos formas equivalentes

```cpp
this->nombre
(*this).nombre
```

## Lee la asignación

En `this->nombre = nombre`, la izquierda es el miembro y la derecha es el parámetro. `this->` evita el conflicto de nombres. Si no hay conflicto, normalmente es opcional.

## Recuerda

this existe en métodos no estáticos. En un método const apunta a un objeto const. Los métodos públicos expresan operaciones del tipo; no es obligatorio crear un getter y un setter por cada dato.

Los bloques son fragmentos didácticos. El ejemplo completo compilable está en `ejemplos/`.

Fuente: C++20: [class.this], [class.access].
