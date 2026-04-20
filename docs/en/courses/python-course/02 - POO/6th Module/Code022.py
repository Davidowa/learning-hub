# Bonus topic
# Class vs Instance attributes

# Class attributes are attributes that are shared by all instances of a class.
# Instance attributes are attributes that are unique to each instance of a class.
# Lets see an example.

class Person:
    # Class attribute
    species = "human"

    def __init__(self, name: str, age: int) -> None:
        # Instance attributes
        self.name = name
        self.age = age


my_person = Person("John", 36)
print(my_person.name)  # John
print(my_person.age)  # 36
print(my_person.species)  # human
print(Person.species)  # human
my_person.species = "alien"
print(my_person.species)  # alien
print(Person.species)  # human

# But if i modify the class attribute, it will be modified for all instances of the class.
Person.species = "animals"
print(my_person.species)  # animals
print(Person.species)  # animals

# Typically, class attributes are constants.
# They are not modified.
# They are used to store values that are shared by all instances of a class.
# So mostly you will be using instance attributes.


# Class vs Instance methods
# Same as attributes, methods can be class or instance methods.
# Class methods are methods that are shared by all instances of a class.
# Instance methods are methods that are unique to each instance of a class.
# Lets see an example.

class Person:
    # Class method
    @classmethod
    def get_species(cls):
        return cls.species

    @classmethod
    def zero(cls):
        return cls("", 0)

    # Instance method
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age


my_person = Person("John", 36)
# <bound method Person.get_species of <class '__main__.Person'>>
print(my_person.get_species())
my_person2 = Person.zero()

# In class methods we use the decorator @classmethod.
# In instance methods we do not use any decorator.
# Class methods receive the class as first parameter, by convention we call it cls.
# Class methods are also called factory methods.

# Magic methods
# Magic methods are methods that start and end with double underscores.
# They are also called dunder methods.
# They are used to add functionality to classes.

# We have already seen some magic methods.
# The method __init__ is a magic method.
# # It is the constructor of the class.
# # It is called when an instance of a class is created.
# We have also seen the method __exit__.
# # It is the destructor of the class.
# # It is called when an instance of a class is destroyed.
# # We use it to release resources. That means, to free memory.
# # We will cover this topic in the fourth topic of this course.

# Another magic method is __str__.
# # It is used to convert an object to a string.
# # It is called when we use the function "str" on an object.
# # It is also called when we print an object.
# # Lets see an example.


class Person:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age


my_person = Person("John", 36)
print(my_person)  # <__main__.Person object at 0x0000020D3B3C0A60>

# The output is not very useful. It is not very readable.
# The output is the name of the class, the word "object" and the memory address.
# We can change the output by implementing the magic method __str__.
# Lets modify the class Person.


class Person:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def __str__(self) -> str:
        return f"Name: {self.name}, Age: {self.age}"


my_person = Person("John", 36)
print(my_person)  # Name: John, Age: 36

# Now the output is more useful.

# There are times when we want to compare objects.
# Lets define a Point class


class Point:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y


point1 = Point(1, 2)
point2 = Point(1, 2)
print(point1 == point2)  # False

# The output is False. but the points are equal.
# This happens because the == operator compares the memory addresses of the objects.
print(point1)  # <__main__.Point object at 0x0000020D3B3C0A90>
print(point2)  # <__main__.Point object at 0x0000020D3B3C0AC0>

# We can change the behavior of the == operator.
# We can do that by implementing the magic method __eq__.
# Lets modify the class Point.


class Point:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def __eq__(self, other) -> bool:
        return self.x == other.x and self.y == other.y


point1 = Point(1, 2)
point2 = Point(1, 2)
print(point1 == point2)  # True

# Now the output is True. This is called operator overloading.
# We can change the behavior of operators by implementing magic methods in our classes.
# Examples of magic methods that can have operator overloading are:
# # __eq__ for the == operator
# # __ne__ for the != operator
# # __lt__ for the < operator
# # __gt__ for the > operator
# # __le__ for the <= operator
# # __ge__ for the >= operator
# # __add__ for the + operator
# # __sub__ for the - operator
# # __mul__ for the * operator
# # __truediv__ for the / operator
# # __floordiv__ for the // operator
# # __mod__ for the % operator
# # __pow__ for the ** operator
# # and many more

# You can read the MagicMethods.md file in this repository for more information about magic methods.

# Lets override the __add__ method.
# Lets modify the class Point.


class Point:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"

    def __eq__(self, other) -> bool:
        return self.x == other.x and self.y == other.y


point1 = Point(1, 2)
point2 = Point(3, 4)
point3 = point1 + point2

print(point1)  # (1, 2)
print(point2)  # (3, 4)
print(point3)  # (4, 6)

# In this case, the + operator is used to add the coordinates of the points and return a new point.
