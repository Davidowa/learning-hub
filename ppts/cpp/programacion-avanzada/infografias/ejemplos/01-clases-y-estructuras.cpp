#include <cassert>
#include <string>
#include <type_traits>
#include <utility>
struct Punto { double x{}; double y{}; };
class Alumno {
    std::string nombre;
public:
    explicit Alumno(std::string n) : nombre(std::move(n)) {}
    const std::string& verNombre() const { return nombre; }
};
struct Base { int dato = 42; };
struct DerivadaStruct : Base {};
class DerivadaClass : Base {};
static_assert(std::is_convertible_v<DerivadaStruct*, Base*>);
static_assert(!std::is_convertible_v<DerivadaClass*, Base*>);
int main() {
    Punto p{3.0,5.0}; Alumno a{"Ana"};
    assert(p.x==3.0 && p.y==5.0 && a.verNombre()=="Ana");
}
