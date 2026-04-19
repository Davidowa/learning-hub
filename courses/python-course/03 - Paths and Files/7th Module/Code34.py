from pathlib import Path
from zipfile import ZipFile

# zip files (.zip)
# To work with zip files, we need to import the zipfile module.
# Let's see an example.
# This will create a new zip file and reference it with the zipFile variable.
zip_file = ZipFile("files.zip", "w")

directory = Path() / "03 - Paths and Files/7th Module"
file_path = directory / "test.txt"

# We can now add files to the zip file.
# This will create the zip file in the root directory.
zip_file.write(file_path)
zip_file.close()  # Remember to close the file.


# To save the zip file in a different directory, we can do the following.
directory = Path() / "03 - Paths and Files/7th Module"
zip_file_path = directory / "files.zip"
file_path = directory / "test_copy.txt"
# zipFile = ZipFile(zip_file_path, "w")
# zipFile.write(file_path)
# zip_file.close()

# To zip all the files in a directory, we can do the following.
# Uncomment the following lines to run the code.
# zip = ZipFile("files_all_modules.zip", "w")
# for path in Path().rglob("*.*"):
#     zip.write(path)
# zip.close()

# To zip the files in a specific directory, we can do the following.
# Uncomment the following lines to run the code.
# zip = ZipFile("files_7th_module.zip", "w")
# directory = Path() / "03 - Paths and Files/7th Module"
# for path in directory.rglob("*.*"):
#     zip.write(path)
# zip.close()

# As mentioned before, we can use the with statement to automatically close the file.

# Uncomment the following lines to run the code.
# with ZipFile("files_all_modules_2.zip", "w") as zip:
#     for path in Path().rglob("*.*"):
#         zip.write(path)

# with ZipFile("files_7th_module_2.zip", "w") as zip:
#     directory = Path() / "03 - Paths and Files/7th Module"
#     for path in directory.rglob("*.*"):
#         zip.write(path)

# We can read the contents of a zip file as follows.

with ZipFile("files.zip", "r") as zip:
    # The namelist method will display the contents of the zip file.
    print(zip.namelist())

# We can also extract the files from a zip file.

with ZipFile("files.zip", "r") as zip:
    # The extractall method will extract all the files in the zip file.
    zip.extractall("extracted_files")
