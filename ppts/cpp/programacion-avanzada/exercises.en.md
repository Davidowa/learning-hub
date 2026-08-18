# Exercises · Advanced Programming · COM103

Fifty-one exercises for the second-term group at the School of Engineering, three per session and in the order the topics are taught. Each week opens with a reading exercise, where you predict what a program prints before running it, continues with one written against a closed specification, and closes with one that drags you back into earlier weeks. Difficulty climbs inside the week and across the term: the first exercise of week 12 weighs more than the third of week 4. Every problem lives in the same instrumentation lab, with the same channels and the same beams, so the data from one week turns up again in the next. Hand in one `.cpp` file per exercise, built as C++20 from Visual Studio, zipped without the `x64` folder and uploaded to Blackboard before the following session.

---

## Week 01 · Unit 1 · Basic elements of C++

### 01.1 · Recognise

**A flow meter that averages wrong**

The test bench counts pulses from a flow meter over three sixty-second windows and gets 1240, 1305 and 1198. This program compiles and runs without complaint.

```cpp
#include <iostream>

int main()
{
    int pulses1 = 1240;
    int pulses2 = 1305;
    int pulses3 = 1198;

    int total = pulses1 + pulses2 + pulses3;
    int average = total / 4;

    std::cout << "Total: " << total << "\n";
    std::cout << "Average: " << average << "\n";
    return 0;
}
```

Answer without running it:

1. The two exact lines it prints.
2. If you set a breakpoint with F9 on the average line and run with F5, what the Locals window shows for `total` and for `average` at the instant the program stops.
3. Which line is wrong, and what the corrected program prints.

### 01.2 · Apply

**Report of four pressure readings**

The logger keeps four readings from a pressure transducer, in whole kilopascals: 101, 104, 99 and 108. Write a program that declares them in four variables with names of their own and prints exactly these four lines:

```
Readings: 101 104 99 108
Sum: 412
Integer average: 103
Range: 9
```

The range is the difference between the highest and the lowest reading, both known here in advance. Everything goes inside `main`, with `int` variables, no functions of your own, no `if` and no loops, which arrive later in the course.

### 01.3 · Integrate

**The file that will not compile and the standard that does matter**

A classmate sends this file and says Visual Studio throws a list of errors at him.

```cpp
#include <iostream>

int main()
{
    int samples = 240
    int frequency = 8;

    int duration = samples / frequency;

    std::cout << "Duration: " << duration << " s\n";
    std::cout << "Standard: " << _MSVC_LANG << "\n";
    return 0;
}
```

1. Name the error code that appears first and the line the compiler reports it on, before opening the file on the machine.
2. Fix it. The finished program has to print `Duration: 30 s` and `Standard: 202002`.
3. If the second line prints something else, the project is not on C++20. Say where in the project properties that gets fixed, and why the `__cplusplus` macro is no use for checking it on this compiler.

---

## Week 02 · Unit 1 · Basic elements of C++

### 02.1 · Recognise

**Blocks of 250 samples**

The acquisition unit writes samples to disk in blocks of 250. This run collected 1732 samples.

```cpp
#include <iostream>

int main()
{
    int samples = 1732;
    const int BLOCK = 250;

    int blocks = samples / BLOCK;
    int leftover = samples % BLOCK;

    int sent = blocks++;
    double fill = leftover / BLOCK;

    std::cout << blocks << " " << sent << "\n";
    std::cout << leftover << " " << fill << "\n";
    return 0;
}
```

Write the two lines it prints and, next to each number, the reason it holds that value. Two of the four values surprise a first reading: say which, and why. Then fix `fill` so it shows the real fraction of the block that ended up occupied, without changing the type of `leftover` or of `BLOCK`.

### 02.2 · Apply

**A 16-bit load cell**

A load cell delivers a digital count from 0 to 32768, where full scale corresponds to 5000 N. Today's reading came in at 26214.

Write a program that declares `COUNT_MAX` and `FULL_SCALE_N` as constants with `const`, stores the count in an `int` variable, and works out the force in newtons and the percentage of full scale. The conversion to real has to be explicit, with `static_cast`, at the point where it is needed and not after. Expected output:

```
Count: 26214
Force: 3999.94 N
Full scale: 79.9988 %
```

Add a three-line block comment explaining what the program would print if the conversion were left out.

### 02.3 · Integrate

**Five resistances and a deviation of zero**

Five contact resistance measurements, in milliohms: 118, 121, 117, 123 and 119. The program that processes them came out like this.

```cpp
int sum = m1 + m2 + m3 + m4 + m5;
int average = sum / 5;
double deviation = m5 - average;
```

1. Say what the deviation line prints as it stands, and why that result does not mean the last measurement is the mean.
2. Rewrite the program with the number of measurements in a constant, printing the sum, the integer average, the remainder of the integer division, the real average and the deviation of the last reading from that real average. Expected output:

```
Sum: 598
Integer average: 119
Remainder: 3
Real average: 119.6
Deviation: -0.6
```

3. Find the original mistake with the debugger, without adding any print statements, and say which line you stopped on and what `average` held there.

---

## Week 03 · Unit 2 · Types, namespaces and string

### 03.1 · Recognise

**The thermocouple tag and a counter that wraps around**

```cpp
#include <iostream>
#include <string>

enum class State { Idle, Calibrating, Measuring };

int main()
{
    std::string label = "TC-04-FURNACE";

    unsigned short counter = 0;
    counter = static_cast<unsigned short>(counter - 1);

    State e = State::Measuring;

    std::cout << label.substr(0, 5) << "\n";
    std::cout << label.find("FURNACE") << "\n";
    std::cout << label.length() << "\n";
    std::cout << counter << "\n";
    std::cout << static_cast<int>(e) << "\n";
    return 0;
}
```

