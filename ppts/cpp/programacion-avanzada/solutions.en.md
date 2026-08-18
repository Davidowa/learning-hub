# Solutions · Advanced Programming · COM103

Instructor's copy. It carries the solution to the fifty-one exercises, the real output of each program and the ten-point rubric they are marked against. All the code was compiled and run with `cl /EHsc /std:c++20` on Visual Studio Community 2026, toolset 14.51, x64. The outputs are copied from that run, not reconstructed by hand. Floating point values come out at the precision `cout` uses by default, six significant figures: if a student hands in `2.9416667` instead of `2.94167` it is because they touched the precision, not because they calculated something different.

---

## Week 01 · Unit 1 · Basic elements of C++

### 01.1 · Recognise

**Solution**

1. The program prints the right total and a wrong average.
2. With the breakpoint on the average line, Locals shows `total` at 3743 and `average` holding rubbish, because the debugger stops before running the marked line, not after.
3. The line `int average = total / 4;` divides by four when there are three windows. Corrected to `total / 3` the program prints `Average: 1247`, the integer division of 3743 by 3.

**Output**

```
Total: 3743
Average: 935
```

And with the divisor corrected:

```
Total: 3743
Average: 1247
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The two output lines, exact | 3 |
| Locals with `total` at 3743 and `average` with no useful value | 3 |
| Identifies the divisor line and gives 1247 as the corrected result | 4 |

**Most common mistake**

They answer that `average` is zero when the program stops. The giveaway is that they write "0" where the window shows a large number, different on every run.

### 01.2 · Apply

**Solution**

```cpp
#include <iostream>

int main()
{
    int reading1 = 101;
    int reading2 = 104;
    int reading3 = 99;
    int reading4 = 108;

    int sum = reading1 + reading2 + reading3 + reading4;
    int average = sum / 4;
    int range = reading4 - reading3;

    std::cout << "Readings: " << reading1 << " " << reading2 << " "
              << reading3 << " " << reading4 << "\n";
    std::cout << "Sum: " << sum << "\n";
    std::cout << "Integer average: " << average << "\n";
    std::cout << "Range: " << range << "\n";
    return 0;
}
```

**Output**

```
Readings: 101 104 99 108
Sum: 412
Integer average: 103
Range: 9
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The four values in named variables, not written straight into the output | 3 |
| Sum, average and range correct | 4 |
| The output matches character for character, colons and spaces included | 3 |

**Most common mistake**

They write the numbers inside the `cout` instead of using the variables. The giveaway is that the readings line comes out right while the sum appears as a 412 typed by hand.

### 01.3 · Integrate

**Solution**

The semicolon at the end of `int samples = 240` is missing. The compiler does not complain about that line but about the next one, because until then it goes on reading what it believes is the same declaration. On this toolchain the message is `error C2144: syntax error: 'int' should be preceded by ';'` on line 6, the same family as the C2143 seen in the session. The standard is set in Project Properties, C/C++, Language, C++ Language Standard, and it has to be set in both configurations. `__cplusplus` is no use for checking it because MSVC keeps it frozen at 199711 for compatibility, even with the project on C++20.

```cpp
#include <iostream>

int main()
{
    int samples = 240;
    int frequency = 8;

    int duration = samples / frequency;

    std::cout << "Duration: " << duration << " s\n";
    std::cout << "Standard: " << _MSVC_LANG << "\n";
    return 0;
}
```

**Output**

```
Duration: 30 s
Standard: 202002
```

And before the fix:

```
e01_3broken.cpp(6): error C2144: syntax error: 'int' should be preceded by ';'
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| Anticipates that the error is reported on the line after the missing semicolon | 3 |
| The corrected program compiles and prints the two lines | 4 |
| Explains where the standard is set and why `__cplusplus` lies here | 3 |

**Most common mistake**

They hunt for the error on line 6, where the compiler points, and delete or alter that line. The giveaway is that the submitted file has `int frequency` modified while the declaration above still has no semicolon.

---

## Week 02 · Unit 1 · Basic elements of C++

### 02.1 · Recognise

**Solution**

`blocks` holds 6 after the integer division of 1732 by 250. `leftover` holds 232, the remainder. `sent` receives 6 because the suffix hands over the old value, and at that same instant `blocks` moves to 7, which is what gets printed. `fill` is 0 because 232 over 250 is computed between integers and truncated before the `double` on the left can do anything about it. The two that surprise are the 7 sitting next to the 6, and the 0. The fix is `double fill = static_cast<double>(leftover) / BLOCK;`, which gives 0.928.

**Output**

```
7 6
232 0
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The two lines, exact | 3 |
| Explains the suffix: `sent` with the old value and `blocks` already incremented | 3 |
| Explains the integer division and fixes it with `static_cast` without changing the source types | 4 |

**Most common mistake**

They fix the fill by changing `BLOCK` to 250.0. The giveaway is that the exercise forbids touching those types, and the constant stops being the block size in samples.

### 02.2 · Apply

**Solution**

```cpp
#include <iostream>

int main()
{
    const int COUNT_MAX = 32768;
    const double FULL_SCALE_N = 5000.0;

    int count = 26214;

    double force = static_cast<double>(count) / COUNT_MAX * FULL_SCALE_N;
    double percent = static_cast<double>(count) / COUNT_MAX * 100.0;

    std::cout << "Count: " << count << "\n";
    std::cout << "Force: " << force << " N\n";
    std::cout << "Full scale: " << percent << " %\n";
    return 0;
}
```

Without the `static_cast`, `count / COUNT_MAX` gives 0 and the two outputs would read `0 N` and `0 %`.

**Output**

```
Count: 26214
Force: 3999.94 N
Full scale: 79.9988 %
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The two constants with `const` and names that say what they hold | 2 |
| The explicit conversion before the division, not after | 4 |
| The two results correct | 2 |
| The comment states that both come out at zero without the conversion | 2 |

**Most common mistake**

They write `double force = count / COUNT_MAX * FULL_SCALE_N;` trusting the destination type to sort out the arithmetic. The giveaway is that the force comes out at exactly 0 and so does the percentage.

### 02.3 · Integrate

**Solution**

In the original program, `average` is an `int` holding 119 and the deviation works out 119 minus 119, so it prints 0. That zero does not say the last reading is the mean, it says the mean lost its fraction before the subtraction. The debugger shows it by stopping on the deviation line with `average` at 119 and `sum` at 598.

```cpp
#include <iostream>

int main()
{
    const int N = 5;

    int m1 = 118;
    int m2 = 121;
    int m3 = 117;
    int m4 = 123;
    int m5 = 119;

    int sum = m1 + m2 + m3 + m4 + m5;
    int integerAverage = sum / N;
    int remainder = sum % N;

    double realAverage = static_cast<double>(sum) / N;
    double deviation = m5 - realAverage;

    std::cout << "Sum: " << sum << "\n";
    std::cout << "Integer average: " << integerAverage << "\n";
    std::cout << "Remainder: " << remainder << "\n";
    std::cout << "Real average: " << realAverage << "\n";
    std::cout << "Deviation: " << deviation << "\n";
    return 0;
}
```

**Output**

```
Sum: 598
Integer average: 119
Remainder: 3
Real average: 119.6
Deviation: -0.6
```

And the original program, before the fix:

```
Sum: 598
Average: 119
Deviation: 0
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| Predicts the 0 of the deviation and explains where it comes from | 3 |
| The number of measurements in a constant, used in all three calculations | 2 |
| The five lines correct, with the remainder at 3 and the deviation at -0.6 | 3 |
| Reports the line where it stopped and the value of `average` there | 2 |

**Most common mistake**

They declare `double average = sum / N;` and believe it fixed. The giveaway is that the real average comes out at 119 instead of 119.6 and the deviation goes back to 0.

---

## Week 03 · Unit 2 · Types, namespaces and string

### 03.1 · Recognise

**Solution**

`substr(0, 5)` copies five characters from the start and leaves `TC-04`. `find("FURNACE")` returns 6, the position where the text being searched for begins. `length()` counts thirteen characters. The counter wraps around: in a 16-bit `unsigned short`, zero minus one is 65535, and with `short` it would have printed -1 because that type does take negatives. `Measuring` is 2 because the values of an `enum class` start at zero and climb by one; without the `static_cast` the compiler rejects the conversion, which is exactly what `enum class` exists to prevent.

**Output**

