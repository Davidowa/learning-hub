#include <cassert>
#include <iostream>
#include <string>
class Shape {
private:
    unsigned id{};
protected:
    std::string nombre;
public:
    void mostrar() const { std::cout<<id<<": "<<nombre<<'\n'; }
};
class Circle:public Shape {
public:
    void renombrar() { nombre="Círculo"; /* id=1; sería un error. */ }
    void otroCircle(Circle& otro) { otro.nombre="Círculo"; }
    // void soloBase(Shape& base) { base.nombre="Círculo"; } // Error.
    bool nombreCorrecto() const { return nombre=="Círculo"; }
};
int main() {
    Circle c, otro; c.renombrar(); c.otroCircle(otro);
    assert(c.nombreCorrecto() && otro.nombreCorrecto());
    c.mostrar();
}
