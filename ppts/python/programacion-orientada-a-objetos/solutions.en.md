# Solutions · Object-Oriented Programming · COM102

Professor's copy. Every exercise carries the solution as it ran on Python 3.13, the real output it produced, a ten-point rubric and the mistake that turns up most often while marking. The week 14 and 15 solutions that open a window were checked against the PyQt6 documentation and compiled with `py_compile`, but they were not executed here, because PyQt6 is not installed on the marking machine. That is flagged where it matters.

## Week 01 · Course orientation

### 01.1 · Recognise
**Solution**
```text
Line 4: tag[0] is 'B' and tag[-1] is 'P', the last letter of PUMP.
Line 5: the slice [0:5] takes position 0 and stops before position 5, so it
        gives B-101.
Line 6: hours is text, not a number. "4820" * 2 repeats the string and leaves
        "48204820", eight characters long. That is why it prints 8 and not 4.
Line 7: the plus sign between two strings joins them, it does not add them.
Line 12: the loop accumulates 10 + 20 + 30.
```
**Output**
```text
B P
B-101
8
48200
60
```
**Rubric** (totals 10)
| Criterion | Points |
|---|---|
| The five output lines, exact | 5 |
| Explains that hours is a str and that the asterisk repeats | 3 |
| Explains the slice rule and the negative index | 2 |

**Most common mistake**
They answer 4 on the third line because they read 4820 as a number, and they give themselves away by also answering 9640 on the fourth.

### 01.2 · Apply
**Solution**
```python
def classify_pressure(bar: float) -> str:
    if bar < 2.0:
        return "low"
    if bar <= 8.0:
        return "normal"
    return "high"


readings = [1.4, 2.0, 6.7, 8.0, 9.3]

for reading in readings:
    print(f"{reading:.1f} bar -> {classify_pressure(reading)}")
```
**Output**
```text
1.4 bar -> low
2.0 bar -> normal
6.7 bar -> normal
8.0 bar -> normal
9.3 bar -> high
```
**Rubric** (totals 10)
| Criterion | Points |
|---|---|
| The function returns the string instead of printing it | 4 |
| Both boundaries, 2.0 and 8.0, land on normal | 3 |
| The line format and the single decimal with an f-string | 3 |

**Most common mistake**
They write `print` inside the function and `return` never appears, so the loop prints `None` at the end of every line.

### 01.3 · Integrate
**Solution**
```python
readings = [
    ("TT-101", "74.5"),
    ("PT-205", "6.1"),
    ("TT-101", "n/a"),
    ("FT-330", "118.0"),
    ("PT-205", "6.4"),
    ("FT-330", "no data"),
]


def separate(records: list) -> tuple:
    valid = []
    discarded = 0
    for tag, text in records:
        try:
            valid.append((tag, float(text)))
        except ValueError:
            discarded += 1
    return valid, discarded


def average(values: list) -> float:
    total = 0.0
    for value in values:
        total += value
    return total / len(values)


def tags(records: list) -> list:
    every = []
    for tag, text in records:
        every.append(tag)
    return sorted(set(every))


valid, discarded = separate(readings)

numbers = []
for tag, value in valid:
    numbers.append(value)

print(f"Valid: {len(valid)}")
print(f"Discarded: {discarded}")
print(f"Average: {average(numbers):.2f}")
print(tags(readings))
```
**Output**
```text
Valid: 4
Discarded: 2
Average: 51.25
['FT-330', 'PT-205', 'TT-101']
```
**Rubric** (totals 10)
| Criterion | Points |
|---|---|
| The try wraps the conversion only, and names ValueError | 4 |
| The three functions return, and none prints inside | 3 |
| The tags with no repeats come from a set, not from a loop with an if | 2 |
| The average comes out with two decimals | 1 |

**Most common mistake**
They put the whole loop inside a single `try`: the first bad reading cuts the walk short and the average comes out of two values instead of four.

## Week 02 · Topic 1 · Introduction to OOP

### 02.1 · Recognise
**Solution**
```text
remove deleted B-102 from tags and left hours untouched. The loop walks the two
positions tags has left and reads hours by that same position, so C-310 takes
the 1150 hours that belonged to B-102, and its own 6300 are left orphaned at
the end of the list.

The missing line was hours.remove(1150), or better, deleting by index in both
lists at once. Python does not complain because it has no idea the two lists
travel together: that relation lives only in the head of whoever wrote the
program.
```
**Output**
```text
B-101 4820
C-310 1150
```
**Rubric** (totals 10)
| Criterion | Points |
|---|---|
| The two output lines | 4 |
| Says the 1150 hours belonged to B-102 | 3 |
| Explains that the match between lists is nowhere in the code | 3 |

**Most common mistake**
They answer that the program blows up with `IndexError`. It does not, because the shorter list is the one driving the `range`.

### 02.2 · Apply
**Solution**
```text
1. Function. A number goes in, another comes out, nothing is remembered.
2. Class. The hours and the state survive from one call to the next.
3. Function. It walks and counts; the result is not kept anywhere.
4. Class. Number, equipment and progress only make sense together, and they
   change over time.
5. Function. It takes a list and returns another.
6. Class. Deducting pieces changes something that has to still be there later.
```
```python
def psi_to_bar(psi: float) -> float:
    return psi * 0.0689476


print(f"{psi_to_bar(120):.2f} bar")
print(f"{psi_to_bar(45):.2f} bar")
```
**Output**
```text
8.27 bar
3.10 bar
```
**Rubric** (totals 10)
| Criterion | Points |
|---|---|
| The six cases sorted correctly | 4 |
| Every justification mentions whether there is state or not | 3 |
| The function converts and returns, with two decimals | 3 |

**Most common mistake**
They file point 3 as a class because it says "counting". The verb does not decide. What decides is whether anything survives the call.

### 02.3 · Integrate
**Solution**
```python
tags = ["B-101", "B-102", "C-310", "M-204"]
hours = [4820, 1150, 6300, 2210]
states = ["running", "stopped", "running", "running"]
inspection = [1180, 40, 900, 310]


def to_records(tags: list, hours: list, states: list, inspection: list) -> list:
    records = []
    for i in range(len(tags)):
        records.append({
            "tag": tags[i],
            "hours": hours[i],
            "state": states[i],
            "inspection": inspection[i],
        })
    return records


def retire(records: list, tag: str) -> list:
    left = []
    for item in records:
        if item["tag"] != tag:
            left.append(item)
    return left


def show(records: list) -> None:
    for item in records:
        print(item["tag"], item["hours"], item["state"], item["inspection"])


plant = to_records(tags, hours, states, inspection)
plant = retire(plant, "B-102")

show(plant)
print(len(plant))
```
**Output**
```text
B-101 4820 running 1180
C-310 6300 running 900
M-204 2210 running 310
3
```
**Rubric** (totals 10)
| Criterion | Points |
|---|---|
| One dictionary per piece of equipment, with the four keys | 4 |
| retire returns a new list and does not modify the one it receives | 3 |
| C-310 keeps its 6300 hours after the retirement | 2 |
| Each of the three functions does one job | 1 |

**Most common mistake**
`retire` deletes while walking the same list: the loop skips an element, and the piece of equipment right after the retired one stays in.

## Week 03 · Topic 2 · Building blocks

### 03.1 · Recognise
**Solution**
```text
alarms was declared in the body of the class, so there is a single list for
every pump. self.alarms.append creates nothing new: it looks the name up on the
object, does not find it there, finds it on the class and appends there. B-102
sees the two alarms of B-101, and both names point at the same object.
```
```python
    def __init__(self, tag):
        self.tag = tag
        self.alarms = []
```
**Output**
```text
2
['E12', 'E07']
True
```
**Rubric** (totals 10)
| Criterion | Points |
|---|---|
| The three outputs | 4 |
| Explains that the list lives on the class, not on the object | 3 |
| The fix assigns the list inside __init__, on self | 3 |

**Most common mistake**
They answer 0 and then get caught out by the `True`. The third line is what closes off the escape route of "every object has its own".

### 03.2 · Apply
**Solution**
```python
class Pump:
    def __init__(self, tag: str, flow_l_s: float, hours: float) -> None:
        self.tag = tag
        self.flow_l_s = flow_l_s
        self.hours = hours

    def log_hours(self, run: float) -> None:
        self.hours = self.hours + run

    @property
    def flow_m3_h(self) -> float:
        return self.flow_l_s * 3.6

    @property
    def hours_to_service(self) -> float:
        return 5000 - self.hours


b101 = Pump("B-101", 120.0, 4820.0)

print(f"{b101.tag}: {b101.flow_m3_h:.1f} m3/h")
print(f"Hours to service: {b101.hours_to_service:.0f}")

b101.log_hours(260)

print(f"Hours to service: {b101.hours_to_service:.0f}")
```
**Output**
```text
B-101: 432.0 m3/h
Hours to service: 180
Hours to service: -80
```
**Rubric** (totals 10)
| Criterion | Points |
|---|---|
| Constructor with the three attributes on self | 3 |
| The two properties read without parentheses and compute on the spot | 4 |
| log_hours accumulates instead of replacing | 2 |
| The second result comes out negative and is not clipped to zero | 1 |

**Most common mistake**
They store the flow in m3/h as an attribute inside the constructor: change the litres per second and the other figure goes stale, which is exactly what the property prevents.

### 03.3 · Integrate
**Solution**
```python
class Sensor:
    def __init__(self, tag: str, unit: str, low: float, high: float) -> None:
        self.tag = tag
        self.unit = unit
        self.low = low
        self.high = high

    def in_range(self, value: float) -> bool:
        return value >= self.low and value <= self.high

    @property
    def span(self) -> float:
        return self.high - self.low


sensors = {
    "TT-101": Sensor("TT-101", "C", 0.0, 400.0),
    "PT-205": Sensor("PT-205", "bar", 0.0, 10.0),
    "FT-330": Sensor("FT-330", "L/s", 0.0, 200.0),
}

readings = [
    ("TT-101", 412.0),
    ("PT-205", 6.1),
    ("FT-330", 118.0),
    ("TT-101", 74.5),
    ("PT-205", 11.2),
]

outside = 0
for tag, value in readings:
    sensor = sensors[tag]
    if sensor.in_range(value):
        print(f"{tag} {value} {sensor.unit} inside")
    else:
        print(f"{tag} {value} {sensor.unit} OUTSIDE")
        outside = outside + 1

flow_meter = sensors["FT-330"]

print(f"Out of range: {outside}")
print(f"FT-330 span: {flow_meter.span:.0f} L/s")
```
**Output**
```text
TT-101 412.0 C OUTSIDE
PT-205 6.1 bar inside
FT-330 118.0 L/s inside
TT-101 74.5 C inside
PT-205 11.2 bar OUTSIDE
Out of range: 2
FT-330 span: 200 L/s
```
**Rubric** (totals 10)
| Criterion | Points |
|---|---|
| The Sensor class with its four attributes and the range method | 3 |
| The sensor is looked up by key in a dictionary | 3 |
| The span property computes, it is not stored | 2 |
| The count of out-of-range readings and the format of each line | 2 |