```
TC-04
6
13
65535
2
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The five lines, exact | 4 |
| Explains the 65535 and says `short` would have given -1 | 3 |
| Explains why `enum class` demands the explicit conversion | 3 |

**Most common mistake**

They answer 13 on the second line and 6 on the third, swapping `find` for `length`. The giveaway is that the two answers are interchanged.

### 03.2 · Apply

**Solution**

```cpp
#include <iostream>
#include <string>

enum class Scale { Celsius, Kelvin };
using Temperature = double;

int main()
{
    std::string channel = "TC";
    std::string id = "04";
    std::string zone = "FURNACE";

    std::string label = channel + "-" + id + "-" + zone;

    Scale scale = Scale::Kelvin;
    Temperature reading = 373.15;

    std::cout << label << "\n";
    std::cout << label.length() << "\n";
    std::cout << label.substr(0, 2) << "\n";
    std::cout << label.find("-", 3) << "\n";
    std::cout << static_cast<int>(scale) << "\n";
    std::cout << reading << "\n";
    return 0;
}
```

**Output**

```
TC-04-FURNACE
13
TC
5
1
373.15
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The tag is built by concatenation, not written out whole | 3 |
| `enum class` and the `using` alias declared and used | 3 |
| The six lines correct, with the 5 from the search starting at index 3 | 4 |

**Most common mistake**

They write `"TC" + "-" + "04"` with no `std::string` in the middle and the compiler rejects the addition of two literals. The giveaway is a pointer error on a line that looks harmless.

### 03.3 · Integrate

**Solution**

```cpp
#include <iostream>
#include <string>

int main()
{
    const int COUNT_MAX = 4095;
    const double VREF = 3.3;
    const double V_ZERO = 0.5;
    const double SLOPE = 0.01;

    int count = 2867;

    double volts = static_cast<double>(count) / COUNT_MAX * VREF;
    double degrees = (volts - V_ZERO) / SLOPE;

    std::string report = "ADC-12 channel 3";

    std::cout << report << "\n";
    std::cout << report.substr(7, 7) << "\n";
    std::cout << volts << " V\n";
    std::cout << degrees << " C\n";
    std::cout << sizeof(int) << " " << sizeof(double) << "\n";
    return 0;
}
```

**Output**

```
ADC-12 channel 3
channel
2.3104 V
181.04 C
4 8
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The four constants with `const` | 2 |
| The explicit conversion and the correct voltage | 3 |
| The temperature worked out from the voltage, not from the count | 3 |
| `substr` pulls out exactly `channel` and the sizes come out 4 and 8 | 2 |

**Most common mistake**

They ask for `substr(7, 13)` thinking the second argument is the end position. The giveaway is that the output drags the rest of the string along instead of cutting at seven characters.

---

## Week 04 · Unit 3 · User-defined functions I

### 04.1 · Recognise

**Solution**

212 degrees Fahrenheit are 100 Celsius, and 373.15 in Kelvin. `margin` is still 2.5 because `twice` received a copy: the parameter `x` was born on entry, doubled and died on the way out, never touching the variable in `main`. If the prototype of `kelvin` is deleted, the compiler reports `C3861: identifier not found` on the line of the call, plus a chain of derived errors that vanish once the first is fixed. The parameter `c` of `kelvin` and the variable `c` in `main` are two different variables in two different scopes that happen to share a name and a value during the call.

**Output**

```
100 373.15
2.5
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The two lines, exact | 3 |
| Explains passing by value with the copy and the moment it dies | 4 |
| Names error C3861 and says the rest follow from it | 3 |

**Most common mistake**

They answer 5.0 on the second line because they assume `twice` modified the original. The giveaway is that they ignore that the return value was never stored anywhere.

### 04.2 · Apply

**Solution**

```cpp
#include <iostream>

double cube(double x);
double secondMoment(double b, double h);
double deflection(double F, double L, double E, double I);
double toMillimetres(double metres);

int main()
{
    const double B = 0.04;
    const double H = 0.06;
    const double LOAD = 800.0;
    const double LENGTH = 1.2;
    const double YOUNG = 200.0e9;

    double I = secondMoment(B, H);
    double d = deflection(LOAD, LENGTH, YOUNG, I);

    std::cout << "Second moment: " << I << " m4\n";
    std::cout << "Deflection: " << d << " m\n";
    std::cout << "Deflection: " << toMillimetres(d) << " mm\n";
    return 0;
}

double cube(double x)
{
    return x * x * x;
}

double secondMoment(double b, double h)
{
    return b * cube(h) / 12.0;
}

double deflection(double F, double L, double E, double I)
{
    return F * cube(L) / (3.0 * E * I);
}

double toMillimetres(double metres)
{
    return metres * 1000.0;
}
```

**Output**

```
Second moment: 7.2e-07 m4
Deflection: 0.0032 m
Deflection: 3.2 mm
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| Four prototypes before `main` and four definitions after | 3 |
| Each function does one job and `cube` is reused in two places | 2 |
| The three values correct | 3 |
| `main` calculates nothing, it only calls and prints | 2 |

**Most common mistake**

They divide by `3 * E * I` with the 3 as an integer. Here it changes nothing because `E` is real, but the giveaway is that the same habit breaks the formula as soon as both operands are integers.

### 04.3 · Integrate

**Solution**

```cpp
#include <iostream>
#include <string>

double volts(int count, int countMax, double vref);
double degrees(double v, double vZero, double slope);
std::string label(std::string channel, std::string zone);

int main()
{
    const int COUNT_MAX = 4095;
    const double VREF = 3.3;
    const double V_ZERO = 0.5;
    const double SLOPE = 0.01;

    int count = 2867;

    double v = volts(count, COUNT_MAX, VREF);
    double t = degrees(v, V_ZERO, SLOPE);
    std::string name = label("TC", "FURNACE");

    std::cout << name << "\n";
    std::cout << name.length() << "\n";
    std::cout << v << " V\n";
    std::cout << t << " C\n";
    return 0;
}

double volts(int count, int countMax, double vref)
{
    return static_cast<double>(count) / countMax * vref;
}

double degrees(double v, double vZero, double slope)
{
    return (v - vZero) / slope;
}

std::string label(std::string channel, std::string zone)
{
    return channel + "-" + zone;
}
```

**Output**

```
TC-FURNACE
10
2.3104 V
181.04 C
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The three functions with prototypes and the right types | 3 |
| The explicit conversion lives inside `volts` | 2 |
| The four output values correct | 3 |
| No function prints and `main` does not calculate | 2 |

**Most common mistake**

They put the `cout` inside the conversion functions to avoid passing the result out. The giveaway is that `main` shrinks to two lines and the functions can no longer be tested with other values.

---

## Week 05 · Unit 4 · User-defined functions II

### 05.1 · Recognise

**Solution**

`calls` is `static`, so its initialisation line runs once in the whole program and the value survives between calls: 1 and then 2. `samples` inside the function is a fresh local variable on every call that also covers up the global, so it is born at 100, climbs to 101 and dies. Nobody ever touches the global and it ends at 0. `scale` does modify its argument because it takes it by reference: 3.5 by 2 is 7, and 7 by 10 is 70.

**Output**

```
1 101
2 101
70 0
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The three lines, exact | 3 |
| Explains that `static` changes the lifetime of the variable and not its scope | 4 |
| Explains that the local covers the global and that the global therefore stays at 0 | 3 |

**Most common mistake**

They answer 102 on the second line, carrying the local forward as if it were `static` too. The giveaway is that they apply the same rule to both variables when only one carries the word.

### 05.2 · Apply

**Solution**

```cpp
#include <iostream>
#include <string>

void summary(const std::string& channel, double a, double b, double c,
             double& sum, double& mean, std::string unit = "mm/s");
void summary(const std::string& channel, double a, double b, double c, double d,
             double& sum, double& mean, std::string unit = "mm/s");

int main()
{
    double sum = 0.0;
    double mean = 0.0;

    summary("VIB-02", 2.4, 3.1, 2.8, sum, mean);
    std::cout << sum << " " << mean << "\n";

    summary("VIB-02", 2.4, 3.1, 2.8, 3.6, sum, mean, "mm/s rms");
    std::cout << sum << " " << mean << "\n";
    return 0;
}

void summary(const std::string& channel, double a, double b, double c,
             double& sum, double& mean, std::string unit)
{
    sum = a + b + c;
    mean = sum / 3.0;
    std::cout << channel << " 3 samples " << unit << "\n";
}

