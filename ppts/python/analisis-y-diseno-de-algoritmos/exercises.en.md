# Exercises · Analysis and Design of Algorithms · COM101

This set runs alongside the seventeen sessions of the course and is written for the first-semester Engineering group. Every week carries three exercises: Recognise is answered by reading code and predicting what it prints, Apply asks for a program written against a specification that already states its data and its expected result, and Integrate ties the topic of the week back to the weeks before it. Difficulty climbs inside each week and across the term, so the Recognise of week 12 asks for more than the Integrate of week 4. Every problem happens in the same place: machining cell C-3, its four stations, the 12.00 mm bronze bushings it turns out, and the metrology bench where they get measured. Hand in one `.py` file per exercise through Blackboard, except where the statement asks for paper, with the output exactly as your program produced it.

The tolerance band on the bushing is the same all term: 12.00 mm nominal, 11.95 mm lower limit, 12.05 mm upper limit. Both limits are written as constants at the top of the program and never worked out inside a condition.

---

## Week 01 · Course introduction and the bridge from Excel to Python

### 01.1 · Recognise

**The six shifts of cell C-3**

Machining cell C-3 turns bronze bushings. These are the good parts from the six shifts of last week, in two paired lists. Without running anything, write the four lines this program prints.

```python
shifts = ["T1", "T2", "T3", "T4", "T5", "T6"]
parts = [1240, 1385, 1120, 1510, 1295, 1440]

total = sum(parts)
average = total / len(parts)
best = shifts[parts.index(max(parts))]

print(shifts[0], parts[0])
print(total)
print(average)
print(best)
```

Then answer two things. Which shift `parts[3]` belongs to, and which row that value would sit on in the spreadsheet it came from, if row 1 holds the headers. And what happens if you add `print(parts[6])` at the end of the program.

### 01.2 · Apply

**The week summary, formatted**

Write the program that summarises those same six shifts and prints four aligned lines: parts for the week with a thousands separator, average per shift to one decimal, the best shift with its figure, and how far above the average that shift finished.

The figures it has to give are 7,990 parts for the week, 1,331.7 on average, and shift T4 with 1,510, which sits 178.3 parts above the average. No number gets typed by hand inside a `print`: all four come out of the two lists.

### 01.3 · Integrate

**The reading that got captured again**

Metrology reports that shift T3 was captured wrong. Not 1120 parts but 1320. Fix the value in your 01.2 program, run it again, and report the three new figures next to the old ones.

The program also prints the ticket number of the lot they were measuring, `00847`, held in a text variable.

Then answer three things, one line each. What would have happened with that change in a spreadsheet, and which of the four breaking points from the session explains the difference. What shows in the cell if somebody captures that ticket number with a number format. And which of the four breaking points that one is about.

---

## Week 02 · Unit 1 · Algorithm design

### 02.1 · Recognise

**Tracing the verdict on a bushing**

The nominal bushing measures 12.00 mm and the tolerance band runs from 11.95 to 12.05 mm. This is the pseudocode the metrology bench follows for every part that reaches it.

```text
START
    READ diameter

    IF diameter > 12.05 THEN
        verdict = "Reject: oversize"
    ELSE IF diameter < 11.95 THEN
        verdict = "Reject: undersize"
    ELSE
        verdict = "Accepted"

    WRITE verdict
END
```

Write the full trace for three parts: one at 12.08 mm, one at 11.94 mm, and one at exactly 12.05 mm. On each one note which conditions were evaluated, which were never read, and the verdict it ends on.

The operator then reorders the branches like this and claims the algorithm does the same thing.

```text
IF diameter >= 11.95 THEN
    verdict = "Accepted"
ELSE IF diameter > 12.05 THEN
    verdict = "Reject: oversize"
ELSE
    verdict = "Reject: undersize"
```

Trace the 12.08 mm part against this second version and say which verdict it leaves with. Explain in two lines why this version satisfies the five properties of an algorithm and still cannot be used on the bench.

### 02.2 · Apply

**The cell start-up, on paper**

Write the algorithm for the pre-start check on cell C-3, in pseudocode and as a flowchart. The sequence checks three things in this order: that the guard is closed, that the emergency stop is released, and that the spindle temperature sits below 68 °C. If all three hold, arm the cell. If any one fails, name the one that failed and leave the cell interlocked.

Hand in the pseudocode in the words of the course, the flowchart with the four symbols, and the expected trace of two cases: guard closed, stop released and 61 °C; and guard closed, stop released and 71 °C. No computer.

### 02.3 · Integrate

**An instruction that is not an algorithm**

The whiteboard in the inspection area reads: «if the part looks off size, send it to rework».

Run the two-person test on it and explain in two lines which of the five properties breaks and why. Then rewrite it as an algorithm, with the 11.95 to 12.05 mm band and three outputs: rework if the part came out oversize, scrap if it came out undersize, and release if it sits inside.

Write down which values are the input and what the output is. Add at the end one edge case your first version did not cover, and say what you had to change to cover it.

---

## Week 03 · Units 1 and 2 · Paradigms and an introduction to programming

### 03.1 · Recognise

**Three lines that overwrite each other and four files that do not run**

First, the trace. Write what `parts` holds after each line and what the program prints.

```python
parts = 1240
parts = parts + 85
parts = parts * 2

print(parts)
```

Then four fragments, each saved in its own file. For each one say whether it runs. When it does not, say which of the five rules from the session was broken, what kind of error gets raised, and which line Python will complain about.

```python
# A
readings = [1496, 1502]
print(Sum(readings))

# B
readings = [1496, 1502]
print("average:, readings)

# C
total = 1496 + 1502
print(total

# D
total = 2998
Print(total)
```

