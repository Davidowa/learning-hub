# Bonus
# Method overring and polimorphism
# Method overriding and polymorphism are related concepts in object-oriented programming

# Lets see an example of method overriding.

class Animal:
    def __init__(self, name: str) -> None:
        self.name = name

    def talk(self) -> None:
        print("Animal talk")


class Dog(Animal):
    def __init__(self, name: str) -> None:
        super().__init__(name)

    def talk(self) -> None:
        print("Woof")


class Cat(Animal):
    def __init__(self, name: str) -> None:
        super().__init__(name)

    def talk(self) -> None:
        print("Meow")


dog = Dog("Bobby")
dog.talk()  # Woof
cat = Cat("Kitty")
cat.talk()  # Meow

# Polimorphism
# Polimorphism means that different classes can have the same method name.
# Lets see an example.

animals = [Dog("Bobby"), Cat("Kitty"), Dog("Rex"), Cat("Luna")]
for animal in animals:
    animal.talk()  # Woof Meow Woof Meow

# The Animal class defines the method "talk". The Dog and Cat classes override the method "talk".
# When iterating the list of animals, the method "talk" is called for each animal.
# And the appropriate method is called depending on the class of the animal.
# This demonstrates runtime polimorphism.
