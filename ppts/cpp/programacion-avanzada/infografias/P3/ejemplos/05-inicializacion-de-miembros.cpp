#include <cassert>
#include <string>
#include <utility>
#include <vector>
class Shape {
    unsigned id;
    std::string nombre;
public:
    Shape(unsigned i,std::string n):id(i),nombre(std::move(n)) {}
    virtual ~Shape()=default;
    unsigned verId() const { return id; }
    const std::string& verNombre() const { return nombre; }
};
class Circle:public Shape {
    double radio;
protected:
    double factorEscala;
public:
    Circle(unsigned id,double r);
    double verRadio() const { return radio; }
};
Circle::Circle(unsigned id,double r)
    :Shape(id,"Círculo"),radio(r>0.0?r:1.0),factorEscala(1.0) {}
// Alternativa independiente: asignación en el cuerpo, sin leer antes los double.
class CircleAsignacion:public Shape {
    double radio;
protected:
    double factorEscala;
public:
    CircleAsignacion(unsigned id,double r):Shape(id,"Círculo") {
        radio=r>0.0?r:1.0; factorEscala=1.0;
    }
    double verRadio() const { return radio; }
};
struct Enlace { const int id; double& ref; Enlace(int i,double& r):id(i),ref(r) {} };
struct ConInicializador { const int id=7; };
struct Paso {
    std::vector<int>& traza;
    Paso(std::vector<int>& t,int n):traza(t) { traza.push_back(n); }
};
struct BaseOrden { BaseOrden(std::vector<int>& t) { t.push_back(0); } };
struct Orden:BaseOrden {
    Paso primero; Paso segundo;
    explicit Orden(std::vector<int>& t):BaseOrden(t),primero(t,1),segundo(t,2) { t.push_back(3); }
};
int main() {
    Circle c{23,-1.0}; CircleAsignacion a{23,-1.0};
    assert(c.verRadio()==1 && c.verRadio()==a.verRadio() && c.verId()==23);
    double valor=2; Enlace e{3,valor}; e.ref=4;
    assert(valor==4 && e.id==3 && ConInicializador{}.id==7);
    std::vector<int> t; Orden orden{t}; assert((t==std::vector<int>{0,1,2,3}));
}
