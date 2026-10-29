#include <cassert>
#include <string>
#include <utility>
struct Registro { std::string nombre; };
class Estudiante {
    std::string nombre;
public:
    explicit Estudiante(std::string n):nombre(std::move(n)) {}
    void fijarNombre(std::string nombre) { this->nombre=std::move(nombre); }
    const std::string& verNombre() const { return nombre; }
    bool formasEquivalentes() const { return &this->nombre==&(*this).nombre; }
};
int main() {
    Registro r{"Ana"}; r.nombre="Luis";
    Estudiante e{"Ana"}; e.fijarNombre("Luis");
    assert(e.verNombre()==r.nombre && e.formasEquivalentes());
}
