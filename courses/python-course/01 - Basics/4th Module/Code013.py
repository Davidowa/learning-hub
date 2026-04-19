# Tuples
# A tuple is a collection which is ordered and unchangeable. In Python tuples are written with round brackets.
# It is basic a read-only list
# Example
this_tuple = ("apple", "banana", "cherry")
print(this_tuple)  # ('apple', 'banana', 'cherry')

# You can access tuple items by referring to the index number, inside square brackets
# Example
this_tuple = ("apple", "banana", "cherry")

print(this_tuple[1])  # banana

# You can also use the tuple() constructor to make a tuple
# Example
# note the double round-brackets
this_tuple = tuple(("apple", "banana", "cherry"))
print(this_tuple)  # ('apple', 'banana', 'cherry')

# You can extend a tuple by adding another tuple
# Example
this_tuple = ("apple", "banana", "cherry")
another_tuple = ("orange", "mango", "grapes")
new_tuple = this_tuple + another_tuple
print(new_tuple)  # ('apple', 'banana', 'cherry', 'orange', 'mango', 'grapes')

# or use the extend() method
# Example
this_tuple = ("apple", "banana", "cherry")
another_tuple = ("orange", "mango", "grapes")
this_tuple.extend(another_tuple)
print(this_tuple)  # ('apple', 'banana', 'cherry', 'orange', 'mango', 'grapes')

# You can also use the * operator to repeat a tuple a given number of times
# Example
this_tuple = ("apple", "banana", "cherry")
another_tuple = this_tuple * 2
print(another_tuple)  # ('apple', 'banana', 'cherry', 'apple', 'banana', 'cherry')

# You can convert a list to a tuple
# Example
this_list = ["apple", "banana", "cherry"]
this_tuple = tuple(this_list)  # ('apple', 'banana', 'cherry')

# Copy a Tuple
# You cannot copy a tuple simply by typing tuple2 = tuple1, because: tuple2 will only be a reference to tuple1
# Changes made in tuple1 will automatically also be made in tuple2. To avoid this, you can use the copy() method
# Example
this_tuple = ("apple", "banana", "cherry")
my_tuple = this_tuple.copy()
print(my_tuple)  # ('apple', 'banana', 'cherry')

# You can unpack a tuple in variables
# Example
this_tuple = ("apple", "banana", "cherry")
# fruit_1 = "apple", fruit_2 = "banana", fruit_3 = "cherry"
fruit_1, fruit_2, fruit_3 = this_tuple

# Tuples are useful when you want to return multiple values from a function
# Example


def myfunc() -> tuple:
    return 1, 2, 3


print(myfunc())  # (1, 2, 3)

# You use tuples when you want to make sure that the data in the collection cannot be changed
# For instance, in an airport, the baggage of a passenger is checked in at the check-in counter and then it is sent to the baggage handling area
# Each piece of luggage is associated with a unique identification number, the passenger name, the destination, and the weight of the luggage
# Therefore, we can use a tuple to represent this data
# Example
luggage = [
    ("ID001", "John Smith", "London", 20),
    ("ID002", "Jane Doe", "Paris", 30),
    ("ID003", "John Doe", "Athens", 15),
]

# You can check if an item exists in a tuple
# Same as lists, you can use the in keyword to check if an item exists in a tuple
# Example
this_tuple = ("apple", "banana", "cherry")
if "apple" in this_tuple:
    print("Yes, 'apple' is in the fruits tuple")

# You can loop through a tuple
# Example
this_tuple = ("apple", "banana", "cherry")
for fruit in this_tuple:
    print(fruit)  # apple, banana, cherry

# You can use the len() method to return the length of a tuple
# Example
this_tuple = ("apple", "banana", "cherry")
print(len(this_tuple))  # 3

# You can use the count() method to count the number of times a value appears in a tuple
# Example
this_tuple = ("apple", "banana", "cherry", "apple")
print(this_tuple.count("apple"))  # 2

# You can use the index() method to find the index of a value in a tuple
# Example
this_tuple = ("apple", "banana", "cherry")
print(this_tuple.index("banana"))  # 1

# You can use the del keyword to delete a tuple completely
# Example
this_tuple = ("apple", "banana", "cherry")
del this_tuple
# print(this_tuple) # name 'this_tuple' is not defined

# You can use the clear() method to empty a tuple
# Example
this_tuple = ("apple", "banana", "cherry")
this_tuple.clear()
print(this_tuple)  # ()

# An interesting use of tuples in programming is swapping the values of two variables
# Example
a = 1
b = 2
a, b = b, a  # a = 2, b = 1

# In this example, we are swapping the values of a and b by using a tuple

# Other methods or practices of tuples are:
# To modify a tuple, you can convert it to a list, modify it, and convert it back to a tuple
# Example
this_tuple = ("apple", "banana", "cherry")
this_list = list(this_tuple)
this_list[1] = "mango"
this_tuple = tuple(this_list)
print(this_tuple)  # ('apple', 'mango', 'cherry')

# insert()
# You can insert an item at a given index but you need to convert the tuple to a list first
# Example
this_tuple = ("apple", "banana", "cherry")
this_list = list(this_tuple)
this_list.insert(1, "orange")
this_tuple = tuple(this_list)
print(this_tuple)  # ('apple', 'orange', 'banana', 'cherry')

# pop()
# You can remove an item at a given index but you need to convert the tuple to a list first
# Example
this_tuple = ("apple", "banana", "cherry")
this_list = list(this_tuple)
this_list.pop(1)
this_tuple = tuple(this_list)
print(this_tuple)  # ('apple', 'cherry')

# You can also use remove()
this_tuple = ("apple", "banana", "cherry")
this_list = list(this_tuple)
this_list.remove("apple")
this_tuple = tuple(this_list)
print(this_tuple)  # ('banana', 'cherry')

# reverse()
# To reverse the order of the items in a tuple
# Example
this_tuple = ("apple", "banana", "cherry")
this_list = list(this_tuple)
this_list.reverse()
this_tuple = tuple(this_list)
print(this_tuple)  # ('cherry', 'banana', 'apple')

# sort()
# To sort the items in a tuple
# Example
this_tuple = ("apple", "cherry", "banana", "watermelon")
this_list = list(this_tuple)
this_list.sort()
this_tuple = tuple(this_list)
print(this_tuple)  # ('apple', 'banana', 'cherry', 'watermelon')

# We can see in these examples that tuples are very similar to lists, the only difference is that tuples are immutable
# This means that once you create a tuple, you cannot modify it
# Therefore, if you want to modify a tuple, you need to convert it to a list, modify it, and then convert it back to a tuple
