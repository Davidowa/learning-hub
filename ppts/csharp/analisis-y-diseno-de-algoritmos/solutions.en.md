# Solutions · Analysis and Design of Algorithms · COM101

Instructor copy. Every solution was compiled and run with SDK 10.0.302 against `net10.0` before it was written down, and the output that appears here is what the machine produced, not what it ought to produce. Exit codes were measured in PowerShell 7 on Windows 11. The numbering is the same as the exercise file.

## Week 01 · Course framing and grading

### 01.1 · Recognise

**Solution**

```csharp
Console.WriteLine(10478 / 7);
Console.WriteLine(0.1 + 0.7);
Console.WriteLine(0.1 + 0.7 == 0.8);
```

Both operands of the first line are integers, so the slash does integer division and throws the remainder away. The second and the third are the same fact seen twice: 0.1 and 0.7 have no exact representation in binary and their sum lands a little under 0.8.

**Output**

```text
1496
0.7999999999999999
False
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The three predictions are written before the run | 3 |
| The three real outputs are pasted unedited | 3 |
| Explains that the slash between two integers truncates | 2 |
| Explains that the binary sum does not land on 0.8 | 2 |

**Most common mistake**

They write 1496.857142857143 as the first prediction; it gives itself away because the same sheet later accepts that the result was 1496 without explaining where the change came from.

### 01.2 · Apply

**Solution**

```csharp
Console.WriteLine("EST-07 TEST BENCH");
Console.WriteLine("Channel A · roller conveyor");
Console.WriteLine("Nominal band: 1480 to 1520 rpm");
Console.WriteLine(Environment.Version);
```

**Output**

```text
EST-07 TEST BENCH
Channel A · roller conveyor
Nominal band: 1480 to 1520 rpm
10.0.10
```

The exit code was 0. The last line depends on the machine: `Environment.Version` reports the runtime and `dotnet --version` reports the SDK, and on this box they are 10.0.10 and 10.0.302.

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The three text lines come out in the order asked for | 3 |
| The `Environment.Version` value of their own machine appears | 3 |
| The run was done with `dotnet run` and the terminal is visible | 2 |
| Reports the exit code | 2 |

**Most common mistake**

They copy the version number off a classmate's capture; it gives itself away because the number does not match the `dotnet --version` they handed in on the same sheet.

### 01.3 · Integrate

**Solution**

With `<ImplicitUsings>disable</ImplicitUsings>` the compiler stops generating `obj/Debug/net10.0/est07.GlobalUsings.g.cs`, so `Console` no longer exists in the context. The line that fixes it without touching the `csproj` is `using System;` at the top of the file.

```csharp
using System;

Console.WriteLine("EST-07 online");
```

**Output**

With the property off and without the `using`:

```text
Program.cs(1,1): error CS0103: The name 'Console' does not exist in the current context

Build FAILED.
    0 Warning(s)
    1 Error(s)
```

The `bin/Debug/net10.0` folder is left with zero files. With the `using` added the build passes and the program prints `EST-07 online`.

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| Quotes the full message with file, line, column and error code | 3 |
| Reports that the output folder was left empty | 3 |
| Gives the line `using System;` and checks it by running | 3 |
| Tells the generated file apart from the `csproj` that asks for it | 1 |

**Most common mistake**

They put the property back to `enable` and report that it works now; it gives itself away because the `csproj` they hand in carries `disable` nowhere.

## Week 02 · Unit 1 · Algorithm design

### 02.1 · Recognise

**Solution**

The trace has seven lines. The level starts at 12.0 and climbs 15.0 at a time until the condition stops holding.

| Step | level before | level after | What it prints |
|---|---|---|---|
| 0 | 12.0 | 12.0 | AIR PURGE STARTED |
| 1 | 12.0 | 27.0 | filling tank: 27.0 L |
| 2 | 27.0 | 42.0 | filling tank: 42.0 L |
| 3 | 42.0 | 57.0 | filling tank: 57.0 L |
| 4 | 57.0 | 72.0 | filling tank: 72.0 L |
| 5 | 72.0 | 72.0 | level reached, open recirculation pump |
| 6 | 72.0 | 72.0 | bench ready |

The tank ends with 72.0 litres, not 60.0. The condition is tested before every pulse and the last pulse goes in whole, so the level overshoots the setpoint by twelve litres.

**Output**

Run of the pseudocode translated into C#:

```text
AIR PURGE STARTED
filling tank: 27.0 L
filling tank: 42.0 L
filling tank: 57.0 L
filling tank: 72.0 L
level reached, open recirculation pump
bench ready
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The four level values are 27.0, 42.0, 57.0 and 72.0 | 4 |
| Counts the seven lines, header and closing line included | 2 |
| Says the tank ends at 72.0 and not at 60.0 | 2 |
| Explains that the pulse goes in whole after the test | 2 |

**Most common mistake**

They write three pulses and leave the tank at 57.0, because they stop once the level is nearly there; it gives itself away because their last line says ABORT even though the level they wrote down is under the setpoint they copied themselves.

### 02.2 · Apply

**Solution**

```text
START
    READ door, estop, rpm

    IF door = closed THEN
        IF estop = released THEN
            IF rpm < 50 THEN
                WRITE "ARMED"
            ELSE
                WRITE "INTERLOCKED: the shaft is still turning"
        ELSE
            WRITE "INTERLOCKED: emergency stop pressed"
    ELSE
        WRITE "INTERLOCKED: guard door open"
END
```

The flowchart carries three diamonds in cascade, each one with its NO exit running to a different message rectangle, and a single YES path that reaches the ARMED rectangle.

**Output**

Expected trace, written before anything was run:

```text
guard door closed, e-stop released, 20 rpm
ARMED

guard door open, e-stop released, 20 rpm
INTERLOCKED: guard door open
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The three conditions are tested in the order asked for | 3 |
| Every failure names its cause instead of a generic message | 3 |
| The diagram has the three diamonds with their two exits | 2 |
| The two expected traces are written before the run | 2 |

**Most common mistake**

One diamond with the three conditions glued together and one INTERLOCKED message; it gives itself away because the second data set cannot say which of the three failed.

### 02.3 · Integrate

**Solution**

The original instruction breaks precision: "firm" is decided by whoever reads it, and two technicians will tighten differently. It breaks finiteness too, because "until it feels firm" never says in how many steps it ends.

```text
START
    lines = 0

    FOR pass = 1 TO 3
        torque = pass * 8
        FOR bolt = 1 TO 4
            WRITE "pass", pass, "bolt", bolt,
                  ": tighten to", torque, "N·m"
            lines = lines + 1

    WRITE "tightening finished in", lines, "operations"
END
```

**Output**

```text
pass 1 bolt 1: tighten to 8 N·m
pass 1 bolt 2: tighten to 8 N·m
pass 1 bolt 3: tighten to 8 N·m
pass 1 bolt 4: tighten to 8 N·m
pass 2 bolt 1: tighten to 16 N·m
pass 2 bolt 2: tighten to 16 N·m
pass 2 bolt 3: tighten to 16 N·m
pass 2 bolt 4: tighten to 16 N·m
pass 3 bolt 1: tighten to 24 N·m
pass 3 bolt 2: tighten to 24 N·m
pass 3 bolt 3: tighten to 24 N·m
pass 3 bolt 4: tighten to 24 N·m
tightening finished in 12 operations
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| Names the property that breaks and argues for it | 2 |
| The two FOR loops are nested and the torque comes off the pass | 3 |
| The trace carries the twelve lines in the right order | 3 |
| The last line reports 12 operations | 2 |

**Most common mistake**

They nest it the other way round, with the bolt outside and the pass inside, and tighten each bolt to 24 N·m before touching the next; it gives itself away because the trace they hand in climbs the torque in threes inside a single bolt, which is exactly what cross-pattern tightening exists to prevent.

## Week 03 · Unit 2 · Introduction to programming

### 03.1 · Recognise

**Solution**

| Case | Compiles | First message | What it misread |
|---|---|---|---|
| A | no | `Program.cs(2,33): error CS1002: ; expected` | The statement never ended and it is still waiting |
| B | no | `Program.cs(2,5): error CS1001: Identifier expected` | It read `int`, expected a name and found a digit |
| C | no | `Program.cs(2,9): error CS0117: 'Console' does not contain a definition for 'writeline'` | The type exists, the member with that case does not |
| D | no | `Program.cs(2,19): error CS0103: The name 'NominalTorque' does not exist in the current context` | The name belongs to the student and exists nowhere |
| E | no | `Program.cs(1,5): error CS1001: Identifier expected` | `class` is a reserved word and cannot be a name |

Case E returns seven errors. After the `int class` the parser believes a type declaration is starting, and everything that follows on the same line becomes a fresh stumble: `CS1002`, another `CS1001`, `CS1514`, `CS1513`, `CS8803` and `CS1525`.

**Output**

```text
E · int class = 7;

Program.cs(1,5): error CS1001: Identifier expected
Program.cs(1,5): error CS1002: ; expected
Program.cs(1,11): error CS1001: Identifier expected
Program.cs(1,11): error CS1514: { expected
Program.cs(1,11): error CS1513: } expected
Program.cs(1,11): error CS8803: Top-level statements must precede namespace and type declarations.
Program.cs(1,11): error CS1525: Invalid expression term '='

Build FAILED.
    0 Warning(s)
    7 Error(s)
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The five codes are assigned correctly | 5 |
| Identifies case E as the one with seven errors | 2 |
| Explains that C and D fail on case but with different codes | 2 |
| Not one of the five is declared to compile | 1 |

**Most common mistake**

They say C and D give the same code because both are about capitals; it gives itself away because they never paste the message, they only describe it.

### 03.2 · Apply

**Solution**

```csharp
// Week 3 · 3.2 · case sensitivity and naming conventions
int nominalTorque = 24;      // nominal tightening torque, in N·m
/* The same word written in another
   case is a different variable. */
int NominalTorque = 26;
int NOMINALTORQUE = 22;

Console.WriteLine($"nominalTorque={nominalTorque} NominalTorque={NominalTorque} NOMINALTORQUE={NOMINALTORQUE}");
Console.WriteLine("different: " + (nominalTorque != NominalTorque));
Console.WriteLine("text with // inside: " + "check // before the shift");
Console.WriteLine("Console vs console: " + ("Console" == "console"));
```

**Output**

```text
nominalTorque=24 NominalTorque=26 NOMINALTORQUE=22
different: True
text with // inside: check // before the shift
Console vs console: False
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The three variables coexist and print on one line | 3 |
| Both comments are present and the `//` inside the text survives | 3 |
| The comparison of the two strings prints `False` | 2 |
| The names follow camelCase and one comment states the unit | 2 |

**Most common mistake**

They write `nominaltorque` in one of the three prints and the program stops compiling with `CS0103`; it gives itself away because they hand in the `.cs` with no output and a note saying it would not run.

### 03.3 · Integrate

**Solution**

Four files, four attempts, one message each.

```csharp
// A · missing semicolon
int nominalTorque = 24;
Console.WriteLine(nominalTorque)

// B · identifier that opens with a digit
int nominalTorque = 24;
int 2sensor = 7;

// C · member with the wrong case
int nominalTorque = 24;
Console.writeline(nominalTorque);

// D · own name with the wrong case
int nominalTorque = 24;
Console.WriteLine(NominalTorque);
```

**Output**

```text
A  Program.cs(2,33): error CS1002: ; expected
B  Program.cs(2,5): error CS1001: Identifier expected
C  Program.cs(2,9): error CS0117: 'Console' does not contain a definition for 'writeline'
D  Program.cs(2,19): error CS0103: The name 'NominalTorque' does not exist in the current context
```

C and D come out of the same slip and return different codes because the name in C belongs to the framework. `Console` does exist, so the compiler can say exactly which member is missing. `NominalTorque` exists nowhere, and the only thing it can answer is that it does not know it.

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The four messages are copied verbatim, with line and column | 4 |
| Each case carries a line saying what the compiler misread | 3 |
| Explains the difference between CS0117 and CS0103 | 2 |
| The four attempts were run separately | 1 |

**Most common mistake**

They put the four slips into one file and report the first message of the pile; it gives itself away because the code they quote is `CS1003` and it appears in none of the four cases run on their own.

## Week 04 · Unit 3 · Data, types and primitive operations

### 04.1 · Recognise

**Solution**

```csharp
int lo = 1471, hi = 1533;
Console.WriteLine(lo + hi / 2);
Console.WriteLine((lo + hi) / 2);
Console.WriteLine((lo + hi) / 2.0);
Console.WriteLine(hi % 100);
Console.WriteLine(7 / 2 * 2);
```

