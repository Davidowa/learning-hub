# Modules
# Modules are pieces of code that other people have written to fulfill common tasks,
# such as generating random numbers, performing mathematical operations, etc.

# This means that we should split our code into different files.

# A module should contain related functions, classes and other things.

# Lets say we have two functions: calculate_tax and calculate_shipping.
# These two functions are related to e-commerce.
# Therefore, we should put these two functions in a file called ecommerce.py.

# To use a module in a file, we first have to import it with the import statement.

# Example Folder Structure:
# 06 - Advanced
# └── A01 - Modules
#     ├── sales.py
#     └── app.py

# Module search path
# When we import a module, Python looks at different places to find it.
# The places where Python searches for modules are called paths.
# To see the paths, we can use the sys module.

import sys
import sales  # This is the file ecommerce.py
# We can also import specific functions from a module.
from sales import tax_rate, calculate_tax
# We can also import all the functions in a module.
# But this is not recommended because it can cause name collisions.
from sales import *
# We can also import a module with an alias.
import sales as s

# print(sys.path)
# ['C:\\Users\\User\\Desktop\\Python\\Python\\06 - Advanced\\A01 - Modules',
# 'C:\\Users\\User\\AppData\\Local\\Programs\\Python\\Python39\\python39.zip',
# 'C:\\Users\\User\\AppData\\Local\\Programs\\Python\\Python39\\DLLs',
# 'C:\\Users\\User\\AppData\\Local\\Programs\\Python\\Python39\\lib',
# 'C:\\Users\\User\\AppData\\Local\\Programs\\Python\\Python39',
# 'C:\\Users\\User\\AppData\\Roaming\\Python\\Python39\\site-packages',
# 'C:\\Users\\User\\AppData\\Local\\Programs\\Python\\Python39\\lib\\site-packages']

# These are the paths where Python searches for modules.

# For the sales module to be available in the file app.py, we have to import it.

# Now we can use the sales module.

sales.tax_rate

# Because we imported the variable or functions, we don't need to use the module name.

tax_rate

# Because we imported the module with an alias, we can use the alias instead of the module name.

s.tax_rate

# Recommendation, use the module name to call the functions because it is more readable.

# When we run this file, Python creates a variable called __pycache__
# This variable contains the compiled code of the module.
# This means that the next time we run the file, Python will use the compiled code instead of compiling the code again.
# This speeds up the execution of the program.
