# Now lets see how to work with different types of files.
# The main types of files are:
# Text files (.txt)
# CSV files (.csv)
# JSON files (.json)
# zip files (.zip)

from pathlib import Path

# Lets start with the first type of file.
# Text files (.txt)
# Text files are the simplest type of files.
# They contain plain text or they can contain structured data.

# To work with text files in Python, we use built-in functions.
# The most common way to read a text file is by using the 'open' function.

# The 'open' function requires the path to the file.
# Optionally, you can specify the mode in which the file should be opened, like 'r' for read or 'w' for write.
# By default, 'open' uses 'r' (read) mode.

# Let's start with a simple example of opening and reading a file.

# Specify the path to your text file
file_path = Path() / "03 - Paths and Files/7th Module" / "sample.txt"
file = open(file_path, "r")
file.close()

# Open the file using 'with' statement which ensures the file is properly closed after its suite finishes
with open(file_path, 'r') as file:
    # Read the content of the file
    content = file.read()

    # Print the content of the file
    print(content)
    print()

# The 'read' method reads the entire content of the file.
# If the file is large, this might not be the most efficient way.

# An alternative way is to read the file line by line using a loop.
# This is more memory-efficient, especially for large files.

with open(file_path, 'r') as file:
    # Iterate over each line in the file
    for line in file:
        # Print each line
        # 'strip' removes any leading/trailing whitespace including newlines
        print(line.strip())
    print()

# Sometimes, you might want to process each line differently or store it in a data structure.
# For example, storing each line in a list.

lines = []  # List to store lines

with open(file_path, 'r') as file:
    # Read each line and add it to the list
    for line in file:
        lines.append(line.strip())

# Now 'lines' contains each line of the file as a separate element in the list
print(lines)
print()

# Now lets see structure data.
# Text files can sometimes contain structured data with separators.
# Common separators include commas, tabs, or even spaces.
# While CSV files typically use commas, other text files might use different separators.

# Let's assume our text file uses semi-colons as separators.

file_path = Path() / "03 - Paths and Files/7th Module" / "data.txt"

# Open and read the file
with open(file_path, 'r') as file:
    # Iterate over each line in the file
    for line in file:
        # Split the line into parts using the comma as separator
        parts = line.strip().split(';')

        # Now 'parts' is a list where each element is a piece of data from the line
        # You can process these parts as needed
        print(parts)
    print()

# Now lets see how to create a dictionary from a text file.
# Open and read the file
with open(file_path, 'r') as file:
    # Read the first line (header) and split it into keys
    header = file.readline().strip().split(';')

    # Iterate over the remaining lines in the file
    for line in file:
        # Split the line into parts using semi-colon as separator
        parts = line.strip().split(';')

        # Create a dictionary from the header and parts
        # Zip together the header and parts and create a dictionary
        row_dict = dict(zip(header, parts))

        # Now 'row_dict' is a dictionary where each key is from the header
        # and the corresponding value is from the current line
        # You can process this dictionary as needed
        print(row_dict)

# Finally, lets see how to write to a text file.

file_path = Path() / "03 - Paths and Files/7th Module" / "example.txt"

# Writing to a text file
# This will create a new file if it doesn't exist, or overwrite it if it does
with open(file_path, 'w') as file:
    file.write("This is the first line of the file.\n")
    file.write("This is the second line of the file.\n")

# Appending to a text file
# If the file doesn't exist, it will be created.
# If it does exist, the new content will be added at the end of the file.
with open(file_path, 'a') as file:
    file.write("This line is appended to the file.\n")
    file.write("This is another appended line.\n")