Write the five output lines. For the fourth, explain where that number comes from and what it would have printed if `counter` were `short` instead of `unsigned short`. For the fifth, say why the `static_cast` is needed and what error you get without it.

### 03.2 · Apply

**Building a channel tag**

The system names its channels by gluing three pieces together: the sensor type, the channel number and the zone. For thermocouple four in the furnace the pieces are `"TC"`, `"04"` and `"FURNACE"`.

Write a program that:

- keeps the three pieces in separate `std::string` variables and builds the full tag with hyphens between them,
- declares `enum class Scale { Celsius, Kelvin }` and an alias `using Temperature = double;`,
- stores 373.15 in a variable of type `Temperature`,
- prints the tag, its length, its first two characters, the position of the second hyphen searching from index 3, the integer value of `Scale::Kelvin` and the temperature.

Expected output, in that order: `TC-04-FURNACE`, `13`, `TC`, `5`, `1`, `373.15`.

### 03.3 · Integrate

**From the ADC to degrees, with the channel tag**

The analogue to digital converter is 12 bits, so its count runs from 0 to 4095, and its reference is 3.3 V. The sensor delivers 0.5 V at zero degrees and rises 0.01 V per degree. The count that arrived is 2867.

Write a program that works out the voltage and the temperature, with the four constants declared using `const` and with the type conversion explicit where it is needed. Store the channel tag in a `std::string` holding the text `ADC-12 channel 3` and print from it only the word `channel`, pulled out with `substr`. Close by printing how many bytes an `int` and a `double` take on this platform. Expected output:

```
ADC-12 channel 3
channel
2.3104 V
181.04 C
4 8
```

---

## Week 04 · Unit 3 · User-defined functions I

### 04.1 · Recognise

**Three conversion functions and a parameter that does not change**

```cpp
#include <iostream>

double celsius(double f);
double kelvin(double c);
double twice(double x);

int main()
{
    double readingF = 212.0;

    double c = celsius(readingF);
    double k = kelvin(c);

    double margin = 2.5;
    twice(margin);

    std::cout << c << " " << k << "\n";
    std::cout << margin << "\n";
    return 0;
}

double celsius(double f)
{
    return (f - 32.0) * 5.0 / 9.0;
}

double kelvin(double c)
{
    return c + 273.15;
}

double twice(double x)
{
    x = x * 2.0;
    return x;
}
```

Write the two output lines. Then answer: why `margin` holds what it holds after the call, what error the compiler reports if the prototype of `kelvin` on line 4 is deleted, and how the parameter `c` of `kelvin` differs from the variable `c` sitting in `main`.

### 04.2 · Apply

**Deflection of a cantilever beam**

A cantilever beam of rectangular section has a base of 0.04 m and a height of 0.06 m, measures 1.2 m long and is made of steel, with a Young's modulus of 200 GPa. An 800 N load hangs from the tip. The deflection at the end is `F L³ / (3 E I)`, and the second moment of area of the rectangular section is `b h³ / 12`.

Write the program with four functions, each with its prototype before `main` and its definition after: one that cubes, one that works out the second moment of area, one that works out the deflection in metres and one that converts metres to millimetres. `main` does no arithmetic at all, it only calls and prints.

```
Second moment: 7.2e-07 m4
Deflection: 0.0032 m
Deflection: 3.2 mm
```

### 04.3 · Integrate

**Conversion chain for channel 3**

Pick up the data from exercise 03.3, now spread across functions. Write three functions with prototypes: one that takes the count, the maximum count and the reference voltage and returns the voltage; another that takes the voltage, the voltage at zero degrees and the slope and returns the temperature; and one that takes two `std::string` and returns the tag joined with a hyphen.

With count 2867, maximum count 4095, reference 3.3 V, zero at 0.5 V and a slope of 0.01 V per degree, and with the pieces `"TC"` and `"FURNACE"`, the output is:

```
TC-FURNACE
10
2.3104 V
181.04 C
```

None of the three functions may print anything, and `main` may not compute anything.

---

## Week 05 · Unit 4 · User-defined functions II

### 05.1 · Recognise

**A counter that survives and a global that gets covered up**

```cpp
#include <iostream>

int samples = 0;

void record(double v)
{
    static int calls = 0;
    int samples = 100;

    calls = calls + 1;
    samples = samples + 1;

    std::cout << calls << " " << samples << "\n";
}

void scale(double& v, double factor = 2.0)
{
    v = v * factor;
}

int main()
{
    double reading = 3.5;

    record(reading);
    record(reading);

    scale(reading);
    scale(reading, 10.0);

    std::cout << reading << " " << samples << "\n";
    return 0;
}
```

Write the three output lines. Explain why the second column repeats the same number on the first two lines while the first column advances, and why the global variable `samples` ends as it started even though a line inside `record` adds to it.

### 05.2 · Apply

**Vibration summary by reference**

Channel VIB-02 measures vibration velocity in mm/s. The first batch gave 2.4, 3.1 and 2.8. The second gave those three plus a fourth of 3.6.

Write a `void` function that takes the channel name by constant reference and the three readings by value, and hands back the sum and the mean through two reference parameters. Add a last parameter with the default value `"mm/s"` for the unit. The function prints one line with the channel, how many samples it processed and the unit, and nothing else. Overload it with a second version that accepts four readings.