### 03.2 · Apply

**The first tachometer program**

The conveyor tachometer in the cell logged five readings during the shift: 1496, 1502, 1488, 1511 and 1494 rpm. Write a program with the full anatomy from the session: a comment at the top saying where the data came from, the import of `mean` from `statistics`, the list of readings, and three `print` calls showing the number of samples, the average, and the highest reading, each with its label.

The average comes to 1498.2 rpm and the highest reading to 1511 rpm.

Then break your own program three ways, one at a time: remove the closing parenthesis of a `print`, change `print` to `Print`, and delete a quotation mark. Hand in a three-row table with the exact message each one gave, including the line it pointed at.

### 03.3 · Integrate

**The week 2 pseudocode, said in Python**

Translate the verdict pseudocode from 02.1 into Python, with the diameter held in a variable at the top of the program and the result printed with its label. The translation is almost line for line: five words change and the colons appear.

Run it three times, with 12.05, with 11.94 and with 12.00, and paste the three outputs. Answer two more things: why the 12.00 run prints `12.0` and not `12.00`, and what verdict a 12.08 mm part would get if you swapped the first two branches.

---

## Week 04 · Unit 3 · Data, data types and primitive operations

### 04.1 · Recognise

**Eight lines of tray arithmetic**

Finished parts go into trays of 24. Without running anything, write the eight lines this program prints.

```python
parts = 1240
per_tray = 24

print(parts / per_tray)
print(parts // per_tray)
print(parts % per_tray)
print("12" + "05")
print(int("12") + int("05"))
print(12.00 + 0.05 == 12.05)
print(0.05 * 3 == 0.15)
print(0.05 * 3)
```

Then answer two things. What the results of the second and third lines mean, in trays and in parts. And why the sixth line gives one answer and the seventh gives the opposite, when both compare decimals that come out exact on paper.

### 04.2 · Apply

**The EST-01 shift, with every value in its own type**

Station EST-01 closed the shift of 8 January 2026 with 1240 parts produced, 37 rejected, and 86.4 kWh of energy. The station stayed running and logged no stoppage.

Declare eight variables with the type each value calls for, including the flag for the station running and the last stoppage, which does not exist. Work out the reject rate as a percentage and the energy per part in kWh, rounded to two and to four decimals. Print both metrics with their label and their unit, then the `type` of five variables to check what Python understood.

The reject rate comes to 2.98 % and the energy per part to 0.0697 kWh. No variable name may be a single letter.

### 04.3 · Integrate

**Two parentheses that change the answer**

With the same EST-01 data, somebody wants to know how much energy each good part costs and writes this.

```python
per_part = energy_kwh / parts - rejects
```

Write both versions, the one above and the one that answers the question, print them both rounded to four decimals, and say in one line what each one calculates. One gives a negative number and the other 0.0718 kWh.

Solve two more things in the same program. How many full trays of 24 come out of the good parts and how many parts are left loose, with integer division and remainder. And what happens to the lot ticket number, `"00847"`, when you convert it to an integer and back to text: print the three values on a single line and explain in one line what got lost on the way.

---

## Week 05 · Unit 4 · Statements, input and output

### 05.1 · Recognise

**Seven lines of formatting**

Without running anything, write exactly what each line prints, with its commas, its decimals and its spaces.

```python
parts = 1240
energy = 86.4
rate = 37 / 1240

print(f"Parts: {parts:,}")
print(f"Energy: {energy:,.2f} kWh")
print(f"Rejects: {rate:.1%}")
print(f"Rejects: {rate:.2%}")
print(f"{'EST-01':<10}{parts:>8}")
print(f"Raw rate: {rate}")
print("Energy: {energy:.2f} kWh")
```

Then explain in one line why the third and fourth lines show the same value as two different figures, and in another what the last line is missing to do what it appears to do.

### 05.2 · Apply

**Capturing the shift**

Write the program that captures a shift from the keyboard and returns the station report. Ask for four values, each with its own prompt: the station, the parts produced, the parts rejected, and the shift energy in kWh. Convert whatever needs converting before you do arithmetic on it.

The report is five labelled lines: station, parts with a thousands separator, rejects, reject rate to two decimals of a percentage, and energy per part to four decimals.

Test it with EST-01, 1240, 37 and 86.4. It has to give 2.98 % and 0.0697 kWh. Hand in the whole session, with what you typed on the same line as the prompt.

### 05.3 · Integrate

**The report that goes to production**

Extend the previous program so it also works out the cycle time and the energy per good part. The shift runs eight hours, that is 28800 seconds, and that constant goes at the top of the program with a name. Cycle time is the shift divided by the parts produced. Energy per good part is the kWh turned into watt hours and split across the parts that were not rejected.

The five figures of the report line up in a column, name on the left in twenty-two spaces and number on the right in ten, each with its format and its unit.

Test it with EST-03, 1512 parts, 68 rejects and 112.8 kWh. It has to give 1,444 good parts, 4.50 % rejects, 19.05 seconds of cycle, and 78.1 Wh per good part. Hand in the whole session.

---

## Week 06 · Unit 4.4 · Selection structures

### 06.1 · Recognise

**The part that lands right on the limit**

Two programs, each with a different part. Without running anything, say what each one prints and why.

```python
# First
diameter = 12.05

if diameter > 12.05:
    verdict = "Reject: oversize"
else:
    verdict = "Accepted"

print(diameter, verdict)
```

```python
# Second
diameter = 12.08

if diameter >= 11.95:
    verdict = "Accepted"
elif diameter > 12.05:
    verdict = "Reject: oversize"
else:
    verdict = "Reject: undersize"

print(diameter, verdict)
```

