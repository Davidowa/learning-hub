# Bonus - Properties
# A property is a special kind of attribute that allows us to define a method that will be executed when we try to access or modify the value of an attribute.
# We use the decorator "@property" to define a property.
# Lets see an example. Lets define a class called "Product".
# The class "Product" has a constructor and some methods.

class Product:
    def __init__(self, price: float) -> None:
        self.price = price

    def get_price(self) -> float:
        return self.__price

    def set_price(self, value: float) -> None:
        if value < 0:
            raise ValueError("Price cannot be negative.")
        self.__price = value

    price = property(get_price, set_price)

    def __str__(self) -> str:
        return f"Price: {self.price}"


# The class "Product" has a property called "price".
# The property "price" has a getter and a setter.
# The getter is called when we try to access the value of the property.
# The setter is called when we try to modify the value of the property.

my_product = Product(10)
print(my_product.price)  # 10
my_product.price = 20
print(my_product.price)  # 20

# However, this syntax is not very Pythonic.
# Pythonic code is code that is written in a way that is natural to the Python language.
# For properties, we prefer to use decorators.
# Lets rewrite the class "Product" using decorators.


class Product:
    def __init__(self, price: float) -> None:
        # self.price calls the setter method of the property "price".
        self.price = price

    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, value: float) -> None:
        if value < 0:
            raise ValueError("Price cannot be negative.")
        self.__price = value

    def __str__(self) -> str:
        return f"Price: {self.price}"


my_product = Product(10)
# 10. The getter method of the property "price" is called.
print(my_product.price)
my_product.price = 20  # The setter method of the property "price" is called.

# # By using self.price in the __init__ method,
# # you're utilizing the setter method of the price property.
# # This means that the value assignment in the __init__ method will go
# # through the validation logic you've provided in the setter
# # (if value < 0: raise ValueError("Price cannot be negative.")).

# If you donw want to raise an error, you can use a conditional statement.


class Product:
    def __init__(self, price: float) -> None:
        self.price = price

    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, value: float) -> None:
        if value < 0:
            print("Negative price provided. Setting price to 0.")
            self.__price = 0
        else:
            self.__price = value

    def __str__(self) -> str:
        return f"Price: {self.price}"


# Example usage:
product = Product(-15.5)
print(product)  # Outputs: Price: 0

# Lastly, properties that have only getters are called read-only properties.
