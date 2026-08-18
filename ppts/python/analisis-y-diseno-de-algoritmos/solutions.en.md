# Solutions · Analysis and Design of Algorithms · COM101

Instructor copy. Every exercise carries the solution as it was run, the exact output it produced, the ten-point rubric, and the mistake that turns up most often while marking it. All the Python was executed with the course interpreter; the week 2 solutions are paper work and get checked against the trace. The exercises that read from the keyboard are shown as a full session, with what the student types on the same line as the prompt.

The data are the same all term: machining cell C-3, its stations EST-01 to EST-04, the 12.00 mm bronze bushing with its 11.95 to 12.05 mm band, and the `measurements.csv` file of weeks 14 to 17.

---

## Week 01 · Course introduction and the bridge from Excel to Python

### 01.1 · Recognise

**Solution**

```text
T1 1240
7990
1331.6666666666667
T4
```

`parts[3]` is shift T4, with 1510 parts. In the spreadsheet the value came from, it sits on row 5: row 1 holds the headers, row 2 holds T1, and from there Python's index 3 lands two rows below what intuition says.

`print(parts[6])` raises `IndexError`. The list holds six elements and the last valid index is 5.

**Output**

```text
T1 1240
7990
1331.6666666666667
T4
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The four lines correct, average included and unrounded | 4 |
| Identifies `parts[3]` as T4 | 2 |
| Places the spreadsheet row counting the header | 2 |
| Explains the `IndexError` and names the last valid index | 2 |

**Most common mistake**

Answering `T3 1120` on the first line and calling `parts[3]` shift T3. That is counting from one, and the giveaway is that every answer ends up shifted by exactly one position.

### 01.2 · Apply

**Solution**

```python
shifts = ["T1", "T2", "T3", "T4", "T5", "T6"]
parts = [1240, 1385, 1120, 1510, 1295, 1440]

total = sum(parts)
average = total / len(parts)
best_shift = shifts[parts.index(max(parts))]
best_value = max(parts)
above_average = best_value - average

print(f"Parts this week:   {total:,}")
print(f"Average per shift: {average:,.1f}")
print(f"Best shift:        {best_shift} with {best_value:,}")
print(f"Above the average: {above_average:,.1f}")
```

**Output**

```text
Parts this week:   7,990
Average per shift: 1,331.7
Best shift:        T4 with 1,510
Above the average: 178.3
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The four figures are correct | 4 |
| The best shift comes out of `index` and `max`, not typed by hand | 3 |
| Thousands separator and one decimal where they belong | 2 |
| The labels let the report be read without the code | 1 |

**Most common mistake**

Writing `best_shift = "T4"` because it already showed up in the previous output. The program gives the right answer and stops giving it the moment one value changes, which is exactly what happens in 01.3.

### 01.3 · Integrate

**Solution**

```python
shifts = ["T1", "T2", "T3", "T4", "T5", "T6"]
parts = [1240, 1385, 1320, 1510, 1295, 1440]

total = sum(parts)
average = total / len(parts)
best_shift = shifts[parts.index(max(parts))]

ticket = "00847"

print(f"Lot ticket:        {ticket}")
print(f"Parts this week:   {total:,}")
print(f"Average per shift: {average:,.1f}")
print(f"Best shift:        {best_shift}")
```

Before the correction: 7,990 parts, 1,331.7 average, T4. After it: 8,190 parts, 1,365.0 average, T4. The best shift does not change because T3 still sits below T4.

In a spreadsheet the change would have propagated on its own. In Python nothing is recalculated until the file gets run again, and that is the second of the four breaking points. The advantage shows up the other way round: the procedure is written down, so the same correction can be applied again three months from now and give exactly the same thing.

Captured with a number format, the ticket shows as 847: leading zeros are not part of a numeric value and they vanish. That is the third of the four breaking points, the one about types. A ticket number is stored as text because it is an identifier. It never gets added up, it never gets averaged, and its shape is the only thing that lets anyone find it again in the system that issued it.

**Output**

```text
Lot ticket:        00847
Parts this week:   8,190
Average per shift: 1,365.0
Best shift:        T4
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The three new figures are correct and get compared with the old ones | 3 |
| Notices that the best shift does not change and says why | 2 |
| Names the recalculation breaking point and explains it | 2 |
| Explains that the ticket captured as a number shows as 847 | 2 |
| Explains why a ticket number is text | 1 |

**Most common mistake**

Claiming the best shift is now T3 because T3 is the one that changed. The reasoning follows the value that was touched instead of the result, and comparing 1320 with 1510 settles it.

---

## Week 02 · Unit 1 · Algorithm design

### 02.1 · Recognise

**Solution**

Part at 12.08 mm. `12.08 > 12.05` is evaluated and holds, so the verdict is set to «Reject: oversize». The other two branches are never read.

Part at 11.94 mm. `11.94 > 12.05` is evaluated and fails. `11.94 < 11.95` is evaluated and holds, so the verdict is set to «Reject: undersize». The closing `ELSE` is never read.

Part at exactly 12.05 mm. `12.05 > 12.05` is evaluated and fails, because the operator asks for strictly greater. `12.05 < 11.95` also fails. It lands in the `ELSE` and the verdict is «Accepted». The part sits right on the limit and gets released.

With the second version, the 12.08 mm part enters through `12.08 >= 11.95`, which holds, and leaves as «Accepted». The oversize branch is unreachable: any diameter above 12.05 is also greater than or equal to 11.95, so the first condition takes it every time.

That second version is finite, precise and well defined, it has input and it has output. It satisfies all five properties and still releases parts that do not pass. An algorithm that is correct in form can be solving the wrong problem, which is why the order of the conditions gets checked with cases rather than by eye.

**Output**

```text
Part       Condition tested      Result       Verdict
12.08 mm   12.08 > 12.05         Holds        Reject: oversize
11.94 mm   11.94 > 12.05         Fails        -
11.94 mm   11.94 < 11.95         Holds        Reject: undersize
12.05 mm   12.05 > 12.05         Fails        -
12.05 mm   12.05 < 11.95         Fails        Accepted

Second version
12.08 mm   12.08 >= 11.95        Holds        Accepted
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The three traces correct, with the unread conditions marked | 4 |
| The 12.05 case comes out accepted and the reason is given | 2 |
| Traces the second version and spots the unreachable oversize branch | 2 |
| Argues that it satisfies the five properties and is still wrong | 2 |

**Most common mistake**

Saying the 12.05 part gets rejected because it «reached the limit». The limit is being confused with the reject zone, and it shows up as the student reading `>` as though it were `>=`.

### 02.2 · Apply

**Solution**

```text
START
    READ guard_closed, stop_released, spindle_temperature

    IF guard_closed = FALSE THEN
        WRITE "Cell interlocked: guard open"
    ELSE IF stop_released = FALSE THEN
        WRITE "Cell interlocked: emergency stop pressed"
    ELSE IF spindle_temperature >= 68 THEN
        WRITE "Cell interlocked: spindle hot"
    ELSE
        WRITE "Cell armed"

    END
```

The flowchart carries an oval for the start, a parallelogram reading the three values, three diamonds chained on their NO branch, four parallelograms for the writes, and an oval for the end. Each diamond has both of its exits labelled.

The order matters: the guard gets checked first because it is the condition protecting the operator, and a cell with the guard open does not get armed no matter how cool the spindle is.

**Output**

```text
Case 1: guard closed, stop released, 61 C
  Diamond 1: guard_closed = FALSE?   No, carry on
  Diamond 2: stop_released = FALSE?  No, carry on
  Diamond 3: 61 >= 68?               No, carry on
  Output: Cell armed

Case 2: guard closed, stop released, 71 C
  Diamond 1: guard_closed = FALSE?   No, carry on
  Diamond 2: stop_released = FALSE?  No, carry on
  Diamond 3: 71 >= 68?               Yes
  Output: Cell interlocked: spindle hot
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The pseudocode checks the three conditions in the order asked for | 3 |
| Every failure names the condition that failed, not a generic message | 2 |
| The flowchart uses the four symbols for what they mean | 2 |
| The diamonds have both exits labelled and both lead somewhere | 1 |
| The two traces are correct | 2 |

**Most common mistake**

One single diamond holding all three conditions and a «check failed» message. The algorithm decides correctly and is useless, because the operator has no idea what to go and look at.

### 02.3 · Integrate

**Solution**

The two-person test: two inspectors holding the same 12.06 mm part can decide differently, because «looks off size» depends on who is looking. The property that breaks is precision, and being well defined goes with it, because the same input stops producing the same result.

```text
START
    READ diameter

    IF diameter > 12.05 THEN
        destination = "Rework: regrind"
    ELSE IF diameter < 11.95 THEN
        destination = "Scrap: undersize"
    ELSE
        destination = "Release"

    WRITE destination
END
```

Input: the measured diameter of a part, in millimetres. Output: where that part goes, one text value out of three.

Edge case the first version did not cover: a reading of 0.00 mm, which happens when the micrometer never made contact. With the algorithm above that part comes out as scrap for being undersize, and that is not true: the part has not been measured. It gets covered with a branch at the top that rejects readings at or below zero and asks for the part to be measured again.

**Output**

```text
Original instruction     Two inspectors, one 12.06 mm part, two destinations
Property broken          Precision, and being well defined along with it

Trace of three parts
12.06 mm   12.06 > 12.05    Holds    Rework: regrind
11.90 mm   11.90 > 12.05    Fails
11.90 mm   11.90 < 11.95    Holds    Scrap: undersize
12.00 mm   both fail                 Release

Edge case added
 0.00 mm   diameter <= 0    Holds    Measure again
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| Applies the two-person test with a concrete value | 2 |
| Names the broken property and justifies it | 2 |
| The algorithm has the three outputs and uses the right band | 3 |
| Identifies input and output in writing | 1 |
| The edge case broke the earlier version and the change is explained | 2 |

**Most common mistake**

Rewriting the instruction with more words and no numbers. «If the diameter is well off nominal» still depends on who reads it, and it is spotted because neither 11.95 nor 12.05 appears anywhere on the page.

---

## Week 03 · Units 1 and 2 · Paradigms and an introduction to programming

### 03.1 · Recognise

**Solution**

The trace: after the first line `parts` holds 1240, after the second 1325, and after the third 2650. The program prints 2650. The equals sign does not compare, it stores, and every line overwrites what the one before left behind.

Fragment A: does not run. `NameError`, because `Sum` with a capital does not exist. It breaks the rule about capital letters.

Fragment B: does not run. `SyntaxError` for an unterminated string, on line 2. It breaks the rule about quotation marks.

Fragment C: does not run. `SyntaxError` saying the parenthesis was never closed, reported on line 2 even though the problem is right there at the end of the file. It breaks the rule about parentheses.

Fragment D: does not run. `NameError`, because `Print` with a capital is not `print`. It breaks the rule about capital letters.

**Output**

```text
2650

A  NameError: name 'Sum' is not defined. Did you mean: 'sum'?
B  SyntaxError: unterminated string literal (detected at line 2)
C  SyntaxError: '(' was never closed
D  NameError: name 'Print' is not defined. Did you mean: 'print'?
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The trace of the three lines with their intermediate values | 3 |
| The four fragments classified as running or not | 2 |
| The right kind of error on all four | 3 |
| Names the rule broken in each one | 2 |

**Most common mistake**

Answering 250 on the trace, multiplying before adding. The program is being read as a formula with precedence, when it is three assignments that run in order.

### 03.2 · Apply

**Solution**

```python
# Tachometer readings from the cell conveyor, in rpm.
from statistics import mean

readings = [1496, 1502, 1488, 1511, 1494]

average = mean(readings)
highest = max(readings)

print("Samples:", len(readings))
print("Average rpm:", average)
print("Highest reading:", highest)
```

The table of the three deliberate breakages, with the line each one was made on:

| What was broken | Message |
|---|---|
| Closing parenthesis, line 11 | `SyntaxError: '(' was never closed` |
| `print` with a capital, line 9 | `NameError: name 'Print' is not defined. Did you mean: 'print'?` |
| Quotation mark deleted, line 10 | `SyntaxError: unterminated string literal (detected at line 10)` |

**Output**

```text
Samples: 5
Average rpm: 1498.2
Highest reading: 1511
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The program runs and the three figures are correct | 3 |
| Carries the comment, the import and labels on the `print` calls | 2 |
| The three error messages are transcribed in full | 3 |
| Reports the line each error pointed at | 2 |

**Most common mistake**

Handing in the messages paraphrased, along the lines of «it threw a syntax error». What gets lost is exactly the useful part, which is the last words of the message and the line number.

### 03.3 · Integrate

**Solution**

```python
# The week 2 verdict pseudocode, said in Python.
diameter = 12.05

if diameter > 12.05:
    verdict = "Reject: oversize"
elif diameter < 11.95:
    verdict = "Reject: undersize"
else:
    verdict = "Accepted"

print("Measured diameter:", diameter, "mm")
print("Verdict:", verdict)
```