The second program accepts a part measuring 12.08 mm, three hundredths above the upper limit. Explain in two lines why the second branch is never reached, and write the correct order of the three conditions.

### 06.2 · Apply

**The metrology bench classifier**

Write the program that asks from the keyboard for the number of a part and its measured diameter, and hands it one of three verdicts: reject as oversize above 12.05 mm, reject as undersize below 11.95 mm, and accepted in any other case. Both limits go at the top of the program as named constants.

The output is a single line with the part number, the diameter to two decimals, and the verdict.

Test five parts and hand in the five runs: 12.06, 11.94, 12.05, 11.95 and 12.00. The two that land exactly on a limit have to come out accepted.

### 06.3 · Integrate

**Five destinations and one impossible reading**

Production decides three categories are not enough. An oversize part can be reground as long as it does not pass 12.15 mm; above that there is no material left to take off. An undersize part can be released under concession as long as it does not drop below 11.85 mm; below that it is scrap.

Write the five-category classifier with those five destinations, plus a check that rejects an impossible reading before it classifies anything: any reading at or below zero, or above 20 mm, comes out as an invalid reading and sends the micrometer for inspection. All five boundaries go in as named constants.

Test these eleven readings and hand in the whole table: 12.30, 12.15, 12.06, 12.05, 12.00, 11.95, 11.90, 11.85, 11.80, -3.00 and 25.00. Document at the end, in a five-row table, which verdict the exact value of each boundary gets and why you chose `>` or `>=` on each one.

---

## Week 07 · Unit 4.4 · Nested selection and logical operators

### 07.1 · Recognise

**Four conditions that do not say what they look like**

Without running anything, write the five lines this program prints and explain each one in a line.

```python
station = "EST-03"

if station == "EST-01" or "EST-03":
    print("Critical station")
else:
    print("Normal station")

reading_a = [12.01, 11.98, 12.06]
reading_b = [12.01, 11.98, 12.06]

print(reading_a == reading_b)
print(reading_a is reading_b)

parts = 0
rejects = 0

if parts > 0 and rejects / parts > 0.03:
    print("Stop the station")
else:
    print("Not enough data")

last_stoppage = None
print(last_stoppage is None)
```

Answer two more things. What the first condition would print if the station were EST-04, and how it is written correctly. And why the `and` in the third condition avoids a `ZeroDivisionError` that `or` would have blown up on.

### 07.2 · Apply

**The lot release policy**

A lot gets released when three things hold at once: the station is not in maintenance, the lot carries at least 500 parts, and the reject rate does not pass 3 %. If it is not released there are two roads: if the station is one of the critical ones, EST-01 and EST-03, it gets held and marked as a critical station that missed the policy; otherwise it gets held for one hundred per cent inspection.

Write the program that asks from the keyboard for the station, the parts in the lot, the rejected parts, and whether it is in maintenance, then decides. The list of critical stations and the two thresholds go in as constants at the top. Membership is asked with `in`, not with a row of `or`.

Test these five cases and hand in the five runs: EST-01 with 1240 and 37, not in maintenance; EST-03 with 1512 and 68, not in maintenance; EST-04 with 760 and 9, not in maintenance; EST-02 with 420 and 5, not in maintenance; and EST-01 with 1240 and 37, in maintenance.

### 07.3 · Integrate

**The nesting that was really an and**

The automatic spindle stop arrived from the supplier written like this, with four branches.

```python
if temperature > 68.0:
    if vibration > 4.5:
        action = "Stop the station"
    else:
        action = "Keep running"
else:
    if vibration > 4.5:
        action = "Keep running"
    else:
        action = "Keep running"
```

Write a program that asks for the spindle temperature and the vibration from the keyboard, works out the action with that nested version and with the version collapsed into a single condition, and prints both along with a `True` or `False` saying whether they match.

Run the four cases of the truth table and hand in the four outputs: 70.2 with 5.1; 70.2 with 3.8; 64.0 with 5.1; and 64.0 with 3.8.

Close with two lines. The first explains why this nesting could be collapsed. The second describes a case from the same cell where the nesting cannot be collapsed, and says what its inner branches have to look like for that to happen.

---

## Week 08 · Unit 4.5 · Repetition · First midterm

### 08.1 · Recognise

**A for that steps by four and a tank that does not last**

Without running anything, write everything this program prints and how many lines that is.

```python
for speed in range(38, 56, 4):
    print(speed)

coolant = 50.0
use_per_shift = 7.5
shifts = 0

while coolant > 0:
    coolant -= use_per_shift
    shifts += 1

print(shifts, coolant)
```

Then answer three things. Why the `for` does not print 56 even though it appears in the `range`. How many complete shifts the coolant tank really lasts and why the printed number is not that one. And what would happen if you deleted the line that subtracts the use.

### 08.2 · Apply

**The four stations, in a single pass**

These are the figures for the shift of 8 January, in four paired lists.

```python
stations = ["EST-01", "EST-02", "EST-03", "EST-04"]
parts = [1240, 984, 1512, 760]
rejects = [37, 12, 68, 9]
energy = [86.4, 61.5, 112.8, 48.2]
```

Write the program that walks them once and produces the shift table: a header and one row per station with the station, the parts with a thousands separator, the reject rate to two decimals of a percentage, and the kWh per part to four decimals, all aligned in columns.

The last row is the whole cell, with 4,496 parts, 2.80 % rejects and 0.0687 kWh per part. That row gets worked out by adding and dividing the totals, not by averaging the four rates.

The loop has to keep working if a fifth station is added to the four lists tomorrow, without touching a single line inside it.

