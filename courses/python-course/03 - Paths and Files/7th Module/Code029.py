# Paths and Directories in Files
# There are times when you want to work with external resources.
# These live in directories.
# A useful module for working with directories is the "pathlib" module.
# Let's see an example.

from pathlib import Path

path = Path()  # This provides the current directory.
print(path)  # .
print(path.exists())  # True
print(path.resolve())  # This will display the absolute path to the directory
print(path.is_file())  # False
print(path.is_dir())  # True

# But maybe we want the Path to be the 7th Module directory.
# We can do this as follows.
path = Path("03 - Paths and Files/7th Module")
print(path.resolve())  # This will display the absolute path to the directory

# To access this file, we can use the Path as follows.
file_path = Path("03 - Paths and Files/7th Module/Code029.py")
print(path)
print(file_path.exists())  # True
print(file_path.resolve())  # This will display the absolute path to the file
print(file_path.is_file())  # True
print(file_path.name)  # Code029.py
print(file_path.stem)  # Code029
print(file_path.suffix)  # .py
print(file_path.parent)  # 03 - Paths and Files/7th Module

# We can also create a new file.
# Let's see an example.
new_file_path = file_path.with_name("Code029.txt")
print(new_file_path)  # 03 - Paths and Files/7th Module/Code029.txt
print(new_file_path.absolute())  # It is the same as resolve()

# We can also iterate over the files in a directory.
# Let's see an example.
workspace_path = Path()

paths = [path for path in workspace_path.iterdir() if path.is_dir()]
py_files_in_folder = [file for file in workspace_path.glob("*.py")]
print(paths)
# It is empty as there are no .py files in the current directory
print(py_files_in_folder)

# To check subfolders, we can use the rglob method.
py_files_in_subfolder = [file for file in workspace_path.rglob("*.py")]
print(py_files_in_subfolder)

# We can also create a new path variable.
# Let's see an example.

new_path = Path(r"C:\Users\user\Desktop")

# In this case, we have to use the raw string.
# A raw string is a string that is prefixed with an r.
# This means that the string is interpreted as it is written.
# This is useful when we want to write a path.

# For macOS and Linux, we can use the following.
new_path = Path("/Users/user/Desktop")

# Lastly, we can also combine paths.
# Let's see an example.

new_path = Path(r"C:\Users\user\Desktop") / "Folder" / "File.txt"

# In this case, we have joined the paths and created a new path to the file.
