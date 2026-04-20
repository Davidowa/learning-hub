import matplotlib.pyplot as plt
import math

# Function to plot a linear equation graph with specified x range
def plot_linear_equation(m, c, x_initial, x_end):
    x, y = [], []
    step = 0.1  # Define step size
    while x_initial <= x_end:
        x.append(x_initial)
        y.append(m * x_initial + c)
        x_initial += step

    plt.plot(x, y)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Graph of Linear Equation')
    plt.grid(True)
    plt.show()

# Function to plot exponential growth
def plot_exponential_growth(x_initial, x_end):
    x, y = [], []
    step = 0.1  # Define step size
    
    while x_initial <= x_end:
        x.append(x_initial)
        y.append(math.exp(x_initial))
        x_initial += step

    plt.plot(x, y)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Exponential Growth Function')
    plt.grid(True)
    plt.show()

# Function to plot sine and cosine waves
def plot_sine_cosine_waves(x_initial, x_end):
    x, y_sin, y_cos = [], [], []
    step = 0.1  # Define step size
    
    while x_initial <= x_end:
        x.append(x_initial)
        y_sin.append(math.sin(x_initial))
        y_cos.append(math.cos(x_initial))
        x_initial += step

    plt.plot(x, y_sin, label='sin(x)')
    plt.plot(x, y_cos, label='cos(x)')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Sine and Cosine Waves')
    plt.legend()
    plt.grid(True)
    plt.show()

# Function to plot a histogram of letter frequency in a string
def plot_letter_frequency(input_string):
    input_string = input_string.lower()
    letter_counts = {}
    for char in input_string:
        # char.isalpha() checks if the character is an alphabet
        if char.isalpha():
            if char in letter_counts:
                letter_counts[char] += 1
            else:
                letter_counts[char] = 1

    letters = list(letter_counts.keys())
    frequencies = list(letter_counts.values())

    plt.bar(letters, frequencies)
    plt.xlabel('Letters')
    plt.ylabel('Frequency')
    plt.title('Histogram of Letter Frequency')
    plt.grid(axis='y')
    plt.show()

# Function to implement the Collatz Conjecture and plot each step
def collatz_conjecture(n):
    # The Collatz Conjecture is a sequence defined as follows:
    # If n is even, divide it by 2
    # If n is odd, multiply it by 3 and add 1
    # Repeat the process until n becomes 1

    # Initialize the list with the starting number
    steps = [n] 
    
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        steps.append(n)
    
    plt.figure(figsize=(10, 8))
    plt.plot(steps, marker='o')
    plt.xlabel('Step')
    plt.ylabel('n')
    plt.title('Collatz Conjecture')
    plt.grid(True)
    plt.show()

# Function to calculate the GCD of two numbers using the Euclidean algorithm
def gcd(a, b):
    # The Euclidean algorithm is an efficient method for computing the greatest common divisor of two numbers
    # It is based on the principle that the greatest common divisor of two numbers does not change 
    # if the larger number is replaced by its difference with the smaller number

    # The algorithm is based on the fact that the GCD of two numbers also divides their difference
    # and any linear combination of the two numbers.
    while b: # While b is not 0, meaning there is a remainder and 0 in boolean is False and any positive number is True
        a, b = b, a % b
    return a

# Function to calculate the number of months to reach a savings goal
def savings_goal_tracker(starting_amount, monthly_savings, goal):
    months = 0
    current_savings = starting_amount
    while current_savings < goal:
        current_savings += monthly_savings
        months += 1
    return months