### 08.3 · Integrate

**First midterm review: the whole L-2601 lot**

This exercise crosses what the midterm covers: types, formatting, selection and repetition. These are the twelve parts of lot L-2601 with their measured diameter.

```python
parts = ["BJ-1001", "BJ-1002", "BJ-1003", "BJ-1004",
         "BJ-1005", "BJ-1006", "BJ-1007", "BJ-1008",
         "BJ-1009", "BJ-1010", "BJ-1011", "BJ-1012"]
diameters = [12.01, 11.98, 12.06, 12.00, 11.94, 12.03,
             11.99, 12.05, 11.96, 12.02, 12.08, 11.97]
```

Write the program that walks the two paired lists and prints one row per part with its number, its diameter to two decimals, and its verdict, using the three categories from week 6 and the band constants.

When the pass ends, print two more lines: the average diameter of the lot to four decimals, and how many of the twelve parts came out of tolerance, with the percentage to one decimal. The average comes to 12.0075 mm and 3 of 12 fall out.

Close by answering in two lines why part BJ-1008, which measures 12.05, does not count as out of tolerance, and what would have happened to that count if the program used `>=` instead of `>` in the first condition.

---

## Week 09 · Unit 4.5 · Accumulators, flags and nested loops

### 09.1 · Recognise

**An accumulator that wipes itself and a search that leaves early**

Two programs. Without running anything, say what each one prints.

```python
# First
energy_use = [86.4, 61.5, 112.8, 48.2]

for use in energy_use:
    total = 0.0
    total += use

print(total)
```

```python
# Second
stations = ["EST-01", "EST-02", "EST-03", "EST-04"]
parts = [1240, 984, 1512, 760]
rejects = [37, 12, 68, 9]

for i in range(len(stations)):
    if parts[i] < 1000:
        continue

    if rejects[i] / parts[i] > 0.03:
        print("First out of control:", stations[i])
        break
else:
    print("No station goes over the limit")
```

From the first, say what the expected result was, what comes out, and which single line has to move. From the second, write the trace of the four passes saying what happens on each one, and explain why the `else` on the `for` does not run and in what case it would.

### 09.2 · Apply

**Three questions, one pass**

With the four lists from the shift in 08.2, write the program that answers three different questions inside one `for`, with the three variables declared before the loop.

How much energy the whole cell used, which is an accumulator. How many stations went over the 3 % reject target, which is a counter. And whether there is at least one station spending more than 0.070 kWh per part, which is a flag.

The three answers print with a label: 308.9 kWh, 1 station off target, and the flag on `True`. Both targets go in as named constants.

Close by explaining in one line why the second question cannot be answered with an accumulator and the first cannot be answered with a counter.

### 09.3 · Integrate

**The production projection, station by shift**

Industrial engineering wants the projected parts for each station on each of the three shifts of the day. These are the rates and the durations.

```python
stations = ["EST-01", "EST-02", "EST-03", "EST-04"]
parts_per_hour = [155, 123, 189, 95]
shifts = ["T1", "T2", "T3"]
hours = [8, 8, 6]
```

Write the program with two nested loops that prints one row per pairing, with the station, the shift, and the projection with a thousands separator, aligned. Before you run it, write in your notebook how many rows should come out; if that does not match what it prints, the nesting is wrong.

When it ends, print two summary lines: the projected output of the cell, which comes to 12,364 parts, and how many pairings pass 1000 parts, which is 5.

The two loop variables have to carry different names and say what they walk. Close by explaining in two lines how many passes this program would make if the plant had 40 stations and 3 shifts, and at what size you would start to worry.

---

## Week 10 · Unit 5 · User-defined functions

### 10.1 · Recognise

**A function that calculates fine and hands back nothing**

Without running anything, say what each of the three closing lines of this program prints.

```python
def reject_rate(parts, rejects):
    rejects / parts


def energy_per_part(energy_kwh, parts):
    per_unit = energy_kwh * 1000 / parts
    return per_unit


print(reject_rate(1240, 37))
print(energy_per_part(86.4, 1240))
print(per_unit)
```

Then answer three things, one line each. What the first function is missing, and why the error does not surface inside it but wherever somebody uses its result. Why the third line fails even though `per_unit` was calculated. And what would happen if the second function had `print(per_unit)` instead of `return per_unit`.

### 10.2 · Apply

**Two shift calculations, packaged**

Write two functions, each with a one-line docstring. The first, `reject_rate(parts, rejects)`, returns the fraction of parts rejected. The second, `in_tolerance(diameter)`, returns true or false against the 11.95 to 12.05 mm band, which lives in two constants outside the function.

Neither one may print anything. They take values and they return values.

Test them with six calls and paste the output: the rate for EST-01 with 1240 and 37, the rate for EST-03 with 1512 and 68, the rate for a 760-part lot with no rejects at all, and the tolerance of 12.00, of 12.05 and of 12.06. The three rates rounded to four decimals come to 0.0298, 0.045 and 0.0.

Close by explaining in one line why 12.05 is the case that always has to be tested, and what would have happened if the function used `<` instead of `<=`.

### 10.3 · Integrate

**Lot L-2601, solved with functions**

Solve exercise 08.3 again, now with four functions and without repeating a single condition.

`in_tolerance(diameter)` answers whether the part sits inside the band. `verdict(diameter)` returns accepted, rework or scrap, and calls the first one from inside instead of comparing all over again. `accepted_parts(diameters)` counts how many readings in a list fall inside. `average_diameter(diameters)` returns the average.

No function prints. The main program walks the twelve parts of the lot, prints the row for each one, and closes with three lines: measured, accepted and average. That comes to 12 measured, 9 accepted and 12.0075 mm.

