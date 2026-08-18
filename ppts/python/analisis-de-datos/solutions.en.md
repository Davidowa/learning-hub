# Solutions · Data Analysis · TIA502

Instructor's copy. For every exercise it carries the solution as it was run, the exact output it produces, the ten-point rubric and the mistake that shows up most while marking. The programs from weeks 1 to 14 run on Python 3.13 and the standard library. Those from weeks 15 to 17 need pandas, and those from 16 and 17 also need matplotlib and seaborn. Runs that use `input` are shown as they look on screen, with the typed value beside the prompt.

---

## Week 01 · Course introduction and the bridge from Excel to Python

### 01.1 · Recognise

**Solution**

```text
jan 128400
jun 134050
54850
6
```

`sales[3]` is the fourth item of the column, so it corresponds to row 5 of the sheet: row 1 is the header and the data starts at row 2. `print(months[6])` raises `IndexError`, because the list has six items and the last valid index is 5.

**Output**

```text
jan 128400
jun 134050
54850
6
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The four lines, in order and with both values where two belong | 4 |
| The subtraction on the third line gives 54850 | 2 |
| The spreadsheet row is placed correctly and the offset is explained | 2 |
| `IndexError` named, with the last valid index | 2 |

**Most common mistake**

Answering that `sales[3]` is row 3 of the sheet. The giveaway is an explanation that mentions neither the header nor the zero index.

### 01.2 · Apply

**Solution**

```python
months = ["jan", "feb", "mar", "apr", "may", "jun"]
sales = [128400, 96750, 143200, 118900, 151600, 134050]

total = sum(sales)
average = total / len(sales)
best = months[sales.index(max(sales))]
gap = max(sales) - average

print(f"Half-year sales: {total:,.0f}")
print(f"Monthly average: {average:,.2f}")
print(f"Best month: {best} with {max(sales):,.0f}")
print(f"The best month beats the average by {gap:,.2f}")
```

**Output**

```text
Half-year sales: 772,900
Monthly average: 128,816.67
Best month: may with 151,600
The best month beats the average by 22,783.33
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| Total and average correct, worked out with `sum` and `len` | 3 |
| The best month comes from `index` over `max`, not typed in | 3 |
| The gap against the average is correct | 2 |
| The four formats applied where the statement asks for them | 2 |

**Most common mistake**

Writing `best = "may"` because the list is right there. The giveaway is a program that still says may after one figure in the list changes.

### 01.3 · Integrate

**Solution**

```python
products = ["Professional notebook", "Black ballpoint pen",
            "Ring binder", "Permanent marker"]
units = [1840, 5210, 960, 2375]
prices = [38.50, 9.90, 74.00, 22.50]

position = units.index(max(units))
leader = products[position]
amount = units[position] * prices[position]
share = units[position] / sum(units) * 100

print(f"Leading product: {leader}")
print(f"Pieces sold: {units[position]:,}")
print(f"Amount it brought in: {amount:,.2f}")
print(f"Share of the pieces: {share:.1f} %")
print(f"Pieces sold in the month: {sum(units):,}")
```

**Output**

```text
Leading product: Black ballpoint pen
Pieces sold: 5,210
Amount it brought in: 51,579.00
Share of the pieces: 50.2 %
Pieces sold in the month: 10,385
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The position is worked out once and serves all three lists | 3 |
| Amount correct, using the price belonging to that position | 2 |
| Share correct, with one decimal and its symbol | 2 |
| The five lines carry a readable label | 2 |
| The program stays correct when the leader changes | 1 |

**Most common mistake**

Working out the position three times, once per list, repeating `units.index(max(units))`. It works, and it gives away that the three lists sharing one position never landed.

---

## Week 02 · Algorithm design

### 02.1 · Recognise

**Solution**

| Customer | Conditions evaluated | Which one holds | discount |
|---|---|---|---|
| Abarrotes La Paz | Overdue > 0? No. 620,000 ≥ 500,000 and 36 ≥ 24? Yes | The second | 0.12 |
| Ferretería Muñoz | Overdue > 0? Yes | The first | 0 |
| Papelera Bruno | Overdue > 0? No. 200,000 ≥ 500,000? No. 200,000 ≥ 200,000? Yes | The third | 0.06 |

Ferretería Muñoz buys more than La Paz and gets no discount, because the overdue balance is checked first and no later condition is ever evaluated. Papelera Bruno lands in the third branch on the exact boundary value: the operator includes the limit.

The property that would break with «IF the customer is important» is precision. Who counts as important is decided by whoever reads the algorithm, and two people will decide differently about the same customer. Once precision goes, definiteness goes with it, because the same data stops producing the same result.

**Output**

What gets handed in is the trace table above, with the three discounts of 0.12, 0 and 0.06, plus the paragraph on the property.

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The three discounts correct | 3 |
| The trace shows which conditions were evaluated and which were not | 3 |
| Precision is named and explained through the case, not in the abstract | 3 |
| It is stated that Ferretería Muñoz never reaches the second branch | 1 |

**Most common mistake**

Giving 0.12 to Ferretería Muñoz because both amounts qualify. The giveaway is a trace with no row for the overdue balance.

### 02.2 · Apply

**Solution**

```text
START
    READ salary, tenure, rating, absences

    IF tenure < 6 THEN
        bonus = 0
    ELSE IF rating >= 4.5 THEN
        bonus = salary * 0.15
    ELSE IF rating >= 3.5 THEN
        bonus = salary * 0.08
    ELSE
        bonus = 1200

    IF absences > 3 THEN
        bonus = bonus / 2

    WRITE bonus
END
```

The absence penalty sits outside the chain of decisions, after the bonus has already been worked out. Putting it inside would force it to be repeated in all four branches.

The flowchart carries an oval for the start, a parallelogram reading the four values, three chained diamonds with their yes and no exits labelled, four assignment rectangles, one more diamond for the absences, a rectangle for the division and a parallelogram writing the result before the end oval.

Trace for Marina Cortés: tenure 8, so the first branch is skipped. Rating 4.6, so the second branch is taken: bonus = 24,500 × 0.15 = 3,675. Absences 4, more than 3: bonus = 3,675 / 2 = 1,837.50.

**Output**

```text
bonus = 1837.50
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The four bonus branches, in the right order | 3 |
| The absence penalty sits outside the chain and is applied once | 2 |
| The flowchart uses each symbol for what it is meant for | 2 |
| Every diamond carries both exits labelled and both lead somewhere | 2 |
| The trace for Marina Cortés arrives at 1,837.50 | 1 |

**Most common mistake**

Writing the absence penalty inside every branch and forgetting it in one. The giveaway is pseudocode with four divisions by two instead of one.

### 02.3 · Integrate

**Solution**

One defensible decomposition splits the close into three pieces:

1. **Work out gross pay.** Takes base salary, days worked, overtime hours and commissions. Hands back total gross pay for the period.
2. **Work out deductions.** Takes total gross pay, outstanding loans and the withholding rate. Hands back total deductions.
3. **Work out net pay and produce the payslip.** Takes gross pay and deductions. Hands back the net amount and the breakdown.

Each piece can be tested on its own because its input and its output are stated. The second one does not need to know how gross pay was worked out, only what it adds up to.

Pseudocode for the first piece:

```text
START
    READ base_salary, days_worked, overtime_hours, commissions

    daily_rate = base_salary / 30
    pro_rata = daily_rate * days_worked

    IF overtime_hours > 9 THEN
        overtime_pay = daily_rate / 8 * (9 * 2 + (overtime_hours - 9) * 3)
    ELSE
        overtime_pay = daily_rate / 8 * overtime_hours * 2

    gross_pay = pro_rata + overtime_pay + commissions

    WRITE gross_pay
END
```

Edge case: an employee who joined halfway through the fortnight and carries zero days worked because of sick leave. The first version, the one multiplying the daily rate by 15 without reading the days, paid them the full fortnight. The version above solves it by reading the days as input, and with zero days the pro rata comes to zero with no special case at all.

**Output**

What gets handed in is the decomposition into three pieces with their inputs and outputs, the pseudocode for one of them, and the paragraph on the edge case with the wrong result it used to produce.

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| Three subproblems with a name, an input and an output declared | 3 |
| The pieces are independent: none needs the inside of another | 2 |
| The chosen pseudocode has at least two decisions and terminates | 2 |
| The edge case broke the earlier version and the fix is stated | 2 |
| The swap test was carried out and its result is reported | 1 |

**Most common mistake**

Splitting the process into three steps that are really one step written across three lines, such as read, calculate and print. The giveaway is that none of the three pieces can be tested without the other two.

---

## Week 03 · Paradigms and an introduction to programming

### 03.1 · Recognise

**Solution**

```python
budget = 250000
budget = budget - 40000
budget = budget * 2
budget = budget + 15000

print(budget)
```

Every line reads the value the previous one left and stores over it: 250000, 210000, 420000, 435000.

| Line | Error | Where it reports it |
|---|---|---|
| `Print(budget)` | `NameError`, because `Print` with a capital does not exist | On that same line, as it runs |
| `print("Budget: , budget)` | `SyntaxError`, the closing quote never arrives | On that line or the next one |
| `print(budget` | `SyntaxError`, the parenthesis is never closed | Almost always on the line below |

**Output**

```text
435000
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The result is 435000 | 3 |
| It is explained that the equals sign stores rather than compares | 2 |
| The three error types named correctly | 3 |
| It is stated that an unclosed parenthesis is reported one line down | 2 |

**Most common mistake**

Answering 250000 because «the first line is the one that defines the variable». The giveaway is an answer with no intermediate trace at all.

### 03.2 · Apply

**Solution**

```python
# Fortnightly payroll for the sales area.
from statistics import mean

salaries = [23200, 42800, 82700, 24500, 31600, 28900]

average = mean(salaries)
highest = max(salaries)

print("Employees:", len(salaries))
print("Average salary:", average)
print("Highest salary:", highest)
```

**Output**

```text
Employees: 6
Average salary: 38950
Highest salary: 82700
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The program runs and shows the three lines | 3 |
| The average comes from `mean`, imported at the top of the file | 3 |
| Header comment present and useful | 2 |
| The variable names say what they hold | 2 |

**Most common mistake**

Importing `statistics` inside the body of the program, in among the calculations. It runs the same, and it hides what the file depends on.

### 03.3 · Integrate

**Solution**

```python
# Cash close for the Reforma branch.
from statistics import mean

days = ["mon", "tue", "wed", "thu", "fri", "sat"]
revenue = [18400, 15750, 21300, 19850, 27600, 34200]

average = mean(revenue)
best = days[revenue.index(max(revenue))]

print("Days recorded:", len(revenue))
print("Revenue for the week:", sum(revenue))
print("Average revenue:", average)
print("Best day:", best)
```

