# Exceptions with Files
# There are times when you want to work with external resources.
# For example, you may want to read data from a file.
# Or you may want to connect to a database.
# Or you may want to send an HTTP request to a web service.

# Handling exceptions is important while working with file I/O.
# This is to gracefully handle scenarios where the file might not exist or you don't have the permission to read it.

from pathlib import Path

try:
    file_path = Path() / "03 - Paths and Files/7th Module" / "x.txt"
    with open(file_path, 'r') as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print(f"The file at {file_path} was not found.")
except IOError:
    print(f"An error occurred while reading the file at {file_path}.")


# As we can see, in all of these cases, you need to open a connection to the resource.
# And once you're done, you need to close it.

# And this is where try and finally statements come in handy.
# Let's see an example.

# try:
#     file = open("app.py")
# except Exception as ex:
#     print("Could not open the file")
# else:
#     print("File opened successfully")
# finally:
#     file.close() # This will always be executed, but if the file does not exist, it will throw an error.


# However, if an object has a method called "__exit__", we can use it with a with statement.
# The with statement will automatically close the connection to the resource.
# Lets see an example.

try:
    with open("app.py") as file:
        print("File opened")
except Exception as ex:
    print("Could not open the file")