# Function to solve a quadratic equation
def solve_quadratic(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant >= 0:
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        return (root1, root2)
    else:
        real_part = -b / (2*a)
        imaginary_part = math.sqrt(-discriminant) / (2*a)
        return (complex(real_part, imaginary_part), complex(real_part, -imaginary_part))

# Function to check if a set of numbers is a Pythagorean triple
def is_pythagorean_triple(a, b, c):
    result = (a**2 + b**2 == c**2)
    return result

# Function to convert degrees to radians
def degrees_to_radians(degrees):
    return degrees * (math.pi / 180)

# Function to convert radians to degrees
def radians_to_degrees(radians):
    return radians * (180 / math.pi)

# Function to print the multiplication table of a number
def print_multiplication_table(N):
    for i in range(1, N+1):
        for j in range(1, N+1):
            print(f"{i*j}\t", end='')
        print()

# Function to calculate the BMI
def calculate_bmi(weight, height):
    return weight / (math.pow(height, 2))

# Function to calculate the area of a polygon
def polygon_area(sides, length):
    if sides < 3:
        return "Invalid polygon"
    elif sides == 3:
        return (math.sqrt(3) / 4) * length**2  # Area of an equilateral triangle
    elif sides == 4:
        return length**2  # Area of a square
    else:
        # General formula for regular polygons with more than 4 sides
        return (sides * (length ** 2)) / (4 * math.tan(math.pi / sides))

# Usage of the functions
# Example usage: Plotting Linear Equation y = 2x + 1, from x = -10 to x = 10
plot_linear_equation(2, 1, -10, 10)
# Example usage: Plotting Exponential Growth Function from x = -2 to x = 20
plot_exponential_growth(-2, 20)
# Example usage: Plotting Sine and Cosine Waves from x = -π to x = π
plot_sine_cosine_waves(-math.pi, math.pi)
# Example usage: Plot letter frequency in a string
plot_letter_frequency("Example string with multiple letter counts.")
# Example usage: Plotting Collatz Conjecture for n = 27
collatz_conjecture(27)
# Example usage: Calculate the GDC of 48 and 180
print(f"The GDC of 48 and 180 is {gcd(48, 180)}")  # Should return 12
# Example usage: Calculate the number of months to reach a savings goal
print(f"To save 5000, starting with 1000 and making savings of 500, it would take {savings_goal_tracker(1000, 500, 5000)} months to reach the goal.")  # Should return 8
# Example usage: Calculate the roots of a quadratic equation
print(solve_quadratic(1, 0, -1))  # Should handle real roots
print(solve_quadratic(1, 0, 1))  # Should handle complex roots
# Example usage: Check if a set of numbers is a Pythagorean triple
print(is_pythagorean_triple(3, 4, 5))  # Should return True
print(is_pythagorean_triple(5, 9, 11))  # Should return False
# Example usage: Convert between degrees and radians
print(degrees_to_radians(180))  # Should return π
print(radians_to_degrees(math.pi))  # Should return 180
# Example usage: Print the multiplication table of 5
print_multiplication_table(5)
# Example usage: Calculate the BMI
print(calculate_bmi(70, 1.75))  # Should return the BMI
# Example usage: Calculate the area of a polygon
print(polygon_area(3, 10))  # Triangle
print(polygon_area(4, 10))  # Square
print(polygon_area(5, 10))  # Pentagon

from datetime import datetime

def gregorian_to_approx_lunar(year, month, day):
    # Define a base date for which we know the lunar date. 
    # This is purely illustrative and not based on any real lunar calendar system.
    # Let's assume January 1, 2000, corresponds to the 1st day of a lunar month.
    base_date = datetime(2000, 1, 1)
    target_date = datetime(year, month, day)

    # Calculate the difference between the target date and the base date
    delta = target_date - base_date

    # Assuming an average lunar month is about 29.53 days
    lunar_month_length = 29.53

    # Calculate the elapsed lunar months and days since the base date
    elapsed_lunar_months = int(delta.days / lunar_month_length)
    elapsed_days = delta.days % lunar_month_length

    # Calculate the approximate lunar year, month, and day
    # This is a very rough approximation, assuming 12 lunar months per year
    lunar_year = 2000 + elapsed_lunar_months // 12
    lunar_month = elapsed_lunar_months % 12 + 1  # Adding 1 to make the month 1-indexed
    lunar_day = int(elapsed_days) + 1  # Adding 1 to make the day 1-indexed

    return lunar_year, lunar_month, lunar_day

# Example usage:
year, month, day = 2024, 2, 19  # Example Gregorian date
lunar_year, lunar_month, lunar_day = gregorian_to_approx_lunar(year, month, day)
print(f"Gregorian Date: {year}-{month}-{day} => Approximate Lunar Date: {lunar_year}-{lunar_month}-{lunar_day}")
