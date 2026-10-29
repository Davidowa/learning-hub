#include <cassert>
#include <type_traits>
namespace simple { struct A {}; struct B:public A {}; }
namespace multiple { struct A {}; struct B {}; struct C:public A,public B {}; }
namespace multinivel { struct A {}; struct B:public A {}; struct C:public B {}; }
namespace jerarquica { struct A {}; struct B:public A {}; struct C:public A {}; struct D:public A {}; }
namespace diamante {
    struct A { int id{}; }; struct B:public A {}; struct C:public A {}; struct D:public B,public C {};
}
namespace virtuales {
    struct A { int id{}; }; struct B:virtual public A {}; struct C:virtual public A {}; struct D:public B,public C {};
}
static_assert(std::is_convertible_v<simple::B*,simple::A*>);
static_assert(std::is_convertible_v<multiple::C*,multiple::A*>);
static_assert(std::is_convertible_v<multiple::C*,multiple::B*>);
static_assert(std::is_convertible_v<multinivel::C*,multinivel::A*>);
static_assert(!std::is_convertible_v<diamante::D*,diamante::A*>);
static_assert(std::is_convertible_v<virtuales::D*,virtuales::A*>);
int main() {
    diamante::D d;
    auto* a1=static_cast<diamante::A*>(static_cast<diamante::B*>(&d));
    auto* a2=static_cast<diamante::A*>(static_cast<diamante::C*>(&d));
    assert(a1!=a2);
    virtuales::D v;
    auto* b=static_cast<virtuales::B*>(&v);auto* c=static_cast<virtuales::C*>(&v);
    assert(static_cast<virtuales::A*>(b)==static_cast<virtuales::A*>(c));
    v.id=9; assert(b->id==9 && c->id==9);
}
