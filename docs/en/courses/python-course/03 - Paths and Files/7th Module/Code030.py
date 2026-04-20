# Working with Files in Python

# Lets start by importing the pathlib module.

from pathlib import Path
from time import ctime
import shutil

# Create the path to the current directory.
path = Path() / "03 - Paths and Files/7th Module" / "Code030.py"

# Check if the path exists.
print(path.exists())  # True

print(path.stat())  # This will display information about the file.

# os.stat_result(st_mode=33206, st_ino=1125899907072335, st_dev=3656981857665640941, st_nlink=1, st_uid=0, st_gid=0, st_size=358, st_atime=1706578508, st_mtime=1706578508, st_ctime=1698224369)
# st_atime: time of most recent access
# st_mtime: time of most recent content modification
# st_ctime: time of creation

# These values are in seconds since the epoch. It depends on the operating system.
# To convert them to a datetime object, we can use the ctime module.

print(ctime(path.stat().st_ctime))  # This is the creation time of the file

# We can use the read_text method to read the contents of the file.
print(path.read_text())

# A different way to read the contents of the file is to use the open method.

with open(path, "r") as file:
    print(file.read())

# It is worth nothing that the read_text method is more efficient than the open method.
# This is because in the read_text method, the file is opened and closed automatically.

# We can also write to a file.
# Let's see an example.

path = Path() / "03 - Paths and Files/7th Module" / "test.txt"
with open(path, "a") as file:
    file.write("# Working with Files in Python\n")

# In this case, the "a" means that we want to append to the file.
# We also have the "w" option which means that we want to overwrite the file.
# And, as we saw in line 31, we have the "r" option which means that we want to read the file.

# Now, we can instead use the write_text method.

path = Path() / "03 - Paths and Files/7th Module" / "test.txt"
path.write_text("# Working with Files in Python with write_text\n")

# This will overwrite the file.

# To preserve the contents of the file, we need to combine the read_text and write_text methods.

path = Path() / "03 - Paths and Files/7th Module" / "test.txt"
path.write_text(path.read_text() + "# Adding a new line\n")

# Lastly, we can use the shutil module to copy files directly from Python.
source = Path() / "03 - Paths and Files/7th Module" / "test.txt"
target = Path() / "03 - Paths and Files/7th Module" / "test_copy.txt"

shutil.copy(source, target)
