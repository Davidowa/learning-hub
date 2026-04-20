import timeit
import time

# When writing applications, many things can go wrong.
# For example, a user may provide invalid input.
# Or a file may not exist.
# Or the network may be down.
# In each of these cases, an error occurs.
# And if you don't handle the error, the program will crash.

# To handle errors, we use try and except statements.
# The try block contains code that may raise an error.
# And the except block contains code to handle the error.
# Let's see an example.
age = int(input("Age: "))
print(age)

# # If we enter a string, we get an error.
# # ValueError: invalid literal for int() with base 10: 'a'

# # To handle this error, we use a try and except statement.
try:
    age = int(input("Age: "))
    print(age)
except Exception:
    print("Invalid value")

# # If we enter a string, we get the message "Invalid value".

# To know the type of error, you can use the "as" keyword.
# Let's see an example.

try:
    age = int(input("Age: "))
    print(age)
except Exception as ex:
    print(type(ex))

# Once we know the type of error, we can properly handle it.

# # To handle this error, we use a try and except statement.
try:
    age = int(input("Age: "))
    print(age)
except ValueError:
    print("Invalid value")

# You can also print the error message.
# Let's see an example.

try:
    age = int(input("Age: "))
    print(age)
except ValueError as ex:
    print("Invalid value")
    print("Error:", ex)

# If we want to handle different types of errors, we can use multiple except statements.
# Let's see an example.

try:
    age = int(input("Age: "))
    print(age)
    xfactor = 10 / age
except ValueError:
    print("Invalid value")
except ZeroDivisionError:
    print("Age cannot be 0")

# # If we enter a string, we get the message "Invalid value".
# # If we enter 0, we get the message "Age cannot be 0".

# If you want to show the same message for different types of errors, you can use a tuple.
# Let's see an example.

try:
    age = int(input("Age: "))
    print(age)
    xfactor = 10 / age
except (ValueError, ZeroDivisionError):
    print("Invalid value")

# You can also use else and finally statements.
# Let's see an example.

try:
    age = int(input("Age: "))
    print(age)
    xfactor = 10 / age
except ValueError:
    print("Invalid value")
except ZeroDivisionError:
    print("Age cannot be 0")
else:
    print("No exceptions were thrown")
finally:
    print("Execution completed")

# # If we enter a string, we get the message "Invalid value".
# # If we enter 0, we get the message "Age cannot be 0".
# # If we enter a valid age, we get the message "No exceptions were thrown".
# # And finally, we get the message "Execution completed".

# You can also create your own exceptions.
# https://docs.python.org/3/library/exceptions.html#exception-hierarchy
# Let's see an example.


def calculate_xfactor(age):
    if age <= 0:
        raise ValueError("Age cannot be 0 or less.")
    return 10 / age


try:
    calculate_xfactor(-1)
except ValueError as error:
    print(error)

# It is not advisable to use exceptions to control the flow of your program.
# An important thing to note is that when you raise an exception, the performace of your program will be affected.

# Lets evaluate the performance of our program.
# We will use the timeit module.

# # The timeit module provides a simple way to time small bits of Python code.

code1 = """
def calculate_xfactor(age):
    if age <= 0:
        raise ValueError("Age cannot be 0 or less.")
    return 10 / age

try:
    calculate_xfactor(-1)
except ValueError as error:
    print(error)
"""

# Its better to use if statements to control the flow of your program.

code2 = """
def calculate_xfactor(age):
    if age <= 0:
        return None
    return 10 / age

xfactor = calculate_xfactor(-1)
if xfactor == None:
    print("Age cannot be 0 or less.")
"""

# The number parameter is the number of executions.
# print("First code:", timeit.timeit(code1, number=10000)) # 0.865
# print("Second code:", timeit.timeit(code2, number=10000)) # 0.854

# If you change the codes to pass the try and except statements, you will see that the performance is affected.

code1 = """
def calculate_xfactor(age):
    if age <= 0:
        raise ValueError("Age cannot be 0 or less.")
    return 10 / age

try:
    calculate_xfactor(-1)
except ValueError as error:
    pass
"""

code2 = """
def calculate_xfactor(age):
    if age <= 0:
        return None
    return 10 / age

xfactor = calculate_xfactor(-1)
if xfactor == None:
    pass
"""

# The number parameter is the number of executions.
print("First code:", timeit.timeit(code1, number=10000))  # 0.015
print("Second code:", timeit.timeit(code2, number=10000))  # 0.009

# We obtain a better performance when we use if statements to control the flow of our program.

# Another way to time your code is to use the time module.
# The time module provides various time-related functions.

# time.time() returns the number of seconds since the epoch, which means the time since 00:00:00 UTC on 1 January 1970.
# The epoch can vary on different operating systems, but it is commonly January 1, 1970.

# Lets simulate we want to send emails to 10,000 users.
# We will use the time module to evaluate the performance of our program.


def send_emails():
    for i in range(10000):
        pass


start = time.time()
send_emails()
end = time.time()
duration = end - start
print(duration)
