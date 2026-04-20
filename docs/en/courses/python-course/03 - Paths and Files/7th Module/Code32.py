from pathlib import Path
import csv

# CSV files (.csv)
# CSV stands for comma-separated values.
# Its a simplify spreadsheet stored as a plain text file.
# We need to import the csv module to work with CSV files.

# In this folder we have a file called sample.csv.
# It contains the following information:
# Username, Identifier, First name, Last name

# We can open the file as follows.
file_path = Path() / "03 - Paths and Files/7th Module" / "sample.csv"
file = open(file_path, "r")
file.close()

# However, this is not the best way to open a file.
with open(file_path, "r") as file:
    print(file.read())


# Now, if we want to read the file and store the information in a list, we can do the following.

# If we want to preserve the data after the with statement, we need to create a empty list before the with statement.
data = []
with open(file_path, "r") as file:
    csv_reader = csv.reader(file)
    # This will return an object.
    # We can convert it to a list as follows.
    data = list(csv_reader)
    # This will display the data in a list of lists, as each row is a list.
    print(data)
    print()

# Now using the data list, we can access the information in the file.

for row in data:
    print(row)
print()

# Another thing we can do is while reading the file, we can remove the header.

with open(file_path, "r") as file:
    csv_reader = csv.reader(file)
    # This will return an object.
    # We can convert it to a list as follows.
    data = list(csv_reader)

    # Now we can remove the header.
    header = data.pop(0)
    print(header)
    print(data)
    print()

# Lastly, we can also use dictionaries to store the information.
# Let's see an example.

data = []  # This will store the information as a list of dictionaries.
keys = []  # This will store the keys of the dictionaries.
with open(file_path, "r") as file:
    csv_reader = csv.DictReader(file)
    data = list(csv_reader)
    # store the keys in a variable
    keys = data[0].keys()
    print(data)
    print()

# Now lets print the information of the first row using the keys.
for key in keys:
    print(key, "\t: ", data[0][key])

# To write to a CSV file, we can use the csv module.
# Let's see an example.

file_path = Path() / "03 - Paths and Files/7th Module" / "data.csv"

# Open the file with the newline parameter set to an empty string
with open(file_path, "w", newline='') as file:
    csv_writer = csv.writer(file)
    # We can write the header as follows.
    # The wreiterow method takes a list as an argument.
    csv_writer.writerow(["transaction_id", "product_id", "price"])
    # Now we can write the data.
    csv_writer.writerow([1000, 1, 5])
    csv_writer.writerow([1001, 2, 15])
