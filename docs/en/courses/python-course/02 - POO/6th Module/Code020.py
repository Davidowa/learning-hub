# Classes
# Lets continue with the last two principles of object oriented programming:
# Inheritance: The idea is to reuse code.
# We can create a class that inherits from another class.
# The class that inherits is called subclass.
# The class that is inherited is called superclass.
# The subclass inherits the attributes and methods of the superclass.

# Lets see an example.
class Animal:
    def __init__(self, name: str) -> None:
        self.name = name

    def eat(self) -> None:
        print("eat")

# The class "Animal" has a constructor and a method called "eat".
# Lets create a subclass of the class "Animal".
# The subclass is called "Mammal".
# The superclass is called "Animal".
# The subclass inherits the attributes and methods of the superclass.
# The subclass can have its own attributes and methods.
# Lets see an example.


class Mammal(Animal):
    def __init__(self, name: str) -> None:
        super().__init__(name)


my_mammal = Mammal("dog")
print(my_mammal.name)  # dog
my_mammal.eat()  # eat

# The subclass "Mammal" inherits the constructor and the method "eat" from the superclass "Animal".
# The subclass "Mammal" has its own constructor.
# The constructor of the subclass calls the constructor of the superclass.
# The constructor of the superclass is called with the function "super".
# The function "super" receives the name of the subclass and the object as parameters.
# The function "super" returns an object of the superclass.
# The function "super" can be used to call the methods of the superclass.

# Lets see another an example.


class Fish(Animal):
    def __init__(self, name: str) -> None:
        super().__init__(name)

    def swim(self) -> None:
        print("swim")


my_fish = Fish("shark")
my_fish.swim()  # swim

# The subclass "Fish" has its own method called "swim".
# The method "swim" is not in the superclass "Animal".
# The method "swim" is only in the subclass "Fish".

# To make private attributes and methods of a class available to its subclasses we need to use the double underscore.
# Lets see an example.


class Person:
    def __init__(self, name: str, age: int) -> None:
        self.__name = name
        self.age = age

    def talk(self) -> None:
        print(f"Hi, my name is {self.__name}")

# The class "Person" has a private attribute called "name".
# The class "Person" has a public attribute called "age".
# The class "Person" has a public method called "talk".
# Lets create a subclass of the class "Person".
# The subclass is called "Student".
# The superclass is called "Person".
# The subclass inherits the attributes and methods of the superclass.
# The subclass can have its own attributes and methods.
# Lets see an example.


class Student(Person):
    def __init__(self, name: str, age: int, student_id: int) -> None:
        super().__init__(name, age)
        self.student_id = student_id

    def study(self) -> None:
        print("study")


my_student = Student("John", 20, 1234)
print(my_student.age)  # 20
my_student.talk()  # Hi, my name is John
my_student.study()  # study
# AttributeError: 'Student' object has no attribute '__name'
# print(my_student.__name)
# The attribute __name is private, so it cannot be accessed from outside the class.

# To make protected attributes and methods of a class available to its subclasses, the convention is to use the single underscore.
# Lets see an example.


class Person:
    def __init__(self, name: str, age: int) -> None:
        self._name = name
        self.age = age

    def talk(self) -> None:
        print(f"Hi, my name is {self._name}")


# The class "Person" has a protected attribute called "name".
# The class "Person" has a public attribute called "age".
my_person = Person("John", 20)
print(my_person._name)  # John, it will work but it is not recommended.
# protected attributes and methods should not be accessed from outside the class.
# python does not have a way to make protected attributes and methods private.

# Polymorphism: The idea is to have many forms of a method.
# We can have a method with the same name in different classes.
# The method can have different implementations in different classes.
# The method can be called from an object of any of the classes.
# The subclass can override the method of the superclass.
# Lets see an example.


class Animal:
    def __init__(self, name: str) -> None:
        self.name = name

    def eat(self) -> None:
        print("eat")

# The class "Animal" has a constructor and a method called "eat".
# Lets create a subclass of the class "Animal".
# The subclass is called "Reptile".


class Reptile(Animal):
    def __init__(self, name: str) -> None:
        super().__init__(name)

    def eat(self) -> None:
        print("eat insects")

# The subclass "Reptile" has its own implementation of the method "eat".


my_reptile = Reptile("snake")
my_reptile.eat()  # eat insects

# The method "eat" of the subclass "Reptile" overrides the method "eat" of the superclass "Animal".

# Lets see another example.


class Shape:
    def area(self):
        pass

    def display(self):
        print(f"Area of {self.__class__.__name__}: {self.area()}")


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


shapes = [Shape(), Circle(5), Rectangle(4, 5)]
for shape in shapes:
    shape.display()

# The class "Shape" has two methods: "area" and "display".
# The method "display" calls the method "area".
# The class "Circle" has a constructor and a method called "area".
# The class "Rectangle" has a constructor and a method called "area".
# The method "area" of the class "Circle" calculates the area of a circle.
# The method "area" of the class "Rectangle" calculates the area of a rectangle.
# The method "display" of the class "Shape" calls the method "area" of the object.
# The method "display" of the class "Shape" prints the name of the class of the object.
# The method "display" of the class "Shape" prints the area of the object.

# Polymorphism is demonstrated when we iterate the list of shapes, as the method "display" is called for each shape.
# A detailed explanation of the code is in 02 - POO/5th Module/Code026.py.

# Result:
# Area of Shape: None
# Area of Circle: 78.5
# Area of Rectangle: 20