**Most common mistake**
They walk a list of sensors hunting for the tag with a `for` inside the `for` over the readings. It works with three sensors, and it is what week 10 will call "using a list to search".

## Week 04 · Topic 2 · Building blocks

### 04.1 · Recognise
**Solution**
```text
self.registered += 1 reads the 0 from the class, adds one and stores the result
on the object. Every piece of equipment ends up with its own 1 and the class
never finds out, which is why Equipment.registered is still 0 and a.registered
is 1. The attribute with two leading underscores does exist, but renamed to
_Equipment__tag, so hasattr with the original name answers False.

The fix is writing Equipment.registered += 1 inside the constructor.
```
**Output**
```text
0
1
B-101
False
```
**Rubric** (totals 10)
| Criterion | Points |
|---|---|
| The four outputs | 4 |
| Explains that the assignment created an instance attribute | 3 |
| Names the renaming and why hasattr gives False | 2 |
| The fix writes on the class | 1 |

**Most common mistake**
They answer 2 on the first line, which is the right answer for the counter that does work, so they notice nothing until they read the second.

### 04.2 · Apply
**Solution**
```python
class PressureGauge:
    def __init__(self, tag: str, pressure: float) -> None:
        self.tag = tag
        self.pressure = pressure

    @property
    def pressure(self) -> float:
        return self.__pressure

    @pressure.setter
    def pressure(self, value: float) -> None:
        if value < 0.0 or value > 10.0:
            raise ValueError(f"{value} bar is outside the 0 to 10 range")
        self.__pressure = value

    @classmethod
    def from_psi(cls, tag: str, psi: float) -> "PressureGauge":
        return cls(tag, psi * 0.0689476)


pt205 = PressureGauge("PT-205", 6.1)
print(f"{pt205.tag}: {pt205.pressure:.2f} bar")

pt205.pressure = 9.0
print(f"{pt205.tag}: {pt205.pressure:.2f} bar")

try:
    pt205.pressure = 12.5
except ValueError as ex:
    print("Rejected:", ex)

print(f"{pt205.tag}: {pt205.pressure:.2f} bar")

pt301 = PressureGauge.from_psi("PT-301", 120.0)
print(f"{pt301.tag}: {pt301.pressure:.2f} bar")
```
**Output**
```text
PT-205: 6.10 bar
PT-205: 9.00 bar
Rejected: 12.5 bar is outside the 0 to 10 range
PT-205: 9.00 bar
PT-301: 8.27 bar
```
**Rubric** (totals 10)
| Criterion | Points |
|---|---|
| Property with a setter, and the setter is the only place that assigns the private attribute | 4 |
| The constructor goes through the property, not through the attribute | 2 |
| The classmethod uses cls and returns an object already validated | 2 |
| The ValueError carries the rejected value and the object does not change | 2 |

**Most common mistake**
Inside the setter they write `self.pressure = value`: the property calls itself and the program dies with `RecursionError` on the first construction.

### 04.3 · Integrate
**Solution**
```python
class Tank:
    installed = 0

    def __init__(self, tag: str, capacity: float, level: float) -> None:
        self.tag = tag
        self.capacity = capacity
        self.__level = level
        Tank.installed += 1

    @property
    def level(self) -> float:
        return self.__level

    @property
    def percent(self) -> float:
        return self.__level / self.capacity * 100

    def fill(self, litres: float) -> None:
        if self.__level + litres > self.capacity:
            raise ValueError(f"{litres:.0f} L overflow {self.tag}")
        self.__level += litres

    def drain(self, litres: float) -> None:
        if litres > self.__level:
            raise ValueError(f"{self.tag} only holds {self.__level:.0f} L")
        self.__level -= litres


def status(tank: Tank) -> str:
    return f"{tank.tag}: {tank.level:.0f} L ({tank.percent:.1f} %)"


tq01 = Tank("TQ-01", 5000.0, 1200.0)
tq02 = Tank("TQ-02", 2000.0, 800.0)

tq01.fill(2000)
print(status(tq01))

try:
    tq01.drain(4000)
except ValueError as ex:
    print("Rejected:", ex)

try:
    tq01.fill(3000)
except ValueError as ex:
    print("Rejected:", ex)

tq01.drain(1200)
print(status(tq01))
print(status(tq02))
print("Tanks installed:", Tank.installed)
```
**Output**
```text
TQ-01: 3200 L (64.0 %)
Rejected: TQ-01 only holds 3200 L
Rejected: 3000 L overflow TQ-01
TQ-01: 2000 L (40.0 %)
TQ-02: 800 L (40.0 %)
Tanks installed: 2
```
**Rubric** (totals 10)
| Criterion | Points |
|---|---|
| Private level and the two read-only properties | 3 |
| Both methods validate before moving the level | 3 |
| The counter is written on the class and reaches 2 | 2 |
| Both rejections are caught by type and the level is left intact | 2 |

**Most common mistake**
They validate after adding: the tank overflows, and only then does the error fire, with the level already wrong.

## Week 05 · Topic 2 · Building blocks

### 05.1 · Recognise
**Solution**
```text
The second def overwrites the first, the same way assigning a variable twice
does. Only the three-parameter version exists, so the call with three values
runs and the one with two blows up over the missing argument.
```
```python
class Recorder:
    def record(self, tag, value, unit="C"):
        print("record:", tag, value, unit)
```
**Output**
```text
three values: TT-101 74.5 C
Traceback (most recent call last):
  File "recorder.py", line 11, in <module>
    r.record("PT-205", 6.1)
    ~~~~~~~~^^^^^^^^^^^^^^^
TypeError: Recorder.record() missing 1 required positional argument: 'unit'
```
**Rubric** (totals 10)
| Criterion | Points |
|---|---|
| The first call prints the three-value version | 3 |
| Names the TypeError and the missing argument | 3 |
| Explains that the method name is one entry holding one value | 2 |
| The fix uses a default value, with no if counting arguments | 2 |

**Most common mistake**
They answer that Python picks the method by its arguments. That is Java, and here the first definition no longer exists.

### 05.2 · Apply
**Solution**
```python
class StockItem:
    def __init__(self, code: str, pieces: int) -> None:
        self.code = code
        self.pieces = pieces

    def __str__(self) -> str:
        return f"{self.code} x{self.pieces}"

    def __eq__(self, other) -> bool:
        return self.code == other.code and self.pieces == other.pieces

    def __add__(self, other) -> "StockItem":
        if self.code != other.code:
            raise ValueError("Different codes cannot be added")
        return StockItem(self.code, self.pieces + other.pieces)


store = StockItem("BL-220", 12)
delivery = StockItem("BL-220", 8)

print(store)
print(store + delivery)
print(store == StockItem("BL-220", 12))
print(store == delivery)

try:
    print(store + StockItem("SM-4471", 6))
except ValueError as ex:
    print("Rejected:", ex)
```
**Output**
```text
BL-220 x12
BL-220 x20
True
False
Rejected: Different codes cannot be added
```
**Rubric** (totals 10)
| Criterion | Points |
|---|---|
| __str__ in the format asked for | 2 |
| __eq__ compares both fields and not identity | 3 |
| __add__ returns a new object without touching the operands | 3 |
| Different codes raise ValueError | 2 |

**Most common mistake**
`__add__` does `self.pieces += other.pieces` and returns `self`: the sum modifies the store, and the line that prints it leaves it at 20 with nobody having asked.

### 05.3 · Integrate
**Solution**
```python
class StockItem:
    def __init__(self, code: str, pieces: int) -> None:
        self.code = code
        self.pieces = pieces

    def __str__(self) -> str:
        return f"{self.code} x{self.pieces}"


class Inventory:
    def __init__(self, warehouse: str) -> None:
        self.warehouse = warehouse
        self.__stock: dict[str, int] = {}

    def receive(self, *codes: str, **options) -> None:
        pieces = options.get("pieces", 1)
        for code in codes:
            current = self.__stock.get(code, 0)
            self.__stock[code] = current + pieces
        if options.get("notify", False):
            print(f"{len(codes)} codes received at {self.warehouse}")

    def listing(self) -> list:
        rows = []
        for code, pieces in self.__stock.items():
            rows.append(StockItem(code, pieces))
        return rows

    def __str__(self) -> str:
        total = 0
        for code, pieces in self.__stock.items():
            total += pieces
        return f"{self.warehouse}: {len(self.__stock)} codes, {total} pieces"


if __name__ == "__main__":
    store = Inventory("North Warehouse")

    store.receive("BL-220", "SM-4471", pieces=4, notify=True)
    store.receive("EM-905", pieces=30)
    store.receive("BL-220")

    for row in store.listing():
        print(row)

    print(store)
```
**Output**
```text
2 codes received at North Warehouse
BL-220 x5
SM-4471 x4
EM-905 x30
North Warehouse: 3 codes, 39 pieces
```
**Rubric** (totals 10)
| Criterion | Points |
|---|---|
| *codes collects as many as arrive, and **options reads pieces and notify with get | 4 |
| BL-220 accumulates 4 plus 1 and ends at 5 | 2 |
| The dictionary is private and only shows through listing and __str__ | 2 |
| The test block does not run when the module is imported | 2 |

**Most common mistake**
They read the options with square brackets instead of `get`: the second call, which passes no `notify`, dies with `KeyError`.

## Week 06 · Topic 3 · Core properties

### 06.1 · Recognise
**Solution**
```text
The promise did not hold. The getter handed back the list itself, not a copy, so
the append from outside wrote straight into the private attribute and skipped
the upper. The two underscores protected the name of the attribute, not the
object sitting behind it.
```
```python
    def entries(self):
        return list(self.__entries)
```
**Output**
```text
2
FAULT ON B-101
all good
```
**Rubric** (totals 10)
| Criterion | Points |
|---|---|
| The three outputs | 4 |
| Says the capitals promise broke, and on which entry | 2 |
| Explains the difference between closing the name and closing the object | 2 |
| The fix returns a copy | 2 |

**Most common mistake**
They answer `AttributeError` because they spotted the two underscores. The method sits inside the class, so it reaches the attribute with no trouble.

