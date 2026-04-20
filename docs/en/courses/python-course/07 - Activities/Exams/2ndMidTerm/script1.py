# 1. Read the contents of the text file named `menu.txt`.
# This file contains the menu items that you will process.
# 2. Store the contents of the file in a variable.
# Ensure that the entire content is captured in this variable
# as a single string or a list of strings, depending on
# how you choose to read the file.

menu = []
filepath = "./07 - Activities/Exams/2ndMidTerm/"
filename = "menu.txt"

with open(filepath + filename, "r") as file:
    # Read the contents of the file and store them in the 'menu' list
    menu = file.readlines()

    # Remove any leading or trailing whitespace characters
    for line in range(len(menu)):
        menu[line] = menu[line].strip()

# 3. Define a function named `print_menu` that accepts one argument.
# This argument will be the variable where you stored the file's contents.


def print_menu(menu: list) -> None:
    # 4. Inside the print_menu function, write code that
    # prints the contents of the menu to the console.
    for item in menu:
        print(item)


# 5. Call the `print_menu` function to display the menu.
print_menu(menu)
