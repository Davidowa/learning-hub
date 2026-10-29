#include <cassert>
#include <cmath>
#include <iomanip>
#include <iostream>
#include <numbers>
#include <type_traits>
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
static_assert(std::is_abstract_v<Shape>);
static_assert(!std::is_abstract_v<Circle>);
static_assert(std::has_virtual_destructor_v<Shape>);
int main() {
    Circle c{5}; Shape* figura=&c;
    assert(std::abs(figura->area()-78.53981633974483)<1e-10);
    std::cout<<std::fixed<<std::setprecision(2)<<figura->area()<<'\n';
}