| Problem | Message | Fix |
|---|---|---|
| `Print` with a capital | `NameError: name 'Print' is not defined` | Write it in lower case |
| Unclosed parenthesis on that same line | `SyntaxError`, reported on the next line | Close the parenthesis |
| Missing comma before `average` | `SyntaxError: invalid syntax` | Separate the arguments with a comma |
| `best` is worked out and never printed | No error | Add the fourth `print` |

**Output**

```text
Days recorded: 6
Revenue for the week: 137100
Average revenue: 22850
Best day: sat
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The corrected program runs and shows the four lines | 3 |
| The three syntax errors identified with their type | 3 |
| The fourth problem is recognised as a calculation with no output, not an error | 2 |
| The table says where Python reports each error | 2 |

**Most common mistake**

Reporting three problems instead of four. The calculation that never prints raises nothing, which is exactly why it gets walked past.

---

## Week 04 · Data, data types and primitive operations

### 04.1 · Recognise

**Solution**

```text
179
4
32
12500
<class 'float'>
```

The fourth line concatenates because `price` is text: it sticks the `"0"` onto the end of `"1250"`. The fifth says `float` because division with a single slash always returns a decimal, even when both operands are integers and the division comes out exact.

**Output**

```text
179
4
32
12500
<class 'float'>
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The five lines correct | 5 |
| The concatenation is explained through the type of `price` | 3 |
| It is explained that single-slash division always returns `float` | 2 |

**Most common mistake**

Answering 1260 on the fourth line. The giveaway is an explanation that talks about addition rather than text stuck together.

### 04.2 · Apply

**Solution**

```python
units = 4300
per_box = 24
price_text = "18.75"
freight = 3200

price = float(price_text)
full_boxes = units // per_box
loose = units % per_box
goods = units * price

per_box_no_brackets = goods / full_boxes + freight
per_box_with_brackets = (goods + freight) / full_boxes

print("Full boxes:", full_boxes)
print("Loose pieces:", loose)
print("Cost of the goods:", round(goods, 2))
print("Without parentheses:", round(per_box_no_brackets, 2))
print("With parentheses:", round(per_box_with_brackets, 2))
print(type(price), type(full_boxes))
```

The version with parentheses is the one that answers what it costs to put one box on the loading dock: it spreads the freight across the 179 boxes. The other one adds the whole freight bill to every single box, which is why it gives a number almost eight times larger without flagging anything.

**Output**

```text
Full boxes: 179
Loose pieces: 4
Cost of the goods: 80625.0
Without parentheses: 3650.42
With parentheses: 468.3
<class 'float'> <class 'int'>
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| Full boxes and loose pieces with `//` and `%` | 3 |
| The price is converted with `float` before any multiplication | 2 |
| Both versions of the cost per box, with their figures | 2 |
| The explanation says which one answers the loading dock question and why | 2 |
| Both types printed at the end | 1 |

**Most common mistake**

Multiplying `units * price_text` without converting. It raises nothing: it repeats the text 4,300 times and fills the screen.

### 04.3 · Integrate

**Solution**

```python
suppliers = ["Papelera del Centro", "Insumos Aurora",
             "Distribuidora Sol", "Comercial Bravo", "Grupo Nardo"]
costs = [18420.50, 9375.00, 24680.75, 6120.25, 15302.50]
vat_rate = 0.16
pieces = 3400
pieces_per_pallet = 48

subtotal = sum(costs)
total = subtotal
total *= (1 + vat_rate)
cost_per_piece = total / pieces
pallets = pieces // pieces_per_pallet
left_over = pieces % pieces_per_pallet

print(f"Suppliers on the order: {len(suppliers)}")
print(f"Subtotal: ${subtotal:,.2f}")
print(f"Total with VAT: ${total:,.2f}")
print(f"Cost per piece: ${cost_per_piece:,.2f}")
print(f"Full pallets: {pallets}, left over: {left_over}")
print(type(subtotal), type(pallets))
```

**Output**

```text
Suppliers on the order: 5
Subtotal: $73,899.00
Total with VAT: $85,722.84
Cost per piece: $25.21
Full pallets: 70, left over: 40
<class 'float'> <class 'int'>
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| Subtotal with `sum` and total with `*=` on a variable | 3 |
| Cost per piece worked out on the total with VAT | 2 |
| Pallets and pieces left over with the two divisions | 2 |
| Currency format with thousands and two decimals | 2 |
| Both types printed and correct | 1 |

**Most common mistake**

Writing `total = subtotal * 1.16` on one line. It gives the same number and skips the operator the statement asked for, which is the one that later stops the rate being repeated in three places.

---

## Week 05 · Statements, input and output

### 05.1 · Recognise

**Solution**

```text
248,910
2.7%
$41,250.50
Reach: {impressions:,}
|     248,910|
```

The fourth string is missing its opening `f`, so the braces print exactly as written. Python does not flag it because a string with braces is a valid string: the program does precisely what it says, it just is not what its author wanted. The fifth reserves twelve spaces and aligns right, which is where the five spaces before the number come from.

**Output**

```text
248,910
2.7%
$41,250.50
Reach: {impressions:,}
|     248,910|
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The five lines, with commas and symbols where they belong | 5 |
| The percentage rounded to one decimal, not truncated | 1 |
| The missing `f` identified and explained as not being an error | 2 |
| The padding on the last line is five spaces | 2 |

**Most common mistake**

Answering `0.0%` on the second line. The giveaway is a student forgetting that the percentage code already multiplies by a hundred.

### 05.2 · Apply

**Solution**

```python
campaign = input("Campaign name: ")
impressions = int(input("Impressions: "))
clicks = int(input("Clicks: "))
spend = float(input("Spend in pesos: "))

conversion = clicks / impressions
cost_per_click = spend / clicks
cost_per_thousand = spend / impressions * 1000

print(f"Campaign: {campaign}")
print(f"Impressions: {impressions:,}")
print(f"Conversion: {conversion:.2%}")
print(f"Cost per click: ${cost_per_click:,.2f}")
print(f"Cost per thousand impressions: ${cost_per_thousand:,.2f}")
```

**Output**

```text
Campaign name: Verano Bajío
Impressions: 248910
Clicks: 6795
Spend in pesos: 52400
Campaign: Verano Bajío
Impressions: 248,910
Conversion: 2.73%
Cost per click: $7.71
Cost per thousand impressions: $210.52
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The four `input` calls with a prompt, and the name left unconverted | 2 |
| `int` and `float` wrapping the `input`, not applied afterwards | 3 |
| The three metrics correct | 3 |
| Thousands, percentage and currency applied where they belong | 2 |

**Most common mistake**

Converting after reading, on a separate line that reassigns the variable. It works here, and the moment an operation sits between the reading and the conversion the result comes out wrong with no warning.

### 05.3 · Integrate

**Solution**

```python
week = input("Week: ")
revenue = float(input("Revenue for the week: "))
outgoings = float(input("Outgoings for the week: "))
customers = int(input("Customers served: "))

balance = revenue - outgoings
margin = balance / revenue
average_sale = revenue / customers
daily = balance / 7

print(f"Cash flow for week {week}")
print(f"{'Revenue':<22}{revenue:>14,.2f}")
print(f"{'Outgoings':<22}{outgoings:>14,.2f}")
print(f"{'Balance':<22}{balance:>14,.2f}")
print(f"{'Margin':<22}{margin:>14.1%}")
print(f"{'Average sale':<22}{average_sale:>14,.2f}")
print(f"{'Balance per day':<22}{daily:>14,.2f}")
```

**Output**

```text
Week: 14
Revenue for the week: 186400
Outgoings for the week: 143750
Customers served: 612
Cash flow for week 14
Revenue                   186,400.00
Outgoings                 143,750.00
Balance                    42,650.00
Margin                         22.9%
Average sale                  304.58
Balance per day             6,092.86
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The four inputs with the right type each | 2 |
| Balance, margin, average sale and balance per day correct | 3 |
| The columns aligned to the widths the statement asks for | 3 |
| The margin as a percentage and the money with two decimals | 2 |

**Most common mistake**

Converting the week to an integer. Nothing breaks here, and the moment somebody enters «14 bis» the program falls over on its first line. What is not operated on does not get converted.

---

## Week 06 · Selection structures

### 06.1 · Recognise

**Solution**

```text
18.0% · High
```

| turnover | Winning branch | Output |
|---|---|---|
| 0.25 | The first, because the operator includes the limit | `25.0% · Critical` |
| 0.099 | None of the three, it falls to the `else` | `9.9% · Low` |
| 0.30 | The first | `30.0% · Critical` |

With `>` instead of `>=` on the second `elif`, an area turning over exactly 18 % would stop being High and drop to Normal, which is the band that triggers different actions in human resources.

**Output**

```text
18.0% · High
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The exact line, with the percentage formatted | 3 |
| The three cases in the table correct | 3 |
| It is explained that 0.25 enters through the first branch, not the second | 2 |
| The effect of swapping `>=` for `>` is stated using the 18 % case | 2 |

**Most common mistake**

Classifying 0.25 as High because «it satisfies the second condition too». It satisfies both, and the first one that holds is the only one that runs.

### 06.2 · Apply

**Solution**

```python
supplier = input("Supplier: ")
on_time = float(input("On-time deliveries (0 to 1): "))

if on_time >= 0.95:
    category = "Preferred"
elif on_time >= 0.85:
    category = "Reliable"
elif on_time >= 0.70:
    category = "Under watch"
else:
    category = "Contract under review"

print(f"{supplier}: {on_time:.1%} · {category}")
```

**Output**

```text
Supplier: Insumos Aurora
On-time deliveries (0 to 1): 0.96
Insumos Aurora: 96.0% · Preferred

Supplier: Distribuidora Sol
On-time deliveries (0 to 1): 0.85
Distribuidora Sol: 85.0% · Reliable

Supplier: Comercial Bravo
On-time deliveries (0 to 1): 0.62
Comercial Bravo: 62.0% · Contract under review
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The four categories, from most demanding to least | 4 |
| The categories are exclusive: no supplier lands in two | 2 |
| The three runs handed in, the boundary one included | 2 |
| The output line with name, percentage and category | 2 |

**Most common mistake**

Writing the conditions from lowest to highest. In that order Insumos Aurora comes out «Under watch», because 0.96 is also greater than or equal to 0.70 and that branch gets evaluated first.

### 06.3 · Integrate

**Solution**

