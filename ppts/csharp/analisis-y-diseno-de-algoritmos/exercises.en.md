# Exercises · Analysis and Design of Algorithms · COM101

This set runs alongside the seventeen sessions of the course and is written for the first-semester Engineering group. Every week carries three exercises: Recognise is answered by reading code and predicting what it prints, Apply asks for a program written against a specification with concrete data, and Integrate ties the topic of the week to what came before. Difficulty climbs inside the week and across the term, so the Recognise of week 12 weighs more than the Integrate of week 4. Every problem lives on the same test bench: the roller conveyor at station EST-07, its tachometer with a nominal band of 1480 to 1520 rpm, the coolant tank, the thermocouples and the inspection fixture. Hand in through Blackboard, with the source code and the real output pasted in, never described in words.

## Week 01 · Course framing and grading

### 01.1 · Recognise
Write in your notebook, before touching the keyboard, what each of these three lines prints. Then run them without changing a letter and note the real output beside your prediction.

```csharp
Console.WriteLine(10478 / 7);
Console.WriteLine(0.1 + 0.7);
Console.WriteLine(0.1 + 0.7 == 0.8);
```

The 10478 is the sum of the seven rpm readings taken during the shift and the 7 is the number of samples. Explain in one line why the first line does not print 1496.857142857143.

### 01.2 · Apply
Create a new project with `dotnet new console -o est07` and edit the scaffold so it prints exactly these four things, in this order: the line `EST-07 TEST BENCH`, the line `Channel A · roller conveyor`, the line `Nominal band: 1480 to 1520 rpm`, and the value of `Environment.Version`.

Run it with `dotnet run` from a terminal, not from the button in the IDE. Hand in the capture showing the code and the output, plus the exit code your shell reported.

### 01.3 · Integrate
In the `est07.csproj` of your project change the property `<ImplicitUsings>enable</ImplicitUsings>` to `<ImplicitUsings>disable</ImplicitUsings>` and leave `Program.cs` alone. Try to build.

Answer three things in writing: the full compiler message, with file, line, column and error code; how many files were left in `bin/Debug/net10.0` after the attempt; and the single line you have to add at the top of `Program.cs` so it builds again without putting the property back to `enable`. Check all three, do not assume them.

## Week 02 · Unit 1 · Algorithm design

### 02.1 · Recognise
The coolant tank on the bench starts at 12.0 litres and the fill pump delivers 15.0 litres per pulse. This is the pseudocode of the purge routine.

```text
START
    level = 12.0
    WRITE "AIR PURGE STARTED"

    WHILE level < 60.0
        level = level + 15.0
        WRITE "filling tank:", level, "L"

    IF level >= 60.0 THEN
        WRITE "level reached, open recirculation pump"
    ELSE
        WRITE "ABORT: the tank never reached the level"

    WRITE "bench ready"
END
```

Write the full trace: how many lines it prints, with what level on each one, and how much liquid the tank ends with. Then answer whether the tank stopped at exactly 60.0 litres, and why.

### 02.2 · Apply
Write the prestart check of the conveyor on paper. The sequence tests three things in this order: that the guard door is closed, that the emergency stop is released, and that the shaft turns below 50 rpm. If all three hold, it arms the machine. If any one fails, it names that one and leaves the machine interlocked.

Hand in the pseudocode using the seven words of the course and the matching flowchart. Attach the expected trace for two data sets: door closed, e-stop released and 20 rpm; and door open, e-stop released and 20 rpm.

### 02.3 · Integrate
The maintenance instruction reads: "tighten the gearbox cover in a cross pattern until it feels firm". Put it through the two-person test and explain in two lines which of the five properties of an algorithm it breaks.

Then rewrite it as an algorithm. The cover has four bolts, the tightening runs in three passes, and the torque of each pass is 8, 16 and 24 N·m. Write the pseudocode with two nested FOR loops and, before anybody runs anything, write the full expected trace, line by line. The last line has to say how many tightening operations were done.

## Week 03 · Unit 2 · Introduction to programming

### 03.1 · Recognise
Five snippets, each one in its own file. For each say whether it compiles and, when it does not, what the code of the first error is and what the compiler misread.

```csharp
// A
int nominalTorque = 24;
Console.WriteLine(nominalTorque)

// B
int nominalTorque = 24;
int 2sensor = 7;

// C
int nominalTorque = 24;
Console.writeline(nominalTorque);

// D
int nominalTorque = 24;
Console.WriteLine(NominalTorque);

// E
int class = 7;
```

One of the five produces seven errors out of a single slip. Say which one and why the compiler sees so many.

### 03.2 · Apply
Write a program that declares three integer variables with the same name written in different case, `nominalTorque`, `NominalTorque` and `NOMINALTORQUE`, holding 24, 26 and 22 N·m. The program has to print the three values on one line, print whether the first two differ, print a string that contains the characters `//` without them turning into a comment, and print the result of comparing `"Console"` with `"console"`.

The file carries one line comment and one block comment, and the names follow the convention of the course. Hand in the `.cs` and the output.

