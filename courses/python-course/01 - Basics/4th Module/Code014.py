# Sets
# Sets are unordered collections of unique elements.
# Set does not allow duplicates.

# Lets create a set
# Example
my_set = {"apple", "banana", "cherry"}
print(my_set)  # {'apple', 'banana', 'cherry'}

# We can also use the set() constructor to create a set
# Example
my_set = set(("apple", "banana", "cherry"))
print(my_set)  # {'apple', 'banana', 'cherry'}

# Set can be used to remove duplicates from a list
# Example
my_list = ["apple", "banana", "cherry", "apple", "banana"]
my_set = set(my_list)
print(my_set)  # {'apple', 'banana', 'cherry'}

# To add an item to a set, you can use the add() method
# Example
my_set = {"apple", "banana", "cherry"}
my_set.add("orange")
print(my_set)  # {'apple', 'banana', 'cherry', 'orange'}

# To add multiple items to a set, you can use the update() method
# Example
my_set = {"apple", "banana", "cherry"}
my_set.update(["orange", "mango", "grapes"])
print(my_set)  # {'apple', 'banana', 'cherry', 'orange', 'mango', 'grapes'}

# To remove an item from a set, you can use the remove() or the discard() method
# Example
my_set = {"apple", "banana", "cherry"}
my_set.remove("banana")
print(my_set)  # {'apple', 'cherry'}

my_set = {"apple", "banana", "cherry"}
my_set.discard("cherry")
print(my_set)  # {'apple', 'banana'}

# To know the length of a set, you can use the len() method
# Example
my_set = {"apple", "banana", "cherry"}
print(len(my_set))  # 3

# You can iterate over a set using a for loop
# Example
my_set = {"apple", "banana", "cherry"}
for x in my_set:
    print(x)

# However, you cannot access items in a set by referring to an index or a key
# And when you iterate over a set, the items are returned in random order
# So maybe the first time you run the code, you will get this output:
# banana
# cherry
# apple
# And the second time you run the code, you will get this output:
# cherry
# apple
# banana

# Sets were conceived to be used in mathematical operations
# Therefore, we have methods like union(), intersection(), difference(), symmetric_difference(), issubset(), issuperset(), isdisjoint()
# union()
# To return a set containing the union of sets
# Example
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)  # {1, 2, 3, 'b', 'a', 'c'}

# Or you can use the | operator
# Example
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1 | set2
print(set3)  # {1, 2, 3, 'b', 'a', 'c'}

# intersection()
# To return a set containing the intersection of sets
# Example
set1 = {"a", "b", "c"}
set2 = {"c", "d", "e"}
set3 = set1.intersection(set2)
print(set3)  # {'c'}

# Or you can use the & operator
# Example
set1 = {"a", "b", "c"}
set2 = {"c", "d", "e"}
set3 = set1 & set2
print(set3)  # {'c'}

# difference()
# To return a set containing the difference between two or more sets
# Example
set1 = {"a", "b", "c"}
set2 = {"c", "d", "e"}
set3 = set1.difference(set2)
print(set3)  # {'a', 'b'}

# Or you can use the - operator
# Example
set1 = {"a", "b", "c"}
set2 = {"c", "d", "e"}
set3 = set1 - set2
print(set3)  # {'a', 'b'}

# symmetric_difference()
# The symetric difference is the difference between two sets, but the result will contain only the elements that are not present in both sets
# Example
set1 = {"a", "b", "c"}
set2 = {"c", "d", "e"}
set3 = set1.symmetric_difference(set2)
print(set3)  # {'d', 'e', 'a', 'b'}

# Or you can use the ^ operator
# Example
set1 = {"a", "b", "c"}
set2 = {"c", "d", "e"}
set3 = set1 ^ set2
print(set3)  # {'d', 'e', 'a', 'b'}

# issubset()
# To check if a set is a subset of another set
# A subset is a set that contains all the elements of another set
# Example
set1 = {"a", "b", "c"}
set2 = {"c", "d", "e"}
set3 = set1.issubset(set2)
print(set3)  # False

# Lets see a case where a set is a subset of another set
# Example
set1 = {"a", "b", "c"}
set2 = {"c", "b", "a", "d", "e"}
# Whith this syntax, we are checking if set1 is a subset of set2
set3 = set1.issubset(set2)
print(set3)  # True

# issuperset()
# To check if a set is a superset of another set
# A supper set is the opposite of a subset.
# A superset is a set that contains all the elements of another set
# Example
set1 = {"a", "b", "c"}
set2 = {"c", "d", "e"}
set3 = set1.issuperset(set2)
print(set3)  # False

# Lets see a case where a set is a superset of another set
# Example
set1 = {"a", "b", "c"}
set2 = {"c", "b", "a", "d", "e"}
# Whith this syntax, we are checking if set1 is a superset of set2
set3 = set1.issuperset(set2)
print(set3)  # True

# isdisjoint()
# To check if two sets have a null intersection
# Two sets are disjoint if their intersection is the empty set
# Example
set1 = {"a", "b", "c"}
set2 = {"c", "d", "e"}
set3 = set1.isdisjoint(set2)
print(set3)  # False

# Lets see a case where two sets are disjoint
# Example
set1 = {"a", "b", "c"}
set2 = {"d", "e"}
set3 = set1.isdisjoint(set2)
print(set3)  # True

# You can also check if an item is present in a set by using the in keyword
# Example
set1 = {"a", "b", "c"}
print("a" in set1)  # True
print("d" in set1)  # False