void summary(const std::string& channel, double a, double b, double c, double d,
             double& sum, double& mean, std::string unit)
{
    sum = a + b + c + d;
    mean = sum / 4.0;
    std::cout << channel << " 4 samples " << unit << "\n";
}
```

**Output**

```
VIB-02 3 samples mm/s
8.3 2.76667
VIB-02 4 samples mm/s rms
11.9 2.975
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The two results leave through reference parameters, not through `return` | 3 |
| The two overloaded versions live together and the compiler picks correctly | 3 |
| The default value appears once, in the prototype | 2 |
| The four numbers correct | 2 |

**Most common mistake**

They repeat the default value in the prototype and in the definition. The giveaway is the compiler error pointing at the definition, not at the call.

### 05.3 · Integrate

**Solution**

```cpp
#include <iostream>

double cube(double x);
double secondMoment(double b, double h);
int logCall();
void deflection(double F, double L, double E, double I,
                double& metres, double& millimetres);
void deflection(double F, double L, double E, double b, double h,
                double& metres, double& millimetres);

int main()
{
    const double LOAD = 800.0;
    const double LENGTH = 1.2;
    const double YOUNG = 200.0e9;

    double metres = 0.0;
    double mm = 0.0;

    deflection(LOAD, LENGTH, YOUNG, 7.2e-7, metres, mm);
    std::cout << metres << " m " << mm << " mm\n";

    deflection(LOAD, LENGTH, YOUNG, 0.04, 0.06, metres, mm);
    std::cout << metres << " m " << mm << " mm\n";
    return 0;
}

double cube(double x)
{
    return x * x * x;
}

double secondMoment(double b, double h)
{
    return b * cube(h) / 12.0;
}

int logCall()
{
    static int times = 0;
    times = times + 1;
    return times;
}

void deflection(double F, double L, double E, double I,
                double& metres, double& millimetres)
{
    metres = F * cube(L) / (3.0 * E * I);
    millimetres = metres * 1000.0;
    std::cout << "calculation " << logCall() << "\n";
}

void deflection(double F, double L, double E, double b, double h,
                double& metres, double& millimetres)
{
    deflection(F, L, E, secondMoment(b, h), metres, millimetres);
}
```

The counter reaches 2 because `logCall` is only called from the version that receives the second moment of area. The version that takes base and height counts nothing: it works out the moment and delegates, so its call passes through the counter exactly once.

**Output**

```
calculation 1
0.0032 m 3.2 mm
calculation 2
0.0032 m 3.2 mm
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The two overloaded versions, told apart by the number of parameters | 3 |
| The second delegates to the first instead of repeating the formula | 2 |
| The `static` counter in its own function, with the right value | 3 |
| The explanation of the 2 instead of the 3 | 2 |

**Most common mistake**

They put the `static` variable inside both overloads, so each keeps its own tally. The giveaway is that the output says `calculation 1` twice.

---

## Week 06 · Unit 5 · Classes and data abstraction

### 06.1 · Recognise

**Solution**

The object is born at 250 kPa, which is 2.5 bar. The mutator then leaves it at 101.3 kPa, which is 1.013 bar. The line `s.kpa = 300.0;` does not compile: `kpa` is private and the compiler reports `error C2248: cannot access private member declared in class 'PressureSensor'`. It shows up at compile time, before the program exists. The line that does the same thing and does compile is `s.setKpa(300.0);`, because it goes through the door the class left open.

**Output**

```
PT-07
250
2.5
1.013
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The four lines, exact | 4 |
| Names C2248 and says it happens at compile time | 3 |
| Points at the mutator as the equivalent legal route | 3 |

**Most common mistake**

They say the access to the private member "fails at run time". The giveaway is that they talk about a message on screen when the program was never generated.

### 06.2 · Apply

**Solution**

```cpp
#include <iostream>
#include <string>

class Beam {
public:
    Beam(std::string id, double b, double h, double length, double young)
    {
        tag = id;
        base = b;
        height = h;
        L = length;
        E = young;
    }

    std::string getTag() { return tag; }
    double secondMoment() { return base * height * height * height / 12.0; }
    double deflectionM(double load) { return load * L * L * L / (3.0 * E * secondMoment()); }
    double deflectionMm(double load) { return deflectionM(load) * 1000.0; }

private:
    std::string tag;
    double base;
    double height;
    double L;
    double E;
};

int main()
{
    Beam v1("VG-01", 0.04, 0.06, 1.2, 200.0e9);
    Beam v2("VG-02", 0.04, 0.08, 1.2, 200.0e9);

    std::cout << v1.getTag() << " " << v1.secondMoment() << " " << v1.deflectionMm(800.0) << "\n";
    std::cout << v2.getTag() << " " << v2.secondMoment() << " " << v2.deflectionMm(800.0) << "\n";
    return 0;
}
```

**Output**

```
VG-01 7.2e-07 3.2
VG-02 1.70667e-06 1.35
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The five private data members and a constructor that leaves them complete | 3 |
| `deflectionMm` leans on the other two and does not repeat the formula | 2 |
| The two lines with the right values | 3 |
| `main` does no arithmetic | 2 |

**Most common mistake**

They forget the semicolon after the brace that closes the class. The giveaway is that the compiler error points at the `int main` line, where there is nothing strange.

### 06.3 · Integrate

**Solution**

```cpp
class Beam {
public:
    Beam(std::string id, double b, double h, double length, double young)
    {
        tag = id;
        base = b;
        height = h;
        L = length;
        E = young;
    }

    double secondMoment() { return base * height * height * height / 12.0; }
    double deflectionMm(double load = 800.0)
    {
        return load * L * L * L / (3.0 * E * secondMoment()) * 1000.0;
    }

    void report(double& mm, double& moment, double load = 800.0)
    {
        mm = deflectionMm(load);
        moment = secondMoment();
        std::cout << tag << " at " << load << " N\n";
    }

private:
    std::string tag;
    double base;
    double height;
    double L;
    double E;
};
```

The second moment of area depends on the geometry of the section and not on whatever is hung from it, so both calls give 7.2e-07. The deflection is proportional to the load: with 1200 N instead of 800 it rises in the same proportion, from 3.2 to 4.8 mm.

**Output**

```
VG-01 at 800 N
7.2e-07 m4 3.2 mm
VG-01 at 1200 N
7.2e-07 m4 4.8 mm
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| `report` delivers both results by reference | 3 |
| The default load works on both calls | 3 |
| The four lines correct | 2 |
| The explanation separates what depends on geometry from what depends on load | 2 |

**Most common mistake**

They put the parameter with the default value before the reference parameters. The giveaway is the compiler error, which demands that parameters with default values sit at the end.

---

## Week 07 · Unit 6 · Control structures I

### 07.1 · Recognise

**Solution**

`if (alarms = 1)` assigns instead of comparing, the condition is worth 1 and always takes the first path, leaving `alarms` at 1 on the way. The sum `0.1 + 0.2` is not exactly 0.3 in binary, so the equality is false and the `else` runs, even though the number prints as 0.3. The `switch` enters case 2 and, since that case carries no `break`, falls into case 3 and runs both. The smallest fixes are a second equals sign, a comparison against a tolerance, and a `break` in case 2.

**Output**

```
ADbarpsi
1 250
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The two lines, exact, with `barpsi` run together | 4 |
| Explains the three traps | 3 |
| Gives the smallest fix for each one | 3 |

**Most common mistake**

They write `ADbar` because they assume the `switch` runs one case and leaves. The giveaway is that the `psi` is precisely what the exercise wants recognised.

### 07.2 · Apply

**Solution**

```cpp
std::string classify(double t)
{
    if (t < 0.0)
        return "low";
    else if (t <= 120.0)
        return "normal";
    else if (t <= 300.0)
        return "high";
    else
        return "critical";
}

std::string unit(int code)
{
    switch (code)
    {
    case 1:
        return "C";
    case 2:
        return "kPa";
    case 3:
        return "um/m";
    default:
        return "?";
    }
}

bool calibrated(double measured, double reference, double tolerance)
{
    if (measured > reference - tolerance && measured < reference + tolerance)
        return true;
    return false;
}
```

**Output**

```
normal
low
critical
C kPa ?
1 0
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The `if-else` chain covers the four ranges with no gaps and no overlaps | 3 |
| The `switch` has a default case and every case returns | 3 |
| `calibrated` compares against a tolerance and never for exact equality | 3 |
| The five lines correct | 1 |

**Most common mistake**

