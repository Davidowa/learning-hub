# 1. Define a `Videogame` Class:
#    - **Attributes:** Include attributes for title, year, genre, and platform.
#    - **Methods:**
#      - `print_info()`: Prints the complete information of the video game in a readable format.
class Videogame:
    def __init__(self, title, year, genre, platform):
        self.title = title
        self.year = year
        self.genre = genre
        self.platform = platform

    def print_info(self):
        print(f"{self.title}, ({self.year}) - {self.genre} - {self.platform}")


# 2. Open and read the contents of `videogames.csv`, where each line contains details such
# as title, year, genre, and platform.
videogame_list = []
filepath = "./07 - Activities/Exams/2ndMidTerm/"
filename = "videogames.csv"

with open(filepath + filename, "r") as file:
    for line in file:
        title, year, genre, platform = line.strip().split(",")
        videogame = Videogame(title, year, genre, platform)
        videogame_list.append(videogame)


# 3. Make a function name `print_list_of_videogames` that takes one argument.
# This argument is the list of `Videogame` objects and prints each video game's
# details using the `print_info` method.
def print_list_of_videogames(videogames: list[Videogame]) -> None:
    for game in videogames:
        game.print_info()
    print()


# 4. Make a function name `amount_of_games_per_platform` that takes one argument.
# This argument is the list of `Videogame` objects and prints the count of video
# games per platform.
def amount_of_games_per_platform(videogames: list[Videogame]) -> None:
    platform_count = {}
    for game in videogames:
        if game.platform in platform_count:
            platform_count[game.platform] += 1
        else:
            platform_count[game.platform] = 1

    for platform, count in platform_count.items():
        print(f"{platform}: {count}")
    print()


# 5. Make a function called `add_videogame` that takes one argument.
#  This argument is the list of `Videogame` objects.
#    - This function prompts the user for details of a new video game,
#      creates a `Videogame` object, and appends it to the list.

def add_videogame(videogames: list[Videogame]) -> None:
    title = input("Enter the title of the video game: ")
    year = input("Enter the year of the video game: ")
    genre = input("Enter the genre of the video game: ")
    platform = input("Enter the platform of the video game: ")

    new_game = Videogame(title, year, genre, platform)
    videogames.append(new_game)


# 6. Make a function called `update_file` that takes one argument.
# This argument is the list of `Videogame` objects and writes the
# updated list of video games back to the `videogames.csv` file.
def update_file(videogames: list[Videogame]) -> None:
    with open(filepath + filename, "w") as file:
        for game in videogames:
            file.write(f"{game.title},{game.year},{
                       game.genre},{game.platform}\n")


# 7. Execute Functions:
#    - Call `print_list_of_videogames` to display all video games.
#    - Call `amount_of_games_per_platform` to see how many games each platform has.
#    - Call `add_videogame` to add a new game to the collection.
#    - Call `update_file` to save the updated list to the CSV file.
print_list_of_videogames(videogame_list)
amount_of_games_per_platform(videogame_list)
add_videogame(videogame_list)
update_file(videogame_list)