### 03.3 · Integrate
Break the scaffold on purpose four times, one per file, and build a table with what each attempt returns. The four slips are: dropping the semicolon from the `Console.WriteLine` call, declaring `int 2sensor = 7;`, writing `Console.writeline` in lower case, and asking for `NominalTorque` when the variable is called `nominalTorque`.

Copy the first full message of each attempt, unedited, with file, line, column and error code. Add one line per case saying what the compiler misread. Two of the four complain about a name and return different codes: explain why.

## Week 04 · Unit 3 · Data, types and primitive operations

### 04.1 · Recognise
The tachometer band widened to 1471 and 1533 rpm. Predict the five outputs before running anything.

```csharp
int lo = 1471, hi = 1533;
Console.WriteLine(lo + hi / 2);
Console.WriteLine((lo + hi) / 2);
Console.WriteLine((lo + hi) / 2.0);
Console.WriteLine(hi % 100);
Console.WriteLine(7 / 2 * 2);
```

One of the five prints a number no tachometer on the planet can read. Point at it and say which operator won the race.

### 04.2 · Apply
Write the identity card of a bench gauge using the five types, one per value: the station is `EST-11`, the channel is the letter `C`, 12 samples were taken, the measured dimension is 24.972 mm and the channel is online. The nominal dimension, 25.0 mm, goes under `const` because it must not move for the whole run.

The program computes the deviation against nominal, prints it raw and to three decimals, and prints whether it fits inside a tolerance of 0.05 mm. The tolerance check is done with `Math.Abs`, never with an equals sign.

### 04.3 · Integrate
One program, three traps, zero warnings on the build. Write it and explain each result in one line.

1. A counter of inspected parts declared `byte` holds 250 and you add 10 to it with `+=`. Print the result.
2. A sampling window declared `short` holds 32000 and you add 1000 to it with `+=`. Print the result.
3. Four measured deviations are 0.5, 1.5, 2.5 and 3.5 microns. Print three sums: the real one, the one that comes out of rounding each with plain `Math.Round`, and the one that comes out of rounding each with `MidpointRounding.AwayFromZero`.
4. With `lo = 1471` and `hi = 1533`, print the midpoint of the band with brackets and without them.

Close with two lines: which of the two rounding rules you would use to report the accumulated wear of a batch of a hundred parts, and why.

## Week 05 · Unit 4 · Statements, input and output

### 05.1 · Recognise
The limits of the band are 1480 and 1520. Predict the five outputs.

```csharp
int lo = 1480, hi = 1520;
Console.WriteLine("rpm " + lo + hi);
Console.WriteLine("rpm " + (lo + hi));
Console.WriteLine(lo + hi + " rpm");
Console.WriteLine($"rpm {lo + hi}");
Console.WriteLine("deviations " + 2 + 3 + 4);
```

None of the five is an error. Explain in two lines the rule that decides when the plus sign adds and when it glues.

### 05.2 · Apply
Write the capture front end of the bench. Ask for three things with `Console.Write`, in this order: the station tag, the number of samples taken and the reading in rpm. Store each line in a variable before converting it.

Convert the samples with `int.TryParse` and the reading with `double.TryParse`, and keep the `bool` each one returns. Then print a block with the tag, the two `bool` values with their converted value beside them, the reading to three fixed decimals and the cycles of the shift, 148230, with a thousands separator.

There is no `if` in the course yet, so the `bool` gets printed, not used to decide. Run the program with `EST-07`, `12` and `1496.857142857143`.

### 05.3 · Integrate
The reading `480.50` comes off equipment that reports the allowable load in kilonewtons. Write a program that sets the machine culture to `es-MX`, converts that string with `double.TryParse` and prints the `bool` and the value; that then sets the culture to `de-DE` and repeats exactly the same; and that in each culture also prints 1496.857142 to two decimals, 148230 with a thousands separator and 0.0342 as a percentage with one decimal.

At the end, back in `es-MX`, print the allowable load raw and to two decimals, computed as 480.50 over a safety factor of 1.10.

Answer in writing: under `de-DE` the guard returned `True` and the value came out wrong. Explain in two lines why checking the `bool` is not enough and what else you would have to pin down.

## Week 06 · Unit 4.4 · Selection structures

### 06.1 · Recognise
The gearbox coolant interlock opens the bypass when the reading goes over 28.0 degrees. Somebody took the braces off the block.

```csharp
double coolantC = 26.8;

if (coolantC > 28.0)
    Console.WriteLine("alarm: coolant over limit");
    Console.WriteLine("bypass valve opened");

Console.WriteLine($"reading {coolantC} C logged");
```

Predict how many lines it prints and which ones. Then answer what it would print with `coolantC = 31.4` and, in one line, what bench failure this version of the program causes when the coolant is cold.

### 06.2 · Apply
Write a program that asks for the shaft rpm with `Console.Write`, reads them with `int.TryParse` and classifies them with an `else if` ladder into five cases: non-numeric reading, negative reading (tachometer cable loose), under 800 (idle), under 3000 (nominal) and the rest (overspeed, cut torque).

