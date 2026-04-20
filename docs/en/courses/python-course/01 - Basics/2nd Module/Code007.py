# Conditional Statements
# Conditional staments are used to make decisions

# The if statement is used to check a condition, and execute a code if the condition is True
# if statement
# if condition:
#     code

temperature = 20
if temperature > 30:
    print("It's a hot day")
    print("Drink plenty of water")
print("Done")

# In this case, if the temperature is greater than 30, the code inside the if statement is executed
# If the temperature is less than 30, the code inside the if statement is not executed
# Therefore, if we have a temperature of 10, nothing is printed. Let see this

temperature = 10
if temperature > 30:
    print("It's a hot day")
    print("Drink plenty of water")
print("Done")

# In this case, we declared the variable temperature and because its value is less than 30 nothing is printed in the console

# if else statement
# The else statement is used to execute a code if the condition of the if statement is False
# if condition:
#     code
# else:
#     code

temperature = 20
if temperature > 30:
    print("It's a hot day")
    print("Drink plenty of water")
else:
    print("It's a cold day")
    print("Wear warm clothes")
print("Done")

# The elif statement is used to check another condition if the condition of the if statement is False
# We can have multiple elif statements. This is useful when we have multiple conditions to check
# if elif else statement
# if condition:
#     code
# elif condition:
#     code
# else:
#     code

temperature = 20
if temperature > 30:
    print("It's a hot day")
    print("Drink plenty of water")
elif temperature > 20:
    print("It's a nice day")
elif temperature > 10:
    print("It's a bit cold")
else:
    print("It's a cold day")
    print("Wear warm clothes")
print("Done")

# In the elif statement, the else statement is not necessary, this is optional.
# Usually, we use the else statement to catch all the other cases that are not covered by the if and elif statements
# It is usually a good idea to have an else statement at the end of the if statement, as this is going to be the default case

# Its important to note that the code inside the if statement is indented
# In Python, the indentation is very important
# This indentation is done with the Tab key

# The code inside the if statement is called a block of code
# All the code inside the block of code must be indented
# If the condition is True, the block of code is executed

# The code outside the if statement is not indented
# Therefore, it is not part of the block of code

# Lastly, we have a special operator called the ternary operator
# This operator is used to simplify the if statement
# The ternary operator is a one line if statement
# ternary operator
# condition_if_true if condition else condition_if_else

age = 22
message = "Eligible" if age >= 18 else "Not eligible"  # Eligible

# The ternary operator is used to assign a value to a variable based on a condition
# In this case, if the age is greater than or equal to 18, the value of the message variable is going to be "Eligible"

# The equivalent if statement is the following:
age = 12
if age >= 18:
    message = "Eligible"
else:
    message = "Not eligible"