Division binds tighter than addition, so the first line computes 1471 plus 766. The third divides by a real literal and the result no longer truncates, even though in this case the sum is even and the number happens to match. The fifth groups left to right: 7 over 2 gives 3, then 3 times 2 gives 6.

**Output**

```text
2237
1502
1502
33
6
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The five predictions match the run | 5 |
| Points at the first line as the one no tachometer can read | 2 |
| Names precedence as the cause | 2 |
| Explains the 6 of the last line through associativity | 1 |

**Most common mistake**

They predict 3.5 on the last line; it gives itself away because the same sheet accepts two lines earlier that the slash between integers truncates.

### 04.2 · Apply

**Solution**

```csharp
const double Nominal = 25.0;

string station = "EST-11";
char channel = 'C';
int samples = 12;
double measured = 24.972;
bool online = true;

double dev = measured - Nominal;
bool inside = Math.Abs(dev) <= 0.05;

Console.WriteLine($"station {station} channel {channel}");
Console.WriteLine($"samples {samples}  online {online}");
Console.WriteLine($"measured {measured:F3} mm");
Console.WriteLine($"nominal  {Nominal:F3} mm");
Console.WriteLine($"raw deviation {dev}");
Console.WriteLine($"deviation {dev:F3} mm");
Console.WriteLine($"within +-0.05 -> {inside}");
```

**Output**

```text
station EST-11 channel C
samples 12  online True
measured 24.972 mm
nominal  25.000 mm
raw deviation -0.027999999999998693
deviation -0.028 mm
within +-0.05 -> True
```

The raw deviation is not -0.028. Subtracting two numbers that neither of them fits exactly in binary leaves fifteen digits of noise, and that is why tolerance gets checked with `Math.Abs` against a margin and never with an equality.

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The five types are present and each holds the value that belongs to it | 3 |
| The nominal dimension sits under `const` | 2 |
| The deviation prints raw and to three decimals | 2 |
| Tolerance is checked with `Math.Abs` and not with `==` | 3 |

**Most common mistake**

They declare `int measured = 24;` because the gauge gives millimetres; it gives itself away because their deviation prints -1 and the tolerance comes out `False` on a part that was good.

### 04.3 · Integrate

**Solution**

```csharp
byte parts = 250;
parts += 10;
Console.WriteLine($"parts inspected:   {parts}");

short window = 32000;
window += 1000;
Console.WriteLine($"sampling window:   {window}");

double raw = 0.5 + 1.5 + 2.5 + 3.5;
double toEven = Math.Round(0.5) + Math.Round(1.5)
              + Math.Round(2.5) + Math.Round(3.5);
double away = Math.Round(0.5, MidpointRounding.AwayFromZero)
            + Math.Round(1.5, MidpointRounding.AwayFromZero)
            + Math.Round(2.5, MidpointRounding.AwayFromZero)
            + Math.Round(3.5, MidpointRounding.AwayFromZero);

Console.WriteLine($"raw sum            {raw}");
Console.WriteLine($"sum, half to even  {toEven}");
Console.WriteLine($"sum, half away     {away}");

int lo = 1471, hi = 1533;
Console.WriteLine($"no brackets {lo + hi / 2}");
Console.WriteLine($"brackets    {(lo + hi) / 2}");
```

**Output**

```text
parts inspected:   4
sampling window:   -32536
raw sum            8
sum, half to even  8
sum, half away     10
no brackets 2237
brackets    1502
```

The `+=` slips in a cast that the long form does not have, so the first two lines build with zero warnings and wrap around in silence. For reporting accumulated wear the half-to-even rule is the one to take, because over many values it does not drag a bias upwards: over these four deviations it gives 8, the same total as the real sum, while half away from zero gives 10.

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| Both overflows are reported with their real value | 3 |
| The three rounding sums are present and do not agree | 3 |
| Both versions of the midpoint were run | 2 |
| Justifies the rounding rule through bias, not through taste | 2 |

**Most common mistake**

They report that the `byte` gives an error; it gives itself away because their capture shows `Build succeeded` with zero warnings right above the 4.

## Week 05 · Unit 4 · Statements, input and output

### 05.1 · Recognise

**Solution**

```csharp
int lo = 1480, hi = 1520;
Console.WriteLine("rpm " + lo + hi);
Console.WriteLine("rpm " + (lo + hi));
Console.WriteLine(lo + hi + " rpm");
Console.WriteLine($"rpm {lo + hi}");
Console.WriteLine("deviations " + 2 + 3 + 4);
```

It reads left to right. While both sides are numbers the plus adds; the moment one of the two is text the plus glues, and everything that follows gets glued too.

**Output**

```text
rpm 14801520
rpm 3000
3000 rpm
rpm 3000
deviations 234
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The five predictions match the run | 5 |
| Explains the left-to-right rule | 3 |
| Points out that the third one adds first because the text sits at the end | 2 |

**Most common mistake**

They predict 3000 on the first line because the brackets are understood; it gives itself away because they predict the second line, which does carry them, exactly the same.

### 05.2 · Apply

**Solution**

```csharp
Console.Write("Station tag: ");
string tag = Console.ReadLine() ?? "";

Console.Write("Samples taken: ");
string sSamples = Console.ReadLine() ?? "";
bool okSamples = int.TryParse(sSamples, out int samples);

Console.Write("Reading in rpm: ");
string sReading = Console.ReadLine() ?? "";
bool okReading = double.TryParse(sReading, out double reading);

Console.WriteLine();
Console.WriteLine($"tag             {tag}");
Console.WriteLine($"samples read    {okSamples}  value {samples}");
Console.WriteLine($"reading read    {okReading}  value {reading:F3} rpm");
Console.WriteLine($"cycles in shift {148230:N0}");
```

**Output**

With the inputs `EST-07`, `12` and `1496.857142857143`:

```text
Station tag: Samples taken: Reading in rpm: 
tag             EST-07
samples read    True  value 12
reading read    True  value 1496.857 rpm
cycles in shift 148,230
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The three prompts use `Console.Write` and not `WriteLine` | 2 |
| Each line is stored in a variable before it is converted | 2 |
| Both conversions are `TryParse` and their `bool` gets printed | 3 |
| The reading comes out to three decimals and the cycles with a separator | 3 |

**Most common mistake**

They use `Convert.ToInt32` because it is shorter; it gives itself away because the program dies with `FormatException` the moment the marker types something that is not a number.

### 05.3 · Integrate

**Solution**

```csharp
using System.Globalization;

CultureInfo.CurrentCulture = new CultureInfo("es-MX");
bool okMx = double.TryParse("480.50", out double mx);
Console.WriteLine($"es-MX  TryParse -> {okMx}   value {mx}");
Console.WriteLine($"es-MX  {1496.857142:F2} rpm");
Console.WriteLine($"es-MX  {148230:N0} cycles");
Console.WriteLine($"es-MX  {0.0342:P1} out of band");

CultureInfo.CurrentCulture = new CultureInfo("de-DE");
bool okDe = double.TryParse("480.50", out double de);
Console.WriteLine($"de-DE  TryParse -> {okDe}   value {de}");
Console.WriteLine($"de-DE  {1496.857142:F2} rpm");
Console.WriteLine($"de-DE  {148230:N0} cycles");
Console.WriteLine($"de-DE  {0.0342:P1} out of band");

CultureInfo.CurrentCulture = new CultureInfo("es-MX");
double load = 480.50 / 1.10;
Console.WriteLine($"raw    {load}");
Console.WriteLine($"to F2  {load:F2} kN");
```

**Output**

```text
es-MX  TryParse -> True   value 480.5
es-MX  1496.86 rpm
es-MX  148,230 cycles
es-MX  3.4% out of band
de-DE  TryParse -> True   value 48050
de-DE  1496,86 rpm
de-DE  148.230 cycles
de-DE  3,4 % out of band
raw    436.81818181818176
to F2  436.82 kN
```

Under `de-DE` the dot is a thousands separator, so `480.50` reads as forty-eight thousand and fifty and the guard returns `True` all the same. Checking the `bool` only says the text could be converted, not that it was converted into what the operator meant. What is missing is pinning the culture of the conversion, with `CultureInfo.InvariantCulture` when the value comes off a file or a piece of equipment.

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| Both conversions are present, each with its culture pinned | 3 |
| The three format specifiers appear under both cultures | 3 |
| The safety factor prints raw and to two decimals | 2 |
| Explains why a `bool` of `True` guarantees nothing about the value | 2 |

**Most common mistake**

They leave the culture on `de-DE` at the end and report the load as 436,82 without noticing; it gives itself away because the same document claims the machine is configured in Mexican Spanish.

## Week 06 · Unit 4.4 · Selection structures

### 06.1 · Recognise

**Solution**

Without braces only the line that follows the `if` belongs to the decision. The second one runs every time, whatever the indentation promises.

```csharp
double coolantC = 26.8;

if (coolantC > 28.0)
    Console.WriteLine("alarm: coolant over limit");
    Console.WriteLine("bypass valve opened");

Console.WriteLine($"reading {coolantC} C logged");
```

**Output**

```text
bypass valve opened
reading 26.8 C logged
```

With `coolantC = 31.4` it prints the three lines. The failure it causes is the worse of the two: with the coolant at 26.8 degrees, which is cold, the bypass is left open and the gearbox runs with no coolant in the main circuit, and no alarm says a word about it.

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| Predicts two lines and names which ones | 4 |
| Predicts three lines with the reading of 31.4 | 2 |
| Explains that the braces mark the block, not the indentation | 2 |
| Names the physical failure the slip produces | 2 |

**Most common mistake**

They predict a single line, the logged reading; it gives itself away because their explanation says the `if` is false so both lines get skipped, which is exactly the reading the braces would have made true.

### 06.2 · Apply

**Solution**

```csharp
Console.Write("shaft rpm: ");
string line = Console.ReadLine() ?? "";
bool read = int.TryParse(line, out int rpm);

if (!read)
{
    Console.WriteLine("reading is not a number, channel discarded");
}
else if (rpm < 0)
{
    Console.WriteLine($"{rpm} rpm -> invalid, check the tachometer cable");
}
else if (rpm < 800)
{
    Console.WriteLine($"{rpm} rpm -> idle");
}
else if (rpm < 3000)
{
    Console.WriteLine($"{rpm} rpm -> nominal");
}
else
{
    Console.WriteLine($"{rpm} rpm -> overspeed, cut torque");
}
```

**Output**

```text
shaft rpm: 800 rpm -> nominal
shaft rpm: -5 rpm -> invalid, check the tachometer cable
shaft rpm: 799 rpm -> idle
shaft rpm: 3000 rpm -> overspeed, cut torque
shaft rpm: reading is not a number, channel discarded
```

The rung says strictly less than 800, so 799 still lands in idle and 800 already belongs to the band above. The value on the limit always belongs to the upper band when the comparison is strict.

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The `TryParse` guard is the first rung | 2 |
| The five cases are present and mutually exclusive | 3 |
| The five runs are pasted with their real output | 3 |
| Explains which band the value on the limit belongs to | 2 |

**Most common mistake**

They put the idle rung above the negative reading, and then a disconnected tachometer gets reported as a stopped shaft; it gives itself away because their run with `-5` says idle and builds without a single warning.

### 06.3 · Integrate

**Solution**

```csharp
const double LimitC = 28.0;

Console.Write("coolant temperature in C: ");
string sTemp = Console.ReadLine() ?? "";
bool okTemp = double.TryParse(sTemp, out double temp);

Console.Write("shaft rpm: ");
string sRpm = Console.ReadLine() ?? "";
bool okRpm = int.TryParse(sRpm, out int rpm);

bool hot = temp > LimitC;
bool onTheLimit = temp == LimitC;

if (!okTemp)
{
    Console.WriteLine("temperature is not a number, interlock held for missing data");
}
else if (!okRpm)
{
    Console.WriteLine("rpm is not a number, interlock held for missing data");
}
else if (hot)
{
    Console.WriteLine($"reading {temp:F1} C over {LimitC:F1} C");
    Console.WriteLine("bypass OPEN");
}
else
{
    Console.WriteLine($"reading {temp:F1} C at or under {LimitC:F1} C");
    Console.WriteLine("bypass closed");
}

Console.WriteLine($"hot {hot}  on the limit {onTheLimit}  rpm {rpm}");
```

**Output**

```text
coolant temperature in C: shaft rpm: reading 31.4 C over 28.0 C
bypass OPEN
hot True  on the limit False  rpm 1502

coolant temperature in C: shaft rpm: reading 28.0 C at or under 28.0 C
bypass closed
hot False  on the limit True  rpm 1502