Every branch prints a single line that includes the reading. Run the program five times, with `800`, `-5`, `799`, `3000` and `abc`, and paste the five outputs. Explain in one line why 799 and 800 land in different bands.

### 06.3 · Integrate
Write the gearbox interlock console. Ask for two values, the coolant temperature in degrees and the shaft rpm, and convert both with `TryParse`, keeping their `bool`. The limit of 28.0 degrees goes under `const`.

Store in two named `bool` variables whether the reading is hot and whether it lands exactly on the limit. The ladder decides, in this order: non-numeric temperature, non-numeric rpm, hot (bypass open) and the rest (bypass closed). The branches that do have data print the reading to one decimal next to the limit.

The last line of the program always prints the two `bool` values and the rpm that were read, whatever happens. Run the program with three data sets: `31.4` and `1502`, `28.0` and `1502`, and `abc` and `1502`. Explain in two lines what would have changed in the second set if the comparison were `>=` instead of `>`.

## Week 07 · Unit 4.4 · Selection in depth

### 07.1 · Recognise
Four output lines, and not one line of this program is an error. Predict them.

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

Then answer two things in writing. What would happen if the `&&` of the first condition were a single `&`, and which `if` the `else` of the second block bound itself to.

### 07.2 · Apply
Write the part inspector of the bench. Ask for two values, the measured dimension in millimetres and the coolant temperature in degrees, and read both with `double.TryParse`. The nominal dimension, 25.00 mm, and the tolerance, 0.05 mm, go under `const`.

If either capture fails, the program prints a single line saying the part is not judged and computes nothing else. If both are good, compute the absolute deviation with `Math.Abs`, decide with a `switch` expression over the `bool` whether the part is accepted or rejected, and classify the temperature with another five-arm `switch` expression: negative (thermocouple unplugged), under 20.0 (cold), at or under 28.0 (nominal), under 90.0 (hot, bypass open) and the discard arm (shutdown on overtemperature).

Run the program with four sets: `25.06` and `31.4`, `24.97` and `28.0`, `25.00` and `-3.0`, and `abc` and `28.0`.

### 07.3 · Integrate
Write the interlock matrix of the machine. Ask for three values: the pressure in bar, whether the guard door is closed (1 or 0) and the mode (0 stop, 1 automatic, 2 jog). All three are read with `TryParse` and if any one fails the program prints one line and leaves the machine interlocked.

The pressure is in range between 3.5 and 5.0 bar, the two comparisons joined by `&&`. The machine starts only if the pressure is in range, the door is closed and the mode is automatic. A `switch` expression with a discard arm turns the mode number into its name.

The program prints four lines with the intermediate `bool` values and the result of `start`. When `start` is false, a nested ladder with braces names the first cause, in the order pressure, door, mode.

Hand in the truth table with these four rows and the four runs beside it: `4.2 1 1`, `4.2 0 1`, `0.5 1 1` and `4.2 1 2`. Add two lines explaining why `&&` is what protects this matrix and what would start up with `||` in its place.

## Week 08 · Unit 4.5 · Repetition · First midterm

The three exercises of this week review units 1 to 4 and repetition at the level it was taught today. The `for`, the nesting and the counted cost belong to week 9 and are out of scope here.

### 08.1 · Recognise
Seven bolts on the gearbox cover were measured with a torque wrench. Predict the five numbers this program prints.

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

Console.WriteLine($"bolts inspected      {inspected}");
Console.WriteLine($"skipped as loose     {skipped}");
Console.WriteLine($"sum within tolerance {sum}");
Console.WriteLine($"index of the cut     {cut}");
Console.WriteLine($"never inspected      {torque.Length - inspected}");
```

Point your finger at the line that makes the `while` condition false and say what happens if you delete the `i++` that sits before the `continue`.

### 08.2 · Apply
Write the defended capture of the coolant temperature. The program asks for a value with `Console.Write`, reads it with `double.TryParse` and accepts it only if it falls between 10.0 and 95.0 degrees. While it does not accept, it asks again and prints an indented line showing in quotes exactly what was typed.

The loop cuts out at four attempts and leaves the bench interlocked. On accepting, it prints the temperature to one decimal and how many attempts it cost.

Run the program twice. The first time with `abc`, `120`, `-5` and `31.4`. The second with four junk entries in a row. Justify in a paragraph why `do-while` belongs here and `while` does not.

### 08.3 · Integrate
Write the shift close console. Cross everything you carry from the term into a single file, in this order.

1. The limits of the band, 1480 and 1520, go under `const`.
2. A `do-while` asks for the closing sample in rpm, reads it with `int.TryParse` and accepts it only inside the band. Three attempts and it interlocks.
3. If it accepted, an `else if` ladder classifies it into low band (under 1490), middle (under 1510) or high.
4. Three interlocks joined with `&&` decide whether the machine ends up armed: door closed, e-stop released and the sample inside the band.
5. A `while` walks the run `{ 1480, 1502, 1495, 1533, 1471, 1509, 1488 }` accumulating the sum and counting the out-of-band readings under the rule `r < 1480 || r > 1520`.
6. Print sum, integer mean, real mean to three decimals and the out-of-band count.

Run the program with `abc` and then `1502`. Explain in two lines why the integer mean and the real mean are not the same number.

## Week 09 · Unit 4.5 · Repetition in depth

### 09.1 · Recognise
Four bench sensors are compared in pairs. Predict the three numbers.

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

Console.WriteLine($"outer passes {outer}");
Console.WriteLine($"inner passes {inner}");
Console.WriteLine($"pairs counted {pairs}");
```