They write `if (t < 0) ... if (t <= 120) ...` without the `else`, and the value -4.0 enters through two branches. The giveaway is that the classification of negatives is printed twice or keeps only the last one.

### 07.3 · Integrate

**Solution**

```cpp
class Thermocouple {
public:
    Thermocouple(std::string e)
    {
        label = e;
        celsius = 0.0;
        rejects = 0;
    }

    void setCelsius(double c)
    {
        if (c < -200.0 || c > 1300.0)
        {
            rejects++;
            std::cout << "rejected " << c << "\n";
        }
        else
        {
            celsius = c;
        }
    }

    double getCelsius() { return celsius; }
    int getRejects() { return rejects; }

    char state()
    {
        if (celsius < 0.0)
            return 'B';
        else if (celsius <= 120.0)
            return 'N';
        else if (celsius <= 300.0)
            return 'A';
        else
            return 'C';
    }

private:
    std::string label;
    double celsius;
    int rejects;
};

void run(int option, Thermocouple& t)
{
    switch (option)
    {
    case 1:
        std::cout << t.getCelsius() << "\n";
        break;
    case 2:
        std::cout << t.state() << "\n";
        break;
    case 3:
        std::cout << t.getRejects() << "\n";
        break;
    default:
        std::cout << "invalid option\n";
    }
}
```

**Output**

```
rejected 1500
87.5
N
1
invalid option
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The validation lives in the mutator and the data is untouched when rejected | 4 |
| The reject counter rises only when it should | 2 |
| The `switch` with its `break` statements and its default case | 2 |
| The five lines correct | 2 |

**Most common mistake**

They validate in `main` before calling the mutator. The giveaway is that the class still accepts any value if somebody else uses it, which is exactly what encapsulation came to prevent.

---

## Week 08 · Unit 6 · Control structures II

### 08.1 · Recognise

**Solution**

The inner loop starts twelve times and in three of them the `continue` jumps out before counting, so the useful body runs nine times. The sum per row is `row * (1 + 2 + 4)`, that is `7 * row`, and adding the three rows gives 42. The `do-while` runs the body before checking anything: `attempts` ends at 1 and `code` at 3, and the condition `3 > 5` is false. A `while` with that same condition would never have entered, because 5 is not greater than 5, and would have left `attempts` at 0.

**Output**

```
9 42
1 3
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The two lines, exact | 3 |
| Twelve turns started, three skipped, nine complete | 3 |
| Explains that the equivalent `while` would have printed nothing | 4 |

**Most common mistake**

They count twelve cells because they read the `continue` as if it only skipped the sum. The giveaway is that the 42 comes out right and the count does not.

### 08.2 · Apply

**Solution**

```cpp
#include <iostream>

int main()
{
    const double T_FURNACE = 100.0;
    const double TAU = 5.0;
    const double DT = 1.0;
    const double LIMIT = 90.0;
    const int MAX_STEPS = 20;

    double t = 20.0;
    int step = 0;

    while (step < MAX_STEPS)
    {
        step++;
        t = t + (DT / TAU) * (T_FURNACE - t);
        std::cout << step << " " << t << "\n";

        if (t > LIMIT)
            break;
    }

    std::cout << "steps " << step << "\n";
    return 0;
}
```

**Output**

```
1 36
2 48.8
3 59.04
4 67.232
5 73.7856
6 79.0285
7 83.2228
8 86.5782
9 89.2626
10 91.4101
steps 10
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The five named constants and no loose number inside the loop | 3 |
| The recurrence written correctly, with the previous temperature on both sides | 3 |
| The `break` cuts on the first step past 90 | 2 |
| The ten lines and the final count | 2 |

**Most common mistake**

They write `t = (DT / TAU) * (T_FURNACE - t);` without adding the previous temperature. The giveaway is that the first line comes out at 16 instead of 36 and the series no longer converges to 100.

### 08.3 · Integrate

**Solution**

```cpp
double simulate(int step);

class Thermocouple {
public:
    Thermocouple(std::string e, double limit)
    {
        label = e;
        alarmAt = limit;
        alarms = 0;
        sum = 0.0;
        n = 0;
    }

    void record(double c)
    {
        if (c < -200.0 || c > 1300.0)
        {
            std::cout << "out of range " << c << "\n";
        }
        else
        {
            sum = sum + c;
            n++;

            if (c > alarmAt)
                alarms++;
        }
    }

    std::string getLabel() { return label; }
    double mean() { return sum / n; }
    int getAlarms() { return alarms; }
    int getN() { return n; }

private:
    std::string label;
    double alarmAt;
    int alarms;
    double sum;
    int n;
};

double simulate(int step)
{
    return 20.0 + 9.5 * step;
}
```

**Output**

```
1 29.5
2 39
3 48.5
4 58
5 67.5
6 77
7 86.5
8 96
out of range 1500
TC-04
accepted 8
mean 62.75
alarms 2
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The simulation function kept separate, with a prototype | 2 |
| The class accumulates, counts and discards with no help from `main` | 3 |
| The `for` walks the eight steps and the rejection leaves the accumulators alone | 2 |
| Mean 62.75 and two alarms | 3 |

**Most common mistake**

They add the rejected reading to the accumulator before checking the range. The giveaway is that the mean jumps from 62.75 to over two hundred, even though the out of range notice still prints.

---

## Week 09 · Unit 7 · Inheritance and composition

### 09.1 · Recognise

**Solution**

`getLabel` comes from the base and works without being written again. `describe` uses `label` directly because the member is `protected`, which is exactly what opens the door to the child class and keeps it shut for everything else: if `main` writes `t.label`, out comes `error C2248`. `t.toUnits(400)` runs the `Thermocouple` version, because the object is a `Thermocouple` and that function covers the one in the base, so it gives 100. The object `s` is a genuine `Sensor` and uses the base version, which gives 400. If `Sensor(e)` is removed from the initialiser list, the compiler goes looking for a constructor with no arguments in the base, does not find one and rejects the derived class.

**Output**

```
TC-04
TC-04 type K
100
400
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The four lines, exact | 4 |
| Explains the protected level and names C2248 for access from `main` | 3 |
| Explains what is missing when the call to the base constructor is removed | 3 |

**Most common mistake**

They answer 400 on the third line believing the base function is the one that runs. The giveaway is that they apply to a concrete object the rule that only appears with pointers and `virtual`, which is week 12 material.

### 09.2 · Apply

**Solution**

```cpp
class Sensor {
public:
    Sensor(std::string e, std::string u) { label = e; unit = u; }
    std::string getLabel() { return label; }
    std::string getUnit() { return unit; }
protected:
    std::string label;
    std::string unit;
};

class Thermocouple : public Sensor {
public:
    Thermocouple(std::string e, double p, double z) : Sensor(e, "C"), slope(p), zero(z) {}
    double convert(double volts) { return (volts - zero) / slope; }
private:
    double slope;
    double zero;
};

class StrainGauge : public Sensor {
public:
    StrainGauge(std::string e, double f) : Sensor(e, "um/m"), factor(f) {}
    double convert(double ratio) { return ratio / factor * 1000000.0; }
private:
    double factor;
};

class Channel {
public:
    Channel(int n, Thermocouple t) : number(n), sensor(t) {}
    void report(double volts)
    {
        std::cout << number << " " << sensor.getLabel() << " "
                  << sensor.convert(volts) << " " << sensor.getUnit() << "\n";
    }
private:
    int number;
    Thermocouple sensor;
};
```

A thermocouple is a sensor and so is a strain gauge, so there inheritance describes something real. A channel is not a thermocouple: it has one, along with a number and whatever gets added to it later. Changing the sensor of a channel is changing a member, not rebuilding a hierarchy.

**Output**

```
TC-04 181 C
SG-11 100 um/m
3 TC-04 181 C
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| Both derived classes call the base constructor with their unit | 3 |
| `Channel` contains a `Thermocouple` and does not inherit from it | 3 |
| The three lines correct | 2 |
| The comment applies the "is a" against "has a" test to both decisions | 2 |

**Most common mistake**

They make `Channel` inherit from `Thermocouple` so they can call `convert` without writing the member. The giveaway is that the channel ends up exposing `getUnit` as though it were a sensor itself.

### 09.3 · Integrate

**Solution**

