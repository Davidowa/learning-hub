# Exercises · Object-Oriented Programming · COM102

This booklet runs alongside the seventeen sessions of the course. Every week brings three exercises: **Recognise** is answered by reading code and predicting what it prints, **Apply** asks for code written against a specification with the data given, and **Integrate** ties the topic of the week to what came before. Difficulty climbs inside the week and across the term, so the Recognise of week 12 weighs more than the Integrate of week 4. Every problem happens in the same pumping plant: equipment with ISA tags (B-101, C-310, M-204, V-12), instruments (TT-101, PT-205, FT-330), work orders, spare parts and logbooks. Hand in one `.py` file per exercise, through Blackboard, named `surname_NN_M.py`.

## Week 01 · Course orientation

### 01.1 · Recognise
Types and a loop, traced.

The program below runs without errors. Write, line by line, what it prints, and explain in one sentence why the third output is not 4.

```python
tag = "B-101-PUMP"
hours = "4820"

print(tag[0], tag[-1])
print(tag[0:5])
print(len(hours * 2))
print(hours + "0")

total = 0
for i in range(1, 4):
    total += i * 10
print(total)
```

### 01.2 · Apply
Classifying a pressure.

Gauge PT-205 reports pressures in bar. Write the function `classify_pressure(bar)` that **returns** (does not print) one of three strings: `"low"` when the pressure is under 2.0, `"normal"` when it sits between 2.0 and 8.0 with both ends included, and `"high"` when it goes past 8.0.

Then walk the list `[1.4, 2.0, 6.7, 8.0, 9.3]` and print one line per reading in this exact format, with one decimal:

```text
1.4 bar -> low
```

The boundaries matter: 2.0 and 8.0 are "normal", not "low" and not "high".

### 01.3 · Integrate
Readings that are not always numbers.

The data logger hands over the shift readings as a list of tuples, and now and then the value arrives as text because the instrument did not answer:

```python
readings = [
    ("TT-101", "74.5"),
    ("PT-205", "6.1"),
    ("TT-101", "n/a"),
    ("FT-330", "118.0"),
    ("PT-205", "6.4"),
    ("FT-330", "no data"),
]
```

Write three functions, each one returning a value and with no `print` inside:

1. `separate(records)` returns two things: the list of tuples whose value did convert to `float`, and how many were thrown out. The conversion goes inside a `try` with the exception type named.
2. `average(values)` returns the mean of a list of numbers.
3. `tags(records)` returns the tags with no repeats, in alphabetical order.

The main program prints how many readings were valid, how many were discarded, the average with two decimals and the list of tags.

## Week 02 · Topic 1 · Introduction to OOP

### 02.1 · Recognise
Parallel lists that fall out of step.

The program below keeps the equipment inventory in two lists that match by position. Somebody retired pump B-102. Predict the output, then answer this: which piece of equipment do the 1150 hours on screen actually belong to?

```python
tags = ["B-101", "B-102", "C-310"]
hours = [4820, 1150, 6300]

tags.remove("B-102")

for i in range(len(tags)):
    print(tags[i], hours[i])
```

Write as well which line was missing, and why Python did not complain.

### 02.2 · Apply
What needs a class and what needs a function.

These six modules turn up in the plant maintenance system. Sort each one as **class** or **function**, with one line of justification that uses the criterion from the session: if it keeps something between one call and the next, there is state, and where there is state there is a class.

1. Converting a pressure reading from psi to bar.
2. A pump with running hours and a current state.
3. Counting how many logbook rows say "fault".
4. A work order with a number, an assigned piece of equipment and progress.
5. Sorting a list of spare parts by code.
6. A spare parts inventory that deducts pieces as they are issued.

Of the ones you sorted as functions, implement the first: `psi_to_bar(psi)` with the factor 0.0689476, and print the result for 120 psi and for 45 psi, with two decimals and the unit.

### 02.3 · Integrate
From the row of lists to the record.

The current system keeps four parallel lists:

```python
tags = ["B-101", "B-102", "C-310", "M-204"]
hours = [4820, 1150, 6300, 2210]
states = ["running", "stopped", "running", "running"]
inspection = [1180, 40, 900, 310]
```

Rewrite it with a single list of dictionaries, one dictionary per piece of equipment with the keys `tag`, `hours`, `state` and `inspection`. Write `to_records(...)` for the conversion, `retire(records, tag)` returning a new list without that equipment, and `show(records)` printing one line per piece of equipment.

Retire B-102 and print what is left, plus the total count. No data may end up out of step, and no function may modify the list it receives.

## Week 03 · Topic 2 · Building blocks

### 03.1 · Recognise
The list every pump shares.

B-101 logged two alarms. B-102 logged none. Predict the three outputs and explain in one line where the `alarms` list lives.

```python
class Pump:
    alarms = []

    def __init__(self, tag):
        self.tag = tag

    def alarm(self, code):
        self.alarms.append(code)


b1 = Pump("B-101")
b2 = Pump("B-102")

b1.alarm("E12")
b1.alarm("E07")

print(len(b2.alarms))
print(b2.alarms)
print(b1.alarms is b2.alarms)
```

Write the fix as well, which fits on one line.

### 03.2 · Apply
The pump as a class.

Write the class `Pump` with a constructor taking `tag`, `flow_l_s` and `hours`. Add:

- the method `log_hours(run)`, adding the hours of the shift to the accumulated ones;
- the property `flow_m3_h`, returning the flow in cubic metres per hour (multiply litres per second by 3.6);
- the property `hours_to_service`, returning how many hours are left before the 5000 of the major service.

Build B-101 with 120.0 L/s and 4820 hours. Print the flow in m3/h with one decimal, print the hours left, log another 260 hours and print them again. The second number comes out negative, and that is how it should come out: the service is already overdue.

### 03.3 · Integrate
Sensors with a range of their own.

Write the class `Sensor` with `tag`, `unit`, `low` and `high`, the method `in_range(value)` returning true or false, and the property `span` returning the width of the scale.

Build a dictionary with three sensors: TT-101 in degrees C from 0.0 to 400.0, PT-205 in bar from 0.0 to 10.0 and FT-330 in L/s from 0.0 to 200.0. Walk these readings and print, for each one, the tag, the value, the unit and whether it landed inside or `OUTSIDE`:

```python
readings = [
    ("TT-101", 412.0),
    ("PT-205", 6.1),
    ("FT-330", 118.0),
    ("TT-101", 74.5),
    ("PT-205", 11.2),
]
```

Finish by printing how many readings fell out of range and the span of FT-330. The sensor is looked up by tag through the dictionary, not by walking a list.

## Week 04 · Topic 2 · Building blocks

### 04.1 · Recognise
The private one, the counter and the renaming.

Predict the four outputs. Two of them surprise half the group.

```python
class Equipment:
    registered = 0

    def __init__(self, tag):
        self.__tag = tag
        self.registered += 1

    def label(self):
        return self.__tag


a = Equipment("B-101")
b = Equipment("C-310")

print(Equipment.registered)
print(a.registered)
print(a._Equipment__tag)
print(hasattr(a, "__tag"))
```

Explain in two lines why the class counter stayed where it stayed, and which line repairs it.

### 04.2 · Apply
A gauge that rejects the impossible.

Write the class `PressureGauge` with a public `tag` and the pressure kept in a private attribute. The pressure is exposed as a property with a setter, and the setter raises `ValueError` when the value leaves the 0.0 to 10.0 bar range, with a message carrying the rejected value. The constructor assigns through the property, not through the private attribute.

Add the alternative constructor `from_psi(tag, psi)` as a class method, with the factor 0.0689476.

Test it like this: build PT-205 at 6.1 bar and print it with two decimals; raise it to 9.0 and print it; try to set it to 12.5 inside a `try` and print the error message; print the pressure again to show it did not change; build PT-301 from 120.0 psi and print it.

### 04.3 · Integrate
A tank that does not overflow.

Write the class `Tank` with public `tag` and `capacity`, the level in a private attribute, and a class attribute `installed` counting how many tanks have been built. Expose `level` and `percent` as read-only properties. The methods `fill(litres)` and `drain(litres)` raise `ValueError` when the operation would leave the tank overflowing or in negative.

Build TQ-01 with capacity 5000.0 L and level 1200.0, and TQ-02 with capacity 2000.0 L and level 800.0. Fill TQ-01 with 2000 L and print its status. Then try to drain 4000 L from it and to fill it with another 3000 L, each attempt inside its own `try`, printing whatever message arrives. Drain 1200 L, print the status of both tanks and the class counter.

The status format is `TQ-01: 3200 L (64.0 %)` and comes out of a separate function that takes the tank and returns the string.

## Week 05 · Topic 2 · Building blocks

### 05.1 · Recognise
Two methods with the same name.

This file is called `recorder.py`. Predict what the first call prints, what happens with the second, and write the complete error type.

```python
class Recorder:
    def record(self, tag, value):
        print("two values:", tag, value)

    def record(self, tag, value, unit):
        print("three values:", tag, value, unit)


r = Recorder()
r.record("TT-101", 74.5, "C")
r.record("PT-205", 6.1)
```

Rewrite the class with a single method covering both cases, with no `if` on the number of arguments.

### 05.2 · Apply
Stock that adds up and compares.

Write the class `StockItem` with `code` and `pieces`, and three magic methods:

- `__str__` returns `BL-220 x12`;
- `__eq__` compares code and pieces, not identity;
- `__add__` returns a new stock item with the pieces added, and raises `ValueError` when the codes do not match.

With `store = StockItem("BL-220", 12)` and `delivery = StockItem("BL-220", 8)`, print the store, the sum of the two, the comparison against `StockItem("BL-220", 12)`, the comparison against the delivery, and the error message from trying to add `StockItem("SM-4471", 6)` to it inside a `try`.

### 05.3 · Integrate
An inventory that takes whatever arrives.

Write the module `inventory.py` with the class `StockItem` from 05.2 (only `__str__`) and the class `Inventory`, which keeps a private dictionary of code to pieces.

The method `receive(*codes, **options)` accepts as many codes as arrive. The option `pieces` says how many of each, and is 1 when it is not passed. The option `notify` prints `2 codes received at North Warehouse` when it is true. The method `listing()` returns a list of `StockItem` objects, and `__str__` returns `North Warehouse: 3 codes, 39 pieces`.

Below that, a block that runs only when the file is executed and not when it is imported: receive BL-220 and SM-4471 with 4 pieces, notifying; receive EM-905 with 30 pieces; receive BL-220 again without saying how many; print the listing line by line and then the inventory.