Answer two more questions. Which of the two loops the `break` leaves, and what the compiler answers if you write `Console.WriteLine(a);` after the outer loop.

### 09.2 · Apply
Over the run `{ 1480, 1502, 1495, 1533, 1471, 1509, 1488 }`, write a program with a single `for` that fills four accumulators: the sum, the count of readings outside the 1480 to 1520 band under the rule `r < 1480 || r > 1520`, the index of the maximum and the index of the minimum. The four variables are declared before the loop.

Then add a `foreach` that sums and counts the readings again, to check that it gives the same. The program prints nine lines: readings, sum with the foreach sum in brackets, integer mean, raw real mean, mean to three decimals, out-of-band count, maximum with its index, minimum with its index and the range.

Explain in one line which of the four accumulators cannot be written with `foreach` and why.

### 09.3 · Integrate
Write the fatigue report of the bench. A single file with three blocks and their outputs.

1. Over the seven readings of the run, count the ones that fall outside the band and print the percentage four ways: `outside * 100 / 7`, `outside * 100.0 / 7`, that same value to one decimal, and the raw count. Explain which of the three numbers you would report to the maintenance lead.
2. With two nested loops count how many comparisons the full mesh of the seven sensors against all of them makes, and how many the version that starts the inner loop at `a + 1` makes. Print both counts.
3. A cycle counter declared `int` starts at `int.MaxValue - 2` and goes up three times inside a `for`, printing its value on every pass. The same count repeated in `long` is printed at the end. Close with how many days of continuous running at 25 cycles per second the `int` counter would take to reach its ceiling, to one decimal.

Write two lines at the end: what the maintenance system would have reported the morning the `int` counter wrapped around, and how that case is caught without changing the type.

## Week 10 · Unit 5.1 · User-defined functions

### 10.1 · Recognise
Three separate files. For each one say whether it compiles, what code the compiler returns and what it prints when it runs.

```csharp
// A
static void PrintHeader()
{
    Console.WriteLine("EST-07 BENCH - SHIFT CLOSE");
}

// B
double m = ShowMean(21.0, 39.5);
Console.WriteLine(m);

static void ShowMean(double a, double b)
{
    Console.WriteLine((a + b) / 2);
}

// C
int limitC = 30;
Console.WriteLine(OverLimit(39));

static int OverLimit(int reading)
{
    return reading - limitC;
}
```

File A compiles. Explain in one line why it prints nothing and what the compiler is warning it about. For C, say which word has to go for it to compile and what is lost by removing it.

### 10.2 · Apply
Take the accumulator sweep of week 9 and split it into four named methods, all marked `static`.

- `Sum` takes the array of readings and returns the total.
- `Mean` takes the array and returns the real average, leaning on `Sum`.
- `OutOfBand` takes the array and the two limits, and returns how many readings fall outside.
- `IndexOfMax` takes the array and returns the position of the highest reading.

The top-level code only calls the four and builds four output lines over the run `{ 1480, 1502, 1495, 1533, 1471, 1509, 1488 }` with limits 1480 and 1520. The mean prints to three decimals. None of the four methods prints anything on its own.

### 10.3 · Integrate
Write the program that measures what reaches the caller when an array crosses the boundary of a method. Over the run of seven readings, in this order:

1. `Zero` takes the array and writes a 0 at position 0. Print `rpm[0]` after calling it.
2. `Replace` takes the array and assigns it, inside, a brand new three-element array of minus one. Print `rpm[0]` after calling it.
3. `ReplaceRef` does exactly the same, but the parameter goes with `ref`. Print `rpm[0]` after calling it.
4. `Window` takes the array, a start index and a count, and returns a new array with that window. Cut the window that starts at 2 and measures 3, write a 0 into its first position and print the window and also `original[2]`.
5. `Mean` is declared with `params int[] samples` and returns `double.NaN` when it receives none. Call it with two samples, with the whole run and with no arguments.

Explain in three lines why point 1 reaches the caller, why point 2 does not, and which word changes the ending of point 3.

## Week 11 · Unit 5.3 · Passing parameters by reference

### 11.1 · Recognise
Predict the three lines. The body of the two swap methods is identical.

```csharp
int channelA = 1, channelB = 2;

SwapByValue(channelA, channelB);
Console.WriteLine($"by value      {channelA}, {channelB}");

SwapByRef(ref channelA, ref channelB);
Console.WriteLine($"by reference  {channelA}, {channelB}");

int stored = 999;
bool ok = int.TryParse("abc", out stored);
Console.WriteLine($"TryParse      {ok}, stored = {stored}");

static void SwapByValue(int a, int b)
{
    int t = a; a = b; b = t;
}

static void SwapByRef(ref int a, ref int b)
{
    int t = a; a = b; b = t;
}
```

