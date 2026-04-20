# When working with data, databases are essential.
# A database is a structured collection of data stored in a computer system.
# While databases can exist in various forms, they're most commonly
# hosted on servers, which can be on-premises or in the cloud.
# There are many types of databases, but we will focus on relational databases.

# The relational database was invented by E. F. Codd at IBM in 1970.
# In a relational database, data is stored in tables.
# Each table has columns and rows, similar to a spreadsheet.
# Each column has a name and a data type.
# Each row is a record, which is a collection of related data.
# Each record has a unique identifier, which is called a primary key.
# The primary key is used to identify each record in a table.
# To relate data between tables, we use foreign keys.
# A foreign key is a column in a table that references the primary key of another table.

# When working with relational databases, we use SQL, which stands for Structured Query Language.

# In python, we can use the sqlite3 module to work with SQLite databases.

from pathlib import Path
import os
import sqlite3
import json

# Lets read the JSON we created in the previous module.
# Note: We can also use csv, excel, etc to load data into a database.
file_path = Path() / "03 - Paths and Files/7th Module" / "pixar_movies.json"

pixar_movies = json.loads(file_path.read_text())
print(pixar_movies)
print()

# Now let's create a database.
database_file = Path() / "04 - SQLite/8th Module" / "pixar_movies.db"

# Connect to the SQLite database using the path
# Let us delete the file before running the code, otherwise you will get an error of 'table already exists' or repeated data.

if database_file.exists():
    # If it exists, delete the file
    os.remove(database_file)

with sqlite3.connect(database_file) as connection:
    create_command = "CREATE TABLE IF NOT EXISTS Movies (id INTEGER PRIMARY KEY, title TEXT NOT NULL, year INTEGER NOT NULL)"
    connection.execute(create_command)

    for movie in pixar_movies:
        # The question marks are placeholders.
        insert_command = "INSERT INTO Movies VALUES (?, ?, ?)"
        # The placeholders are replaced by the values in the tuple.
        connection.execute(
            insert_command, (movie["id"], movie["title"], movie["year"]))
    # Commit the changes to the database.
    connection.commit()

# Now the database 'pixar_movies.db' should be in the '04 - SQLite/8th Module' directory.

# We can visualize the database using DB Browser for SQLite.
# https://sqlitebrowser.org/dl/
# Download the appropriate version for your operating system.

# Now the database is created, filled with the data from the JSON file, and saved.

# Now lets query the database.
# A query is a request for data from a database table or combination of tables.
# We use the SELECT statement to query the database.

# Lets query all the movies.

with sqlite3.connect(database_file) as connection:
    select_command = "SELECT * FROM Movies"
    # When we execute the command, we get a cursor object.
    # A cursor is virtual pointer that helps navigate through the database.
    # You use a cursor to execute queries and retrieve results.
    cursor = connection.execute(select_command)
    for row in cursor:
        # For each row, we get a tuple.
        print(row)
    # We can also get all the rows at once using the fetchall method.
    # fetched_pixar_movies = cursor.fetchall()
    # print(fetched_pixar_movies)
    # However, as we have already iterated through the cursor, it is empty.
    # To see the results again, we need to execute the query again or comment lines 71-73 and uncomment line 75 and 76.
    print()


# Databases and queries are beyond the scope of this course.
# However, I uploaded a book on Moodle that you can read if you want to learn more about databases.

# But lets see one last topic before we move on.
# Let's see how we can use SQL to filter the results.
# We use the WHERE clause to filter the results.

with sqlite3.connect(database_file) as connection:
    select_command = "SELECT * FROM Movies WHERE year > 2010"
    cursor = connection.execute(select_command)
    for row in cursor:
        print(row)

# Now lets how we can relate data between tables.
# We will create a new table called 'MovieViewers'.
# This table will have the following columns:
# id: The primary key of the table.
# movie_id: The foreign key that references the primary key of the Movies table.
# name: The name of the viewer.
# last_name: The last name of the viewer.
        
# Lets read the movie_viewers.json file.

file_path = Path() / "04 - SQLite/8th Module" / "movie_viewers.json"

movie_viewers = json.loads(file_path.read_text())

# Now lets create the table.

with sqlite3.connect(database_file) as connection:
    create_command = "CREATE TABLE IF NOT EXISTS MovieViewers (id INTEGER PRIMARY KEY, movie_id INTEGER NOT NULL, name TEXT NOT NULL, last_name TEXT NOT NULL, FOREIGN KEY (movie_id) REFERENCES Movies(id))"
    connection.execute(create_command)

    for viewer in movie_viewers:
        insert_command = "INSERT INTO MovieViewers VALUES (?, ?, ?, ?)"
        connection.execute(
            insert_command, (viewer["id"], viewer["movie_id"], viewer["name"], viewer["last_name"]))
    connection.commit()

print()
# You can notice that the movie_id column is a foreign key that references the primary key of the Movies table.
# This is how we relate data between tables. By doing this, we can join the tables and get the data we want.
# In this case we have a one-to-many relationship between the Movies and MovieViewers tables.
# This type of relationship is one of the most common types of relationships in relational databases.
    
# Now lets query the database to get the viewers of a specific movie.
# We will use the INNER JOIN clause to join the tables.

# Lets say we want to get the viewers of the movie 'Toy Story'.

movie_title = "Toy Story"

with sqlite3.connect(database_file) as connection:
    select_command = "SELECT * FROM Movies INNER JOIN MovieViewers ON Movies.id = MovieViewers.movie_id WHERE Movies.title = ?"
    cursor = connection.execute(select_command, (movie_title,))
    for row in cursor:
        print(row)

# The sintax of the INNER JOIN clause is:
# SELECT * - The asterisk means all the columns.
# FROM table1
# INNER JOIN table2
# ON table1.column = table2.column - This is the relationship between foreign key and primary key.
# WHERE table1.column = value - This is the filter.