The 12.00 run prints `12.0` because the trailing zero is not part of the value. The number stored is twelve, and how many decimals get shown is a presentation decision solved with formatting, not with the data.

If the first two branches get swapped, a 12.08 mm part still comes out as a reject for being oversize, because `12.08 < 11.95` fails and the second branch does get evaluated. The swap that really breaks the algorithm is the one from week 2, where the accepted branch goes first.

**Output**

```text
Measured diameter: 12.05 mm
Verdict: Accepted

Measured diameter: 11.94 mm
Verdict: Reject: undersize

Measured diameter: 12.0 mm
Verdict: Accepted
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The translation respects the order of the three branches | 3 |
| The three runs are pasted in full and are correct | 3 |
| Explains why it prints `12.0` | 2 |
| Answers correctly about swapping the branches | 2 |

**Most common mistake**

Writing three loose `if` statements instead of `if`, `elif` and `else`. With these three conditions the result matches, and the student never notices that three comparisons were evaluated where one would have done.

---

## Week 04 · Unit 3 · Data, data types and primitive operations

### 04.1 · Recognise

**Solution**

```text
51.666666666666664
51
16
1205
17
True
False
0.15000000000000002
```

The second line says how many trays get filled completely: 51. The third says how many parts are left loose once those are filled: 16.

The sixth and seventh lines compare decimals that come out exact on paper and give opposite results. The reason is that 0.05 cannot be represented exactly in binary. In one case the rounding errors cancel and the equality holds; in the other they do not. That is why the tolerance band gets written as two constants and never worked out by adding and subtracting inside a condition.

**Output**

```text
51.666666666666664
51
16
1205
17
True
False
0.15000000000000002
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The eight lines correct, with the first one unrounded | 4 |
| Reads integer division and remainder as trays and parts | 2 |
| Tells text concatenation apart from adding integers | 2 |
| Explains why two similar comparisons give opposite results | 2 |

**Most common mistake**

Answering `True` on the seventh line because 0.05 times 3 is 0.15 on paper. It is the same correct reasoning that produces a tolerance condition failing once every thousand parts.

### 04.2 · Apply

**Solution**

```python
cell = "C-3"
station = "EST-01"
date = "2026-01-08"
parts = 1240
rejects = 37
energy_kwh = 86.4
station_running = True
last_stoppage = None

reject_rate = rejects / parts
energy_per_part = energy_kwh / parts

print(f"{cell} {station} {date}")
print(f"Reject rate:     {round(reject_rate * 100, 2)} %")
print(f"Energy per part: {round(energy_per_part, 4)} kWh")
print(type(parts), type(energy_kwh))
print(type(station), type(station_running), type(last_stoppage))
```

The date is stored as text because there is nothing to do with it yet. `last_stoppage` holds `None`, which is absence of data and not zero: zero minutes of stoppage is a measurement, `None` is nobody recording anything.

**Output**

```text
C-3 EST-01 2026-01-08
Reject rate:     2.98 %
Energy per part: 0.0697 kWh
<class 'int'> <class 'float'>
<class 'str'> <class 'bool'> <class 'NoneType'>
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The eight variables carry the type that belongs to each value | 3 |
| `last_stoppage` is `None` and not zero, with the explanation | 2 |
| Both metrics correct and rounded | 3 |
| The names say what they hold and none is a single letter | 2 |

**Most common mistake**

Writing `last_stoppage = 0`. The program runs, and the average stoppage length comes out wrong the moment anybody works it out, because a shift with no stoppages enters the average as a stoppage of zero minutes.

### 04.3 · Integrate

**Solution**

```python
parts = 1240
rejects = 37
energy_kwh = 86.4
per_tray = 24

per_part_wrong = energy_kwh / parts - rejects
per_part_right = energy_kwh / (parts - rejects)

print(f"Without parentheses: {round(per_part_wrong, 4)}")
print(f"With parentheses:    {round(per_part_right, 4)} kWh per good part")

good = parts - rejects
full_trays = good // per_tray
loose = good % per_tray

print(f"Good parts: {good}")
print(f"Full trays: {full_trays}, loose parts: {loose}")

ticket = "00847"

print(f"Ticket: {ticket}  integer: {int(ticket)}  back to text: {str(int(ticket))}")
```

The first version divides the energy across every part and then subtracts 37 from the result, which is subtracting parts from an energy per part. It comes out negative because it is taking pears away from kilowatts. The second one splits the shift energy across the 1203 parts that were actually any good, which is the question that was asked.

The ticket number loses its leading zeros the moment it becomes an integer, and it does not get them back on the way to text. What was lost is not the number, it is the identifier.

**Output**

```text
Without parentheses: -36.9303
With parentheses:    0.0718 kWh per good part
Good parts: 1203
Full trays: 50, loose parts: 3
Ticket: 00847  integer: 847  back to text: 847
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| Both expressions written and both results shown | 3 |
| Explains what each one calculates, not just which is right | 2 |
| Full trays and loose parts correct | 3 |
| Reports the loss of the leading zeros and what it implies | 2 |

**Most common mistake**

Working the trays out from the 1240 parts produced instead of the 1203 good ones. The number lands close to the right one, which is why nobody checks it until parts are missing from the shipment.

---

## Week 05 · Unit 4 · Statements, input and output

### 05.1 · Recognise

**Solution**

```text
Parts: 1,240
Energy: 86.40 kWh
Rejects: 3.0%
Rejects: 2.98%
EST-01        1240
Raw rate: 0.029838709677419355
Energy: {energy:.2f} kWh
```

The third and fourth lines show the same value with a different number of decimals: the one-decimal version rounds 2.98 up to 3.0, and in a quality report that difference decides whether the station appears inside or outside a 3 % target.

The last line is missing the `f` before the quotation mark. It is not an error: the string prints as written, braces and format code and all, and the program carries on as if nothing happened.

**Output**

```text
Parts: 1,240
Energy: 86.40 kWh
Rejects: 3.0%
Rejects: 2.98%
EST-01        1240
Raw rate: 0.029838709677419355
Energy: {energy:.2f} kWh
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The seven lines correct, with their commas and their spaces | 5 |
| Explains the rounding of 2.98 to 3.0 and why it matters | 2 |
| Spots the missing `f` and says it raises no error | 3 |

**Most common mistake**

Writing `Rejects: 0.0%` on the third line. The percentage code already multiplies by a hundred, and the tell is that the same student also writes `2.98` as though it were the raw value.

### 05.2 · Apply

**Solution**

```python
station = input("Station: ")
parts = int(input("Parts produced: "))
rejects = int(input("Parts rejected: "))
energy = float(input("Shift energy in kWh: "))

rate = rejects / parts
per_part = energy / parts

print(f"Station:         {station}")
print(f"Parts:           {parts:,}")
print(f"Rejects:         {rejects:,}")
print(f"Reject rate:     {rate:.2%}")
print(f"Energy per part: {per_part:.4f} kWh")
```

**Output**

```text
Station: EST-01
Parts produced: 1240
Parts rejected: 37
Shift energy in kWh: 86.4
Station:         EST-01
Parts:           1,240
Rejects:         37
Reject rate:     2.98%
Energy per part: 0.0697 kWh
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The four `input` calls carry a prompt and get converted where needed | 3 |
| Both metrics are correct | 3 |
| Thousands, percentage and four-decimal formats applied | 2 |
| The session is handed in complete, with what was typed | 2 |

**Most common mistake**

Converting after operating, with `int(parts / rejects)` instead of converting each `input`. Dividing two strings blows up first, and when it does not, it is because the student concatenated without noticing.

### 05.3 · Integrate

**Solution**

```python
SHIFT_SECONDS = 28800

station = input("Station: ")
parts = int(input("Parts produced: "))
rejects = int(input("Parts rejected: "))
energy = float(input("Shift energy in kWh: "))

good = parts - rejects
rate = rejects / parts
cycle = SHIFT_SECONDS / parts
per_good = energy * 1000 / good

print(f"Shift report {station}")
print(f"{'Parts produced':<22}{parts:>10,}")
print(f"{'Good parts':<22}{good:>10,}")
print(f"{'Reject rate':<22}{rate:>10.2%}")
print(f"{'Cycle time':<22}{cycle:>10.2f} s")
print(f"{'Energy per good part':<22}{per_good:>10.1f} Wh")
```

Cycle time is worked out from the parts produced, because the machine spent time on the ones that came out wrong too. Energy per good part is split across the good ones only, because it is a cost that has to be carried by what actually gets sold. Two different denominators in one report, each with its reason.

**Output**

```text
Station: EST-03
Parts produced: 1512
Parts rejected: 68
Shift energy in kWh: 112.8
Shift report EST-03
Parts produced             1,512
Good parts                 1,444
Reject rate                4.50%
Cycle time                 19.05 s
Energy per good part        78.1 Wh
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The five figures are correct | 4 |
| The shift constant has a name and sits at the top | 1 |
| The five lines line up at the widths asked for | 2 |
| Every figure carries its unit | 1 |
| Justifies the two different denominators | 2 |

**Most common mistake**

Working the cycle time out from the good parts. It comes to 19.94 seconds and sounds reasonable, but the machine did not stop working on the 68 parts that came out wrong.

---

## Week 06 · Unit 4.4 · Selection structures

### 06.1 · Recognise

**Solution**

The first program prints `12.05 Accepted`. The condition asks for strictly greater, and 12.05 is not greater than 12.05, so the part falls into the `else`. That is the right behaviour: the upper limit is part of the band.

The second program prints `12.08 Accepted`, and that is wrong. The first condition asks whether the diameter is greater than or equal to the lower limit, and a part at 12.08 satisfies it. Since the first branch that holds is the one that runs, the oversize branch is never reached: any value above 12.05 is also greater than or equal to 11.95.

The correct order runs from the most demanding to the least: oversize first, undersize second, and acceptance last as the remaining case.

**Output**

```text
12.05 Accepted
12.08 Accepted
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| Both outputs correct | 4 |
| Explains why 12.05 is accepted under the strict operator | 2 |
| Spots the unreachable oversize branch and says why | 2 |
| Writes the correct order of the three conditions | 2 |

**Most common mistake**

Saying the second program raises an error because two conditions hold. There is no error: the first one runs and the rest are never read, which is exactly what makes it dangerous.

### 06.2 · Apply

**Solution**

```python
LOWER_LIMIT = 11.95
UPPER_LIMIT = 12.05

part = input("Part number: ")
diameter = float(input("Measured diameter in mm: "))

if diameter > UPPER_LIMIT:
    verdict = "Reject: oversize"
elif diameter < LOWER_LIMIT:
    verdict = "Reject: undersize"
else:
    verdict = "Accepted"

print(f"Part {part}: {diameter:.2f} mm -> {verdict}")
```

**Output**

```text
Part number: BJ-1003
Measured diameter in mm: 12.06
Part BJ-1003: 12.06 mm -> Reject: oversize

Part number: BJ-1005
Measured diameter in mm: 11.94
Part BJ-1005: 11.94 mm -> Reject: undersize

Part number: BJ-1008
Measured diameter in mm: 12.05
Part BJ-1008: 12.05 mm -> Accepted

Part number: BJ-1013
Measured diameter in mm: 11.95
Part BJ-1013: 11.95 mm -> Accepted

Part number: BJ-1004
Measured diameter in mm: 12.00
Part BJ-1004: 12.00 mm -> Accepted
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The three verdicts correct across the five runs | 4 |
| Both limits are named constants, not loose numbers | 2 |
| The 12.05 and 11.95 parts come out accepted | 2 |
| The part number is read as text and the diameter converted to decimal | 2 |

**Most common mistake**

Using `>=` in the first condition. Parts at 12.05 get rejected, the station loses roughly one in ten, and the program looks perfectly correct.

### 06.3 · Integrate

**Solution**

```python
NOMINAL = 12.00
LOWER_LIMIT = 11.95
UPPER_LIMIT = 12.05
REWORK_CEILING = 12.15
CONCESSION_FLOOR = 11.85

diameter = float(input("Measured diameter in mm: "))

if diameter <= 0 or diameter > 20:
    verdict = "Invalid reading: check the micrometer"
elif diameter > REWORK_CEILING:
    verdict = "Scrap: oversize"
elif diameter > UPPER_LIMIT:
    verdict = "Rework: regrind"
elif diameter >= LOWER_LIMIT:
    verdict = "Accepted"
elif diameter >= CONCESSION_FLOOR:
    verdict = "Deviation: release under concession"
else:
    verdict = "Scrap: undersize"