```cpp
class TestBench {
public:
    TestBench(std::string n, Thermocouple t, double lim) : name(n), sensor(t)
    {
        limit = lim;
        alarms = 0;
        sum = 0.0;
        samples = 0;
    }

    void measure(double volts)
    {
        double c = sensor.convert(volts);
        sum += c;
        samples++;

        if (c > limit)
        {
            alarms++;
            std::cout << "ALARM " << sensor.getLabel() << " " << c << "\n";
        }
        else
        {
            std::cout << "ok " << sensor.getLabel() << " " << c << "\n";
        }
    }

    double mean() { return sum / samples; }
    int getAlarms() { return alarms; }
    std::string getName() { return name; }

private:
    std::string name;
    Thermocouple sensor;
    double limit;
    int alarms;
    double sum;
    int samples;
};
```

**Output**

```
ok TC-04 50
ok TC-04 90
ALARM TC-04 130
ALARM TC-04 170
ALARM TC-04 210
Furnace 2
mean 130
alarms 3
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The bench contains the sensor and delegates the conversion to it | 3 |
| The loop generates the five voltages instead of writing them one by one | 2 |
| The five measurement lines with the right label | 3 |
| Mean 130 and three alarms | 2 |

**Most common mistake**

They keep the `Thermocouple` as a copy but convert in `main` and hand the bench the already converted result. The giveaway is that the bench no longer needs the sensor and its member sits unused.

---

## Week 10 · Unit 8 · Arrays and strings

### 10.1 · Recognise

**Solution**

`sizeof` of the array over `sizeof` of one element gives 6. The sum of the six readings is 728. `readings[n - 1]` is the last valid slot and holds 130. The label has two hyphens. With `readings[n]` the program would print whatever sits in the memory next door, a different number on every run, and it would not fail: nobody checks the index. Inside a function that receives the array, the parameter is an address and `sizeof` measures that address, so the calculation would give 8 over 4, that is 2, no matter how many elements there are.

**Output**

```
6 728
130 2
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The two lines, exact | 3 |
| Says the out of range access prints rubbish and does not interrupt the program | 4 |
| Explains why `sizeof` stops working inside a function | 3 |

**Most common mistake**

They answer that the program "blows up" when it reads `readings[n]`. The giveaway is that the exercise asks precisely for recognising the error that gives no warning.

### 10.2 · Apply

**Solution**

```cpp
int readings[8] = {118, 121, 117, 123, 119, 130, 112, 126};
int n = sizeof(readings) / sizeof(readings[0]);

int sum = 0;
int highest = readings[0];
int lowest = readings[0];

for (int i = 0; i < n; i++)
{
    sum = sum + readings[i];

    if (readings[i] > highest)
        highest = readings[i];

    if (readings[i] < lowest)
        lowest = readings[i];
}

double mean = static_cast<double>(sum) / n;

int above = 0;
for (int i = 0; i < n; i++)
    if (readings[i] > mean)
        above++;
```

**Output**

```
n 8
mean 120.75
highest 130
lowest 112
range 18
above 4
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The size is worked out with `sizeof` and no loop carries the 8 | 3 |
| Highest and lowest start from the first element, not from zero | 3 |
| The mean is real, with an explicit conversion | 2 |
| The six lines correct | 2 |

**Most common mistake**

They start `highest` at 0 and `lowest` at 0. The highest comes out right by luck and the lowest comes out 0, and the giveaway is that the reported value is not in the array.

### 10.3 · Integrate

**Solution**

```cpp
double mean(const int data[], int n)
{
    int sum = 0;
    for (int i = 0; i < n; i++)
        sum = sum + data[i];
    return static_cast<double>(sum) / n;
}

void extremes(const int data[], int n, int& highest, int& lowest)
{
    highest = data[0];
    lowest = data[0];

    for (int i = 1; i < n; i++)
    {
        if (data[i] > highest)
            highest = data[i];
        if (data[i] < lowest)
            lowest = data[i];
    }
}

int countAbove(const int data[], int n, double threshold)
{
    int howMany = 0;
    for (int i = 0; i < n; i++)
        if (data[i] > threshold)
            howMany++;
    return howMany;
}

int countDigits(const std::string& s)
{
    int howMany = 0;
    for (int i = 0; i < static_cast<int>(s.length()); i++)
        if (s.at(i) >= '0' && s.at(i) <= '9')
            howMany++;
    return howMany;
}
```

The size travels as a parameter because inside the function the array is no longer an array, it is the address of its first slot, and from there is no way back to how many elements it held.

**Output**

```
SG-11-BEAM-A3 13 3
mean 120.75
highest 130 lowest 112
above the mean 4
above 125 2
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The four functions with the array received as `const` | 3 |
| `extremes` delivers its two results by reference | 2 |
| `countAbove` serves both thresholds without changing a line | 2 |
| The five lines correct and the explanation of the size as a parameter | 3 |

**Most common mistake**

They write `countDigits` comparing against the numbers 0 and 9 instead of the characters `'0'` and `'9'`. The giveaway is that the count comes out at zero, because no printable character has a code that low.

---

## Week 11 · Unit 9 · Records

### 11.1 · Recognise

**Solution**

`Sample b = a;` copies field by field, so changing `b.value` does not touch `a`. `table[1]` received that copy and keeps the time stamp 100. The fields add up to 4 plus 8, that is 12, but `sizeof(Sample)` gives 16: the compiler slips four bytes of padding in after the `int` so the `double` lands on an eight-byte boundary. The array of three takes 48 for the same reason. Before the two assignments, both fields of `table[2]` carry rubbish, because declaring the array initialises nothing.

**Output**

```
2.5 9.9
100 1.25
16 48
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The three lines, exact | 3 |
| Explains that the assignment copies and that from there they are two independent records | 3 |
| Explains the padding: adds to 12, takes 16, and the array 48 | 4 |

**Most common mistake**

They answer 12 and 36 on the third line, adding the fields by hand. The giveaway is that the number squares with the arithmetic and not with what the program prints.

### 11.2 · Apply

**Solution**

```cpp
struct Sample {
    int t_ms;
    double value;
};

Sample make(int t, double v)
{
    Sample m;
    m.t_ms = t;
    m.value = v;
    return m;
}

int main()
{
    Sample table[6];

    table[0] = make(0, 2.41);
    table[1] = make(100, 2.65);
    table[2] = make(200, 3.12);
    table[3] = make(300, 2.98);
    table[4] = make(400, 3.44);
    table[5] = make(500, 3.05);

    int n = sizeof(table) / sizeof(table[0]);

    double sum = 0.0;
    int iMax = 0;

    for (int i = 0; i < n; i++)
    {
        sum += table[i].value;

        if (table[i].value > table[iMax].value)
            iMax = i;
    }

    std::cout << "t_ms\tvalue\n";
    for (int i = 0; i < n; i++)
        std::cout << table[i].t_ms << "\t" << table[i].value << "\n";

    std::cout << "mean " << sum / n << "\n";
    std::cout << "max " << table[iMax].value << " at " << table[iMax].t_ms << " ms\n";
    return 0;
}
```

**Output**

```
t_ms	value
0	2.41
100	2.65
200	3.12
300	2.98
400	3.44
500	3.05
mean 2.94167
max 3.44 at 400 ms
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The record with its two fields and the function that builds and returns it | 3 |
| A single pass works out the sum and the index of the maximum | 3 |
| It stores the index and not the value, which is why it can report the time stamp | 2 |
| The table, the mean and the maximum correct | 2 |

**Most common mistake**

They keep the maximum value in a loose variable and afterwards cannot say which time it belongs to. The giveaway is that they add a second pass to look for the position it was in.

### 11.3 · Integrate

**Solution**

```cpp
bool valid(const Sample& m)
{
    if (m.t_ms < 0 || m.value <= 0.0)
        return false;
    return true;
}

double meanOfValid(const Sample table[], int n, int& used)
{
    double sum = 0.0;
    used = 0;

    for (int i = 0; i < n; i++)
    {
        if (valid(table[i]))
        {
            sum += table[i].value;
            used++;
        }
        else
        {
            std::cout << "discarded " << table[i].t_ms << " ms\n";
        }
    }

    return sum / used;
}

void extremes(const Sample table[], int n, int& iMax, int& iMin)
{
    iMax = -1;
    iMin = -1;

    for (int i = 0; i < n; i++)
    {
        if (valid(table[i]))
        {
            if (iMax < 0 || table[i].value > table[iMax].value)
                iMax = i;
            if (iMin < 0 || table[i].value < table[iMin].value)
                iMin = i;
        }
    }
}
```

A record goes by constant reference because copying it duplicates every field on every call, and `const` promises the function will not modify it. At sixteen bytes the difference is invisible; with a record of a hundred fields it is not.