Close with two lines. Delete the comparison against the lower limit from the body of `in_tolerance` and say which of your four tests catches it; if none of them does, add the one that is missing and say so.

---

## Week 11 · Unit 5 · Arguments, built-in functions and modules

### 11.1 · Recognise

**The argument that landed in the wrong slot**

Without running anything, write the three numbers this program prints, rounded to two decimals, and say which parameter the 5.0 reached in each call.

```python
def energy_per_part(energy_kwh, parts, factor=1000, losses=0.0):
    return energy_kwh * factor / parts + losses


print(energy_per_part(86.4, 1240))
print(energy_per_part(86.4, 1240, 5.0))
print(energy_per_part(86.4, 1240, losses=5.0))
```

The second call returns a number that looks nothing like the other two. Explain in two lines what happened, why Python raised no error, and what would happen to the definition if you moved `factor=1000` ahead of `parts`.

### 11.2 · Apply

**A function that serves more than one bushing**

The cell also machines 8.00 mm bushings to the same tolerance, and now and then runs a special batch with an open tolerance of 0.10 mm. Write `out_of_tolerance(diameter, nominal=12.00, tolerance=0.05)`, with its docstring, that works out both limits inside and returns true when the part falls outside.

Test it with five calls: 12.06 with the defaults; 12.05 with the defaults; 12.06 with nominal and tolerance given by position; 12.06 passing only the tolerance by keyword; and 8.02 passing only the nominal by keyword.

Add two lines at the end that check, before you trust the function, that `12.00 - 0.05` gives exactly 11.95 and that `12.00 + 0.05` gives exactly 12.05. Explain in one line why that check is not wasted effort, even though both come out true here.

### 11.3 · Integrate

**What the lot average does not tell you**

With the twelve readings of lot L-2601, write the program that imports `mean`, `median`, and a third function from the `statistics` module that we did not see in class, one that measures how spread out the readings are. Find that third function on docs.python.org and cite the page.

The program prints seven lines: number of readings, average, median and spread to four decimals, the lowest and the highest to two, and the capability index, which is the width of the tolerance band over six times the spread. It gives an average of 12.0075, a median of 12.0050, a spread of 0.0406, and an index of 0.41.

At the end, repeat the average and the median over a list of thirteen values, the same ones plus a reading of 12.90 mm that somebody captured with the micrometer badly set. One of the two numbers moves far more than the other.

Close with three lines: what a capability index of 0.41 means for the process, what you would tell the production manager with that figure, and which of the two measures of centre you would report when you suspect a bad reading.

---

## Week 12 · Unit 6 · Lists and tuples

### 12.1 · Recognise

**A method that sorts and wipes the backup**

Without running anything, write the seven lines this program prints and what happens on the last one.

```python
diameters = [12.01, 11.98, 12.06, 12.00, 11.94]

print(diameters[0], diameters[-1])
print(diameters[1:3])
print(sorted(diameters))
print(diameters)

ordered = diameters.sort()
print(ordered)
print(diameters)

backup = diameters
copy = diameters.copy()
diameters.append(12.10)

print(len(backup), len(copy))
print(diameters[6])
```

Answer three more things. Why `diameters[1:3]` returns two values and not three. Why `backup` and `copy` end with a different number of elements, when both were created at the same moment. And what would have happened to the data if instead of `ordered = diameters.sort()` somebody writes `diameters = diameters.sort()`.

### 12.2 · Apply

**Four questions about the diameter column**

With the twelve readings of lot L-2601, write the program that prints the list at the start, answers four questions, and prints the list again at the end, where it has to come out identical.

The highest and the lowest reading. The three highest readings, sorted from high to low. Which position holds the 11.94 reading and which part number it belongs to, given that the first part is BJ-1001. And the last three readings of the lot, taken with a slice.

The three highest are 12.08, 12.06 and 12.05. The 11.94 reading sits at position 4 and belongs to part BJ-1005.

### 12.3 · Integrate

**The out-of-band parts, without touching the original**

Write the program that walks the twelve readings and builds a new list with the ones that fall outside the band, leaving the original list alone. Then sort it from high to low and print it.

The band goes in a three-value tuple, `(12.00, 11.95, 12.05)`, which is nominal, lower limit and upper limit. Every comparison reads that tuple by position.

The report is five lines: the band with its three figures, how many readings were checked, how many fell outside, the list of the ones that fell outside sorted from high to low, and the whole original list to prove it stayed intact. That comes to 3 of 12, and the out-of-band list is 12.08, 12.06 and 11.94.

Close with a line that tries to change the upper limit of the tuple to 12.10 and paste the full error it raises. Explain in one line why the band is better off in a tuple than in a list.

---

## Week 13 · Unit 6 · Sets and dictionaries · Second midterm

### 13.1 · Recognise

**A catalogue that grows and a code that does not exist**

Without running anything, write the eight lines this program prints and what happens on the last one.

```python
defects = {"D01": "Diameter out of tolerance",
           "D02": "Excessive roughness",
           "D03": "Burr on the chamfer"}

defects["D02"] = "Roughness above Ra 1.6"
defects["D04"] = "Ding on the front face"

print(len(defects))
print(defects["D02"])
print(defects.get("D09"))
print(defects.get("D09", "Code not in the catalogue"))

shift_a = {"D01", "D02", "D01", "D03"}
shift_b = {"D02", "D03", "D05"}

print(len(shift_a))
print(sorted(shift_a & shift_b))
print(sorted(shift_a - shift_b))
print(sorted(shift_a ^ shift_b))
print(defects["D09"])
```