### 06.2 · Apply
**Solution**
```python
class FaultCounter:
    def __init__(self) -> None:
        self.__faults: dict[str, int] = {}

    def record(self, tag: str) -> None:
        key = tag.upper()
        current = self.__faults.get(key, 0)
        self.__faults[key] = current + 1

    def __getitem__(self, tag: str) -> int:
        return self.__faults.get(tag.upper(), 0)

    def __setitem__(self, tag: str, count: int) -> None:
        self.__faults[tag.upper()] = count

    def __len__(self) -> int:
        return len(self.__faults)


counter = FaultCounter()

counter.record("B-101")
counter.record("b-101")
counter.record("C-310")

print(counter["B-101"])
print(counter["b-101"])
print(counter["V-12"])
print(len(counter))

counter["v-12"] = 5
print(counter["V-12"])
print(len(counter))
```
**Output**
```text
2
2
0
2
5
3
```
**Rubric** (totals 10)
| Criterion | Points |
|---|---|
| __getitem__, __setitem__ and __len__ all working | 4 |
| The normalising to capitals sits in one place, inside the class | 3 |
| A tag with no faults returns 0 instead of KeyError | 2 |
| The dictionary cannot be reached from outside | 1 |

**Most common mistake**
They normalise in `record` and forget to do it in `__getitem__`, so `counter["b-101"]` returns 0 with the fault already stored.

### 06.3 · Integrate
**Solution**
```python
class Sensor:
    def __init__(self, tag: str, low: float, high: float) -> None:
        self.tag = tag
        self.low = low
        self.high = high

    def in_range(self, value: float) -> bool:
        return value >= self.low and value <= self.high


class Logbook:
    def __init__(self) -> None:
        self.__entries: list[str] = []

    def record(self, text: str) -> None:
        self.__entries.append(text.upper())

    def entries(self) -> list:
        return list(self.__entries)

    def __len__(self) -> int:
        return len(self.__entries)


class Station:
    def __init__(self, name: str, sensors: dict, logbook: Logbook) -> None:
        self.name = name
        self.__sensors = sensors
        self.__logbook = logbook

    def measure(self, tag: str, value: float) -> None:
        sensor = self.__sensors[tag]
        if not sensor.in_range(value):
            self.__logbook.record(f"{tag} out of range at {value}")

    def history(self) -> list:
        return self.__logbook.entries()


sensors = {
    "TT-101": Sensor("TT-101", 0.0, 400.0),
    "PT-205": Sensor("PT-205", 0.0, 10.0),
}

north = Station("North Plant", sensors, Logbook())

north.measure("TT-101", 412.0)
north.measure("PT-205", 6.1)
north.measure("PT-205", 11.2)

north.history().append("fake entry")

for entry in north.history():
    print(entry)

print(len(north.history()))
```
**Output**
```text
TT-101 OUT OF RANGE AT 412.0
PT-205 OUT OF RANGE AT 11.2
2
```
**Rubric** (totals 10)
| Criterion | Points |
|---|---|
| Station receives its pieces and delegates to them, inheriting from neither | 4 |
| The fake entry does not get in, because the history returns a copy | 3 |
| Only what fell out of range gets recorded | 2 |
| The three classes can be tested separately | 1 |

**Most common mistake**
They make `Station` inherit from `Logbook` to reuse `record`. The sentence "a station is a logbook" does not stand up, and the "is a" test knocks it over the moment it is read aloud.

## Week 07 · Topic 3 · Core properties

### 07.1 · Recognise
**Solution**
```text
Defining __init__ in the child replaces the one in the parent. Since nobody
called super().__init__(tag), Equipment never ran and the object was born with
no tag and no hours. flow does exist, which is why the first line prints. The
second one dies while reading self.tag.

The missing line is super().__init__(tag), and it goes as the first statement of
the Pump constructor, before flow is assigned.
```
**Output**
```text
120.0
Traceback (most recent call last):
  File "equipment.py", line 17, in <module>
    print(b101.card())
          ~~~~~~~~~^^
  File "equipment.py", line 12, in card
    return f"{self.tag}: {self.flow} L/s"
              ^^^^^^^^
AttributeError: 'Pump' object has no attribute 'tag'
```
**Rubric** (totals 10)
| Criterion | Points |
|---|---|
| The first line prints and the second one blows up | 3 |
| Names AttributeError and the tag attribute | 3 |
| Explains that the constructor of the child replaces the one of the parent | 2 |
| Places super().__init__ at the start of the constructor | 2 |

**Most common mistake**
They answer that the error is a `TypeError` over arguments. The constructor got both arguments it asked for; the trouble shows up later, reading an attribute that was never created.

### 07.2 · Apply
**Solution**
```python
class Equipment:
    def __init__(self, tag: str, hours: float) -> None:
        self._tag = tag
        self._hours = hours

    def summary(self) -> str:
        return f"{self._tag} with {self._hours:.0f} h"

    def log_hours(self, run: float) -> None:
        self._hours += run


class Pump(Equipment):
    def __init__(self, tag: str, hours: float, flow: float) -> None:
        super().__init__(tag, hours)
        self.flow = flow

    def start(self) -> str:
        return f"{self._tag} starts at {self.flow} L/s"


class Compressor(Equipment):
    def __init__(self, tag: str, hours: float, pressure: float) -> None:
        super().__init__(tag, hours)
        self.pressure = pressure

    def purge(self) -> str:
        return f"{self._tag} purges at {self.pressure} bar"


b101 = Pump("B-101", 4820.0, 120.0)
c310 = Compressor("C-310", 6300.0, 8.5)

print(b101.summary())
print(b101.start())

c310.log_hours(40)
print(c310.summary())
print(c310.purge())

print(isinstance(b101, Equipment), isinstance(b101, Compressor))
print(issubclass(Compressor, Equipment))
```
**Output**
```text
B-101 with 4820 h
B-101 starts at 120.0 L/s
C-310 with 6340 h
C-310 purges at 8.5 bar
True False
True
```
**Rubric** (totals 10)
| Criterion | Points |
|---|---|
| Both children hang off the same parent, not one off the other | 3 |
| Both constructors chain with super | 3 |
| The methods of each child read the protected attribute of the parent | 2 |
| isinstance and issubclass answer what they should | 2 |

**Most common mistake**
They assign `self._tag` again in the child after calling `super`. Nothing breaks today, and it hides the fact that the parent had already done it.

### 07.3 · Integrate
**Solution**
```text
The six-level chain flattens like this. Asset stays as the parent, Pump and
Compressor hang off it, and VariableSpeedDrive leaves the tree because "a drive
is a pump with a drive" holds up under no reading at all: the pump uses a drive,
it is not one. That is composition.

Asset -> Pump: a pump is an asset of the plant. It holds.
Asset -> Compressor: a compressor is an asset of the plant. It holds.
Pump receives a VariableSpeedDrive: a usage relation, solved with a parameter.
```
```python
class VariableSpeedDrive:
    def __init__(self, brand: str, hz: float) -> None:
        self.brand = brand
        self.hz = hz

    def adjust(self, hz: float) -> None:
        self.hz = hz


class Asset:
    def __init__(self, tag: str, hours: float) -> None:
        self._tag = tag
        self._hours = hours

    def summary(self) -> str:
        return f"{self._tag} with {self._hours:.0f} h"


class Pump(Asset):
    def __init__(self, tag: str, hours: float, flow: float, drive=None) -> None:
        super().__init__(tag, hours)
        self.flow = flow
        self.drive = drive

    def start(self) -> str:
        if self.drive is None:
            return f"{self._tag} starts direct on line"
        return f"{self._tag} starts at {self.drive.hz} Hz"


class Compressor(Asset):
    def __init__(self, tag: str, hours: float, pressure: float) -> None:
        super().__init__(tag, hours)
        self.pressure = pressure


b101 = Pump("B-101", 4820.0, 120.0)
b102 = Pump("B-102", 1150.0, 120.0, VariableSpeedDrive("Danfoss", 45.0))
c310 = Compressor("C-310", 6300.0, 8.5)

print(b101.summary())
print(b101.start())
print(b102.start())

b102.drive.adjust(38.0)
print(b102.start())

print(c310.summary())
print(isinstance(b102, Asset), isinstance(b102.drive, Asset))
```
**Output**
```text
B-101 with 4820 h
B-101 starts direct on line
B-102 starts at 45.0 Hz
B-102 starts at 38.0 Hz
C-310 with 6300 h
True False
```
**Rubric** (totals 10)
| Criterion | Points |
|---|---|
| No branch runs deeper than two levels | 3 |
| VariableSpeedDrive leaves the tree and comes in through the constructor | 3 |
| One justification per relation kept, phrased as a type sentence | 2 |
| The case with no drive works and does not blow up on None | 2 |

**Most common mistake**
They leave `DosingPump` hanging off `Pump` "because it really is a pump". The relation does hold, but the exercise asks for two levels, and dosing fits as an attribute.

## Week 08 · Topic 3 · Core properties

### 08.1 · Recognise
**Solution**
```text
report is written in Equipment, but self keeps the real class of the object.
Python looks draw_kw up starting from that class, not from the class where the
method was written. V-12 keeps the parent version, M-204 uses the one in Motor
and C-310 the one in Compressor. Compressor also overrides report and extends
it: super().report() prints the parent line and then it adds its own.

With the super call at the end, "check the filter" would come out first and the
kW line after it.
```
**Output**
```text
V-12: 0.0 kW
M-204: 45.0 kW
C-310: 75.0 kW
C-310: check the filter
```
**Rubric** (totals 10)
| Criterion | Points |
|---|---|
| The four lines, in order | 4 |
| Says that self outranks where the method is written | 3 |
| Explains what super does inside an overridden method | 2 |
| Answers the change of order correctly | 1 |

**Most common mistake**
They answer 0.0 kW for all three because `report` lives in `Equipment`. That is exactly the confusion the exercise is hunting for.

### 08.2 · Apply
**Solution**
```python
from abc import ABC, abstractmethod


class Instrument(ABC):
    def __init__(self, tag: str) -> None:
        self.tag = tag
        self.calibrated = False

    def calibrate(self) -> None:
        self.calibrated = True

    @abstractmethod
    def read(self) -> str:
        ...


class Thermocouple(Instrument):
    def read(self) -> str:
        return f"{self.tag}: 74.5 C"


class PressureGauge(Instrument):
    def read(self) -> str:
        return f"{self.tag}: 6.1 bar"


class FlowMeter(Instrument):
    def read(self) -> str:
        return f"{self.tag}: 118.0 L/s"


panel = [Thermocouple("TT-101"), PressureGauge("PT-205"), FlowMeter("FT-330")]

for instrument in panel:
    instrument.calibrate()
    print(instrument.read(), instrument.calibrated)

try:
    loose = Instrument("XX-000")
except TypeError as ex:
    print("Rejected:", ex)
```
**Output**
```text
TT-101: 74.5 C True
PT-205: 6.1 bar True
FT-330: 118.0 L/s True
Rejected: Can't instantiate abstract class Instrument without an implementation for abstract method 'read'
```
**Rubric** (totals 10)
| Criterion | Points |
|---|---|
| ABC and @abstractmethod together, not one without the other | 3 |
| The three children implement read and inherit calibrate | 3 |
| The loop asks no object what type it is | 2 |
| The abstract class refuses to be built | 2 |