## Week 06 · Topic 3 · Core properties

### 06.1 · Recognise
The getter that handed back the real list.

The logbook promises every entry ends up in capitals. Predict the three outputs and say whether the promise held.

```python
class Logbook:
    def __init__(self):
        self.__entries = []

    def record(self, text):
        self.__entries.append(text.upper())

    def entries(self):
        return self.__entries


b = Logbook()
b.record("fault on B-101")
b.entries().append("all good")

print(len(b.entries()))
print(b.entries()[0])
print(b.entries()[1])
```

The attribute carries two leading underscores. Explain in one line why that was not enough, and write the one-line fix.

### 06.2 · Apply
Fault counter with square brackets.

Write the class `FaultCounter`, keeping a private dictionary of tag to number of faults. The only rule of the class is that the tag gets normalised to capitals, and that rule lives inside the class and nowhere else.

Expose three things and nothing more: `record(tag)`, the square bracket operator for reading and writing, and `len`. Asking for a tag that never failed returns 0 instead of raising `KeyError`.

Test it by recording `"B-101"`, `"b-101"` and `"C-310"`, then print: the count for B-101, the one for b-101, the one for V-12, the total number of tags, the result of assigning 5 to `counter["v-12"]`, and the total again.

### 06.3 · Integrate
A station built by composition.

Write three classes with not one line of inheritance between them:

- `Sensor` with `tag`, `low`, `high` and `in_range(value)`.
- `Logbook` with a private list, `record(text)` storing in capitals, `entries()` returning a copy and `__len__`.
- `Station`, which takes a dictionary of sensors and a logbook in the constructor and delegates to them. Its method `measure(tag, value)` asks the sensor whether the value is in range and, when it is not, asks the logbook to record `TT-101 out of range at 412.0`. The method `history()` returns whatever the logbook hands over.

Build the North Plant station with TT-101 from 0.0 to 400.0 and PT-205 from 0.0 to 10.0. Measure 412.0 on TT-101, 6.1 on PT-205 and 11.2 on PT-205. Then try to add a fake entry to the history from outside, print the whole history and its size. The fake entry must not show up.

## Week 07 · Topic 3 · Core properties

### 07.1 · Recognise
The subclass that forgot its parent.

The file is called `equipment.py`. The first line prints fine. Predict what happens with the second, with which error type and over which attribute.

```python
class Equipment:
    def __init__(self, tag):
        self.tag = tag
        self.hours = 0.0


class Pump(Equipment):
    def __init__(self, tag, flow):
        self.flow = flow

    def card(self):
        return f"{self.tag}: {self.flow} L/s"


b101 = Pump("B-101", 120.0)
print(b101.flow)
print(b101.card())
```

Write the missing line and the exact spot in the constructor where it goes.

### 07.2 · Apply
Equipment with a shared parent.

Write the class `Equipment` with the protected attributes `_tag` and `_hours`, the method `summary()` returning `B-101 with 4820 h`, and `log_hours(run)`.

Hang two children off the same parent, each one chaining its constructor with `super`:

- `Pump` adds `flow` and the method `start()`, returning `B-101 starts at 120.0 L/s`;
- `Compressor` adds `pressure` and the method `purge()`, returning `C-310 purges at 8.5 bar`.

Both new methods read `_tag` from the parent. Build B-101 with 4820.0 h and 120.0 L/s, and C-310 with 6300.0 h and 8.5 bar. Print the summary and the method of the pump, log 40 hours on the compressor, print its summary and its own method, and close with `isinstance` of the pump against `Equipment` and against `Compressor`, plus `issubclass` of `Compressor` against `Equipment`.

### 07.3 · Integrate
Flattening a six-level hierarchy.

The vendor delivered this tree. It compiles, it runs, and nobody understands it.

```python
class Asset: ...
class RotatingEquipment(Asset): ...
class Pump(RotatingEquipment): ...
class DosingPump(Pump): ...
class PumpWithDrive(DosingPump): ...
class VariableSpeedDrive(PumpWithDrive): ...
```

Flatten it to two levels at most, applying the "is a" test out loud to every relation. One of the six classes fails the test in every reading, and has to leave the tree and come back in by composition.

Hand in the code with `Asset` as the parent, its direct children, and the class that left received as a constructor parameter defaulting to `None`. Test with B-101 without that part, B-102 with a Danfoss part at 45.0 Hz, and C-310 as a compressor. Print the summary of B-101, how each pump starts, adjust the part to 38.0 Hz, print how B-102 starts now, the summary of C-310, and two `isinstance` calls showing the composed part is no part of the hierarchy. Add one line of justification for every relation you kept.

## Week 08 · Topic 3 · Core properties

### 08.1 · Recognise
Who decides which method runs.

`report` is written once, in the parent class. Predict the four outputs and say, for each object, which `draw_kw` ran and why.

```python
class Equipment:
    def __init__(self, tag):
        self.tag = tag

    def draw_kw(self):
        return 0.0

    def report(self):
        print(f"{self.tag}: {self.draw_kw():.1f} kW")


class Motor(Equipment):
    def draw_kw(self):
        return 45.0


class Compressor(Equipment):
    def draw_kw(self):
        return 75.0

    def report(self):
        super().report()
        print(f"{self.tag}: check the filter")


for item in [Equipment("V-12"), Motor("M-204"), Compressor("C-310")]:
    item.report()
```