coolant temperature in C: shaft rpm: temperature is not a number, interlock held for missing data
hot False  on the limit False  rpm 1502
```

With `>=` instead of `>`, the second set would have opened the bypass. The reading of 28.0 sits exactly on the line and the only thing that decides which side it falls on is the extra character in the operator.

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The limit is under `const` and both captures use `TryParse` | 3 |
| The ladder tests the guards before the bands | 2 |
| The last line runs down all four paths | 2 |
| The three runs are pasted | 2 |
| Explains the change `>=` produces on the reading of 28.0 | 1 |

**Most common mistake**

They tuck the last line inside the final `else`, and then the runs with an invalid capture print no `bool` values at all; it gives itself away because their third run has two lines and the others have three.

## Week 07 · Unit 4.4 · Selection in depth

### 07.1 · Recognise

**Solution**

```csharp
int sum = 0, count = 0;

if (count > 0 && sum / count > 1500)
    Console.WriteLine("mean is high");
Console.WriteLine("A: with && the empty window survives");

double c = -3.0;
string said = "(nothing)";
if (c > 0)
    if (c > 10)
        said = "over the limit";
    else
        said = "under the limit";
Console.WriteLine($"B: with c = {c} -> {said}");

double reading = 0.1 + 0.2;
Console.WriteLine($"C: 0.1 + 0.2 == 0.3 -> {reading == 0.3}");
Console.WriteLine($"D: |diff| < 1e-9     -> {Math.Abs(reading - 0.3) < 1e-9}");
```

**Output**

```text
A: with && the empty window survives
B: with c = -3 -> (nothing)
C: 0.1 + 0.2 == 0.3 -> False
D: |diff| < 1e-9     -> True
```

With a single `&` the short circuit disappears, both sides get evaluated and the division by zero kills the program with `DivideByZeroException` before anything is printed. The `else` of the second block bound itself to the inner `if`, the one on `c > 10`, and not to the outer one the indentation promises. That is why a reading of -3 degrees, which is the unplugged thermocouple, prints absolutely nothing about itself.

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The four predicted lines match | 4 |
| Says that with `&` the program dies and names the exception | 3 |
| Identifies which `if` the `else` bound itself to | 3 |

**Most common mistake**

They predict `under the limit` on line B, reading the indentation; it gives itself away because the same student then claims the `else` belongs to the outer `if`, which is the opposite of what the compiler does.

### 07.2 · Apply

**Solution**

```csharp
const double Nominal = 25.00;
const double Tolerance = 0.05;

Console.Write("measured dimension in mm: ");
bool okSize = double.TryParse(Console.ReadLine(), out double measured);

Console.Write("coolant temperature in C: ");
bool okTemp = double.TryParse(Console.ReadLine(), out double temp);

if (!okSize || !okTemp)
{
    Console.WriteLine("invalid entry, the part is not judged");
}
else
{
    double dev = Math.Abs(measured - Nominal);
    bool inside = dev <= Tolerance;

    string verdict = inside switch
    {
        true => "accept",
        false => "reject"
    };

    string band = temp switch
    {
        < 0.0 => "thermocouple unplugged",
        < 20.0 => "cold",
        <= 28.0 => "nominal",
        < 90.0 => "hot, bypass open",
        _ => "shutdown on overtemperature"
    };

    Console.WriteLine($"size    {measured:F2} mm   deviation {dev:F4} mm");
    Console.WriteLine($"size    {verdict}");
    Console.WriteLine($"coolant {temp:F1} C -> {band}");
}
```

**Output**

```text
measured dimension in mm: coolant temperature in C: size    25.06 mm   deviation 0.0600 mm
size    reject
coolant 31.4 C -> hot, bypass open

measured dimension in mm: coolant temperature in C: size    24.97 mm   deviation 0.0300 mm
size    accept
coolant 28.0 C -> nominal

measured dimension in mm: coolant temperature in C: size    25.00 mm   deviation 0.0000 mm
size    accept
coolant -3.0 C -> thermocouple unplugged

measured dimension in mm: coolant temperature in C: invalid entry, the part is not judged
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The capture guard goes first and cuts off the rest of the calculation | 2 |
| Tolerance is decided with `Math.Abs` against a declared margin | 3 |
| The `switch` expression has its arms in order and its discard | 3 |
| The four runs are pasted, the bad capture included | 2 |

**Most common mistake**

They order the arms with `< 90.0` above `< 20.0`; it gives itself away because the compiler answers `CS8510: The pattern is unreachable` and the file they hand in does not build.

### 07.3 · Integrate

**Solution**

```csharp
Console.Write("pressure in bar: ");
bool okP = double.TryParse(Console.ReadLine(), out double pressure);

Console.Write("guard door closed (1 = yes, 0 = no): ");
bool okD = int.TryParse(Console.ReadLine(), out int doorNum);

Console.Write("mode (0 stop, 1 automatic, 2 jog): ");
bool okM = int.TryParse(Console.ReadLine(), out int mode);

if (!okP || !okD || !okM)
{
    Console.WriteLine("invalid entry, the machine stays interlocked");
}
else
{
    bool door = doorNum == 1;
    bool pressureOk = pressure >= 3.5 && pressure <= 5.0;
    bool start = pressureOk && door && mode == 1;

    string modeName = mode switch
    {
        0 => "stop",
        1 => "automatic",
        2 => "jog",
        _ => "unknown mode"
    };

    Console.WriteLine($"pressure {pressure:F2} bar in range -> {pressureOk}");
    Console.WriteLine($"guard door closed             -> {door}");
    Console.WriteLine($"mode {mode}                        -> {modeName}");
    Console.WriteLine($"start                         -> {start}");

    if (!start)
    {
        if (!pressureOk)
        {
            Console.WriteLine("cause: pressure outside 3.5 to 5.0 bar");
        }
        else if (!door)
        {
            Console.WriteLine("cause: guard door open");
        }
        else
        {
            Console.WriteLine("cause: the machine is not in automatic");
        }
    }
}
```

**Output**

The four runs, in the order `4.2 1 1`, `4.2 0 1`, `0.5 1 1` and `4.2 1 2`. The three prompts
come out with `Console.Write`, so the first line of every run carries them glued together:

```text
pressure in bar: guard door closed (1 = yes, 0 = no): mode (0 stop, 1 automatic, 2 jog): pressure 4.20 bar in range -> True
guard door closed             -> True
mode 1                        -> automatic
start                         -> True

pressure in bar: guard door closed (1 = yes, 0 = no): mode (0 stop, 1 automatic, 2 jog): pressure 4.20 bar in range -> True
guard door closed             -> False
mode 1                        -> automatic
start                         -> False
cause: guard door open

pressure in bar: guard door closed (1 = yes, 0 = no): mode (0 stop, 1 automatic, 2 jog): pressure 0.50 bar in range -> False
guard door closed             -> True
mode 1                        -> automatic
start                         -> False
cause: pressure outside 3.5 to 5.0 bar

pressure in bar: guard door closed (1 = yes, 0 = no): mode (0 stop, 1 automatic, 2 jog): pressure 4.20 bar in range -> True
guard door closed             -> True
mode 2                        -> jog
start                         -> False
cause: the machine is not in automatic
```

The `&&` demands all three conditions, so one interlock failing is enough to leave the start at `False`. With `||` in its place, the row `4.2 0 1` would start the machine with the guard door open, for no reason other than the pressure being right.

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The three captures are read with `TryParse` and there is a guard | 2 |
| `pressureOk` is two comparisons joined and `start` is the three | 3 |
| The nested ladder carries braces and names the first cause | 2 |
| The four rows of the truth table were run | 2 |
| Explains what would start up with `||` | 1 |

**Most common mistake**

They write `pressure >= 3.5 || pressure <= 5.0`, which is true for any pressure at all; it gives itself away because their `0.5` row reports the pressure as in range.

## Week 08 · Unit 4.5 · Repetition · First midterm

### 08.1 · Recognise

**Solution**

```csharp
int[] torque = { 22, 24, 25, 19, 24, 31, 23 };

int i = 0, inspected = 0, skipped = 0, sum = 0, cut = -1;

while (i < torque.Length)
{
    inspected++;
    if (torque[i] > 30) { cut = i; break; }
    if (torque[i] < 20) { skipped++; i++; continue; }
    sum += torque[i];
    i++;
}
```

The line that makes the condition false is `i++`, and it appears twice: at the end of the body and also inside the `continue` branch. Delete the one in the `continue` and the 19 N·m bolt gets inspected forever, with the terminal running until you cut it off.

**Output**

```text
bolts inspected      6
skipped as loose     1
sum within tolerance 95
index of the cut     5
never inspected      1
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The five numbers match the run | 5 |
| Points at `i++` as the fourth beat | 2 |
| Explains that there are two `i++` and why the one in the `continue` is compulsory | 3 |

**Most common mistake**

They answer 7 for bolts inspected because the array holds seven; it gives itself away because their last line also says 0 for the ones never inspected, and the two counts cannot both be true with a `break` in between.

### 08.2 · Apply

**Solution**

```csharp
int attempts = 0;
double temp;
bool ok;

do
{
    attempts++;
    Console.Write("coolant temperature in C (10 to 95): ");
    string line = Console.ReadLine() ?? "";
    bool read = double.TryParse(line, out temp);
    ok = read && temp >= 10.0 && temp <= 95.0;
    if (!ok)
    {
        Console.WriteLine($"  rejected '{line}'");
    }
} while (!ok && attempts < 4);

if (ok)
{
    Console.WriteLine($"accepted {temp:F1} C after {attempts} attempts");
}
else
{
    Console.WriteLine("INTERLOCKED: four invalid entries, manual reset");
}
```

**Output**

```text
coolant temperature in C (10 to 95):   rejected 'abc'
coolant temperature in C (10 to 95):   rejected '120'
coolant temperature in C (10 to 95):   rejected '-5'
coolant temperature in C (10 to 95): accepted 31.4 C after 4 attempts

coolant temperature in C (10 to 95):   rejected 'a'
coolant temperature in C (10 to 95):   rejected 'b'
coolant temperature in C (10 to 95):   rejected 'c'
coolant temperature in C (10 to 95):   rejected 'd'
INTERLOCKED: four invalid entries, manual reset
```

It is a `do-while` because the sample has to be asked for before it can be judged. With `while` you would have to test a variable nobody has filled yet, and that forces you to invent a fake starting value nobody later remembers the reason for. The body has to run at least once, and that is exactly the guarantee `do-while` gives and `while` does not.

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| It is a `do-while` and the loop depends on `ok` | 3 |
| The two guards go in order: format first, range after | 2 |
| The rejection message shows in quotes what was typed | 2 |
| The cap of four attempts cuts out and interlocks | 2 |
| The paragraph justifies `do-while` through the minimum pass | 1 |

**Most common mistake**

The final `while` tests `attempts < 4` and forgets `ok`, so the program asks for four temperatures even when the first one is good; it gives itself away because their good run has four prompts and a single acceptance line at the end.

### 08.3 · Integrate

**Solution**

```csharp
const int Minimum = 1480;
const int Maximum = 1520;

int attempts = 0, rpm;
bool ok;
do
{
    attempts++;
    Console.Write($"closing sample in rpm ({Minimum}-{Maximum}): ");
    string line = Console.ReadLine() ?? "";
    bool read = int.TryParse(line, out rpm);
    ok = read && rpm >= Minimum && rpm <= Maximum;
    if (!ok) Console.WriteLine($"  rejected '{line}'");
} while (!ok && attempts < 3);

if (!ok)
{
    Console.WriteLine("INTERLOCKED: three invalid entries");
}
else
{
    Console.WriteLine($"accepted {rpm} rpm after {attempts} attempts");

    if (rpm < 1490) Console.WriteLine("low band");
    else if (rpm < 1510) Console.WriteLine("middle band");
    else Console.WriteLine("high band");

    bool door = true, estop = true;
    bool armed = door && estop && rpm >= Minimum;
    Console.WriteLine($"armed -> {armed}");

    int[] run = { 1480, 1502, 1495, 1533, 1471, 1509, 1488 };
    int i = 0, sum = 0, outside = 0;
    while (i < run.Length)
    {
        sum += run[i];
        if (run[i] < Minimum || run[i] > Maximum) outside++;
        i++;
    }

    Console.WriteLine($"sum         {sum}");
    Console.WriteLine($"mean int    {sum / run.Length}");
    Console.WriteLine($"mean real   {(double)sum / run.Length:F3}");
    Console.WriteLine($"out of band {outside} of {run.Length}");
}
```

**Output**

```text
closing sample in rpm (1480-1520):   rejected 'abc'
closing sample in rpm (1480-1520): accepted 1502 rpm after 2 attempts
middle band
armed -> True
sum         10478
mean int    1496
mean real   1496.857
out of band 2 of 7
```

The integer mean divides two integers and throws the remainder away. The real mean casts the sum to `double` before dividing, so the remainder survives. Over these seven readings the difference is 0.857 rpm, which on a tachometer sounds like nothing and on a trend report accumulated over a month does not.

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The limits under `const` and the capture defended with a cap | 2 |
| The ladder classifies into three mutually exclusive bands | 2 |
| The interlock joins three conditions with `&&` | 2 |
| The `while` accumulates the sum and counts out of band under the written rule | 2 |
| Explains the difference between integer mean and real mean | 2 |

**Most common mistake**

They declare `sum` inside the `while` and the total ends up being the last reading; it gives itself away because their sum prints 1488 and their mean prints 212.

## Week 09 · Unit 4.5 · Repetition in depth

### 09.1 · Recognise

**Solution**

```csharp
int outer = 0, inner = 0, pairs = 0;