```python
centre = input("Cost centre: ")
budget = float(input("Budget for the month: "))
spent = float(input("Actual spend: "))

variance = (spent - budget) / budget

if variance > 0.10:
    status = "Overspend"
elif variance >= 0:
    status = "At the limit"
elif variance >= -0.15:
    status = "Within range"
else:
    status = "Underspend"

print(f"Cost centre: {centre}")
print(f"Budget: ${budget:,.2f}")
print(f"Actual spend: ${spent:,.2f}")
print(f"Variance: {variance:.1%}")
print(f"Status: {status}")
```

Spending 8.5 % over budget does not land in the first category because the policy put the overspend boundary above 10 %, not above zero. Spending over budget without passing that margin is what the policy calls being at the limit.

**Output**

```text
Cost centre: Logistics
Budget for the month: 480000
Actual spend: 521000
Cost centre: Logistics
Budget: $480,000.00
Actual spend: $521,000.00
Variance: 8.5%
Status: At the limit
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The variance is worked out over the budget, not over the spend | 2 |
| The four categories in the right order | 3 |
| The negatives are handled properly: the `-0.15` sits where it belongs | 2 |
| The five lines with currency and percentage format | 2 |
| The explanation of the 10 % boundary | 1 |

**Most common mistake**

Dividing by the actual spend. It gives 7.9 % instead of 8.5 % and the status comes out the same, so the error survives a quick review.

---

## Week 07 · Nested selection and logical operators

### 07.1 · Recognise

**Solution**

```text
Established territory
False
True
True
True
```

In `region == "North" or "West"`, Python evaluates two separate things: the comparison, which gives `False`, and the string `"West"`, which counts as true because it is not empty. The `or` keeps the second one and the condition always holds, whatever the region is. The correct version repeats the variable or uses membership:

```python
if region in ["North", "West"]:
    print("Established territory")
else:
    print("Developing territory")
```

**Output**

```text
Established territory
False
True
True
True
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The five lines correct | 4 |
| It is explained that a non-empty string evaluates as true | 3 |
| The corrected version uses `in` or repeats the full comparison | 3 |

**Most common mistake**

Answering «Developing territory» because Bajío is neither of the two. That is the result anybody would expect from reading the condition out loud, and it is exactly why the error survives for months in a file.

### 07.2 · Apply

**Solution**

```python
ELIGIBLE_SECTORS = ["Commerce", "Manufacturing", "Services"]

name = input("Customer: ")
income = float(input("Verified monthly income: "))
tenure = int(input("Months the business has traded: "))
sector = input("Sector: ")
credit = input("Clean credit history? (yes/no): ")

clean_history = credit == "yes"

if (income >= 25000 and tenure >= 24
        and sector in ELIGIBLE_SECTORS and clean_history):
    outcome = "Approved"
elif income >= 60000 and clean_history:
    outcome = "Approved on income"
elif not clean_history:
    outcome = "Rejected on credit history"
else:
    outcome = "Rejected"

print(f"{name}: {outcome}")
```

**Output**

```text
Customer: Abarrotes La Paz
Verified monthly income: 31500
Months the business has traded: 36
Sector: Commerce
Clean credit history? (yes/no): yes
Abarrotes La Paz: Approved

Customer: Taller Mecánico Rueda
Verified monthly income: 72000
Months the business has traded: 14
Sector: Services
Clean credit history? (yes/no): yes
Taller Mecánico Rueda: Approved on income

Customer: Constructora Zafiro
Verified monthly income: 84000
Months the business has traded: 60
Sector: Construction
Clean credit history? (yes/no): no
Constructora Zafiro: Rejected on credit history
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The first rule joins its four conditions with `and` | 3 |
| The sectors live in a list and are checked with `in` | 2 |
| The order of the rules matches the statement | 2 |
| The three runs handed in and correct | 2 |
| The outcome is stored in a variable and printed once | 1 |

**Most common mistake**

Putting the high income rule ahead of the credit history one. Constructora Zafiro comes out «Approved on income» and the rejection on credit is lost, which is exactly the case the policy was built to catch.

### 07.3 · Integrate

**Solution**

```python
CRITICAL = ["Insumos Aurora", "Grupo Nardo"]

supplier = input("Supplier: ")
contract_live = input("Contract in force? (yes/no): ") == "yes"
on_time = float(input("On-time deliveries (0 to 1): "))

if contract_live:
    if on_time >= 0.95:
        action = "Increase volume"
    elif on_time >= 0.85:
        action = "Hold volume"
    else:
        action = "Audit and cut volume"
else:
    action = "Renew the contract before evaluating"

if supplier in CRITICAL and on_time < 0.85:
    alert = "Find a second source"
else:
    alert = "No alert"

print(f"{supplier}: {on_time:.0%} · {action}")
print(f"Alert: {alert}")
```

Nesting the action buys something real: with no contract, the compliance record decides nothing and the three bands never get evaluated. The alert is different: both its conditions can always be asked, which is why they sit joined by `and` on a single level. Written nested it would look like this:

```python
if supplier in CRITICAL:
    if on_time < 0.85:
        alert = "Find a second source"
    else:
        alert = "No alert"
else:
    alert = "No alert"
```

Both versions give the same result in all four possible cases. The first reads better because «No alert» appears once: in the nested one it is written twice, and whoever changes one and forgets the other leaves the program with two different behaviours.

**Output**

```text
Supplier: Insumos Aurora
Contract in force? (yes/no): yes
On-time deliveries (0 to 1): 0.82
Insumos Aurora: 82% · Audit and cut volume
Alert: Find a second source

Supplier: Distribuidora Sol
Contract in force? (yes/no): no
On-time deliveries (0 to 1): 0.97
Distribuidora Sol: 97% · Renew the contract before evaluating
Alert: No alert
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The nested action keeps the contract question on the outside | 3 |
| The three inner bands, in order and exclusive | 2 |
| The alert combines membership and comparison with `and` | 2 |
| The two runs handed in | 1 |
| The argument compares both versions on readability, not on taste | 2 |

**Most common mistake**

Asking about compliance before asking about the contract. Distribuidora Sol comes out «Increase volume» on an expired contract, which is a recommendation nobody can act on.

---

## Week 08 · Repetition · First midterm

### 08.1 · Recognise

**Solution**

```text
3
7
11
5 0
```

`range(3, 12, 4)` starts at 3 and steps by four without reaching 12, so it produces 3, 7 and 11.

| Pass | Fund on entry | Fund ≥ 96,000? | Fund on exit | month |
|---|---|---|---|---|
| 4 | 192,000 | Yes | 96,000 | 4 |
| 5 | 96,000 | Yes | 0 | 5 |
| – | 0 | No | 0 | 5 |

On this data, `fund > 0` would give the same result, because 480,000 is an exact multiple of 96,000. The difference shows up with a fund that does not divide evenly: `fund > 0` lets one more pass through and ends with the fund negative, which is a month that cannot actually be paid.

**Output**

```text
3
7
11
5 0
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The three values of the `range`, without 11 plus four | 3 |
| The last line is `5 0` | 2 |
| The trace shows the condition being checked before every pass | 3 |
| The answer on `fund > 0` mentions the case that does not divide evenly | 2 |

**Most common mistake**

Answering that the `range` produces four values because 11 plus 4 is 15 and «there is still room». The stop value is excluded and 15 is already past it.

### 08.2 · Apply

**Solution**

```python
branches = ["Reforma", "Satélite", "Valle", "Chapalita", "Mitras"]
leavers = [7, 12, 4, 9, 15]
headcount = [86, 140, 62, 108, 125]

for i in range(len(branches)):
    turnover = leavers[i] / headcount[i]
    print(f"{branches[i]:<12}{leavers[i]:>4}{headcount[i]:>6}{turnover:>9.1%}")

print(f"{'Global':<12}{sum(leavers):>4}{sum(headcount):>6}"
      f"{sum(leavers) / sum(headcount):>9.1%}")
```

**Output**

```text
Reforma        7    86     8.1%
Satélite      12   140     8.6%
Valle          4    62     6.5%
Chapalita      9   108     8.3%
Mitras        15   125    12.0%
Global        47   521     9.0%
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The loop walks with `range(len(...))` and works for any length | 3 |
| The five turnover figures correct | 2 |
| The global figure divides sum by sum instead of averaging the five | 3 |
| The column widths and the percentage with one decimal | 2 |

**Most common mistake**

Working out the global figure as the average of the five percentages. It gives 8.7 % instead of 9.0 %, and the gap widens as soon as the headcounts differ in size.

### 08.3 · Integrate

**Solution**

```python
months = ["jan", "feb", "mar", "apr", "may", "jun"]
revenue = [412000, 388500, 455200, 401800, 372900, 468300]
outgoings = [398400, 401200, 430600, 418500, 395700, 402100]

print(f"{'Month':<6}{'Revenue':>12}{'Outgoings':>12}{'Balance':>12}  Status")

for i in range(len(months)):
    balance = revenue[i] - outgoings[i]

    if balance >= 0:
        status = "Surplus"
    else:
        status = "Deficit"

    print(f"{months[i]:<6}{revenue[i]:>12,}{outgoings[i]:>12,}"
          f"{balance:>12,}  {status}")

print(f"{'Total':<6}{sum(revenue):>12,}{sum(outgoings):>12,}"
      f"{sum(revenue) - sum(outgoings):>12,}")

fund = 250000
deficit = 22800
months_covered = 0

while fund >= deficit:
    fund -= deficit
    months_covered += 1

print(f"The fund covers {months_covered} months of deficit "
      f"and ${fund:,} is left unused.")
```

**Output**

```text
Month      Revenue   Outgoings     Balance  Status
jan        412,000     398,400      13,600  Surplus
feb        388,500     401,200     -12,700  Deficit
mar        455,200     430,600      24,600  Surplus
apr        401,800     418,500     -16,700  Deficit
may        372,900     395,700     -22,800  Deficit
jun        468,300     402,100      66,200  Surplus
Total    2,498,700   2,446,500      52,200
The fund covers 10 months of deficit and $22,000 is left unused.
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The `for` works out the balance month by month and classifies it | 3 |
| The totals come from `sum` over the complete lists | 2 |
| The `while` terminates and reports 10 months with 22,000 left | 3 |
| The table stays aligned and the figures carry a thousands separator | 2 |

**Most common mistake**

Writing the `while` with `fund > 0`. It gives 11 months and leaves the fund at minus 800 pesos, which is a month the treasury cannot pay.

---

## Week 09 · Accumulators, flags and nested loops

### 09.1 · Recognise

**Solution**

```text
15302
3
True
No purchase goes to committee
```

The first line does not print 73,877 because `total = 0` sits inside the loop: it resets on every pass and by the end holds only the last requisition. The fix is one line, moving the initialisation above the `for`:

```python
total = 0

for purchase in purchases:
    total += purchase
