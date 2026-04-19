# Inheritance prevents us from repeating code.
# Also inheritance allows us to create subclasses that have their own attributes and methods.
# And provides ways to mantaing the code.

# However, it is worth mentioning that inheritance can be abused.

# Multi-level inheritance
# Lets see an example.
class Animal:
    def __init__(self, name: str) -> None:
        self.name = name

    def eat(self) -> None:
        print("eat")


class Bird(Animal):
    def __init__(self, name: str) -> None:
        super().__init__(name)

    def fly(self) -> None:
        print("fly")


class Chicken(Bird):
    def __init__(self, name: str) -> None:
        super().__init__(name)

# But a chicken cannot fly!
# This is what we call a multi-level inheritance.

# Lets see another example.
# An employee is a person.
# A person is a living being.
# A living being is an thing.
# And so on to model the entire universe.
# You are gonna shoot yourself in the foot if you do multi-level inheritance.

# Multi-level inheritance increases the complexity of the code.

# Remember that inheritance is used to prevent code repetition.
# And the methods you define in a class are created to solve a business/specific problem
# Lets go back to the Animal example
# just because an Animal can eat, it does mean that you have to implement the eat method in the Animal class

# Recommendation - Your inheritance tree should not be more than 2 levels deep.

# Multiple inheritance
# A class can inherit from multiple classes.
# Lets see an example of multiple inheritance. Lets define an Employee class and a Person class
# and that a Manager is an Employee and a Person.


class Person:
    def __init__(self, name: str) -> None:
        self.name = name

    def greet(self) -> None:
        print(f"Hello, my name is {self.name}")


class Employee:
    def __init__(self, id: int) -> None:
        self.id = id

    def work(self) -> None:
        print(f"Employee {self.id} is working")


class Manager(Person, Employee):
    def __init__(self, name: str, id: int) -> None:
        Person.__init__(self, name)
        Employee.__init__(self, id)


manager = Manager("John", 1)
manager.greet()  # Hello, my name is John
manager.work()  # Employee 1 is working

# Lets see a problem with multiple inheritance. Imagine that Employee and Person have a method called greet.


class Person:
    def __init__(self, name: str) -> None:
        self.name = name

    def greet(self) -> None:
        print(f"Hello, my name is {self.name}")


class Employee:
    def __init__(self, id: int) -> None:
        self.id = id

    def work(self) -> None:
        print(f"Employee {self.id} is working")

    def greet(self) -> None:
        print(f"Hello, I am employee {self.id}")


class Manager(Employee, Person):
    def __init__(self, name: str, id: int) -> None:
        Person.__init__(self, name)
        Employee.__init__(self, id)


manager = Manager("John", 1)
manager.greet()
# Which greet method is called when we create a Manager object?

# The answer is the greet method of the Employee class, as it is the first class in the inheritance list.
# If the Employee class does not have a greet method, then the greet method of the Person class is called.

# And imagine that some time later a new programmer is hired and he change the order of the classes in the inheritance list.
# Our program will have a different behavior.

# Same as multiple inheritance, multiple inheritance increases the complexity of the code.
# It also could produce unwanted results or bugs - As a chicken that can fly!

# Solution - Use composition instead of inheritance.

# Composition is a design principle in object-oriented programming
# where a class is constructed by using references to other classes in its definition.
# Instead of a class inheriting properties and behaviors from a super class (as in inheritance),
# it has them by containing instances of other classes.

# Lets see an example. Lets say we want to model a computer.


class CPU:
    def __init__(self, brand: str, model: str) -> None:
        self.brand = brand
        self.model = model

    def execute(self) -> None:
        print("Executing program...")


class RAM:
    def __init__(self, capacity: int) -> None:
        self.capacity = capacity

    def load(self, data: str) -> None:
        print(f"Loading {data} to RAM...")


class HardDrive:
    def __init__(self, size: int) -> None:
        self.size = size

    def read(self, file: str) -> None:
        print(f"Reading {file} from hard drive...")


class Computer:
    def __init__(self, cpu: CPU, ram: RAM, hdd: HardDrive) -> None:
        self.cpu = cpu
        self.ram = ram
        self.hdd = hdd

    def start(self, program: str) -> None:
        self.hdd.read(f"{program}.exe")
        self.ram.load(program)
        self.cpu.execute()


# Create components
intel_cpu = CPU("Intel", "i7-9700k")
ddr4_ram = RAM("16GB")
ssd = HardDrive("1TB")

# Compose a computer using these components
my_computer = Computer(intel_cpu, ddr4_ram, ssd)
# Reading Photoshop.exe from hard drive... Loading Photoshop to RAM... Executing program...
my_computer.start("Photoshop")

# The advantage of using composition is that it promotes a more modular and flexible structure.
# You can change or replace parts of a composed object without needing to touch other parts.
# # This adheres to the principle of "composition over inheritance,"
# # which suggests it's better to compose what an object can do (has-a relationship)
# # rather than inheriting what it is (is-a relationship).

# As a comment, so why does python have inheritance?
# Inheritance is not bad. It is a very useful tool.
# But you should use it wisely.
# If classes are used to reuse code, then inheritance is a good choice.
# Things get complicated when classes have things in common.

# Lets see a good example of multiple inheritance.


class Flyer:
    def fly(self) -> None:
        print("fly")


class Swimmer:
    def swim(self) -> None:
        print("swim")

# These classes are very small and abstract, and
# These classes have nothing in common!
# So, it is a good idea to use inheritance here to create a FlyingFish class.


class FlyingFish(Flyer, Swimmer):
    pass

# This is a good example of multiple inheritance.

# Now lets see a good example of multi-level inheritance.


class Shape:
    def __init__(self, name: str) -> None:
        self.name = name

    def display(self) -> None:
        print(f"This is a {self.name}.")


class Polygon(Shape):
    def __init__(self, name: str, sides: int) -> None:
        super().__init__(name)
        self.sides = sides

    def display_sides(self) -> None:
        print(f"This {self.name} has {self.sides} sides.")


class Triangle(Polygon):
    def __init__(self, base: float, height: float) -> None:
        super().__init__("Triangle", 3)
        self.base = base
        self.height = height

    def area(self) -> float:
        return 0.5 * self.base * self.height


triangle = Triangle(10, 20)
triangle.display()  # This is a Triangle.
triangle.display_sides()  # This Triangle has 3 sides.
# Area of the triangle: 100.0
print(f"Area of the triangle: {triangle.area()}")

# In this example:
# Shape is a super class.
# Polygon is derived from Shape and introduces the concept of sides.
# Triangle is derived from Polygon and adds functionality specific to triangles, such as calculating the area.
# This hierarchy is logical and represents real-world relationships among these entities.