Answer as well what would change if `Compressor.report` called `super().report()` at the end instead of at the start.

### 08.2 · Apply
Instruments with a compulsory contract.

Write the abstract class `Instrument` inheriting from `ABC`. Its constructor takes `tag` and leaves `calibrated` false. It carries the concrete method `calibrate()`, which sets `calibrated` to true, and the abstract method `read()`.

Write three concrete children: `Thermocouple` returns `TT-101: 74.5 C`, `PressureGauge` returns `PT-205: 6.1 bar` and `FlowMeter` returns `FT-330: 118.0 L/s`.

Build the list `panel` with one object of each class, walk it calibrating and printing the reading and the calibration state. The loop may not ask what class each object is. Close by trying to build `Instrument("XX-000")` inside a `try` and printing the message of the `TypeError`.

### 08.3 · Integrate
The whole plant, revision for the first midterm.

Close units 1, 2 and 3 in a single file. Write the abstract class `Equipment(ABC)` with:

- the class attribute `census`, counting how many pieces of equipment were built;
- a protected `_tag` and the hours in a private attribute;
- the read-only properties `tag` and `hours`;
- `log_hours(run)`, raising `ValueError` on negative hours;
- the abstract method `draw_kw()`;
- the concrete method `report()`, returning `B-101: 4820 h, 38.4 kW`.

`Pump` takes a flow and draws 0.32 kW for every L/s. `Compressor` takes a pressure, draws 8.0 kW per bar, and extends `report()` by adding ` (air)` at the end with `super`. `Valve` is declared inheriting from `Equipment` and does not implement `draw_kw`, on purpose.

Walk a list with B-101 (4820.0 h, 120.0 L/s) and C-310 (6300.0 h, 8.5 bar) printing each report and accumulating the total draw. Log 180 hours on the pump and print its report again. Try to log 5 negative hours and to build the valve, each attempt in its own `try`, and print both messages. Close with the census.

## Week 09 · Topic 4 · Advanced functions and structures

### 09.1 · Recognise
The history nobody agreed to share.

Predict the four outputs. The third and the fourth are the reason for the exercise.

```python
def record_fault(tag, history=[]):
    history.append(tag)
    return history


print(record_fault("B-101"))
print(record_fault("C-310"))
print(record_fault("V-12", []))
print(record_fault("M-204"))
```

Explain in one line the exact moment the list shared by the calls was created, and write the corrected signature.

### 09.2 · Apply
Spare parts sorted by stock.

The store hands over the spare parts as tuples of code, description and pieces:

```python
spares = [
    ("BL-220", "bearing", 12),
    ("SM-4471", "mechanical seal", 6),
    ("EM-905", "gasket", 30),
    ("RT-118", "oil seal", 2),
]
```

Write three functions:

1. `by_stock(spares)` returns a new list sorted from fewest to most pieces, with `key` and a lambda, leaving the original list alone.
2. `critical(spares, minimum)` returns the codes holding fewer pieces than the minimum. It returns, it does not print.
3. `show(spares)` numbers the sorted listing with `enumerate` starting at 1, in the format `1. RT-118 oil seal: 2`.

Print the listing, the critical codes with a minimum of 5, and at the end the code of the first tuple of the original list, to show it is still intact.

### 09.3 · Integrate
Counting the pieces of a bill of materials.

The bill of materials for pump B-101 arrives as nested dictionaries. Every node carries its name, how many pieces it is and its parts:

```python
PUMP = {
    "name": "B-101",
    "pieces": 1,
    "parts": [
        {
            "name": "rotor assembly",
            "pieces": 1,
            "parts": [
                {"name": "impeller", "pieces": 1, "parts": []},
                {"name": "bearing BL-220", "pieces": 2, "parts": []},
            ],
        },
        {"name": "seal SM-4471", "pieces": 2, "parts": []},
        {"name": "bolt", "pieces": 8, "parts": []},
    ],
}
```

Write three recursive functions, each one with an explicit base case:

1. `count_pieces(node)` adds the pieces of the node and of everything hanging off it. For this pump it gives 15.
2. `depth(node)` returns how many levels the tree has, counting the node it received. For this pump it gives 3.
3. `leaves(node)` returns the list of names of the parts that have no parts of their own, in the order they appear.

None of the three prints anything inside. The third accumulates into a list that cannot be the default value of the parameter, for the reason you saw in 09.1.

## Week 10 · Topic 4 · Advanced functions and structures

### 10.1 · Recognise
Alias, set and accumulator.

Predict the four outputs. Count the first one carefully: one line modifies the list through the other name.

```python
readings = [74.5, 74.5, 118.0, 6.1, 118.0]
backup = readings

backup.append(6.1)
unique = set(readings)

counts = {}
for value in readings:
    counts[value] = counts.get(value, 0) + 1

print(len(readings), len(unique))
print(counts[118.0], counts[6.1])
print(backup is readings)
print(counts.get(9.9, 0))
```

Explain in one line what would have changed if the second line read `backup = list(readings)`.

### 10.2 · Apply
Filtering faults and grouping them.

With this shift data:

```python
faults = [
    ("B-101", "vibration"),
    ("C-310", "overheating"),
    ("B-101", "leak"),
    ("V-12", "leak"),
    ("B-101", "vibration"),
]

readings = [74.5, 118.0, 6.1, 203.0, 99.9, 118.0]
```

Answer four queries, each one with the mechanism named:

1. The tags of the equipment with a leak fault, with a list comprehension.
2. How many faults each piece of equipment had, with an accumulator dictionary and `get`.
3. The readings above 100, with a list comprehension.
4. The tags from point 1, with no repeats and sorted.

Print the four results, one per line.

### 10.3 · Integrate
A roster with the right container.

The plant roster arrives as a list of dictionaries with `tag`, `type` and `hours`, with five pieces of equipment: B-101 pump 4820.0, B-102 pump 1150.0, C-310 compressor 6300.0, M-204 motor 2210.0 and V-12 valve 300.0.

Write the class `Roster`, which takes that list in the constructor and keeps inside, in private attributes, whatever structures are needed. Expose five methods, and each one has to use the container that answers it without walking more than it needs:

- `exists(tag)` answers whether the tag is registered;
- `hours(tag)` returns the hours of one piece of equipment, or 0.0 when it does not exist;
- `sorted_tags()` returns the tags in alphabetical order;
- `by_type()` returns a dictionary of type to count;
- `overdue(limit)` returns the tags with more hours than the limit.

Print: whether C-310 exists and whether X-999 exists, on the same line; the hours of B-101; the sorted list; the count by type; and the overdue ones with a limit of 5000. In the written justification say, one line per method, which container you chose and why.

## Week 11 · Topic 4 · Advanced functions and structures

### 11.1 · Recognise
The order finally runs in.

Predict the complete output, in order, with the six lines that show up.

```python
def read(value):
    try:
        return 100 / float(value)
    except ValueError:
        return -1.0
    except ZeroDivisionError:
        return 0.0
    finally:
        print("attempt", value)


print(read("4"))
print(read("0"))
print(read("n/a"))
```

Answer as well which exception `float("n/a")` raises, and why the second `except` never gets examined on that call.

### 11.2 · Apply
An exception named after the problem.

Define `ReadingOutOfRange` inheriting from `Exception`. Write the class `Sensor` with public `tag`, `low` and `high`, and the value kept in a private attribute that starts at the low end.

Expose the value as a property with a setter. The setter raises `ReadingOutOfRange` when the reading leaves the range, with a message giving the tag, the measured value and the full range.

Build TT-101 from 0.0 to 400.0 and walk the readings 74.5, 412.0 and 180.0. Every assignment goes in its own `try`. When the value is rejected, print the class name of the exception and its message. When it goes through, print the confirmation from the `else` clause. Close by printing the last value that did get stored.

### 11.3 · Integrate
Ingesting dirty telemetry.

The acquisition system hands over this, and not one of the seven tuples can be taken on trust:

```python
raw = [
    ("TT-101", "74.5"),
    ("PT-205", "6.1"),
    ("TT-101", "412.0"),
    ("XX-999", "12.0"),
    ("FT-330", "n/a"),
    ("PT-205", None),
    ("FT-330", "118.0"),
]
```

Define three exceptions of your own: `InvalidReading` inherits from `Exception`, and `ReadingOutOfRange` and `UnknownSensor` inherit from the first.

Write `validate(tag, text)`, which validates at the boundary and returns a `float`. Reject the tag that is not in the `RANGES` dictionary holding TT-101 from 0.0 to 400.0, PT-205 from 0.0 to 10.0 and FT-330 from 0.0 to 200.0. Reject the missing datum. Reject the text that does not convert. Reject the value out of range. Every rejection carries its type and a message saying what to correct.

The main program walks the tuples with one `try` per turn and three `except` in the right order, most specific to most general. For every rejection it prints a different label depending on the type. At the end it prints how many were accepted, how many were rejected and the average of the accepted ones with two decimals.

## Week 12 · Topic 5 · Files

### 12.1 · Recognise
The mode that wipes on opening.

The file `logbook.txt` does not exist when the program starts. Predict exactly what it prints, second line included.

```python
from pathlib import Path

path = Path("logbook.txt")

with open(path, "w", encoding="utf-8") as f:
    f.write("08:00 B-101 starts\n")

with open(path, "a", encoding="utf-8") as f:
    f.write("09:15 PT-205 at 6.1 bar\n")

with open(path, "w", encoding="utf-8") as f:
    f.write("11:40 C-310 alarm\n")

print(path.read_text(encoding="utf-8"))
print(len(path.read_text(encoding="utf-8")))
```

Say at what instant the 08:00 line disappeared, and which of the three openings kept what was already there.

### 12.2 · Apply
Telemetry that goes out to CSV and comes back.

Write a program that stores these five readings in `telemetry.csv` and then reads them back to average them per instrument:

```python
rows = [
    {"tag": "TT-101", "value": 74.5},
    {"tag": "PT-205", "value": 6.1},
    {"tag": "TT-101", "value": 81.2},
    {"tag": "FT-330", "value": 118.0},
    {"tag": "PT-205", "value": 6.4},
]
```

The write uses `DictWriter` with a header, and the read uses `DictReader`, so the program cannot assume the order of the columns. Both accesses go inside a `with`, with `newline=""` and `encoding="utf-8"` spelled out. The average accumulates with one dictionary of totals and another of counts.