Also answer what the compiler says if you drop the two `ref` keywords from the second call site and leave the signature as it is.

### 11.2 · Apply
Write two bench pieces in a single file.

`MinMax` takes the thermocouple array `{ 21.0, 39.5, 22.4 }` and two `out` parameters, and leaves in them the coldest and the hottest reading. The caller prints both to one decimal.

`Fill` and `Drain` take the level of the coolant tank by `ref` and an amount in litres. `Fill` rejects any operation that goes over 60.0 litres and `Drain` rejects any that would leave the tank under 5.0 litres. The rejection message says the number that would have been left, not just that it could not be done.

Start the tank at 40.0 litres and chain four operations: fill 15.0, fill 10.0, drain 20.0 and drain 40.0. Print the level after each one.

### 11.3 · Integrate
Write the calibration routine of one bench channel. In this order:

1. Declare `bench = { 21.0, 39.5, 22.4 }` and a second name `alias` assigned from the first. Write 99.9 into `alias[0]` and print `bench[0]` and the result of `ReferenceEquals`. Put `bench[0]` back to 21.0.
2. A `do-while` asks for the calibration offset in degrees and reads it with `double.TryParse`. It accepts only values between -5.0 and 5.0, cuts out at three attempts and in that case leaves the bench untouched.
3. If it accepted, `Apply` adds the offset to channel 1 taking the array element by `ref`, and `Clip` leaves that same element at 30.0 if it went over, reporting what it clipped from and to.
4. `MinMax` with two `out` parameters reports the new minimum and maximum of the bench.

Run the program with `abc` and then `-2.5`. Explain in three lines why the array of point 1 is shared without anybody writing `ref`, and why point 3 does need the word.

## Week 12 · Unit 5.4 · Predefined functions

### 12.1 · Recognise
Ten output lines and one compiler warning. Predict the ten and say which line the warning comes from.

```csharp
double nan = Math.Sqrt(-1);

Console.WriteLine($"Math.Sqrt(-1)          {nan}");
Console.WriteLine($"nan == nan             {nan == nan}");
Console.WriteLine($"double.IsNaN(nan)      {double.IsNaN(nan)}");
Console.WriteLine($"Math.Sin(Math.PI)      {Math.Sin(Math.PI)}");
Console.WriteLine($"|sin(pi)| < 1e-9       {Math.Abs(Math.Sin(Math.PI)) < 1e-9}");
Console.WriteLine($"Math.Round(2.5)        {Math.Round(2.5)}");
Console.WriteLine($"Round(2.5) away from 0 {Math.Round(2.5, MidpointRounding.AwayFromZero)}");
Console.WriteLine($"1.0 / 0                {1.0 / 0}");
Console.WriteLine($"Math.Clamp(39.5,0,30)  {Math.Clamp(39.5, 0.0, 30.0)}");
Console.WriteLine($"Math.Pow(2, 10)        {Math.Pow(2, 10)}");
```

Answer three more things. Why the second line does not print `True`. What code the compiler returns if you write `int capacity = Math.Pow(2, 10);`. And what `Math.Sqrt("9")` returns.

### 12.2 · Apply
The vibration window of the gearbox carries seven samples in mm/s: `{ 0.42, -0.31, 0.55, -0.48, 0.12, -0.27, 0.61 }`. Write the program that computes the RMS value.

Walk the window with `foreach`, accumulate the square of each sample with `Math.Pow` and carry the peak with `Math.Max` over `Math.Abs`. The RMS is the square root of the average of the squares, with `Math.Sqrt`. Compute as well the crest factor, which is the peak over the RMS, and the RMS clipped to the alarm threshold of 0.4500 mm/s with `Math.Clamp`.

Print six lines: the raw RMS with all its digits, the RMS to four decimals with its unit, the peak, the crest factor, the clipped RMS and whether the RMS crossed the threshold.

### 12.3 · Integrate
The bench is stripped down and the accumulators have to be tested without it. Write the program that simulates twenty rpm samples and puts them through the sweep of week 9.

The seed, 2026, goes under `const` and the generator is built once, outside the loop. Every sample comes out of `Next(1400, 1601)`. One `for` fills the array and another accumulates the sum, counts the readings outside the 1480 to 1520 band and carries the index of the highest one.

The program prints the seed, the first five samples, the sum, the mean to three decimals, the out-of-band count and the peak with its index. It closes by building a status word: add 1 if there were out-of-band readings, add 2 if the peak went over 1520 and add 4 if the integer mean went over 1500. Print that word in decimal, in binary and in hexadecimal with `Convert.ToString`.

Run the program twice in a row and paste both outputs. Explain in two lines what would have changed if the generator were built inside the loop.

## Week 13 · Unit 6.1 · Arrays and strings · Second midterm

The three exercises review the whole of unit 5 and unit 6 up to subtopic 6.1.3. Two-index grids and the sorting and searching algorithms belong to week 14 and are out of scope. The `Array.Sort` call is in scope, because the deck of today uses it to pull a median.