`main` calls both and then prints the sum and the mean of each. The first call lets the unit take its default and the second passes `"mm/s rms"`.

```
VIB-02 3 samples mm/s
8.3 2.76667
VIB-02 4 samples mm/s rms
11.9 2.975
```

### 05.3 · Integrate

**The beam, now with references and overloading**

Take the beam program from exercise 04.2 and change it wholesale into this shape:

- a `void` function that takes load, length, modulus and second moment of area, and delivers the deflection in metres and in millimetres through two reference parameters,
- a second overloaded version that takes base and height instead of the second moment of area, works it out and delegates to the first,
- a separate function with a `static` variable that keeps count of how many calculations have been asked for, which the first version calls to print the calculation number.

`main` calls first the version that takes `7.2e-7` directly and then the one that takes 0.04 and 0.06, and with a load of 800 N, a length of 1.2 m and 200 GPa the two give the same:

```
calculation 1
0.0032 m 3.2 mm
calculation 2
0.0032 m 3.2 mm
```

Explain in three lines why the counter reaches 2 and not 3, even though the second call passes through both functions.

---

## Week 06 · Unit 5 · Classes and data abstraction

### 06.1 · Recognise

**A pressure sensor with private data**

```cpp
class PressureSensor {
public:
    PressureSensor(std::string e, double k) { label = e; kpa = k; }
    std::string getLabel() { return label; }
    double getKpa() { return kpa; }
    double inBar() { return kpa / 100.0; }
    void setKpa(double k) { kpa = k; }
private:
    std::string label;
    double kpa;
};

int main()
{
    PressureSensor s("PT-07", 250.0);

    std::cout << s.getLabel() << "\n";
    std::cout << s.getKpa() << "\n";
    std::cout << s.inBar() << "\n";

    s.setKpa(101.3);
    std::cout << s.inBar() << "\n";
    return 0;
}
```

Write the four output lines. Then say what happens if the line `s.kpa = 300.0;` is added to `main`, with the exact error code and the moment it appears, and which other line of the program does the same thing but does compile.

### 06.2 · Apply

**The beam turned into a class**

Write a class `Beam` that holds the tag, the base, the height, the length and the Young's modulus as private members. The constructor takes the five values. The class exposes three public member functions: the tag, the second moment of area, and the deflection in millimetres for a load received as an argument.

`main` creates two beams of the same base but different height, VG-01 at 0.04 by 0.06 and VG-02 at 0.04 by 0.08, both 1.2 m and 200 GPa, and asks for the deflection of both under 800 N.

```
VG-01 7.2e-07 3.2
VG-02 1.70667e-06 1.35
```

No data member may be public and `main` may do no arithmetic. No `if` and no loops.

### 06.3 · Integrate

**The beam that reports two results**

Extend the class from 06.2 with a member function `report` that takes two reference parameters, one for the deflection in millimetres and one for the second moment of area, and a third parameter defaulting to 800.0 for the load. The function prints a single line with the tag and the load used, and leaves the two results in the reference parameters.

`main` declares beam VG-01 with 0.04, 0.06, 1.2 and 200 GPa, calls `report` without giving a load, prints what it got back, and calls again with 1200 N.

```
VG-01 at 800 N
7.2e-07 m4 3.2 mm
VG-01 at 1200 N
7.2e-07 m4 4.8 mm
```

Explain in two lines why the second moment of area did not change between the two calls and the deflection did.

---

## Week 07 · Unit 6 · Control structures I

### 07.1 · Recognise

**Four traps in a single run**

```cpp
int main()
{
    double pressure = 250.0;
    int code = 2;
    int alarms = 0;

    if (alarms = 1)
        std::cout << "A";
    else
        std::cout << "B";

    double sum = 0.1 + 0.2;

    if (sum == 0.3)
        std::cout << "C";
    else
        std::cout << "D";

    switch (code)
    {
    case 1: std::cout << "kPa";
    case 2: std::cout << "bar";
    case 3: std::cout << "psi"; break;
    default: std::cout << "?";
    }

    std::cout << "\n" << alarms << " " << pressure << "\n";
    return 0;
}
```

Write the two output lines, character by character. Then point out the three decisions that did not do what they appear to do and, for each one, the smallest fix: one letter in the first, a different comparison in the second, one word in the third.

### 07.2 · Apply

**Temperature classifier and unit table**

Write three functions:

- `classify` takes a temperature in degrees Celsius and returns a `std::string`: `low` below zero, `normal` up to and including 120, `high` up to and including 300, and `critical` above that. It is solved with a chained `if-else`.
- `unit` takes an integer code and returns the unit with a `switch`: 1 is `C`, 2 is `kPa`, 3 is `um/m` and anything else is `?`.
- `calibrated` takes the reading, the reference and a tolerance, and returns `bool`. It is calibrated if the reading falls inside the tolerance band around the reference, without comparing reals for exact equality.

`main` tries `classify` with 87.5, -4.0 and 310.0, `unit` with 1, 2 and 9, and `calibrated` with 99.97 and with 100.2 against a reference of 100.0 and a tolerance of 0.05.

```
normal
low
critical
C kPa ?
1 0
```

### 07.3 · Integrate

**The thermocouple that defends itself**

Write a class `Thermocouple` with a label, a temperature in degrees Celsius and a reject counter, all three private. The mutator accepts values between -200 and 1300 degrees; outside that range it leaves the data untouched, adds a reject and prints `rejected` followed by the value. Add a member function `state` that returns a `char`: `B` below zero, `N` up to 120, `A` up to 300 and `C` above.

