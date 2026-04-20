# In this code, we will learn how to generate random values in Python
# We have the random module in Python that allows us to work with random values

from string import ascii_letters, digits
from random import random, randint, choice, choices, shuffle

print(random())  # This will print a random float between 0 and 1
print(randint(1, 10))  # This will print a random integer between 1 and 10
print(choice([1, 2, 3, 4, 5]))  # This will print a random value from the list
# This will print a list of 2 (k-value) random values from the list
print(choices([1, 2, 3, 4, 5], k=2))

# Choises method is usefull if we want to generate random values, for instance a password
# Example
# This will print a list of 4 random characters from the string
print(choices("abcdefgh", k=4))
# however, this will print a list of 4 random characters from the string

# To obtain a string, we can use the join method
# Example
# This will print a string of 4 random characters from the string
print("".join(choices("abcdefgh", k=4)))
# This will print a string of 4 random characters from the string
# The "" means that we want to join the list of characters without any separator, you can use any separator you want (, - _ etc.)

# But lets imagine we want a password with 8 characters, 4 letters and 4 digits
# it would be tedious to write all the letters and digits, so we can use the ascii_letters and digits from the string module

print("".join(choices(ascii_letters + digits, k=8)))
# This will print a string of 8 random characters from the string

# We can also the random module to shuffle a list using the shuffle method
# Example
numbers = [1, 2, 3, 4, 5]
shuffle(numbers)
print(numbers)  # This will print a shuffled list of numbers
