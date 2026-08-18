# Exercises · Data Analysis · TIA502

This booklet runs alongside the seventeen weeks of the course, and everything in it is solved with what has already been covered in class, never with what comes later. Each week carries three exercises: the first is read and predicted without running anything, the second is written against a specification that already states its data and its expected result, and the third ties the week's topic to the ones before it. Difficulty climbs in two directions, inside each week and across the term, so the recognise exercise of week 12 asks for more than the integrate exercise of week 4. Submit one `.py` file per exercise on Blackboard, together with the output exactly as your program produced it, except where the statement asks for paper.

---

## Week 01 · Course introduction and the bridge from Excel to Python

### 01.1 · Recognise

**Indices of a sales column**

Comercializadora Aurora has the first half of the year captured in two paired lists. Without running anything, write the four lines the program prints.

```python
months = ["jan", "feb", "mar", "apr", "may", "jun"]
sales = [128400, 96750, 143200, 118900, 151600, 134050]

print(months[0], sales[0])
print(months[-1], sales[-1])
print(sales[4] - sales[1])
print(len(sales))
```

Answer two more things, one line each. If that data lived in a spreadsheet with the header in row 1, which row does `sales[3]` correspond to? What happens if you add `print(months[6])` at the end?

### 01.2 · Apply

**Summary of a half year**

With the two lists from the previous exercise, write a program that prints four lines:

1. Sales for the half year, with a thousands separator and no decimals.
2. The monthly average, with a thousands separator and two decimals.
3. The best month and its figure, on a single line.
4. How far the best month sits above the average, with two decimals.

Sales for the half year come to 772,900 and the monthly average to 128,816.67. If those two figures do not match, check before going any further. Use `sum`, `len`, `max` and `index`, and no loops.

### 01.3 · Integrate

**The product that carries the month**

The stationery shop closed March with four product keys, captured in three lists that line up by position:

```python
products = ["Professional notebook", "Black ballpoint pen",
            "Ring binder", "Permanent marker"]
units = [1840, 5210, 960, 2375]
prices = [38.50, 9.90, 74.00, 22.50]
```

Write a program that finds the product with the most pieces sold and reports five things: the product name, its pieces, the amount it brought in (pieces times price), what percentage of the month's pieces that represents, with one decimal and the symbol written beside it, and the total pieces for the month.

The leading product moves 5,210 pieces and its share is 50.2 %. No writing index 1 by hand: the position has to come out of the data, so the program still works when a different month puts a different product on top.

---

## Week 02 · Algorithm design

The three exercises this week are handed in on paper. No computer, and no syntax from any language.

### 02.1 · Recognise

**Trace of a discount policy**

Corporate purchasing authorises a customer's discount with this algorithm:

```text
START
    READ annual_purchases, months_as_customer, overdue_balance

    IF overdue_balance > 0 THEN
        discount = 0
    ELSE IF annual_purchases >= 500000 AND months_as_customer >= 24 THEN
        discount = 0.12
    ELSE IF annual_purchases >= 200000 THEN
        discount = 0.06
    ELSE
        discount = 0.02

    WRITE discount
END
```

Fill in a trace table for these three customers, stating which conditions get evaluated, which one holds and what discount comes out:

| Customer | annual_purchases | months_as_customer | overdue_balance |
|---|---|---|---|
| Abarrotes La Paz | 620,000 | 36 | 0 |
| Ferretería Muñoz | 780,000 | 30 | 4,500 |
| Papelera Bruno | 200,000 | 8 | 0 |

Then answer which of the five properties of an algorithm would break if the third line read «IF the customer is important THEN discount = 0.12», and explain in two lines why.

### 02.2 · Apply

**Pseudocode for the quarterly bonus**

Human resources pays a quarterly bonus under these rules, which today live in an email:

- Anyone with less than six months of tenure gets no bonus.
- With six months or more and a rating of 4.5 or above, the bonus is 15 % of the monthly salary.
- With six months or more and a rating between 3.5 and 4.49, the bonus is 8 %.
- With six months or more and a rating below 3.5, the bonus is a flat 1,200 pesos.
- Anyone with more than three absences in the quarter has whatever they earned cut in half, no matter which branch they came in through.

Write the complete pseudocode, with `START`, `READ`, its decisions and `WRITE`. Then draw the flowchart with the four symbols, and label both exits of every diamond.

Test your algorithm on Marina Cortés: a salary of 24,500, eight months of tenure, a rating of 4.6 and four absences. Her bonus is 1,837.50.

### 02.3 · Integrate

**Breaking down the payroll close**

The fortnightly close is today a one-sentence process: «work out what each person gets paid». Split it into three subproblems that can be solved separately, name them, and say what each one takes in and what it hands back.

Pick one of the three and write it as pseudocode with at least two decisions. Then add an edge case your first version did not cover, say what wrong result it produced, and how you fixed it.

What you hand in has to survive the swap test: give it to a classmate along with your input data and compare results. If they differ, something was ambiguous and you have to point at where.

---

## Week 03 · Paradigms and an introduction to programming

### 03.1 · Recognise

**The budget that overwrites itself**

Marketing adjusted its annual budget four times in the same file. Predict what it prints.

```python
budget = 250000
budget = budget - 40000
budget = budget * 2
budget = budget + 15000

print(budget)
```

Then build a three-row table. For each of these lines, say what kind of error Python raises and on which line it reports it:

```python
Print(budget)
print("Budget: , budget)
print(budget
```

### 03.2 · Apply

**First payroll program**

