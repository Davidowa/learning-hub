# Dictionaries
# This is a very powerful data type to hold a lot of information in a single variable.
# Dictionaries are used to store data values in key:value pairs.
# A dictionary is a collection which is ordered*, changeable and does not allow duplicates.
# As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.

# Dictionaries are written with curly brackets, and have keys and values:
# Example
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

# You can also use the dict() constructor to make a dictionary:
# Example
car = dict(brand="Ford", model="Mustang", year=1964)


# if you use an already used key, the last value will be used
# Example
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    "year": 2020
}
print(car)  # {'brand': 'Ford', 'model': 'Mustang', 'year': 2020}

# And if you use an invalid key to access a value, you will get an error
# Example

# car = {
#     "brand": "Ford",
#     "model": "Mustang",
#     "year": 1964
# }
# print(car["color"])  # KeyError: 'color'

# You can access the items of a dictionary by referring to its key name, inside square brackets:
# Example
x = car["model"]
print(x)  # Mustang

# There is also a method called get() that will give you the same result:
# Example
x = car.get("brand")
print(x)  # Ford

# get can also return a default value if the key does not exist
# Example
x = car.get("color", "white")  # white

# You can change the value of a specific item by referring to its key name:
# Example
car["year"] = 2020
print(car)  # {'brand': 'Ford', 'model': 'Mustang', 'year': 2020}

# To delete an item in a dictionary, use the pop() method:
# Example
car.pop("model")  # {'brand': 'Ford', 'year': 2020}

# The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead):
# Example
car.popitem()  # {'brand': 'Ford'}

# The del keyword removes the item with the specified key name:
# Example
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
del car["model"]  # {'brand': 'Ford', 'year': 1964}

# The del keyword can also delete the dictionary completely:
# Example
del car

# You can loop through a dictionary by using a for loop.
# When looping through a dictionary, the return value are the keys of the dictionary, but there are methods to return the values as well.
# Example
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

for x in car:
    print(x)  # brand model year

# In this case, the keys are printed.

# You can also get the same result by using the keys() method
# Example
for x in car.keys():
    print(x)  # brand model year

# Print all values in the dictionary, one by one:
# Example
for x in car:
    print(car[x])  # Ford Mustang 2020

# You can also use the values() method to return values of a dictionary:
# Example
for x in car.values():
    print(x)  # Ford Mustang 2020

# Loop through both keys and values, by using the items() method:
# Example
for x, y in car.items():
    print(x, y)  # brand Ford model Mustang year 2020

# This produces a tuple for each key/value pair

# To determine if a specified key is present in a dictionary use the in keyword:
# Example
if "model" in car:
    # Yes, 'model' is one of the keys in the car dictionary
    print("Yes, 'model' is one of the keys in the car dictionary")

# Dictionary Length
# To determine how many items (key-value pairs) a dictionary has, use the len() method.
# Example
print(len(car))  # 3

# Adding Items
# Adding an item to the dictionary is done by using a new index key and assigning a value to it:
# Example
car["color"] = "red"

# Copy a Dictionary
# To copy a dictionary, you can use the copy() method.
# Example
my_car = car.copy()
# {'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'color': 'red'}
print(my_car)

# Another way to make a copy is to use the built-in function dict().
# Example
my_car = dict(car)
# {'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'color': 'red'}
print(my_car)

# Nested Dictionaries
# A dictionary can also contain many dictionaries, this is called nested dictionaries.
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

# Or, if you want to nest three dictionaries that already exists as dictionaries:
# Example
child1 = {
    "name": "Emil",
    "year": 2004
}
child2 = {
    "name": "Tobias",
    "year": 2007
}
child3 = {
    "name": "Linus",
    "year": 2011
}

my_family = {
    "child1": child1,
    "child2": child2,
    "child3": child3
}

# To access the nested dictionary, use the correct keys.
# Example

print(my_family["child1"])  # {'name': 'Emil', 'year': 2004}

# Or, if you want to print all the values in the nested dictionary:
# Example

for x in my_family.values():
    # {'name': 'Emil', 'year': 2004} {'name': 'Tobias', 'year': 2007} {'name': 'Linus', 'year': 2011}
    print(x)

# Or if you want to access a specific value in the nested dictionary:
# Example
print(my_family["child1"]["name"])  # Emil
