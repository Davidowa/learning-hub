"""Rebuild the three CSV files the advanced modules teach against.

Run it only if you want to regenerate them. The seed is fixed, so the output is
byte for byte the same every time, which is what keeps the numbers printed on a
slide matching the numbers in the file.

The sales table is deliberately dirty, and each defect exists to teach one
cleaning step: blank cells, duplicated rows, a text column that should be a
number, and a region name typed four different ways. Nothing here is random at
run time, so the numbers on a slide keep matching the file forever.
"""
import csv
import random
from datetime import date, timedelta
from pathlib import Path

# The files land next to this script, so the whole folder can be copied anywhere.
OUT = Path(__file__).resolve().parent

rng = random.Random(20260808)

REGIONS = ['North', 'South', 'Centre', 'West']
CHANNELS = ['Retail', 'Online', 'Wholesale']
PRODUCTS = {
    'Espresso machine': 8990.0,
    'Coffee grinder': 2450.0,
    'Filter kettle': 1290.0,
    'Bean subscription': 690.0,
    'Travel mug': 349.0,
}
# each region pulls a different mix, so a group-by actually shows something
REGION_WEIGHT = {'North': 1.30, 'South': 0.80, 'Centre': 1.55, 'West': 0.95}
CHANNEL_WEIGHT = {'Retail': 1.00, 'Online': 1.25, 'Wholesale': 2.10}
# a seasonal curve: January is slow, November and December are not
MONTH_WEIGHT = [0.72, 0.78, 0.90, 0.95, 1.00, 1.05, 0.98, 0.92, 1.08, 1.15, 1.45, 1.60]

rows = []
start = date(2025, 1, 6)
for week in range(52):
    day = start + timedelta(weeks=week)
    for region in REGIONS:
        for _ in range(rng.randint(1, 2)):
            product = rng.choice(list(PRODUCTS))
            channel = rng.choice(CHANNELS)
            base = 9 * REGION_WEIGHT[region] * CHANNEL_WEIGHT[channel] * MONTH_WEIGHT[day.month - 1]
            units = max(1, round(rng.gauss(base, base * 0.28)))
            price = PRODUCTS[product] * rng.choice([1.00, 1.00, 1.00, 0.90, 0.85])
            rows.append({
                'date': day.isoformat(),
                'region': region,
                'channel': channel,
                'product': product,
                'units': str(units),
                'unit_price': f'$ {price:,.2f}',   # text on purpose, so it has to be converted
            })

# ── the deliberate dirt
# 1. a region typed four ways, so the group-by splits until it is normalised
for i in rng.sample(range(len(rows)), 24):
    rows[i]['region'] = rng.choice(['north', 'NORTH', ' North', 'North '])
# 2. blank unit counts, so a sum has to decide what to do with them
for i in rng.sample(range(len(rows)), 11):
    rows[i]['units'] = ''
# 3. rows captured twice, the way a paste error leaves them
for i in rng.sample(range(len(rows)), 7):
    rows.append(dict(rows[i]))

rng.shuffle(rows)
with (OUT / 'sales.csv').open('w', newline='', encoding='utf-8') as f:
    sales_out = csv.DictWriter(f, fieldnames=['date', 'region', 'channel',
                                              'product', 'units', 'unit_price'])
    sales_out.writeheader()
    sales_out.writerows(rows)
print(f'sales.csv      {len(rows)} rows')

# ── the lookup table: this is the VLOOKUP of the course, and later the merge
with (OUT / 'regions.csv').open('w', newline='', encoding='utf-8') as f:
    regions_out = csv.writer(f)
    regions_out.writerow(['region', 'manager', 'country', 'monthly_target'])
    regions_out.writerows([
        ['North', 'Ana Robles', 'Mexico', 480000],
        ['South', 'Luis Ferrer', 'Mexico', 300000],
        ['Centre', 'Paula Ines', 'Mexico', 560000],
        ['West', 'Marco Duarte', 'Mexico', 360000],
        ['East', 'Sofia Lara', 'Mexico', 220000],   # no sales rows: shows what a left join does
    ])
print('regions.csv    5 rows')

# ── the HR table, clean, for group-by and merge practice
AREAS = {
    'Sales': (['Account executive', 'Sales analyst', 'Sales manager'], 24000, 62000),
    'Marketing': (['Content specialist', 'Campaign analyst', 'Brand manager'], 22000, 58000),
    'Finance': (['Accounts clerk', 'Financial analyst', 'Controller'], 26000, 74000),
    'People': (['Recruiter', 'People analyst', 'People manager'], 21000, 55000),
    'Operations': (['Warehouse lead', 'Logistics analyst', 'Operations manager'], 20000, 60000),
}
CITIES = ['Mexico City', 'Guadalajara', 'Monterrey', 'Queretaro']
emp = []
for n in range(1, 121):
    area = rng.choice(list(AREAS))
    titles, low, high = AREAS[area]
    idx = rng.choices([0, 1, 2], weights=[5, 3, 1])[0]
    tenure = rng.randint(2, 132)
    salary = round(low + (high - low) * (idx / 2) * rng.uniform(0.82, 1.10)
                   + tenure * 45, -2)
    emp.append({
        'employee_id': f'E{n:04d}',
        'area': area,
        'job_title': titles[idx],
        'city': rng.choice(CITIES),
        'tenure_months': tenure,
        'monthly_salary': int(salary),
    })
with (OUT / 'employees.csv').open('w', newline='', encoding='utf-8') as f:
    emp_out = csv.DictWriter(f, fieldnames=list(emp[0]))
    emp_out.writeheader()
    emp_out.writerows(emp)
print(f'employees.csv  {len(emp)} rows')