Print one line per instrument in the format `TT-101: 77.85 (n=2)`, in the order they first appeared.

### 12.3 · Integrate
A logbook that outlives the program.

Write the class `Logbook`, which takes a `Path` in the constructor and stores every event as a row of a CSV with the columns `time`, `tag` and `text`.

- `record(time, tag, text)` opens in append mode and writes the header only the first time, while the file does not exist yet.
- `entries()` returns the list of dictionaries, and returns an empty list when the file is not there, catching `FileNotFoundError` by name.
- `report(target)` counts events per piece of equipment and writes a text file with the header `Events per equipment` and one line per piece of equipment.

Test it by recording four events: 08:00 B-101 normal start, 09:15 PT-205 reading 6.1 bar, 11:40 C-310 temperature alarm and 13:05 B-101 shutdown for maintenance. Print how many entries are there, the four line by line, the contents of the report, and last of all the size of a logbook pointed at a file that does not exist.

## Week 13 · Topic 5 · Files

### 13.1 · Recognise
The cursor, byte by byte.

Predict the five outputs. The last one separates whoever understood the cursor from whoever assumed it.

```python
from pathlib import Path

path = Path("index.bin")

with open(path, "wb") as f:
    f.write(b"B-101B-102C-310")

with open(path, "rb") as f:
    print(f.tell())
    f.seek(5)
    print(f.read(5))
    print(f.tell())
    f.seek(10)
    print(f.read(5))
    print(f.read(5))
```

Explain in one line why the last read returns what it returns, and where the cursor ended up.

### 13.2 · Apply
Fixed-size records.

Write a program that stores the tags `["B-101", "B-102", "C-310", "M-204"]` in `equipment.bin` as binary records of 32 bytes each, padded with spaces on the right through the format specifier of the f-strings and encoded in UTF-8.

Write the function `read_record(path, number)`, which opens the file in binary mode, jumps straight to the record asked for without reading the ones before it, reads its 32 bytes and returns the tag without the padding spaces. The position is worked out from the record number and the fixed size.

Print how many bytes the whole file takes, and then records 2, 0 and 3, in that order.

### 13.3 · Integrate
From the CSV to the binary index.

Close units 4 and 5. The program writes `telemetry.csv` with these five rows and from then on works on the file, not on the list:

```python
rows = [
    {"tag": "TT-101", "value": "74.5"},
    {"tag": "PT-205", "value": "6.1"},
    {"tag": "TT-101", "value": "81.2"},
    {"tag": "FT-330", "value": "118.0"},
    {"tag": "PT-205", "value": "n/a"},
]
```

Write four functions:

1. `read_readings(path)` returns the list of dictionaries with `DictReader`, or an empty list when the file does not exist.
2. `summarise(readings)` returns a dictionary of tag to average. The row that does not convert to a number is discarded, printing `Discarded: PT-205 sent n/a` and carrying on with the next turn.
3. `write_index(path, averages)` stores one binary record of 40 bytes per instrument, with the tag left aligned in 10 positions and the average right aligned in 10 with two decimals. It raises the custom exception `EmptyIndex` when there is nothing to index.
4. `read_index(path, number)` jumps to the record asked for and returns its contents without padding. It raises `IndexError` with a message of its own when the record does not exist.

Print how many rows were read and how many instruments were left, the averages with two decimals, record 1 and record 0 of the index, and last the messages of the two errors: asking for record 9, and writing an index from an empty dictionary. Each attempt goes in its own `try`.

## Week 14 · Topic 6 · Graphical interfaces

### 14.1 · Recognise
The parentheses that fire the click.

This window never gets as far as opening. Say what gets printed, how many times, at what moment, and what `connect` receives as its argument.

```python
class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        button = QPushButton("Look up", self)
        button.clicked.connect(self.on_look_up())

    def on_look_up(self):
        print("click")
```

Write the fix and explain in one line what `connect` stores once the fix is in. Answer as well what other problem this window would have even with `connect` correct, knowing that `button` was not stored on `self`.

### 14.2 · Apply
A window that normalises tags.

Write `TagWindow`, inheriting from `QMainWindow`, with the title `Tag normaliser` and geometry 200, 200, 380, 140. Every control hangs off a central `QWidget` and is placed with coordinates, because layouts arrive next week.

- a `QLineEdit` with the placeholder text `b-101`, at 20, 20, 220, 28;
- a `QPushButton` labelled `Normalise`, at 250, 20, 110, 28;
- a `QLabel` starting at `Nothing entered`, at 20, 70, 340, 28.

The button connects to a slot that computes nothing: it reads the box, hands it to the free function `normalise(tag)` and puts the result in the label. The function strips the edges, converts to capitals and returns `Nothing entered` when nothing is left. All three controls are stored on `self`.

Hand in the `.py` file and a screenshot of the window after typing `  b-101 ` and pressing the button.

### 14.3 · Integrate
The window asks, the panel decides.

Write two files. `panel.py` holds the exception `UnknownTag` and the class `Panel`, with a private dictionary of tag to a pair of value and unit. Its method `record(tag, value, unit)` normalises the tag to capitals, and `read(tag)` strips spaces, normalises, raises `UnknownTag` when the tag is not registered and returns `TT-101: 74.5 C` when it is. Below that, a block that runs only when the file is executed, testing the class from the console with `tt-101`, with `  PT-205 ` and with `XX-999`.

