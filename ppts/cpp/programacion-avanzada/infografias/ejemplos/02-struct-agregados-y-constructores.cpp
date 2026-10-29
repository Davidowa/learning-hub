#include <cassert>
#include <type_traits>
struct Punto { double x; double y; };
struct PuntoConConstructor {
    double x; double y;
    PuntoConConstructor(double a,double b):x(a),y(b) {}
};
struct ConVirtual { virtual void f() {} };
class ClaseAgregada { public: int valor; };
static_assert(std::is_aggregate_v<Punto>);
static_assert(!std::is_aggregate_v<PuntoConConstructor>);
static_assert(!std::is_aggregate_v<ConVirtual>);
static_assert(std::is_aggregate_v<ClaseAgregada>);
int main() {
    Punto p{3.0,5.0}; PuntoConConstructor q{3.0,5.0};
    assert(p.x==q.x && p.y==q.y);
}
