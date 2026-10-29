# class y struct cambian los accesos predeterminados

C++20 · Las dos formas pueden tener métodos, constructores y herencia.

## Compara los valores por defecto

| Característica | class | struct |
| --- | --- | --- |
| Acceso a miembros | private | public |
| Acceso de herencia | private | public |
| Constructores y destructores | Sí | Sí |
| Métodos y funciones virtuales | Sí | Sí |
| Miembros private y protected | Sí | Sí |

## Un tipo con datos públicos

```cpp
struct Punto {
    double x{};
    double y{};
};
Punto p{3.0, 5.0};
```

## Un tipo con interfaz pública

```cpp
class Alumno {
    std::string nombre;
public:
    explicit Alumno(std::string n)
        : nombre(std::move(n)) {}
    const std::string& verNombre() const {
        return nombre;
    }
};
```

## Elige según el diseño

struct suele comunicar datos públicos relacionados. class suele expresar una interfaz que mantiene invariantes. Son convenciones de diseño; ambas palabras permiten controlar el acceso.

## Evita esta confusión

Usar struct no garantiza compatibilidad con C. Depende de los tipos, la disposición de memoria y la interfaz binaria.

Los bloques son fragmentos didácticos. El ejemplo completo compilable está en `ejemplos/`.

Fuente: C++20: [class.access], [class.access.base]. C++ Core Guidelines C.2 y C.8.
