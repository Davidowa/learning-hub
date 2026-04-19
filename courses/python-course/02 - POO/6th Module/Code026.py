# A good example of inheritance is a Stream class that can read and write data.
# Lets define a Stream class and a FileStream class that inherits from Stream.

from abc import ABC, abstractmethod


class Stream:
    def __init__(self) -> None:
        self.opened = False

    def open(self) -> None:
        if self.opened:
            raise Exception("Stream already opened.")
        self.opened = True

# But we dont want a generic Exception. We want a specific Exception.
# Lets create a new class called InvalidOperationError that inherits from Exception.
# And lets raise an InvalidOperationError instead of a generic Exception.


class InvalidOperationError(Exception):
    pass


class Stream:
    def __init__(self) -> None:
        self.opened = False

    def open(self) -> None:
        if self.opened:
            raise InvalidOperationError("Stream already opened.")
        self.opened = True

    def close(self) -> None:
        if not self.opened:
            raise InvalidOperationError("Stream already closed.")
        self.opened = False

# These are the common methods that a Stream class should have.

# Now lets define a FileStream class that inherits from Stream.


class FileStream(Stream):
    def read(self) -> None:
        print("Reading data from a file")

# Now lets define a NetworkStream class that inherits from Stream.
# How we read data from a file is different from how we read data from a network.


class NetworkStream(Stream):
    def read(self) -> None:
        print("Reading data from a network")

# This is a good example of inheritance.
# First of all we only have one or two levels of inheritance depending on how you count.
# We have the Stream class on the top of our hierarchy.
# And we have two subclasses the FileStream and NetworkStream classes.
# We should go beyond two levels of inheritance.
# Also our subclasses dont have multiple inheritance - no multiple parents.
# *smiley face*


# But lets continue with our example.
# Lets say we want to create an instance of Stream.

stream = Stream()

# And lets say we want to open the stream.

stream.open()

# But what means to open a stream?
# Are we opening a file or a network connection?
# We should not be able to create an instance of Stream.
# We should always create an instance of FileStream or NetworkStream.
# Therefore, we should make the Stream class abstract.
# In Python, an abstract class is a class that should not be instantiated.
# We can make a class abstract by importing the ABC class from the abc module.

# And by inheriting from the ABC class.


class Stream(ABC):
    def __init__(self) -> None:
        self.opened = False

    def open(self) -> None:
        if self.opened:
            raise InvalidOperationError("Stream already opened.")
        self.opened = True

    def close(self) -> None:
        if not self.opened:
            raise InvalidOperationError("Stream already closed.")
        self.opened = False

# Now we cannot create an instance of Stream.

# stream = Stream()  # TypeError: Can't instantiate abstract class Stream with abstract methods read

# Moreover we can use the abstractmethod decorator to mark a method as abstract.


class Stream(ABC):
    def __init__(self) -> None:
        self.opened = False

    def open(self) -> None:
        if self.opened:
            raise InvalidOperationError("Stream already opened.")
        self.opened = True

    def close(self) -> None:
        if not self.opened:
            raise InvalidOperationError("Stream already closed.")
        self.opened = False

    @abstractmethod
    def read(self) -> None:
        pass

# Now lets create a MemoryStream class that inherits from Stream.


class MemoryStream(Stream):
    pass

# If we try to create an instance of MemoryStream we get an error.
# stream = MemoryStream()
# This happens because we have not implemented the read method.
# Whenevere we use an abstractmethod decorator, we have to implement it in the subclass.
# Lets implement the read method.


class MemoryStream(Stream):
    def read(self) -> None:
        print("Reading data from a memory stream")


# Now we can create an instance of MemoryStream.
stream = MemoryStream()

# Classes that have defined abstract methods are called concrete classes.