```

The `else` of the last loop runs because no purchase passes 30,000 and the `break` never fired. That is exactly what it is for: saying «I walked the whole thing and found nothing».

**Output**

```text
15302
3
True
No purchase goes to committee
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The four lines correct | 4 |
| The accumulator resetting inside the loop is explained | 2 |
| The proposed fix moves the initialisation instead of adding an `if` | 2 |
| It is explained that the `else` of a `for` depends on the `break` | 2 |

**Most common mistake**

Answering 73877 on the first line because «the loop adds up all five». It adds up all five and wipes the result four times.

### 09.2 · Apply

**Solution**

```python
campaigns = ["Instagram", "Meta", "Google", "TikTok", "Email", "Display"]
clicks = [5074, 3820, 6910, 1240, 2480, 7350]
spend = [38500, 29800, 51200, 9600, 12400, 61300]

total_spend = 0
with_volume = 0
any_expensive = False
best_cost = spend[0] / clicks[0]
best_campaign = campaigns[0]

for i in range(len(campaigns)):
    cost = spend[i] / clicks[i]
    total_spend += spend[i]

    if clicks[i] > 3000:
        with_volume += 1

    if cost > 8:
        any_expensive = True

    if cost < best_cost:
        best_cost = cost
        best_campaign = campaigns[i]

print(f"Total spend: ${total_spend:,}")
print(f"Campaigns above 3,000 clicks: {with_volume}")
print(f"Any above $8.00 per click? {any_expensive}")
print(f"Best cost per click: {best_campaign} with ${best_cost:,.2f}")
print(f"Overall cost per click: ${total_spend / sum(clicks):,.2f}")
```

The overall cost divides total spend by total clicks, so every campaign weighs according to what it spent. The average of the six individual costs gives the same weight to Display, which took 61,300 pesos, and to TikTok, which took 9,600. The committee gets the overall figure, because that is the one answering what a click really cost over the quarter.

**Output**

```text
Total spend: $202,800
Campaigns above 3,000 clicks: 4
Any above $8.00 per click? True
Best cost per click: Email with $5.00
Overall cost per click: $7.55
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| A single pass answers all five questions | 3 |
| The accumulator, the counter and the flag sit outside the loop | 2 |
| The best campaign is carried along with its name, not just its figure | 2 |
| The overall figure divides sum by sum | 2 |
| The explanation talks about weighting by spend, not about rounding | 1 |

**Most common mistake**

Initialising `best_cost = 0` and comparing with less than. No campaign goes below zero, so the best one stays Instagram, which is only the first in the list.

### 09.3 · Integrate

**Solution**

```python
branches = ["North", "Centre", "West"]
quarters = ["Q1", "Q2", "Q3", "Q4"]
sales = [412000, 388000, 455000, 501000,
         298000, 331000, 305000, 362000,
         214000, 240000, 268000, 291000]

print(f"{'Branch':<10}{'Q1':>10}{'Q2':>10}{'Q3':>10}{'Q4':>10}{'Total':>12}")

overall = 0
strong_quarters = 0

for i in range(len(branches)):
    line = f"{branches[i]:<10}"
    subtotal = 0

    for j in range(len(quarters)):
        sale = sales[i * len(quarters) + j]
        subtotal += sale
        line += f"{sale / 1000:>10,.0f}"

        if sale >= 400000:
            strong_quarters += 1

    overall += subtotal
    print(line + f"{subtotal / 1000:>12,.0f}")

print(f"{'Overall':<10}{'':>40}{overall / 1000:>12,.0f}")
print(f"Quarters above 400 thousand: {strong_quarters} of "
      f"{len(branches) * len(quarters)}")
```

**Output**

```text
Branch            Q1        Q2        Q3        Q4       Total
North            412       388       455       501       1,756
Centre           298       331       305       362       1,296
West             214       240       268       291       1,013
Overall                                                  4,065
Quarters above 400 thousand: 3 of 12
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The inner loop makes its four passes for every pass of the outer one | 2 |
| The index is worked out with `i * len(quarters) + j` | 3 |
| The subtotal resets per branch and the overall figure does not | 2 |
| The three row totals and the grand total are correct | 2 |
| The counter of strong quarters gives 3 of 12 | 1 |

**Most common mistake**

Declaring `subtotal = 0` above the outer loop. The rows come out carrying the previous branch: Centre reports 3,052 and West 4,065, and that last figure matches the grand total, which makes the error look correct.

---

## Week 10 · User-defined functions

### 10.1 · Recognise

**Solution**

```text
None
5400.0
```

After those two lines the program stops with `NameError: name 'base' is not defined`.

`commission` is missing its `return`: it works out the product and throws it away. Once fixed it would print 9000.0. The third line fails because `base` is born inside `bonus`, lives while the function runs and disappears when it finishes. And `result + 100` would raise `TypeError`, because an integer cannot be added to `None`.

**Output**

```text
None
5400.0
Traceback (most recent call last):
  File "returning.py", line 14, in <module>
    print(base)
          ^^^^
NameError: name 'base' is not defined. Did you mean: 'False'?
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| `None` and 5400.0 on the first two lines | 3 |
| `NameError` named, with the local scope explanation | 3 |
| It is stated that a fixed `commission` would return 9000.0 | 2 |
| `TypeError` identified for the addition with `None` | 2 |

**Most common mistake**

Answering 9000.0 on the first line because the function «does the multiplication». It does it, and without `return` it does not hand it over.

### 10.2 · Apply

**Solution**

```python
def break_even(fixed_costs, price, variable_cost):
    """Returns how many units have to be sold to neither lose nor gain."""
    margin = price - variable_cost

    return fixed_costs / margin


print(f"Coffee shop: {break_even(145000, 68.00, 23.00):,.2f} units")
print(f"Medical equipment: {break_even(980000, 1250.00, 845.00):,.2f} units")
print(f"Workshop: {break_even(60000, 40.00, 20.00):,.2f} units")
```

If the price and the variable cost were equal, the margin would come to zero and the function would raise `ZeroDivisionError`. For the business it means every unit sold leaves not a single peso towards the fixed costs, so no volume reaches break-even: the problem is not selling more, it is the price.

**Output**

```text
Coffee shop: 3,222.22 units
Medical equipment: 2,419.75 units
Workshop: 3,000.00 units
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The function returns and does not print | 3 |
| Docstring stating what it hands back | 2 |
| The three calls with their three correct results | 3 |
| `ZeroDivisionError` named and translated into business terms | 2 |

**Most common mistake**

Putting the `print` inside the function and calling it three times without storing anything. It looks identical on screen, and it leaves all three numbers out of reach of any later calculation.

### 10.3 · Integrate

**Solution**

```python
def turnover(leavers, headcount):
    """Returns the turnover index of the period as a proportion."""
    return leavers / headcount


def classify(index):
    """Returns the turnover band that the index belongs to."""
    if index >= 0.20:
        return "Critical"
    elif index >= 0.15:
        return "High"
    elif index >= 0.10:
        return "Normal"
    else:
        return "Low"


areas = ["Sales", "Operations", "Administration", "Logistics", "IT"]
leavers = [9, 21, 3, 14, 2]
headcount = [74, 112, 48, 96, 25]

print(f"{'Area':<16}{'Leavers':>7}{'Headcount':>11}{'Turnover':>10}  Band")

for i in range(len(areas)):
    index = turnover(leavers[i], headcount[i])
    print(f"{areas[i]:<16}{leavers[i]:>7}{headcount[i]:>11}"
          f"{index:>10.1%}  {classify(index)}")

company = turnover(sum(leavers), sum(headcount))
print(f"{'Company':<16}{sum(leavers):>7}{sum(headcount):>11}"
      f"{company:>10.1%}  {classify(company)}")
```

The company index is not the average of the five because each area contributes a different headcount. Operations weighs 112 people and IT weighs 25, so the overall index looks far more like Operations than like IT.

**Output**

```text
Area            Leavers  Headcount  Turnover  Band
Sales                 9         74     12.2%  Normal
Operations           21        112     18.8%  High
Administration        3         48      6.2%  Low
Logistics            14         96     14.6%  Normal
IT                    2         25      8.0%  Low
Company              49        355     13.8%  Normal
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| Both functions return, neither prints | 3 |
| The company line reuses the same two functions | 2 |
| The five bands correct | 2 |
| The table aligned with the percentage to one decimal | 2 |
| The explanation of the weighted average | 1 |

**Most common mistake**

Writing the classification out again inside the loop, with an `if` instead of calling `classify`. The table comes out right, and when the boundaries change there will be two places to fix and only one will get fixed.

---

## Week 11 · Arguments, built-in functions and modules

### 11.1 · Recognise

**Solution**

```text
13920.0
4212000
14270.0
23590 18400
```

On the second call, the 350 lands in the second parameter, which is `vat`. The function works out 12000 times 351 and returns 4,212,000 without flagging anything, because a VAT rate of 350 is a perfectly valid number. For it to mean the shipping it has to be named: `total_cost(12000, shipping=350)`.

The average sits above the median because the 42,300 salary drags the sum and leaves the middle value alone. A candidate gets told the median: it describes what half the area earns, not what the manager earns.

**Output**

```text
13920.0
4212000
14270.0
23590 18400
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The four lines correct | 4 |
| It is explained that the 350 landed in `vat` by position | 2 |
| The fix names the argument | 1 |
| The average against median explanation uses the high salary | 2 |
| The choice of the median is justified | 1 |

**Most common mistake**

Answering that the second line raises an error for passing the arguments wrongly. The call is valid, and that is exactly the problem.

### 11.2 · Apply

**Solution**

```python
def payroll_cost(base_salary, months=12, bonus=0.0, benefits=1.35):
    """Returns the annual cost of a role, benefits and bonus included."""
    return base_salary * months * benefits * (1 + bonus)


print(f"Standard role: ${payroll_cost(18400):,.2f}")
print(f"With a thirteenth month: ${payroll_cost(18400, 13):,.2f}")
print(f"With a 10 % bonus: ${payroll_cost(18400, bonus=0.10):,.2f}")
```

`payroll_cost(18400, 0.10)` hands back 2,484.00: the 0.10 lands in `months`, so it works out a tenth of one month. No error, just an annual cost of two thousand pesos that nobody will question on a sheet holding twenty roles.

**Output**

```text
Standard role: $298,080.00
With a thirteenth month: $322,920.00
With a 10 % bonus: $327,888.00
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The three optional parameters at the end and with their default value | 3 |
| The three calls, one of them by keyword skipping `months` | 3 |
| The three results correct | 2 |
| What happens with `payroll_cost(18400, 0.10)` is explained | 2 |

**Most common mistake**

Declaring the function as `payroll_cost(base_salary, bonus=0.0, months)`. Python rejects it while reading the file with `SyntaxError`, before running a single line.

### 11.3 · Integrate

**Solution**

```python
from statistics import mean, median