Answer two more things. Why the dictionary ends with four entries when two codes were assigned to it after it was created. And why `shift_a` holds three elements when the list it came from carries four.

### 13.2 · Apply

**The defect catalogue for the cell**

Build the dictionary of the six defect codes the cell handles: D01 diameter out of tolerance, D02 roughness above Ra 1.6, D03 burr on the chamfer, D04 ding on the front face, D05 concentricity out of spec, and D06 tool mark.

The shift reported these eight codes, in this order: D01, D03, D01, D05, D01, D02, D03 and D09.

Write the program that prints the whole catalogue by walking it with `items`, then three labelled figures (codes in the catalogue, parts reported, and distinct codes reported), and at the end the sorted list of distinct codes, each with its description.

Looking up the description has to go through `get` with a default value, because D09 is not in the catalogue and the program cannot stop there. That gives 6 codes in the catalogue, 8 parts reported and 5 distinct codes.

### 13.3 · Integrate

**Second midterm review: the shift board**

This exercise crosses what the midterm covers: repetition, functions and collections. The data are these.

```python
stations = ["EST-01", "EST-02", "EST-03", "EST-04"]
energy = [86.4, 61.5, 112.8, 48.2]
parts = [1240, 984, 1512, 760]

reported_a = ["D01", "D03", "D01", "D05", "D01", "D02", "D03"]
reported_b = ["D02", "D02", "D06", "D03", "D01"]
```

First, build the dictionary that goes from station to energy with a loop. It does not get typed by hand. Print it with `items`, get the total with `values`, and find the hungriest station by walking the dictionary rather than by eye. The total comes to 308.9 kWh and the hungriest station is EST-03 with 112.8.

Second, count how many times each code of shift A appears using a dictionary as a counter, with `get` and a default of zero. Print it sorted by code.

Third, compare the codes of the two shifts with set operations, never with a loop and an `if`: the ones that showed up in both, the ones only in shift A, the ones new in shift B, and the ones in one but not in both.

Close with two lines: what maintenance decision you would take on the code that showed up new in shift B, and why the count for shift A could not have been done with a set.

---

## Week 14 · Unit 7 · Text and CSV files

### 14.1 · Recognise

**What a CSV hands back, and of what type**

The four weeks that are left work on the same file. Create it under the name `measurements.csv`, saved in the same folder as your programs and encoded in UTF-8. It holds 30 rows from the metrology bench of cell C-3, exported exactly as the system gave them, with three days of measurements and three lots.

```text
date,station,lot,diameter_mm,cycle_s,energy_kj
2026-01-08,EST-01,L-2601,12.01,44,"1,240 kJ"
2026-01-08,EST-02,L-2601,11.98,39,980 kJ
2026-01-08, EST-01,L-2601,12.06,46,"1,310 kJ"
2026-01-08,EST-03,L-2601,12.00,51,"1,505 kJ"
2026-01-08,est-01,L-2601,11.94,,"1,190 kJ"
2026-01-08,EST-04,L-2601,12.03,38,760 kJ
2026-01-09,EST-01,L-2602,11.99,45,"1,260 kJ"
2026-01-09,EST-02,L-2602,12.05,41,"1,020 kJ"
2026-01-09,EST-03,L-2602,12.08,52,"1,540 kJ"
2026-01-09,EST-01 ,L-2602,12.02,43,"1,225 kJ"
2026-01-09,EST-04,L-2602,11.96,,745 kJ
2026-01-09,EST-03,L-2602,11.97,50,"1,480 kJ"
2026-01-12,EST-01,L-2603,12.04,44,"1,255 kJ"
2026-01-12,est-02,L-2603,12.07,40,"1,005 kJ"
2026-01-12,EST-03,L-2603,11.95,49,"1,460 kJ"
2026-01-12,EST-04,L-2603,12.00,37,735 kJ
2026-01-12,EST-01,L-2603,11.93,47,"1,330 kJ"
2026-01-12,EST-02,L-2603,12.01,,995 kJ
2026-01-08,EST-02,L-2601,12.02,40,"1,010 kJ"
2026-01-08,EST-03,L-2601,12.09,53,"1,575 kJ"
2026-01-09,EST-01,L-2602,11.99,45,"1,260 kJ"
2026-01-09,EST-04,L-2602,12.03,39,755 kJ
2026-01-12,EST-03,L-2603,12.02,48,"1,435 kJ"
2026-01-12,EST-04,L-2603,11.98,38,742 kJ
2026-01-08,EST-04,L-2601,12.05,37,730 kJ
2026-01-09,EST-02,L-2602,11.95,42,"1,035 kJ"
2026-01-12,EST-01,L-2603,12.04,44,"1,255 kJ"
2026-01-08,EST-03 ,L-2601,11.91,54,"1,610 kJ"
2026-01-09,EST-03,L-2602,12.06,51,"1,520 kJ"
2026-01-12,EST-02,L-2603,11.97,41,"1,015 kJ"
```

Without running anything, write the six lines this program prints.

```python
import csv
from pathlib import Path

DATA = Path(__file__).resolve().parent

with (DATA / "measurements.csv").open(encoding="utf-8") as f:
    rows = list(csv.DictReader(f))

print(len(rows))
print(rows[0]["station"], rows[0]["diameter_mm"])
print(type(rows[0]["diameter_mm"]))
print(rows[0]["diameter_mm"] + rows[1]["diameter_mm"])
print(rows[4]["cycle_s"] == "")
print(rows[2]["station"] == "EST-01")
```

Then answer three things, one line each. Why the fourth line raises no error at all, given that it is adding things wrongly. Why the sixth line comes out false when that row in the file reads EST-01. And what would happen to the file if that same open call carried `"w"` instead of the default mode.