Write a complete program, with its header comment and its import at the top, working on the six salaries of the sales area:

```python
salaries = [23200, 42800, 82700, 24500, 31600, 28900]
```

It has to print three labelled lines: how many employees there are, the average salary and the highest salary. The average is calculated with `mean`, from the `statistics` module, not by dividing by hand. The average comes to 38950.

### 03.3 · Integrate

**Repairing the cash close**

This program from the Reforma branch does not run. It has three syntax errors and one that is not: it calculates something it never shows.

```python
# Cash close for the Reforma branch.
from statistics import mean

days = ["mon", "tue", "wed", "thu", "fri", "sat"]
revenue = [18400, 15750, 21300, 19850, 27600, 34200]

average = mean(revenue)
best = days[revenue.index(max(revenue))]

Print("Days recorded:", len(revenue)
print("Revenue for the week:", sum(revenue))
print("Average revenue:" average)
```

Hand in the corrected program, printing four lines: days recorded, revenue for the week, average revenue and best day. Revenue for the week is 137100 and the average is 22850.

Hand in a table of the four problems as well: the line, the message Python gives (or «no error» where it gives none), and what fixes it.

---

## Week 04 · Data, data types and primitive operations

### 04.1 · Recognise

**Five lines from the warehouse**

A shipment arrived and somebody wrote this to check it. Predict the five lines of output.

```python
units = 4300
per_box = 24
price = "1250"

print(units // per_box)
print(units % per_box)
print(2 ** 5)
print(price + "0")
print(type(units / per_box))
```

Explain in one line why the fourth line does not print 1260, and in another why the fifth says `float` when both numbers were integers.

### 04.2 · Apply

**Cost per box of the shipment**

The shipment carries 4,300 units packed 24 to a box. The unit price arrived from the system as the text `"18.75"` and the freight for the whole operation cost 3,200 pesos.

Write a program that declares those four variables with the type each one deserves and prints six lines: full boxes, loose pieces, cost of the goods, the cost per box calculated as `cost / boxes + freight`, the cost per box calculated as `(cost + freight) / boxes`, and the type of the price and of the boxes.

That gives 179 full boxes with 4 pieces left over. The two versions of the cost per box give 3650.42 and 468.3. Explain in two lines which of the two answers «what does it cost me to put one box on the loading dock», and why the other one runs just as well while answering a different question.

### 04.3 · Integrate

**Purchase order with VAT**

The October order pulls together five suppliers and 3,400 pieces travelling on pallets of 48.

```python
suppliers = ["Papelera del Centro", "Insumos Aurora",
             "Distribuidora Sol", "Comercial Bravo", "Grupo Nardo"]
costs = [18420.50, 9375.00, 24680.75, 6120.25, 15302.50]
```

Write a program that prints six lines: how many suppliers are on the order, the subtotal, the total with 16 % VAT, the cost per piece, how many full pallets come out and how many pieces are left over, and the type of the subtotal and of the pallets.

VAT is applied with `*=` on a variable that starts out holding the subtotal, not by writing the result in by hand. The subtotal is 73,899.00 and the total with VAT is 85,722.84. Money figures carry a thousands separator and two decimals.

---

## Week 05 · Statements, input and output

### 05.1 · Recognise

**Five formats on the same campaign**

Predict the five lines this program prints. Write them respecting spaces, commas and symbols.

```python
impressions = 248910
conversion = 0.0273
spend = 41250.5

print(f"{impressions:,}")
print(f"{conversion:.1%}")
print(f"${spend:,.2f}")
print("Reach: {impressions:,}")
print(f"|{impressions:>12,}|")
```

The fourth line does not print what its author expected. Say what it is missing and why Python does not flag it as an error.

### 05.2 · Apply

**A campaign report you can actually send**

Write a program that asks the keyboard for four pieces of campaign data: name, impressions, clicks and spend. Every `input` carries its own prompt, and the three numeric ones are converted as they come in, not afterwards.

The report it prints is five lines: campaign name, impressions with a thousands separator, conversion as a percentage with two decimals, cost per click with a peso sign and two decimals, and cost per thousand impressions in the same format.

Run the program on the «Verano Bajío» campaign: 248910 impressions, 6795 clicks and 52400 of spend. Conversion comes to 2.73 % and cost per click to $7.71. Hand in the file and the transcript of the run.

### 05.3 · Integrate

**Cash flow for the week**

The branch closes its week and wants the report in a column, aligned, ready to paste into Monday's email.

Write a program that asks the keyboard for four things: week number, revenue, outgoings and customers served. From those, calculate the balance, the margin (balance over revenue), the average sale (revenue over customers) and the balance per day, dividing by seven.

The output is seven lines: a heading with the week number and six lines with the label left-aligned in 22 spaces and the figure right-aligned in 14. Money carries thousands and two decimals, and the margin goes as a percentage with one decimal.

Try it on week 14: revenue of 186400, outgoings of 143750 and 612 customers. The balance is 42,650.00, the margin 22.9 % and the average sale 304.58.

---

## Week 06 · Selection structures

### 06.1 · Recognise

**The exact boundary of a turnover band**

Human resources classifies the annual turnover of each area with this program.

```python
turnover = 0.18

if turnover >= 0.25:
    band = "Critical"
elif turnover >= 0.18:
    band = "High"
elif turnover >= 0.10:
    band = "Normal"
else:
    band = "Low"

print(f"{turnover:.1%} · {band}")
```

