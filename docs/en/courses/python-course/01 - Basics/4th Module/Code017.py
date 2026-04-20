# Bonus topics are not required to complete the course, but they are recommended to get a deeper understanding of the language

from sys import getsizeof
from collections import deque

# * args - xargs

# In functions that accept a variable number of arguments, you can use the *args syntax to specify a variable number of positional arguments
# Example


def sum(*numbers: tuple) -> int:  # In this case *numbers is a tuple
    total = 0
    for number in numbers:
        total += number
    return total


print(sum(1, 2, 3, 4, 5))  # 15

# In this example, we define a function named sum, which accepts a variable number of arguments and returns the sum of the arguments

# **args - xxargs

# We have a similar syntax for keyword arguments, which is **args
# Example


def save_user(**user):
    print(user)
    print(user["id"])
    print(user["name"])
    print(user["age"])


save_user(id=1, name="John", age=22)  # {'id': 1, 'name': 'John', 'age': 22}

# In this example, we define a function named save_user, which accepts a variable number of keyword arguments and prints them
# The **args syntax is used to pass a variable number of keyword arguments to a function, which is stored in a dictionary


# enumerate in for loop
# Example
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):  # enumerate returns a tuple
    print(index, fruit)

# 0 apple, 1 banana, 2 cherry
# You use enumarate to get the index of the item in the list


# Lambda Functions
# A lambda function is also called an anonymous function, this is a function that does not have a name
# Lets take the following example. Lets define a list of tuples, where each tuple contains a product name and a corresponding price
# Example
products = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12),
]

# Now, lets sort this list by price. To do that, we can use the sort method of the list class
# Example
print(products)  # [('Product1', 10), ('Product2', 9), ('Product3', 12)]
products.sort()
print(products)  # [('Product1', 10), ('Product2', 9), ('Product3', 12)]

# Notice that this will not be sorted

# We can use a lambda function to specify the sorting key
# The key parameter in sort method accepts a function that returns the value that we want to sort by
# product is a tuple, and we are sorting by the second item in the tuple which is the price
products.sort(key=lambda product: product[1])
print(products)

# Lets say we want to add 10 to an argument and return the result
# Example


def add_10(x): return x + 10


print(add_10(1))  # 11

# Now lets say we want to add two numbers and return the result
# Example


def add(x, y): return x + y


print(add(5, 10))  # 15

# We can also use lambda in functions that accept a variable number of arguments
# Example


def myfunc(n):
    return lambda a: a * n


# In this case, the lambda function returns a function that multiplies a number by n
# So if we call this function with 2, it will return a function that multiplies a number by 2
# Example
mydoubler = myfunc(2)  # mydoubler is a function that multiplies a number by 2
mytripler = myfunc(3)  # mytripler is a function that multiplies a number by 3

print(mydoubler(11))  # 22
print(mytripler(11))  # 33


# Map function
# The map function is used to apply a function to each item in an iterable object
# Lets use the products list that we defined earlier
# Example
products = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12),
]


# Lets say we want to get the price of each product in a new list
# Example
prices = []
for product in products:
    prices.append(product[1])
print(prices)  # [10, 9, 12]

# However, we can use the map function to do this in a more elegant way
prices = list(map(lambda product: product[1], products))
print(prices)  # [10, 9, 12]


# Lets take another example. Lets we want to add 10 to each item in the list
# Example
numbers = [1, 2, 3, 4, 5]
print(numbers)  # [1, 2, 3, 4, 5]
numbers_plus10 = list(map(lambda number: number + 10, numbers))
print(numbers_plus10)  # [11, 12, 13, 14, 15]


# Filter function
# The filter function is used to filter an iterable object
# Lets take the products list that we defined earlier
# Example
products = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12),
]

# Lets say we want to get the products that are more expensive than 10
# Example
filtered = []
for product in products:
    if product[1] >= 10:
        filtered.append(product)
print(filtered)  # [('Product1', 10), ('Product3', 12)]

# However, we can use the filter function to do this in a more elegant way
filtered = list(filter(lambda product: product[1] >= 10, products))
print(filtered)  # [('Product1', 10), ('Product3', 12)]


# Comprehensions
# Comprehensions are a way to create lists, dictionaries and sets
# Lets take the following example. Lets define a list of numbers
# Example
numbers = [1, 2, 3, 4, 5]

# Lets say we want to create a new list that contains the square of each number in the list
# Example
squares = []
for number in numbers:
    squares.append(number ** 2)
print(squares)  # [1, 4, 9, 16, 25]

# However, we can use comprehensions to do this in a more elegant way
# Example
squares = [number ** 2 for number in numbers]
print(squares)  # [1, 4, 9, 16, 25]

# The syntax is as follows:
# [expression for item in iterable]

# Lets go back to the products list that we defined earlier
# Example
products = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12),
]

# Lets say we want to create a new list that contains the name of each product in the list
# Example
names = [product[0] for product in products]
print(names)  # ['Product1', 'Product2', 'Product3']

# Now the prices
prices = [product[1] for product in products]  # The same as map
print(prices)  # [10, 9, 12]

# Now lets do a filter with comprehensions
# Lets say we want to get the products that are more expensive than 10
# The same as filter
filtered = [product for product in products if product[1] >= 10]
print(filtered)  # [('Product1', 10), ('Product3', 12)]


# Dictionaries Comprehensions
# Example

my_family = {
    "child1": {
        "name": "Emil",
        "year": 2004
    },
    "child2": {
        "name": "Tobias",
        "year": 2007
    },
    "child3": {
        "name": "Linus",
        "year": 2011
    }
}