Write a separate free function that takes an option number and the thermocouple by reference, and that with a four-case `switch` prints the temperature, the state, the number of rejects or the invalid option notice.

`main` assigns 87.5, then tries to assign 1500.0, and calls the function with options 1, 2, 3 and 7.

```
rejected 1500
87.5
N
1
invalid option
```

The validation has to live inside the class. If `main` checks the range before calling the mutator, the exercise does not count.

---

## Week 08 · Unit 6 · Control structures II

### 08.1 · Recognise

**A 3 by 4 grid with a continue**

```cpp
int main()
{
    int cells = 0;
    int sum = 0;

    for (int row = 1; row <= 3; row++)
    {
        for (int col = 1; col <= 4; col++)
        {
            if (col == 3)
                continue;
            cells++;
            sum = sum + row * col;
        }
    }

    int attempts = 0;
    int code = 5;

    do
    {
        attempts++;
        code = code - 2;
    } while (code > 5);

    std::cout << cells << " " << sum << "\n";
    std::cout << attempts << " " << code << "\n";
    return 0;
}
```

Write the two output lines and, next to the first, how many times the inner loop body started in total and how many times it was skipped. For the second, say how many times the same block written as a `while` with that same condition would have printed, and why.

### 08.2 · Apply

**First-order heating, step by step**

An RTD starts at 20 °C and goes into a furnace held at 100 °C. Its response is first order with a time constant of 5 s. With a 1 s step, the temperature at the next instant is `T = T + (dt / tau) * (Tamb - T)`.

Write a program with a `while` that advances step by step, prints the step number and the temperature of each, stops with `break` as soon as the temperature passes 90 °C, and never runs past twenty steps. At the end it prints how many steps were needed.

The first three lines and the last are:

```
1 36
2 48.8
3 59.04
...
steps 10
```

The 100.0, the 5.0, the 1.0 and the 90.0 go in named constants. No loose numbers inside the loop.

### 08.3 · Integrate

**First partial review: eight steps and one impossible reading**

This exercise crosses everything the first partial covers, unit 1 through unit 6, and brings no new material.

The bench simulates the temperature of step `k` with the formula `20.0 + 9.5 * k`, for `k` from 1 to 8. Write:

- a function that takes the step number and returns that temperature,
- a class `Thermocouple` with a label and an alarm limit in the constructor, and a member function `record` that discards any value outside the range -200 to 1300 degrees, printing `out of range` and the value, and that otherwise accumulates the sum, increases the count and adds an alarm if the value passes the limit,
- accessors for the count, the mean, the number of alarms and the label.

`main` walks the eight steps with a `for`, prints the step and the reading of each, then tries to record 1500.0, and closes with the summary. With TC-04 and a limit of 80 degrees:

```
1 29.5
...
8 96
out of range 1500
TC-04
accepted 8
mean 62.75
alarms 2
```

---

## Week 09 · Unit 7 · Inheritance and composition

### 09.1 · Recognise

**Thermocouple inheriting from Sensor**

```cpp
class Sensor {
public:
    Sensor(std::string e) { label = e; }
    std::string getLabel() { return label; }
    double toUnits(int count) { return count * 1.0; }
protected:
    std::string label;
};

class Thermocouple : public Sensor {
public:
    Thermocouple(std::string e, double p) : Sensor(e), slope(p) {}
    double toUnits(int count) { return count * slope; }
    std::string describe() { return label + " type K"; }
private:
    double slope;
};

int main()
{
    Thermocouple t("TC-04", 0.25);

    std::cout << t.getLabel() << "\n";
    std::cout << t.describe() << "\n";
    std::cout << t.toUnits(400) << "\n";

    Sensor s("PT-07");
    std::cout << s.toUnits(400) << "\n";
    return 0;
}
```

Write the four output lines. Answer as well: why `describe` can use `label` with no accessor at all, what error you get if `main` writes `t.label`, and what happens if `Sensor(e)` is removed from the initialiser list of the `Thermocouple` constructor.

### 09.2 · Apply

**Two sensors that inherit and a channel that composes**

Write a base class `Sensor` with a protected label and unit and public accessors. Derive two classes from it:

- `Thermocouple`, which holds a slope and a voltage at zero degrees, has unit `C`, and converts volts to degrees with `(volts - zero) / slope`,
- `StrainGauge`, which holds the gauge factor, has unit `um/m`, and converts a strain ratio to micrometres per metre with `ratio / factor * 1000000.0`.

Then write a class `Channel` that inherits from nobody, that has a `Thermocouple` as a member plus a channel number, and a member function that takes the voltage and prints the number, the label, the converted value and the unit.

`main` creates thermocouple TC-04 with slope 0.01 and zero at 0.5, strain gauge SG-11 with factor 2.05, and channel 3 with the thermocouple inside. The thermocouple is fed 2.31 V and the gauge a ratio of 0.000205.

```
TC-04 181 C
SG-11 100 um/m
3 TC-04 181 C
```

Close with a three-line comment applying the sentence test to both decisions: why `Thermocouple` inherits and why `Channel` does not.

### 09.3 · Integrate

**Test bench with a thermocouple inside**

Write a class `TestBench` whose members are a name, a `Thermocouple` by composition and an alarm limit, plus whatever accumulators it needs. Its member function `measure` takes the voltage, converts it with the sensor it carries inside, accumulates, and prints `ALARM` with the label and the value if it passes the limit, or `ok` with the same data if it does not.