def summarise(label, value):
    """Returns the formatted line of one payroll metric."""
    return f"{label:<22}${value:>12,.2f}"


salaries = [12800, 15600, 17950, 18400, 19250, 22400, 26500, 33900, 84000]
ordered = sorted(salaries)

print(f"Roles in the area: {len(salaries)}")
print(summarise("Monthly payroll", sum(salaries)))
print(summarise("Average", mean(salaries)))
print(summarise("Median", median(salaries)))
print(summarise("Highest salary", max(salaries)))
print(summarise("Lowest salary", min(salaries)))
print(summarise("Second highest", ordered[-2]))
print(f"The average sits {mean(salaries) - median(salaries):,.2f} above "
      f"the median.")
```

The area director gets the monthly payroll, $250,800.00, because that is the figure that goes against the budget. The union gets the median, $19,250.00, because it describes what the middle role earns. Both are true and both come out of the same nine numbers: one measures what the area costs, the other what a typical person in that area earns.

**Output**

```text
Roles in the area: 9
Monthly payroll       $  250,800.00
Average               $   27,866.67
Median                $   19,250.00
Highest salary        $   84,000.00
Lowest salary         $   12,800.00
Second highest        $   33,900.00
The average sits 8,616.67 above the median.
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| `summarise` returns the string and does not print | 2 |
| The six metrics correct | 3 |
| The second highest comes from `sorted`, with the original list intact | 2 |
| The column widths respected | 1 |
| The three closing answers, with their justification | 2 |

**Most common mistake**

Reordering the original list instead of asking `sorted` for a copy. Everything else keeps working, so nobody notices until somebody needs the order the roles were captured in.

---

## Week 12 · Lists and tuples

### 12.1 · Recognise

**Solution**

```text
None
[125, 210, 340, 470, 890]
6
6 0
[210, 340, 470]
890
```

`sort` orders the list in place and returns `None`, which is why the first line prints nothing useful. `backup = units` does not copy: it creates a second name for the same list, so the `append` is visible from both. For the original to stay put it had to read `backup = units.copy()`.

**Output**

```text
None
[125, 210, 340, 470, 890]
6
6 0
[210, 340, 470]
890
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The six lines correct | 4 |
| It is explained that `sort` returns `None` and modifies in place | 2 |
| The alias is explained and `copy` is proposed | 2 |
| The slice excludes index 4 and the negative points at the second to last | 2 |

**Most common mistake**

Answering `[210, 340, 470, 890]` on the second to last line. The first index is included and the second is not, which is why a slice from 1 to 4 returns three items.

### 12.2 · Apply

**Solution**

```python
inventory = [340, 125, 890, 470, 210, 655, 890, 305, 148, 720, 415, 260]

print("At the start:", inventory)

ordered = inventory.copy()
ordered.sort()
ordered.reverse()

print("Three SKUs with the most pieces:", ordered[0:3])
print("Pieces in the inventory:", sum(inventory))
print("Position of the SKU with 720 pieces:", inventory.index(720))
print("How many times 890 appears:", inventory.count(890))
print("At the end:", inventory)
```

**Output**

```text
At the start: [340, 125, 890, 470, 210, 655, 890, 305, 148, 720, 415, 260]
Three SKUs with the most pieces: [890, 890, 720]
Pieces in the inventory: 5428
Position of the SKU with 720 pieces: 9
How many times 890 appears: 2
At the end: [340, 125, 890, 470, 210, 655, 890, 305, 148, 720, 415, 260]
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The first and the last line are identical | 3 |
| The sorting happens on a copy made with `copy` | 2 |
| The three highest figures include the repeated 890 | 2 |
| `index` and `count` used where they belong | 2 |
| Total pieces correct | 1 |

**Most common mistake**

Copying with `ordered = inventory`. Both inventory lines come out sorted and the student concludes the program works, because they never compare the first with the last.

### 12.3 · Integrate

**Solution**

```python
skus = ["PAP-100", "PAP-215", "OFI-330", "OFI-412",
        "LIM-501", "LIM-620", "TEC-710", "TEC-844"]
units = [1840, 5210, 960, 2375, 3120, 880, 1450, 640]
prices = [38.50, 9.90, 74.00, 22.50, 15.75, 96.20, 58.40, 210.00]

THRESHOLD = 70000
relevant = []

for i in range(len(skus)):
    amount = units[i] * prices[i]

    if amount >= THRESHOLD:
        relevant.append((amount, skus[i]))

relevant.sort()
relevant.reverse()

print(f"SKUs above ${THRESHOLD:,} of sales: {len(relevant)} of {len(skus)}")

for amount, sku in relevant:
    print(f"{sku:<10}{amount:>12,.2f}")

print("The original list still holds", len(skus), "keys and starts at", skus[0])
```

The tuple holds the amount first because the ordering of a list of tuples is decided by the first element. That is what lets the sorting happen on money without losing sight of which key every figure belongs to.

**Output**

```text
SKUs above $70,000 of sales: 5 of 8
TEC-844     134,400.00
TEC-710      84,680.00
LIM-620      84,656.00
OFI-330      71,040.00
PAP-100      70,840.00
The original list still holds 8 keys and starts at PAP-100
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The new list is filled with `append` inside the loop | 2 |
| The elements are tuples of amount and key | 2 |
| The descending order keeps the pairing intact | 2 |
| The five correct keys, with their amounts | 2 |
| The threshold lives in one variable and appears in the text | 2 |

**Most common mistake**

Keeping two parallel lists of amounts and keys, and sorting only the amounts. The amounts end up neatly ordered and the keys stay in capture order, so the table assigns every figure to the wrong SKU.

---

## Week 13 · Sets and dictionaries · Second midterm

### 13.1 · Recognise

**Solution**

```text
4
4
None
15
['Bravo', 'Sol']
['Nardo', 'Zafiro']
5
```

The dictionary measures 4 because `lead_days["Sol"] = 4` overwrote a key that already existed, and only `Nardo` added a new entry. Keys do not repeat.

`lead_days["Zafiro"]` would have raised `KeyError` and stopped the program right there. `get` returns `None`, or whatever default is passed to it.

The question of who invoiced in one month and not the other, regardless of which, is answered by the symmetric difference: `march ^ april`, which here would return `['Aurora', 'Nardo', 'Zafiro']`.

**Output**

```text
4
4
None
15
['Bravo', 'Sol']
['Nardo', 'Zafiro']
5
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The seven lines correct | 4 |
| The overwriting of the repeated key is explained | 2 |
| `KeyError` named as what `get` avoids | 2 |
| The symmetric difference identified, with its result | 2 |

**Most common mistake**

Answering 5 on the first line, counting the three initial entries plus the two assignments. One of the two was a key that already existed.

### 13.2 · Apply

**Solution**

```python
suppliers = ["Aurora", "Sol", "Bravo", "Nardo", "Zafiro", "Delta"]
days = [3, 4, 5, 9, 6, 12]

catalogue = {}

for i in range(len(suppliers)):
    catalogue[suppliers[i]] = days[i]

print(f"Suppliers in the catalogue: {len(catalogue)}")

for name, lead in catalogue.items():
    print(f"{name:<10}{lead:>4} days")

print("Average lead time:", sum(catalogue.values()) / len(catalogue), "days")
print("Lookup for Bravo:", catalogue.get("Bravo", 30), "days")
print("Lookup for Quintana:", catalogue.get("Quintana", 30), "days")
```

**Output**

```text
Suppliers in the catalogue: 6
Aurora       3 days
Sol          4 days
Bravo        5 days
Nardo        9 days
Zafiro       6 days
Delta       12 days
Average lead time: 6.5 days
Lookup for Bravo: 5 days
Lookup for Quintana: 30 days
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The dictionary is built with a loop from the two lists | 3 |
| The walk uses `items` and pulls key and value at once | 2 |
| The average comes from `values` | 2 |
| Both lookups use `get` with a default | 2 |
| The table stays aligned | 1 |

**Most common mistake**

Typing the dictionary out by hand with the six pairs. It gives the same output and stops being usable the moment the catalogue arrives with forty suppliers.

### 13.3 · Integrate

**Solution**

```python
def consolidate(names, amounts):
    """Returns the purchase total per supplier for a single month."""
    summary = {}

    for i in range(len(names)):
        summary[names[i]] = summary.get(names[i], 0) + amounts[i]

    return summary


def variation(before, after):
    """Returns the percentage change between two amounts."""
    return (after - before) / before


march_names = ["Aurora", "Sol", "Bravo", "Aurora", "Nardo", "Sol"]
march_amounts = [18400, 9375, 24680, 6120, 15302, 8100]
april_names = ["Sol", "Bravo", "Zafiro", "Bravo", "Aurora", "Zafiro"]
april_amounts = [11250, 19800, 7400, 5600, 22150, 9900]

march = consolidate(march_names, march_amounts)
april = consolidate(april_names, april_amounts)

print(f"March purchases: ${sum(march.values()):,}")
print(f"April purchases: ${sum(april.values()):,}")
print(f"Change in spend: {variation(sum(march.values()), sum(april.values())):.1%}")

new = set(april) - set(march)
lost = set(march) - set(april)
constant = set(march) & set(april)

print("New suppliers:", sorted(new))
print("Suppliers that stopped invoicing:", sorted(lost))

print("Movement of the ones present in both months:")

for name in sorted(constant):
    print(f"{name:<10}{march[name]:>10,}{april[name]:>10,}"
          f"{variation(march[name], april[name]):>9.1%}")
```

The heart of the accumulation is `summary.get(names[i], 0) + amounts[i]`: the first time a supplier appears there is no key, `get` returns zero and the sum starts with no special case.

**Output**

```text
March purchases: $81,977
April purchases: $76,100
Change in spend: -7.2%
New suppliers: ['Zafiro']
Suppliers that stopped invoicing: ['Nardo']
Movement of the ones present in both months:
Aurora        24,520    22,150    -9.7%
Bravo         24,680    25,400     2.9%
Sol           17,475    11,250   -35.6%
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| `consolidate` accumulates with `get` and returns the dictionary | 3 |
| The two totals and the overall change correct | 2 |
| New and lost suppliers come from set operations | 2 |
| The table of the three constant suppliers, with their changes | 2 |
| Both functions with a docstring and no `print` inside | 1 |

**Most common mistake**

Writing `summary[names[i]] = amounts[i]` without adding. Aurora ends up at 6,120 instead of 24,520 because the second invoice overwrites the first, and the March total drops to 54,202 with nothing pointing it out.

---

## Week 14 · Text and CSV files