`window.py` holds `PanelWindow`, which takes the assembled panel in the constructor, stores it, and builds box, button and label as in 14.2. The slot calls `panel.read` inside a `try` and puts either the result or the message of the exception in the label.

`panel.py` may not import PyQt6. Hand in both files, the console output of the first, and a screenshot of the window looking up a tag that does not exist.

## Week 15 · Topic 6 · Graphical interfaces

### 15.1 · Recognise
Where the button lands in the grid.

The grid receives five controls from the plant panel. Draw the resulting grid and say which cells each one occupies.

```python
grid = QGridLayout(central)

grid.addWidget(QLabel("B-101"), 0, 0)
grid.addWidget(QLabel("C-310"), 1, 0)
grid.addWidget(QLabel("M-204"), 2, 0)
grid.addWidget(stop_button, 0, 1, 2, 1)
grid.addWidget(start_button, 2, 1, 1, 2)
```

Answer three things: what each of the four numbers of `addWidget` means, which of the two buttons is taller and which is wider, and what would happen if somebody added another label at position 0, 1.

### 15.2 · Apply
An entry form with layouts.

Redo the work order entry without a single coordinate. The window inherits from `QMainWindow`, with the title `New work orders` and geometry 200, 200, 460, 320.

On the central widget goes a `QVBoxLayout`, and inside it, in this order:

1. a `QFormLayout` with four rows labelled `Number`, `Equipment`, `Priority` and `Description`, each one with its `QLineEdit`;
2. a `QHBoxLayout` with the buttons `Save` and `Clear`;
3. a notice `QLabel` starting at `Enter a work order`;
4. a `QListWidget` where what has been entered piles up.

Save adds to the list a row with number, equipment and priority, updates the notice with the running total and clears the four fields. Clear only empties the fields. Each button connects to its own slot.

Hand in the file and two screenshots: the window at its original size and the same window stretched to double the width, to show that nothing overlaps.

### 15.3 · Integrate
The domain that knows nothing about Qt.

Split the window of 15.2 into two files.

`register.py` holds the exception `InvalidData`, the class `WorkOrder` with `number`, `tag`, `priority`, `description` and a `__str__` returning `OT-1042 B-101 P1: Mechanical seal replacement`, and the class `Register` with a private list of orders. Its method `add(number, tag, priority, description)` takes the four fields as text, validates them in that order and raises `InvalidData` with the message that fits:

- the number carries at least six characters;
- the tag carries at least three;
- the priority has to convert to an integer and land between 1 and 3;
- the description cannot be empty.

When everything passes, it builds the order with the tag in capitals, stores it and returns it. Add `listing()` and `__len__`. Below that, a block that runs only when the file is executed, entering OT-1042 on b-101 with priority 1 and OT-1043 on C-310 with priority 3, and then attempting three bad entries: a short number, priority 9, and a priority written as a word. Print the two good orders, the three rejection messages and the total.

`window.py` holds the same window as 15.2, except that the save slot calls `register.add` inside a `try`. When the exception arrives, the message goes into the notice label and nothing is added to the list. `register.py` may not import PyQt6, and the slot may not validate anything on its own.

## Week 16 · Topic 7 · Databases and project

### 16.1 · Recognise
The connection that closed without committing.

The file `spares.db` does not exist when the program starts. Predict the two outputs.

```python
import sqlite3
from pathlib import Path

path = Path("spares.db")

connection = sqlite3.connect(path)
connection.execute(
    "CREATE TABLE IF NOT EXISTS SpareParts (code TEXT PRIMARY KEY, pieces INTEGER)")
connection.commit()
connection.close()

connection = sqlite3.connect(path)
connection.execute("INSERT INTO SpareParts VALUES ('BL-220', 12)")
connection.close()

connection = sqlite3.connect(path)
cursor = connection.execute("SELECT COUNT(*) FROM SpareParts")
print(cursor.fetchone())

connection.execute("INSERT INTO SpareParts VALUES ('SM-4471', 6)")
connection.commit()
connection.close()

connection = sqlite3.connect(path)
cursor = connection.execute("SELECT COUNT(*) FROM SpareParts")
print(cursor.fetchone())
connection.close()
```

Explain why the bearing never reached the disk and the seal did, and why `fetchone` returns what it returns instead of a bare number.

### 16.2 · Apply
Spare parts in a table.

Write a program that creates `store.db` with the table `SpareParts`, of columns `code` as the primary key, `description` mandatory and `pieces` mandatory. Insert these four with a loop, one `execute` call per part, passing the values as parameters:

```python
spares = [
    ("BL-220", "bearing", 12),
    ("SM-4471", "mechanical seal", 6),
    ("EM-905", "gasket", 30),
    ("RT-118", "oil seal", 2),
]
```

Then query three things, always with placeholders and never gluing the value inside the string: the codes and pieces of whatever holds fewer than 10 pieces, ordered by pieces; the description of code EM-905; and the total number of rows. Print whatever each query returns exactly as it arrives.

Everything goes inside `with` blocks, with an explicit `commit` after the inserts. Note in a comment what has to happen before the program runs again, and why.

### 16.3 · Integrate
Objects that travel to the database and back.

