# El acceso cambia según el lugar desde donde se usa el miembro

C++20 · Ejemplo con Circle : public Shape, sin declaraciones friend.

## Clase base

```cpp
class Shape {
private:
    unsigned id{};
protected:
    std::string nombre;
public:
    void mostrar() const;
};
```

## Clase derivada

```cpp
class Circle : public Shape {
public:
    void renombrar() {
        nombre = "Círculo";  // Permitido.
        // id = 1;         // Error.
    }
};
```

## Acceso a los miembros de shape

| Desde... | private: id | protected: nombre | public: mostrar() |
| --- | --- | --- | --- |
| Un método de Shape | Sí | Sí | Sí |
| Un método de Circle, sobre *this | No | Sí | Sí |
| Código externo, como main() | No | No | Sí |

## Una precisión sobre protected

Dentro de Circle, acceder al miembro no estático protegido exige un objeto Circle o derivado de Circle. Una referencia Shape& no permite ese acceso por sí sola.

## No confundas acceso con existencia

Los datos privados de Shape forman parte del subobjeto base de Circle, aunque Circle no pueda nombrarlos directamente.

## Alcance de la tabla

La herencia es public. Una base private o protected cambia el acceso heredado. Los miembros y amigos autorizados tienen reglas de acceso adicionales.

Los bloques son fragmentos didácticos. El ejemplo completo compilable está en `ejemplos/`.

Fuente: C++20: [class.access], [class.protected], [class.access.base].
