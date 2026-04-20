# Comparisson Operators

# We use comparisson operators to compare values
# The result of a comparisson operator is a boolean value (True or False)

# Value comparisson operators
# == Equal to
# != Not equal to
# > Greater than
# < Less than
# >= Greater than or equal to
# <= Less than or equal to

print(5 == 5)  # True
print(5 != 5)  # False
print(5 > 5)  # False
print(5 < 5)  # False
print(5 >= 5)  # True
print(5 <= 5)  # True
print()

# You can also compare strings
print("Python" == "Python")  # True
print("Python" != "Python")  # False
print("Python" > "Python")  # False
print("Python" < "Python")  # False
print("Python" >= "Python")  # True
print("Python" <= "Python")  # True
print()

# Lets see two different strings
print("Python" == "python")  # False, because 'P' is not equal to 'p'
print("bag" > "apple")  # True, because 'b' is greater than 'a'
print("bag" == "BAG")  # False, becase letters have numeric values

# Lets see the numeric values of the letters
# ord() is a function that returns the numeric value of a letter
print(ord("b"))  # 98
print(ord("B"))  # 66
