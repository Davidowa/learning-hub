# Classes
# Classes are used to define new types.

# Object oriented programming stablishes four principles, lets see the first two:
# Abstraction: The idea is to define the characteristics of an object.
# The object is an abstraction of a real world entity.
# Abstraction lets us focus on the essential characteristics of an object, the ones that make it unique.

# Encapsulation: The idea is to hide the complexity of the code.
# It is a way to organize the code.
# It is a way to protect the data of the object.
# It is a way to prevent the code from being modified by accident.
# There are three levels of encapsulation: public, protected and private.
# Public: The attributes and methods of the class are public. This means that they can be accessed from outside the class.
# Protected: The attributes and methods of the class are protected. This means that they can only be accessed from the class and its subclasses.
# Private: The attributes and methods of the class are private. This means that they can only be accessed from the class.

# Lets imagine an object that let us manage shopping carts in an online store.
# We can define a class called "Shopping_Cart" that represents a shopping cart.
# A class is a blueprint for creating new objects.
# An object is an instance of a class.

# Lets see an example.
class ShoppingCart:
    pass


# # We can create an object of the class "Shopping_Cart".
cart1 = ShoppingCart()
cart2 = ShoppingCart()
print(type(cart1))  # <class '__main__.Shopping_Cart'>

# A class can have attributes and methods.
# Attributes are variables that belong to an object.
# Methods are functions that belong to an object.
# Lets create a class called Point that represents a point in 2D space.


class Point:
    def draw(self) -> None:
        print("draw")

# Every object that we create from this class will have a method called "draw".


point = Point()
point.draw()  # draw

# We have a function called isinstance that let us know if an object is an instance of a class.
print(isinstance(point, Point))  # True

# Lets go back to the point class.
# The self parameter is a reference to the current object.
# This parameter is used to access variables that belong to the object.
# We always have to pass the self parameter to the methods of a class to access the attributes and methods of the class.

# Moreover, a class needs to have a constructor.
# A constructor is a method that is called when we create an object of a class.
# The constructor is used to initialize the object.
# The constructor is always called "__init__".
# The constructor can receive parameters.
# The constructor can be used to initialize attributes of the object.
# Lets create a constructor for the point class.


class Point:
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def draw(self) -> None:
        print("draw")


# In this case, the constructor receives two parameters.
# The constructor initializes the attributes "x" and "y" of the object. This is the abstraction principle.
# Lets create an object of the class "Point".
point = Point(1, 2)
print(point.x)  # 1
print(point.y)  # 2

# In python all the attributes and methods of a class are public. This is the encapsulation principle.
# This means that we can access them from outside the class.
# Usually you want to prevent this by stablishing different levels of encapsulation.
# Thats why Python use two underscore before the name of an attribute or method to indicate that it is private.

# Lets create a class called "Person" that has a private attribute called "name" and a atributte called "age".
# The "name" attribute can only be accessed from inside the class.
# The "age" attribute can be accessed from outside the class.
# Lets create a constructor that receives the name and age of the person.


class Person:
    def __init__(self, name: str, age: int) -> None:
        self.__name = name
        self.age = age

    def talk(self) -> None:
        print(f"Hi, my name is {self.__name}")

# Typically, a person never changes its name.
# But it can change its age.


person = Person("John", 20)
print(person.age)  # 20
person.age = 21
print(person.age)  # 21

# We can access the "age" attribute from outside the class.
# However, we cannot access the "name" attribute from outside the class.

# print(person.name)  # AttributeError: 'Person' object has no attribute 'name'

# To be able to access the "name" attribute from outside the class we need to create a method that returns the value of the attribute.
# Lets create a method called "get_name" that returns the value of the attribute "name".
# Lets create a method called "set_name" that receives a value and assigns it to the attribute "name".
# The gettter and setter methods are used to access private attributes from outside the class.


class Person:
    def __init__(self, name: str, age: int) -> None:
        self.__name = name
        self.age = age

    def talk(self) -> None:
        print(f"Hi, my name is {self.__name} and I am {self.age} years old")

    def get_name(self) -> str:
        return self.__name

    def set_name(self, name: str) -> None:
        self.__name = name

# Private methods
# They can only be accessed from inside the class.
# Lets create a private method called "say_age".


class Person:
    def __init__(self, name: str, age: int) -> None:
        self.__name = name
        self.age = age

    def talk(self) -> None:
        print(f"Hi, my name is {self.__name} and {self.__say_age()}")

    def get_name(self) -> str:
        return self.__name

    def set_name(self, name: str) -> None:
        self.__name = name

    def __say_age(self) -> None:
        print(f"I am {self.age} years old")


my_person = Person("John", 20)
my_person.talk()  # Hi, my name is John and I am 20 years old
# my_person.__say_age()  # AttributeError: 'Person' object has no attribute '__say_age'