**Output**

```
discarded 200 ms
records 6 valid 5
mean 2.906
max 3.44 at 400 ms
min 2.41 at 0 ms
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| `valid` takes by constant reference and decides with a single condition | 2 |
| The mean is worked out only over the valid ones and the count leaves by reference | 3 |
| `extremes` ignores the invalid one and starts without assuming the first is usable | 3 |
| The five lines correct | 2 |

**Most common mistake**

They start `iMin` at index 0 without checking whether that sample is valid, and when the invalid one is first the reported minimum is the one that was discarded. The giveaway is that the printed minimum also shows up on the discarded line.

---

## Week 12 · Unit 10 · Pointers, virtual and abstract

### 12.1 · Recognise

**Solution**

`*p = 800;` writes through the pointer, so `count` changes without its name appearing on the line, and `p == &count` is true, printed as 1. `convert` is virtual: which one runs is decided by the real object while the program runs, and since the object is a `Thermocouple`, 800 times 0.25 gives 200. `scale` is not virtual: the decision is taken by the compiler from the type of the pointer, which is `Sensor*`, and gives 1. If the `delete` is removed, the object reserved with `new` leaks. If instead the `virtual` is taken off the destructor, the `delete` does free memory but destroys only the base part, and whatever the child had reserved stays behind.

**Output**

```
800 1
200 1
25
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The three lines, exact | 3 |
| Explains who decides and when, with the pair 200 and 1 as evidence | 4 |
| Tells the leak from a missing `delete` apart from the leak from a non-virtual destructor | 3 |

**Most common mistake**

They answer `200 0.25` on the second line, applying dynamic dispatch to both functions. The giveaway is that they ignore the single word that separates one line from the other.

### 12.2 · Apply

**Solution**

```cpp
class Sensor {
public:
    Sensor(std::string e) : label(e) {}
    virtual double convert(int count) = 0;
    virtual std::string unit() = 0;
    std::string getLabel() { return label; }
    virtual ~Sensor() {}
protected:
    std::string label;
};

class Thermocouple : public Sensor {
public:
    Thermocouple(std::string e, double p) : Sensor(e), slope(p) {}
    double convert(int count) override { return count * slope; }
    std::string unit() override { return "C"; }
private:
    double slope;
};

class StrainGauge : public Sensor {
public:
    StrainGauge(std::string e, double f) : Sensor(e), factor(f) {}
    double convert(int count) override { return count / factor; }
    std::string unit() override { return "um/m"; }
private:
    double factor;
};

int main()
{
    Sensor* channels[3];
    channels[0] = new Thermocouple("TC-04", 0.25);
    channels[1] = new StrainGauge("SG-11", 2.05);
    channels[2] = new Thermocouple("TC-05", 0.50);

    int counts[3] = {400, 410, 300};
    int over = 0;

    for (int i = 0; i < 3; i++)
    {
        double v = channels[i]->convert(counts[i]);

        if (v > 120.0)
            over++;

        std::cout << channels[i]->getLabel() << " " << v << " "
                  << channels[i]->unit() << "\n";
    }

    std::cout << "over 120: " << over << "\n";

    for (int i = 0; i < 3; i++)
        delete channels[i];

    return 0;
}
```

**Output**

```
TC-04 100 C
SG-11 200 um/m
TC-05 150 C
over 120: 2
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| Abstract class with two pure virtual functions and a virtual destructor | 3 |
| A single loop walks all three without asking what type they are | 3 |
| The three `new` each have their `delete` | 2 |
| The four lines correct | 2 |

**Most common mistake**

They declare the array as `Sensor channels[3]` instead of pointers and the compiler rejects the program because the class is abstract. The giveaway is that the error talks about instantiating an abstract type and not about a conversion.

### 12.3 · Integrate

**Solution**

```cpp
std::unique_ptr<Sensor> channels[2];
channels[0] = std::make_unique<Thermocouple>("TC-04", 0.25);
channels[1] = std::make_unique<StrainGauge>("SG-11", 2.05);

const int N = 4;
Sample* table = new Sample[N];

for (int i = 0; i < N; i++)
{
    table[i].t_ms = i * 100;
    table[i].count = 400 + 20 * i;
}

for (int c = 0; c < 2; c++)
{
    double sum = 0.0;

    for (int i = 0; i < N; i++)
        sum += channels[c]->convert(table[i].count);

    std::cout << channels[c]->getLabel() << " mean "
              << sum / N << " " << channels[c]->unit() << "\n";
}

delete[] table;
```

What disappeared is the final loop that deleted the sensors one by one, and with it the chance of forgetting it or of an early exit skipping it. The `unique_ptr` frees in its destructor, so the release happens even if the program leaves by another route. The table still asks for `delete[]` because it was reserved with `new[]`.

**Output**

```
TC-04 mean 107.5 C
SG-11 mean 209.756 um/m
unmatched new: 0
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The sensors in `unique_ptr` created with `make_unique` | 3 |
| The table with `new[]` and its `delete[]`, not a plain `delete` | 3 |
| The two means correct | 2 |
| The explanation of which lines went and why | 2 |

**Most common mistake**

They free the table with `delete table;` without brackets. The program often runs the same way, and the giveaway is that the same error on an array of objects with destructors stops calling every one after the first.

---

## Week 13 · Unit 11 · Input and output

### 13.1 · Recognise

**Solution**

The end of file flag turns on after a read that fails, not before, so the loop enters a fourth time, the read gets nothing and the body prints again whatever was left in `t` and `v` from the previous turn. The count reaches 4. On the file that does not exist, the extraction is not even attempted because the stream is already in a failed state, which is why `n` keeps the 7 it was declared with. The condition that fixes the loop is the read itself: `while (in >> label >> t >> v)`.

**Output**

```
100 2.41
200 2.65
300 3.12
300 3.12
lines 4
0 7
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The six lines, exact, with the repeated one | 4 |
| Explains that `eof` turns on after the failure | 3 |
| Writes the correct condition and explains the 7 that survives | 3 |

**Most common mistake**

They predict `0 0` on the repeated line, assuming the failed read clears the variables. The giveaway is that on this toolchain the stream was already failed and never touched them.

### 13.2 · Apply

**Solution**

```cpp
std::ofstream out("furnace.txt");

if (!out.is_open())
{
    std::cout << "could not write\n";
    return 1;
}

out << "TC-04 0 21.5\n";
out << "TC-04 100 48.2\n";
out << "TC-04 200 76.9\n";
out << "TC-04 300 98.4\n";
out << "TC-04 400 121.7\n";
out << "TC-04 500 133.0\n";
out.close();

std::ifstream in("furnace.txt");

if (!in.is_open())
{
    std::cout << "could not open furnace.txt\n";
    return 1;
}

std::string label;
int t = 0;
double c = 0.0;

int n = 0;
double sum = 0.0;
int over = 0;

while (in >> label >> t >> c)
{
    n++;
    sum += c;

    if (c > 100.0)
        over++;
}
in.close();
```

**Output**

```
records 6
mean 83.2833
over 100 C 2
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| `is_open` checked on the write and on the read | 3 |
| The loop is driven by the read and not by a counter nor by `eof` | 3 |
| Both files are closed | 2 |
| The three lines correct | 2 |

**Most common mistake**

They walk the file with a `for` of six turns because they know how many lines they wrote. The giveaway is that the program stops working the moment somebody else generates the file.

### 13.3 · Integrate

**Solution**

```cpp
struct Record {
    std::string label;
    int t_ms;
    double celsius;
};

class Channel {
public:
    Channel(std::string e, double lim)
    {
        label = e;
        limit = lim;
        sum = 0.0;
        n = 0;
        alarms = 0;
        discarded = 0;
    }

    void add(const Record& r)
    {
        if (r.celsius < -200.0 || r.celsius > 1300.0)
        {
            discarded++;
        }
        else
        {
            sum += r.celsius;
            n++;

            if (r.celsius > limit)
                alarms++;
        }
    }

    double mean() { return sum / n; }
    int getN() { return n; }
    int getAlarms() { return alarms; }
    int getDiscarded() { return discarded; }
    std::string getLabel() { return label; }

private:
    std::string label;
    double limit;
    double sum;
    int n;
    int alarms;
    int discarded;
};
```

Reading the file stops on whichever comes first:

```cpp
while (read < 10 && in >> table[read].label >> table[read].t_ms >> table[read].celsius)
    read++;
```