print(f"{diameter:>7.2f} mm  {verdict}")
```

The check goes first because a reading of -3.00 mm is not a short part, it is a badly used micrometer, and filing it as scrap would hide the fault in the instrument.

Boundary table:

| Boundary | Exact value | Verdict | Why that operator |
|---|---|---|---|
| Rework ceiling | 12.15 | Rework | `>` leaves 12.15 on the recoverable side, which is what the grinder can handle |
| Upper limit | 12.05 | Accepted | `>` keeps the limit inside the band, as the drawing says |
| Lower limit | 11.95 | Accepted | `>=` keeps the limit inside the band |
| Concession floor | 11.85 | Concession | `>=` leaves 11.85 on the side engineering can release |
| Validity check | 0 and 20 | Invalid | `<=` on zero because a zero reading means no contact |

**Output**

```text
Measured diameter in mm: 12.30
  12.30 mm  Scrap: oversize
Measured diameter in mm: 12.15
  12.15 mm  Rework: regrind
Measured diameter in mm: 12.06
  12.06 mm  Rework: regrind
Measured diameter in mm: 12.05
  12.05 mm  Accepted
Measured diameter in mm: 12.00
  12.00 mm  Accepted
Measured diameter in mm: 11.95
  11.95 mm  Accepted
Measured diameter in mm: 11.90
  11.90 mm  Deviation: release under concession
Measured diameter in mm: 11.85
  11.85 mm  Deviation: release under concession
Measured diameter in mm: 11.80
  11.80 mm  Scrap: undersize
Measured diameter in mm: -3.00
  -3.00 mm  Invalid reading: check the micrometer
Measured diameter in mm: 25.00
  25.00 mm  Invalid reading: check the micrometer
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The five categories are exclusive and sit in the right order | 3 |
| The check runs before any classification and catches both impossible cases | 2 |
| The eleven runs are correct | 2 |
| The five boundaries are named constants | 1 |
| The table documents the verdict of each boundary value | 2 |

**Most common mistake**

Putting the validity check at the end, after the `else`. It never runs, because by then the -3.00 has already been filed as scrap for being undersize and the program flags nothing.

---

## Week 07 · Unit 4.4 · Nested selection and logical operators

### 07.1 · Recognise

**Solution**

```text
Critical station
True
False
Not enough data
True
```

Line 1. The condition is `station == "EST-01" or "EST-03"`. Python evaluates the comparison, which is false, then evaluates the string `"EST-03"`, which counts as true because it is not empty. The whole condition is always true, EST-04 included. The correct form is `station in ["EST-01", "EST-03"]`.

Line 2. Both lists hold the same values in the same order, so they are equal.

Line 3. They are two different lists in memory, so `is` gives false. The double equals compares content, `is` compares identity.

Line 4. With zero parts, `parts > 0` is false and Python never evaluates the division. That is the short-circuit of `and`, and it is what avoids the `ZeroDivisionError`. With `or`, a first condition that is false forces the second one to be evaluated, and that is where it blows up.

Line 5. `last_stoppage is None` is the right way to ask whether a value is absent.

**Output**

```text
Critical station
True
False
Not enough data
True
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The five lines correct | 4 |
| Explains why the first condition is always true and fixes it with `in` | 2 |
| Tells `==` apart from `is` with the identity argument | 2 |
| Explains short-circuiting and why `or` would blow up | 2 |

**Most common mistake**

Answering «Normal station» on the first line by reasoning about what the code meant to say. What the author intended is being read instead of what Python evaluates, and it shows because the same student sees nothing odd about EST-04 either.

### 07.2 · Apply

**Solution**

```python
CRITICAL = ["EST-01", "EST-03"]
MAX_RATE = 0.03
MIN_PARTS = 500

station = input("Station: ")
parts = int(input("Parts in the lot: "))
rejects = int(input("Parts rejected: "))
in_maintenance = input("In maintenance (yes/no): ") == "yes"

rate = rejects / parts

if not in_maintenance and parts >= MIN_PARTS and rate <= MAX_RATE:
    decision = "Lot released"
elif station in CRITICAL:
    decision = "Hold: critical station missed the policy"
else:
    decision = "Hold for one hundred per cent inspection"

print(f"{station} {parts:>5} parts  rate {rate:.2%}  -> {decision}")
```

**Output**

```text
Station: EST-01
Parts in the lot: 1240
Parts rejected: 37
In maintenance (yes/no): no
EST-01  1240 parts  rate 2.98%  -> Lot released

Station: EST-03
Parts in the lot: 1512
Parts rejected: 68
In maintenance (yes/no): no
EST-03  1512 parts  rate 4.50%  -> Hold: critical station missed the policy

Station: EST-04
Parts in the lot: 760
Parts rejected: 9
In maintenance (yes/no): no
EST-04   760 parts  rate 1.18%  -> Lot released

Station: EST-02
Parts in the lot: 420
Parts rejected: 5
In maintenance (yes/no): no
EST-02   420 parts  rate 1.19%  -> Hold for one hundred per cent inspection

Station: EST-01
Parts in the lot: 1240
Parts rejected: 37
In maintenance (yes/no): yes
EST-01  1240 parts  rate 2.98%  -> Hold: critical station missed the policy
```

The fourth case is the one that teaches something: EST-02 has a rate of 1.19 %, better than EST-01, and still gets held. The 420-part lot does not reach the minimum, and without volume the rate means nothing.

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The five decisions are correct | 4 |
| The release rule uses `and` across the three conditions | 2 |
| Membership is asked with `in` over the list of critical stations | 2 |
| The three thresholds are named constants | 1 |
| Comments on the small lot with the good rate | 1 |

**Most common mistake**

Writing `station in "EST-01"` without the brackets. The condition turns into asking whether one string is contained in the other, works by accident on EST-01, and fails silently on anything else.

### 07.3 · Integrate

**Solution**

```python
TEMPERATURE_LIMIT = 68.0
VIBRATION_LIMIT = 4.5

temperature = float(input("Spindle temperature in C: "))
vibration = float(input("Vibration in mm/s: "))

if temperature > TEMPERATURE_LIMIT:
    if vibration > VIBRATION_LIMIT:
        nested = "Stop the station"
    else:
        nested = "Keep running"
else:
    if vibration > VIBRATION_LIMIT:
        nested = "Keep running"
    else:
        nested = "Keep running"

if temperature > TEMPERATURE_LIMIT and vibration > VIBRATION_LIMIT:
    combined = "Stop the station"
else:
    combined = "Keep running"

print(f"{temperature:>5.1f} C  {vibration:>4.1f} mm/s  "
      f"nested: {nested:<18} combined: {combined:<18} "
      f"match: {nested == combined}")
```

This nesting could be collapsed because both inner branches of the outer `else` do exactly the same thing. When that happens, the second question contributes nothing along that path, and the four branches reduce to one condition joined with `and`.

A case from the same cell where the nesting does not collapse: if the station is in maintenance its vibration means nothing and the action is to bring it back online; if it is not, the vibration decides between raising the feed, holding, and stopping. There the inner branches do three different things and the outer branch does a fourth, so the nesting earns something real.

**Output**

```text
Spindle temperature in C: 70.2
Vibration in mm/s: 5.1
 70.2 C   5.1 mm/s  nested: Stop the station   combined: Stop the station   match: True

Spindle temperature in C: 70.2
Vibration in mm/s: 3.8
 70.2 C   3.8 mm/s  nested: Keep running       combined: Keep running       match: True

Spindle temperature in C: 64.0
Vibration in mm/s: 5.1
 64.0 C   5.1 mm/s  nested: Keep running       combined: Keep running       match: True

Spindle temperature in C: 64.0
Vibration in mm/s: 3.8
 64.0 C   3.8 mm/s  nested: Keep running       combined: Keep running       match: True
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The collapsed version is correct and uses a single condition | 3 |
| The four cases match and the check is handed in | 3 |
| Explains that identical inner branches are the signal | 2 |
| Describes a case where the nesting is justified | 2 |

**Most common mistake**

Collapsing with `or` instead of `and`. The four cases stop matching on the second and the third, and the student who never ran the check hands both versions in as equivalent.

---

## Week 08 · Unit 4.5 · Repetition · First midterm

### 08.1 · Recognise

**Solution**

The `for` prints five lines: 38, 42, 46, 50 and 54. The `range` with a step of 4 starts at 38 and stops before 56, so 56 never appears. The last value that fits is 54.

The `while` prints `7 -2.5`. The tank starts at 50.0 litres and each shift takes 7.5, so after six shifts there are 5.0 litres left. The condition asks whether there is more than zero, and 5.0 litres satisfies it, so it enters a seventh pass and subtracts 7.5 again. The counter ends at 7 and the level at -2.5.

Complete shifts the tank really lasts: six. The seventh started and ran out of coolant halfway through, and the negative number is the evidence.

If the line that subtracts the use gets deleted, the condition never changes and the loop never ends. It has to be stopped with Control C.

**Output**

```text
38
42
46
50
54
7 -2.5
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The five lines of the `for` and the count | 3 |
| The `while` output with the negative level | 3 |
| Tells the 7 printed apart from the 6 real complete shifts | 2 |
| Identifies the infinite loop if the subtraction goes | 2 |

**Most common mistake**

Answering that the tank lasts 7 shifts because that is what the program prints. The number is calculated correctly and answers a different question, and the -2.5 sitting next to it is precisely the clue nobody reads.

### 08.2 · Apply

**Solution**

```python
stations = ["EST-01", "EST-02", "EST-03", "EST-04"]
parts = [1240, 984, 1512, 760]
rejects = [37, 12, 68, 9]
energy = [86.4, 61.5, 112.8, 48.2]

total_parts = 0
total_rejects = 0
total_energy = 0.0

print(f"{'Station':<10}{'Parts':>8}{'Rejects':>10}{'kWh/part':>12}")

for i in range(len(stations)):
    rate = rejects[i] / parts[i]
    per_part = energy[i] / parts[i]

    total_parts += parts[i]
    total_rejects += rejects[i]
    total_energy += energy[i]

    print(f"{stations[i]:<10}{parts[i]:>8,}{rate:>10.2%}{per_part:>12.4f}")

cell_rate = total_rejects / total_parts
cell_energy = total_energy / total_parts

print(f"{'CELL C-3':<10}{total_parts:>8,}{cell_rate:>10.2%}{cell_energy:>12.4f}")
```

The cell row divides the sum of rejects by the sum of parts. Averaging the four rates would give 2.47 %, which weights EST-04 with its 760 parts the same as EST-03 with 1512, and that is not what the cell produced.

**Output**

```text
Station      Parts   Rejects    kWh/part
EST-01       1,240     2.98%      0.0697
EST-02         984     1.22%      0.0625
EST-03       1,512     4.50%      0.0746
EST-04         760     1.18%      0.0634
CELL C-3     4,496     2.80%      0.0687
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The four rows and their three figures are correct | 3 |
| The cell row divides sums instead of averaging rates | 3 |
| One single pass, with the three accumulators outside the loop | 2 |
| The loop works unchanged if a fifth station is added | 1 |
| Output aligned in columns | 1 |

**Most common mistake**

Working the cell rate out as the average of the four. It comes to 2.47 % instead of 2.80 %, looks reasonable, and understates the rejects exactly where the volume is.

### 08.3 · Integrate

**Solution**

```python
LOWER_LIMIT = 11.95
UPPER_LIMIT = 12.05

parts = ["BJ-1001", "BJ-1002", "BJ-1003", "BJ-1004",
         "BJ-1005", "BJ-1006", "BJ-1007", "BJ-1008",
         "BJ-1009", "BJ-1010", "BJ-1011", "BJ-1012"]
diameters = [12.01, 11.98, 12.06, 12.00, 11.94, 12.03,
             11.99, 12.05, 11.96, 12.02, 12.08, 11.97]

out_of_band = 0
total = 0.0

for i in range(len(parts)):
    diameter = diameters[i]
    total += diameter

    if diameter > UPPER_LIMIT:
        verdict = "Reject: oversize"
        out_of_band += 1
    elif diameter < LOWER_LIMIT:
        verdict = "Reject: undersize"
        out_of_band += 1
    else:
        verdict = "Accepted"

    print(f"{parts[i]:<9}{diameter:>7.2f}  {verdict}")

average = total / len(diameters)
rate = out_of_band / len(diameters)

print(f"{'Average':<9}{average:>7.4f} mm")
print(f"Out of tolerance: {out_of_band} of {len(diameters)} ({rate:.1%})")
```

Part BJ-1008 measures 12.05, which is exactly the upper limit, and the limit belongs to the band. With `>=` in the first condition, 4 parts would come out of tolerance instead of 3, and the rate for the lot would move from 25.0 % to 33.3 % without a single part changing size.

**Output**