Write the exact line it prints. Then fill in a table with what it would print if `turnover` held 0.25, 0.099 and 0.30, and answer which area would end up misclassified if the second `elif` used `>` instead of `>=`.

### 06.2 · Apply

**Supplier traffic light**

Purchasing rates every supplier on the percentage of on-time deliveries for the quarter, in four exclusive bands:

| On-time deliveries | Category |
|---|---|
| 95 % or more | Preferred |
| From 85 % to 94.9 % | Reliable |
| From 70 % to 84.9 % | Under watch |
| Below 70 % | Contract under review |

Write a program that asks for the supplier name and its percentage as a proportion (0.96 for 96 %), and prints a single line with the name, the percentage with one decimal and the category.

Hand in three runs: Insumos Aurora at 0.96, Distribuidora Sol at 0.85 and Comercial Bravo at 0.62. The second one is the one that matters, because it lands exactly on the boundary.

### 06.3 · Integrate

**Budget variance by cost centre**

Finance reviews every cost centre by comparing actual spend against budget. The variance is `(spent - budget) / budget`, and it is classified like this:

| Variance | Status |
|---|---|
| Above 10 % | Overspend |
| From 0 % to 10 % | At the limit |
| From minus 15 % to below 0 % | Within range |
| Below minus 15 % | Underspend |

Write a program that asks for the cost centre name, its budget and its actual spend, and prints five lines: cost centre, budget, actual spend, variance as a percentage with one decimal, and status. Money carries a peso sign, thousands and two decimals.

Run the program on Logistics: a budget of 480000 and actual spend of 521000. The variance is 8.5 % and the status is «At the limit». Explain in two lines why spending 8.5 % over budget does not land in the first category.

---

## Week 07 · Nested selection and logical operators

### 07.1 · Recognise

**The condition that always holds**

This program classifies commercial territories, and its first line of output surprises the person who wrote it. Predict the five lines.

```python
region = "Bajío"
tenure = 30
income = 48000

if region == "North" or "West":
    print("Established territory")
else:
    print("Developing territory")

print(tenure >= 24 and income >= 50000)
print(tenure >= 24 or income >= 50000)
print(not (region in ["North", "West"]))
print(region in ["North", "West", "Bajío"])
```

Explain in two lines what Python actually evaluates in the `if` condition, and write the corrected version, the one that does compare the region against both values.

### 07.2 · Apply

**A credit policy with three conditions**

Credit and collections approves a customer's line under these rules, in this order:

1. Approved if they earn 25,000 or more a month, have traded for 24 months or more, their sector is on the eligible list and their credit history is clean.
2. Approved on income if they earn 60,000 or more and their credit history is clean, whatever their tenure or sector.
3. Rejected on credit history if the history is not clean.
4. Rejected in any other case.

The eligible sectors are Commerce, Manufacturing and Services, and they live in a list, not in a chain of `or`.

Write the program. Ask the keyboard for name, monthly income, tenure in months, sector and credit history, and use `and`, `or` and `in` at least once each. Print one line with the name and the outcome.

Hand in three runs: Abarrotes La Paz (31500, 36 months, Commerce, clean history), Taller Mecánico Rueda (72000, 14 months, Services, clean history) and Constructora Zafiro (84000, 60 months, Construction, history not clean). They come out approved, approved on income and rejected on credit history.

### 07.3 · Integrate

**Supplier review with a contract in force**

Purchasing decides what to do with each supplier. The first question is whether the contract is still in force, because the compliance record of somebody who no longer has a contract decides nothing.

With a contract in force: at 95 % or more, volume goes up; from 85 % to 94.9 %, volume holds; below 85 %, they get audited and volume comes down. Without a contract in force, the only action is to renew before evaluating.

Separately from that, if the supplier is on the critical list and its compliance sits below 85 %, the alert to find a second source goes up. The critical suppliers are Insumos Aurora and Grupo Nardo.

Write the program with the three keyboard inputs and two lines of output: name with percentage and action, and the alert. Hand in two runs: Insumos Aurora with a contract in force and 0.82, and Distribuidora Sol with no contract and 0.97.

Add half a page answering this: the alert was written as one `if` with two conditions joined by `and`. Write it nested as well, and say which of the two you would rather read six months from now.

---

## Week 08 · Repetition · First midterm

### 08.1 · Recognise

**How many passes these two loops make**

Predict the complete output. It is four lines.

```python
for quarter in range(3, 12, 4):
    print(quarter)

fund = 480000
spend = 96000
month = 0

while fund >= spend:
    fund -= spend
    month += 1

print(month, fund)
```

Write out the trace of the last two passes of the `while` as well, with columns for pass, fund on entry, whether the condition holds, fund on exit and month. Then answer what would change if the condition read `fund > 0` instead of `fund >= spend`.

### 08.2 · Apply

**Turnover by branch**

Human resources has the closed year in three paired lists:

```python
branches = ["Reforma", "Satélite", "Valle", "Chapalita", "Mitras"]
leavers = [7, 12, 4, 9, 15]
headcount = [86, 140, 62, 108, 125]
```

Write a program that walks the five branches with a `for` and `range(len(...))`, printing one line per branch with the name left-aligned in 12 spaces, leavers in 4, headcount in 6 and turnover in 9 as a percentage with one decimal.

Close with a totals line labelled «Global», dividing the sum of leavers by the sum of headcounts. Mitras comes out at 12.0 % and the global figure at 9.0 %.

The program has to keep working without touching the loop if a sixth branch is added tomorrow.

### 08.3 · Integrate