for (int a = 0; a < 4; a++)
{
    outer++;
    for (int b = a + 1; b < 4; b++)
    {
        inner++;
        if (b == 3) break;
        pairs++;
    }
}
```

The `break` leaves the inner loop and nothing else. The outer one takes its four full turns, which is why the outer count is 4 even though three of those turns end cut short from the inside.

**Output**

```text
outer passes 4
inner passes 6
pairs counted 3
```

After the loop, `Console.WriteLine(a);` does not compile: `error CS0103: The name 'a' does not exist in the current context`. The control variable is born and dies in the header of the `for`.

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The three numbers match the run | 5 |
| Says the `break` ends the inner loop | 2 |
| Quotes `CS0103` for the use of `a` outside the loop | 3 |

**Most common mistake**

They answer 12 for inner passes, multiplying 4 by 3; it gives itself away because their count ignores that the inner loop starts at `a + 1` and that the `break` cuts it.

### 09.2 · Apply

**Solution**

```csharp
int[] rpm = { 1480, 1502, 1495, 1533, 1471, 1509, 1488 };

int sum = 0, outside = 0;
int maxIdx = 0, minIdx = 0;

for (int i = 0; i < rpm.Length; i++)
{
    sum += rpm[i];
    if (rpm[i] < 1480 || rpm[i] > 1520) outside++;
    if (rpm[i] > rpm[maxIdx]) maxIdx = i;
    if (rpm[i] < rpm[minIdx]) minIdx = i;
}

int count = 0;
int sumForeach = 0;
foreach (int reading in rpm)
{
    sumForeach += reading;
    count++;
}

Console.WriteLine($"readings    {count}");
Console.WriteLine($"sum         {sum}  (foreach {sumForeach})");
Console.WriteLine($"mean int    {sum / rpm.Length}");
Console.WriteLine($"mean real   {(double)sum / rpm.Length}");
Console.WriteLine($"mean to F3  {(double)sum / rpm.Length:F3}");
Console.WriteLine($"out of band {outside} of {rpm.Length}");
Console.WriteLine($"maximum     {rpm[maxIdx]} at index {maxIdx}");
Console.WriteLine($"minimum     {rpm[minIdx]} at index {minIdx}");
Console.WriteLine($"range       {rpm[maxIdx] - rpm[minIdx]}");
```

**Output**

```text
readings    7
sum         10478  (foreach 10478)
mean int    1496
mean real   1496.857142857143
mean to F3  1496.857
out of band 2 of 7
maximum     1533 at index 3
minimum     1471 at index 4
range       62
```

The indices of the maximum and the minimum cannot be carried with `foreach`, because that loop hands over the value and not the position. The moment the question moves from what the maximum is to where the maximum is, you go back to the `for`. And the index is exactly what tells the technician which sample to go and check.

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The four accumulators are declared before the loop | 3 |
| A single `for` fills them all | 2 |
| The `foreach` reproduces sum and count | 2 |
| The nine lines come out with the measured values | 2 |
| Identifies the accumulator that demands an index and explains it | 1 |

**Most common mistake**

They start `minIdx` at the index of the last element so that it begins large; it gives itself away because their minimum prints 1488 instead of 1471 and their range comes out at 45.

### 09.3 · Integrate

**Solution**

```csharp
int[] rpm = { 1480, 1502, 1495, 1533, 1471, 1509, 1488 };

int outside = 0;
for (int i = 0; i < rpm.Length; i++)
    if (rpm[i] < 1480 || rpm[i] > 1520) outside++;

Console.WriteLine($"out of band      {outside} of {rpm.Length}");
Console.WriteLine($"pct integer      {outside * 100 / rpm.Length}");
Console.WriteLine($"pct real         {outside * 100.0 / rpm.Length}");
Console.WriteLine($"pct to F1        {outside * 100.0 / rpm.Length:F1}");

int full = 0, triangular = 0;
for (int a = 0; a < rpm.Length; a++)
{
    for (int b = 0; b < rpm.Length; b++) full++;
    for (int b = a + 1; b < rpm.Length; b++) triangular++;
}
Console.WriteLine($"full mesh        {full}");
Console.WriteLine($"distinct pairs   {triangular}");

int cycles = int.MaxValue - 2;
for (int k = 0; k < 3; k++)
{
    cycles++;
    Console.WriteLine($"+1 cycle in int  {cycles}");
}
long cyclesL = int.MaxValue - 2;
for (int k = 0; k < 3; k++) cyclesL++;
Console.WriteLine($"the same in long {cyclesL}");
Console.WriteLine($"at 25 cycles/s   {int.MaxValue / 25.0 / 3600.0 / 24.0:F1} days");
```

**Output**

```text
out of band      2 of 7
pct integer      28
pct real         28.571428571428573
pct to F1        28.6
full mesh        49
distinct pairs   21
+1 cycle in int  2147483646
+1 cycle in int  2147483647
+1 cycle in int  -2147483648
the same in long 2147483648
at 25 cycles/s   994.2 days
```

The maintenance lead gets 28.6, because the 28 ate half a point without saying so and nobody is going to read the seventeen-digit number. The morning the counter wrapped around, the system reported minus two thousand one hundred and forty-seven million cycles, a number that sounds to nobody like a type error and does look like a broken sensor. It is caught without changing the type by comparing the new value against the previous one: if the counter went down when nobody reset it, it wrapped.

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The four percentages are present and one is chosen for the report | 3 |
| The two pair counts are present and do not agree | 2 |
| The `int` counter is seen going negative, and the `long` is not | 3 |
| The days of continuous running come out to one decimal | 1 |
| Gives a way of catching the wrap without changing the type | 1 |

**Most common mistake**

They expect an exception on the overflow; it gives itself away because their report says it dies here and the run they paste keeps printing lines after the negative number.

## Week 10 · Unit 5.1 · User-defined functions

### 10.1 · Recognise

**Solution**

| File | Compiles | What it answers | What it prints |
|---|---|---|---|
| A | yes | `warning CS8321: The local function 'PrintHeader' is declared but never used` | nothing |
| B | no | `error CS0029: Cannot implicitly convert type 'void' to 'double'` | nothing |
| C | no | `error CS8421: A static local function cannot contain a reference to 'limitC'` | nothing |

File A compiles, runs and exits with 0 without printing a single line, because declaring a method does not execute it. The compiler flags it with `CS8321`, which is a warning and not an error.

In file C the word to remove is `static`. Take it away and the method can read `limitC` and the file compiles, but the isolation is gone: the piece can no longer be tested on its own, because its result depends on a variable the caller never handed it.

**Output**

```text
A  Build succeeded with 1 warning, dotnet run prints nothing, exit 0
B  Program.cs(1,12): error CS0029: Cannot implicitly convert type 'void' to 'double'
C  Program.cs(6,22): error CS8421: A static local function cannot contain a reference to 'limitC'.
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The three outcomes are classified correctly | 4 |
| Quotes `CS8321` and explains that A prints nothing | 2 |
| Quotes `CS0029` and tells returning apart from printing | 2 |
| Says what is lost by removing `static` in C | 2 |

**Most common mistake**

They say A does not compile because it is never called; it gives itself away because they never paste the `Build succeeded` their own machine printed.

### 10.2 · Apply

**Solution**

```csharp
int[] rpm = { 1480, 1502, 1495, 1533, 1471, 1509, 1488 };

Console.WriteLine($"sum         {Sum(rpm)}");
Console.WriteLine($"mean        {Mean(rpm):F3}");
Console.WriteLine($"out of band {OutOfBand(rpm, 1480, 1520)} of {rpm.Length}");
int idx = IndexOfMax(rpm);
Console.WriteLine($"maximum     {rpm[idx]} at index {idx}");

static int Sum(int[] v)
{
    int total = 0;
    foreach (int x in v) total += x;
    return total;
}

static double Mean(int[] v)
{
    return (double)Sum(v) / v.Length;
}

static int OutOfBand(int[] v, int lo, int hi)
{
    int count = 0;
    foreach (int x in v)
        if (x < lo || x > hi) count++;
    return count;
}

static int IndexOfMax(int[] v)
{
    int idx = 0;
    for (int i = 1; i < v.Length; i++)
        if (v[i] > v[idx]) idx = i;
    return idx;
}
```

**Output**

```text
sum         10478
mean        1496.857
out of band 2 of 7
maximum     1533 at index 3
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The four methods exist, with `static` and their full signature | 3 |
| None of them prints on its own, all of them return | 3 |
| `Mean` leans on `Sum` and casts before dividing | 2 |
| The limits arrive as parameters, not typed inside | 2 |

**Most common mistake**

`Mean` returns `int` and the result comes out at 1496; it gives itself away because the `:F3` of the print shows 1496.000, which is an average with no remainder over seven numbers that do not divide evenly.

### 10.3 · Integrate

**Solution**

```csharp
int[] rpm = { 1480, 1502, 1495, 1533, 1471, 1509, 1488 };

Zero(rpm);
Console.WriteLine($"after Zero        rpm[0] = {rpm[0]}");

Replace(rpm);
Console.WriteLine($"after Replace     rpm[0] = {rpm[0]}");

ReplaceRef(ref rpm);
Console.WriteLine($"after ReplaceRef  rpm[0] = {rpm[0]}");

int[] original = { 1480, 1502, 1495, 1533, 1471, 1509, 1488 };
int[] window = Window(original, 2, 3);
window[0] = 0;
Console.WriteLine($"window cut out    {window[0]} {window[1]} {window[2]}");
Console.WriteLine($"original untouched original[2] = {original[2]}");

Console.WriteLine($"mean of 2         {Mean(1480, 1502):F3}");
Console.WriteLine($"mean of 7         {Mean(original):F3}");
Console.WriteLine($"mean of none      {Mean()}");

static void Zero(int[] v) { v[0] = 0; }

static void Replace(int[] v) { v = new int[] { -1, -1, -1 }; }

static void ReplaceRef(ref int[] v) { v = new int[] { -1, -1, -1 }; }

static int[] Window(int[] v, int start, int count)
{
    int[] w = new int[count];
    for (int i = 0; i < count; i++) w[i] = v[start + i];
    return w;
}

static double Mean(params int[] samples)
{
    if (samples.Length == 0) return double.NaN;
    int total = 0;
    foreach (int m in samples) total += m;
    return (double)total / samples.Length;
}
```

**Output**

```text
after Zero        rpm[0] = 0
after Replace     rpm[0] = 0
after ReplaceRef  rpm[0] = -1
window cut out    0 1533 1471
original untouched original[2] = 1495
mean of 2         1491.000
mean of 7         1496.857
mean of none      NaN
```

Point 1 reaches the caller because the parameter variable is a copy of the reference, and that copy points at the same array. Point 2 does not reach it because assigning a new array changes the copy of the reference, not the caller's. The word that changes the ending of point 3 is `ref`, which hands over the variable itself rather than a copy of it.

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The first three methods exist and the difference is visible | 3 |
| `Window` returns a new array and the original is left alone | 2 |
| `Mean` with `params` handles two, seven and no samples | 2 |
| Returns `NaN` with zero samples instead of dying | 1 |
| The three explanation lines tell element apart from replacement | 2 |

**Most common mistake**

They write `Window` copying the reference instead of building a new array, and then writing into the window changes the original; it gives itself away because their untouched-original line prints 0 instead of 1495.

## Week 11 · Unit 5.3 · Passing parameters by reference

### 11.1 · Recognise

**Solution**

The two bodies are identical and both do the right thing. What changes is what they work on: the first on copies that get destroyed on the way out, the second on the caller's variables.

**Output**

```text
by value      1, 2
by reference  2, 1
TryParse      False, stored = 0
```

Drop the two `ref` keywords from the call site and leave the signature as it is, and the compiler answers `error CS1620: Argument 1 must be passed with the 'ref' keyword` plus another just like it for argument 2. The word goes on both sides or on neither.

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The three predicted lines match | 5 |
| Explains that the body of the first one is written correctly | 2 |
| Quotes `CS1620` for the call without the keyword | 3 |

**Most common mistake**

They predict `stored = 999` because if it failed it left it alone; it gives itself away because the same student writes that `TryParse` returns `False`, and that failure is exactly when it overwrites the variable with 0.

### 11.2 · Apply

**Solution**

```csharp
double[] thermocouples = { 21.0, 39.5, 22.4 };

