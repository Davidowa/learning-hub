#include <cassert>
#include <iostream>
#include <sstream>
#include <string>
class Estudiante {
    char matricula[12] = "123456";
public:
    const char* getMatricula() const;
};
const char* Estudiante::getMatricula() const { return matricula; }
int main() {
    int edad = 20;
    int* ptr = &edad;
    assert(ptr == &edad && *ptr == edad);
    std::ostringstream out;
    out << edad << '\n' << &edad << '\n' << ptr << '\n' << *ptr << '\n';
    *ptr = 25;
    out << edad << '\n';
    std::istringstream in{out.str()};
    std::string val,addr1,addr2,deref,after;
    std::getline(in,val); std::getline(in,addr1); std::getline(in,addr2);
    std::getline(in,deref); std::getline(in,after);
    assert(val == "20" && addr1 == addr2 && deref == "20" && after == "25");
    char matricula[12] = "123456";
    char* cp = matricula;
    assert(cp == &matricula[0]);
    assert(*cp == '1' && std::string(cp) == "123456");
    for (int i=6;i<12;++i) assert(matricula[i] == '\0');
    Estudiante e;
    const char* p = e.getMatricula();
    assert(std::string(p) == "123456" && *p == '1');
    std::ostringstream chars, address;
    chars << p; address << static_cast<const void*>(p);
    assert(chars.str() == "123456" && !address.str().empty());
    std::cout << "Validación C++20: operadores, modificación, 12 caracteres, getter y salida correctos.\n";
}