### 13.1 · Recognise
Nine output lines. Predict them all.

```csharp
int[] src = { 1480, 1502, 1495 };
int[] alias = src;
int[] copy = (int[])src.Clone();

alias[0] = 99;
copy[1] = 77;

Console.WriteLine($"src[0] {src[0]}   src[1] {src[1]}");
Console.WriteLine($"alias is the same {ReferenceEquals(src, alias)}");
Console.WriteLine($"copy is the same  {ReferenceEquals(src, copy)}");

string tag = "sensor-07";
tag.ToUpper();
Console.WriteLine($"tag        {tag}");
Console.WriteLine($"ToUpper()  {tag.ToUpper()}");
Console.WriteLine($"tag.Length {tag.Length}");
Console.WriteLine($"empty inside {tag.Contains("")}");
Console.WriteLine($"fields of the empty {"".Split(';').Length}");
Console.WriteLine($"Substring(9) [{tag.Substring(9)}]");
```

Answer as well what happens if you change `tag.Substring(9)` to `tag.Substring(10)`, and what happens with `tag[9]`. Both indices sit outside the text and they do not fail the same way.

### 13.2 · Apply
The logger hands over this line, with spaces on both sides: `  EST-07:1480.0,1502.5,1495.0,1533.5  `.

Write the program that splits it into tag and readings. Trim first, cut on the colon and then on the commas, and convert each field with `double.Parse` pinning `CultureInfo.InvariantCulture`. Print the tag, how many fields came out, the mean to three decimals and the first and the last reading to one decimal.

In the same file write `IdValid`, which takes a part identifier and returns `bool`. The rules are: trim what arrives, length exactly 10, prefix `SNS-`, suffix `-A` or `-B`, and positions 4 to 7 have to be digits. Both text comparisons use the same policy, `StringComparison.OrdinalIgnoreCase`.

Test it with five inputs: `SNS-4471-A`, `  SNS-4471-A  `, `sns-4471-b`, `SNS-44X1-A` and the empty string. The third one is what gives away whether your validator has one policy or two.

### 13.3 · Integrate
The shift capture arrived with one field ruined: `1480,1502,1495,abc,1533,1471,1509,1488`. Write the program that processes the whole of it.

1. Cut on the commas and convert each field with `int.TryParse`. The good ones are stored and the bad ones counted. Copy the good ones into an array of the exact size.
2. Three `static` methods compute the rest: `Sum`, `Mean` leaning on `Sum`, and `OutOfBand` with both limits as parameters.
3. Take a copy with `Clone`, sort it with `Array.Sort` and report the median. Then print the first element of the original array to check that the copy never touched it.
4. Close with an aligned three-column report, channel, rpm and state, where the state says `out` when the reading leaves the 1480 to 1520 band.

Print as well how many fields arrived, how many were read, how many were rejected, the sum, the integer mean and the real mean to three decimals. Explain in two lines what would have happened with `Convert.ToInt32` instead of `TryParse`.

## Week 14 · Unit 6.2–6.3 · Grids, sorting and searching

### 14.1 · Recognise
The array of sample identifiers is not sorted and all five values are inside it. Predict the six lines.

```csharp
int[] unsorted = { 1502, 1471, 1533, 1480, 1495 };

Console.WriteLine($"search 1533 -> {Array.BinarySearch(unsorted, 1533)}");
Console.WriteLine($"search 1502 -> {Array.BinarySearch(unsorted, 1502)}");
Console.WriteLine($"search 1471 -> {Array.BinarySearch(unsorted, 1471)}");
Console.WriteLine($"search 1495 -> {Array.BinarySearch(unsorted, 1495)}");

int[] sorted = { 1471, 1480, 1488, 1495, 1502, 1509, 1533 };
int missing = Array.BinarySearch(sorted, 1500);
Console.WriteLine($"search 1500 -> {missing}");
Console.WriteLine($"insertion point -> {~missing}");
```

Two of the first four searches return the same number even though the values sit in different positions. Point at them. Then answer how many of the four answered correctly, whether any exception was thrown, and what precondition has to be written next to any call into this library.

### 14.2 · Apply
The inspection fixture measures four points on each of the three part positions. The deviations in millimetres are:

```text
position 0:  -0.012   0.004   0.021  -0.003
position 1:   0.008  -0.031   0.015   0.002
position 2:  -0.005   0.011  -0.047   0.009
```

Write the program that loads that grid into a two-index array, prints how many positions, how many points, how many cells and what `Rank` it has, and then prints the mean of each position and the mean of each point, to four decimals right-aligned.

Close by reporting the worst cell by absolute deviation with both its indices and whether it crosses the tolerance of 0.030 mm. The bounds of every loop come out of `GetLength`, not out of a 3 or a 4 typed by hand. Add a fifth column to the grid and check that the program keeps running without touching a single loop.

### 14.3 · Integrate
Instrument two sorts and two searches over the same readings, and report the counts.

Write `Bubble` with an early-exit flag and `Insertion`, both with two `out` parameters returning comparisons and moves. A bubble comparison is each evaluation of `a[j] > a[j + 1]`, and an insertion one is each evaluation of the key against `a[j - 1]`.