MinMax(thermocouples, out double cold, out double hot);
Console.WriteLine($"minimum {cold:F1} C   maximum {hot:F1} C");

double tank = 40.0;

Fill(ref tank, 15.0);
Console.WriteLine($"tank {tank:F1} L");

Fill(ref tank, 10.0);
Console.WriteLine($"tank {tank:F1} L");

Drain(ref tank, 20.0);
Console.WriteLine($"tank {tank:F1} L");

Drain(ref tank, 40.0);
Console.WriteLine($"tank {tank:F1} L");

static void MinMax(double[] v, out double lo, out double hi)
{
    lo = v[0];
    hi = v[0];
    foreach (double x in v)
    {
        if (x < lo) lo = x;
        if (x > hi) hi = x;
    }
}

static void Fill(ref double litres, double added)
{
    if (litres + added > 60.0)
    {
        Console.WriteLine($"  rejected: {litres + added:F1} L is over the 60.0 L cap");
        return;
    }
    litres += added;
}

static void Drain(ref double litres, double removed)
{
    if (litres - removed < 5.0)
    {
        Console.WriteLine($"  rejected: would leave {litres - removed:F1} L and the floor is 5.0 L");
        return;
    }
    litres -= removed;
}
```

**Output**

```text
minimum 21.0 C   maximum 39.5 C
tank 55.0 L
  rejected: 65.0 L is over the 60.0 L cap
tank 55.0 L
tank 35.0 L
  rejected: would leave -5.0 L and the floor is 5.0 L
tank 35.0 L
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| Both `out` parameters are filled down every path of `MinMax` | 3 |
| `Fill` and `Drain` take the level by `ref` | 2 |
| Both guards reject and the message states the number that would have been left | 3 |
| The four chained operations were run | 2 |

**Most common mistake**

`Drain` subtracts first and checks afterwards, and the tank is left at minus five litres; it gives itself away because the rejection message appears and the level on the next line has already gone down.

### 11.3 · Integrate

**Solution**

```csharp
double[] bench = { 21.0, 39.5, 22.4 };
double[] alias = bench;

alias[0] = 99.9;
Console.WriteLine($"bench[0] after touching the alias  {bench[0]}");
Console.WriteLine($"same array                         {ReferenceEquals(bench, alias)}");

bench[0] = 21.0;

int attempts = 0;
double offset;
bool ok;
do
{
    attempts++;
    Console.Write("calibration offset in C (-5 to 5): ");
    string line = Console.ReadLine() ?? "";
    bool read = double.TryParse(line, out offset);
    ok = read && offset >= -5.0 && offset <= 5.0;
    if (!ok) Console.WriteLine($"  rejected '{line}'");
} while (!ok && attempts < 3);

if (!ok)
{
    Console.WriteLine("calibration cancelled, the bench is left untouched");
}
else
{
    Apply(ref bench[1], offset);
    Clip(ref bench[1], 30.0);

    MinMax(bench, out double cold, out double hot);

    Console.WriteLine($"channel 1 after calibration  {bench[1]:F1} C");
    Console.WriteLine($"minimum {cold:F1} C   maximum {hot:F1} C");
}

static void Apply(ref double reading, double offset)
{
    reading += offset;
}

static void Clip(ref double reading, double limit)
{
    if (reading > limit)
    {
        Console.WriteLine($"  clipped from {reading:F1} to {limit:F1} C");
        reading = limit;
    }
}

static void MinMax(double[] v, out double lo, out double hi)
{
    lo = v[0];
    hi = v[0];
    foreach (double x in v)
    {
        if (x < lo) lo = x;
        if (x > hi) hi = x;
    }
}
```

**Output**

With the inputs `abc` and `-2.5`:

```text
bench[0] after touching the alias  99.9
same array                         True
calibration offset in C (-5 to 5):   rejected 'abc'
calibration offset in C (-5 to 5):   clipped from 37.0 to 30.0 C
channel 1 after calibration  30.0 C
minimum 21.0 C   maximum 30.0 C
```

The array of point 1 is shared because the variable does not carry the three numbers, it carries a reference to them, and assigning it copies the reference. Point 3 does need `ref` because `bench[1]` is a `double`, a loose value, and without the word the method would receive a copy of the number and the calibration would stay inside.

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The alias is demonstrated with `ReferenceEquals` | 2 |
| The `do-while` validates the offset and leaves the bench alone on failure | 3 |
| `Apply` and `Clip` take the array element by `ref` | 3 |
| `MinMax` reports with two `out` parameters after calibrating | 1 |
| Explains why one shares without the keyword and the other needs it | 1 |

**Most common mistake**

They pass `bench[1]` without `ref` and the calibration never shows up; it gives itself away because their final line prints 39.5 and the clip message never comes out.

## Week 12 · Unit 5.4 · Predefined functions

### 12.1 · Recognise

**Solution**

`NaN` is the only value in the language that is not equal to itself, which is why the double equals answers `False` and the only way to ask the question is `double.IsNaN`. The sine of pi does not give zero because `Math.PI` is an approximation of pi to seventeen digits, and the sine of that approximate number is a very small number, not zero.

**Output**

```text
Program.cs(4,45): warning CS1718: Comparison made to same variable; did you mean to compare something else?

Math.Sqrt(-1)          NaN
nan == nan             False
double.IsNaN(nan)      True
Math.Sin(Math.PI)      1.2246467991473532E-16
|sin(pi)| < 1e-9       True
Math.Round(2.5)        2
Round(2.5) away from 0 3
1.0 / 0                ∞
Math.Clamp(39.5,0,30)  30
Math.Pow(2, 10)        1024
```

The warning comes out of line 4, the one that compares `nan` against itself. `int capacity = Math.Pow(2, 10);` returns `error CS0266: Cannot implicitly convert type 'double' to 'int'`, because the signature of `Math.Pow` promises a `double` even when the result looks like a whole number. `Math.Sqrt("9")` returns `error CS1503: Argument 1: cannot convert from 'string' to 'double'`.

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The ten predicted lines match | 4 |
| Places the `CS1718` warning on the right line | 2 |
| Explains why `nan == nan` is `False` | 2 |
| Quotes `CS0266` for `Math.Pow` and `CS1503` for `Math.Sqrt` with text | 2 |

**Most common mistake**

They predict 0 for the sine of pi; it gives itself away because on the next line they accept that the tolerance comparison answers `True`, and both cannot be true at once if the value were exactly zero.

### 12.2 · Apply

**Solution**

```csharp
double[] v = { 0.42, -0.31, 0.55, -0.48, 0.12, -0.27, 0.61 };

double sumOfSquares = 0;
double peak = 0;
foreach (double x in v)
{
    sumOfSquares += Math.Pow(x, 2);
    peak = Math.Max(peak, Math.Abs(x));
}

double rms = Math.Sqrt(sumOfSquares / v.Length);
double crest = peak / rms;
double clipped = Math.Clamp(rms, 0.0, 0.4500);

Console.WriteLine($"raw RMS        {rms}");
Console.WriteLine($"RMS to F4      {rms:F4} mm/s");
Console.WriteLine($"peak           {peak:F4} mm/s");
Console.WriteLine($"crest factor   {crest:F4}");
Console.WriteLine($"clipped RMS    {clipped:F4} mm/s");
Console.WriteLine($"over 0.4500    {rms > 0.4500}");
```

**Output**

```text
raw RMS        0.42507142257003616
RMS to F4      0.4251 mm/s
peak           0.6100 mm/s
crest factor   1.4351
clipped RMS    0.4251 mm/s
over 0.4500    False
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The sum of squares and the root are chained correctly | 3 |
| The peak uses `Math.Abs` and `Math.Max`, not a hand-written `if` | 2 |
| The clipping uses `Math.Clamp` with its three arguments | 2 |
| The RMS prints raw and to four decimals | 2 |
| The crest factor comes out of the peak over the RMS | 1 |

**Most common mistake**

They sum the absolute values instead of the squares and call the result RMS; it gives itself away because their number lands at 0.3943 and their crest factor comes out below 1, which is impossible.

### 12.3 · Integrate

**Solution**

```csharp
const int Seed = 2026;

Random r = new Random(Seed);

int[] sim = new int[20];
for (int i = 0; i < sim.Length; i++)
    sim[i] = r.Next(1400, 1601);

int sum = 0, outside = 0, maxIdx = 0;
for (int i = 0; i < sim.Length; i++)
{
    sum += sim[i];
    if (sim[i] < 1480 || sim[i] > 1520) outside++;
    if (sim[i] > sim[maxIdx]) maxIdx = i;
}

Console.WriteLine($"seed         {Seed}");
Console.WriteLine($"first five   {sim[0]} {sim[1]} {sim[2]} {sim[3]} {sim[4]}");
Console.WriteLine($"sum          {sum}");
Console.WriteLine($"mean         {(double)sum / sim.Length:F3} rpm");
Console.WriteLine($"out of band  {outside} of {sim.Length}");
Console.WriteLine($"peak         {sim[maxIdx]} rpm at index {maxIdx}");

int word = 0;
if (outside > 0) word += 1;
if (sim[maxIdx] > 1520) word += 2;
if (sum / sim.Length > 1500) word += 4;

Console.WriteLine($"status word  {word} = {Convert.ToString(word, 2)} in binary");
Console.WriteLine($"in hex       {Convert.ToString(word, 16)}");
```

**Output**

The two consecutive runs give exactly the same thing:

```text
seed         2026
first five   1432 1456 1584 1599 1584
sum          30052
mean         1502.600 rpm
out of band  16 of 20
peak         1599 rpm at index 3
status word  7 = 111 in binary
in hex       7
```

With the generator built inside the loop, the twenty samples would be the same number repeated twenty times. A seed is the starting point of a sequence, so reseeding on every pass reads its first value again.

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The seed is under `const` and appears in the output | 2 |
| The generator is built once, outside the loop | 3 |
| The accumulators reproduce sum, mean, out of band and peak | 2 |
| The status word comes out in decimal, binary and hexadecimal | 2 |
| The two pasted runs are identical | 1 |

**Most common mistake**

They write `new Random(Seed)` inside the `for`; it gives itself away because their twenty samples are the same number and their out-of-band count is 0 or 20, never anything in between.

## Week 13 · Unit 6.1 · Arrays and strings · Second midterm

### 13.1 · Recognise

**Solution**

Assigning an array creates a second name for the same array. `Clone` does produce an independent one. A string cannot be edited, so `ToUpper` and `Trim` return another string and leave yours where it was.

**Output**

```text
src[0] 99   src[1] 1502
alias is the same True
copy is the same  False
tag        sensor-07
ToUpper()  SENSOR-07
tag.Length 9
empty inside True
fields of the empty 1
Substring(9) []
```

`tag.Substring(10)` throws `ArgumentOutOfRangeException`, while `tag.Substring(9)` over a string of length 9 returns the empty string without complaining. `tag[9]` throws `IndexOutOfRangeException` with the message `Index was outside the bounds of the array`. Two calls into the same library, two different boundaries.

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The nine predicted lines match | 4 |
| Tells alias apart from copy with the two `ReferenceEquals` | 2 |
| Explains that `tag.ToUpper();` on its own line does nothing | 2 |
| Reports both boundary exceptions and the difference | 2 |

**Most common mistake**

They predict `SENSOR-07` on the `tag` line; it gives itself away because they write the line `tag.ToUpper();` as if it stored the result somewhere.

### 13.2 · Apply

**Solution**

```csharp
using System.Globalization;

string line = "  EST-07:1480.0,1502.5,1495.0,1533.5  ";

string[] parts = line.Trim().Split(':');
string tag = parts[0];
string[] fields = parts[1].Split(',');

double[] readings = new double[fields.Length];
for (int i = 0; i < fields.Length; i++)
    readings[i] = double.Parse(fields[i], CultureInfo.InvariantCulture);

double sum = 0;
foreach (double x in readings) sum += x;

Console.WriteLine($"tag        {tag}");
Console.WriteLine($"fields     {fields.Length}");
Console.WriteLine($"mean       {sum / readings.Length:F3} rpm");
Console.WriteLine($"first      {readings[0]:F1}   last {readings[readings.Length - 1]:F1}");

string[] tests = { "SNS-4471-A", "  SNS-4471-A  ", "sns-4471-b", "SNS-44X1-A", "" };
foreach (string p in tests)
    Console.WriteLine($"[{p}] -> {IdValid(p)}");