### 14.1 · Recognise

**Solution**

```text
15
E-001 $18,400.00
<class 'str'>
True
Sales Executive
```

`len(rows)` gives 15 and not 16 because `DictReader` uses the first row as the header: it turns into the keys of every dictionary and stops counting as data.

Opening the file in mode `"w"` empties it the instant it opens, before a single line is read. The payroll would be gone and `DictReader` would find nothing.

`int(rows[4]["days_worked"])` raises `ValueError`, because an empty string represents no number at all. Turning the blank into a zero is a decision that has to be written by hand.

**Output**

```text
15
E-001 $18,400.00
<class 'str'>
True
Sales Executive
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The five lines correct | 4 |
| The header is explained as the reason for the 15 | 2 |
| The effect of mode `"w"` is stated using the word erase | 2 |
| `ValueError` named, and not `TypeError` or zero | 2 |

**Most common mistake**

Answering `<class 'int'>` on the third line because the column carries numbers. A text file hands back text, every time.

### 14.2 · Apply

**Solution**

```python
import csv
from pathlib import Path

DATA = Path(__file__).resolve().parent


def to_float(text):
    """Turns '$18,400.00' into the number 18400.0."""
    clean = text.replace("$", "").replace(",", "").strip()

    return float(clean)


def to_int(text, missing=0):
    """Turns text into an integer and decides what a blank cell is worth."""
    clean = text.strip()

    if clean == "":
        return missing

    return int(clean)


with (DATA / "march_payroll.csv").open(encoding="utf-8") as f:
    rows = list(csv.DictReader(f))

payroll = 0
days = 0
short = 0

for row in rows:
    payroll += to_float(row["monthly_salary"])
    worked = to_int(row["days_worked"])
    days += worked

    if worked < 30:
        short += 1

print(f"Employees in the file: {len(rows)}")
print(f"Monthly payroll: ${payroll:,.2f}")
print(f"Average salary: ${payroll / len(rows):,.2f}")
print(f"Days worked in total: {days}")
print(f"Records with fewer than 30 days: {short}")
```

The last line prints 4 because E-005, the one with the blank cell, came in as zero days and zero is fewer than thirty. The decision inside `to_int` is responsible: turning a blank into a zero turns «I do not know how many days they worked» into «they worked none». On this data E-005 shows up as the worst attendance case of the payroll when it is really the only one nothing is known about.

**Output**

```text
Employees in the file: 15
Monthly payroll: $320,550.00
Average salary: $21,370.00
Days worked in total: 411
Records with fewer than 30 days: 4
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| Both conversion functions, with a docstring | 3 |
| The symbol and the thousands comma are stripped before converting | 2 |
| The five lines with the right figures | 3 |
| E-005 is identified as the record counted in error | 2 |

**Most common mistake**

Adding up `row["monthly_salary"]` without converting. It raises no error: it glues fifteen strings one after another and the total comes out as an enormously long piece of text that looks like a huge number at a glance.

### 14.3 · Integrate

**Solution**

```python
import csv
from pathlib import Path

DATA = Path(__file__).resolve().parent


def to_float(text):
    """Turns '$18,400.00' into the number 18400.0."""
    return float(text.replace("$", "").replace(",", "").strip())


with (DATA / "march_payroll.csv").open(encoding="utf-8") as f:
    rows = list(csv.DictReader(f))

payroll_area = {}
roles_area = {}
without_days = []

for row in rows:
    area = row["area"]
    salary = to_float(row["monthly_salary"])

    payroll_area[area] = payroll_area.get(area, 0) + salary
    roles_area[area] = roles_area.get(area, 0) + 1

    if row["days_worked"].strip() == "":
        without_days.append(row["id"])

with (DATA / "area_summary.csv").open("w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["area", "roles", "payroll", "average_salary"])

    for area in sorted(payroll_area):
        writer.writerow([area, roles_area[area],
                         round(payroll_area[area], 2),
                         round(payroll_area[area] / roles_area[area], 2)])

print(f"{'Area':<16}{'Roles':>8}{'Payroll':>14}{'Average':>13}")

for area in sorted(payroll_area):
    print(f"{area:<16}{roles_area[area]:>8}{payroll_area[area]:>14,.2f}"
          f"{payroll_area[area] / roles_area[area]:>13,.2f}")

print(f"Ids with no days worked: {without_days}")
print("File written: area_summary.csv")
```

The three defensible decisions about the blank cell of E-005 are these. Treating it as zero days, which is what the program does and what leaves the employee looking like the worst attender of the month. Discarding the whole row, which drops the reported payroll of Operations to $68,800.00 and its roles to 4. Or leaving it marked as missing and reporting the average days over the fourteen records that do carry it. For the summary by area none of the three changes the payroll or the number of roles, because the salary of E-005 is complete: what changes is any figure worked out from the days.

**Output**

```text
Area               Roles       Payroll      Average
Administration         4    106,300.00    26,575.00
Operations             5     81,600.00    16,320.00
Sales                  6    132,650.00    22,108.33
Ids with no days worked: ['E-005']
File written: area_summary.csv
```

The file `area_summary.csv` comes out like this:

```text
area,roles,payroll,average_salary
Administration,4,106300.0,26575.0
Operations,5,81600.0,16320.0
Sales,6,132650.0,22108.33
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| Both dictionaries accumulate in a single pass | 3 |
| The table on screen, sorted and aligned | 2 |
| The output file is written with a header and `newline=""` | 3 |
| The ids with no days are reported | 1 |
| The three alternative decisions are stated with their effect | 1 |

**Most common mistake**

Opening the output file without `newline=""`. On Windows the CSV comes out with a blank line between every record, and opening it in the spreadsheet makes it look as though the program wrote twice as many rows.

---

## Week 15 · Series, DataFrame, cleaning, grouping and joining

### 15.1 · Recognise

**Solution**

```text
(22, 5)
date              str
region            str
channel           str
units         float64
unit_price        str
dtype: object
2
2
8
[' North ', 'Centre', 'NORTH', 'North', 'South', 'West', 'centre', 'west']
```

`units` came out `float64` because two cells are empty, and the marker for empty only exists in a decimal column. `unit_price` came out as text because the peso sign and the thousands comma are format, not value, and no column carrying those characters can be read as a number.

There are four real regions: North, Centre, West and South. A `groupby` run right now would report eight, and would split the North figures across four separate piles.

Total pieces can already be worked out, because `units` is numeric and the sum ignores the blanks. The total in money cannot, because the price is still text.

**Output**

```text
(22, 5)
date              str
region            str
channel           str
units         float64
unit_price        str
dtype: object
2
2
8
[' North ', 'Centre', 'NORTH', 'North', 'South', 'West', 'centre', 'west']
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| Shape, types and the three counts correct | 4 |
| The `float64` explanation mentions the empty cells | 2 |
| The price explanation mentions the symbol and the comma | 2 |
| The 4 real regions are told apart from the 8 the file reports | 2 |

**Most common mistake**

Explaining the `float64` by saying the unit counts carry decimals. Every one of them in the file is a whole number: what forces the decimal is the hole, not the data.

### 15.2 · Apply

**Solution**

```python
import pandas as pd
from pathlib import Path

DATA = Path(__file__).resolve().parent

sales = pd.read_csv(DATA / "sales_2026.csv")

print(f"Raw: {len(sales)} rows, "
      f"{sales['region'].nunique()} regions, "
      f"{sales.duplicated().sum()} duplicates, "
      f"{sales['units'].isna().sum()} blank unit counts")

sales = sales.drop_duplicates()
print(f"Without duplicates: {len(sales)} rows")

sales["region"] = sales["region"].str.strip().str.title()
print(f"Region normalised: {sorted(sales['region'].unique())}")

sales["unit_price"] = (sales["unit_price"]
                       .str.replace("$", "", regex=False)
                       .str.replace(",", "", regex=False)
                       .str.strip()
                       .astype(float))
sales["date"] = pd.to_datetime(sales["date"])

sales["amount"] = sales["units"] * sales["unit_price"]
print(f"Amount with the holes still in: ${sales['amount'].sum():,.2f}")

sales = sales.dropna(subset=["units"])
sales["units"] = sales["units"].astype(int)

print(f"Clean: {len(sales)} rows, "
      f"{sales['units'].sum():,} pieces, "
      f"${sales['amount'].sum():,.2f} of revenue")
print(f"Average sale: ${sales['amount'].mean():,.2f}")
print(sales.dtypes)
```

Dropping the rows with blank unit counts did not move the total because the amount on those two rows was already blank: units times price, with the units missing, does not produce zero, it produces absence, and the sum ignores it. The average sale did not move either, for the same reason: `mean` divides by the 18 values that do exist, not by the 20 rows. What did change is the number of rows in the table, and with it the possibility of converting `units` to an integer. And it would change any figure worked out by dividing by `len(sales)` instead of letting pandas do the counting.

**Output**

```text
Raw: 22 rows, 8 regions, 2 duplicates, 2 blank unit counts
Without duplicates: 20 rows
Region normalised: ['Centre', 'North', 'South', 'West']
Amount with the holes still in: $2,301,950.00
Clean: 18 rows, 1,855 pieces, $2,301,950.00 of revenue
Average sale: $127,886.11
date          datetime64[us]
region                   str
channel                  str
units                  int64
unit_price           float64
amount               float64
dtype: object
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The duplicates go before anything is grouped or added up | 2 |
| The region is normalised with `strip` and `title`, and four are left | 2 |
| The price is converted with `regex=False` and `astype` | 2 |
| The log prints one line per step | 2 |
| The explanation of the total that did not move is correct | 2 |

**Most common mistake**

Applying `str.title()` without `str.strip()` first. `" North "` turns into `" North "` with the same capitalisation and still counts as a separate region, so the count drops from eight to five and looks solved.

### 15.3 · Integrate

**Solution**

```python
import pandas as pd
from pathlib import Path

DATA = Path(__file__).resolve().parent

sales = pd.read_csv(DATA / "sales_2026.csv").drop_duplicates()
sales["region"] = sales["region"].str.strip().str.title()
sales["unit_price"] = (sales["unit_price"]
                       .str.replace("$", "", regex=False)
                       .str.replace(",", "", regex=False)
                       .astype(float))
sales = sales.dropna(subset=["units"])
sales["units"] = sales["units"].astype(int)
sales["amount"] = sales["units"] * sales["unit_price"]

summary = sales.groupby("region").agg(
    revenue=("amount", "sum"),
    pieces=("units", "sum"),
    deals=("amount", "count"),
    average=("amount", "mean"),
).round(2).sort_values("revenue", ascending=False)

print(summary)
print()