The mean of the five accepted is 422.8 over 5, that is 84.56.

**Output**

```
TC-04
read 6
accepted 5
discarded 1
mean 84.56
alarms 2
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| `is_open` checked before reading, with a clean exit if it fails | 2 |
| The loop stops on end of file or on capacity, whichever arrives first | 3 |
| The class validates and accumulates, `main` only coordinates | 3 |
| The six lines correct | 2 |

**Most common mistake**

They put the capacity condition after the read, so record number eleven is read over the end of the array before anybody checks. The giveaway is that with long files the program writes outside the array with no warning at all.

---

## Week 14 · Unit 12 · Overloading and templates

### 14.1 · Recognise

**Solution**

Adding forces works component by component: 150.5 and 60. The comparison against `Force(150.5, 60.0)` is true and prints as 1. The template generates two concrete functions, one with `T` equal to `int` and one with `T` equal to `double`, and only those two reach the executable: the template itself does not, it is a recipe. `larger(f1, f2)` does not compile because the body asks for `a > b` and `Force` defines no greater than operator. The error appears at the first call, not where the template was written.

**Output**

```
150.5 60
1
9 2.5
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The three lines, exact | 3 |
| Two instantiations, with the right types, and the template outside the executable | 4 |
| Explains that the error from `larger(f1, f2)` comes out at the call, and why | 3 |

**Most common mistake**

They answer that the template generates one single function serving both types. The giveaway is that they confuse the mechanism with one from a language that resolves types while running.

### 14.2 · Apply

**Solution**

```cpp
class Measurement {
public:
    Measurement(double v, std::string u) : value(v), unit(u) {}

    Measurement operator+(const Measurement& o) { return Measurement(value + o.value, unit); }
    bool operator==(Measurement o) { return value == o.value && unit == o.unit; }
    bool operator>(const Measurement& o) { return value > o.value; }

    double getValue() { return value; }
    std::string getUnit() { return unit; }

private:
    double value;
    std::string unit;
};

std::ostream& operator<<(std::ostream& os, Measurement m)
{
    os << m.getValue() << " " << m.getUnit();
    return os;
}

template <typename T>
T larger(T a, T b)
{
    if (a > b)
        return a;
    return b;
}

template <typename T>
double average(const T data[], int n)
{
    double sum = 0.0;

    for (int i = 0; i < n; i++)
        sum += data[i];

    return sum / n;
}
```

**Output**

```
218.8 kPa
0 1
120.5 kPa
7 9.75
108.8
370
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| Addition, equality and greater than overloaded as member functions | 3 |
| The output operator as a free function that returns the stream | 2 |
| The two templates work with the requested types without a line specific to `Measurement` | 3 |
| The six lines correct | 2 |

**Most common mistake**

They declare `bool operator==(const Measurement& o)` without marking it `const`, and the C++20 compiler rejects the comparison with `error C2666`, because the language also synthesises the reversed version and the two tie. The way out is taking the operand by value.

### 14.3 · Integrate

**Solution**

```cpp
const int CAPACITY = 5;

struct Sample {
    int t_ms;
    double value;
};

std::ostream& operator<<(std::ostream& os, Sample m)
{
    os << m.t_ms << " ms " << m.value;
    return os;
}

template <typename T>
class Buffer {
public:
    Buffer() { n = 0; }

    void add(T v)
    {
        if (n < CAPACITY)
        {
            data[n] = v;
            n++;
        }
        else
        {
            std::cout << "buffer full\n";
        }
    }

    T get(int i) { return data[i]; }
    int size() { return n; }

private:
    T data[CAPACITY];
    int n;
};
```

The buffer full notice prints during the filling, on the sixth call to `add`, and the count prints afterwards, once the loop has finished. That is why the message appears above even though it talks about the end of the array.

**Output**

```
volts 3 mean 2.72667
buffer full
records 5
0 ms 2.41
100 ms 2.66
200 ms 2.91
300 ms 3.16
400 ms 3.41
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The class template serves `double` and `Sample` with no changes | 3 |
| The capacity rejection does not write outside the array | 3 |
| The output operator for `Sample` prints in the requested format | 2 |
| The lines correct and the explanation of the ordering | 2 |

**Most common mistake**

They define the template functions in a separate `.cpp` and the linker cannot find the concrete version. The giveaway is that the error is LNK2019 and not a compilation error.

---

## Week 15 · Unit 13 · Exception handling

### 15.1 · Recognise

**Solution**

The `A` prints, then `2.5` with its space, and at that point `at(9)` throws `std::out_of_range` because the string holds five characters. The `throw` abandons the block and never returns, so the `B` never runs. The first `catch` is the one matching the type thrown and the `C` prints; the second is never touched, because as soon as one catches, the rest are skipped. The program carries on past the block and finishes the line with `E`. In the second block the `catch` for `exception` does catch an `invalid_argument`, because `invalid_argument` descends from `exception`, and `what()` returns the message it was built with.

**Output**

```
A2.5 CE
zero divisor
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The two lines, exact | 4 |
| Explains that the `throw` does not return to the block, hence no `B` | 3 |
| Explains the inheritance between `invalid_argument` and `exception` | 3 |

**Most common mistake**

They write `ACBD` because they assume the program picks the `try` back up after the `catch`. The giveaway is that they slip the `B` into an output where the block had already been abandoned.

### 15.2 · Apply

**Solution**

```cpp
class Calibration {
public:
    Calibration(std::string e, double p, double z)
    {
        if (p == 0.0)
            throw std::invalid_argument("zero slope on " + e);

        label = e;
        slope = p;
        zero = z;
    }

    double convert(double volts) { return (volts - zero) / slope; }
    std::string getLabel() { return label; }

private:
    std::string label;
    double slope;
    double zero;
};

double resistance(double volts, double amperes)
{
    if (amperes == 0.0)
        throw std::runtime_error("zero current, no resistance to measure");

    return volts / amperes;
}
```

**Output**

```
TC-04 181 C
error: zero slope on TC-09
24 ohm
error: zero current, no resistance to measure
the program carries on
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The constructor throws before leaving the object half built | 3 |
| The types thrown are the ones from `stdexcept` and not loose strings | 2 |
| Every `catch` takes by constant reference | 2 |
| The five lines correct and the program ends normally | 3 |

**Most common mistake**

They assign the members and then check the slope, so the object gets to exist wrong before the exception leaves. The giveaway is that the validation sits on the line after the assignments.

### 15.3 · Integrate

**Solution**

```cpp
void open(std::ifstream& in, const std::string& path)
{
    in.open(path);

    if (!in.is_open())
        throw std::runtime_error("could not open " + path);
}
```

The inner `try` lives inside the loop, which is what makes it possible to report the short line and carry on reading:

```cpp
while (in >> label >> celsius)
{
    try
    {
        char zone = label.at(6);
        sum += celsius;
        good++;
        std::cout << "zone " << zone << " " << celsius << "\n";
    }
    catch (const std::out_of_range&)
    {
        bad++;
        std::cout << "malformed line: " << label << "\n";
    }
}
```

The mean is 168.1 over 3, that is 56.0333, because the discarded line does not enter the sum either.

**Output**

```
zone A 21.5
zone B 48.2
malformed line: TC-04
zone C 98.4
good 3 bad 1
mean 56.0333
error: could not open missing.txt
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The opening function throws `runtime_error` with the path in the message | 3 |
| The `try` for the short line sits inside the loop and reading continues | 3 |
| The sum leaves out the rejected line | 2 |
| The seven lines correct | 2 |

**Most common mistake**

They wrap the `try` around the whole loop and the first malformed line stops the reading. The giveaway is that the output ends on the rejected line and the ones still pending are never processed.

---

## Week 16 · Unit 14 · Recursion and concurrency

### 16.1 · Recognise

**Solution**

`sumTo(5)` goes down to the base case and builds the result on the way back: 15. `steps(64)` halves on every call, with `n` holding 64, 32, 16, 8, 4, 2 and 1, that is six calls each adding one to the one below, and seven frames end up alive at the same time, counting the base case. `power(2.0, 10)` gives 1024. With exponent -1 the base case compares against exact zero, the argument moves further away on every call and never reaches it: the program eats the stack and dies on the spot. It does not hang like an infinite loop because the stack has a fixed size and runs out.

**Output**

```
15
6
1024
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The three lines, exact | 3 |
| The chain of `steps(64)` with its values and the number of live frames | 4 |
| Explains the unreachable base case and why it ends instead of hanging | 3 |

