from pathlib import Path
import json

# JSON files (.json)
# JSON stands for JavaScript Object Notation.
# Its a popular format for storing data in a human-readable way.
# For instance, Spotify uses JSON to store information about songs, artists, and albums.
# Other popular services like Twitter, Facebook, and YouTube also use JSON to store data.
# Also, if you want to build a web application, you'll need to know how to work with JSON.

# We start by importing the json module.
# JSON usually contains a collection of key-value pairs, in other words, a dictionary.
# Lets create a dictionary of Pixar movies.

pixar_movies = [
    {"id": 1, "title": "Toy Story", "year": 1995},
    {"id": 2, "title": "A Bug's Life", "year": 1998},
    {"id": 3, "title": "Toy Story 2", "year": 1999},
    {"id": 4, "title": "Monsters, Inc.", "year": 2001},
    {"id": 5, "title": "Finding Nemo", "year": 2003},
    {"id": 6, "title": "The Incredibles", "year": 2004},
    {"id": 7, "title": "Cars", "year": 2006},
    {"id": 8, "title": "Ratatouille", "year": 2007},
    {"id": 9, "title": "WALL-E", "year": 2008},
    {"id": 10, "title": "Up", "year": 2009},
    {"id": 11, "title": "Toy Story 3", "year": 2010},
    {"id": 12, "title": "Cars 2", "year": 2011},
    {"id": 13, "title": "Brave", "year": 2012},
    {"id": 14, "title": "Monsters University", "year": 2013},
    {"id": 15, "title": "Inside Out", "year": 2015},
    {"id": 16, "title": "The Good Dinosaur", "year": 2015},
    {"id": 17, "title": "Finding Dory", "year": 2016},
    {"id": 18, "title": "Cars 3", "year": 2017},
    {"id": 19, "title": "Coco", "year": 2017},
    {"id": 20, "title": "Incredibles 2", "year": 2018},
    {"id": 21, "title": "Toy Story 4", "year": 2019},
    {"id": 22, "title": "Onward", "year": 2020},
    {"id": 23, "title": "Soul", "year": 2020},
    {"id": 24, "title": "Luca", "year": 2021},
    {"id": 25, "title": "Turning Red", "year": 2022},
    {"id": 26, "title": "Lightyear", "year": 2022},
]

# We usually have the attribute "id" because it is a unique identifier.
# This will be useful when we want to search for a specific movie or when we work with databases.

# We can convert this dictionary to a JSON string using the json.dumps() method.

json_string = json.dumps(pixar_movies)
print(json_string)
print()
# When we print the json_string, we can see it has the same structure as the dictionary.

# Now lets write this string to a file.
file_path = Path() / "03 - Paths and Files/7th Module" / "pixar_movies.json"
file_path.write_text(json_string)

# Now lets read the file.
data = file_path.read_text()

# We can convert this string to a dictionary using the json.loads() method.
read_pixar_movies = json.loads(data)
print(read_pixar_movies)