**Most common mistake**
They put `@abstractmethod` on without inheriting from `ABC`: the class builds as if nothing were wrong and the `try` at the end never prints.

### 08.3 · Integrate
**Solution**
```python
from abc import ABC, abstractmethod


class Equipment(ABC):
    census = 0

    def __init__(self, tag: str, hours: float) -> None:
        self._tag = tag
        self.__hours = hours
        Equipment.census += 1

    @property
    def tag(self) -> str:
        return self._tag

    @property
    def hours(self) -> float:
        return self.__hours

    def log_hours(self, run: float) -> None:
        if run < 0:
            raise ValueError("Hours run cannot be negative")
        self.__hours += run

    @abstractmethod
    def draw_kw(self) -> float:
        ...

    def report(self) -> str:
        return f"{self._tag}: {self.hours:.0f} h, {self.draw_kw():.1f} kW"


class Pump(Equipment):
    def __init__(self, tag: str, hours: float, flow: float) -> None:
        super().__init__(tag, hours)
        self.flow = flow

    def draw_kw(self) -> float:
        return self.flow * 0.32


class Compressor(Equipment):
    def __init__(self, tag: str, hours: float, pressure: float) -> None:
        super().__init__(tag, hours)
        self.pressure = pressure

    def draw_kw(self) -> float:
        return self.pressure * 8.0

    def report(self) -> str:
        return super().report() + " (air)"


class Valve(Equipment):
    def __init__(self, tag: str, hours: float) -> None:
        super().__init__(tag, hours)


plant = [Pump("B-101", 4820.0, 120.0), Compressor("C-310", 6300.0, 8.5)]

total = 0.0
for item in plant:
    print(item.report())
    total += item.draw_kw()

print(f"Total draw: {total:.1f} kW")

plant[0].log_hours(180)
print(plant[0].report())

try:
    plant[0].log_hours(-5)
except ValueError as ex:
    print("Rejected:", ex)

try:
    v12 = Valve("V-12", 300.0)
except TypeError as ex:
    print("Rejected:", ex)

print("Equipment built:", Equipment.census)
```
**Output**
```text
B-101: 4820 h, 38.4 kW
C-310: 6300 h, 68.0 kW (air)
Total draw: 106.4 kW
B-101: 5000 h, 38.4 kW
Rejected: Hours run cannot be negative
Rejected: Can't instantiate abstract class Valve without an implementation for abstract method 'draw_kw'
Equipment built: 2
```
**Rubric** (totals 10)
| Criterion | Points |
|---|---|
| Abstract class with an abstract method and a concrete method that uses it | 3 |
| Private hours, read-only properties and validation inside the method | 3 |
| The loop adds up the draw without asking about types | 2 |
| Compressor extends report with super, and the valve refuses to be built | 2 |

**Most common mistake**
The valve does get built, because they gave it a `draw_kw` returning 0. The census then reads 3, and the contract has stopped doing the job it was there for.

## Week 09 · Topic 4 · Advanced functions and structures

### 09.1 · Recognise
**Solution**
```text
The list in the default value was created once, at the moment the def ran, and
every call that does not pass a history writes into it. The third call receives
a list of its own and comes out alone. The fourth goes back to the shared one,
which already carried two tags.
```
```python
def record_fault(tag, history=None):
    if history is None:
        history = []
    history.append(tag)
    return history
```
**Output**
```text
['B-101']
['B-101', 'C-310']
['V-12']
['B-101', 'C-310', 'M-204']
```
**Rubric** (totals 10)
| Criterion | Points |
|---|---|
| The four outputs | 4 |
| Says the list was created when the function was defined | 3 |
| The fix uses None and creates the list inside | 3 |

**Most common mistake**
They answer that the fourth line carries a single tag because the third one "reset" the list. The third one never touched the shared list.

### 09.2 · Apply
**Solution**
```python
spares = [
    ("BL-220", "bearing", 12),
    ("SM-4471", "mechanical seal", 6),
    ("EM-905", "gasket", 30),
    ("RT-118", "oil seal", 2),
]


def by_stock(spares: list) -> list:
    copy = list(spares)
    copy.sort(key=lambda s: s[2])
    return copy


def critical(spares: list, minimum: int) -> list:
    codes = []
    for code, description, pieces in spares:
        if pieces < minimum:
            codes.append(code)
    return codes


def show(spares: list) -> None:
    for number, spare in enumerate(by_stock(spares), start=1):
        code, description, pieces = spare
        print(f"{number}. {code} {description}: {pieces}")


show(spares)
print(critical(spares, 5))
print(spares[0][0])
```
**Output**
```text
1. RT-118 oil seal: 2
2. SM-4471 mechanical seal: 6
3. BL-220 bearing: 12
4. EM-905 gasket: 30
['RT-118']
BL-220
```
**Rubric** (totals 10)
| Criterion | Points |
|---|---|
| sort with key and a lambda over the third element | 3 |
| The original list is left intact, and the last line proves it | 3 |
| critical returns and does not print | 2 |
| enumerate numbers from 1 | 2 |

**Most common mistake**
They write `copy = spares.sort(...)`: `sort` returns `None`, the variable ends up as `None` and the `enumerate` blows up.

### 09.3 · Integrate
**Solution**
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


def count_pieces(node: dict) -> int:
    total = node["pieces"]
    for part in node["parts"]:
        total += count_pieces(part)
    return total


def depth(node: dict) -> int:
    deepest = 0
    for part in node["parts"]:
        level = depth(part)
        if level > deepest:
            deepest = level
    return deepest + 1


def leaves(node: dict, found: list = None) -> list:
    if found is None:
        found = []
    if len(node["parts"]) == 0:
        found.append(node["name"])
    for part in node["parts"]:
        leaves(part, found)
    return found


print(count_pieces(PUMP))
print(depth(PUMP))
print(leaves(PUMP))
```
**Output**
```text
15
3
['impeller', 'bearing BL-220', 'seal SM-4471', 'bolt']
```
**Rubric** (totals 10)
| Criterion | Points |
|---|---|
| The three functions are recursive and each has a base case | 4 |
| count_pieces gives 15 and depth gives 3 | 3 |
| leaves returns the four in order, without repeating the root node | 2 |
| The accumulator is not the default value of the parameter | 1 |

**Most common mistake**
`depth` returns 2 because it counts only the first level of parts. It gives itself away as soon as it is tried on a tree of one node, where the answer has to be 1.

## Week 10 · Topic 4 · Advanced functions and structures

### 10.1 · Recognise
**Solution**
```text
backup and readings are two names for the same list, so the append leaves six
elements in both. The set throws the repeats away and keeps 74.5, 118.0 and 6.1.
The accumulator counts 118.0 twice and 6.1 twice, because the second 6.1 came in
with the append. With list(readings) there would be two lists: the append would
touch the backup only, readings would still hold five, and the count for 6.1
would be 1.
```
**Output**
```text
6 3
2 2
True
0
```
**Rubric** (totals 10)
| Criterion | Points |
|---|---|
| The four outputs | 4 |
| Explains why len(readings) is 6 and not 5 | 3 |
| Says what would change with list(readings) | 2 |
| Mentions that get returns the default without raising KeyError | 1 |

**Most common mistake**
They answer `5 3` on the first line: the append went in through the other name and they missed it.

### 10.2 · Apply
**Solution**
```python
faults = [
    ("B-101", "vibration"),
    ("C-310", "overheating"),
    ("B-101", "leak"),
    ("V-12", "leak"),
    ("B-101", "vibration"),
]

readings = [74.5, 118.0, 6.1, 203.0, 99.9, 118.0]

leaks = [tag for tag, kind in faults if kind == "leak"]

counts = {}
for tag, kind in faults:
    counts[tag] = counts.get(tag, 0) + 1

high = [value for value in readings if value > 100]

print(leaks)
print(counts)
print(high)
print(sorted(set(leaks)))
```
**Output**
```text
['B-101', 'V-12']
{'B-101': 3, 'C-310': 1, 'V-12': 1}
[118.0, 203.0, 118.0]
['B-101', 'V-12']
```
**Rubric** (totals 10)
| Criterion | Points |
|---|---|
| Both comprehensions with their condition | 4 |
| The accumulator uses get with a default of 0 | 3 |
| The repeated 118.0 shows up twice among the high readings | 2 |
| The tags with no repeats come out of a sorted set | 1 |

**Most common mistake**
They write the comprehension with `if` and `else` to do the counting. A comprehension filters; counting by key needs the accumulator dictionary.

### 10.3 · Integrate
**Solution**
```python
class Roster:
    def __init__(self, equipment: list) -> None:
        self.__equipment = list(equipment)
        self.__by_tag = {}
        tags = []
        for item in equipment:
            self.__by_tag[item["tag"]] = item
            tags.append(item["tag"])
        self.__tags = set(tags)

    def exists(self, tag: str) -> bool:
        return tag in self.__tags

    def hours(self, tag: str) -> float:
        item = self.__by_tag.get(tag)
        if item is None:
            return 0.0
        return item["hours"]

    def sorted_tags(self) -> list:
        return sorted([e["tag"] for e in self.__equipment])

    def by_type(self) -> dict:
        counts = {}
        for item in self.__equipment:
            counts[item["type"]] = counts.get(item["type"], 0) + 1
        return counts

    def overdue(self, limit: float) -> list:
        return [e["tag"] for e in self.__equipment if e["hours"] > limit]


equipment = [
    {"tag": "B-101", "type": "pump", "hours": 4820.0},
    {"tag": "B-102", "type": "pump", "hours": 1150.0},
    {"tag": "C-310", "type": "compressor", "hours": 6300.0},
    {"tag": "M-204", "type": "motor", "hours": 2210.0},
    {"tag": "V-12", "type": "valve", "hours": 300.0},
]

roster = Roster(equipment)