**Most common mistake**

They count six frames because they forget the one belonging to the call that returns zero. The giveaway is that the chain they draw does reach 1 but the count leaves it out.

### 16.2 · Apply

**Solution**

```cpp
int search(const int table[], int left, int right, int target)
{
    if (left > right)
        return -1;

    int middle = (left + right) / 2;

    if (table[middle] == target)
        return middle;

    if (table[middle] < target)
        return search(table, middle + 1, right, target);

    return search(table, left, middle - 1, target);
}

double sumRec(const double data[], int n)
{
    if (n <= 0)
        return 0.0;
    return data[n - 1] + sumRec(data, n - 1);
}

std::mutex countLock;
long long total = 0;

void bump(int times)
{
    for (int i = 0; i < times; i++)
    {
        std::lock_guard<std::mutex> hold(countLock);
        total = total + 1;
    }
}
```

The two `jthread` are declared inside a block and join on their own when it ends, so the print that follows sees the complete total. Without the lock, `total = total + 1` is three steps, read, add and write, and two threads interleaving them lose increments: the total comes out below 200000 and different on every run. With the lock, only one thread holds the object at a time and no increment is lost.

**Output**

```
4
-1
14.6
200000
```

The run without `lock_guard` on this machine gave 100000, 100260 and 100000 on three consecutive attempts. The first and the third teach the most: exactly a hundred thousand means one thread wrote clean over the other's work. Any result below 200000 counts for the exercise, and nobody can be asked to reproduce these same three.

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The search is genuinely recursive, with a base case for the failure | 3 |
| The recursive sum uses no loop | 2 |
| The lock is taken with `lock_guard` and the threads join before the print | 3 |
| The four values and the three unlocked totals recorded | 2 |

**Most common mistake**

They print the total inside the same block where the `jthread` live, so they read the variable before the threads finish. The giveaway is that the printed number is below 200000 even with the lock in place.

### 16.3 · Integrate

**Solution**

```cpp
int maxRec(const int data[], int n)
{
    if (n == 1)
        return data[0];

    int rest = maxRec(data, n - 1);

    if (data[n - 1] > rest)
        return data[n - 1];

    return rest;
}

void read(const std::string& path, Record table[], int capacity, int& count)
{
    std::ifstream in(path);

    if (!in.is_open())
        throw std::runtime_error("could not open " + path);

    count = 0;

    while (count < capacity &&
           in >> table[count].label >> table[count].t_ms >> table[count].count)
        count++;

    in.close();
}
```

The mean of the four counts is 448. Converted with the thermocouple at slope 0.25 it gives 112 degrees, and with the strain gauge at factor 2.05 it gives 218.537 micrometres per metre.

**Output**

```
records 4
max count 512
TC-04 mean 112 C
SG-11 mean 218.537 um/m
error: could not open missing.txt
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The record, the read with `is_open` and the exception carrying the path | 3 |
| The abstract hierarchy walked by a single loop over `unique_ptr` | 3 |
| The recursive maximum function, with no loops | 2 |
| The five lines correct | 2 |

**Most common mistake**

They write `maxRec` with the base case at `n == 0` returning zero, so an array of negative counts would report zero as the maximum. The giveaway is that the base case invents a value that is not in the data.

---

## Week 17 · Closing · Integrating project

### 17.1 · Recognise

**Solution**

The four defects, one per rubric criterion:

1. Correctness: `process` never checks `is_open`, the file does not exist, the loop turns zero times and `n` stays at zero. Dividing by zero in floating point does not crash, it produces a value that is not a number, and the program reports it as though it were a result.
2. Design: `process` reads the file, prints every record, works out the mean and prints that too. It is at least two functions glued together.
3. Efficiency and memory: there are two `new` and a single `delete`. The `backup` object leaks whole. And `delete primary` does not do its full job either, because the base destructor is not virtual, so only `~Sensor` runs and the `Thermocouple` part is never destroyed. The output shows it: `closing Sensor` appears and `closing Thermocouple` does not.
4. Documentation: the program never says the file could not be opened, so anyone reading the output has no way of knowing what happened.

**Output**

```
100
200
mean -nan(ind)
result -nan(ind)
closing Sensor
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The five lines, including the way this compiler prints the non-number | 3 |
| The four defects, each with its line and its criterion | 4 |
| Counts two `new` against one `delete` and explains the non-virtual destructor | 3 |

**Most common mistake**

They report a single leak, the pointer with no `delete`, and take the line that does free as sound. The giveaway is that the output carries only one of the two destructor lines and nobody asks about the missing one.

### 17.2 · Apply

**Solution**

```cpp
class Sensor {
public:
    Sensor(std::string e) : label(e) {}
    virtual double convert(int count) = 0;
    std::string getLabel() { return label; }
    virtual ~Sensor() { std::cout << "closing Sensor\n"; }
protected:
    std::string label;
};

class Thermocouple : public Sensor {
public:
    Thermocouple(std::string e, double p) : Sensor(e), slope(p) {}
    double convert(int count) override { return count * slope; }
    ~Thermocouple() override { std::cout << "closing Thermocouple\n"; }
private:
    double slope;
};

bool read(const std::string& path, int counts[], int capacity, int& n)
{
    std::ifstream in(path);

    if (!in.is_open())
        return false;

    std::string label;
    n = 0;

    while (n < capacity && in >> label >> counts[n])
        n++;

    in.close();
    return true;
}

double mean(const int data[], int n)
{
    double sum = 0.0;

    for (int i = 0; i < n; i++)
        sum += data[i];

    return sum / n;
}
```

The last four lines appear because the base destructor is virtual now and because both objects are destroyed. Each one prints the derived class destructor first and the base one after, which is the order an object comes apart in. The two `unique_ptr` live in `main` and are destroyed in reverse order of declaration, so `backup` closes first and `primary` after.

**Output**

```
100
200
could not open missing.txt
records 4
mean count 448
mean on TC-04 112 C
closing Thermocouple
closing Sensor
closing Thermocouple
closing Sensor
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| Virtual destructor in the base and pure virtual conversion | 3 |
| The two raw pointers replaced by `unique_ptr` with `make_unique` | 2 |
| The read separated from the calculation, and a clear notice when the file does not open | 3 |
| The ten lines correct and the explanation of the destruction order | 2 |

**Most common mistake**

They move to `unique_ptr` but leave the base destructor without `virtual`. The giveaway is that the leak is still there and the output prints `closing Sensor` twice and nothing else.

### 17.3 · Integrate

**Solution**

```cpp
struct Reading {
    std::string label;
    int t_ms;
    int count;
};

std::ostream& operator<<(std::ostream& os, Reading l)
{
    os << l.label << " " << l.t_ms << " ms " << l.count;
    return os;
}

template <typename T>
double average(const T data[], int n)
{
    double sum = 0.0;

    for (int i = 0; i < n; i++)
        sum += data[i];

    return sum / n;
}

int maxRec(const int data[], int n)
{
    if (n == 1)
        return data[0];

    int rest = maxRec(data, n - 1);

    if (data[n - 1] > rest)
        return data[n - 1];

    return rest;
}

bool valid(const Reading& l)
{
    if (l.count < 0 || l.count > 4095)
        return false;
    return true;
}

void read(const std::string& path, Reading table[], int capacity, int& n)
{
    std::ifstream in(path);

    if (!in.is_open())
        throw std::runtime_error("could not open " + path);

    n = 0;

    while (n < capacity &&
           in >> table[n].label >> table[n].t_ms >> table[n].count)
        n++;

    in.close();
}
```

`main` separates the valid ones into an array of their own, which keeps the statistics away from the 5000 reading entirely, and the hierarchy is walked by a single loop over the `unique_ptr`. The four valid counts average 448 and their maximum is 512.

**Output**

```
discarded TC-04 200 ms 5000
read 5 valid 4
mean count 448
max count 512
TC-04 112 C
SG-11 218.537 um/m
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| Reading with an exception, range validation and separation of the valid ones | 3 |
| The template and the recursive function work over the filtered array | 2 |
| The abstract hierarchy over `unique_ptr`, walked without asking types | 2 |
| The output operator for `Reading` and the six lines correct | 2 |
| No `new` without a partner and no function doing two jobs | 1 |

**Most common mistake**

They filter the invalid ones but work out the mean over the five original readings. The giveaway is that the mean comes out at 1358.4 instead of 448, even though the discard line prints correctly.