**First midterm review: cash flow for the half year**

This exercise crosses units 1 to 4. The operation has the half year captured like this:

```python
months = ["jan", "feb", "mar", "apr", "may", "jun"]
revenue = [412000, 388500, 455200, 401800, 372900, 468300]
outgoings = [398400, 401200, 430600, 418500, 395700, 402100]
```

The program has three parts.

The first prints a heading with the columns Month, Revenue, Outgoings, Balance and Status.

The second walks the six months with a `for`, works out each month's balance and classifies it as «Surplus» when it is zero or positive and «Deficit» when it is negative. Every line carries its figures with a thousands separator, right-aligned in 12 spaces. Close with a totals line.

The third answers, with a `while`, how many months a contingency fund of 250,000 pesos would survive if the deficit repeated at 22,800 pesos a month, and prints how many months it covers and how much is left unused. That is 10 months with 22,000 pesos left.

The half year closes with a balance of 52,200 pesos. Three of the six months come out in deficit.

---

## Week 09 · Accumulators, flags and nested loops

### 09.1 · Recognise

**An accumulator that does not accumulate**

Purchasing reviewed five requisitions with this program. Predict the four lines of output.

```python
purchases = [18400, 9375, 24680, 6120, 15302]

for purchase in purchases:
    total = 0
    total += purchase

large = 0
has_urgent = False

for purchase in purchases:
    if purchase > 15000:
        large += 1
    if purchase > 24000:
        has_urgent = True

print(total)
print(large)
print(has_urgent)

for purchase in purchases:
    if purchase > 30000:
        print("Needs committee approval")
        break
else:
    print("No purchase goes to committee")
```

Explain in one line why the first line does not print 73,877, and in another why the `else` of the last loop does run. Write out the one-line fix for the first loop as well.

### 09.2 · Apply

**Six campaigns in a single pass**

Marketing closed the quarter with these three paired lists:

```python
campaigns = ["Instagram", "Meta", "Google", "TikTok", "Email", "Display"]
clicks = [5074, 3820, 6910, 1240, 2480, 7350]
spend = [38500, 29800, 51200, 9600, 12400, 61300]
```

Write a program that answers five questions with a single `for`, not with five:

1. How much the quarter's spend adds up to.
2. How many campaigns beat 3,000 clicks.
3. Whether any of them costs more than 8 pesos per click.
4. Which campaign has the best cost per click, and what it is.
5. The overall cost per click, dividing total spend by total clicks.

Total spend is $202,800 and the best campaign is Email at $5.00 per click. The overall cost per click comes to $7.55, which is not the average of the six individual costs. Explain in two lines why those two figures differ and which one you would report to the committee.

### 09.3 · Integrate

**Branch dashboard by quarter**

The year's sales live in a single list of twelve figures, laid out row by row: the four quarters of North, then the four of Centre, then the four of West.

```python
branches = ["North", "Centre", "West"]
quarters = ["Q1", "Q2", "Q3", "Q4"]
sales = [412000, 388000, 455000, 501000,
         298000, 331000, 305000, 362000,
         214000, 240000, 268000, 291000]
```

Write a program with two loops, one inside the other, printing the whole dashboard in thousands of pesos with no decimals: one line per branch with its four quarters and its total, and a final line with the grand total. North closes at 1,756 and the grand total at 4,065.

The figure for branch `i` and quarter `j` sits at position `i * len(quarters) + j` of the list. That calculation has to be written that way, not with the indices put in by hand.

Add a counter at the end for how many quarters of the year beat 400,000 pesos. That is 3 out of 12.

---

## Week 10 · User-defined functions

### 10.1 · Recognise

**The function that returns nothing**

Predict what this program prints, line by line, and what happens when it reaches the last one.

```python
def commission(sale, rate):
    sale * rate


def bonus(sale):
    base = sale * 0.03
    return base


result = commission(180000, 0.05)

print(result)
print(bonus(180000))
print(base)
```

Answer three things. What `commission` is missing and what it would print once fixed. Why the third line fails when `base` exists inside `bonus`. And what error would come out, with its exact name, if somebody tried to add `result + 100`.

### 10.2 · Apply

**Break-even point for three businesses**

Write a function `break_even(fixed_costs, price, variable_cost)` returning how many units have to be sold to neither lose nor gain. The formula divides the fixed costs by the contribution margin, which is the price minus the variable cost.

The function carries a docstring, prints nothing and only returns the number. Call it three times from the main program and print each result with a label, a thousands separator and two decimals:

| Business | Fixed costs | Price | Variable cost |
|---|---|---|---|
| Coffee shop | 145,000 | 68.00 | 23.00 |
| Medical equipment | 980,000 | 1,250.00 | 845.00 |
| Workshop | 60,000 | 40.00 | 20.00 |

The coffee shop needs 3,222.22 units and the workshop exactly 3,000.00. Answer in two lines what error the function would raise if the price and the variable cost were equal, and what that means for the business.

### 10.3 · Integrate

**Turnover dashboard by area**

Write two functions. `turnover(leavers, headcount)` returns the index for the period as a proportion. `classify(index)` returns the band: «Critical» at 0.20 or above, «High» at 0.15 or above, «Normal» at 0.10 or above and «Low» below that. Both carry a docstring and neither prints anything.

With those two functions and this data, print the complete table:

```python
areas = ["Sales", "Operations", "Administration", "Logistics", "IT"]
leavers = [9, 21, 3, 14, 2]
headcount = [74, 112, 48, 96, 25]
```