print(roster.exists("C-310"), roster.exists("X-999"))
print(roster.hours("B-101"))
print(roster.sorted_tags())
print(roster.by_type())
print(roster.overdue(5000))
```
**Output**
```text
True False
4820.0
['B-101', 'B-102', 'C-310', 'M-204', 'V-12']
{'pump': 2, 'compressor': 1, 'motor': 1, 'valve': 1}
['C-310']
```
**Rubric** (totals 10)
| Criterion | Points |
|---|---|
| A set for membership and a dictionary for lookup by key | 4 |
| The structures are private and built once, in the constructor | 2 |
| hours returns 0.0 without raising KeyError | 2 |
| The justification names the container and the reason, method by method | 2 |

**Most common mistake**
`exists` walks the list with a `for` and a `return True` inside. It answers correctly, and it is precisely the query the set settles without walking anything.

## Week 11 · Topic 4 · Advanced functions and structures

### 11.1 · Recognise
**Solution**
```text
finally always runs, even when a return is already waiting its turn. The value
is stored, the block prints, and only then does the function hand it back. That
is why "attempt" shows up before the number on all three calls.

float("n/a") raises ValueError, which is the first except and the only one
examined: as soon as one matches, the rest are never looked at.
```
**Output**
```text
attempt 4
25.0
attempt 0
0.0
attempt n/a
-1.0
```
**Rubric** (totals 10)
| Criterion | Points |
|---|---|
| The six lines in the right order | 5 |
| Explains that finally runs before the value is handed back | 3 |
| Names ValueError and says why the second except is not examined | 2 |

**Most common mistake**
They put the number before the "attempt" in each pair. The `return` looks like it leaves first when you read it, and `finally` slips in between.

### 11.2 · Apply
**Solution**
```python
class ReadingOutOfRange(Exception):
    pass


class Sensor:
    def __init__(self, tag: str, low: float, high: float) -> None:
        self.tag = tag
        self.low = low
        self.high = high
        self.__value = low

    @property
    def value(self) -> float:
        return self.__value

    @value.setter
    def value(self, reading: float) -> None:
        if reading < self.low or reading > self.high:
            raise ReadingOutOfRange(
                f"{self.tag} read {reading} and its range is {self.low} to {self.high}")
        self.__value = reading


tt101 = Sensor("TT-101", 0.0, 400.0)

for reading in [74.5, 412.0, 180.0]:
    try:
        tt101.value = reading
    except ReadingOutOfRange as ex:
        print(type(ex).__name__)
        print(ex)
    else:
        print(f"{tt101.tag} accepted: {tt101.value}")

print(f"Last stored value: {tt101.value}")
```
**Output**
```text
TT-101 accepted: 74.5
ReadingOutOfRange
TT-101 read 412.0 and its range is 0.0 to 400.0
TT-101 accepted: 180.0
Last stored value: 180.0
```
**Rubric** (totals 10)
| Criterion | Points |
|---|---|
| The custom exception inherits from Exception and is caught by its name | 3 |
| The validation lives in the setter, not in the loop that calls it | 3 |
| The else prints only when the assignment went through | 2 |
| The rejected value does not stay stored | 2 |

**Most common mistake**
They validate in the loop with an `if` before assigning. It works in this test and leaves the sensor wide open to any other file that writes to it directly.

### 11.3 · Integrate
**Solution**
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


class InvalidReading(Exception):
    pass


class ReadingOutOfRange(InvalidReading):
    pass


class UnknownSensor(InvalidReading):
    pass


RANGES = {
    "TT-101": (0.0, 400.0),
    "PT-205": (0.0, 10.0),
    "FT-330": (0.0, 200.0),
}


def validate(tag: str, text) -> float:
    if tag not in RANGES:
        raise UnknownSensor(f"{tag} is not on the panel")
    if text is None:
        raise InvalidReading(f"{tag} sent nothing")
    try:
        value = float(text)
    except ValueError:
        raise InvalidReading(f"{tag} sent {text} and that is not a number")
    low, high = RANGES[tag]
    if value < low or value > high:
        raise ReadingOutOfRange(f"{tag} read {value} outside {low} to {high}")
    return value


accepted = []
rejected = 0

for tag, text in raw:
    try:
        accepted.append((tag, validate(tag, text)))
    except ReadingOutOfRange as ex:
        rejected += 1
        print("Out of range:", ex)
    except UnknownSensor as ex:
        rejected += 1
        print("Not registered:", ex)
    except InvalidReading as ex:
        rejected += 1
        print("Bad data:", ex)

print(f"Accepted: {len(accepted)}  Rejected: {rejected}")

total = 0.0
for tag, value in accepted:
    total += value

print(f"Average of accepted: {total / len(accepted):.2f}")
```
**Output**
```text
Out of range: TT-101 read 412.0 outside 0.0 to 400.0
Not registered: XX-999 is not on the panel
Bad data: FT-330 sent n/a and that is not a number
Bad data: PT-205 sent nothing
Accepted: 3  Rejected: 4
Average of accepted: 66.20
```
**Rubric** (totals 10)
| Criterion | Points |
|---|---|
| The three custom exceptions, in the hierarchy that allows catching them together | 3 |
| The excepts run from most specific to most general | 3 |
| All the validation sits in one function, at the boundary | 2 |
| Every message says what to correct, and the final count adds up | 2 |

**Most common mistake**
They put `except InvalidReading` above the other two: it catches everything and the specific messages never print, because both children are also the mother.

## Week 12 · Topic 5 · Files

### 12.1 · Recognise
**Solution**
```text
Mode w empties the file the instant it opens it, before a single character gets
written. The third opening deleted the two lines that were there. The only one
that kept anything was the second, in mode a.

What is left is 18 characters: the 17 of the line plus the newline. The print of
the contents adds a newline of its own, which is why a blank line shows up
before the number.
```
**Output**
```text
11:40 C-310 alarm

18
```
**Rubric** (totals 10)
| Criterion | Points |
|---|---|
| Only the 11:40 line survives | 4 |
| Says the wipe happens on opening, not on writing | 3 |
| The 18 counts the newline | 2 |
| Identifies mode a as the only one that kept anything | 1 |

**Most common mistake**
They answer 17 because they count the letters by hand. The `\n` at the end is a character too.

### 12.2 · Apply
**Solution**
```python
import csv
from pathlib import Path

path = Path("telemetry.csv")

rows = [
    {"tag": "TT-101", "value": 74.5},
    {"tag": "PT-205", "value": 6.1},
    {"tag": "TT-101", "value": 81.2},
    {"tag": "FT-330", "value": 118.0},
    {"tag": "PT-205", "value": 6.4},
]

with open(path, "w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=["tag", "value"])
    writer.writeheader()
    writer.writerows(rows)

totals = {}
counts = {}

with open(path, newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        tag = row["tag"]
        totals[tag] = totals.get(tag, 0.0) + float(row["value"])
        counts[tag] = counts.get(tag, 0) + 1

for tag, total in totals.items():
    print(f"{tag}: {total / counts[tag]:.2f} (n={counts[tag]})")
```
**Output**
```text
TT-101: 77.85 (n=2)
PT-205: 6.25 (n=2)
FT-330: 118.00 (n=1)
```
**Rubric** (totals 10)
| Criterion | Points |
|---|---|
| DictWriter with a header and DictReader by column name | 3 |
| Both accesses with with, an empty newline and an explicit encoding | 3 |
| Two accumulators, totals and counts, with get | 2 |
| The conversion to float happens on reading, because the CSV hands over text | 2 |

**Most common mistake**
They add up `row["value"]` without converting. The CSV returns strings, so the sum concatenates and the average blows up on the division.

### 12.3 · Integrate
**Solution**
```python
import csv
from pathlib import Path


class Logbook:
    FIELDS = ["time", "tag", "text"]

    def __init__(self, path: Path) -> None:
        self.path = path

    def record(self, time: str, tag: str, text: str) -> None:
        fresh = not self.path.exists()
        with open(self.path, "a", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=Logbook.FIELDS)
            if fresh:
                writer.writeheader()
            writer.writerow({"time": time, "tag": tag, "text": text})

    def entries(self) -> list:
        try:
            with open(self.path, newline="", encoding="utf-8") as file:
                return list(csv.DictReader(file))
        except FileNotFoundError:
            return []

    def report(self, target: Path) -> None:
        counts = {}
        for entry in self.entries():
            counts[entry["tag"]] = counts.get(entry["tag"], 0) + 1
        with open(target, "w", encoding="utf-8") as file:
            file.write("Events per equipment\n")
            for tag, times in counts.items():
                file.write(f"{tag}: {times}\n")


logbook = Logbook(Path("logbook.csv"))

logbook.record("08:00", "B-101", "normal start")
logbook.record("09:15", "PT-205", "reading 6.1 bar")
logbook.record("11:40", "C-310", "temperature alarm")
logbook.record("13:05", "B-101", "shutdown for maintenance")

print(len(logbook.entries()))
for entry in logbook.entries():
    print(entry["time"], entry["tag"], entry["text"])

target = Path("report.txt")
logbook.report(target)
print(target.read_text(encoding="utf-8"))

missing = Logbook(Path("missing.csv"))
print(len(missing.entries()))
```
**Output**
```text
4
08:00 B-101 normal start
09:15 PT-205 reading 6.1 bar
11:40 C-310 temperature alarm
13:05 B-101 shutdown for maintenance
Events per equipment
B-101: 2
PT-205: 1
C-310: 1

0
```
**Rubric** (totals 10)
| Criterion | Points |
|---|---|
| Mode a to append, with the header written exactly once | 3 |
| FileNotFoundError caught by name and an empty list handed back | 3 |
| The report groups by equipment and goes out to a new file | 2 |
| Every route is a Path and every opening carries an encoding | 2 |

**Most common mistake**
They write the header on every call to `record`: the CSV ends up with four header rows and `DictReader` reads them as if they were events.

## Week 13 · Topic 5 · Files

### 13.1 · Recognise
**Solution**
```text
The file holds 15 bytes and the positions count from zero. On opening, the
cursor sits at 0. seek(5) leaves it just before the sixth letter, and read(5)
returns B-102 and leaves the cursor at 10. seek(10) and read(5) return C-310 and
leave the cursor at 15, which is the end. The last read finds nothing and
returns an empty byte string, without raising any error at all.
```
**Output**
```text
0
b'B-102'
10
b'C-310'
b''
```
**Rubric** (totals 10)
| Criterion | Points |
|---|---|
| The five outputs, with the b of bytes | 5 |
| Explains that reading advances the cursor and seek places it | 3 |
| Says that the end returns something empty instead of an error | 2 |

**Most common mistake**
They write `'B-102'` without the `b`. In binary mode what arrives is bytes, and that letter is half the point of the session.