my_family = {k: v for (k, v) in my_family.items() if v["year"] > 2004}
# {'child2': {'name': 'Tobias', 'year': 2007}, 'child3': {'name': 'Linus', 'year': 2011}}
print(my_family)

# Generator Expressions
# Generator expressions are similar to comprehensions, but they do not store the list in memory
# Lets take the following example. Lets define a list of numbers
# Example
numbers = [1, 2, 3, 4, 5]

# Lets say we want to create a new list that contains the square of each number in the list
# Example
squares = []
for number in numbers:
    squares.append(number ** 2)
print(squares)  # [1, 4, 9, 16, 25]

# However, we can use generator expressions to do this in a more elegant way
# Example

squares = (number ** 2 for number in numbers)
print(squares)  # <generator object <genexpr> at 0x7f8f4b4a4b30>

# The important thing about generator expressions is that they do not store the list in memory
# Lets see the size of memory that the following generator and comprehension take

# Generator
values = (x * 2 for x in range(100000))
print("gen:", getsizeof(values))  # gen: 112

# Comprehension
values = [x * 2 for x in range(100000)]
print("com:", getsizeof(values))  # com: 824456

# This is the main difference between generator expressions and comprehensions
# Therefore, if you have a big set of data, you can use generator expressions to save memory

# Unpacking Operator

# The unpacking operator is used to unpack an iterable object into individual elements
# Lets take the following example. Lets define a list of numbers
# Example
numbers = [1, 2, 3]

# Lets say we want to pass these numbers as arguments to a function
# Example
print(numbers)  # [1, 2, 3]
print(*numbers)  # 1 2 3

# Lets take another example. Lets define a list of numbers
# Example
numbers = [1, 2, 3]

# Lets say we want to add these numbers to another list
# Example
new_numbers = [4, 5, 6]
numbers.append(new_numbers)
print(numbers)  # [1, 2, 3, [4, 5, 6]]

# However, we can use the unpacking operator to do this in a more elegant way
# Example
numbers = [1, 2, 3]
new_numbers = [4, 5, 6]
numbers.append(*new_numbers)
print(numbers)  # [1, 2, 3, 4, 5, 6]

# Lets take another example. Lets define a list of numbers
# Lets say we want to add these numbers to another list
# However, we can use the unpacking operator to do this in a more elegant way
# Example
numbers = [1, 2, 3]
new_numbers = [4, 5, 6]
numbers = [*numbers, *new_numbers]
print(numbers)  # [1, 2, 3, 4, 5, 6]

# Lets take another example. Lets define a list of numbers
# Lets say we want to add these numbers to another list
# However, we can use the unpacking operator to do this in a more elegant way
# Example
numbers = [1, 2, 3]
new_numbers = [4, 5, 6]
numbers = [*numbers, "a", *new_numbers, *"hello"]
print(numbers)  # [1, 2, 3, 'a', 4, 5, 6, 'h', 'e', 'l', 'l', 'o']

# Lastly, we can use the unpacking operator to unpack a dictionary
# Example
first = {"x": 1}
second = {"x": 10, "y": 2}
combined = {**first, **second, "z": 1}
print(combined)  # {'x': 10, 'y': 2, 'z': 1}

# Zip function
# The zip function is used to combine two or more iterables into a single iterable
# Lets take the following example. Lets define two lists
# Example
list1 = [1, 2, 3]
list2 = [10, 20, 30]

# Lets say we want to combine these two lists into a single list
# Example
combined = []
for i in range(len(list1)):
    combined.append((list1[i], list2[i]))
print(combined)  # [(1, 10), (2, 20), (3, 30)]

# However, we can use the zip function to do this in a more elegant way
# Example
combined = list(zip(list1, list2))

# The syntax is as follows:
# zip(iterable1, iterable2, iterable3, ...)

# But what happens if the two lists have different lengths?
# Example
list1 = [1, 2, 3]
list2 = [10, 20, 30, 40, 50]

combined = list(zip(list1, list2))
print(combined)  # [(1, 10), (2, 20), (3, 30)]
# Notice that the zip function will only combine the items that have the same index

# Stack
# A stack is a data structure that follows the Last In First Out (LIFO) principle
# The last item to be inserted into the stack is the first one to be removed
# Lets imagine you are navigating a website, and you click on a link, and then another link, and then another link
# These links are added to a stack
# When you click the back button, the last link you clicked is removed from the stack
# Example
browsing_session = []
browsing_session.append(1)
browsing_session.append(2)
browsing_session.append(3)
print(browsing_session)  # [1, 2, 3]
last = browsing_session.pop()
print(last)  # 3
print(browsing_session)  # [1, 2]

# To avoid getting an error when popping an empty stack, you can check if the stack is empty before popping
# Example
if not browsing_session:  # If the stack is empty
    browsing_session.pop()


# Queue
# A queue is a data structure that follows the First In First Out (FIFO) principle
# The first item to be inserted into the queue is the first one to be removed
# Lets imagine you are printing documents on a printer
# The documents are added to a queue
# The first document to be added to the queue is the first one to be printed
# Example
# We can use the deque class from the collections module to implement a queue
queue = deque([])
queue.append(1)
queue.append(2)
queue.append(3)
print(queue)  # deque([1, 2, 3])
first = queue.popleft()
print(first)  # 1
print(queue)  # deque([2, 3])

if not queue:  # If the queue is empty
    print("Empty")