```text
BJ-1001    12.01  Accepted
BJ-1002    11.98  Accepted
BJ-1003    12.06  Reject: oversize
BJ-1004    12.00  Accepted
BJ-1005    11.94  Reject: undersize
BJ-1006    12.03  Accepted
BJ-1007    11.99  Accepted
BJ-1008    12.05  Accepted
BJ-1009    11.96  Accepted
BJ-1010    12.02  Accepted
BJ-1011    12.08  Reject: oversize
BJ-1012    11.97  Accepted
Average  12.0075 mm
Out of tolerance: 3 of 12 (25.0%)
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The twelve verdicts are correct | 3 |
| Average to four decimals and out-of-tolerance count | 3 |
| The accumulator and the counter are declared before the loop | 2 |
| Explains the BJ-1008 case and the effect of switching to `>=` | 2 |

**Most common mistake**

Declaring `total = 0.0` inside the `for`. It ends up holding 11.97, the average comes to 0.9975 mm, and what gives it away is that no bushing in this cell measures one millimetre.

---

## Week 09 · Unit 4.5 · Accumulators, flags and nested loops

### 09.1 · Recognise

**Solution**

The first program prints `48.2`. What was expected is 308.9, the sum of the four energy figures. The line `total = 0.0` sits inside the loop, so every pass wipes what was accumulated and only the last value survives. The single line to move is that one, and it goes before the `for`.

The second program prints `First out of control: EST-03`. The trace of the four passes:

| i | Station | Parts | What happens |
|---|---|---|---|
| 0 | EST-01 | 1240 | Passes the filter. 2.98 % does not clear 3 %, carry on |
| 1 | EST-02 | 984 | Fewer than 1000 parts, the `continue` skips it |
| 2 | EST-03 | 1512 | Passes the filter. 4.50 % does clear it, prints and leaves on `break` |
| 3 | EST-04 | 760 | Never evaluated, the `break` already left the loop |

The `else` on the `for` does not run because the loop left through `break`. It would run if no station with at least 1000 parts cleared 3 %, for instance if EST-03 had closed the shift with 40 rejects instead of 68.

**Output**

```text
48.2
First out of control: EST-03
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| Both outputs correct | 3 |
| Identifies the misplaced line and says where it goes | 2 |
| The trace of the four passes with the `continue` and the `break` | 3 |
| Explains when the `else` on the `for` would run | 2 |

**Most common mistake**

Answering 308.9 on the first program. The intent of the code is being read rather than its indentation, and it is exactly the mistake that produces wrong totals nobody checks.

### 09.2 · Apply

**Solution**

```python
RATE_TARGET = 0.03
ENERGY_TARGET = 0.070

stations = ["EST-01", "EST-02", "EST-03", "EST-04"]
parts = [1240, 984, 1512, 760]
rejects = [37, 12, 68, 9]
energy = [86.4, 61.5, 112.8, 48.2]

total_energy = 0.0
off_target = 0
any_over_target = False

for i in range(len(stations)):
    total_energy += energy[i]

    if rejects[i] / parts[i] > RATE_TARGET:
        off_target += 1

    if energy[i] / parts[i] > ENERGY_TARGET:
        any_over_target = True

print(f"Shift energy:            {total_energy:,.1f} kWh")
print(f"Stations off target:     {off_target}")
print(f"Any above 0.070 kWh:     {any_over_target}")
```

The second question counts cases, not magnitudes: adding the rates would give a number with no physical meaning. The first adds magnitudes: counting stations says nothing about how much energy went out. The flag answers whether at least one exists, and that needs neither counting nor adding.

**Output**

```text
Shift energy:            308.9 kWh
Stations off target:     1
Any above 0.070 kWh:     True
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The three answers are correct | 3 |
| The three variables are declared before the loop | 2 |
| One single pass answers all three questions | 2 |
| Both targets are named constants | 1 |
| Explains the difference between counting and adding | 2 |

**Most common mistake**

Writing the flag as `any_over_target = energy[i] / parts[i] > ENERGY_TARGET` with no `if`. The variable gets overwritten every pass and ends up reflecting only the last station, which on this data is false.

### 09.3 · Integrate

**Solution**

```python
stations = ["EST-01", "EST-02", "EST-03", "EST-04"]
parts_per_hour = [155, 123, 189, 95]
shifts = ["T1", "T2", "T3"]
hours = [8, 8, 6]

total_output = 0
high_pairs = 0

for station_index in range(len(stations)):
    for shift_index in range(len(shifts)):
        projection = parts_per_hour[station_index] * hours[shift_index]
        total_output += projection

        if projection > 1000:
            high_pairs += 1

        print(f"{stations[station_index]:<8}{shifts[shift_index]:<5}{projection:>7,}")

print(f"{'TOTAL':<13}{total_output:>7,}")
print(f"Pairs above 1000 parts: {high_pairs}")
```

Four stations by three shifts is twelve rows, and that count gets written down before the program runs. With 40 stations and 3 shifts it would be 120 passes, which is still nothing. The trouble starts when both loops walk long lists: 1000 by 1000 is a million passes, and that is where a nesting stops being free.

**Output**

```text
EST-01  T1     1,240
EST-01  T2     1,240
EST-01  T3       930
EST-02  T1       984
EST-02  T2       984
EST-02  T3       738
EST-03  T1     1,512
EST-03  T2     1,512
EST-03  T3     1,134
EST-04  T1       760
EST-04  T2       760
EST-04  T3       570
TOTAL         12,364
Pairs above 1000 parts: 5
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The twelve rows with the right projection | 3 |
| The total and the count of high pairings | 3 |
| The two loop variables carry different names and say what they walk | 2 |
| Predicts the twelve rows before running the program | 1 |
| Answers how the passes grow, with an example | 1 |

**Most common mistake**

Using `i` in both loops. The inner one overwrites the outer, repeated rows of the last station come out, and the total falls apart without Python flagging anything.

---

## Week 10 · Unit 5 · User-defined functions

### 10.1 · Recognise

**Solution**

The first line prints `None`. The function works out the division and does not return it, so it hands back the value Python returns by default when there is no `return`. The second prints `69.6774193548387`, which is the energy per part in watt hours. The third raises `NameError`.

`reject_rate` is missing its `return`. The error does not surface inside the function because nothing in there is written wrongly: it surfaces later, the moment somebody tries to multiply, compare or format that `None`.

The third line fails because `per_unit` was born inside the function and disappeared when the function ended. Outside it, that name does not exist.

If the second function had `print(per_unit)` instead of `return per_unit`, the number would appear on screen and the function would hand back `None`. The value could not be stored, added, or put into a table.

**Output**

```text
None
69.6774193548387
Traceback (most recent call last):
  File "w10_1.py", line 12, in <module>
    print(per_unit)
          ^^^^^^^^
NameError: name 'per_unit' is not defined
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The three answers correct, with the `NameError` named | 4 |
| Explains the missing `return` and where the `None` detonates | 2 |
| Explains the local scope of `per_unit` | 2 |
| Tells returning apart from printing | 2 |

**Most common mistake**

Answering `0.02983` on the first line. The assumption is that a function which calculates something hands it back, and that assumption is what produces the `None` blowing up three lines further down.

### 10.2 · Apply

**Solution**

```python
LOWER_LIMIT = 11.95
UPPER_LIMIT = 12.05


def reject_rate(parts, rejects):
    """Returns the fraction of parts rejected in a lot."""
    return rejects / parts


def in_tolerance(diameter):
    """Says whether a measured diameter falls in the 11.95 to 12.05 mm band."""
    return diameter >= LOWER_LIMIT and diameter <= UPPER_LIMIT


print(round(reject_rate(1240, 37), 4))
print(round(reject_rate(1512, 68), 4))
print(round(reject_rate(760, 0), 4))

print(in_tolerance(12.00))
print(in_tolerance(12.05))
print(in_tolerance(12.06))
```

The 12.05 case is the one that always has to be tested because it is the boundary, and it is where the question of whether the limit belongs to the band gets decided. With `<` instead of `<=` that part would come out of tolerance, and the function would go on giving correct results on every other value.

**Output**

```text
0.0298
0.045
0.0
True
True
False
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| Both functions return and neither one prints | 3 |
| The six calls give the right result | 3 |
| Each function carries a one-line docstring | 2 |
| Explains why the exact boundary value gets tested | 2 |

**Most common mistake**

Putting the `print` inside `in_tolerance`. The function looks like it works on screen and is useless for counting how many parts pass, which is exactly what the next exercise asks for.

### 10.3 · Integrate

**Solution**

```python
LOWER_LIMIT = 11.95
UPPER_LIMIT = 12.05


def in_tolerance(diameter):
    """Says whether a measured diameter falls inside the tolerance band."""
    return diameter >= LOWER_LIMIT and diameter <= UPPER_LIMIT


def verdict(diameter):
    """Returns where the part goes: accepted, rework or scrap."""
    if in_tolerance(diameter):
        return "Accepted"
    if diameter > UPPER_LIMIT:
        return "Rework"
    return "Scrap"


def accepted_parts(diameters):
    """Counts how many readings in the list fall inside tolerance."""
    accepted = 0

    for diameter in diameters:
        if in_tolerance(diameter):
            accepted += 1

    return accepted


def average_diameter(diameters):
    """Returns the average of the list of readings."""
    total = 0.0

    for diameter in diameters:
        total += diameter

    return total / len(diameters)


parts = ["BJ-1001", "BJ-1002", "BJ-1003", "BJ-1004",
         "BJ-1005", "BJ-1006", "BJ-1007", "BJ-1008",
         "BJ-1009", "BJ-1010", "BJ-1011", "BJ-1012"]
diameters = [12.01, 11.98, 12.06, 12.00, 11.94, 12.03,
             11.99, 12.05, 11.96, 12.02, 12.08, 11.97]

for i in range(len(parts)):
    print(f"{parts[i]:<9}{diameters[i]:>7.2f}  {verdict(diameters[i])}")

print(f"Measured: {len(diameters)}")
print(f"Accepted: {accepted_parts(diameters)}")
print(f"Average:  {average_diameter(diameters):.4f} mm")
```

The test of deleting the lower-limit comparison from `in_tolerance`: part BJ-1005, at 11.94 mm, would start coming out accepted and the count would climb from 9 to 10. The tests that catch it are the ones using a value below the band; if the student only tried 12.00, 12.05 and 12.06, none of them catches it and the 11.94 case has to be added.

**Output**

```text
BJ-1001    12.01  Accepted
BJ-1002    11.98  Accepted
BJ-1003    12.06  Rework
BJ-1004    12.00  Accepted
BJ-1005    11.94  Scrap
BJ-1006    12.03  Accepted
BJ-1007    11.99  Accepted
BJ-1008    12.05  Accepted
BJ-1009    11.96  Accepted
BJ-1010    12.02  Accepted
BJ-1011    12.08  Rework
BJ-1012    11.97  Accepted
Measured: 12
Accepted: 9
Average:  12.0075 mm
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The four functions carry a docstring and none of them prints | 3 |
| `verdict` calls `in_tolerance` instead of repeating the comparison | 2 |
| The twelve rows and the three closing figures are correct | 3 |
| The delete-a-line test with the case that catches it | 2 |

**Most common mistake**

Repeating the band comparison inside `verdict` rather than calling the function. The program works the same, and when engineering changes the tolerance somebody has to remember both places.

---

## Week 11 · Unit 5 · Arguments, built-in functions and modules

### 11.1 · Recognise

**Solution**

```text
69.68
0.35
74.68
```

In the first call nothing optional gets passed: `factor` holds 1000 and `losses` holds 0.0. That is the energy per part in watt hours.

In the second, the 5.0 landed in `factor`, because positional arguments fill the slots in order and `factor` is the one that comes after `parts`. The function worked out 86.4 times 5 over 1240, which means nothing at all. Python flags no error because it received three valid arguments for three parameters that exist.

In the third, the 5.0 goes by keyword into `losses`, skips `factor`, and the result is the earlier 69.68 plus the losses.

If `factor=1000` were moved ahead of `parts`, the file would not even run: a parameter with a default value cannot sit before one without it, and Python rejects it with `SyntaxError` while reading it.

**Output**

```text
69.6774193548387
0.34838709677419355
74.6774193548387
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The three numbers are correct | 4 |
| Identifies that the 5.0 landed in `factor` on the second call | 2 |
| Explains why Python flags no error | 2 |
| Answers that moving the optional to the front is a `SyntaxError` | 2 |

**Most common mistake**

Answering that the second call adds 5.0 to the result. The 5.0 is read as though it were the losses because that is the only optional visible in the third call, and the order of the parameters never gets checked.

### 11.2 · Apply

**Solution**

```python
def out_of_tolerance(diameter, nominal=12.00, tolerance=0.05):
    """Says whether a reading falls outside the nominal plus or minus tolerance band."""
    lower = nominal - tolerance
    upper = nominal + tolerance

    return diameter < lower or diameter > upper


print(out_of_tolerance(12.06))
print(out_of_tolerance(12.05))
print(out_of_tolerance(12.06, 12.00, 0.10))
print(out_of_tolerance(12.06, tolerance=0.10))
print(out_of_tolerance(8.02, nominal=8.00))

print(12.00 - 0.05 == 11.95)
print(12.00 + 0.05 == 12.05)
```

