# Fizz buzz algorithm
# The fizz buzz algorithm is a common programming interview question
# The question is as follows:
# Write a program that prints the numbers from 1 to 100
# But for multiples of three print "Fizz" instead of the number
# And for the multiples of five print "Buzz"
# For numbers which are multiples of both three and five print "FizzBuzz"

def fizz_buzz() -> str:
    for number in range(1, 101):
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz")
        elif number % 3 == 0:
            print("Fizz")
        elif number % 5 == 0:
            print("Buzz")
        else:
            print(number)


def evaluate_fizz_buzz(number: int) -> str:
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)


fizz_buzz()
print()
evaluate_fizz_buzz(15)