Separate the domain from the data access in a single file, with the rule that `SparePart` may not import `sqlite3`.

`SparePart` has `code`, `description` and `pieces`, the method `issue(quantity)` that raises `ValueError` when the pieces do not cover it, and a `__str__` returning `BL-220 (bearing): 12`.

`SQLiteStore` takes the path, creates the table if it does not exist in the constructor, and exposes three methods, with every piece of SQL in the program living inside it: `save(part)`, `load(code)` returning a `SparePart` object or raising the custom exception `SparePartNotFound`, and `below_minimum(minimum)` returning a list of objects ordered by pieces.

Save BL-220 bearing 12, SM-4471 mechanical seal 6 and RT-118 oil seal 2. Load BL-220, issue 9 pieces from it and print the object. Straight after, load BL-220 from the database again and print that too. The two numbers differ: explain in a paragraph why, and which method the access class would need for them to stop differing.

Close by printing what sits below a minimum of 10, and the messages from loading XX-999 and from issuing 100 pieces from the object, each attempt in its own `try`.

## Week 17 · Final assessment

### 17.1 · Recognise
Four rules in a single trace.

Predict the four outputs. Each one depends on a different rule from the term.

```python
class Asset:
    census = 0

    def __init__(self, tag):
        self.__tag = tag
        Asset.census += 1

    @property
    def tag(self):
        return self.__tag

    def kind(self):
        return "asset"

    def card(self):
        return f"{self.tag}/{self.kind()}"


class Rotating(Asset):
    def kind(self):
        return "rotating"


class Pump(Rotating):
    def __init__(self, tag, flow):
        super().__init__(tag)
        self.flow = flow

    def kind(self):
        return "pump " + super().kind()


b101 = Pump("B-101", 120.0)

print(b101.card())
print(Asset.census)
print(hasattr(b101, "_Asset__tag"), hasattr(b101, "__tag"))

try:
    b101.tag = "B-999"
except AttributeError:
    print("the property has no setter")
```

Name the four rules: why `card`, written in the topmost class, ends up calling the method of the granddaughter; why the census holds the number it holds; what happened to the name of the private attribute; and what the property is missing.

### 17.2 · Apply
Contract, validation and export.

Write the abstract class `Equipment(ABC)` whose constructor validates and raises the custom exception `InvalidData`: the tag carries at least three characters, and the hours cannot be negative. The tag is stored clean and in capitals in a protected attribute, and the hours in a private one. Expose `tag` and `hours` as read-only properties. Declare `draw_kw()` and `kind()` abstract, and write the concrete method `row()`, returning a dictionary with the keys `tag`, `type`, `hours` with no decimals and `kw` with one.

`Pump` takes a flow and draws 0.32 kW for every L/s. `Compressor` takes a pressure and draws 8.0 kW per bar.

Write the function `export(equipment, path)`, which stores a CSV with `DictWriter` and a header, inside a `with`, with an empty `newline` and an explicit `encoding`.

Build the plant with `b-101` at 4820.0 h and 120.0 L/s, `B-102` at 1150.0 h and 95.0 L/s, and `c-310` at 6300.0 h and 8.5 bar. Then try to add two bad pieces of equipment, `XX` with 100.0 h and `B-103` with negative hours, each in its own `try`, and print the messages. Export to `equipment.csv`, print the contents of the file and the total number of pieces of equipment that made it in.

### 17.3 · Integrate
From telemetry to report.

The final exam is integrative: a single question touches modelling, collections, errors, files and persistence. This exercise has that shape.

Write a program that takes the raw telemetry, validates it against the instrument panel, stores what is accepted in SQLite and produces a report in text.

- `Instrument(ABC)` takes tag, low and high, exposes `tag` as a property, declares `unit()` abstract, and carries the concrete method `validate(text)`, which converts to `float` and raises `InvalidReading` when the text is not a number or when the value leaves the range. The range message includes the unit. The children are `Thermocouple` in C, `PressureGauge` in bar and `FlowMeter` in L/s.
- `History` takes the path of the database, creates the table `Readings` in the constructor with `id` as the primary key, `tag` and `value`, and exposes `save(tag, value)` and `values(tag)`. Every piece of SQL lives in this class and uses placeholders.
- `load_raw(path)` reads the CSV with `DictReader` and returns an empty list when the file does not exist.
- `write_report(path, summary, discarded)` writes the header `Telemetry report`, one line per instrument with two decimals, the count of discarded readings, and one indented line per reason.

The panel holds TT-101 from 0.0 to 400.0, PT-205 from 0.0 to 10.0 and FT-330 from 0.0 to 200.0. The program first writes `raw.csv` with these seven rows and from then on works on the file, not on the list:

```python
raw = [
    {"tag": "TT-101", "value": "74.5"},
    {"tag": "PT-205", "value": "6.1"},
    {"tag": "TT-101", "value": "81.2"},
    {"tag": "FT-330", "value": "118.0"},
    {"tag": "PT-205", "value": "n/a"},
    {"tag": "TT-101", "value": "412.0"},
    {"tag": "XX-999", "value": "3.0"},
]
```

The tag that is not on the panel is discarded with a check up front, no exception involved. The rest is validated in a `try` with the type named. The average of each instrument is computed over what the database returned, not over the list in memory. At the end it prints the whole report and the stored values of TT-101.