static bool IdValid(string raw)
{
    string id = raw.Trim();
    if (id.Length != 10) return false;

    StringComparison ci = StringComparison.OrdinalIgnoreCase;
    if (!id.StartsWith("SNS-", ci)) return false;
    if (!id.EndsWith("-A", ci) && !id.EndsWith("-B", ci)) return false;

    for (int i = 4; i < 8; i++)
        if (!char.IsDigit(id[i])) return false;

    return true;
}
```

**Output**

```text
tag        EST-07
fields     4
mean       1502.750 rpm
first      1480.0   last 1533.5
[SNS-4471-A] -> True
[  SNS-4471-A  ] -> True
[sns-4471-b] -> True
[SNS-44X1-A] -> False
[] -> False
```

The third input is what separates a validator with one policy from one with two. If the suffix is compared without `OrdinalIgnoreCase` and the prefix is, `sns-4471-b` returns `False` and the defect lives two lines away from its own contradiction.

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| `Trim` before `Split`, and the two cuts in the right order | 2 |
| The culture is pinned in the conversion, not left to the machine | 3 |
| The validator checks length, prefix, suffix and digits | 3 |
| A single comparison policy across both text checks | 2 |

**Most common mistake**

They convert with `double.Parse` and no culture and the file runs fine in the classroom; it gives itself away when the marker runs it on a machine configured in German and the mean jumps to six figures.

### 13.3 · Integrate

**Solution**

```csharp
string capture = "1480,1502,1495,abc,1533,1471,1509,1488";

string[] fields = capture.Split(',');
int[] rpm = new int[fields.Length];
int n = 0, rejected = 0;

foreach (string field in fields)
{
    bool ok = int.TryParse(field.Trim(), out int value);
    if (ok) { rpm[n] = value; n++; }
    else { rejected++; }
}

int[] valid = new int[n];
for (int i = 0; i < n; i++) valid[i] = rpm[i];

Console.WriteLine($"fields      {fields.Length}");
Console.WriteLine($"read        {n}");
Console.WriteLine($"rejected    {rejected}");
Console.WriteLine($"sum         {Sum(valid)}");
Console.WriteLine($"mean int    {Sum(valid) / valid.Length}");
Console.WriteLine($"mean real   {Mean(valid):F3}");
Console.WriteLine($"out of band {OutOfBand(valid, 1480, 1520)} of {valid.Length}");

int[] sorted = (int[])valid.Clone();
Array.Sort(sorted);

Console.WriteLine($"median      {sorted[sorted.Length / 2]}");
Console.WriteLine($"original untouched: valid[0] = {valid[0]}");

Console.WriteLine();
Console.WriteLine("channel  rpm  state");
for (int i = 0; i < valid.Length; i++)
{
    string state = "ok";
    if (valid[i] < 1480 || valid[i] > 1520) state = "out";
    Console.WriteLine($"{i,-5}{valid[i],7}  {state}");
}

static int Sum(int[] v)
{
    int total = 0;
    foreach (int x in v) total += x;
    return total;
}

static double Mean(int[] v) => (double)Sum(v) / v.Length;

static int OutOfBand(int[] v, int lo, int hi)
{
    int c = 0;
    foreach (int x in v) if (x < lo || x > hi) c++;
    return c;
}
```

**Output**

```text
fields      8
read        7
rejected    1
sum         10478
mean int    1496
mean real   1496.857
out of band 2 of 7
median      1495
original untouched: valid[0] = 1480

channel  rpm  state
0       1480  ok
1       1502  ok
2       1495  ok
3       1533  out
4       1471  out
5       1509  ok
6       1488  ok
```

With `Convert.ToInt32` instead of `TryParse`, the program dies on the fourth field with `FormatException` and never prints a single line of the report. The worse case is not that one: `Convert.ToInt32` over `null` returns 0 in silence, and that zero enters the bank as a reading nobody ever took.

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The defended parse counts good and bad separately | 2 |
| The three methods exist, with `static` and no printing inside | 3 |
| `Clone` and `Array.Sort` leave the original untouched and it is checked | 2 |
| The report comes out aligned in three columns | 2 |
| Explains what would happen with `Convert.ToInt32` | 1 |

**Most common mistake**

They compute the mean over the eight-slot array instead of over the seven good readings, and the average drops to 1309; it gives itself away because their read line says 7 and their divisor is 8.

## Week 14 · Unit 6.2–6.3 · Grids, sorting and searching

### 14.1 · Recognise

**Solution**

Over unsorted input the binary search does not fail, it answers wrongly and keeps running. All five values are in the array and only two come back with their true position.

**Output**

```text
search 1533 -> 2
search 1502 -> 0
search 1471 -> -1
search 1495 -> -1
search 1500 -> -5
insertion point -> 4
```

The two that return the same number are `1471` and `1495`: both come back as minus one even though one lives at index 1 and the other at index 4. Two of the four answered correctly, 1533 and 1502, and by luck. No exception was thrown for any of the four. The precondition that has to be written next to any call is that the array must be sorted, because the algorithm never checks it.

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The six predicted lines match | 4 |
| Points at the two searches that return the same number | 2 |
| Says there was no exception in any case | 2 |
| States the precondition of the sorted array | 2 |

**Most common mistake**

They expect an exception for receiving an unsorted array; it gives itself away because their prediction has no numbers for the first four lines, only the word error.

### 14.2 · Apply

**Solution**

```csharp
double[,] dev = {
    { -0.012,  0.004,  0.021, -0.003 },
    {  0.008, -0.031,  0.015,  0.002 },
    { -0.005,  0.011, -0.047,  0.009 }
};

int rows = dev.GetLength(0);
int cols = dev.GetLength(1);

Console.WriteLine($"positions {rows}   points {cols}   cells {dev.Length}");
Console.WriteLine($"Rank {dev.Rank}");
Console.WriteLine();

for (int r = 0; r < rows; r++)
{
    double sum = 0;
    for (int c = 0; c < cols; c++) sum += dev[r, c];
    Console.WriteLine($"position {r}  mean {sum / cols,9:F4} mm");
}

Console.WriteLine();

for (int c = 0; c < cols; c++)
{
    double sum = 0;
    for (int r = 0; r < rows; r++) sum += dev[r, c];
    Console.WriteLine($"point    {c}  mean {sum / rows,9:F4} mm");
}

int worstR = 0, worstC = 0;
for (int r = 0; r < rows; r++)
    for (int c = 0; c < cols; c++)
        if (Math.Abs(dev[r, c]) > Math.Abs(dev[worstR, worstC]))
        {
            worstR = r;
            worstC = c;
        }

Console.WriteLine();
Console.WriteLine($"worst cell [{worstR},{worstC}] at {dev[worstR, worstC]:F4} mm");
Console.WriteLine($"outside +-0.030 mm -> {Math.Abs(dev[worstR, worstC]) > 0.030}");
```

**Output**

```text
positions 3   points 4   cells 12
Rank 2

position 0  mean    0.0025 mm
position 1  mean   -0.0015 mm
position 2  mean   -0.0080 mm

point    0  mean   -0.0030 mm
point    1  mean   -0.0053 mm
point    2  mean   -0.0037 mm
point    3  mean    0.0027 mm

worst cell [2,2] at -0.0470 mm
outside +-0.030 mm -> True
```

Add a fifth column to the grid and the program keeps running without touching a single loop, because both bounds come out of `GetLength` and not out of a number typed by hand. With the fifth column in place the header line reads `positions 3   points 5   cells 15`.

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The grid is declared with two indices and `Length` and `Rank` are reported | 2 |
| The means per position and per point are present and correct | 3 |
| The worst cell is chosen by absolute value and reports both indices | 3 |
| The bounds come out of `GetLength` and the extra-column test passes | 2 |

**Most common mistake**

They choose the worst cell by the signed value and report the plus 0.021 instead of the minus 0.047; it gives itself away because their worst cell does not cross the tolerance and their very next line says it does.

### 14.3 · Integrate

**Solution**

```csharp
int[] run = { 1480, 1502, 1495, 1533, 1471, 1509, 1488 };
int[] sorted = { 1471, 1480, 1488, 1495, 1502, 1509, 1533 };
int[] reversed = { 1533, 1509, 1502, 1495, 1488, 1480, 1471 };

Console.WriteLine("input        bubble cmp/mov   insertion cmp/mov");
Report("run      ", run);
Report("sorted   ", sorted);
Report("reversed ", reversed);

Console.WriteLine();
int[] target = (int[])run.Clone();
Array.Sort(target);
Console.WriteLine($"sequential 1533 -> {Sequential(target, 1533)} comparisons");
Console.WriteLine($"binary     1533 -> {Binary(target, 1533)} comparisons");
Console.WriteLine($"sequential 1471 -> {Sequential(target, 1471)} comparisons");
Console.WriteLine($"binary     1471 -> {Binary(target, 1471)} comparisons");

static void Report(string name, int[] source)
{
    int[] a = (int[])source.Clone();
    int[] b = (int[])source.Clone();
    Bubble(a, out int bc, out int bm);
    Insertion(b, out int ic, out int im);
    Console.WriteLine($"{name}        {bc,3} / {bm,-3}          {ic,3} / {im}");
}

static void Bubble(int[] a, out int cmp, out int mov)
{
    cmp = 0;
    mov = 0;
    for (int i = 0; i < a.Length - 1; i++)
    {
        bool swapped = false;
        for (int j = 0; j < a.Length - 1 - i; j++)
        {
            cmp++;
            if (a[j] > a[j + 1])
            {
                int t = a[j];
                a[j] = a[j + 1];
                a[j + 1] = t;
                mov++;
                swapped = true;
            }
        }
        if (!swapped) break;
    }
}

static void Insertion(int[] a, out int cmp, out int mov)
{
    cmp = 0;
    mov = 0;
    for (int i = 1; i < a.Length; i++)
    {
        int key = a[i], j = i;
        while (j >= 1)
        {
            cmp++;
            if (a[j - 1] <= key) break;
            a[j] = a[j - 1];
            j--;
            mov++;
        }
        a[j] = key;
    }
}

static int Sequential(int[] a, int key)
{
    int c = 0;
    for (int i = 0; i < a.Length; i++)
    {
        c++;
        if (a[i] == key) return c;
    }
    return c;
}

static int Binary(int[] a, int key)
{
    int lo = 0, hi = a.Length - 1, c = 0;
    while (lo <= hi)
    {
        c++;
        int mid = lo + (hi - lo) / 2;
        if (a[mid] == key) return c;
        if (a[mid] < key) lo = mid + 1; else hi = mid - 1;
    }
    return c;
}
```

**Output**

```text
input        bubble cmp/mov   insertion cmp/mov
run               20 / 10            15 / 10
sorted             6 / 0              6 / 0
reversed          21 / 21            21 / 21

sequential 1533 -> 7 comparisons
binary     1533 -> 3 comparisons
sequential 1471 -> 1 comparisons
binary     1471 -> 3 comparisons
```

Both of them like the already sorted input, where the bubble flag and the early exit of insertion drop both counts to 6. Neither one stops moving on the reversed input, and there both reach 21. Selection is the one that never changes its count, because it looks at everything whatever happens, which is why it does not appear in this table with three different numbers. The sequential search beats the binary one when looking for 1471, which ended up at position 0 of the sorted array: one comparison against three.

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The counters live inside the algorithm, with two `out` parameters | 3 |
| The three inputs run over a `Clone` and do not contaminate each other | 2 |
| The six pairs of counts match the measurement | 3 |
| The two searches return comparisons and not the position | 1 |
| Explains the case where the sequential search wins | 1 |

**Most common mistake**

They count each bubble swap as three moves, because a swap is three assignments; it gives itself away because their move count triples the one from class and their definition of a move is written down nowhere.

## Week 15 · Unit 7.1 · Records and enumerations

### 15.1 · Recognise

**Solution**

A `struct` fills itself in before you do: the numeric fields start at 0 and the enumeration field starts at the name worth 0, which here is `Ok`. Copying a `struct` copies it field by field, and when a field is a reference what gets copied is the reference.

**Output**

```text
Program.cs(22,16): warning CS0649: Field 'Sample.SensorId' is never assigned to, and will always have its default value 0
Program.cs(23,19): warning CS0649: Field 'Sample.Celsius' is never assigned to, and will always have its default value 0
Program.cs(24,19): warning CS0649: Field 'Sample.State' is never assigned to, and will always have its default value