Both closing checks come out true, so in this case the calculated limits match the ones on the drawing. The check is not wasted: with another tolerance the result can differ, as week 4 showed with 0.05 times 3. When a function works boundaries out from decimals, the boundary gets tested before anyone trusts it.

**Output**

```text
True
False
False
False
False
True
True
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The function carries both optional parameters last, plus its docstring | 2 |
| The five calls give the right result | 4 |
| One call passes the tolerance by keyword, skipping the nominal | 2 |
| Both boundary checks appear and get commented on | 2 |

**Most common mistake**

Writing `out_of_tolerance(12.06, 0.10)` meaning to open the tolerance. The 0.10 lands in `nominal`, the function compares against a band of 0.05 to 0.15 mm, and returns true for the wrong reason.

### 11.3 · Integrate

**Solution**

```python
from statistics import mean, median, pstdev

LOWER_LIMIT = 11.95
UPPER_LIMIT = 12.05

diameters = [12.01, 11.98, 12.06, 12.00, 11.94, 12.03,
             11.99, 12.05, 11.96, 12.02, 12.08, 11.97]

with_outlier = [12.01, 11.98, 12.06, 12.00, 11.94, 12.03,
                11.99, 12.05, 11.96, 12.02, 12.08, 11.97, 12.90]

print(f"Readings:  {len(diameters)}")
print(f"Average:   {mean(diameters):.4f} mm")
print(f"Median:    {median(diameters):.4f} mm")
print(f"Spread:    {pstdev(diameters):.4f} mm")
print(f"Lowest:    {sorted(diameters)[0]:.2f} mm")
print(f"Highest:   {max(diameters):.2f} mm")

cp = (UPPER_LIMIT - LOWER_LIMIT) / (6 * pstdev(diameters))
print(f"Cp:        {round(cp, 3)}")

print(f"Average with the 12.90 reading: {mean(with_outlier):.4f} mm")
print(f"Median with the 12.90 reading:  {median(with_outlier):.4f} mm")
```

The third function is `pstdev`, the population standard deviation, documented on the `statistics` module page at docs.python.org. It takes a series of numeric data and returns the standard deviation of that series taken as a complete population rather than as a sample.

A capability index of 0.41 means the variation of the process is wider than the tolerance band. The band measures 0.10 mm and six standard deviations measure 0.24 mm, so even perfectly centred the process would keep producing parts outside. The production manager is not asked to adjust the centring: the report says the machine does not hold the tolerance the drawing calls for, and that the spread is what has to be attacked.

With the 12.90 mm reading the average jumps from 12.0075 to 12.0762 and the median only moves from 12.0050 to 12.0100. When a reading is suspect, the median is the one to report.

**Output**

```text
Readings:  12
Average:   12.0075 mm
Median:    12.0050 mm
Spread:    0.0406 mm
Lowest:    11.94 mm
Highest:   12.08 mm
Cp:        0.41
Average with the 12.90 reading: 12.0762 mm
Median with the 12.90 reading:  12.0100 mm
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The three imports and the seven figures are correct | 3 |
| The third function comes from the documentation and is cited | 2 |
| The capability index is correct and gets interpreted | 3 |
| Compares average and median with the outlier and picks one | 2 |

**Most common mistake**

Reporting the capability index as though it were a percentage of good parts. 0.41 is not 41 %, it is a ratio between the width of the tolerance and the width of the spread, and confusing them turns a serious alert into a number that sounds tolerable.

---

## Week 12 · Unit 6 · Lists and tuples

### 12.1 · Recognise

**Solution**

```text
12.01 11.94
[11.98, 12.06]
[11.94, 11.98, 12.0, 12.01, 12.06]
[12.01, 11.98, 12.06, 12.0, 11.94]
None
[11.94, 11.98, 12.0, 12.01, 12.06]
6 5
```

The last line raises `IndexError`. The list holds six elements after the `append`, so the last valid index is 5.

`diameters[1:3]` returns two values because the first index is included and the second is not. That is what makes the size of a slice the difference between the two numbers.

`backup` and `copy` end up different because `backup = diameters` copied nothing: it created a second name for the same list, and the `append` changed it. `copy = diameters.copy()` did build a new list, which never heard about the change.

With `diameters = diameters.sort()`, the method sorts the list and returns `None`, and that assignment leaves the name `diameters` pointing at `None`. The data is gone and the error turns up later, on the next line that tries to use it.

**Output**

```text
12.01 11.94
[11.98, 12.06]
[11.94, 11.98, 12.0, 12.01, 12.06]
[12.01, 11.98, 12.06, 12.0, 11.94]
None
[11.94, 11.98, 12.0, 12.01, 12.06]
6 5
Traceback (most recent call last):
  File "w12_1.py", line 17, in <module>
    print(diameters[6])
          ~~~~~~~~~^^^
IndexError: list index out of range
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The seven lines correct and the closing `IndexError` | 4 |
| Explains the slice rule with the second index excluded | 2 |
| Explains alias against copy and why they give 6 and 5 | 2 |
| Explains what happens with `diameters = diameters.sort()` | 2 |

**Most common mistake**

Answering `[11.98, 12.06, 12.0]` on the second line. Three positions get counted because three minus one is two and the student adds the endpoint, and checking that the length is always the difference between the two indices settles it.

### 12.2 · Apply

**Solution**

```python
diameters = [12.01, 11.98, 12.06, 12.00, 11.94, 12.03,
             11.99, 12.05, 11.96, 12.02, 12.08, 11.97]

print("At the start:", diameters)

highest = max(diameters)
lowest = min(diameters)
top_three = sorted(diameters, reverse=True)[0:3]
position = diameters.index(11.94)

print(f"Highest:            {highest:.2f} mm")
print(f"Lowest:             {lowest:.2f} mm")
print(f"Top three:          {top_three}")
print(f"Position of 11.94:  {position}")
print(f"Part it belongs to: BJ-{1001 + position}")
print(f"Last three:         {diameters[9:12]}")

print("At the end:", diameters)
```

The ordering is asked for with `sorted` and its keyword argument `reverse`, which is week 11 applied here. With the `sort` method the original list would come out ordered and the exercise asks for the opposite.

Position 4 corresponds to the fifth part, BJ-1005, because the part numbers start at BJ-1001 and the index starts at 0.

**Output**

```text
At the start: [12.01, 11.98, 12.06, 12.0, 11.94, 12.03, 11.99, 12.05, 11.96, 12.02, 12.08, 11.97]
Highest:            12.08 mm
Lowest:             11.94 mm
Top three:          [12.08, 12.06, 12.05]
Position of 11.94:  4
Part it belongs to: BJ-1005
Last three:         [12.02, 12.08, 11.97]
At the end: [12.01, 11.98, 12.06, 12.0, 11.94, 12.03, 11.99, 12.05, 11.96, 12.02, 12.08, 11.97]
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The four answers are correct | 4 |
| The list comes out identical at the start and at the end | 3 |
| The part number is worked out from the position, not looked up by hand | 2 |
| Uses `sorted` and not the `sort` method | 1 |

**Most common mistake**

Answering BJ-1004 for the 11.94 reading. The index gets added to the starting number without noticing that position 4 is the fifth part, and the result lands one off.

### 12.3 · Integrate

**Solution**

```python
BAND = (12.00, 11.95, 12.05)

diameters = [12.01, 11.98, 12.06, 12.00, 11.94, 12.03,
             11.99, 12.05, 11.96, 12.02, 12.08, 11.97]

out_of_band = []

for diameter in diameters:
    if diameter < BAND[1] or diameter > BAND[2]:
        out_of_band.append(diameter)

sorted_out = sorted(out_of_band, reverse=True)

print(f"Nominal {BAND[0]:.2f} mm, band from {BAND[1]:.2f} to {BAND[2]:.2f} mm")
print(f"Readings:    {len(diameters)}")
print(f"Out of band: {len(out_of_band)}")
print(f"Out of band, highest first: {sorted_out}")
print(f"Original untouched: {diameters}")

BAND[2] = 12.10
```

The band goes in a tuple because those are the values from the drawing and they must not change while the program runs. In a list, any line could modify it by accident and the program would carry on with a tolerance different from the one on the print. The attempted assignment fails immediately and with a clear message, which is exactly what a constant is for.

**Output**

```text
Nominal 12.00 mm, band from 11.95 to 12.05 mm
Readings:    12
Out of band: 3
Out of band, highest first: [12.08, 12.06, 11.94]
Original untouched: [12.01, 11.98, 12.06, 12.0, 11.94, 12.03, 11.99, 12.05, 11.96, 12.02, 12.08, 11.97]
Traceback (most recent call last):
  File "w12_3.py", line 20, in <module>
    BAND[2] = 12.10
    ~~~~^^^
TypeError: 'tuple' object does not support item assignment
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The new list holds exactly the three that fall outside | 3 |
| The original list keeps its order and its contents | 2 |
| The descending order is obtained without destroying anything | 2 |
| The tuple error is pasted in full | 1 |
| Argues why the band goes in a tuple | 2 |

**Most common mistake**

Writing `out_of_band = diameters` and then removing the parts that do pass. There are not two lists, there are two names for the same one, and the line printing the original at the end gives it away.

---

## Week 13 · Unit 6 · Sets and dictionaries · Second midterm

### 13.1 · Recognise

**Solution**

```text
4
Roughness above Ra 1.6
None
Code not in the catalogue
3
['D02', 'D03']
['D01']
['D01', 'D05']
```

The last line raises `KeyError` on the key `D09`.

The dictionary ends with four entries because `defects["D02"] = ...` adds nothing: the key already existed and its value got overwritten. `defects["D04"] = ...` does add a new entry. Three plus one is four.

`shift_a` holds three elements because a set keeps no duplicates: the `D01` appearing twice counts once. That is the difference from the list it came from.

**Output**

```text
4
Roughness above Ra 1.6
None
Code not in the catalogue
3
['D02', 'D03']
['D01']
['D01', 'D05']
Traceback (most recent call last):
  File "w13_1.py", line 20, in <module>
    print(defects["D09"])
          ~~~~~~~^^^^^^^
KeyError: 'D09'
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The eight lines are correct | 4 |
| The `KeyError` on the last line, named | 2 |
| Explains why the dictionary settles at four entries | 2 |
| Explains why the set settles at three elements | 2 |

**Most common mistake**

Answering 5 on the first line. The two assignments get counted as two new entries, without noticing that D02 was already there and that a key never repeats.

### 13.2 · Apply

**Solution**

```python
defects = {"D01": "Diameter out of tolerance",
           "D02": "Roughness above Ra 1.6",
           "D03": "Burr on the chamfer",
           "D04": "Ding on the front face",
           "D05": "Concentricity out of spec",
           "D06": "Tool mark"}

reported = ["D01", "D03", "D01", "D05", "D01", "D02", "D03", "D09"]

print("Defect catalogue")
for code, description in defects.items():
    print(f"  {code}  {description}")

print(f"Codes in the catalogue: {len(defects)}")
print(f"Parts reported:         {len(reported)}")
print(f"Distinct codes:         {len(set(reported))}")

for code in sorted(set(reported)):
    print(f"  {code}  {defects.get(code, 'Code not in the catalogue')}")
```

D09 is not in the catalogue, and with square brackets the program would have stopped there. With `get` and its default value the report comes out complete and also shows that somebody is capturing a code that does not exist, which is useful information for the area.

**Output**

```text
Defect catalogue
  D01  Diameter out of tolerance
  D02  Roughness above Ra 1.6
  D03  Burr on the chamfer
  D04  Ding on the front face
  D05  Concentricity out of spec
  D06  Tool mark
Codes in the catalogue: 6
Parts reported:         8
Distinct codes:         5
  D01  Diameter out of tolerance
  D02  Roughness above Ra 1.6
  D03  Burr on the chamfer
  D05  Concentricity out of spec
  D09  Code not in the catalogue
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The catalogue is walked with `items` and comes out complete | 2 |
| The three figures are correct | 3 |
| The lookup uses `get` with a default value | 3 |
| D09 appears in the report without stopping the program | 2 |

**Most common mistake**

Counting the distinct codes with `len(reported)`. It gives 8 instead of 5, and it confuses how many parts were reported with how many kinds of defect there are.

### 13.3 · Integrate

**Solution**

```python
stations = ["EST-01", "EST-02", "EST-03", "EST-04"]
energy = [86.4, 61.5, 112.8, 48.2]
parts = [1240, 984, 1512, 760]

reported_a = ["D01", "D03", "D01", "D05", "D01", "D02", "D03"]
reported_b = ["D02", "D02", "D06", "D03", "D01"]