`main` builds thermocouple TC-04 with slope 0.01 and zero at 0.5, creates the bench `Furnace 2` with a limit of 120 degrees, and walks five voltages generated as `1.0 + 0.4 * k` with `k` from 0 to 4 inside a `for`. At the end it prints the bench name, the mean of everything measured and the number of alarms.

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

---

## Week 10 · Unit 8 · Arrays and strings

### 10.1 · Recognise

**Six readings, two hyphens and a size worked out**

```cpp
int main()
{
    int readings[6] = {118, 121, 117, 123, 119, 130};
    int n = sizeof(readings) / sizeof(readings[0]);

    int sum = 0;
    for (int i = 0; i < n; i++)
        sum = sum + readings[i];

    std::string label = "SG-11-BEAM";
    int hyphens = 0;
    for (int i = 0; i < static_cast<int>(label.length()); i++)
        if (label.at(i) == '-')
            hyphens++;

    std::cout << n << " " << sum << "\n";
    std::cout << readings[n - 1] << " " << hyphens << "\n";
    return 0;
}
```

Write the two output lines. Then answer: what the second line would print if it said `readings[n]` instead of `readings[n - 1]`, whether the program would fail while running, and what happens to `n` if that same `sizeof` calculation is done inside a function that receives the array as a parameter.

### 10.2 · Apply

**Statistics of eight strain readings**

A strain gauge on the beam delivered eight strain readings, in micrometres per metre: 118, 121, 117, 123, 119, 130, 112 and 126.

Write a program that keeps the eight in an array, works out the element count with `sizeof`, and in a single pass obtains the sum, the highest reading and the lowest. Then, in a second pass, counts how many sit above the mean.

```
n 8
mean 120.75
highest 130
lowest 112
range 18
above 4
```

No loop may carry the number 8 written by hand. Changing the array to nine readings must not force a change to any other line.

### 10.3 · Integrate

**The same eight readings, spread across functions**

Rewrite 10.2 with four functions and a `main` that only calls and prints:

- `mean` takes the array as `const int data[]` and its size, and returns a `double`,
- `extremes` takes the same and hands back the highest and the lowest through two reference parameters,
- `countAbove` takes the array, the size and a threshold, and returns how many pass it,
- `countDigits` takes a `const std::string&` and returns how many of its characters are digits.

With the same eight readings and the label `SG-11-BEAM-A3`:

```
SG-11-BEAM-A3 13 3
mean 120.75
highest 130 lowest 112
above the mean 4
above 125 2
```

Explain in two lines why the functions take the size as a parameter instead of working it out inside.

---

## Week 11 · Unit 9 · Records

### 11.1 · Recognise

**Copying a record and measuring what it takes up**

```cpp
struct Sample {
    int t_ms;
    double value;
};

int main()
{
    Sample a;
    a.t_ms = 100;
    a.value = 2.5;

    Sample b = a;
    b.value = 9.9;

    Sample table[3];
    table[0] = a;
    table[1] = b;
    table[2].t_ms = 300;
    table[2].value = 1.25;

    std::cout << a.value << " " << b.value << "\n";
    std::cout << table[1].t_ms << " " << table[2].value << "\n";
    std::cout << sizeof(Sample) << " " << sizeof(table) << "\n";
    return 0;
}
```

Write the three output lines. The third has a number that is not the sum of the field sizes: say what the sum is, what gets printed and why the compiler decided that. Say as well which field of `table[2]` would hold rubbish if it were printed before the two assignments.

### 11.2 · Apply

**Six time-stamped samples**

The acquisition unit stores pairs of time and voltage. Today's run left these six: (0, 2.41), (100, 2.65), (200, 3.12), (300, 2.98), (400, 3.44) and (500, 3.05), with the time in milliseconds.

Write a `struct Sample` with the two fields, a function `make` that takes both values and returns the assembled sample, and a `main` that fills an array of six by calling that function. In a single pass work out the sum and the index of the sample with the highest value. Print the whole table separated by tabs, the mean, and the maximum with its time stamp.

```
t_ms	value
0	2.41
...
500	3.05
mean 2.94167
max 3.44 at 400 ms
```

### 11.3 · Integrate

**The table with one invalid sample**

Repeat the table from 11.2, except that the 200 ms sample arrived as -1.00, which is impossible on this channel. Write:

- `valid`, which takes a `const Sample&` and returns `false` if the time is negative or the value is not greater than zero,
- `meanOfValid`, which takes the table as `const Sample table[]`, the size and a reference parameter where it leaves how many it used, prints `discarded` with the time stamp of each rejection, and returns the mean of the survivors,
- `extremes`, which leaves in two reference parameters the indices of the highest and the lowest among the valid ones.

```
discarded 200 ms
records 6 valid 5
mean 2.906
max 3.44 at 400 ms
min 2.41 at 0 ms
```

Explain in two lines why the functions take the table by constant reference and not by value.

---

## Week 12 · Unit 10 · Pointers, virtual and abstract

### 12.1 · Recognise

**A pointer, a virtual and one that is not**

```cpp
class Sensor {
public:
    virtual double convert(int count) { return count * 1.0; }
    double scale() { return 1.0; }
    virtual ~Sensor() {}
};

class Thermocouple : public Sensor {
public:
    double convert(int count) override { return count * 0.25; }
    double scale() { return 0.25; }
};

int main()
{
    int count = 400;
    int* p = &count;

    *p = 800;

    Thermocouple t;
    Sensor* s = &t;

    std::cout << count << " " << (p == &count) << "\n";
    std::cout << s->convert(count) << " " << s->scale() << "\n";

    Sensor* d = new Thermocouple();
    std::cout << d->convert(100) << "\n";
    delete d;
    return 0;
}
```