Every line carries the area left-aligned in 16 spaces, leavers in 7, headcount in 11, turnover in 10 as a percentage with one decimal, and the band. Close with a «Company» line using the same two functions on the sums.

Operations comes out «High» at 18.8 % and the company «Normal» at 13.8 %. Explain in two lines why the company index is not the average of the five.

---

## Week 11 · Arguments, built-in functions and modules

### 11.1 · Recognise

**An argument that lands in the wrong place**

Predict the four lines of output.

```python
from statistics import mean, median


def total_cost(base, vat=0.16, shipping=0):
    return round(base * (1 + vat) + shipping, 2)


print(total_cost(12000))
print(total_cost(12000, 350))
print(total_cost(12000, shipping=350))

salaries = [18400, 17950, 42300, 12800, 26500]

print(mean(salaries), median(salaries))
```

The second line prints an absurd number and the program flags nothing. Explain in two lines what Python understood the 350 to be and how the call is written so it means what its author wanted.

Answer as well why the average of those five salaries sits so far above the median, and which of the two figures you would use to tell a candidate what that area pays.

### 11.2 · Apply

**Annual cost of a role**

Write a function `payroll_cost(base_salary, months=12, bonus=0.0, benefits=1.35)` returning the annual cost of a role: the base salary times the months, times the benefits factor, times one plus the bonus.

Call it three times on a base salary of 18,400 pesos and print each result with a label, a peso sign, thousands and two decimals:

1. The standard role, touching none of the optional parameters.
2. The same role over thirteen months, passing the argument by position.
3. The same role with a 10 % bonus, passing the argument by keyword and skipping `months`.

The standard role costs $298,080.00 a year and the one with the bonus costs $327,888.00. Explain in one line what would happen if you wrote `payroll_cost(18400, 0.10)` expecting the bonus.

### 11.3 · Integrate

**Payroll diagnostic for one area**

The area has nine roles on these monthly salaries:

```python
salaries = [12800, 15600, 17950, 18400, 19250, 22400, 26500, 33900, 84000]
```

Write a function `summarise(label, value)` returning, without printing, a line with the label left-aligned in 22 spaces and the value right-aligned in 12, with a peso sign, thousands and two decimals.

Use that function to print the diagnostic: monthly payroll, average, median, highest salary, lowest salary and second highest salary. Above all of it goes a plain line with how many roles there are. At the end, a sentence stating how far the average sits above the median.

The average and the median come from `statistics`. The second highest salary comes from a sorted copy made with `sorted`, leaving the original list untouched. The monthly payroll is $250,800.00 and the average sits 8,616.67 above the median.

Close with three lines: which figure you would report to the area director, which one to the union, and why both are true.

---

## Week 12 · Lists and tuples

### 12.1 · Recognise

**Six lines on the same list**

This program touches an inventory list six different ways. Predict the six lines of output.

```python
units = [340, 125, 890, 470, 210]

result = units.sort()
print(result)
print(units)

backup = units
backup.append(999)
print(len(units))

copy = units.copy()
copy.clear()
print(len(units), len(copy))

print(units[1:4])
print(units[-2])
```

Answer three things. Why the first line does not print the sorted list. Why `units` measures 6 after only `backup` was touched. And what would have to change on the `backup` line for the original list to stay put.

### 12.2 · Apply

**The three SKUs that weigh most**

The central warehouse inventory is twelve keys with these pieces:

```python
inventory = [340, 125, 890, 470, 210, 655, 890, 305, 148, 720, 415, 260]
```

Write a program that prints six lines: the list at the start, the three highest figures, the total pieces in the inventory, the position of the SKU holding 720 pieces, how many times the value 890 appears, and the list at the end.

The condition that grades this exercise is that the first and the last line come out identical. Sort on a copy, not on the original. The inventory adds up to 5,428 pieces and the SKU with 720 sits at position 9.

### 12.3 · Integrate

**The keys above the threshold**

The catalogue of eight keys arrives as three paired lists:

```python
skus = ["PAP-100", "PAP-215", "OFI-330", "OFI-412",
        "LIM-501", "LIM-620", "TEC-710", "TEC-844"]
units = [1840, 5210, 960, 2375, 3120, 880, 1450, 640]
prices = [38.50, 9.90, 74.00, 22.50, 15.75, 96.20, 58.40, 210.00]
```

Write a program that works out the amount for each key (units times price) and builds a new list, empty at the start, holding the keys whose amount reaches or beats 70,000 pesos. Every element of that new list is a tuple of amount and key, so the ordering can be worked out without losing the name.

Sort that list from highest to lowest amount and print, in this order: how many keys are left out of how many, one line per key with the key on the left in 10 spaces and the amount on the right in 12 with thousands and two decimals, and a final line proving the original lists are still complete and still in their order.

Five keys of 8 make the cut. The first is TEC-844 at 134,400.00 and the last one in is PAP-100 at 70,840.00. The threshold is declared once, in a variable, and appears in the printed text as well.

---

## Week 13 · Sets and dictionaries · Second midterm

### 13.1 · Recognise

**One catalogue and two months of suppliers**

Predict the seven lines this program prints.

```python
lead_days = {"Aurora": 3, "Sol": 7, "Bravo": 5}
lead_days["Sol"] = 4
lead_days["Nardo"] = 9

print(len(lead_days))
print(lead_days.get("Sol"))
print(lead_days.get("Zafiro"))
print(lead_days.get("Zafiro", 15))

march = {"Aurora", "Sol", "Bravo"}
april = {"Sol", "Bravo", "Nardo", "Zafiro"}

print(sorted(march & april))
print(sorted(april - march))
print(len(march | april))
```

