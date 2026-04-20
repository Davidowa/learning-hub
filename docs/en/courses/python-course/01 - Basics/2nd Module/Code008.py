# Logical Operators
# In Python, we have three logical operators:
#     and
#     or
#     not

# and operator
# The and operator is used to check if two conditions are True
# if condition_1 and condition_2:
#     code

temperature = 30
wind_speed = 5
if temperature > 30 and wind_speed < 10:
    print("It's a hot day")
    print("Drink plenty of water")
else:
    print("It's not a hot day")
    print("Wear warm clothes")

# In this case, the temperature is greater than 30 and the wind speed is less than 10, so the code inside the if statement is executed

# You can have multiple conditions in the same if statement
# if condition_1 and condition_2 and condition_3:
#     code
# In these case, the computer will evaluate the conditions from left to right and in couple of two conditions
# This means that the computer will evaluate the first two conditions, and if they are True, it will evaluate the third condition
# If the first two conditions are False, the third condition will not be evaluated
# This is called short-circuit evaluation

# Lets see a case where we use boolean variables

high_income = True
good_credit = True
if high_income and good_credit:
    print("Eligible for loan")
else:
    print("Not eligible for loan")

# In this case, the high_income and good_credit variables are True, so the code inside the if statement is executed
# We ommit the comparison with True because the variables are already boolean variables
# If we want to compare the variables with True, we can do it like this

high_income = True
good_credit = True
if high_income == True and good_credit == True:
    print("Eligible for loan")
else:
    print("Not eligible for loan")

# However, this is not recommended because it is redundant


# or operator
# The or operator is used to check if at least one of the conditions is True
# if condition_1 or condition_2:
#     code

temperature = 30
wind_speed = 5
if temperature > 30 or wind_speed < 10:
    print("It's a hot day")
    print("Drink plenty of water")
else:
    print("It's not a hot day")
    print("Wear warm clothes")

# In this case, the temperature is greater than 30, so the code inside the if statement is executed
# In the or operator, if the first condition is True, the second condition is not evaluated

# One thing to keep in mind is that the and operator has precedence over the or operator
# This is called operator precedence
# This means that the computer will evaluate the and operator first, and then the or operator
# If you want to change the order of evaluation, you can use parentheses
# Lets see an example

high_income = True
temperature = 30
wind_speed = 5
if (temperature > 30 or wind_speed < 10) and high_income:
    print("It's a hot day")
    print("Drink plenty of water")
else:
    print("It's not a hot day")
    print("Wear warm clothes")

# In this case, the temperature is greater than 30, AND the high_income variable is True, so the code inside the if statement is executed

# not operator
# The not operator is used to invert the value of a boolean variable
# if not condition:
#     code

student = False
if not student:  # This is the same as if student == False
    print("Eligible for loan")
else:
    print("Not eligible for loan")

# In this case, the student variable is False, so the code inside the if statement is executed as the not operator inverts the value of the variable

# Chain comparison operators
# You can chain comparison operators
# Lets see an example

age = 22
if age >= 18 and age < 65:
    print("Eligible")

# In this case, the age variable is greater than or equal to 18, AND the age variable is less than 65, so the code inside the if statement is executed
# Another way to write this is

age = 22
if 18 <= age < 65:
    print("Eligible")

# In Python we can chain comparison operators like this as a mathematical expression
