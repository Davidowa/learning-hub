# Choosing the rows and columns you care about.
#
# In a spreadsheet this is scrolling, hiding columns and switching the AutoFilter
# on and off. In pandas you describe what you want and get a new table back. The
# original is never touched, which means you can try a filter without fear.

import pandas as pd
from pathlib import Path

DATA = Path(__file__).resolve().parent.parent / "data"
employees = pd.read_csv(DATA / "employees.csv")

print("The table we will work on:")
print(employees.head())


# ────────────────────────────────────────────────────────── choosing columns

# One column, by name. This gives back a Series.
print("\nOne column:")
print(employees["monthly_salary"].head(3))

# Several columns, by passing a list of names. This gives back a DataFrame.
# The double brackets confuse everyone once: the outer pair is the selection,
# the inner pair is the list of names you are selecting.
print("\nThree columns:")
print(employees[["employee_id", "area", "monthly_salary"]].head(3))


# ───────────────────────────────────────────────────────────── choosing rows

# A condition applied to a column returns a column of True and False, one per
# row. This is the mask, and it is the whole idea behind filtering in pandas.
mask = employees["monthly_salary"] > 50000
print("\nThe mask, first five rows:")
print(mask.head())
print("Rows that satisfy it:", mask.sum())

# Feed the mask back to the DataFrame and you get only the rows marked True.
well_paid = employees[mask]
print("\nEmployees earning more than 50,000:", len(well_paid))
print(well_paid.head(3))

# Usually the mask is written inline rather than named.
print("\nFinance area only:", len(employees[employees["area"] == "Finance"]))


# ─────────────────────────────────────────────────────── combining conditions

# Two rules that must both hold. Note the ampersand, not the word "and", and
# note the parentheses: without them Python applies the comparison in the wrong
# order and raises an error that reads like nonsense.
senior_finance = employees[(employees["area"] == "Finance") &
                           (employees["tenure_months"] > 60)]
print("\nFinance with more than five years:", len(senior_finance))

# Either rule. The pipe is "or".
either = employees[(employees["area"] == "Finance") |
                   (employees["area"] == "Sales")]
print("Finance or Sales:", len(either))

# For more than two options, isin reads better than a chain of pipes. This is
# the pandas answer to a filter with several boxes ticked.
front_office = employees[employees["area"].isin(["Sales", "Marketing"])]
print("Sales or Marketing:", len(front_office))

# The tilde negates a mask: everything the condition did not match.
back_office = employees[~employees["area"].isin(["Sales", "Marketing"])]
print("Everything else:", len(back_office))


# ────────────────────────────────────────────────── filtering on text columns

# Text columns get their own set of tools under .str, and they apply to the
# whole column at once. This is where the wildcards of a spreadsheet go.
managers = employees[employees["job_title"].str.contains("manager", case=False)]
print("\nManagers of any kind:", len(managers))
print(managers[["job_title", "area"]].head(3))


# ────────────────────────────────────────────────── rows and columns together

# loc takes rows first, columns second, and it works with labels.
print("\nSalary and area of the managers, first three:")
print(managers.loc[:, ["area", "job_title", "monthly_salary"]].head(3))

# iloc does the same thing with positions instead of labels. The row numbers
# here count from 0, and the end of a range is not included, exactly as slicing
# worked back in the basics module.
print("\nFirst two rows, first three columns, by position:")
print(employees.iloc[0:2, 0:3])


# ───────────────────────────────────────────────────────────────── sorting

# One column, largest first.
top = employees.sort_values("monthly_salary", ascending=False)
print("\nThe five highest salaries:")
print(top[["employee_id", "area", "job_title", "monthly_salary"]].head())

# Several columns: area alphabetically, then salary descending inside each area.
by_area = employees.sort_values(["area", "monthly_salary"], ascending=[True, False])
print("\nSorted by area, then by salary:")
print(by_area[["area", "job_title", "monthly_salary"]].head())


# ──────────────────────────────────────────────────────────── what to remember
#
# 1. A filter is a column of True and False handed back to the table.
# 2. Use & and |, never the words "and" and "or", and wrap each condition in
#    parentheses. That single rule prevents the most confusing error in pandas.
# 3. Selecting never changes the original table. Assign the result to a name if
#    you want to keep it.