### 13.2 · Apply
**Solution**
```python
from pathlib import Path

SIZE = 32
path = Path("equipment.bin")

equipment = ["B-101", "B-102", "C-310", "M-204"]

with open(path, "wb") as file:
    for tag in equipment:
        file.write(f"{tag:<32}".encode("utf-8"))


def read_record(path: Path, number: int) -> str:
    with open(path, "rb") as file:
        file.seek(number * SIZE)
        raw = file.read(SIZE)
    return raw.decode("utf-8").strip()


print(len(equipment) * SIZE)
print(read_record(path, 2))
print(read_record(path, 0))
print(read_record(path, 3))
```
**Output**
```text
128
C-310
B-101
M-204
```
**Rubric** (totals 10)
| Criterion | Points |
|---|---|
| Every record measures exactly 32 bytes | 3 |
| The position comes from number times size, and seek jumps to it | 3 |
| Encoding on the way out and decoding on the way in, in UTF-8 | 2 |
| The padding is stripped before the tag is returned | 2 |

**Most common mistake**
They write without padding and the records end up five bytes long: the multiplication by 32 points into the middle of a tag, and everything after that is shifted.

### 13.3 · Integrate
**Solution**
```python
import csv
from pathlib import Path

SIZE = 40


class EmptyIndex(Exception):
    pass


def read_readings(path: Path) -> list:
    try:
        with open(path, newline="", encoding="utf-8") as file:
            return list(csv.DictReader(file))
    except FileNotFoundError:
        return []


def summarise(readings: list) -> dict:
    totals = {}
    counts = {}
    for row in readings:
        tag = row["tag"]
        try:
            value = float(row["value"])
        except ValueError:
            print(f"Discarded: {tag} sent {row['value']}")
            continue
        totals[tag] = totals.get(tag, 0.0) + value
        counts[tag] = counts.get(tag, 0) + 1
    averages = {}
    for tag, total in totals.items():
        averages[tag] = total / counts[tag]
    return averages


def write_index(path: Path, averages: dict) -> None:
    if len(averages) == 0:
        raise EmptyIndex("There are no averages to index")
    with open(path, "wb") as file:
        for tag, average in averages.items():
            record = f"{tag:<10}{average:>10.2f}"
            file.write(f"{record:<40}".encode("utf-8"))


def read_index(path: Path, number: int) -> str:
    with open(path, "rb") as file:
        file.seek(number * SIZE)
        raw = file.read(SIZE)
    if len(raw) < SIZE:
        raise IndexError(f"Record {number} does not exist")
    return raw.decode("utf-8").strip()


rows = [
    {"tag": "TT-101", "value": "74.5"},
    {"tag": "PT-205", "value": "6.1"},
    {"tag": "TT-101", "value": "81.2"},
    {"tag": "FT-330", "value": "118.0"},
    {"tag": "PT-205", "value": "n/a"},
]

source = Path("telemetry.csv")
with open(source, "w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=["tag", "value"])
    writer.writeheader()
    writer.writerows(rows)

readings = read_readings(source)
averages = summarise(readings)

print(len(readings), len(averages))
for tag, average in averages.items():
    print(f"{tag}: {average:.2f}")

index = Path("averages.bin")
write_index(index, averages)

print(read_index(index, 1))
print(read_index(index, 0))

try:
    print(read_index(index, 9))
except IndexError as ex:
    print("Rejected:", ex)

try:
    write_index(Path("empty.bin"), {})
except EmptyIndex as ex:
    print("Rejected:", ex)
```
**Output**
```text
Discarded: PT-205 sent n/a
5 3
TT-101: 77.85
PT-205: 6.10
FT-330: 118.00
PT-205          6.10
TT-101         77.85
Rejected: Record 9 does not exist
Rejected: There are no averages to index
```
**Rubric** (totals 10)
| Criterion | Points |
|---|---|
| The CSV is read with DictReader and a missing file gives back an empty list | 2 |
| The average drops the bad row without cutting the walk short, and says so | 3 |
| The index records measure 40 bytes and are read with seek | 3 |
| Both exceptions, the custom one and the index one, with messages of their own | 2 |

**Most common mistake**
They compute the average over the list in memory and write the index without checking the size: asking for record 9 returns an empty string instead of an error, and nobody finds out the query failed.

## Week 14 · Topic 6 · Graphical interfaces

Solutions 14.2 and 14.3 open a window and were not executed on the marking machine, which has no PyQt6 installed. They are written against the PyQt6 API, read line by line and compiled with `py_compile`, which reports no errors. The domain half of 14.3 does run, and its output is real.

### 14.1 · Recognise
**Solution**
```text
The parentheses call the method right there, while the window is being built.
That is why "click" prints once, and before anything shows on screen. The method
returns nothing, so connect receives None and the construction fails with
TypeError, because None cannot be called later on.

Even with the connect correct, the button is a local variable of the
constructor: once __init__ ends nobody references it, Python collects it, and
the window opens empty. Controls get stored on self.
```
```python
        self.button = QPushButton("Look up", self)
        self.button.clicked.connect(self.on_look_up)
```
**Output**
```text
click
```
After that line the construction ends with `TypeError`, because `connect` received `None` instead of something callable.

**Rubric** (totals 10)
| Criterion | Points |
|---|---|
| "click" prints once, while the window is built | 3 |
| connect receives None and the construction fails | 3 |
| The fix drops the parentheses | 2 |
| Spots that the button was not stored on self | 2 |

**Most common mistake**
They answer that it prints on every click. That is what the intention of the code says, not what the parentheses say.

### 14.2 · Apply
**Solution**
```python
import sys

from PyQt6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
                             QPushButton, QWidget)


def normalise(tag: str) -> str:
    clean = tag.strip().upper()
    if len(clean) == 0:
        return "Nothing entered"
    return clean


class TagWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Tag normaliser")
        self.setGeometry(200, 200, 380, 140)

        central = QWidget(self)
        self.setCentralWidget(central)

        self.box = QLineEdit(central)
        self.box.setPlaceholderText("b-101")
        self.box.setGeometry(20, 20, 220, 28)

        self.button = QPushButton("Normalise", central)
        self.button.setGeometry(250, 20, 110, 28)

        self.result = QLabel("Nothing entered", central)
        self.result.setGeometry(20, 70, 340, 28)

        self.button.clicked.connect(self.on_normalise)

    def on_normalise(self) -> None:
        self.result.setText(normalise(self.box.text()))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TagWindow()
    window.show()
    sys.exit(app.exec())
```
**Output**
```text
The window opens with an empty box and the label reading "Nothing entered".
Typing "  b-101 " and pressing Normalise puts B-101 in the label.
With the box empty, the label goes back to "Nothing entered".
```
**Rubric** (totals 10)
| Criterion | Points |
|---|---|
| The window is a class inheriting from QMainWindow and chaining super | 3 |
| The three controls are stored on self and hang off the central widget | 3 |
| connect with no parentheses, onto a method of the window | 2 |
| The slot computes nothing: it calls normalise and shows the result | 2 |

**Most common mistake**
They read `self.box.text()` inside the constructor and store the result. At that moment the box is empty, so the label never changes however many clicks it gets.

### 14.3 · Integrate
**Solution**
```python
class UnknownTag(Exception):
    pass


class Panel:
    def __init__(self) -> None:
        self.__readings = {}

    def record(self, tag: str, value: float, unit: str) -> None:
        self.__readings[tag.upper()] = (value, unit)

    def read(self, tag: str) -> str:
        key = tag.strip().upper()
        if key not in self.__readings:
            raise UnknownTag(f"{key} is not on the panel")
        value, unit = self.__readings[key]
        return f"{key}: {value} {unit}"


if __name__ == "__main__":
    panel = Panel()
    panel.record("TT-101", 74.5, "C")
    panel.record("PT-205", 6.1, "bar")

    print(panel.read("tt-101"))
    print(panel.read("  PT-205 "))

    try:
        print(panel.read("XX-999"))
    except UnknownTag as ex:
        print("Rejected:", ex)
```
```python
import sys

from PyQt6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
                             QPushButton, QWidget)

from panel import Panel, UnknownTag


class PanelWindow(QMainWindow):
    def __init__(self, panel: Panel) -> None:
        super().__init__()
        self.panel = panel

        self.setWindowTitle("Panel lookup")
        self.setGeometry(200, 200, 400, 140)

        central = QWidget(self)
        self.setCentralWidget(central)

        self.box = QLineEdit(central)
        self.box.setPlaceholderText("tt-101")
        self.box.setGeometry(20, 20, 240, 28)

        self.button = QPushButton("Look up", central)
        self.button.setGeometry(270, 20, 110, 28)

        self.result = QLabel("Type a tag", central)
        self.result.setGeometry(20, 70, 360, 28)

        self.button.clicked.connect(self.on_look_up)

    def on_look_up(self) -> None:
        try:
            self.result.setText(self.panel.read(self.box.text()))
        except UnknownTag as ex:
            self.result.setText(str(ex))


if __name__ == "__main__":
    panel = Panel()
    panel.record("TT-101", 74.5, "C")
    panel.record("PT-205", 6.1, "bar")
    panel.record("FT-330", 118.0, "L/s")

    app = QApplication(sys.argv)
    window = PanelWindow(panel)
    window.show()
    sys.exit(app.exec())
```
**Output**
```text
TT-101: 74.5 C
PT-205: 6.1 bar
Rejected: XX-999 is not on the panel
```
That is the output of running `panel.py` from the terminal. In the window, looking up `xx-999` leaves the label reading `XX-999 is not on the panel`.

**Rubric** (totals 10)
| Criterion | Points |
|---|---|
| panel.py does not import PyQt6 and runs from the terminal | 4 |
| The window receives the assembled panel and stores it | 2 |
| The slot catches the custom exception and shows it in the label | 3 |
| The tag normalising lives in the domain, not in the slot | 1 |

**Most common mistake**
They put the `strip().upper()` in the slot. The window ends up carrying a business rule, and the same class stops being usable from the console script.

## Week 15 · Topic 6 · Graphical interfaces

Same as the week before: the window code was checked against the PyQt6 API and compiled with `py_compile`, and it was not executed here. The domain class of 15.3 does run, and its output is real.

### 15.1 · Recognise
**Solution**
```text
The four numbers of addWidget are row, column, how many rows it spans and how
many columns it spans. The first two count from zero, the same as list indices.
When the last two are left out, the control takes a single cell.

           column 0      column 1        column 2
row 0      B-101         stop_button     (empty)
row 1      C-310         stop_button     (empty)
row 2      M-204         start_button    start_button

stop_button is the taller one: it spans two rows and one column.
start_button is the wider one: it spans one row and two columns.

One more label at position 0, 1 would land on top of the stop button. The grid
gives no warning: both end up in the same cell, and the trouble shows up when
the window runs, not when it is written.
```
**Output**
```text
This exercise prints nothing. What gets marked is the drawing of the grid and
the three answers.
```
**Rubric** (totals 10)
| Criterion | Points |
|---|---|
| The grid puts the five controls in the right cells | 4 |
| Explains the four numbers of addWidget | 3 |
| Identifies which button is taller and which is wider | 2 |
| Says that two controls in one cell overlap without any error | 1 |