SensorId 0
Celsius  0
State    Ok
looks healthy -> True
r1.Name        RUN-A
r1.Readings[0] 99.9
```

The text field did not move because a string cannot be edited in place: assigning something else to `r2.Name` changes the reference held by `r2` and leaves the one held by `r1` where it was. The array field did move because `r2.Readings[0] = 99.9` does not change the reference, it writes inside the array both of them point at.

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| Predicts the three `CS0649` and names them by field | 3 |
| The six predicted lines match | 3 |
| Explains why `State` comes out as `Ok` without anyone assigning it | 2 |
| Tells the text field apart from the array field | 2 |

**Most common mistake**

They predict `RUN-B` and 99.9, treating the `struct` as if it were a class; it gives itself away because the name line comes out wrong and the array line comes out right for the wrong reason.

### 15.2 · Apply

**Solution**

```csharp
Sample[] bank = new Sample[3];

bank[0] = new Sample { SensorId = 1, Celsius = 20.0, State = Status.Ok };
bank[1] = new Sample { SensorId = 2, Celsius = 99.9, State = Status.Fault };

Console.WriteLine("sensor  celsius  state");
foreach (Sample m in bank)
    Console.WriteLine($"{m.SensorId,-8}{m.Celsius,7:F1}  {m.State}");

Sample hottest = Hottest(bank);
Console.WriteLine();
Console.WriteLine($"hottest: sensor {hottest.SensorId} at {hottest.Celsius:F1} C");

Console.WriteLine($"slot 2 never filled: {bank[2].SensorId}, {bank[2].Celsius}, {bank[2].State}");
Console.WriteLine($"and it reports healthy -> {bank[2].State == Status.Ok}");

for (int i = 0; i < bank.Length; i++)
    bank[i].Celsius = bank[i].Celsius + 1.0;

Sample copy = bank[0];
copy.Celsius = 0.0;

Console.WriteLine();
Console.WriteLine($"after the for   bank[0].Celsius = {bank[0].Celsius:F1}");
Console.WriteLine($"after the copy  bank[0].Celsius = {bank[0].Celsius:F1}");
Console.WriteLine($"the copy holds                   {copy.Celsius:F1}");

static Sample Hottest(Sample[] b)
{
    int idx = 0;
    for (int i = 1; i < b.Length; i++)
        if (b[i].Celsius > b[idx].Celsius) idx = i;
    return b[idx];
}

enum Status { Ok, Warning, Fault }

struct Sample
{
    public int SensorId;
    public double Celsius;
    public Status State;
}
```

**Output**

```text
sensor  celsius  state
1          20.0  Ok
2          99.9  Fault
0           0.0  Ok

hottest: sensor 2 at 99.9 C
slot 2 never filled: 0, 0, Ok
and it reports healthy -> True

after the for   bank[0].Celsius = 21.0
after the copy  bank[0].Celsius = 21.0
the copy holds                   0.0
```

The `for` wrote into the bank because `bank[i]` is the `struct` itself, not a copy of it. The local variable is a copy, made at the moment of the assignment, and writing a field of it reaches nowhere.

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The record and the enumeration are declared at the end of the file | 2 |
| The table comes out aligned with the three samples, the empty one included | 2 |
| `Hottest` takes the array and returns a record | 2 |
| The unfilled slot is reported with its three fields and its comparison | 2 |
| The `for` writes and the copy does not, and both outputs prove it | 2 |

**Most common mistake**

They use `foreach` to raise the degree and the compiler answers `CS1654: Cannot modify members of 'm' because it is a 'foreach iteration variable'`; it gives itself away because they hand in the `.cs` with no output.

### 15.3 · Integrate

**Solution**

```csharp
Channel[] bank = new Channel[3];

bank[0] = new Channel
{
    Id = 1,
    Readings = new double[] { 1480, 1502, 1495 },
    State = Status.Unknown
};
bank[1] = new Channel
{
    Id = 2,
    Readings = new double[] { 1533, 1471, 1509 },
    State = Status.Unknown
};
bank[2] = new Channel
{
    Id = 3,
    Readings = new double[] { 1488, 1496, 1501 },
    State = Status.Unknown
};

for (int i = 0; i < bank.Length; i++)
{
    int outside = 0;
    foreach (double r in bank[i].Readings)
        if (r < 1480 || r > 1520) outside++;

    if (outside == 0) bank[i].State = Status.Ok;
    else if (outside == 1) bank[i].State = Status.Warning;
    else bank[i].State = Status.Fault;
}

Console.WriteLine("channel     mean  state    verdict");
foreach (Channel c in bank)
{
    double sum = 0;
    foreach (double r in c.Readings) sum += r;
    double mean = sum / c.Readings.Length;

    string verdict = c.State switch
    {
        Status.Ok => "stays online",
        Status.Warning => "check at shift close",
        Status.Fault => "take out of service",
        _ => "unclassified"
    };

    Console.WriteLine($"{c.Id,-8}{mean,8:F2}  {c.State,-8} {verdict}");
}

Console.WriteLine();
Console.WriteLine($"Status.Unknown is  {(int)Status.Unknown}");
Console.WriteLine($"Status.Fault is    {(int)Status.Fault}");
Console.WriteLine($"(Status)9 defined  {Enum.IsDefined((Status)9)}");

Channel copy = bank[0];
copy.Id = 99;
copy.Readings[0] = 0;

Console.WriteLine();
Console.WriteLine($"bank[0].Id           {bank[0].Id}");
Console.WriteLine($"bank[0].Readings[0]  {bank[0].Readings[0]}");

enum Status { Unknown = 0, Ok = 1, Warning = 2, Fault = 3 }

struct Channel
{
    public int Id;
    public double[] Readings;
    public Status State;
}
```

**Output**

```text
channel     mean  state    verdict
1        1492.33  Ok       stays online
2        1504.33  Fault    take out of service
3        1495.00  Ok       stays online

Status.Unknown is  0
Status.Fault is    3
(Status)9 defined  False

bank[0].Id           1
bank[0].Readings[0]  0
```

Channel 2 has the highest mean of the three and is the only one that goes out of service: the mean hides that two of its three readings left the band in opposite directions. When the record is copied, the identifier did not move because it is a loose value, and the first reading did move because both records share the array.

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The enumeration reserves zero for the unclassified | 2 |
| The three channels are filled and classified with a `for` | 2 |
| The report uses `foreach` and a `switch` expression with a discard | 2 |
| The three enumeration checks were run | 2 |
| The copy proves that the array is shared and the `int` is not | 2 |

**Most common mistake**

They leave `Ok = 0` and classify with the default value, so a channel nobody got round to classifying shows up as online; it gives itself away because their table has no channel in `Unknown` even though the array has slots the loop never touched.

## Week 16 · Unit 7 · Integration and final project

### 16.1 · Recognise

**Solution**

The counter `count` reaches 3, which is already a slot that does not exist in an array of three. The write of the fourth sample blows up and the `done` line never runs.

**Output**

```text
stored in slot 0
stored in slot 1
stored in slot 2
Unhandled exception. System.IndexOutOfRangeException: Index was outside the bounds of the array.
   at Program.<Main>$(String[] args) in Program.cs:line 6
```

Exit codes measured off the same binary: PowerShell 7 reports -532462766 and Git Bash reports 127, because POSIX shells trim the status to eight bits.

The version of `ReadOption` with `Convert.ToInt32` dies with `FormatException` when the operator types a letter, dies the same way with `3.7`, and dies again with empty input. Only with `null`, which is what arrives when the console is closed, does it return 0 in silence, and that zero reads as the exit option.

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| Predicts three lines and the exception, with no `done` | 3 |
| Reports both exit codes and says they belong to the shell | 3 |
| Classifies the four inputs of `ReadOption` | 3 |
| Points at the `null` case as the most dangerous of the four | 1 |

**Most common mistake**

They report a single exit code without saying which shell they measured it in; it gives itself away because the number they quote does not match the capture next to it.

### 16.2 · Apply

**Solution**

```csharp
Sample[] bank = new Sample[3];
int count = 0;
bool running = true;

while (running)
{
    Console.WriteLine("1 register  2 list  3 stats  0 exit");
    Console.Write("option: ");
    switch (ReadOption())
    {
        case 1: Register(bank, ref count); break;
        case 2: ListAll(bank, count); break;
        case 3: ShowStats(bank, count); break;
        case 0: running = false; break;
        default: Console.WriteLine("invalid option"); break;
    }
}

Console.WriteLine("done");

static int ReadOption()
{
    string? line = Console.ReadLine();
    if (line == null) return 0;
    if (int.TryParse(line, out int v)) return v;
    return -1;
}

static void Register(Sample[] b, ref int count)
{
    if (count >= b.Length)
    {
        Console.WriteLine("bank full, rejected");
        return;
    }
    b[count].SensorId = count + 1;
    b[count].Celsius = 20.0 + count;
    b[count].State = Status.Ok;
    count++;
    Console.WriteLine($"stored in slot {count - 1}");
}

static void ListAll(Sample[] b, int count)
{
    if (count == 0)
    {
        Console.WriteLine("no samples");
        return;
    }
    for (int i = 0; i < count; i++)
        Console.WriteLine($"{b[i].SensorId,-4}{b[i].Celsius,7:F1}  {b[i].State}");
}

static void ShowStats(Sample[] b, int count)
{
    if (count == 0)
    {
        Console.WriteLine("no samples, no stats");
        return;
    }
    double sum = 0;
    for (int i = 0; i < count; i++) sum += b[i].Celsius;
    Console.WriteLine($"n = {count}   mean = {sum / count:F2} C");
}

enum Status { Unknown = 0, Ok = 1, Warning = 2, Fault = 3 }

struct Sample
{
    public int SensorId;
    public double Celsius;
    public Status State;
}
```

**Output**

With the sequence `3, 1, 1, 1, 1, x, 2, 3, 0`, and `Build succeeded` with zero warnings:

```text
1 register  2 list  3 stats  0 exit
option: no samples, no stats
1 register  2 list  3 stats  0 exit
option: stored in slot 0
1 register  2 list  3 stats  0 exit
option: stored in slot 1
1 register  2 list  3 stats  0 exit
option: stored in slot 2
1 register  2 list  3 stats  0 exit
option: bank full, rejected
1 register  2 list  3 stats  0 exit
option: invalid option
1 register  2 list  3 stats  0 exit
option: 1      20.0  Ok
2      21.0  Ok
3      22.0  Ok
1 register  2 list  3 stats  0 exit
option: n = 3   mean = 21.00 C
1 register  2 list  3 stats  0 exit
option: done
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The menu has a tested way out: `running` changes only in `case 0` | 2 |
| `ReadOption` tells empty, number and junk apart without throwing | 2 |
| `Register` takes the counter by `ref` and carries the capacity guard | 3 |
| `ShowStats` cuts out before dividing when there are no samples | 2 |
| The build reports zero warnings | 1 |

**Most common mistake**

`Register` takes the counter by value, so the bank always writes into slot 0; it gives itself away because their run prints "stored in slot 0" three times and the stats report n equal to 0.

### 16.3 · Integrate

**Solution**

```csharp
using System.Globalization;

const int Minimum = 1480;
const int Maximum = 1520;
const string Station = "EST-07";

string capture = "1480,1502,1495,abc,1533,1471,1509,1488";

int attempts = 0;
double threshold;
bool ok;
do
{
    attempts++;
    Console.Write("alert threshold in rpm (5 to 60): ");
    string line = Console.ReadLine() ?? "";
    bool read = double.TryParse(line, NumberStyles.Float,
                                CultureInfo.InvariantCulture, out threshold);
    ok = read && threshold >= 5.0 && threshold <= 60.0;
    if (!ok) Console.WriteLine($"  rejected '{line}'");
    if (attempts == 3) break;
} while (!ok);

if (!ok)
{
    Console.WriteLine("INTERLOCKED: three invalid entries, console stopped");
}
else
{
    string[] fields = capture.Split(',');
    int[] valid = new int[fields.Length];
    int n = 0, rejected = 0;
    foreach (string field in fields)
    {
        if (int.TryParse(field.Trim(), out int value)) { valid[n] = value; n++; }
        else rejected++;
    }

    Sample[] bank = new Sample[n];
    for (int i = 0; i < n; i++)
    {
        bank[i].Channel = i;
        bank[i].Rpm = valid[i];
        bank[i].State = Classify(valid[i], Minimum, Maximum, threshold);
    }

    int sum = 0, notOk = 0;
    foreach (Sample m in bank)
    {
        sum += m.Rpm;
        if (m.State != Status.Ok) notOk++;
    }
    MinMax(bank, out int lowest, out int highest);

    Console.WriteLine();
    Console.WriteLine($"station    {Station.ToUpper()}  threshold {threshold:F1} rpm");
    Console.WriteLine($"fields {fields.Length}  read {n}  rejected {rejected}");
    Console.WriteLine($"mean int      {sum / n}");
    Console.WriteLine($"mean real     {(double)sum / n:F3} rpm");
    Console.WriteLine($"band midpoint {(Minimum + Maximum) / 2} rpm");
    Console.WriteLine($"range         {highest - lowest} rpm  ({lowest} to {highest})");
    Console.WriteLine($"max deviation {Math.Abs(highest - (Minimum + Maximum) / 2.0):F1} rpm");
    Console.WriteLine($"not Ok        {notOk} of {n}");

    Console.WriteLine();
    Console.WriteLine("channel  rpm  state    verdict");
    foreach (Sample m in bank)
    {
        string verdict = m.State switch
        {
            Status.Ok => "online",
            Status.Warning => "check at shift close",
            Status.Fault => "take out of service",
            _ => "unclassified"
        };
        Console.WriteLine($"{m.Channel,-5}{m.Rpm,7}  {m.State,-8} {verdict}");
    }
}

static Status Classify(int rpm, int lo, int hi, double threshold)
{
    if (rpm >= lo && rpm <= hi) return Status.Ok;
    double excess = Math.Max(lo - rpm, rpm - hi);
    if (excess <= threshold) return Status.Warning;
    return Status.Fault;
}

static void MinMax(Sample[] b, out int lowest, out int highest)
{
    lowest = b[0].Rpm;
    highest = b[0].Rpm;
    foreach (Sample m in b)
    {
        if (m.Rpm < lowest) lowest = m.Rpm;
        if (m.Rpm > highest) highest = m.Rpm;
    }
}

enum Status { Unknown = 0, Ok = 1, Warning = 2, Fault = 3 }

struct Sample
{
    public int Channel;
    public int Rpm;
    public Status State;
}
```