grid = sales.pivot_table(index="region", columns="channel",
                         values="amount", aggfunc="sum",
                         margins=True, margins_name="Total")
print((grid / 1000).round(1))
print()

catalogue = pd.DataFrame({
    "region": ["North", "Centre", "West", "South", "Gulf"],
    "manager": ["Lucía Ramos", "Iván Peña", "Marta Ocampo",
                "Diego Salas", "Rocío Trejo"],
    "target": [900000, 700000, 650000, 250000, 200000],
})

audit = summary.reset_index().merge(catalogue, on="region",
                                    how="outer", indicator=True)
print(audit["_merge"].value_counts())
print(sorted(audit.loc[audit["_merge"] == "right_only", "region"]))
print()

board = summary.reset_index().merge(catalogue, on="region", how="left")
board["attainment"] = board["revenue"] / board["target"]
print(board[["region", "manager", "revenue", "target", "attainment"]]
      .to_string(index=False,
                 formatters={"revenue": "{:,.2f}".format,
                             "target": "{:,.0f}".format,
                             "attainment": "{:.1%}".format}))
```

The empty cell in the grid is South in Online. The only sale in that combination was the one on 18 June, which arrived with blank units and was discarded while cleaning: the combination exists in the commercial catalogue and has no complete deal in the year.

The audit flags Gulf as `right_only`: it is in the territory catalogue and invoiced nothing in 2026. That is not a data error, it is an open territory that sold nothing, and the fact that it shows up is exactly what has to be reported. With `inner` it would have vanished in silence and the dashboard would look complete with four regions, with nobody asking about the fifth.

**Output**

```text
         revenue  pieces  deals   average
region                                   
North   954450.0     765      7  136350.0
Centre  610350.0     490      5  122070.0
West    568900.0     465      4  142225.0
South   168250.0     135      2   84125.0

channel  Online  Retail  Wholesale   Total
region                                    
Centre    112.5   158.7      339.2   610.4
North     368.8    82.8      502.9   954.4
South       NaN    55.2      113.0   168.2
West      106.2    75.9      386.8   568.9
Total     587.5   372.6     1341.8  2302.0

_merge
both          4
right_only    1
left_only     0
Name: count, dtype: int64
['Gulf']

region      manager    revenue  target attainment
 North  Lucía Ramos 954,450.00 900,000     106.0%
Centre    Iván Peña 610,350.00 700,000      87.2%
  West Marta Ocampo 568,900.00 650,000      87.5%
 South  Diego Salas 168,250.00 250,000      67.3%
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The `agg` produces the four columns under the names asked for | 2 |
| The grid sums instead of averaging and carries its totals | 2 |
| The audit reports the three counts before joining | 2 |
| The final join uses left mode and works out attainment | 2 |
| The empty cell and the Gulf case are explained | 2 |

**Most common mistake**

Calling `pivot_table` without `aggfunc`. It returns averages, the grid looks reasonable and its rows no longer add up to the year's revenue, which is the check almost nobody runs.

---

## Week 16 · Visualisation, matplotlib and seaborn

### 16.1 · Recognise

**Solution**

`sns.barplot` averages by default, so that call draws the average sale, not the revenue: North 136,350.00, Centre 122,070.00, West 142,225.00 and South 84,125.00.

The ranking on that chart runs West, North, Centre, South. The one on total revenue runs North, Centre, West, South. The top two positions swap over, and anybody looking at the chart without reading the axis will conclude West is the most important region of the year.

For it to draw the total it needs `estimator="sum"`, and `errorbar=None` is worth adding so it does not lay a confidence interval over every bar.

A title that carries both readings: «North sells more often, West sells bigger on every deal».

| Line | What is wrong |
|---|---|
| `ax.set_ylim(500000, 1000000)` | It cuts the axis: South disappears from the chart and the gap between North and Centre looks twice as large as it is |
| `ax.plot(...)` over regions | A line claims there is a path between North and Centre, and between categories no such path exists |
| `ax.pie(...)` | With four slices it already forces the reader to compare angles, which is exactly what people get wrong; on sorted bars the answer reads itself |

**Output**

What gets handed in is the four averages, the two rankings, the fix to the call and the table of the three decisions.

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The four averages identified as what the bar draws | 3 |
| The two rankings written out and compared | 2 |
| `estimator="sum"` proposed, with `errorbar=None` | 2 |
| The three chart decisions explained | 3 |

**Most common mistake**

Answering that the bar draws the revenue because «that is the column it was handed». It is handed the column, and what it draws depends on the estimator, which nobody wrote.

### 16.2 · Apply

**Solution**

```python
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import pandas as pd

MONTHS = ["jan", "feb", "mar", "apr", "may", "jun",
          "jul", "aug", "sep", "oct", "nov", "dec"]

revenue = pd.Series(
    [1284000, 962000, 1431000, 1189000, 1516000, 1340000,
     1208000, 1377000, 1465000, 1623000, 2048000, 3412000],
    index=MONTHS,
)

annual = revenue.sum()
last_quarter = revenue[["oct", "nov", "dec"]].sum() / annual
december_share = revenue["dec"] / annual

fig, ax = plt.subplots(figsize=(10, 5))

bars = ax.bar(MONTHS, revenue.values, color="#C7D6E8")

for month in ["oct", "nov", "dec"]:
    bars[MONTHS.index(month)].set_color("#2B5F8F")

ax.set_title(f"The last quarter carried {last_quarter:.0%} "
             f"of the year's revenue")
ax.set_ylabel("Monthly revenue (millions of pesos)")
ax.set_ylim(0, 3_600_000)
ax.yaxis.set_major_formatter(
    ticker.FuncFormatter(lambda v, _: f"{v / 1_000_000:.1f}M"))
fig.text(0.01, 0.01, "Source: monthly close 2026, Comercializadora Aurora. "
                     "12 months invoiced.", fontsize=8, color="#555555")

fig.savefig("seasonality_2026.png", dpi=150, bbox_inches="tight")
plt.close(fig)

print(f"Revenue for the year: ${annual:,.0f}")
print(f"Weight of the last quarter: {last_quarter:.1%}")
print(f"Weight of December alone: {december_share:.1%}")
print(f"Lowest month: {revenue.idxmin()} with ${revenue.min():,.0f}")
print("Chart saved to seasonality_2026.png")
```

The title reads «The last quarter carried 38% of the year's revenue» because the title format rounds to zero decimals what the output prints as 37.6%. It is the same figure out of the same calculation: nobody typed it in, and if a month changes the title changes on its own.

**Output**

```text
Revenue for the year: $18,855,000
Weight of the last quarter: 37.6%
Weight of December alone: 18.1%
Lowest month: feb with $962,000
Chart saved to seasonality_2026.png
```

The image comes out with twelve bars, the three of the last quarter in strong blue, the vertical axis running from 0.0M to 3.5M and the source in the bottom left corner.

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The three bars of the last quarter highlighted, the other nine not | 2 |
| The title carries the finding and its figure comes from the calculation | 2 |
| Vertical axis from zero, labelled and carrying its unit | 2 |
| The formatter leaves the ticks reading as 1.5M | 2 |
| Source at the foot and the figure closed at the end | 2 |

**Most common mistake**

Typing the 38 % into the title by hand. It looks identical today and it is left lying the day somebody adds a month or corrects a figure.

### 16.3 · Integrate

**Solution**

```python
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pathlib import Path

DATA = Path(__file__).resolve().parent

sns.set_theme(style="whitegrid", palette="deep")

payroll = pd.read_csv(DATA / "march_payroll.csv")
payroll["monthly_salary"] = (payroll["monthly_salary"]
                             .str.replace("$", "", regex=False)
                             .str.replace(",", "", regex=False)
                             .astype(float))

order = (payroll.groupby("area")["monthly_salary"]
         .median()
         .sort_values(ascending=False).index)

fig, ax = plt.subplots(figsize=(9, 5))
sns.boxplot(data=payroll, x="area", y="monthly_salary", order=order,
            hue="area", legend=False, ax=ax)
ax.set_title("Sales spreads salaries more unevenly than Operations")
ax.set_xlabel("")
ax.set_ylabel("Monthly salary (pesos)")
ax.set_ylim(0, 46000)
fig.text(0.01, 0.01, "Source: March 2026 payroll, 15 roles.",
         fontsize=8, color="#555555")
fig.savefig("salaries_by_area.png", dpi=150, bbox_inches="tight")
plt.close(fig)

print(payroll.groupby("area")["monthly_salary"]
      .agg(["count", "median", "mean", "max"]).round(2))

sales = pd.read_csv(DATA / "sales_2026.csv").drop_duplicates()
sales["region"] = sales["region"].str.strip().str.title()
sales["unit_price"] = (sales["unit_price"]
                       .str.replace("$", "", regex=False)
                       .str.replace(",", "", regex=False)
                       .astype(float))
sales = sales.dropna(subset=["units"])
sales["amount"] = sales["units"] * sales["unit_price"]

grid = sales.pivot_table(index="region", columns="channel",
                         values="amount", aggfunc="sum") / 1000

fig, ax = plt.subplots(figsize=(7, 4))
sns.heatmap(grid, annot=True, fmt=".0f", cmap="Blues", ax=ax)
ax.set_title("Wholesale carries the revenue in all four regions")
ax.set_xlabel("")
ax.set_ylabel("")
fig.text(0.01, 0.01, "Source: 2026 sales, 18 clean deals. "
                     "Figures in thousands of pesos.", fontsize=8,
         color="#555555")
fig.savefig("region_channel_grid.png", dpi=150, bbox_inches="tight")
plt.close(fig)

print()
print(grid.round(1))
print("Charts saved: salaries_by_area.png, region_channel_grid.png")
```

Alt text for the box plot: box plot of the monthly salary of fifteen roles, spread across three areas and sorted by median. Administration has the highest median, 25,350 pesos, and the tightest spread, between 21,700 and 33,900. Sales has a median of 18,225 and reaches 42,300, so its box is the longest and shows the widest internal inequality of any area.

Alt text for the heatmap: heatmap of four regions against three channels, with the year's revenue in thousands of pesos written in every cell. The strongest cell is North in Wholesale, at 503 thousand pesos. Wholesale is the most loaded column in all four regions and South in Online comes out blank, because its only sale was discarded while cleaning.

**Output**

