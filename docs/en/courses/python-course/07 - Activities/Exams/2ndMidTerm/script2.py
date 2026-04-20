# 1. Define a function named `read_numbers` that opens and
# reads the contents of a file named `values.txt`.
# This file contains two numbers separated by a dash (-).
# The function should split these numbers, convert them to integers,
# and return them as two separate values.

filepath = "./07 - Activities/Exams/2ndMidTerm/"
filename = "values.txt"


def read_numbers() -> tuple:
    with open(filepath + filename, "r") as file:
        # Read the contents of the file and store them in the 'menu' list
        data = file.readline().strip().split("-")

        return int(data[0]), int(data[1])


# 2. Call the `read_numbers` function and store the
# returned values in two variables, `num1` and `num2`.
num1, num2 = read_numbers()

# 3. Define another function named `perform_operations` that takes two parameters.
# These parameters will be the variables where you stored the numbers from the file.
# 4. Within the `perform_operations` function, implement code to print the results
# of the following arithmetic operations:
#    1. Addition (`num1` + `num2`).
#    2. Subtraction (`num1` - `num2`).
#    3. Multiplication (`num1` * `num2`).
#    4. Division (`num1` / `num2`).
#    5. Modulus (`num1` % `num2`).


def perform_operations(n1: int, n2: int) -> None:
    print(f"Addition: {n1} + {n2} = {n1 + n2}")
    print(f"Subtraction: {n1} - {n2} = {n1 - n2}")
    print(f"Multiplication: {n1} * {n2} = {n1 * n2}")
    # The :.2f formats the number to 2 decimal places
    print(f"Division: {n1} / {n2} = {n1 / n2:.2f}")
    print(f"Modulus: {n1} % {n2} = {n1 % n2}")


# 5. Call `perform_operations` using `num1` and `num2` as arguments to
# display the results of the arithmetic operations.
perform_operations(num1, num2)