### 14.2 · Apply

**The station summary, read by column name**

Write the program that reads `measurements.csv` with `DictReader` and produces the bench summary. You need three short functions, each with its docstring: one that turns the energy into a decimal by stripping the thousands comma and the unit, one that turns the cycle time into an integer and reports a missing value as `None` when the cell comes in empty, and one that normalises the station name by stripping the spaces at both ends and leaving one single way of writing it.

The program first prints four diagnostic lines: rows read, rows with no cycle time, distinct ways of writing the station, and stations left after normalising. That comes to 30 rows, 3 with no cycle time, and 9 spellings reduced to 4 stations.

Then it prints the table by station, sorted by name, with parts measured, total energy in kJ, and average diameter to four decimals, plus the row for the whole cell. With the file as it comes, the cell adds up to 34,977 kJ across 30 measurements.

Paths get built from the location of the file, never typed by hand.

### 14.3 · Integrate

**Clean it, decide, and write the output file**

Now the same file gets processed with engineering judgement and the result gets saved.

The program drops the exactly duplicated rows by comparing the whole row rather than a single column, normalises the station, converts the energy, and marks each part as out of tolerance when its diameter falls outside the band. Rows with no cycle time are kept, because their diameter was measured and that is the variable deciding whether the part is any good; the program reports how many they are and leaves the decision written down.

It prints six log figures: 30 rows in the file, 2 exact duplicates removed, 28 rows left, 3 rows with no cycle time kept, 8 parts out of tolerance, and 32,462 kJ of cell energy.

Then it writes a new file called `station_summary.csv`, with the header `station,parts,out_of_tolerance,energy_kj` and one row per station sorted by name. Writing a CSV on Windows takes the parameter that avoids the blank row between records. At the end the program prints the contents of the file it has just written.

That energy is 2,515 kJ lower than the one in the previous exercise. Explain in two lines where the exact difference comes from, and why a duplicate inflates the total and barely moves the average diameter.

---

## Week 15 · Unit 8.1 · Series, DataFrame, cleaning and grouping

### 15.1 · Recognise

**What pandas inferred from the file, and why**

Without running anything, say what each of the seven statements in this program prints. It runs on the same `measurements.csv`.

```python
import pandas as pd
from pathlib import Path

DATA = Path(__file__).resolve().parent

measurements = pd.read_csv(DATA / "measurements.csv")

print(measurements.shape)
print(measurements.dtypes)
print(measurements["cycle_s"].isna().sum())
print(measurements.duplicated().sum())
print(measurements["station"].nunique())
print(measurements["station"].value_counts())
print(measurements["diameter_mm"].describe().round(3))
```

Then answer four things, one line each. Why `cycle_s` came out decimal and not integer, when every time in the file is a round number of seconds. Why `energy_kj` came out as text. Why two rows in the `value_counts` output look identical and are still separate entries. And which columns `describe` summarises and which it leaves out.

### 15.2 · Apply

**The four repairs, with their log**

Write the program that loads `measurements.csv` with pandas and leaves it ready to analyse, printing the count before and after each repair.

The order is this: report the starting state, drop duplicates, normalise the station with string methods, strip the thousands comma and the unit off the energy and convert it to a decimal, and convert the date to a date type. Print the types of the six columns when you are done.

The numbers it has to report are 30 rows on loading, 2 duplicates, 9 ways of writing the station, 3 rows with no cycle time, 28 rows once the duplicates are gone, and 4 real stations.

Then add the `verdict` column, which reads «In tolerance» everywhere and «Out of tolerance» where the diameter falls outside the band, written in a single step with `loc`. That gives 20 in and 8 out.

Close with four more figures: how many EST-03 parts came out of tolerance, which is 4; how many measurements belong to EST-01 or EST-02, which is 14 and gets asked with `isin`; the total energy, which comes to 32,462 kJ; and the average cycle, which comes to 44.36 seconds. Report as well how many rows you would be left with if you discarded the three with no cycle time, and explain in two lines why keeping them is the better call for this file.

Combined conditions use the symbols and their parentheses, never the words.

### 15.3 · Integrate

**The cell board, the grid by lot, and the audited join**

Wrap the whole cleanup of 15.2 in a function `load_clean()` with its docstring, so you never write it again for the rest of the term.

First, group by station and ask for four summaries in a single statement: parts measured, energy, average cycle, and average diameter, rounded to three decimals and sorted by energy from high to low. EST-03 leads with 12,125 kJ across 8 parts.

Second, print how many out-of-tolerance parts each station contributed. Look at how many rows that table carries and explain in one line why it is not four.

Third, build the grid of station against lot with the energy summed, filling anything with no record with zero and adding the row and column totals. The most expensive cell is lot L-2601 on EST-03 with 4,690 kJ, and the grand total comes to 32,462.

Fourth, build this catalogue as a DataFrame from a dictionary of columns and join it to the board.

```python
catalogue = pd.DataFrame({
    "station": ["EST-01", "EST-02", "EST-03", "EST-04", "EST-05"],
    "machine": ["CNC lathe", "CNC mill", "Cylindrical grinder",
                "Test bench", "Radial drill"],
    "cycle_target_s": [42, 40, 48, 36, 30],
})
```

Audit the join in both directions before you trust it. It has to come out at 28 rows on both sides, 1 only in the catalogue and 0 only in the measurements. Explain in two lines what each of those three numbers means for the plant.

Close with the cycle drift board: station, machine, parts, real cycle, target cycle, and drift as a fraction, rounded to three decimals. EST-01 runs 6.7 % above its target and EST-02 only 1.2 %. Write in two lines what you would report to maintenance with those figures.