energy_by_station = {}
for i in range(len(stations)):
    energy_by_station[stations[i]] = energy[i]

counts = {}
for code in reported_a:
    counts[code] = counts.get(code, 0) + 1

print("Energy by station")
for station, kwh in energy_by_station.items():
    print(f"  {station}  {kwh:>6.1f} kWh")

print(f"Cell total: {sum(energy_by_station.values()):.1f} kWh")

hungriest = ""
highest = 0.0
for station, kwh in energy_by_station.items():
    if kwh > highest:
        highest = kwh
        hungriest = station

print(f"Hungriest station: {hungriest} with {highest:.1f} kWh")

print("Shift A defects")
for code in sorted(counts):
    print(f"  {code}  {counts[code]}")

codes_a = set(reported_a)
codes_b = set(reported_b)

print(f"In both shifts:      {sorted(codes_a & codes_b)}")
print(f"Only in shift A:     {sorted(codes_a - codes_b)}")
print(f"New in shift B:      {sorted(codes_b - codes_a)}")
print(f"In one but not both: {sorted(codes_a ^ codes_b)}")
```

The new code in shift B is D06, tool mark, and that is the one triggering a maintenance action: a tool mark that was not there the shift before points at a worn or badly seated insert, and it gets checked before production carries on.

The shift A count could not have been done with a set because a set drops the repeats, and what was wanted was precisely how many times each code repeated. The set answers which ones there are, the dictionary answers how many of each.

**Output**

```text
Energy by station
  EST-01    86.4 kWh
  EST-02    61.5 kWh
  EST-03   112.8 kWh
  EST-04    48.2 kWh
Cell total: 308.9 kWh
Hungriest station: EST-03 with 112.8 kWh
Shift A defects
  D01  3
  D02  1
  D03  2
  D05  1
In both shifts:      ['D01', 'D02', 'D03']
Only in shift A:     ['D05']
New in shift B:      ['D06']
In one but not both: ['D05', 'D06']
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The dictionary is built with a loop from the lists | 2 |
| The total comes from `values` and the hungriest station from a walk | 2 |
| The counter uses `get` with a default of zero | 2 |
| The four comparisons use set operations | 2 |
| Both conclusions are written | 2 |

**Most common mistake**

Comparing the two shifts with a loop and an `if` instead of set operations. The result comes out the same, takes fifteen lines, and falls apart the moment the fourth question has to be answered, the one about codes in one but not in both.

---

## Week 14 · Unit 7 · Text and CSV files

### 14.1 · Recognise

**Solution**

```text
30
EST-01 12.01
<class 'str'>
12.0111.98
True
False
```

The fourth line raises no error because both values are text and `+` between two strings glues them together. The result, `12.0111.98`, is not a number and the program carries on anyway. That is the most expensive conversion mistake of the term: it does not warn you.

The sixth line comes out false because the third row of the file carries the station written as `" EST-01"`, with a space in front. Two strings that look the same on screen and differ by one character are different values, and that is why a grouping by station would report nine stations where there are four.

If that same open call carried `"w"`, the file would be emptied the instant it opened, before anything was read. The thirty rows would be gone and the program would then fail trying to read a file opened for writing.

**Output**

```text
30
EST-01 12.01
<class 'str'>
12.0111.98
True
False
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The six lines are correct | 4 |
| Explains why adding two strings raises no error | 2 |
| Spots the leading space on the third row | 2 |
| Explains what the `"w"` mode does to the file | 2 |

**Most common mistake**

Answering `23.99` on the fourth line. The two diameters get added as though `DictReader` had converted the types, when a CSV holds only text and nobody else is going to convert it for you.

### 14.2 · Apply

**Solution**

```python
import csv
from pathlib import Path

DATA = Path(__file__).resolve().parent


def to_decimal(text):
    """Converts to decimal, dropping the thousands comma and the kJ unit."""
    clean = text.replace(",", "").replace("kJ", "")
    return float(clean.strip())


def to_integer(text):
    """Converts to integer. An empty cell is reported as missing, with None."""
    text = text.strip()
    return int(text) if text else None


def normalise(text):
    """Leaves one single way of writing the station: no spaces, upper case."""
    return text.strip().upper()


with (DATA / "measurements.csv").open(encoding="utf-8") as f:
    rows = list(csv.DictReader(f))

spellings = set()
no_cycle = 0

for row in rows:
    spellings.add(row["station"])
    if to_integer(row["cycle_s"]) is None:
        no_cycle += 1

normalised = set()
for row in rows:
    normalised.add(normalise(row["station"]))

print(f"Rows read:                   {len(rows)}")
print(f"Rows with no cycle time:     {no_cycle}")
print(f"Ways of writing the station: {len(spellings)}")
print(f"Stations after normalising:  {len(normalised)}")

energy = {}
measured = {}
diameter_total = {}

for row in rows:
    station = normalise(row["station"])
    energy[station] = energy.get(station, 0.0) + to_decimal(row["energy_kj"])
    measured[station] = measured.get(station, 0) + 1
    diameter_total[station] = diameter_total.get(station, 0.0) + float(row["diameter_mm"])

print(f"{'Station':<10}{'Parts':>8}{'Energy kJ':>13}{'Diameter':>11}")

energy_total = 0.0
measured_total = 0

for station in sorted(energy):
    average = diameter_total[station] / measured[station]
    energy_total += energy[station]
    measured_total += measured[station]
    print(f"{station:<10}{measured[station]:>8}{energy[station]:>13,.0f}{average:>11.4f}")

print(f"{'CELL C-3':<10}{measured_total:>8}{energy_total:>13,.0f}")
```

`to_integer` returns `None` and not zero, because a cycle time that was never captured is not a cycle of zero seconds. What to do about that absence gets decided in the next exercise, not here.

The dictionaries with `get` and a default value are week 13 applied: each station shows up for the first time without the program having to know in advance how many there are.

**Output**

```text
Rows read:                   30
Rows with no cycle time:     3
Ways of writing the station: 9
Stations after normalising:  4
Station      Parts    Energy kJ   Diameter
EST-01           9       11,325    12.0022
EST-02           7        7,060    12.0071
EST-03           8       12,125    12.0100
EST-04           6        4,467    12.0083
CELL C-3        30       34,977
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The three functions carry a docstring and one responsibility each | 3 |
| The four diagnostic lines are correct | 2 |
| The table by station and the cell total are correct | 3 |
| The path is built with `pathlib` from the location of the file | 1 |
| Reads by column name, not by position | 1 |

**Most common mistake**

Converting the energy with a plain `float(row["energy_kj"])`. It raises `ValueError` on the first row because of the comma and the unit, and the student usually blames the file instead of the format.

### 14.3 · Integrate

**Solution**

```python
import csv
from pathlib import Path

DATA = Path(__file__).resolve().parent
LOWER_LIMIT = 11.95
UPPER_LIMIT = 12.05


def to_decimal(text):
    """Converts to decimal, dropping the thousands comma and the kJ unit."""
    clean = text.replace(",", "").replace("kJ", "")
    return float(clean.strip())


def normalise(text):
    """Leaves one single way of writing the station: no spaces, upper case."""
    return text.strip().upper()


def out_of_tolerance(diameter):
    """Says whether the reading falls outside the 11.95 to 12.05 mm band."""
    return diameter < LOWER_LIMIT or diameter > UPPER_LIMIT


with (DATA / "measurements.csv").open(encoding="utf-8") as f:
    rows = list(csv.DictReader(f))

seen = set()
clean_rows = []

for row in rows:
    fingerprint = (row["date"], row["station"], row["lot"],
                   row["diameter_mm"], row["cycle_s"], row["energy_kj"])

    if fingerprint in seen:
        continue

    seen.add(fingerprint)
    clean_rows.append(row)

energy = {}
measured = {}
out_of_band = {}
no_cycle = 0

for row in clean_rows:
    station = normalise(row["station"])
    diameter = float(row["diameter_mm"])

    energy[station] = energy.get(station, 0.0) + to_decimal(row["energy_kj"])
    measured[station] = measured.get(station, 0) + 1
    out_of_band[station] = out_of_band.get(station, 0)

    if out_of_tolerance(diameter):
        out_of_band[station] += 1

    if row["cycle_s"].strip() == "":
        no_cycle += 1

print(f"Rows in the file:             {len(rows)}")
print(f"Exact duplicates removed:     {len(rows) - len(clean_rows)}")
print(f"Rows left:                    {len(clean_rows)}")
print(f"Rows with no cycle time kept: {no_cycle}")
print(f"Parts out of tolerance:       {sum(out_of_band.values())}")
print(f"Cell energy:                  {sum(energy.values()):,.0f} kJ")

output = DATA / "station_summary.csv"

with output.open("w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["station", "parts", "out_of_tolerance", "energy_kj"])

    for station in sorted(energy):
        writer.writerow([station, measured[station], out_of_band[station],
                         round(energy[station], 1)])

print(f"File written: {output.name}")

with output.open(encoding="utf-8") as f:
    print(f.read().strip())
```

The fingerprint of a row is a tuple of the six columns, and the set of fingerprints is what catches the exact duplicate. Comparing only by date and station would have deleted legitimate measurements of different parts from the same shift.

The 2,515 kJ of difference is the sum of the two duplicated rows: 1,260 from the EST-01 row of 9 January and 1,255 from the EST-01 row of 12 January. A duplicate inflates the total because the energy gets added twice, and it barely moves the average diameter because there the repeated value enters the numerator and the denominator at once.

**Output**

```text
Rows in the file:             30
Exact duplicates removed:     2
Rows left:                    28
Rows with no cycle time kept: 3
Parts out of tolerance:       8
Cell energy:                  32,462 kJ
File written: station_summary.csv
station,parts,out_of_tolerance,energy_kj
EST-01,7,3,8810.0
EST-02,7,1,7060.0
EST-03,8,4,12125.0
EST-04,6,0,4467.0
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| Duplicates are detected by comparing the whole row | 2 |
| The six log figures are correct | 3 |
| The output file carries the header and the four rows asked for | 2 |
| It gets written with an empty `newline` and no blank rows | 1 |
| Explains the exact 2,515 kJ difference | 2 |

**Most common mistake**

Detecting duplicates by date and station only. Measurements of different parts get deleted, the count drops from 28 to 18, and the energy total lands far below where it should with nothing to flag it.

---

## Week 15 · Unit 8.1 · Series, DataFrame, cleaning and grouping

### 15.1 · Recognise

**Solution**

`shape` gives `(30, 6)`. The types: `date`, `station`, `lot` and `energy_kj` come out as text, `diameter_mm` and `cycle_s` come out `float64`. There are 3 missing values in `cycle_s`, 2 duplicated rows and 9 distinct ways of writing the station.

`cycle_s` came out decimal and not integer because three cells are empty, and the marker for a missing value only exists in a decimal column. That is not a failing in pandas: it is the price of a column with holes, and it is why the times print as 44.0 instead of 44.

`energy_kj` came out as text because the thousands comma and the unit are formatting, not value. While they sit there, that column cannot be summed.

In `value_counts` two rows look identical, `EST-01` and `EST-01 `, and they are separate entries because one carries a trailing space. That space is invisible on screen and it does split the groups.

`describe` only summarises `diameter_mm` and `cycle_s`, the two numeric columns. The other four are text as far as pandas is concerned, the date included, and that is why they stay out.

**Output**

```text
(30, 6)
date               str
station            str
lot                str
diameter_mm    float64
cycle_s        float64
energy_kj          str
dtype: object
3
2
9
station
EST-03     7
EST-01     6
EST-02     6
EST-04     6
 EST-01    1
est-01     1
EST-01     1
est-02     1
EST-03     1
Name: count, dtype: int64
count    30.000
mean     12.007
std       0.046
min      11.910
25%      11.972
50%      12.010
75%      12.040
max      12.090
Name: diameter_mm, dtype: float64
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The seven outputs correct, with the types of the six columns | 3 |
| Explains the `float64` on `cycle_s` through the missing values | 2 |
| Explains the text on `energy_kj` through the comma and the unit | 2 |
| Spots the two rows that look the same in `value_counts` | 2 |
| Says which columns `describe` summarises and why | 1 |

**Most common mistake**

Saying `cycle_s` came out decimal because the times carry decimals. Every time in the file is a whole number, and whoever does not check `isna` never finds out the cause is the three empty cells.

### 15.2 · Apply

**Solution**