Run them over three inputs of seven readings: the logged run `{ 1480, 1502, 1495, 1533, 1471, 1509, 1488 }`, that same run already sorted and that same run reversed. Each run works on a `Clone`, so all three start from the same place. Build a table with the six pairs of counts.

Then write `Sequential` and `Binary`, both with the signature `static int Search(int[] a, int key)`, returning how many comparisons it cost to arrive. Search for 1533 and 1471 over the already sorted array and report the four numbers.

Close with three lines: which input suits each sort, which of the two never changes its count, and why the sequential search beats the binary one in one of the four cases you measured.

## Week 15 · Unit 7.1 · Records and enumerations

### 15.1 · Recognise
This program compiles with three warnings and prints six lines. Predict the three warnings and the six lines.

```csharp
Sample empty = new Sample();
Console.WriteLine($"SensorId {empty.SensorId}");
Console.WriteLine($"Celsius  {empty.Celsius}");
Console.WriteLine($"State    {empty.State}");
Console.WriteLine($"looks healthy -> {empty.State == Status.Ok}");

Run r1 = new Run();
r1.Name = "RUN-A";
r1.Readings = new double[] { 20.0, 21.0 };

Run r2 = r1;
r2.Name = "RUN-B";
r2.Readings[0] = 99.9;

Console.WriteLine($"r1.Name        {r1.Name}");
Console.WriteLine($"r1.Readings[0] {r1.Readings[0]}");

enum Status { Ok, Warning, Fault }

struct Sample
{
    public int SensorId;
    public double Celsius;
    public Status State;
}

struct Run
{
    public string Name;
    public double[] Readings;
}
```

Explain in two lines why the text field did not move and the array field did, when the copy was field by field in both cases.

### 15.2 · Apply
Declare `Sample` with three fields, the sensor identifier, the reading in degrees and the state, and an enumeration `Status` with `Ok`, `Warning` and `Fault`. Create an array of three samples and fill only the first two: sensor 1 at 20.0 degrees in `Ok` and sensor 2 at 99.9 degrees in `Fault`.

The program prints the full table of the three samples aligned in three columns, reports with a `Hottest` method which sensor carries the highest reading, and prints the three fields of the slot nobody ever filled together with the result of comparing it against `Status.Ok`.

Then raise all three samples by one degree with a `for`, take a copy of the first into a local variable, set the copy to 0.0 and print the first sample of the array and the copy again. Explain in two lines why the `for` wrote into the bank and the copy did not.

### 15.3 · Integrate
Design the record of the channel bank and run it. `Channel` has three fields: the identifier, an array of readings and the state. The enumeration `Status` holds `Unknown = 0`, `Ok = 1`, `Warning = 2` and `Fault = 3`, with zero reserved for whatever nobody classified.

Fill three channels, each one with three readings: channel 1 with `1480, 1502, 1495`, channel 2 with `1533, 1471, 1509` and channel 3 with `1488, 1496, 1501`. All of them are born in `Unknown`.

A `for` classifies each channel by counting its readings outside the 1480 to 1520 band: zero outside is `Ok`, one is `Warning` and two or more is `Fault`. A `foreach` then walks the bank to print the aligned report with the identifier, the mean to two decimals, the state and a verdict pulled from a `switch` expression with a discard arm.

Close with three checks: the integer value of `Unknown` and of `Fault`, what `Enum.IsDefined` answers about `(Status)9`, and what happens to channel 1 when you copy its record into another variable, change the identifier and write a 0 into the first reading of the copy.

## Week 16 · Unit 7 · Integration and final project

### 16.1 · Recognise
This is the bench record without the guard, with room for three samples and four to store.

```csharp
Sample[] bank = new Sample[3];
int count = 0;

for (int i = 0; i < 4; i++)
{
    bank[count].SensorId = i + 1;
    bank[count].Celsius = 20.0 + i;
    count++;
    Console.WriteLine($"stored in slot {count - 1}");
}

Console.WriteLine("done");
```

Predict how many lines it manages to print, which exception kills it and whether it gets as far as printing `done`. Then run it in PowerShell and in Git Bash and report the exit code of each.

Answer as well what this version of the menu option read does when the operator types a letter, when they type `3.7` and when the input arrives empty:

```csharp
static int ReadOption()
{
    string line = Console.ReadLine();
    return Convert.ToInt32(line);
}
```

### 16.2 · Apply
Build the reference skeleton of the project, the one that compiles and runs before it has a single feature inside it.

The menu is a `while` with four options: 1 register, 2 list, 3 stats and 0 exit, resolved with a `switch` that has a `default` arm. `ReadOption` returns 0 when the input runs out, the number when `int.TryParse` manages it, and minus one in any other case.

`Register` takes the array and the counter by `ref`, and before writing it checks whether the bank is full. `ListAll` and `ShowStats` take the counter by value and report when there are no samples, so the division by zero never happens.

The bank has three slots and holds a `struct Sample` with identifier, degrees and a `Status`. Run the sequence `3, 1, 1, 1, 1, x, 2, 3, 0` and paste the output. The build has to report zero warnings.