---

## Week 16 · Unit 8.2 · Visualisation with matplotlib and seaborn

### 16.1 · Recognise

**The bar that says average when the subject line says total**

Somebody in production built this chart from the already clean file and emailed it with the subject «shift energy by station».

```python
sns.barplot(data=measurements, x="station", y="energy_kj", ax=ax)
```

Without running anything, answer what number each bar is showing, what that bar is worth for EST-01 and what it would be worth if it showed what the subject line says, and what would have to be added to the call for it to show the total.

Then write the short program that prints the three tables holding up your answer: the sum, the average and the count of energy by station; the average, the spread, the minimum and the maximum of diameter by station, sorted by spread; and how many out-of-tolerance parts each one contributed.

Close by choosing the right chart for each of these four questions, with one line of justification each.

- How the energy of the four stations compares.
- How the measured diameters spread out inside each station.
- How the average diameter of the cell moved across the three days.
- Whether the parts with the longest cycle are also the ones furthest off size.

### 16.2 · Apply

**The energy of the cell, in a chart that travels on its own**

With the clean file, group the energy by station and produce a bar chart saved as `energy_station.png` at 150 dots per inch.

The chart carries five things: a title with the finding rather than with the names of the axes, the vertical axis labelled with its unit, the vertical axis starting at zero, the vertical axis formatted in thousands so nobody has to count digits, and the source at the foot. The bar of the peak station goes in strong blue and the other three in pale blue.

EST-03 takes 37.4 % of the energy of the cell with 12,125 kJ, and that percentage gets worked out inside the program rather than typed by hand in the title.

The program prints the series by station and a line confirming the file was generated. Close the figure when you are done.

Write the alt text for the chart as well, two or three lines, where every figure you mention can be checked against the printed series.

### 16.3 · Integrate

**Three seaborn charts and the story they tell together**

Set the seaborn theme once at the top and produce three images from the clean file.

The first is a bar chart of the energy by station, with the right estimator and without the error bar it draws by default. It gets saved as `energy_bars.png`.

The second is a box plot of the measured diameters by station, with the stations ordered by spread from low to high and two dashed horizontal lines at 11.95 and 12.05 marking the band. It gets saved as `box_station.png`.

The third is a heat map of the station against lot grid, with the energy in thousands of kJ, the value written inside each cell, and one decimal. It gets saved as `heatmap_station_lot.png`.

All three carry a title with the finding. The program prints the table of average, median, spread and count of diameter by station sorted by spread, and the grid in thousands.

In that table, EST-01 has the average closest to nominal of the four stations and is still the second worst for parts outside the band. Write in three lines the conclusion that comes out of putting the three charts together, with at least three checkable figures, and say which of the three you would send to maintenance if you could only send one.

---

## Week 17 · Review and final exam

### 17.1 · Recognise

**The six expensive mistakes, all in one file**

This program runs start to finish and produces six results. Five of them are wrong.

```python
import pandas as pd
from pathlib import Path

DATA = Path(__file__).resolve().parent

measurements = pd.read_csv(DATA / "measurements.csv")

averages = measurements.groupby("station")["diameter_mm"].mean()
print(len(averages))

measurements[measurements["station"] == "EST-03"]["verdict"] = "Review"
print("verdict" in measurements.columns)

diameters = [12.01, 11.98, 12.06]
diameters = diameters.sort()
print(diameters)

for use in [86.4, 61.5, 112.8, 48.2]:
    total = 0.0
    total += use
print(total)

print(measurements["energy_kj"][0] + measurements["energy_kj"][1])

print(measurements["diameter_mm"][1])
```

Without running anything, write the six lines it prints and, for each one, name the mistake from the list of the term, say what the correct result was, and explain in one line why the program did not stop. The last line prints a number that does exist in the file and still answers the wrong question; say what the question was.

### 17.2 · Apply

**From file to finding, in a single run**

Write the program that goes from the raw file to a conclusion, in this order and without skipping a step: inspect, clean, group and conclude.

The inspection prints four figures: rows, duplicates, ways of writing the station, and rows with no cycle time. The cleanup drops duplicates, normalises the station, converts the energy, and marks the verdict on every part.

The board by station carries six columns: parts, energy, average diameter, spread, parts out of tolerance, and out-of-tolerance rate, sorted by energy from high to low. The out-of-tolerance column has to read zero on the station that contributed none, not come out empty.

The last line is the conclusion, and it gets built inside the program from the board rather than typed by hand: which station carries the highest rate, what percentage of the energy of the cell it draws, and what percentage of the out-of-tolerance parts it holds. Those come to 37.4 % of the energy and 50 % of the parts out.

### 17.3 · Integrate

**The close: cleaning changes the answer, and you have to be able to say by how much**

Wrap the cleanup in `load_clean()` and the verdict marking in its own function, both with a docstring.

First, report the out-of-tolerance rate with the file uncleaned and with the file clean: 8 of 30 against 8 of 28. Explain in two lines why the numerator does not change and the denominator does, and which of the two figures you would report to quality.

Second, print the board by station with parts, energy, average diameter and spread, sorted by spread from high to low.

Third, audit the join against the five-station catalogue of 15.3 and report the three indicator counts.

Fourth, produce a single box plot of the diameters by station, ordered by spread, with the two band lines, a title with the finding, and the source at the foot, saved as `spread_station.png`.

The checkable finding is that EST-03 is the only station whose upper quartile, 12.065 mm, clears the 12.05 mm limit. Close with three lines: what you would ask maintenance for, which two figures back it up, and what data this file is missing before you could claim the cause.