```python
import pandas as pd
from pathlib import Path

DATA = Path(__file__).resolve().parent
LOWER_LIMIT = 11.95
UPPER_LIMIT = 12.05

measurements = pd.read_csv(DATA / "measurements.csv")

print(f"On loading:               {len(measurements)} rows")
print(f"Exact duplicates:         {measurements.duplicated().sum()}")
print(f"Ways of writing station:  {measurements['station'].nunique()}")
print(f"No cycle time:            {measurements['cycle_s'].isna().sum()}")

measurements = measurements.drop_duplicates()
print(f"Without duplicates:       {len(measurements)} rows")

measurements["station"] = measurements["station"].str.strip().str.upper()
print(f"Real stations:            {measurements['station'].nunique()}")

measurements["energy_kj"] = (measurements["energy_kj"]
                             .str.replace(",", "", regex=False)
                             .str.replace("kJ", "", regex=False)
                             .str.strip()
                             .astype(float))

measurements["date"] = pd.to_datetime(measurements["date"])

print(measurements.dtypes)

measurements["verdict"] = "In tolerance"
measurements.loc[(measurements["diameter_mm"] < LOWER_LIMIT) |
                 (measurements["diameter_mm"] > UPPER_LIMIT),
                 "verdict"] = "Out of tolerance"

print(measurements["verdict"].value_counts())

critical = measurements[(measurements["station"] == "EST-03") &
                        (measurements["verdict"] == "Out of tolerance")]
print(f"EST-03 out of tolerance:  {len(critical)}")

first_two = measurements[measurements["station"].isin(["EST-01", "EST-02"])]
print(f"Parts from EST-01 and EST-02: {len(first_two)}")

print(f"Total energy:             {measurements['energy_kj'].sum():,.0f} kJ")
print(f"Average cycle:            {measurements['cycle_s'].mean():.2f} s")
print(f"Rows left if the three without cycle time go: "
      f"{len(measurements.dropna(subset=['cycle_s']))}")
```

Discarding the three rows with no cycle time would leave 25 measurements. Keeping them is the better call because the value deciding whether a part is any good is the diameter, and that one was measured in all three cases. Throwing them out would cost three good diameters in order not to lose three cycle times, and the average cycle can be worked out from the 25 that do carry it without deleting anything.

**Output**

```text
On loading:               30 rows
Exact duplicates:         2
Ways of writing station:  9
No cycle time:            3
Without duplicates:       28 rows
Real stations:            4
date           datetime64[us]
station                   str
lot                       str
diameter_mm           float64
cycle_s               float64
energy_kj             float64
dtype: object
verdict
In tolerance        20
Out of tolerance     8
Name: count, dtype: int64
EST-03 out of tolerance:  4
Parts from EST-01 and EST-02: 14
Total energy:             32,462 kJ
Average cycle:            44.36 s
Rows left if the three without cycle time go: 25
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The six log figures are correct | 3 |
| The four repairs applied in order and the closing types correct | 2 |
| The `verdict` column is written with `loc` in a single step | 2 |
| The three filters give 4, 14 and the right totals | 2 |
| Justifies in writing the decision on the rows with no cycle time | 1 |

**Most common mistake**

Writing the column with `measurements[measurements[...]]["verdict"] = ...`. Chained assignment does nothing, the column stays entirely on «In tolerance», and the count comes out 28 and 0 without a single error being raised.

### 15.3 · Integrate

**Solution**

```python
import pandas as pd
from pathlib import Path

DATA = Path(__file__).resolve().parent
LOWER_LIMIT = 11.95
UPPER_LIMIT = 12.05


def load_clean():
    """Loads measurements.csv and applies the four repairs from session 15.2."""
    data = pd.read_csv(DATA / "measurements.csv").drop_duplicates()

    data["station"] = data["station"].str.strip().str.upper()
    data["energy_kj"] = (data["energy_kj"]
                         .str.replace(",", "", regex=False)
                         .str.replace("kJ", "", regex=False)
                         .str.strip()
                         .astype(float))
    data["date"] = pd.to_datetime(data["date"])

    data["verdict"] = "In tolerance"
    data.loc[(data["diameter_mm"] < LOWER_LIMIT) |
             (data["diameter_mm"] > UPPER_LIMIT),
             "verdict"] = "Out of tolerance"

    return data


measurements = load_clean()

board = measurements.groupby("station").agg(
    parts=("diameter_mm", "count"),
    energy=("energy_kj", "sum"),
    cycle=("cycle_s", "mean"),
    diameter=("diameter_mm", "mean"),
).round(3)

print(board.sort_values("energy", ascending=False))

out = measurements[measurements["verdict"] == "Out of tolerance"]
print(out.groupby("station").size())

grid = measurements.pivot_table(index="station", columns="lot",
                                values="energy_kj", aggfunc="sum",
                                fill_value=0, margins=True)
print(grid.round(0))

catalogue = pd.DataFrame({
    "station": ["EST-01", "EST-02", "EST-03", "EST-04", "EST-05"],
    "machine": ["CNC lathe", "CNC mill", "Cylindrical grinder",
                "Test bench", "Radial drill"],
    "cycle_target_s": [42, 40, 48, 36, 30],
})

audit = measurements.merge(catalogue, on="station", how="outer", indicator=True)
print(audit["_merge"].value_counts())

joined = board.reset_index().merge(catalogue, on="station", how="left")
joined["cycle_drift"] = (joined["cycle"] / joined["cycle_target_s"] - 1)

print(joined[["station", "machine", "parts", "cycle",
              "cycle_target_s", "cycle_drift"]].round(3))
```

The out-of-tolerance table carries three rows and not four because EST-04 contributed none. `groupby` only returns the groups present in the data it received, and a station with no parts outside simply does not appear. If that table is going into a subtraction or a division, the zero has to be filled in on purpose.

The audit of the join: 28 rows crossed on both sides, 1 stayed only in the catalogue and 0 only in the measurements. The one from the catalogue is EST-05, the radial drill, which exists in the plant and produced no bushings this week: that is fine and it explains itself. The zero on the other side is the figure that matters: no measurement was left orphaned, so the file carries no unknown station. If that number were not zero, it would have to be reported before publishing any total.

EST-01 runs 6.7 % above its target cycle and EST-03 6.2 %, while EST-02 sits at only 1.2 %. Maintenance is told that two of the four stations are losing around three seconds per part against the standard, and that on EST-03 those three seconds pile onto the longest cycle in the cell.

**Output**

```text
         parts   energy   cycle  diameter
station                                  
EST-03       8  12125.0  51.000    12.010
EST-01       7   8810.0  44.833    11.999
EST-02       7   7060.0  40.500    12.007
EST-04       6   4467.0  37.800    12.008
station
EST-01    3
EST-02    1
EST-03    4
dtype: int64
lot       L-2601   L-2602  L-2603      All
station                                   
EST-01    3740.0   2485.0  2585.0   8810.0
EST-02    1990.0   2055.0  3015.0   7060.0
EST-03    4690.0   4540.0  2895.0  12125.0
EST-04    1490.0   1500.0  1477.0   4467.0
All      11910.0  10580.0  9972.0  32462.0
_merge
both          28
right_only     1
left_only      0
Name: count, dtype: int64
  station              machine  parts   cycle  cycle_target_s  cycle_drift
0  EST-01            CNC lathe      7  44.833              42        0.067
1  EST-02             CNC mill      7  40.500              40        0.012
2  EST-03  Cylindrical grinder      8  51.000              48        0.062
3  EST-04           Test bench      6  37.800              36        0.050
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The cleanup is wrapped in a function with a docstring | 1 |
| The board of four summaries comes out in a single statement | 2 |
| Explains why the out-of-tolerance table carries three rows | 2 |
| The grid with row and column totals is correct | 2 |
| The join is audited both ways and the three numbers get read | 2 |
| The cycle drift board is correct and gets reported | 1 |

**Most common mistake**

Joining with `inner` instead of `left` for the board. On this data the result does not change, so the student gets used to a mode that will silently delete rows the moment a station is missing from the catalogue.

---

## Week 16 · Unit 8.2 · Visualisation with matplotlib and seaborn

### 16.1 · Recognise

**Solution**

The bar shows the average energy per part, because `barplot` averages when it is not told otherwise. For EST-01 the bar is worth 1,258.6 kJ. What the subject line claims, the shift energy, is 8,810 kJ, seven times more. Both numbers are correct and they answer different questions: one is how much each part spent on average, the other is how much the station spent.

To make the bar show the total, `estimator="sum"` has to be added, and along with it `errorbar=None`, because the interval drawn on top of each bar means nothing in an energy report.

The four charts:

- Energy of the four stations: bars, because it compares categories with no natural order. Sorted from high to low, the ranking reads itself.
- Spread of the diameters inside each station: box plot, because the question is not the centre but the shape, and that is where the spread the average hides shows up.
- Average diameter across the three days: line, because the horizontal axis is time and joining two dates does assert something true.
- Cycle against deviation from size: scatter, because it asks whether two numeric variables move together.

**Output**

```text
             sum    mean  count
station                        
EST-03   12125.0  1515.6      8
EST-01    8810.0  1258.6      7
EST-02    7060.0  1008.6      7
EST-04    4467.0   744.5      6
            mean     std    min    max
station                               
EST-04   12.0083  0.0343  11.96  12.05
EST-02   12.0071  0.0435  11.95  12.07
EST-01   11.9986  0.0488  11.93  12.06
EST-03   12.0100  0.0646  11.91  12.09
station
EST-01    3
EST-02    1
EST-03    4
dtype: int64
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| Identifies that the bar shows the average and gives both EST-01 figures | 3 |
| Names `estimator` and `errorbar` as the fix | 2 |
| The three tables print correctly | 2 |
| The four charts chosen and justified | 3 |

**Most common mistake**

Answering that the bar shows the total because the axis reaches into the thousands. All four bars look plausible at that scale, and without running the sum and average table there is no way to notice the factor of seven.

### 16.2 · Apply

**Solution**

```python
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import pandas as pd
from pathlib import Path

from cleaning import load_clean

OUTPUT = Path(__file__).resolve().parent

measurements = load_clean()

energy = (measurements.groupby("station")["energy_kj"]
          .sum()
          .sort_values(ascending=False))

print(energy)

peak = energy.index[0]
share = energy.iloc[0] / energy.sum()

print(f"{peak} takes {share:.1%} of the cell energy")

fig, ax = plt.subplots(figsize=(9, 5))

bars = ax.bar(energy.index, energy.values, color="#C7D6E8")
bars[0].set_color("#2B5F8F")

ax.set_title(f"{peak} takes {share:.0%} of the energy of cell C-3")
ax.set_ylabel("Shift energy (kJ)")
ax.set_ylim(0, 13000)
ax.yaxis.set_major_formatter(
    ticker.FuncFormatter(lambda v, _: f"{v / 1000:.0f}k"))

fig.text(0.01, 0.01, "Source: measurements.csv, cell C-3, 8 to 12 January 2026",
         fontsize=8)

fig.savefig(OUTPUT / "energy_station.png", dpi=150, bbox_inches="tight")
plt.close(fig)

print("File generated:", (OUTPUT / "energy_station.png").exists())
```

`load_clean` is the one from 15.3, saved in a `cleaning.py` file next to this week's programs so the cleanup is not copied into every chart.

Alt text: bar chart of the energy consumed by the four stations of cell C-3 between 8 and 12 January 2026. EST-03 leads with 12,125 kJ, followed by EST-01 with 8,810, EST-02 with 7,060 and EST-04 with 4,467. EST-03 on its own accounts for 37 % of the 32,462 kJ of the cell and spends 2.7 times what EST-04 spends.

**Output**

```text
station
EST-03    12125.0
EST-01     8810.0
EST-02     7060.0
EST-04     4467.0
Name: energy_kj, dtype: float64
EST-03 takes 37.4% of the cell energy
File generated: True
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The series by station is correct and sorted | 2 |
| The title states the finding and the percentage is computed in the program | 2 |
| Axis labelled, base at zero and thousands formatting | 2 |
| The peak bar highlighted and the source at the foot | 2 |
| The alt text carries figures checkable against the series | 2 |

**Most common mistake**

Typing the 37 % into the title by hand. It works until next month's file arrives, and then the chart asserts a percentage its own bars no longer support.

### 16.3 · Integrate

**Solution**