**Most common mistake**
They read the first two numbers as column and row. The button ends up lying on its side and the whole drawing comes out transposed.

### 15.2 · Apply
**Solution**
```python
import sys

from PyQt6.QtWidgets import (QApplication, QFormLayout, QHBoxLayout, QLabel,
                             QLineEdit, QListWidget, QMainWindow, QPushButton,
                             QVBoxLayout, QWidget)


class OrderWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("New work orders")
        self.setGeometry(200, 200, 460, 320)

        central = QWidget(self)
        column = QVBoxLayout(central)

        form = QFormLayout()
        self.number = QLineEdit()
        self.tag = QLineEdit()
        self.priority = QLineEdit()
        self.description = QLineEdit()

        form.addRow("Number", self.number)
        form.addRow("Equipment", self.tag)
        form.addRow("Priority", self.priority)
        form.addRow("Description", self.description)
        column.addLayout(form)

        buttons = QHBoxLayout()
        self.save_button = QPushButton("Save")
        self.clear_button = QPushButton("Clear")
        buttons.addWidget(self.save_button)
        buttons.addWidget(self.clear_button)
        column.addLayout(buttons)

        self.notice = QLabel("Enter a work order")
        column.addWidget(self.notice)

        self.list = QListWidget()
        column.addWidget(self.list)

        self.setCentralWidget(central)

        self.save_button.clicked.connect(self.on_save)
        self.clear_button.clicked.connect(self.on_clear)

    def on_save(self) -> None:
        row = f"{self.number.text()} {self.tag.text()} P{self.priority.text()}"
        self.list.addItem(row)
        self.notice.setText(f"Work orders entered: {self.list.count()}")
        self.on_clear()

    def on_clear(self) -> None:
        self.number.clear()
        self.tag.clear()
        self.priority.clear()
        self.description.clear()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = OrderWindow()
    window.show()
    sys.exit(app.exec())
```
**Output**
```text
The window opens with the four fields empty and the notice reading "Enter a
work order". Entering OT-1042, B-101 and 1 and pressing Save puts
"OT-1042 B-101 P1" in the list, moves the notice to "Work orders entered: 1"
and leaves the fields empty. Stretch the window and the form and the list grow
with it, with nothing overlapping.
```
**Rubric** (totals 10)
| Criterion | Points |
|---|---|
| Not one fixed coordinate anywhere in the window | 3 |
| The form and the button row are nested inside the vertical layout | 3 |
| Each button connected to its own slot, with no parentheses | 2 |
| Save clears the fields by reusing the other slot | 2 |

**Most common mistake**
They add the `QFormLayout` with `addWidget` instead of `addLayout`. A layout is not a widget, and the window opens with no form in it.

### 15.3 · Integrate
**Solution**
```python
class InvalidData(Exception):
    pass


class WorkOrder:
    def __init__(self, number: str, tag: str, priority: int, description: str) -> None:
        self.number = number
        self.tag = tag
        self.priority = priority
        self.description = description

    def __str__(self) -> str:
        return f"{self.number} {self.tag} P{self.priority}: {self.description}"


class Register:
    def __init__(self) -> None:
        self.__orders = []

    def add(self, number: str, tag: str, priority: str, description: str) -> WorkOrder:
        if len(number.strip()) < 6:
            raise InvalidData("The number carries at least six characters")
        if len(tag.strip()) < 3:
            raise InvalidData("The tag carries at least three characters")
        try:
            level = int(priority)
        except ValueError:
            raise InvalidData("The priority is a number from 1 to 3")
        if level < 1 or level > 3:
            raise InvalidData("The priority runs from 1 to 3")
        if len(description.strip()) == 0:
            raise InvalidData("The description cannot be empty")
        order = WorkOrder(number.strip(), tag.strip().upper(), level, description.strip())
        self.__orders.append(order)
        return order

    def listing(self) -> list:
        return list(self.__orders)

    def __len__(self) -> int:
        return len(self.__orders)


if __name__ == "__main__":
    register = Register()

    print(register.add("OT-1042", "b-101", "1", "Mechanical seal replacement"))
    print(register.add("OT-1043", "C-310", "3", "Filter cleaning"))

    for data in [("OT-1", "B-101", "1", "x"), ("OT-1044", "V-12", "9", "Adjustment"),
                 ("OT-1045", "V-12", "two", "Adjustment")]:
        try:
            register.add(data[0], data[1], data[2], data[3])
        except InvalidData as ex:
            print("Rejected:", ex)

    print(len(register))
```
The window is the same one as 15.2, with a single change in the save slot:
```python
    def on_save(self) -> None:
        try:
            order = self.register.add(
                self.number.text(),
                self.tag.text(),
                self.priority.text(),
                self.description.text())
        except InvalidData as ex:
            self.notice.setText(str(ex))
            return
        self.list.addItem(str(order))
        self.notice.setText(f"Work orders entered: {len(self.register)}")
        self.on_clear()
```
**Output**
```text
OT-1042 B-101 P1: Mechanical seal replacement
OT-1043 C-310 P3: Filter cleaning
Rejected: The number carries at least six characters
Rejected: The priority runs from 1 to 3
Rejected: The priority is a number from 1 to 3
2
```
That is the output of running `register.py` from the terminal. In the window, entering priority 9 leaves the notice reading `The priority runs from 1 to 3` and adds nothing to the list.

**Rubric** (totals 10)
| Criterion | Points |
|---|---|
| register.py does not import PyQt6 and runs from the terminal | 3 |
| The four validations in order, each with its message | 3 |
| The slot only translates: it reads, calls, catches and shows | 2 |
| When the entry is rejected, the list does not grow | 2 |

**Most common mistake**
They check the length of the number inside the slot to avoid a pointless call. The rule ends up split between the window and the register, and the two versions contradict each other the moment one of them changes.

## Week 16 · Topic 7 · Databases and project

### 16.1 · Recognise
**Solution**
```text
The first block creates the table and commits it, so the structure lands on
disk. The second inserts the bearing and closes the connection without
committing: the transaction is thrown away and the row never reaches the file,
without a single error message. That is why the first COUNT returns 0.

The third block inserts the seal and does call commit before closing, so the
second COUNT returns 1.

fetchone returns the whole row, and a row always arrives as a tuple, even when
it carries a single column. Hence the comma inside the parentheses.
```
**Output**
```text
(0,)
(1,)
```
**Rubric** (totals 10)
| Criterion | Points |
|---|---|
| Both outputs, in tuple form | 4 |
| Explains that closing without committing throws the insert away | 3 |
| Says there is no error and no warning when that happens | 2 |
| Explains why fetchone returns a tuple | 1 |

**Most common mistake**
They answer `(1,)` and `(2,)` because they assume every INSERT saves itself. The engine holds it pending until somebody commits.

### 16.2 · Apply
**Solution**
```python
import sqlite3
from pathlib import Path

# Delete store.db before running this again: the codes are the primary key, so a
# second INSERT of BL-220 fails as a duplicate.
path = Path("store.db")

spares = [
    ("BL-220", "bearing", 12),
    ("SM-4471", "mechanical seal", 6),
    ("EM-905", "gasket", 30),
    ("RT-118", "oil seal", 2),
]

with sqlite3.connect(path) as connection:
    connection.execute(
        "CREATE TABLE IF NOT EXISTS SpareParts ("
        "code TEXT PRIMARY KEY, description TEXT NOT NULL, pieces INTEGER NOT NULL)")
    for code, description, pieces in spares:
        connection.execute(
            "INSERT INTO SpareParts VALUES (?, ?, ?)", (code, description, pieces))
    connection.commit()

with sqlite3.connect(path) as connection:
    cursor = connection.execute(
        "SELECT code, pieces FROM SpareParts WHERE pieces < ? ORDER BY pieces", (10,))
    for row in cursor:
        print(row)

    cursor = connection.execute(
        "SELECT description FROM SpareParts WHERE code = ?", ("EM-905",))
    print(cursor.fetchone())

    cursor = connection.execute("SELECT COUNT(*) FROM SpareParts")
    print(cursor.fetchone())
```
**Output**
```text
('RT-118', 2)
('SM-4471', 6)
('gasket',)
(4,)
```
**Rubric** (totals 10)
| Criterion | Points |
|---|---|
| The table with a primary key and the two mandatory columns | 2 |
| The values travel as parameters, never glued into the string | 4 |
| An explicit commit after the inserts | 2 |
| The ORDER BY sits in the query and not in Python | 2 |

**Most common mistake**
They build the query with an f-string "because it is only a number". It is the same hole as with text, and one quote inside the data is enough to change the shape of the query.

### 16.3 · Integrate
**Solution**
```python
import sqlite3
from pathlib import Path


class SparePartNotFound(Exception):
    pass


class SparePart:
    def __init__(self, code: str, description: str, pieces: int) -> None:
        self.code = code
        self.description = description
        self.pieces = pieces

    def issue(self, quantity: int) -> None:
        if quantity > self.pieces:
            raise ValueError(f"{self.code} only has {self.pieces} pieces")
        self.pieces -= quantity

    def __str__(self) -> str:
        return f"{self.code} ({self.description}): {self.pieces}"


class SQLiteStore:
    def __init__(self, path: Path) -> None:
        self.path = path
        with sqlite3.connect(self.path) as connection:
            connection.execute(
                "CREATE TABLE IF NOT EXISTS SpareParts ("
                "code TEXT PRIMARY KEY, description TEXT NOT NULL, pieces INTEGER NOT NULL)")
            connection.commit()

    def save(self, part: SparePart) -> None:
        with sqlite3.connect(self.path) as connection:
            connection.execute(
                "INSERT INTO SpareParts VALUES (?, ?, ?)",
                (part.code, part.description, part.pieces))
            connection.commit()

    def load(self, code: str) -> SparePart:
        with sqlite3.connect(self.path) as connection:
            cursor = connection.execute(
                "SELECT code, description, pieces FROM SpareParts WHERE code = ?",
                (code,))
            row = cursor.fetchone()
        if row is None:
            raise SparePartNotFound(f"{code} is not in the store")
        return SparePart(row[0], row[1], row[2])

    def below_minimum(self, minimum: int) -> list:
        with sqlite3.connect(self.path) as connection:
            cursor = connection.execute(
                "SELECT code, description, pieces FROM SpareParts "
                "WHERE pieces < ? ORDER BY pieces", (minimum,))
            rows = cursor.fetchall()
        return [SparePart(r[0], r[1], r[2]) for r in rows]


store = SQLiteStore(Path("plant.db"))

store.save(SparePart("BL-220", "bearing", 12))
store.save(SparePart("SM-4471", "mechanical seal", 6))
store.save(SparePart("RT-118", "oil seal", 2))

bearing = store.load("BL-220")
bearing.issue(9)
print(bearing)
print(store.load("BL-220"))

for part in store.below_minimum(10):
    print(part)

try:
    store.load("XX-999")
except SparePartNotFound as ex:
    print("Rejected:", ex)

try:
    bearing.issue(100)
except ValueError as ex:
    print("Rejected:", ex)
```
**Output**
```text
BL-220 (bearing): 3
BL-220 (bearing): 12
RT-118 (oil seal): 2
SM-4471 (mechanical seal): 6
Rejected: XX-999 is not in the store
Rejected: BL-220 only has 3 pieces
```
The two numbers differ because `load` builds a new object out of whatever the table held at that moment. Issuing nine pieces changed the object living in memory and nobody told the database. For them to stop differing, `SQLiteStore` would need an `update(part)` method carrying an `UPDATE`, called right after the issue.

