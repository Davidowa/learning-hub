# Bonus - Making custom containers

# In this example, we have a class called "TagCloud".
# We will use TagCloud to store tags and their counts.
# We choose the name "TagCloud" because it is a common name for this kind of class.
# The class "TagCloud" has a constructor and some methods.
# The constructor has no parameters.
# The constructor initializes an attribute called "tags".
# The attribute "tags" is a dictionary.

class TagCloud:
    def __init__(self):
        self.__tags = {}

    def add(self, tag):
        self.__tags[tag] = self.__tags.get(tag, 0) + 1

    def __str__(self):
        return str(self.__tags)


cloud = TagCloud()
cloud.add("python")
cloud.add("python")
cloud.add("python")
print(cloud)  # {'python': 3}

# The method "add" receives a tag as parameter.
# The method "add" adds the tag to the dictionary.
# The method "add" uses the method "get" to get the count of the tag.
# The method "add" adds 1 to the count of the tag.

# But why did not we use an old-fashioned dictionary?
# Lets add a Python tag to the dictionary.
cloud.add("Python")
print(cloud)  # {'python': 3, 'Python': 1}

# This is how typical dictionaries work.
# But we can make it better.
# We can make it case insensitive.
# This is something that we cannot do with a typical dictionary.


class TagCloud:
    def __init__(self):
        self.__tags = {}

    def add(self, tag):
        self.__tags[tag.lower()] = self.__tags.get(tag.lower(), 0) + 1

    def __str__(self):
        return str(self.__tags)


cloud = TagCloud()
cloud.add("Python")
cloud.add("python")
cloud.add("python")
print(cloud)  # {'python': 3}

# Now let read the count of the tag "python".
# We can do it with the method "get".
# The method "get" receives a key as parameter.
# The method "get" returns the value of the key.
# The method "get" returns 0 if the key does not exist.


class TagCloud:
    def __init__(self):
        self.__tags = {}

    def add(self, tag):
        self.__tags[tag.lower()] = self.__tags.get(tag.lower(), 0) + 1

    def __str__(self):
        return str(self.__tags)

    def __getitem__(self, tag):
        return self.__tags.get(tag.lower(), 0)

# But we can do better. Lets make a setter and a len method AND lets make it iterable.
# The setter will allow us to change the count of a tag.


class TagCloud:
    def __init__(self):
        self.__tags = {}

    def add(self, tag):
        self.__tags[tag.lower()] = self.__tags.get(tag.lower(), 0) + 1

    def __str__(self):
        return str(self.__tags)

    def __getitem__(self, tag):
        return self.__tags.get(tag.lower(), 0)

    def __setitem__(self, tag, count):
        self.__tags[tag.lower()] = count

    def __len__(self):
        return len(self.__tags)

    def __iter__(self):
        return iter(self.__tags)


# Now we can read and change the count of a tag.
cloud = TagCloud()
cloud.add("python")
cloud.add("python")
cloud.add("python")
print(cloud)  # {'python': 3}
print(cloud["python"])  # 3
cloud["python"] = 10
print(cloud["python"])  # 10
print(len(cloud))  # 1 because we have only one tag
for tag in cloud:
    print(tag)  # python


# Remember that we saw the principle of encapsulation in the 02 - POO/5th Module/Code019.py.
# Lets see what happens if we created the class "TagCloud" without encapsulation.

class TagCloud:
    def __init__(self):
        self.tags = {}

    def add(self, tag):
        self.tags[tag.lower()] = self.tags.get(tag.lower(), 0) + 1

    def __str__(self):
        return str(self.tags)

    def __getitem__(self, tag):
        return self.tags.get(tag.lower(), 0)

    def __setitem__(self, tag, count):
        self.tags[tag.lower()] = count

    def __len__(self):
        return len(self.tags)

    def __iter__(self):
        return iter(self.tags)


# Lets create an object of the class "TagCloud".
cloud = TagCloud()
cloud.add("python")
cloud.add("python")
cloud.add("python")
print(cloud.tags["python"])  # 3
# Here we are accessing the attribute "tags" directly.
# and because "c++" does not exist, it will return an error.
# KeyError: 'c++', which means that the key does not exist.
# print(cloud.tags["c++"])

# This is why we use encapsulation. To avoid errors like this.
