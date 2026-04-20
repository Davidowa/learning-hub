# Data Structures

# Lists
# Lists are used to store multiple items in a single variable.
# Lists are created using square brackets:
# Example
fruits = ["apple", "banana", "cherry"]

# Values in a list are called items or elements. They can have any type.
# Example
fruits = ["apple", "banana", "cherry", 1, 2, 3, True, False, None]

# Lists are ordered, changeable, and allow duplicate values.
# List items are indexed, the first item has index [0], the second item has index [1] etc.
# Example
print(fruits[1])  # banana

# Negative indexing means start from the end
# -1 refers to the last item, -2 refers to the second last item etc.
# Example
print(fruits[-1])  # None

# Range of Indexes
# You can specify a range of indexes by specifying where to start and where to end the range.
# When specifying a range, the return value will be a new list with the specified items.
# Example
print(fruits[1:3])  # ['banana', 'cherry']

# By leaving out the start value, the range will start at the first item:
# Example
print(fruits[:2])  # ['apple', 'banana']

# By leaving out the end value, the range will go on to the end of the list:
# Example
print(fruits[1:])  # ['banana', 'cherry', 1, 2, 3, True, False, None]

# Range of Negative Indexes
# Specify negative indexes if you want to start the search from the end of the list:
# Example
print(fruits[-3:-1])  # [True, False]

# Step - You can specify the step, which tells you how many items to return.
# Example
fruits = ["apple", "banana", "cherry", "blackcurrant"]
print(fruits[::2])  # ['apple', 'cherry']

# Change Item Value
# To change the value of a specific item, refer to the index number:
# Example
fruits[1] = "blackcurrant"
print(fruits)  # ['apple', 'blackcurrant', 'cherry', 'blackcurrant']

# Loop Through a List
# You can loop through the list items by using a for loop:
# Example
for fruit in fruits:
    print(fruit)

# Check if Item Exists
# To determine if a specified item is present in a list use the in keyword:
# Example
if "apple" in fruits:
    print("Yes, 'apple' is in the fruits list")

# List Length
# To determine how many items a list has, use the len() function:
# Example
print(len(fruits))  # 4

# Add Items
# To add an item to the end of the list, use the append() method:
# Example
fruits.append("orange")
print(fruits)  # ['apple', 'blackcurrant', 'cherry', 'blackcurrant', 'orange']

# To add an item at the specified index, use the insert() method:
# Example
fruits.insert(1, "lemon")
# ['apple', 'lemon', 'blackcurrant', 'cherry', 'blackcurrant', 'orange']
print(fruits)

# Remove Item
# There are several methods to remove items from a list:
# Example
fruits.remove("lemon")
print(fruits)  # ['apple', 'blackcurrant', 'cherry', 'blackcurrant', 'orange']

# The pop() method removes the specified index, (or the last item if index is not specified):
# Example
fruits.pop()
print(fruits)  # ['apple', 'blackcurrant', 'cherry', 'blackcurrant']

# The del keyword removes the specified index:
# Example
del fruits[0]
print(fruits)  # ['blackcurrant', 'cherry', 'blackcurrant']

# The del keyword can also delete the list completely:
# Example
# del fruits
# print(fruits) # name 'fruits' is not defined

# The clear() method empties the list:
# Example
fruits.clear()
print(fruits)  # []

# Copy a List
# You cannot copy a list simply by typing list2 = list1, because: list2 will only be a reference to list1
# And changes made in list1 will automatically also be made in list2. - More about references in a later module
# There are ways to make a copy, one way is to use the built-in List method copy().
# Example
fruits = ["apple", "banana", "cherry"]
fruits2 = fruits.copy()
print(fruits2)  # ['apple', 'banana', 'cherry']

# Another way to make a copy is to use the built-in method list().
# Example
fruits3 = list(fruits)
print(fruits3)  # ['apple', 'banana', 'cherry']

# Join Two Lists
# There are several ways to join, or concatenate, two or more lists in Python.
# One of the easiest ways are by using the + operator.
# Example
fruits4 = fruits + fruits2
print(fruits4)  # ['apple', 'banana', 'cherry', 'apple', 'banana', 'cherry']

# Another way to join two lists are by appending all the items from list2 into list1, one by one:
# Example
fruits = ["apple", "banana", "cherry"]
for fruit in fruits2:
    fruits.append(fruit)
print(fruits)  # ['apple', 'banana', 'cherry', 'apple', 'banana', 'cherry']

# Or you can use the extend() method, which purpose is to add elements from one list to another list:
# Example
fruits = ["apple", "banana", "cherry"]
fruits.extend(fruits2)
print(fruits)  # ['apple', 'banana', 'cherry', 'apple', 'banana', 'cherry']

# The list() Constructor
# It is also possible to use the list() constructor to make a new list.
# Example
fruits = list(("apple", "banana", "cherry"))  # note the double round-brackets
print(fruits)  # ['apple', 'banana', 'cherry']

# List Methods
# Python has more of built-in methods that you can use on lists.
# Method	Description
# count()	Returns the number of elements with the specified value
fruits.count("apple")  # 2

# index()	Returns the index of the first element with the specified value
fruits.index("banana")  # 1
# Note: The index() method only returns the first occurrence of the value.
# Moreover, if the item does not exist, it will raise an error.


# reverse()	Reverses the order of the list
fruits.reverse()  # ['cherry', 'banana', 'apple']

# sort()	Sorts the list
fruits.sort()  # ['apple', 'banana', 'cherry']

# sorted()	Returns a sorted list
new_fruits = sorted(fruits)  # ['apple', 'banana', 'cherry']

# List Unpacking
# Unpoacking is a way to assign the values of a list to a group of variables.
# If you have a list of values and a variable number of variables, you can assign the list to the variables.
# Example
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)  # apple
print(y)  # banana
print(z)  # cherry

# If you do not have enough variables to unpack the list, this will cause an error.
# Example
# fruits = ["apple", "banana", "cherry"]
# x, y = fruits  # too many values to unpack

# You can add an * to the variable name and the values will be assigned to the variable as a list.
# Example
fruits = ["apple", "banana", "cherry", "strawberry", "raspberry"]
x, y, *z = fruits


# You can have a list inside another list.
# Example
fruits = ["apple", "banana", "cherry", ["blackcurrant", "orange"]]
print(fruits[3][1])  # orange
# In this example, we use the first index to access the element inside a list, in this case 3 is the index of the nested list
# The second index to access the value inside the nested list.

# Lastly, it is worth nothing that a list can be created using iterable objects.
# Example
# This will create a list of numbers from 1 to 9
numbers = list(range(1, 10))

# This will create a list of characters from the string "Hello World"
chars = list("Hello World")