**Output**

Build with `0 Warning(s)` and `0 Error(s)`. With the inputs `abc` and then `10`:

```text
alert threshold in rpm (5 to 60):   rejected 'abc'
alert threshold in rpm (5 to 60): 
station    EST-07  threshold 10.0 rpm
fields 8  read 7  rejected 1
mean int      1496
mean real     1496.857 rpm
band midpoint 1500 rpm
range         62 rpm  (1471 to 1533)
max deviation 33.0 rpm
not Ok        2 of 7

channel  rpm  state    verdict
0       1480  Ok       online
1       1502  Ok       online
2       1495  Ok       online
3       1533  Fault    take out of service
4       1471  Warning  check at shift close
5       1509  Ok       online
6       1488  Ok       online
```

With a threshold of 10 rpm, the 1471 sample sits nine rpm under the minimum and classifies as a warning, while the 1533 one goes thirteen over the top and classifies as a fault. The alternative that was dropped was classifying into two states only, in band and out of band: with that version both samples get reported the same way, and the technician has no idea which of the two to reach first.

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The eight lines of the checklist appear in the file | 3 |
| The `do-while` validates with the culture pinned and cuts out with `break` | 2 |
| `Classify` and `MinMax` are methods, one of them with two `out` parameters | 2 |
| The report comes out aligned with the verdict pulled from a `switch` | 2 |
| The build reports zero warnings | 1 |

**Most common mistake**

They walk the whole bank for the statistics instead of only the valid readings, and the average drops in one go; it gives itself away because their report prints one extra line with channel 7 at 0 rpm and state `Unknown`.

## Week 17 · All course units · Review and final exam

### 17.1 · Recognise

**Solution**

| Line | Which week it comes from | Why |
|---|---|---|
| 1 and 2 | week 4 | the slash between two integers truncates and the cast goes before the division |
| 3 and 4 | weeks 4 and 7 | two readings are never compared with equals, they are compared by tolerance |
| 5 | weeks 5 and 16 | `Convert.ToInt32` over `null` returns 0 without saying a word |
| 6 | week 15 | a `struct` gets copied field by field |
| 7 | weeks 11 and 13 | an array is a reference and assigning it creates a second name |
| 8 | weeks 4 and 9 | the `int` wraps around with no error and no warning |

**Output**

```text
1  1496
2  1496.857
3  False
4  True
5  0
6  20
7  99
8  -2147483648
```

Line 5 is the most dangerous because it does not die. A zero nobody typed enters the bank as if it were a reading that was taken, drags the average down and leaves no trace in any log. The other seven either give a visibly odd number or give `False`, and that zero looks exactly like good data.

The scope file does not compile: `Program.cs(5,19): error CS0103: The name 'i' does not exist in the current context`. The control variable is born and dies in the header of the `for`, and column 19 points at the `i` inside the brackets.

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The eight predicted lines match | 4 |
| Every trap is tied to the week that taught it | 3 |
| Argues why line 5 is the most dangerous | 2 |
| Quotes `CS0103` with its column | 1 |

**Most common mistake**

They predict `99.9` on line 6 and `20` on line 7, swapping the two rules; it gives itself away because their explanation calls a copy what was shared and shared what was copied.

### 17.2 · Apply

**Solution**

```csharp
using System.Globalization;

string capture = "  EST-07:1480,1502,1495,abc,1533,1471,1509,1488  ";

string[] parts = capture.Trim().Split(':');
string tag = parts[0];
string[] fields = parts[1].Split(',');

int[] rpm = new int[fields.Length];
int n = 0, rejected = 0;
foreach (string field in fields)
{
    bool ok = int.TryParse(field.Trim(), NumberStyles.Integer,
                           CultureInfo.InvariantCulture, out int value);
    if (ok) { rpm[n] = value; n++; }
    else rejected++;
}

Sample[] bank = new Sample[n];
int sum = 0, outside = 0;
for (int i = 0; i < n; i++)
{
    bool bad = rpm[i] < 1480 || rpm[i] > 1520;
    bank[i].Channel = i;
    bank[i].Rpm = rpm[i];
    if (bad) { bank[i].State = Status.Fault; outside++; }
    else bank[i].State = Status.Ok;
    sum += rpm[i];
}

int[] sorted = new int[n];
Array.Copy(rpm, sorted, n);
Array.Sort(sorted);

Console.WriteLine($"tag           {tag}");
Console.WriteLine($"read {n}, rejected {rejected}");
Console.WriteLine($"out of band {outside} of {n}");
Console.WriteLine($"mean int      {sum / n}");
Console.WriteLine($"mean real     {(double)sum / n:F3}");
Console.WriteLine($"median        {sorted[n / 2]}");

int found = Array.BinarySearch(sorted, 1495);
int notFound = Array.BinarySearch(sorted, 1500);
Console.WriteLine($"binary 1495 -> {found}");
Console.WriteLine($"binary 1500 -> {notFound}, would insert at {~notFound}");

Console.WriteLine();
Console.WriteLine("channel  rpm  state");
foreach (Sample m in bank)
    Console.WriteLine($"{m.Channel,-5}{m.Rpm,7}  {m.State}");

enum Status { Unknown = 0, Ok = 1, Warning = 2, Fault = 3 }

struct Sample
{
    public int Channel;
    public int Rpm;
    public Status State;
}
```

**Output**

Build with `0 Warning(s)` and `0 Error(s)`.

```text
tag           EST-07
read 7, rejected 1
out of band 2 of 7
mean int      1496
mean real     1496.857
median        1495
binary 1495 -> 3
binary 1500 -> -5, would insert at 4

channel  rpm  state
0       1480  Ok
1       1502  Ok
2       1495  Ok
3       1533  Fault
4       1471  Fault
5       1509  Ok
6       1488  Ok
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The cut on the colon and on the commas separates tag from readings | 2 |
| `TryParse` with the culture pinned counts good and bad | 2 |
| The record bank classifies and accumulates in a single walk | 2 |
| The sort happens over a copy and the median comes out of it | 2 |
| Both searches are present and the negative is decoded | 2 |

**Most common mistake**

They sort the original array and then print the report by channel, so channel 0 is no longer the first reading of the shift; it gives itself away because their table comes out in ascending order and their median matches the middle row of the table.

### 17.3 · Integrate

**Solution**

```csharp
const double Tolerance = 0.030;
const int Capacity = 3;

double[,] grid = {
    { -0.012,  0.004,  0.021, -0.003 },
    {  0.008, -0.031,  0.015,  0.002 },
    { -0.005,  0.011, -0.047,  0.009 }
};

int rows = grid.GetLength(0);
int cols = grid.GetLength(1);

Position[] board = new Position[Capacity];
int stored = 0;

for (int r = 0; r < rows; r++)
{
    WorstInRow(grid, r, out int col, out double worst);
    Store(board, ref stored, r, col, worst, Tolerance);
}

Console.WriteLine("pos  point  deviation  state");
for (int i = 0; i < stored; i++)
{
    Position p = board[i];
    Console.WriteLine($"{p.Row,-5}{p.Column,-7}{p.Deviation,9:F4}  {p.State}");
}

Store(board, ref stored, 3, 0, 0.001, Tolerance);

double[] row2 = new double[cols];
for (int c = 0; c < cols; c++) row2[c] = grid[2, c];

double[] copy = (double[])row2.Clone();
Insertion(copy, out int cmp, out int mov);

Console.WriteLine();
Console.WriteLine($"row 2 original  {row2[0]:F3} {row2[1]:F3} {row2[2]:F3} {row2[3]:F3}");
Console.WriteLine($"row 2 sorted    {copy[0]:F3} {copy[1]:F3} {copy[2]:F3} {copy[3]:F3}");
Console.WriteLine($"insertion       {cmp} comparisons, {mov} shifts");

int pos = Array.BinarySearch(copy, 0.011);
Console.WriteLine($"binary 0.011 -> {pos}");

int inInt = int.MaxValue - 1;
long inLong = int.MaxValue - 1;
for (int k = 0; k < 3; k++) { inInt++; inLong++; }

Console.WriteLine();
Console.WriteLine($"cycles in int   {inInt}");
Console.WriteLine($"cycles in long  {inLong}");
Console.WriteLine($"they agree      {inInt == inLong}");

static void WorstInRow(double[,] g, int row, out int column, out double worst)
{
    column = 0;
    worst = g[row, 0];
    for (int c = 1; c < g.GetLength(1); c++)
        if (Math.Abs(g[row, c]) > Math.Abs(worst))
        {
            worst = g[row, c];
            column = c;
        }
}

static void Store(Position[] t, ref int count, int row, int column,
                  double deviation, double tolerance)
{
    if (count >= t.Length)
    {
        Console.WriteLine($"board full, position {row} rejected");
        return;
    }
    t[count].Row = row;
    t[count].Column = column;
    t[count].Deviation = deviation;
    if (Math.Abs(deviation) <= tolerance * 0.5) t[count].State = Status.Ok;
    else if (Math.Abs(deviation) <= tolerance) t[count].State = Status.Warning;
    else t[count].State = Status.Fault;
    count++;
}

static void Insertion(double[] a, out int cmp, out int mov)
{
    cmp = 0;
    mov = 0;
    for (int i = 1; i < a.Length; i++)
    {
        double key = a[i];
        int j = i;
        while (j >= 1)
        {
            cmp++;
            if (a[j - 1] <= key) break;
            a[j] = a[j - 1];
            j--;
            mov++;
        }
        a[j] = key;
    }
}

enum Status { Unknown = 0, Ok = 1, Warning = 2, Fault = 3 }

struct Position
{
    public int Row;
    public int Column;
    public double Deviation;
    public Status State;
}
```

**Output**

Build with `0 Warning(s)` and `0 Error(s)`.

```text
pos  point  deviation  state
0    2         0.0210  Warning
1    1        -0.0310  Fault
2    2        -0.0470  Fault
board full, position 3 rejected

row 2 original  -0.005 0.011 -0.047 0.009
row 2 sorted    -0.047 -0.005 0.009 0.011
insertion       5 comparisons, 3 shifts
binary 0.011 -> 3

cycles in int   -2147483647
cycles in long  2147483649
they agree      False
```

Table matching the blocks to the weeks:

| Block | Weeks that made it possible |
|---|---|
| Grid and worst cell with two `out` parameters | 11, 14 |
| Record with a guard and the counter by `ref` | 11, 15, 16 |
| Classification by tolerance and an enumeration with no misleading zero | 4, 7, 15 |
| Instrumented insertion and binary search | 9, 10, 14 |
| Cycle counter in `int` against `long` | 4, 9 |
| Aligned report | 5, 13 |

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| `WorstInRow` uses two `out` parameters and takes its bound from `GetLength` | 2 |
| `Store` carries the guard and the counter by `ref`, and the fourth is rejected | 2 |
| The insertion is instrumented and works over a `Clone` | 2 |
| The `int` counter wraps and the `long` does not, and they get compared | 2 |
| The table matching blocks to weeks is complete | 1 |
| The build reports zero warnings | 1 |

**Most common mistake**

They sort `row2` instead of its `Clone` and then print "the original row" already sorted; it gives itself away because their two row 2 lines are identical and the before-and-after comparison stops saying anything.