Write the three output lines. The second has two numbers coming out of two nearly identical functions of the same class: explain who decides which one runs in each case, and when that decision is taken. Say as well what leaks if the `delete` line is removed, and what leaks differently if instead the `virtual` is taken off the destructor.

### 12.2 · Apply

**Three channels through an array of pointers**

Write an abstract class `Sensor` with a protected label, two pure virtual functions, one converting a count to engineering units and another returning the unit, an accessor for the label and a virtual destructor. Derive `Thermocouple`, which multiplies the count by its slope and reports `C`, and `StrainGauge`, which divides the count by its factor and reports `um/m`.

`main` declares an array of three pointers to `Sensor`, fills it with `new` using TC-04 at slope 0.25, SG-11 at factor 2.05 and TC-05 at slope 0.50, and walks counts 400, 410 and 300 in a single loop, printing label, value and unit, and counting how many pass 120. At the end it frees all three.

```
TC-04 100 C
SG-11 200 um/m
TC-05 150 C
over 120: 2
```

Not one `if` asking what type each object is. If one shows up, a `virtual` is missing.

### 12.3 · Integrate

**The same channels without a single delete**

Rewrite 12.2 with two changes. The array of raw pointers becomes an array of `std::unique_ptr<Sensor>` built with `std::make_unique`, and the samples stop being loose: use a `struct Sample` with a time stamp and a count, reserved with `new Sample[4]` and released with `delete[]`, filled in a loop with times from 0 to 300 ms in hundreds and counts from 400 to 460 in twenties.

For each of the two channels, TC-04 at slope 0.25 and SG-11 at factor 2.05, print the mean of the four converted samples.

```
TC-04 mean 107.5 C
SG-11 mean 209.756 um/m
```

Finish by printing how many `new` were left without their partner, and explain in three lines which lines of the previous version disappeared when you moved to `unique_ptr`.

---

## Week 13 · Unit 11 · Input and output

### 13.1 · Recognise

**The eof loop and the file that is not there**

```cpp
std::ofstream out("log.txt");
out << "TC-04 100 2.41\n";
out << "TC-04 200 2.65\n";
out << "TC-04 300 3.12\n";
out.close();

std::ifstream in("log.txt");
std::string label;
int t = 0;
double v = 0.0;
int lines = 0;

while (!in.eof())
{
    in >> label >> t >> v;
    std::cout << t << " " << v << "\n";
    lines++;
}
in.close();

std::cout << "lines " << lines << "\n";

std::ifstream missing("missing.txt");
int n = 7;
missing >> n;

std::cout << missing.is_open() << " " << n << "\n";
```

The file holds three lines. Write everything the program prints, which is six lines. Explain why the count does not come out at 3, where the values on the repeated line come from, and why reading the missing file leaves `n` as it was instead of setting it to zero. Write the loop condition that fixes the first problem.

### 13.2 · Apply

**Furnace log, written and read back**

Write a program that creates the file `furnace.txt` with six lines, each carrying the label `TC-04`, the time stamp in milliseconds and the temperature: (0, 21.5), (100, 48.2), (200, 76.9), (300, 98.4), (400, 121.7) and (500, 133.0). Close it, reopen it for reading and walk it end to end without knowing beforehand how many records it holds, using the read itself as the loop condition.

The program checks `is_open` after opening, both when writing and when reading, and if that fails it prints a notice and ends with code 1. At the end it reports how many records it read, the mean of the temperatures and how many passed 100 degrees.

```
records 6
mean 83.2833
over 100 C 2
```

### 13.3 · Integrate

**Second partial review: from file to report**

This exercise crosses what the second partial covers, unit 1 through unit 11, and brings no new material.

Write a program that generates `bench.txt` with six lines of label, time and temperature, where the third carries 9999.0 because the channel came loose. Then:

- declare a `struct Record` with the three fields and an array of ten,
- read the file inside a loop that stops on end of file or on filling the array, whichever comes first, checking `is_open` beforehand,
- pass each record to a class `Channel` that discards anything outside the range -200 to 1300 degrees, accumulates the rest and counts the alarms above 100 degrees,
- print the summary.

```
TC-04
read 6
accepted 5
discarded 1
mean 84.56
alarms 2
```

The class does not read the file and `main` does not validate ranges. Each one does a single job.

---

## Week 14 · Unit 12 · Overloading and templates

### 14.1 · Recognise

**Adding forces and two versions of one template**

```cpp
class Force {
public:
    Force(double a, double b) : x(a), y(b) {}
    Force operator+(Force o) { return Force(x + o.x, y + o.y); }
    bool operator==(Force o) { return x == o.x && y == o.y; }
    double x;
    double y;
};

template <typename T>
T larger(T a, T b)
{
    if (a > b)
        return a;
    return b;
}

int main()
{
    Force f1(120.0, 45.0);
    Force f2(30.5, 15.0);

    Force sum = f1 + f2;

    std::cout << sum.x << " " << sum.y << "\n";
    std::cout << (sum == Force(150.5, 60.0)) << "\n";
    std::cout << larger(3, 9) << " " << larger(2.5, 1.5) << "\n";
    return 0;
}
```

Write the three output lines. Say how many concrete functions the compiler generates from the template in this program and with which types, what is left of the template in the executable, and what error shows up if somebody adds the call `larger(f1, f2)`.

### 14.2 · Apply

