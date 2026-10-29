#include <cassert>
#include <cmath>
#include <iomanip>
#include <iostream>
#include <numbers>
#include <string>
#include <type_traits>
#include <vector>
class Shape {
public:
    virtual ~Shape()=default;
    virtual double area() const=0;
};
class Circle:public Shape {
    double radio;
public:
    explicit Circle(double r):radio(r) {}
    double area() const override { return std::numbers::pi*radio*radio; }
};
// Jerarquía didáctica sin setters que cambien base y altura por separado.
class Rectangle:public Shape {
    double base,altura;
protected:
    double devolverBase() const { return base; }
public:
    Rectangle(double b,double h):base(b),altura(h) {}
    double area() const override { return base*altura; }
};
class Square:public Rectangle {
public:
    explicit Square(double lado):Rectangle(lado,lado) {}
    double area() const override { const double lado=devolverBase();return lado*lado; }
};
static_assert(std::is_base_of_v<Rectangle,Square>);
static_assert(std::is_base_of_v<Shape,Square>);
namespace construccion {
    inline std::vector<std::string> traza;
    struct Base {
        Base() { llamar(); }
        virtual ~Base() { llamar(); }
        virtual void llamar() { traza.push_back("Base"); }
    };
    struct Derivada:Base {
        Derivada() { llamar(); }
        ~Derivada() override { llamar(); }
        void llamar() override { traza.push_back("Derivada"); }
    };
}
int main() {
    Circle c{5.0}; Rectangle r{4.0,6.0}; Square s{3.0};
    Shape* figuras[]{&c,&r,&s};
    assert(std::abs(figuras[0]->area()-78.53981633974483)<1e-10);
    assert(figuras[1]->area()==24 && figuras[2]->area()==9);
    std::cout<<std::fixed<<std::setprecision(2);
    for(const Shape* figura:figuras) std::cout<<figura->area()<<'\n';
    { construccion::Derivada ejemplo; }
    assert((construccion::traza==std::vector<std::string>{"Base","Derivada","Derivada","Base"}));
}
