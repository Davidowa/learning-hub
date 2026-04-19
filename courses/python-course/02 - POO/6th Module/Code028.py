from collections import namedtuple
from typing import Any

# Extending built-in classes

# We can extend built-in classes like str, int, list, etc.

# Lets see an example.


class Text(str):
    def __init__(self, text: str) -> None:
        self.text = text

    def duplicate(self) -> str:
        return self.text + self.text


text = Text("Python")
print(text)  # Python
print(text.duplicate())  # PythonPython

# The class Text extends the class str.

# Now lets see an example with the class list.


class TrackList(list):
    def append(self, __object: Any) -> None:
        print("Append called")
        super().append(__object)


my_list = TrackList()
my_list.append("Python")


# Data classes
# Data classes are classes that are used to store data.
# Data classes are classes that have only attributes and no methods.
# Data classes are classes that have only the __init__ method.
# Data classes are symilar to structs in C.

# Lets see an example.


class Point:
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y


point = Point(1, 2)

# The class Point is a data class.
# but if we want to consider operations between points, we should override the __add__ method or another method.
# This makes tthe class Point not a data class anymore.

# Therefore, we can used named tuples instead of data classes.
Point2D = namedtuple("Point2D", ["x", "y"])

p1 = Point2D(x=1, y=2)
p2 = Point2D(x=1, y=2)

print(p1 == p2)  # True

print(p1.x)  # 1

# One thing to remember is that once we create a named tuple, we cannot change its values.
# p1.x = 10  # AttributeError: can't set attribute
# So if we want to modify the value of p1.x, we have to create a new named tuple.
p1 = Point2D(x=10, y=p1.y)