Answer three things. Why the dictionary measures 4 and not 5 after the two assignments. What would have happened with `lead_days["Zafiro"]` instead of `get`. And which set operation answers «which suppliers invoiced in one month and not the other», regardless of which.

### 13.2 · Apply

**Catalogue of lead times**

Purchasing has the suppliers and their lead times in two paired lists:

```python
suppliers = ["Aurora", "Sol", "Bravo", "Nardo", "Zafiro", "Delta"]
days = [3, 4, 5, 9, 6, 12]
```

Write a program that builds the dictionary with a loop, not by typing it out, and then prints: how many suppliers the catalogue holds, the full table walked with `items` (name in 10 spaces on the left, lead time in 4 on the right, followed by the word days), the average lead time, the lookup for Bravo and the lookup for Quintana.

Both lookups use `get` with a default of 30 days, which is the master contract lead time for anyone not in the catalogue. Bravo delivers in 5 days and Quintana in 30. The average lead time is 6.5 days.

### 13.3 · Integrate

**Second midterm review: two months of purchases**

This exercise crosses units 4, 5 and 6. Each month arrives as two lists: who invoiced and how much, with suppliers appearing more than once.

```python
march_names = ["Aurora", "Sol", "Bravo", "Aurora", "Nardo", "Sol"]
march_amounts = [18400, 9375, 24680, 6120, 15302, 8100]
april_names = ["Sol", "Bravo", "Zafiro", "Bravo", "Aurora", "Zafiro"]
april_amounts = [11250, 19800, 7400, 5600, 22150, 9900]
```

Write two functions with a docstring and no `print` inside. `consolidate(names, amounts)` returns a dictionary of accumulated purchases per supplier. `variation(before, after)` returns the percentage change between two amounts.

With those two functions, print the report: total purchases for March, total purchases for April, the change in spend between the two months, the list of new suppliers, the list of the ones that stopped invoicing, and a table of the ones present in both months with their March amount, their April amount and their change.

March closes at $81,977 and April at $76,100, a drop of 7.2 %. The only new supplier is Zafiro and the only one that left is Nardo. All three supplier comparisons come from set operations, not from loops with an `if`.

---

## Week 14 · Text and CSV files

The three exercises this week work on the same file. Create it with this exact content, named `march_payroll.csv`, in the same folder as your program.

```text
id,area,role,monthly_salary,days_worked
E-001,Sales,Executive,"$18,400.00",30
E-002,Sales,Executive,"$17,950.00",28
E-003,Sales,Manager,"$42,300.00",30
E-004,Operations,Warehouse clerk,"$12,800.00",30
E-005,Operations,Warehouse clerk,"$12,800.00",
E-006,Operations,Supervisor,"$26,500.00",30
E-007,Administration,Analyst,"$21,700.00",30
E-008,Administration,Accountant,"$33,900.00",27
E-009,Sales,Executive,"$19,250.00",30
E-010,Operations,Forklift operator,"$15,600.00",30
E-011,Administration,Analyst,"$22,400.00",30
E-012,Sales,Executive,"$18,050.00",30
E-013,Operations,Warehouse clerk,"$13,900.00",30
E-014,Administration,Coordinator,"$28,300.00",30
E-015,Sales,Executive,"$16,700.00",26
```

### 14.1 · Recognise

**What a file hands back**

Predict the five lines of output from this program, running on the file above.

```python
import csv
from pathlib import Path

DATA = Path(__file__).resolve().parent

with (DATA / "march_payroll.csv").open(encoding="utf-8") as f:
    rows = list(csv.DictReader(f))

print(len(rows))
print(rows[0]["id"], rows[0]["monthly_salary"])
print(type(rows[0]["days_worked"]))
print(rows[4]["days_worked"] == "")
print(rows[-1]["area"], rows[-1]["role"])
```

Answer three things. Why the first line prints 15 and not 16. What would happen if somebody swapped `"utf-8"` for mode `"w"` on the `open` line. And why `int(rows[4]["days_worked"])` does not give zero but an error, and which one.

### 14.2 · Apply

**Totals for the March payroll**

Write a program that reads the file with `DictReader` and defines two conversion functions with a docstring:

- `to_float(text)` turns `"$18,400.00"` into the number 18400.0, stripping the symbol and the thousands comma.
- `to_int(text, missing=0)` converts to an integer and decides what a blank cell is worth. The default for a blank cell is zero, and that decision is written down in the docstring.

With those two functions, walk the rows and print five lines: how many employees the file carries, the monthly payroll, the average salary, total days worked, and how many records have fewer than 30 days.

The monthly payroll is $320,550.00 and the days add up to 411. The last line prints 4, not 3. Explain in two lines who it is counting that it should not be, and why the decision you made in `to_int` is responsible.

### 14.3 · Integrate

**Summary by area, written to a new file**

Write a program that reads `march_payroll.csv`, accumulates the payroll and the number of roles per area into two dictionaries, and produces two outputs.

The first is the table on screen, sorted by area name, with the columns Area in 16 spaces on the left, Roles in 8, Payroll in 14 and Average in 13, the last two with thousands and two decimals. Below it goes the list of ids carrying a blank days cell.

The second is the file `area_summary.csv`, written from the program, with the header `area,roles,payroll,average_salary` and one line per area. The file is opened in write mode, with `newline=""` and an explicit encoding.

