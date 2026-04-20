# Functions

# When you write a code, you may hundreds or thousands lines of code
# You shouldn't write all the code in one block
# It is better to divide the code into blocks

# Functions are a block of code which only runs when it is called
# Functions are used to reuse code: define the code once, and use it many times
# Functions are used to have more manageable code: divide the code into blocks
# Functions are better to mantaing and debug because you can focus on one part of the code at a time

# Syntax
# def function_name(parameters):
#     code

# Example
def my_function():
    print("Hello from a function")


my_function()  # Hello from a function

# In this example, we define a function named my_function, which prints a message on the screen
# Then we call the function, which prints the message on the screen

# You can pass data, known as parameters, into a function
# Parameters are specified after the function name, inside the parentheses
# You can add as many parameters as you want, just separate them with a comma
# The following example has a function with one parameter (fname)
# When the function is called, we pass along a first name, which is used inside the function to print the full name
# Example


def print_fullname(first_name):
    print(first_name + " Doe")


print_fullname("John")  # John Doe

# We have mentioned that Python does not require you to specify the type of the variable
# However, you can specify the type of the parameter
# This is useful for documentation, and also for checking if the function is called with the correct type of arguments
# Example


def print_age(age: int):
    print("Age:", age)


print_age(20)  # Age: 20

# You can specify a default value for a parameter
# Whenever you define a default value for a parameter, the parameter becomes optional
# This means that if the function is called without the argument, the default value will be used
# Example


def print_country(country="Norway"):
    print("Country:", country)


print_country("Sweden")  # Country: Sweden
print_country("India")  # Country: India
print_country()  # Country: Norway

# You can specify the data type of the default value
# Example


def print_city(city: str = "Mexico City"):
    print("City:", city)


print_city("Oslo")  # City: Oslo
print_city("Bergen")  # City: Bergen
print_city()  # City: Mexico City

# If you assign a default value to a parameter, all the parameters to the right must also have a default value
# Example


def print_name(first_name: str, last_name: str = "Doe"):
    print(first_name, last_name)


print_name("Jane", "Doe")  # Jane Doe
print_name("John")  # John Doe

# Another example


def print_person_data(age: int, first_name: str = "John", last_name: str = "Doe"):
    print(f"Age: {age}, First name: {first_name}, Last name: {last_name}")


# Age: 20, First name: Jane, Last name: Doe
print_person_data(20, "Jane", "Doe")
# Age: 22, First name: Elizabeth, Last name: Doe
print_person_data(22, "Elizabeth")
# Age: 25, First name: John, Last name: Doe
print_person_data(25)

# Whenever you define a default value for a parameter, the next parameters to the right must also have a default value, and so on

# Moreover, you can return a value from a function
# Example


def square(number: int):
    return number * number


print(square(2))  # 4

# In this example, we define a function named square, which returns the square of the number passed as an argument
# Then we call the function, which returns the square of the number passed as an argument
# The return statement returns a value back to the caller

# You can return multiple values from a function using the return statement
# Example


def square_and_cube(number: int):
    return number * number, number * number * number


print(square_and_cube(2))  # (4, 8)

# In this example, we define a function named square_and_cube, which returns the square and cube of the number passed as an argument

# The same as the parameters, you can specify the type of the return value
# Example


def cube(number: int) -> int:
    return number * number * number

# In this example, we define a function named cube, which returns the cube of the number passed as an argument, and we specify that the return value is an integer

# For functions that does not return a value, the return statement can be omitted or specified as None, which is the default value
# Example


def print_name(first_name: str, last_name: str) -> None:
    print(first_name, last_name)


# You can store the return value in a variable
# Example


def rectangle_area(b: float, h: float) -> float:
    return b * h


area = rectangle_area(2, 3)
print(area)  # 6


# When you return multiple values from a function, you can store the return values in multiple variables
# Example


# tuple is a data type that can store multiple values, ignore it for now
def rectangle_triangle_area(b: float, h: float) -> tuple:
    return b * h, 0.5 * b * h


area1, area2 = rectangle_triangle_area(2, 3)  # 6, 3

# Lasty, you can use keywqord arguments to make the code more readable
# When you use keyword arguments in a function call, the caller identifies the arguments by the parameter name
# Example


def increment(number: int, by: int) -> int:
    return number + by


print(increment(2, 1))
print(increment(2, by=1))  # better
print(increment(number=2, by=1))  # much better