**Rubric** (totals 10)
| Criterion | Points |
|---|---|
| SparePart does not import sqlite3 and all the SQL lives in the other class | 4 |
| load returns an object, not a tuple, and raises the custom exception | 2 |
| The paragraph explains that the object in memory and the row on disk are two things | 3 |
| below_minimum queries with a parameter and an ORDER BY | 1 |

**Most common mistake**
They drop an `import sqlite3` and a `save()` into the `SparePart` class. The class can no longer be tested without a database, and the SQL ends up split across two places.

## Week 17 · Final assessment

### 17.1 · Recognise
**Solution**
```text
Rule 1. card is written in Asset, but self keeps the real class of the object,
which is Pump. Python looks kind up starting from there: it runs the Pump
version, which in turn calls the Rotating one with super. That is where "pump
rotating" comes from.

Rule 2. The census is incremented on the class, with Asset.census += 1, so it
does stay on the class. One object was built, and it reads 1.

Rule 3. The attribute with two leading underscores was renamed to _Asset__tag
inside the interpreter. The first hasattr finds it under that name and the
second does not find it under the original one.

Rule 4. The tag property has a getter only. Assigning to it raises
AttributeError, because there is no setter to take the value.
```
**Output**
```text
B-101/pump rotating
1
True False
the property has no setter
```
**Rubric** (totals 10)
| Criterion | Points |
|---|---|
| The four outputs | 4 |
| Explains the method lookup starting from the real class of the object | 2 |
| Explains the renaming of the private attribute | 2 |
| Explains why the census reads 1 and why the property refuses the assignment | 2 |

**Most common mistake**
They answer "B-101/asset" because `card` is written in `Asset`. It is the same error as week 8, and in the final exam it costs twice as much.

### 17.2 · Apply
**Solution**
```python
import csv
from abc import ABC, abstractmethod
from pathlib import Path


class InvalidData(Exception):
    pass


class Equipment(ABC):
    def __init__(self, tag: str, hours: float) -> None:
        if len(tag.strip()) < 3:
            raise InvalidData(f"Invalid tag: {tag}")
        if hours < 0:
            raise InvalidData(f"{tag} cannot have {hours} hours")
        self._tag = tag.strip().upper()
        self.__hours = hours

    @property
    def tag(self) -> str:
        return self._tag

    @property
    def hours(self) -> float:
        return self.__hours

    @abstractmethod
    def draw_kw(self) -> float:
        ...

    @abstractmethod
    def kind(self) -> str:
        ...

    def row(self) -> dict:
        return {
            "tag": self.tag,
            "type": self.kind(),
            "hours": f"{self.hours:.0f}",
            "kw": f"{self.draw_kw():.1f}",
        }


class Pump(Equipment):
    def __init__(self, tag: str, hours: float, flow: float) -> None:
        super().__init__(tag, hours)
        self.flow = flow

    def draw_kw(self) -> float:
        return self.flow * 0.32

    def kind(self) -> str:
        return "pump"


class Compressor(Equipment):
    def __init__(self, tag: str, hours: float, pressure: float) -> None:
        super().__init__(tag, hours)
        self.pressure = pressure

    def draw_kw(self) -> float:
        return self.pressure * 8.0

    def kind(self) -> str:
        return "compressor"


def export(equipment: list, path: Path) -> None:
    fields = ["tag", "type", "hours", "kw"]
    with open(path, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fields)
        writer.writeheader()
        for item in equipment:
            writer.writerow(item.row())


plant = [
    Pump("b-101", 4820.0, 120.0),
    Pump("B-102", 1150.0, 95.0),
    Compressor("c-310", 6300.0, 8.5),
]

for data in [("XX", 100.0, 50.0), ("B-103", -20.0, 80.0)]:
    try:
        plant.append(Pump(data[0], data[1], data[2]))
    except InvalidData as ex:
        print("Rejected:", ex)

path = Path("equipment.csv")
export(plant, path)

print(path.read_text(encoding="utf-8"))
print(len(plant))
```
**Output**
```text
Rejected: Invalid tag: XX
Rejected: B-103 cannot have -20.0 hours
tag,type,hours,kw
B-101,pump,4820,38.4
B-102,pump,1150,30.4
C-310,compressor,6300,68.0

3
```
**Rubric** (totals 10)
| Criterion | Points |
|---|---|
| The validation lives in the constructor of the abstract class and raises InvalidData | 3 |
| Both abstract methods implemented in both children | 2 |
| The tags land clean and in capitals in the CSV | 2 |
| Export with DictWriter, a header, with and encoding | 3 |

**Most common mistake**
They repeat the validation in every child instead of chaining with `super`. The day the tag rule changes, three constructors need touching, and one of them gets left behind.

### 17.3 · Integrate
**Solution**
```python
import csv
import sqlite3
from abc import ABC, abstractmethod
from pathlib import Path


class InvalidReading(Exception):
    pass


class Instrument(ABC):
    def __init__(self, tag: str, low: float, high: float) -> None:
        self._tag = tag
        self._low = low
        self._high = high

    @property
    def tag(self) -> str:
        return self._tag

    @abstractmethod
    def unit(self) -> str:
        ...

    def validate(self, text: str) -> float:
        try:
            value = float(text)
        except ValueError:
            raise InvalidReading(f"{self._tag} sent {text} and that is not a number")
        if value < self._low or value > self._high:
            raise InvalidReading(
                f"{self._tag} read {value} {self.unit()} outside "
                f"{self._low} to {self._high}")
        return value


class Thermocouple(Instrument):
    def unit(self) -> str:
        return "C"


class PressureGauge(Instrument):
    def unit(self) -> str:
        return "bar"


class FlowMeter(Instrument):
    def unit(self) -> str:
        return "L/s"


class History:
    def __init__(self, path: Path) -> None:
        self.path = path
        with sqlite3.connect(self.path) as connection:
            connection.execute(
                "CREATE TABLE IF NOT EXISTS Readings ("
                "id INTEGER PRIMARY KEY, tag TEXT NOT NULL, value REAL NOT NULL)")
            connection.commit()

    def save(self, tag: str, value: float) -> None:
        with sqlite3.connect(self.path) as connection:
            connection.execute(
                "INSERT INTO Readings (tag, value) VALUES (?, ?)", (tag, value))
            connection.commit()

    def values(self, tag: str) -> list:
        with sqlite3.connect(self.path) as connection:
            cursor = connection.execute(
                "SELECT value FROM Readings WHERE tag = ? ORDER BY id", (tag,))
            return [row[0] for row in cursor.fetchall()]


def load_raw(path: Path) -> list:
    try:
        with open(path, newline="", encoding="utf-8") as file:
            return list(csv.DictReader(file))
    except FileNotFoundError:
        return []


def write_report(path: Path, summary: dict, discarded: list) -> None:
    with open(path, "w", encoding="utf-8") as file:
        file.write("Telemetry report\n")
        for tag, average in summary.items():
            file.write(f"{tag}: {average:.2f}\n")
        file.write(f"Discarded: {len(discarded)}\n")
        for reason in discarded:
            file.write(f"  {reason}\n")


panel = {
    "TT-101": Thermocouple("TT-101", 0.0, 400.0),
    "PT-205": PressureGauge("PT-205", 0.0, 10.0),
    "FT-330": FlowMeter("FT-330", 0.0, 200.0),
}

raw = [
    {"tag": "TT-101", "value": "74.5"},
    {"tag": "PT-205", "value": "6.1"},
    {"tag": "TT-101", "value": "81.2"},
    {"tag": "FT-330", "value": "118.0"},
    {"tag": "PT-205", "value": "n/a"},
    {"tag": "TT-101", "value": "412.0"},
    {"tag": "XX-999", "value": "3.0"},
]

source = Path("raw.csv")
with open(source, "w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=["tag", "value"])
    writer.writeheader()
    writer.writerows(raw)

# The database is rebuilt on every run, or the readings would pile up.
database = Path("history.db")
database.unlink(missing_ok=True)

history = History(database)
discarded = []

for row in load_raw(source):
    tag = row["tag"]
    instrument = panel.get(tag)
    if instrument is None:
        discarded.append(f"{tag} is not on the panel")
        continue
    try:
        history.save(tag, instrument.validate(row["value"]))
    except InvalidReading as ex:
        discarded.append(str(ex))

summary = {}
for tag, instrument in panel.items():
    values = history.values(tag)
    if len(values) == 0:
        continue
    total = 0.0
    for value in values:
        total += value
    summary[tag] = total / len(values)

target = Path("report.txt")
write_report(target, summary, discarded)

print(target.read_text(encoding="utf-8"))
print(history.values("TT-101"))
```
**Output**
```text
Telemetry report
TT-101: 77.85
PT-205: 6.10
FT-330: 118.00
Discarded: 3
  PT-205 sent n/a and that is not a number
  TT-101 read 412.0 C outside 0.0 to 400.0
  XX-999 is not on the panel

[74.5, 81.2]
```
**Rubric** (totals 10)
| Criterion | Points |
|---|---|
| Instrument abstract, with a concrete validate that uses the abstract method | 2 |
| The CSV is read with DictReader and a missing file does not blow up | 2 |
| All the SQL lives in History and uses placeholders | 2 |
| The unknown tag is checked with an if and the rest is validated with try | 2 |
| The report comes out with the averages computed from the database | 2 |

**Most common mistake**
They compute the average over the raw list in memory: the rejected 412.0 slips into the TT-101 figure, which climbs from 77.85 to 189.23 with the report none the wiser.