**A measurement that adds, compares and prints**

Write a class `Measurement` with a `double` value and a `std::string` unit, both private. Overload as member functions the addition, which returns a new measurement carrying the unit of the left operand, the equality, which compares value and unit, and the greater than, which compares only the value. Overload as well the output operator as a free function, so that `cout` prints the value and the unit separated by a space.

Write two templates: `larger`, which returns the larger of two values of any type, and `average`, which takes an array of any type and its size and returns a `double`.

`main` uses measurements of 120.5 kPa and 98.3 kPa, the pressure array {120.5, 98.3, 105.0, 111.4} and the count array {400, 410, 300}, and also calls `larger` with the pair 3 and 7 and with the pair 9.75 and 2.5.

```
218.8 kPa
0 1
120.5 kPa
7 9.75
108.8
370
```

### 14.3 · Integrate

**A buffer that serves any type**

Write a class template `Buffer` with a fixed capacity of 5, declared in a global constant. It keeps the elements in an internal array, tracks how many it holds, and exposes three functions: add, which prints `buffer full` and stores nothing once there is no room; get by index; and size.

Test it twice. First with `Buffer<double>` and the voltages 2.41, 2.65 and 3.12, printing how many it stored and their mean. Then with `Buffer<Sample>`, where `Sample` is the week 11 record with a time stamp and a value, pushing in six samples generated with times in hundreds and values `2.41 + 0.25 * i`. Overload the output operator for `Sample` and walk the buffer printing each one.

```
volts 3 mean 2.72667
buffer full
records 5
0 ms 2.41
...
400 ms 3.41
```

Explain in two lines why the buffer full message appears before the record count.

---

## Week 15 · Unit 13 · Exception handling

### 15.1 · Recognise

**What order it prints in, and who catches what**

```cpp
double ratio(double a, double b)
{
    if (b == 0.0)
        throw std::invalid_argument("zero divisor");
    return a / b;
}

int main()
{
    std::string label = "TC-04";

    try
    {
        std::cout << "A";
        std::cout << ratio(10.0, 4.0) << " ";
        std::cout << label.at(9) << " ";
        std::cout << "B";
    }
    catch (const std::out_of_range&)
    {
        std::cout << "C";
    }
    catch (const std::exception&)
    {
        std::cout << "D";
    }

    std::cout << "E\n";

    try
    {
        std::cout << ratio(10.0, 0.0) << "\n";
    }
    catch (const std::exception& e)
    {
        std::cout << e.what() << "\n";
    }
}
```

Write the two output lines, character by character. Explain what became of the `B`, which of the two `catch` blocks caught the problem in the first block and why the other did not, and why the second block does catch an `invalid_argument` with a `catch` that says `exception`.

### 15.2 · Apply

**The calibration that refuses to exist wrong**

Write a class `Calibration` with a label, a slope and a voltage at zero degrees. If the constructor receives a slope of zero, it throws `std::invalid_argument` with a message that includes the label, because a slope of zero defines no conversion at all. Add the member function that converts volts to degrees.

Write a separate free function `resistance` that takes volts and amperes and throws `std::runtime_error` if the current is zero.

`main` makes three attempts, each inside its own `try` block: it creates the good calibration TC-04 with slope 0.01 and zero at 0.5 and converts 2.31 V; it tries to create TC-09 with slope 0.0; and it works out the resistance with 12 V at 0.5 A and then with 12 V at 0 A. The program never dies mid-way.

```
TC-04 181 C
error: zero slope on TC-09
24 ohm
error: zero current, no resistance to measure
the program carries on
```

Every `catch` takes by constant reference. The class detects and `main` decides.

### 15.3 · Integrate

**A batch with one short line**

The file `batch.txt` carries four lines with a label and a temperature. A normal label carries the zone at position 6, as in `TC-04-A`, but the third line was recorded as `TC-04`, with no zone. The program writes that file before reading it, with the lines `TC-04-A 21.5`, `TC-04-B 48.2`, `TC-04 76.9` and `TC-04-C 98.4`.

Write a function that takes a `std::ifstream&` by reference and a path, opens the file and throws `std::runtime_error` if it could not be opened. In `main`, walk the file with the read as the condition and, inside the loop, pull the zone out with `at`. The short line throws `std::out_of_range`, which is caught inside that same loop, reported, and does not stop the reading of the rest. At the end, a second block tries to open `missing.txt` to show the other exception.

The mean reported at the end is the mean of the three temperatures that could be read:

```
zone A 21.5
zone B 48.2
malformed line: TC-04
zone C 98.4
good 3 bad 1
mean 56.0333
error: could not open missing.txt
```

---

## Week 16 · Unit 14 · Recursion and concurrency

### 16.1 · Recognise

**Three recursions and one that never ends**

```cpp
int sumTo(int n)
{
    if (n <= 0)
        return 0;
    return n + sumTo(n - 1);
}

int steps(int n)
{
    if (n <= 1)
        return 0;
    return 1 + steps(n / 2);
}

double power(double base, int exp)
{
    if (exp == 0)
        return 1.0;
    return base * power(base, exp - 1);
}

int main()
{
    std::cout << sumTo(5) << "\n";
    std::cout << steps(64) << "\n";
    std::cout << power(2.0, 10) << "\n";
    return 0;
}
```

Write the three output lines. For `steps(64)`, draw the chain of calls with the value of `n` in each one and say how many frames are alive at the same time. Then answer what becomes of `power` if it is called with exponent -1, and why that does not hang like an infinite loop but ends the program instead.

### 16.2 · Apply

