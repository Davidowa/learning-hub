course = "Python Programming"
len(course)  # 18
# If you want to show the in the console you can use print() function
print(len(course))  # This will print 18 in the console

# You can use the following functions to manipulate strings
# If you want to access a specific character in a string you can use the following syntax
course[0]  # P - The first character in the string, the index starts from 0 in python
print(course[0])  # This will print P in the console

# If you want to access the last character in a string you can use the following syntax
course[-1]  # g - The last character in the string
print(course[-1])  # This will print g in the console

course[-2]  # n - The second last character in the string

# In python there is something called slicing, which means you can access a range of characters in a string
# If you want to access the first 3 characters in a string you can use the following syntax
course[0:3]  # Pyt - The first 3 characters in the string
# The first index is where the slice starts and the second index is where the slice ends
# This means that the slice will start from the first index (0) and end at the second index - 1 (2)

# If you dont specify the first index, the slice will start from the beginning of the string
course[0:]  # Python Programming - The whole string

# If you dont specify the last index, the slice will end at the end of the string
course[:3]  # Pyt - The first 3 characters in the string

# If you want to copy a string you can use the following syntax
course[:]  # Python Programming - The whole string

# If we have a slicing of 1:-1, this means that the slice will start from the second character and end at the second last character
# ython Programmin - The whole string without the first and last character
course[1:-1]

# If you want to add a break line in a string you can use the following syntax
course = "Python \nProgramming"
# Python
# Programming - The \n will add a break line in the string

# For special characters you can use the backslash (\) before the character
course = "Python \"Programming\""  # Python "Programming"

# Some of the special characters are:
# \"
# \'
# \\
# \n - New line
# \t - Tab

# Formatted strings
# If you want to add a variable in a string you can use the following syntax
first = "John"
last = "Doe"
full = first + " " + last  # John Doe

# This is not the best way to add a variable in a string
# If you want to add a variable in a string you can use the following syntax
full = f"{first} {last}"  # John Doe
# This is called formatted string
# You can add any valid expression inside the curly braces
# You can also call functions inside the curly braces
# You can also use the following syntax
x_position = 1
full = f"{len(first)}, {x_position}, {2 + 3}"  # 4, 1, 5

# String methods
# If you want to convert a string to uppercase you can use the following syntax
course = "Python PRogramming"
course.upper()  # PYTHON PROGRAMMING
course.lower()  # python programming
course.title()  # Python Programming

# Lets say the user input a string with white spaces in the beginning or the end
# If you want to remove the white spaces you can use the following syntax
course = "   Python Programming   "
course.strip()  # Python Programming
# You also have rstrip() and lstrip() methods
# rstrip() will remove the white spaces from the right side
# lstrip() will remove the white spaces from the left side

# If you want to find a specific character in a string you can use the following syntax
course = "Python Programming"
course.find("Pro")  # 7 - The index of the first character in the string
# If the character is not found in the string, the find() method will return -1
# If you use lower p in the find() method, it will return -1, as the string does not contain a pro

# If you want to replace a character in a string you can use the following syntax
course = "Python Programming"
course.replace("P", "J")  # Jython Jrogramming

# If you want to check if a character is in a string you can use the following syntax
course = "Python Programming"
"Pro" in course  # True

# If you want to check if a character is not in a string you can use the following syntax
course = "Python Programming"
"swift" not in course  # True