Sales concentrates 6 roles and $132,650.00. Administration has the highest average salary at $26,575.00. The only id with no days worked is E-005.

Close with three lines explaining what you decided about the blank cell, which two other decisions were defensible, and how each one would change the figures you just reported.

---

## Week 15 · Series, DataFrame, cleaning, grouping and joining

The three exercises this week work on the same file. Create it with this exact content, named `sales_2026.csv`.

```text
date,region,channel,units,unit_price
2026-01-12,North,Wholesale,120,"$1,250.00"
2026-01-28,centre,Retail,45,"$1,380.00"
2026-02-09, North ,Online,80,"$1,250.00"
2026-02-23,West,Wholesale,150,"$1,190.00"
2026-03-05,NORTH,Retail,60,"$1,380.00"
2026-03-19,Centre,Online,,"$1,250.00"
2026-04-02,South,Wholesale,95,"$1,190.00"
2026-04-16,North,Online,110,"$1,250.00"
2026-05-07,Centre,Wholesale,140,"$1,190.00"
2026-05-21,west,Retail,55,"$1,380.00"
2026-06-04,North,Wholesale,130,"$1,250.00"
2026-06-18,South,Online,,"$1,250.00"
2026-07-09,Centre,Retail,70,"$1,380.00"
2026-07-23,West,Online,85,"$1,250.00"
2026-08-06,North,Wholesale,160,"$1,190.00"
2026-08-20,Centre,Online,90,"$1,250.00"
2026-09-03,South,Retail,40,"$1,380.00"
2026-09-17,West,Wholesale,175,"$1,190.00"
2026-10-01,North,Online,105,"$1,250.00"
2026-10-15,Centre,Wholesale,145,"$1,190.00"
2026-08-06,North,Wholesale,160,"$1,190.00"
2026-09-17,West,Wholesale,175,"$1,190.00"
```

### 15.1 · Recognise

**Diagnosis before touching anything**

Predict the complete output of this program, including the types pandas infers.

```python
import pandas as pd
from pathlib import Path

DATA = Path(__file__).resolve().parent

sales = pd.read_csv(DATA / "sales_2026.csv")

print(sales.shape)
print(sales.dtypes)
print(sales["units"].isna().sum())
print(sales.duplicated().sum())
print(sales["region"].nunique())
print(sorted(sales["region"].unique()))
```

Answer four things, one line each. Why `units` came out `float64` and not an integer. Why `unit_price` came out as text. How many distinct regions the operation really has, and how many a `groupby` run right now would report. And whether the total pieces in the file can be worked out yet, or not.

### 15.2 · Apply

**The four repairs, with their log**

Write a program that loads the file and cleans it in this order, printing one line after each step so the log is on the record:

1. On loading: how many rows, how many distinct regions, how many duplicates and how many blank unit counts.
2. After removing duplicates: how many rows are left.
3. After normalising the region with `str.strip` and `str.title`: the list of regions left.
4. After converting the price to a number and the date to a date, and calculating the `amount` column: the total amount.
5. After resolving the holes in units: how many rows, how many pieces and how much revenue, plus the average sale and the final types of every column.

The file starts with 22 rows and 8 regions, and ends with 18 rows and 4 regions. Revenue is $2,301,950.00 and the average sale $127,886.11.

Step 4 and step 5 report the same revenue. Explain in two lines why dropping the rows with blank unit counts did not move the total by a single peso, and what did change with those two rows gone.

### 15.3 · Integrate

**Attainment dashboard**

With the file already clean, produce three outputs.

The first is the summary by region, with `groupby` and `agg`, four columns you name yourself: revenue, pieces, deals and average sale, sorted by revenue from highest to lowest.

The second is the region against channel grid with `pivot_table`, summing amount, with row and column totals, expressed in thousands with one decimal. One of the cells comes out empty: say which one and why.

The third is the attainment dashboard. The territory catalogue lives in the program itself, with this information:

| region | manager | target |
|---|---|---|
| North | Lucía Ramos | 900,000 |
| Centre | Iván Peña | 700,000 |
| West | Marta Ocampo | 650,000 |
| South | Diego Salas | 250,000 |
| Gulf | Rocío Trejo | 200,000 |

Before joining, audit the join in both directions with `indicator` and report the three counts. Then join with the safe mode and add the attainment column, dividing revenue by target.

North closes at 106.0 % of its target and South at 67.3 %. The audit flags one region present on one side only: say which one, which side it is on, and why that is not a data error. Say as well what would have happened to that region if you had joined with `inner` without auditing.

---

## Week 16 · Visualisation, matplotlib and seaborn

### 16.1 · Recognise

**The bar that says something else**

The summary by region from last week's clean file came out like this:

| region | revenue (sum) | average sale | deals |
|---|---|---|---|
| North | 954,450.00 | 136,350.00 | 7 |
| Centre | 610,350.00 | 122,070.00 | 5 |
| West | 568,900.00 | 142,225.00 | 4 |
| South | 168,250.00 | 84,125.00 | 2 |

Somebody is about to present this line to the committee:

```python
sns.barplot(data=sales, x="region", y="amount", ax=ax)
```

Answer four things. What figure that bar draws for each region, with the four numbers taken from the table. What ranking that chart ends up with, and what ranking a total revenue chart would end up with. What the call is missing for it to draw the total. And what one-line sentence you would use as a title if you wanted the reader to leave with both readings.

Answer as well, one line each, what is wrong with these three chart decisions:

```python
ax.set_ylim(500000, 1000000)
ax.plot(["North", "Centre", "West", "South"], revenue)
ax.pie(revenue, labels=regions, autopct="%1.0f%%")
```

### 16.2 · Apply

**A year of seasonality in one bar chart**

Comercializadora Aurora closed 2026 with this monthly revenue:

```python
MONTHS = ["jan", "feb", "mar", "apr", "may", "jun",
          "jul", "aug", "sep", "oct", "nov", "dec"]

revenue = pd.Series(
    [1284000, 962000, 1431000, 1189000, 1516000, 1340000,
     1208000, 1377000, 1465000, 1623000, 2048000, 3412000],
    index=MONTHS,
)
```

Produce a bar chart saved as `seasonality_2026.png`, at 150 dots per inch, meeting six conditions:

1. The three bars of the last quarter go in strong blue and the other nine in pale blue.
2. The title states the finding with its figure, and that figure is calculated in the code, not typed in by hand.
3. The vertical axis is labelled with its unit and starts at zero.
4. The vertical axis ticks read as 1.5M, not as 1500000.
5. The source goes at the foot, with the period and how many months it carries.
6. The figure is closed when the work is done.

The program also prints five lines: revenue for the year, weight of the last quarter, weight of December on its own, lowest month with its figure, and confirmation that the image was saved.

The year closes at $18,855,000, the last quarter weighs 37.6 % and December on its own weighs 18.1 %. Hand in the image and the file that generates it.

### 16.3 · Integrate

**Two charts for the board**

This exercise uses both files of the course: `march_payroll.csv` from week 14 and `sales_2026.csv` from week 15. Set the seaborn theme once, at the top.

The first chart is a box plot of the monthly salary by area, with the areas sorted by median from highest to lowest, base at zero, a title carrying the finding and the source at the foot. It is saved as `salaries_by_area.png`. Before drawing it, print the table of count, median, average and maximum by area, which is where the title has to come from.

The second is a heatmap of region against channel over revenue, in thousands of pesos, with the value written inside each cell and no decimals. It takes the `pivot_table` grid from last week straight in, with no extra preparation. It is saved as `region_channel_grid.png`.

Sales has a median of 18,225.00 and a maximum of 42,300.00. Operations has a median of 13,900.00 and a maximum of 26,500.00.

Write the alt text for each chart at the end, three lines each: what kind of chart it is, what range it covers, and what is visibly going on. Every figure appearing in the alt text has to be in the tables you printed.

---

## Week 17 · Review and final exam

### 17.1 · Recognise

**Four errors that never announce themselves**

This program runs start to finish and all four of its figures are wrong. It works on `sales_2026.csv` without cleaning it.

```python
import pandas as pd
from pathlib import Path

DATA = Path(__file__).resolve().parent

sales = pd.read_csv(DATA / "sales_2026.csv")

by_region = sales.groupby("region")["units"].sum()

sales[sales["region"] == "North"]["channel"] = "Wholesale"

for pieces in sales["units"]:
    total = 0
    total += pieces

order = by_region.tolist()
order = order.sort()

print(len(by_region))
print(sales["channel"].value_counts()["Wholesale"])
print(total)
print(order)
```

Predict the four lines of output and fill in this table, one row per error:

| Line | Which of the six course errors it is | What it prints | What was wanted | How it is fixed |
|---|---|---|---|---|

The second error is the only one that also leaves a warning on screen. Copy it exactly as it appears and explain in one line why a warning is not the same as an error, and why that makes it more dangerous, not less.

### 17.2 · Apply

**From file to finding, in one pass**

Write a program that loads `sales_2026.csv`, inspects it, cleans it, crosses region with channel and closes with a conclusion.

The order is fixed: inspect, clean, group, conclude. The output is four blocks:

1. The loading diagnosis on one line: rows, distinct regions, duplicates and blank unit counts.
2. The same line once clean: rows, distinct regions and revenue.
3. The four region and channel combinations with the most revenue, with their number of deals.
4. A sentence saying which combination is worth attending to first, with two figures: its revenue and what percentage of the year that represents.

The leading combination is North in Wholesale, at $502,900.00, 21.8 % of the year's revenue. If your percentage comes out different, check what total you are dividing by.

### 17.3 · Integrate

**Year-end close with an audit, a dashboard and a chart**

This is the closing exercise and it is solved in a single file with two functions and their docstrings.

`load_clean(path)` takes the path of the sales file and returns the table ready to analyse, with the date converted and the `amount` column already calculated. `board(sales, catalogue)` takes the clean table and the territory catalogue, and returns attainment against target by region, sorted from highest to lowest.

The catalogue is the same one from week 15, with its five territories, their managers and their targets.

The program produces four outputs.

The first is the audit of the join in both directions, with the three counts and the name of the region that shows up on one side only.

The second is the dashboard, with region, manager, revenue, deals, average sale, target and attainment. North lands at 106.0 % and West at 87.5 %, above Centre by 0.3 points despite selling less.

The third is three figures on the monthly operation: how many months had activity, which was the strongest, and what percentage of the year it represents. That comes out as 10 months, month 10 and 13.2 %.

The fourth is a bar chart of revenue by region saved as `year_end_2026.png`, with the leading region highlighted, the title calculated from the data, the vertical axis from zero and in millions, and the source at the foot stating how many rows were analysed out of how many.

Close with a half-page report: the question you answered, what you decided about the incomplete rows and the duplicates, the finding with its figures, and a recommendation for next year. Every cleaning decision goes down in writing and every figure has to be checkable against the program's output.