**Recursive binary search and a counter with a lock**

The ADC calibration table is sorted: 512, 1024, 1536, 2048, 2560, 3072, 3584 and 4095.

Write a recursive function that takes the array, the left index, the right index and the value being sought, and returns the index where it sits or -1 if it is not there. Write as well a recursive function that sums an array of `double` without using any loop. Test them by searching for 2560, searching for 2600, and summing the voltages 2.41, 2.65, 3.12, 2.98 and 3.44.

Close with the concurrency part: a global `long long`, a `std::mutex`, and a function that increments it a hundred thousand times, taking the lock with `std::lock_guard` on every turn. Launch two `std::jthread` on that function inside a block, and print the total on leaving the block.

```
4
-1
14.6
200000
```

Then run the same test with the `lock_guard` removed, three times in a row, and note the three totals you got. Explain in three lines why none of them matches the others and why the locked version always gives the same number.

### 16.3 · Integrate

**Third partial review: full test run**

The third partial covers the whole course, unit 1 through 14. This exercise pulls the core of every block into a single program.

Write a program that generates `run.txt` with four lines of label, time and count: (0, 400), (100, 420), (200, 460) and (300, 512). Then:

- a `struct Record` with the three fields,
- a function `read` that takes the path, the array, its capacity and a reference parameter for the count, and that throws `std::runtime_error` if the file does not open,
- an abstract class `Sensor` with pure virtual conversion and unit, and the usual two derived classes, kept in an array of `std::unique_ptr`,
- a recursive function that returns the highest count in the array, with no loops.

`main` reads the file inside a `try`, prints how many records it holds and the maximum count, walks the two channels printing the converted mean of each, and finishes by trying to read a file that does not exist so the exception message shows.

```
records 4
max count 512
TC-04 mean 112 C
SG-11 mean 218.537 um/m
error: could not open missing.txt
```

---

## Week 17 · Closing · Integrating project

### 17.1 · Recognise

**Four defects with the program working**

This program compiles, runs and does not crash. It is the kind of submission that loses half the rubric without anybody seeing an error on screen.

```cpp
class Sensor {
public:
    Sensor(std::string e) : label(e) {}
    virtual double convert(int count) { return count * 1.0; }
    ~Sensor() { std::cout << "closing Sensor\n"; }
protected:
    std::string label;
};

class Thermocouple : public Sensor {
public:
    Thermocouple(std::string e, double p) : Sensor(e), slope(p) {}
    double convert(int count) override { return count * slope; }
    ~Thermocouple() { std::cout << "closing Thermocouple\n"; }
private:
    double slope;
};

double process(const std::string& path)
{
    std::ifstream in(path);
    std::string label;
    int count = 0;
    double sum = 0.0;
    int n = 0;

    while (in >> label >> count)
    {
        sum += count;
        n++;
        std::cout << label << " " << count << "\n";
    }

    std::cout << "mean " << sum / n << "\n";
    return sum / n;
}

int main()
{
    Sensor* primary = new Thermocouple("TC-04", 0.25);
    Sensor* backup = new Thermocouple("TC-05", 0.50);

    std::cout << primary->convert(400) << "\n";
    std::cout << backup->convert(400) << "\n";

    double m = process("missing.txt");
    std::cout << "result " << m << "\n";

    delete primary;
    return 0;
}
```

1. Write the five lines it prints, with `missing.txt` absent.
2. Point out four defects, one for each criterion of the project rubric, and say which line each one is on and what evidence in the output gives it away.
3. Count the `new` and the `delete`, say how much memory is left unreleased, and why the one `delete` that is there does not do its full job either.

### 17.2 · Apply

**The same program, no leaks and with a notice**

Rewrite 17.1 with four corrections and nothing else:

- the base destructor becomes virtual and the conversion becomes pure virtual,
- the two raw pointers become `std::unique_ptr` created with `std::make_unique`,
- the function that processed gets split in two: one that reads the file into an array of counts and returns `bool` depending on whether it opened, and another that works out the mean,
- `main` gives a clear message when the file does not open, instead of printing a result that means nothing.

The program generates `run17.txt` with four lines of label and count, 400, 420, 460 and 512, tries to read a file that does not exist first and then the good one.

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

Explain in three lines why the last four lines appear now and did not in the previous program, and in what order the two objects are destroyed.

### 17.3 · Integrate

**From the instrumentation file to the final report**

Closing exercise. It is the size and the shape of what the project is expected to be, in a single piece.

Write a program that generates `run17b.txt` with five lines of label, time and count: (0, 400), (100, 420), (200, 5000), (300, 460) and (400, 512). The third count does not fit in a 12-bit converter and has to be discarded. Then:

- `struct Reading` with the three fields, and the output operator overloaded to print it on one line,
- `read`, which throws `std::runtime_error` if the file does not open,
- `valid`, which rejects counts outside the range 0 to 4095,
- a template `average` that serves any numeric array type,
- a recursive function that returns the maximum count,
- an abstract class `Sensor` with two derived classes, kept in an array of `std::unique_ptr`, with TC-04 at slope 0.25 and SG-11 at factor 2.05.

`main` reads inside a `try`, separates the valid from the discarded printing each rejection with the output operator, and closes with the report.

```
discarded TC-04 200 ms 5000
read 5 valid 4
mean count 448
max count 512
TC-04 112 C
SG-11 218.537 um/m
```

When you are done, run the block 1 review from the session over your own program: count the `new` against the `delete`, find the longest function and decide whether it is really two, and check what it prints if you delete the file before running it.
