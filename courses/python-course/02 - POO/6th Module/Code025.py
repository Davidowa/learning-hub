# Bonus - The object class
# The object class is the parent class of all classes in Python.
# All classes in Python inherit from the object class.
# The object class has some special methods.
# Lets see some of them.

o = object()

# Lets define a class called Animal and a subclass called Dog.


class Animal:
    pass


class Dog(Animal):
    pass


class Fish:
    pass

# As we have seen we have a function called isinstance that let us know if an object is an instance of a class.
# Lets see an example.


dog = Dog()
print(isinstance(dog, Dog))  # True
print(isinstance(dog, Animal))  # True
print(isinstance(dog, object))  # True
print(isinstance(dog, Fish))  # False

# Another function is called issubclass
# Lets see an example.

print(issubclass(Dog, Animal))  # True
print(issubclass(Dog, object))  # True
print(issubclass(Animal, object))  # True
print(issubclass(Fish, Animal))  # False

# All classes in Python inherit from the object class.
