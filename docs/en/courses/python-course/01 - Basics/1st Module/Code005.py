# You can use input() function to get input from the user
# A string that you pass to the input function will be displayed in the console
# We always have to store the input in a variable because the input function returns a string
# If you dont store the input in a variable you wont be able to access the input value
# Remember that variables store values
name = input("What is your name? ")
print("Hi " + name)  # If you input John, it will print Hi John

# Type conversion
# If you want to convert a string to an integer you can use the following syntax
x = input("x: ")
x = int(x)
# Or
x = int(input("x: "))  # This is the same as the previous code

# If you want to convert a string to a float you can use the following syntax
x = float(input("x: "))

# If you want to convert a string to a boolean you can use the following syntax
# This will always return True because the input function returns a string
x = bool(input("x: "))
print(x)
# In python we have something that is called falsy values and truthy values

# Falsy values are:
# "" - empty string
# 0
# None
# []
# False

# Truthy values are:
# Everything else that is not falsy

# The type() function will return the type of the variable
# For example if you want to know the type of the variable x you can use the following syntax
x = 1
type(x)  # <class 'int'>

# If you want to convert a number to a string you can use the following syntax
x = 1
str(x)  # "1"

# If we want to print a string and a number we have to convert the number to a string
# For example if you want to print the following string
# I am 1 year old
# You can use the following syntax
age = 1
print("I am " + str(age) + " year old")  # I am 1 year old
# Or
print(f"I am {age} year old")  # I am 1 year old