### 16.3 · Integrate
Write the inspection console of bench EST-07. It is the integrating project in miniature and it has to satisfy the checklist lines numbered below, in a single file, with zero warnings.

1. The station, the minimum and the maximum of the band go under `const`.
2. A `do-while` asks for the alert threshold in rpm, reads it with `double.TryParse` pinning `InvariantCulture` and accepts only between 5.0 and 60.0. It cuts out with a justified `break` at three attempts.
3. The logger line `1480,1502,1495,abc,1533,1471,1509,1488` is cut on the commas and converted with `int.TryParse`, counting the ones that get rejected.
4. An array of `Sample` holds channel, rpm and `Status`, with the enumeration at `Unknown = 0`, `Ok = 1`, `Warning = 2` and `Fault = 3`.
5. A `Classify` method decides the state: inside the band is `Ok`; outside it but with an excess at or under the threshold is `Warning`; past that is `Fault`. The excess is computed with `Math.Max`.
6. A `MinMax` method with two `out` parameters reports the lowest and the highest reading.
7. A `foreach` accumulates the sum and counts the samples that did not end up in `Ok`.
8. The report prints the tag in upper case with `ToUpper`, the field count, the integer mean, the real mean to three decimals, the midpoint of the band with brackets, the range, the maximum deviation with `Math.Abs`, and the aligned table of channel, rpm, state and verdict pulled from a `switch` expression.

Run the program with `abc` and then `10`. Hand in the code, the output and a paragraph with the design alternative you considered and dropped.

## Week 17 · All course units · Review and final exam

The three exercises review the whole term. There is no new material here.

### 17.1 · Recognise
Eight numbered lines. Predict them all and say which week each trap comes from.

```csharp
int sum = 10478, n = 7;
Console.WriteLine($"1  {sum / n}");
Console.WriteLine($"2  {(double)sum / n:F3}");

double reading = 0.1 + 0.2;
Console.WriteLine($"3  {reading == 0.3}");
Console.WriteLine($"4  {Math.Abs(reading - 0.3) < 1e-9}");

string? nothing = null;
Console.WriteLine($"5  {Convert.ToInt32(nothing)}");

Sample s1 = new Sample { SensorId = 1, Celsius = 20.0 };
Sample s2 = s1;
s2.Celsius = 99.9;
Console.WriteLine($"6  {s1.Celsius}");

int[] src = { 20, 21, 22 };
int[] alias = src;
alias[0] = 99;
Console.WriteLine($"7  {src[0]}");

int cycles = int.MaxValue;
cycles++;
Console.WriteLine($"8  {cycles}");

struct Sample
{
    public int SensorId;
    public double Celsius;
}
```

Of the eight, number 5 is the most dangerous in a real program. Explain why in two lines. Then say what the compiler answers to this other file and which column it points at:

```csharp
for (int i = 0; i < 3; i++)
{
    Console.WriteLine(i);
}
Console.WriteLine(i);
```

### 17.2 · Apply
Write the review program that crosses the seven topics of the course. The input is the logger line `  EST-07:1480,1502,1495,abc,1533,1471,1509,1488  `, with spaces on both sides.

1. Trim, cut on the colon, split off the tag and cut the readings on the commas.
2. Convert each field with `int.TryParse` pinning `InvariantCulture`, storing the good ones and counting the bad ones.
3. Fill an array of `Sample` with channel, rpm and `Status`, classifying under the rule `r < 1480 || r > 1520` and counting the out-of-band ones.
4. Copy with `Array.Copy`, sort with `Array.Sort` and report the median.
5. Search for 1495 and 1500 with `Array.BinarySearch` and print the return of each one, plus the insertion point of the one that is missing, decoded with the bitwise complement.
6. Close with the aligned report of channel, rpm and state.

Print as well the tag, how many were read, how many were rejected, the out-of-band count, the integer mean and the real mean to three decimals. The build has to report zero warnings.

### 17.3 · Integrate
Term close on bench EST-07. A single file, zero warnings, four blocks.

1. Load the deviation grid of three positions by four points from week 14. A `WorstInRow` method with two `out` parameters returns the column and the value of the worst cell of a row, comparing by absolute value and taking its bound out of `GetLength`.
2. A `Store` method takes an array of `Position` with room for three and the counter by `ref`, and before writing it checks whether there is room. It classifies each position as `Ok` if the absolute deviation fits in half the tolerance, `Warning` if it fits in the tolerance of 0.030 mm and `Fault` if it goes past. Store the three positions of the grid and then try to store a fourth, so the guard is seen working.
3. Copy row 2 into a one-dimensional array, take a `Clone` of it and sort that with `Insertion` instrumented with two `out` parameters. Print the original row, the sorted one and the two counts. Then search for the value 0.011 in the sorted row with `Array.BinarySearch`.
4. A cycle counter declared `int` and another declared `long` both start at `int.MaxValue - 1` and go up three times inside the same `for`. Print both and whether they agree.

Hand in the code, the full output and a two-column table linking each block of the program to the weeks of the course that made it possible.