```python
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pathlib import Path

from cleaning import load_clean

OUTPUT = Path(__file__).resolve().parent

sns.set_theme(style="whitegrid", palette="deep")

measurements = load_clean()

summary = measurements.groupby("station")["diameter_mm"].agg(
    ["mean", "median", "std", "count"]).round(4)
print(summary.sort_values("std"))

fig, ax = plt.subplots(figsize=(9, 5))
sns.barplot(data=measurements, x="station", y="energy_kj", estimator="sum",
            errorbar=None, hue="station", legend=False, ax=ax)
ax.set_title("EST-03 burns 2.7 times the energy of EST-04 in the same shift")
ax.set_ylabel("Shift energy (kJ)")
fig.savefig(OUTPUT / "energy_bars.png", dpi=150, bbox_inches="tight")
plt.close(fig)

order = (measurements.groupby("station")["diameter_mm"]
         .std().sort_values().index)

fig, ax = plt.subplots(figsize=(9, 5))
sns.boxplot(data=measurements, x="station", y="diameter_mm", order=order,
            hue="station", legend=False, ax=ax)
ax.axhline(11.95, color="#B4462C", linestyle="--", linewidth=1)
ax.axhline(12.05, color="#B4462C", linestyle="--", linewidth=1)
ax.set_title("EST-01 sits on the nominal and still runs outside the band")
ax.set_ylabel("Measured diameter (mm)")
fig.savefig(OUTPUT / "box_station.png", dpi=150, bbox_inches="tight")
plt.close(fig)

grid = measurements.pivot_table(index="station", columns="lot",
                                values="energy_kj", aggfunc="sum",
                                fill_value=0) / 1000
print(grid.round(2))

fig, ax = plt.subplots(figsize=(8, 5))
sns.heatmap(grid, annot=True, fmt=".1f", cmap="Blues", ax=ax)
ax.set_title("Lot L-2601 on EST-03 is the most expensive cell on the board")
fig.savefig(OUTPUT / "heatmap_station_lot.png", dpi=150, bbox_inches="tight")
plt.close(fig)

for name in ["energy_bars.png", "box_station.png", "heatmap_station_lot.png"]:
    print(name, (OUTPUT / name).exists())
```

The conclusion from the three together: EST-03 is the expensive station and the imprecise one at the same time, with 12,125 kJ, the highest spread at 0.0646 mm, and 4 of its 8 parts outside the band. EST-01 has the average closest to nominal, 11.9986 mm, and still 3 parts outside, because its spread is the second highest at 0.0488 mm. EST-04 is the one to copy: 0.0343 mm of spread, no part outside, and the lowest energy.

The box plot is the one to send to maintenance. The bars say how much is being spent and the heat map says where, but the box plot is the only one showing that a centred average does not mean a capable process, which is exactly what has to be fixed on EST-01.

**Output**

```text
            mean  median     std  count
station                                
EST-04   12.0083  12.015  0.0343      6
EST-02   12.0071  12.010  0.0435      7
EST-01   11.9986  12.010  0.0488      7
EST-03   12.0100  12.010  0.0646      8
lot      L-2601  L-2602  L-2603
station                        
EST-01     3.74    2.48    2.58
EST-02     1.99    2.06    3.02
EST-03     4.69    4.54    2.90
EST-04     1.49    1.50    1.48
energy_bars.png True
box_station.png True
heatmap_station_lot.png True
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The theme is set once and the three images get generated | 2 |
| The bar chart uses `estimator` and drops the error bar | 2 |
| The box plot is ordered by spread and carries the two band lines | 2 |
| The heat map comes from the grid, in thousands, with values written in | 1 |
| The three titles state a checkable finding | 1 |
| The conclusion carries at least three figures and picks one chart | 2 |

**Most common mistake**

Leaving the box plot in alphabetical order. The ranking by spread, which is the whole content of that chart, stays hidden and has to be read box by box.

---

## Week 17 · Review and final exam

### 17.1 · Recognise

**Solution**

```text
9
False
None
48.2
1,240 kJ980 kJ
11.98
```

Line 1, grouping before cleaning. Nine stations come out where there are 4, because the spaces and the lower case still split the groups. The correct result is 4.

Line 2, chained assignment. The column was never created. Since pandas 3.0 the operation does nothing and raises no error, only a warning that is easy to walk past. The right form is `measurements.loc[condition, "verdict"] = "Review"`.

Line 3, confusing modifying with returning. `sort` orders the list and returns `None`, so the assignment wiped the data. The right form is `sorted(diameters)`, or calling `diameters.sort()` without assigning.

Line 4, accumulator declared inside. It gives 48.2, which is the last energy figure. The correct total is 308.9.

Line 5, calculating without converting. Both values are text and `+` glues them. The correct result, once converted, is 2,220 kJ.

Line 6, counting from one. `measurements["diameter_mm"][1]` returns 11.98, the second row of the file. The question was about the first, which measures 12.01 and sits at index 0.

The program does not stop on any of the six because all six are valid Python operations on valid data. None of them is a syntax error or a type error: they are correct answers to questions nobody asked.

**Output**

```text
ChainedAssignmentError: A value is being set on a copy of a DataFrame or Series
through chained assignment.
  measurements[measurements["station"] == "EST-03"]["verdict"] = "Review"
9
False
None
48.2
1,240 kJ980 kJ
11.98
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The six lines are correct | 3 |
| The six mistakes are named | 3 |
| The correct result of each one | 2 |
| Explains why the program did not stop | 1 |
| Identifies the real question behind the last line | 1 |

**Most common mistake**

Answering 4 on the first line because the cell has four stations. The answer comes from what is known about the plant instead of what the file carries, and that is the same reflex that leaves a dirty total unchecked.

### 17.2 · Apply

**Solution**

```python
import pandas as pd
from pathlib import Path

DATA = Path(__file__).resolve().parent
LOWER_LIMIT = 11.95
UPPER_LIMIT = 12.05

measurements = pd.read_csv(DATA / "measurements.csv")

print(f"Rows:                    {len(measurements)}")
print(f"Duplicates:              {measurements.duplicated().sum()}")
print(f"Ways of writing station: {measurements['station'].nunique()}")
print(f"No cycle time:           {measurements['cycle_s'].isna().sum()}")

measurements = measurements.drop_duplicates()
measurements["station"] = measurements["station"].str.strip().str.upper()
measurements["energy_kj"] = (measurements["energy_kj"]
                             .str.replace(",", "", regex=False)
                             .str.replace("kJ", "", regex=False)
                             .str.strip()
                             .astype(float))

measurements["verdict"] = "In tolerance"
measurements.loc[(measurements["diameter_mm"] < LOWER_LIMIT) |
                 (measurements["diameter_mm"] > UPPER_LIMIT),
                 "verdict"] = "Out of tolerance"

board = measurements.groupby("station").agg(
    parts=("diameter_mm", "count"),
    energy=("energy_kj", "sum"),
    diameter=("diameter_mm", "mean"),
    spread=("diameter_mm", "std"),
)
board["out"] = (measurements[measurements["verdict"] == "Out of tolerance"]
                .groupby("station").size()
                .reindex(board.index, fill_value=0))
board["rate"] = board["out"] / board["parts"]

print(board.round(4).sort_values("energy", ascending=False))

worst = board["rate"].idxmax()
energy_share = board.loc[worst, "energy"] / board["energy"].sum()
out_share = board.loc[worst, "out"] / board["out"].sum()

print(f"{worst} draws {energy_share:.1%} of the cell energy "
      f"and holds {out_share:.0%} of the parts out of tolerance.")
```

The `reindex` with a zero fill is what keeps EST-04 from coming out empty in the out-of-tolerance column. Without it, the rate for that station would be a missing value and the closing division would give something meaningless. Anyone who does not know `reindex` can reach the same board by joining the count and filling with `fillna(0)`, and both routes mark the same.

**Output**

```text
Rows:                    30
Duplicates:              2
Ways of writing station: 9
No cycle time:           3
         parts   energy  diameter  spread  out    rate
station                                               
EST-03       8  12125.0   12.0100  0.0646    4  0.5000
EST-01       7   8810.0   11.9986  0.0488    3  0.4286
EST-02       7   7060.0   12.0071  0.0435    1  0.1429
EST-04       6   4467.0   12.0083  0.0343    0  0.0000
EST-03 draws 37.4% of the cell energy and holds 50% of the parts out of tolerance.
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The four inspection lines before anything gets touched | 2 |
| The cleanup complete and in the right order | 2 |
| The board with its six correct columns | 3 |
| The station with no parts outside shows zero and not empty | 1 |
| The conclusion is built from the board, with its two figures | 2 |

**Most common mistake**

Skipping the inspection and cleaning straight away. The program hands back the same board and the student cannot say how many duplicates were removed, which is the first question in any review.

### 17.3 · Integrate

**Solution**

```python
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pathlib import Path

DATA = Path(__file__).resolve().parent
LOWER_LIMIT = 11.95
UPPER_LIMIT = 12.05


def mark_verdict(data):
    """Adds the verdict column against the 11.95 to 12.05 mm band."""
    data["verdict"] = "In tolerance"
    data.loc[(data["diameter_mm"] < LOWER_LIMIT) |
             (data["diameter_mm"] > UPPER_LIMIT),
             "verdict"] = "Out of tolerance"
    return data


def load_clean():
    """Loads measurements.csv, drops duplicates, normalises and converts types."""
    data = pd.read_csv(DATA / "measurements.csv").drop_duplicates()

    data["station"] = data["station"].str.strip().str.upper()
    data["energy_kj"] = (data["energy_kj"]
                         .str.replace(",", "", regex=False)
                         .str.replace("kJ", "", regex=False)
                         .str.strip()
                         .astype(float))
    data["date"] = pd.to_datetime(data["date"])

    return mark_verdict(data)


raw = mark_verdict(pd.read_csv(DATA / "measurements.csv"))
clean = load_clean()

out_raw = (raw["verdict"] == "Out of tolerance").sum()
out_clean = (clean["verdict"] == "Out of tolerance").sum()

print(f"Uncleaned: {out_raw} of {len(raw)} out of tolerance "
      f"({out_raw / len(raw):.1%})")
print(f"Cleaned:   {out_clean} of {len(clean)} out of tolerance "
      f"({out_clean / len(clean):.1%})")

board = clean.groupby("station").agg(
    parts=("diameter_mm", "count"),
    energy=("energy_kj", "sum"),
    diameter=("diameter_mm", "mean"),
    spread=("diameter_mm", "std"),
).round(4)

print(board.sort_values("spread", ascending=False))

catalogue = pd.DataFrame({
    "station": ["EST-01", "EST-02", "EST-03", "EST-04", "EST-05"],
    "machine": ["CNC lathe", "CNC mill", "Cylindrical grinder",
                "Test bench", "Radial drill"],
    "cycle_target_s": [42, 40, 48, 36, 30],
})

audit = clean.merge(catalogue, on="station", how="outer", indicator=True)
print(audit["_merge"].value_counts())

sns.set_theme(style="whitegrid", palette="deep")

order = board.sort_values("spread").index

fig, ax = plt.subplots(figsize=(9, 5))
sns.boxplot(data=clean, x="station", y="diameter_mm", order=order,
            hue="station", legend=False, ax=ax)
ax.axhline(LOWER_LIMIT, color="#B4462C", linestyle="--", linewidth=1)
ax.axhline(UPPER_LIMIT, color="#B4462C", linestyle="--", linewidth=1)
ax.set_title("EST-03 is the only station whose upper quartile clears 12.05 mm")
ax.set_ylabel("Measured diameter (mm)")
fig.text(0.01, 0.01, "Source: measurements.csv, cell C-3, January 2026", fontsize=8)
fig.savefig(DATA / "spread_station.png", dpi=150, bbox_inches="tight")
plt.close(fig)

print("Chart generated:", (DATA / "spread_station.png").exists())
```

The numerator does not change because the two duplicated rows are parts that were inside tolerance: 11.99 and 12.04. The denominator does drop, from 30 to 28, and that is why the rate climbs from 26.7 % to 28.6 %. Quality gets told the figure from the clean file, 8 of 28, because repeated measurements are not repeated parts and counting them twice dilutes the problem.

The upper quartile of EST-03 sits at 12.065 mm, above the 12.05 limit. That means more than a quarter of what the station produces runs out on the high side, and not through isolated cases but through where its whole distribution is parked.

Maintenance is asked to look at the cylindrical grinder on EST-03, backed by two figures: a spread of 0.0646 mm against 0.0343 on EST-04, and 4 of the 8 out-of-band parts in the whole cell. The value this file is missing before the cause can be claimed is when the insert was changed or the machine adjusted: without the maintenance log you can point at the station, not at the reason.

**Output**

```text
Uncleaned: 8 of 30 out of tolerance (26.7%)
Cleaned:   8 of 28 out of tolerance (28.6%)
         parts   energy  diameter  spread
station                                  
EST-03       8  12125.0   12.0100  0.0646
EST-01       7   8810.0   11.9986  0.0488
EST-02       7   7060.0   12.0071  0.0435
EST-04       6   4467.0   12.0083  0.0343
_merge
both          28
right_only     1
left_only      0
Name: count, dtype: int64
Chart generated: True
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| Both functions carry a docstring and no code is repeated | 2 |
| Both rates correct, with the numerator and denominator explained | 2 |
| The board sorted by spread is correct | 2 |
| The join audit with its three counts | 1 |
| The chart carries order, band, a title with the finding, and the source | 2 |
| The close carries both figures and names the missing data | 1 |

**Most common mistake**

Reporting the rate from the uncleaned file because «that is what the system gives». 26.7 % against 28.6 % looks like a minor difference, and it is exactly the kind of dilution that makes a problem on one station read as noise across the cell.