```text
                count   median      mean      max
area                                             
Administration      4  25350.0  26575.00  33900.0
Operations          5  13900.0  16320.00  26500.0
Sales               6  18225.0  22108.33  42300.0

channel  Online  Retail  Wholesale
region                            
Centre    112.5   158.7      339.2
North     368.8    82.8      502.9
South       NaN    55.2      113.0
West      106.2    75.9      386.8
Charts saved: salaries_by_area.png, region_channel_grid.png
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The seaborn theme is set once, at the top | 1 |
| The box plot areas are sorted by median | 2 |
| The box plot title states a finding checkable against the table | 2 |
| The heatmap takes the grid straight in, with the values written | 2 |
| Both alt texts, with every figure checkable | 3 |

**Most common mistake**

Writing the alt text from memory, with sentences like «salaries go up across every area». The giveaway is that not one figure in the description appears in the table the same program printed three lines earlier.

---

## Week 17 · Review and final exam

### 17.1 · Recognise

**Solution**

```text
8
10
175.0
None
```

| Line | Error | What it prints | What was wanted | How it is fixed |
|---|---|---|---|---|
| `groupby("region")` without cleaning | Grouping before cleaning | 8 regions | 4 regions | Normalise with `str.strip().str.title()` and drop duplicates before grouping |
| `sales[...]["channel"] = "Wholesale"` | Chained assignment | 10 rows in Wholesale | 12, if the write had worked | `sales.loc[sales["region"] == "North", "channel"] = "Wholesale"` |
| `total = 0` inside the `for` | Accumulator declared inside | 175.0, the last row | 1,855, the sum of the units | Move `total = 0` above the loop |
| `order = order.sort()` | Confusing changing with returning | `None` | The sorted list | `order = sorted(order)`, or call `order.sort()` without assigning |

The warning the second line leaves behind is this:

```text
ChainedAssignmentError: A value is being set on a copy of a DataFrame or Series
through chained assignment.
Such chained assignment never works to update the original DataFrame or Series,
because the intermediate object on which we are setting values always behaves as
a copy (due to Copy-on-Write).

Try using '.loc[row_indexer, col_indexer] = value' instead, to perform the
assignment in a single step.
```

A warning does not stop the program: execution carries on, the four figures print and the file finishes cleanly. That is what makes it more dangerous than an error. An error forces a fix before submission; a warning gets lost in the output and the wrong result arrives at the committee wearing the face of a result.

**Output**

```text
8
10
175.0
None
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The four output lines correct | 3 |
| The four errors named in the vocabulary of the course | 3 |
| The four fixes are the ones from the course, not workarounds | 2 |
| The distinction between a warning and an error is argued | 2 |

**Most common mistake**

Answering 12 on the second line, assuming the chained assignment did write. The giveaway is a student who never noticed the warning, which was printed directly above their own answer.

### 17.2 · Apply

**Solution**

```python
import pandas as pd
from pathlib import Path

DATA = Path(__file__).resolve().parent

sales = pd.read_csv(DATA / "sales_2026.csv")
print(f"On loading: {sales.shape[0]} rows, "
      f"{sales['region'].nunique()} regions, "
      f"{sales.duplicated().sum()} duplicates, "
      f"{sales['units'].isna().sum()} blank unit counts")

sales = sales.drop_duplicates()
sales["region"] = sales["region"].str.strip().str.title()
sales["unit_price"] = (sales["unit_price"]
                       .str.replace("$", "", regex=False)
                       .str.replace(",", "", regex=False)
                       .astype(float))
sales = sales.dropna(subset=["units"])
sales["units"] = sales["units"].astype(int)
sales["amount"] = sales["units"] * sales["unit_price"]

print(f"Once clean: {sales.shape[0]} rows, "
      f"{sales['region'].nunique()} regions, "
      f"${sales['amount'].sum():,.2f} of revenue")

crossing = (sales.groupby(["region", "channel"])
            .agg(revenue=("amount", "sum"), deals=("amount", "count"))
            .sort_values("revenue", ascending=False))

print(crossing.head(4).round(2))

leader = crossing.index[0]
leader_revenue = crossing.iloc[0]["revenue"]
share = leader_revenue / sales["amount"].sum()

print(f"Attend to {leader[0]} in {leader[1]} first: "
      f"${leader_revenue:,.2f}, {share:.1%} of the year's revenue.")
```

**Output**

```text
On loading: 22 rows, 8 regions, 2 duplicates, 2 blank unit counts
Once clean: 18 rows, 4 regions, $2,301,950.00 of revenue
                   revenue  deals
region channel                   
North  Wholesale  502900.0      3
West   Wholesale  386750.0      2
North  Online     368750.0      3
Centre Wholesale  339150.0      2
Attend to North in Wholesale first: $502,900.00, 21.8% of the year's revenue.
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The diagnosis prints before anything is touched | 2 |
| The cleaning covers duplicates, region, price and holes | 3 |
| The crossing groups by both columns and sorts by revenue | 2 |
| The conclusion is one sentence with two checkable figures | 2 |
| The percentage divides by the year's revenue once clean | 1 |

**Most common mistake**

Dividing the share by the region's revenue instead of the year's. It gives 52.7 % instead of 21.8 %, and the resulting sentence claims something the table does not say.

### 17.3 · Integrate

**Solution**

```python
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import pandas as pd
from pathlib import Path

DATA = Path(__file__).resolve().parent


def load_clean(path):
    """Loads the sales file and returns the table ready to analyse."""
    data = pd.read_csv(path).drop_duplicates()
    data["region"] = data["region"].str.strip().str.title()
    data["unit_price"] = (data["unit_price"]
                          .str.replace("$", "", regex=False)
                          .str.replace(",", "", regex=False)
                          .astype(float))
    data["date"] = pd.to_datetime(data["date"])
    data = data.dropna(subset=["units"])
    data["units"] = data["units"].astype(int)
    data["amount"] = data["units"] * data["unit_price"]

    return data


def board(sales, catalogue):
    """Returns attainment against target by region, highest first."""
    summary = sales.groupby("region").agg(
        revenue=("amount", "sum"),
        deals=("amount", "count"),
        average=("amount", "mean"),
    ).reset_index()

    joined = summary.merge(catalogue, on="region", how="left")
    joined["attainment"] = joined["revenue"] / joined["target"]

    return joined.sort_values("attainment", ascending=False)


catalogue = pd.DataFrame({
    "region": ["North", "Centre", "West", "South", "Gulf"],
    "manager": ["Lucía Ramos", "Iván Peña", "Marta Ocampo",
                "Diego Salas", "Rocío Trejo"],
    "target": [900000, 700000, 650000, 250000, 200000],
})

sales = load_clean(DATA / "sales_2026.csv")

audit = (sales.groupby("region")["amount"].sum().reset_index()
         .merge(catalogue, on="region", how="outer", indicator=True))
counts = audit["_merge"].value_counts()

print("Audit of the join")
print(f"  Matching on both sides: {counts.get('both', 0)}")
print(f"  Catalogue only: {counts.get('right_only', 0)} "
      f"{sorted(audit.loc[audit['_merge'] == 'right_only', 'region'])}")
print(f"  Sales only: {counts.get('left_only', 0)}")
print()

report = board(sales, catalogue)
print(report[["region", "manager", "revenue", "deals", "average",
              "target", "attainment"]]
      .to_string(index=False,
                 formatters={"revenue": "{:,.2f}".format,
                             "average": "{:,.2f}".format,
                             "target": "{:,.0f}".format,
                             "attainment": "{:.1%}".format}))
print()

by_month = sales.groupby(sales["date"].dt.month)["amount"].sum()
print(f"Months with activity: {len(by_month)}")
print(f"Strongest month: {by_month.idxmax()} with ${by_month.max():,.2f}")
print(f"Weight of the strongest month: {by_month.max() / by_month.sum():.1%}")

fig, ax = plt.subplots(figsize=(9, 5))
order = report.sort_values("revenue", ascending=False)
bars = ax.bar(order["region"], order["revenue"], color="#C7D6E8")
bars[0].set_color("#2B5F8F")
ax.set_title(f"{order.iloc[0]['region']} brings in "
             f"{order.iloc[0]['revenue'] / sales['amount'].sum():.0%} "
             f"of the year's revenue")
ax.set_ylabel("2026 revenue (millions of pesos)")
ax.set_ylim(0, 1_100_000)
ax.yaxis.set_major_formatter(
    ticker.FuncFormatter(lambda v, _: f"{v / 1_000_000:.1f}M"))
fig.text(0.01, 0.01, "Source: sales_2026.csv, 18 of 22 rows "
                     "after cleaning.", fontsize=8, color="#555555")
fig.savefig("year_end_2026.png", dpi=150, bbox_inches="tight")
plt.close(fig)

print("Chart saved to year_end_2026.png")
```

Closing report, marked alongside the code:

The question was which region is worth attending to first in 2027 and how close each one landed to its target. The file arrived with 22 rows, two of them exact duplicates and two with blank unit counts. The duplicates went because they repeated date, region, channel, units and price: counting them would have inflated the revenue of North and of West by one deal each. The two rows with no units were discarded rather than filled with zero, because the amount on those rows could no longer be worked out and putting a zero there would have dragged down the average sale of their regions with a sale that did happen. That left 18 deals and four regions, after normalising eight ways of capturing the same name.

The finding is that North closed at 106.0 % of its target with 954,450 pesos, and it is the only region above a hundred. West landed at 87.5 % with 568,900 pesos and Centre at 87.2 % with 610,350: West sells less and gets further, because its target is 50,000 pesos lower. South landed at 67.3 % on only two deals in the year. The join audit flagged Gulf on the catalogue side, without a single sale in 2026.

The recommendation for 2027 is to review the target for South before reviewing its operation: two deals in twelve months is not a closing problem, it is a territory with no commercial activity. And to ask for an explanation on Gulf, which has a manager and a target assigned and invoiced nothing, before it goes into the budget again.

**Output**

```text
Audit of the join
  Matching on both sides: 4
  Catalogue only: 1 ['Gulf']
  Sales only: 0

region      manager    revenue  deals    average  target attainment
 North  Lucía Ramos 954,450.00      7 136,350.00 900,000     106.0%
  West Marta Ocampo 568,900.00      4 142,225.00 650,000      87.5%
Centre    Iván Peña 610,350.00      5 122,070.00 700,000      87.2%
 South  Diego Salas 168,250.00      2  84,125.00 250,000      67.3%

Months with activity: 10
Strongest month: 10 with $303,800.00
Weight of the strongest month: 13.2%
Chart saved to year_end_2026.png
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| Both functions with a docstring, with no formulas repeated outside them | 2 |
| The join audit reports both directions before the dashboard | 2 |
| The dashboard carries the seven columns and the ordering by attainment | 2 |
| The chart carries a calculated title, an axis from zero and the source at the foot | 2 |
| The report justifies every cleaning decision with its effect | 2 |

**Most common mistake**

Joining with `how="inner"` instead of auditing. Gulf disappears without a trace and the dashboard looks complete with four regions, so nobody asks about the territory that has a manager assigned and sold nothing.
