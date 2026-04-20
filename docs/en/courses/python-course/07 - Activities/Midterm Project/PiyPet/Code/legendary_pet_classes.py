from datetime import datetime, timedelta

# Let's start defining the parent class called LegendaryPet


class LegendaryPet:
    # The __init__ method is the constructor of the class
    # It is called when an object of the class is created
    # The self parameter is a reference to the current instance of the class
    # It is used to access variables that belong to the class
    def __init__(self, name, energy=100, hunger=0, happiness=100) -> None:
        # We use default parameters for energy, hunger, and happiness as 100, 0, and 100 respectively.
        # This will help us to have a innitiator for the class that can be used to create objects
        # with default values and also with custom values.
        # For instance, when we load values from a file, we can use the custom values for the innitiator,
        # and when we create a new object, we can use the default values.
        self.name = name
        self.energy = energy
        self.hunger = hunger
        self.happiness = happiness
        self.poke_history = []  # List to keep track of the times when the pet was poked

    # Let's define a method called poke that will increase happiness by 2, but will decrease energy by 1 if
    # if the user has poked the pet more than 10 times in the last 30 seconds.
    # We will use the datetime module to keep track of the time of the last poke. So let's start

    def poke(self):
        # Get the current time
        current_time = datetime.now()

        # Clear out poke times older than 30 seconds
        # The self.poke_history as a condition in an if statement will return True if the list is not empty
        # and False if the list is empty. The second part of the condition will return True if the first element
        # of the list is older than 30 seconds and False if it is not older than 30 seconds.
        # The while loop will keep removing the first element of the list until the first element of the list is older than 30 seconds.
        # In case that all the elements of the list are older than 30 seconds, the list will be empty.
        while self.poke_history and current_time - self.poke_history[0] > timedelta(seconds=30):
            self.poke_history.pop(0)

        self.poke_history.append(current_time)  # Record the time of the poke

        # Decrease happiness by 1 if there are more than 10 pokes in the last 30 seconds
        if len(self.poke_history) > 10:
            self.happiness -= 1
        # Increase happiness by 2 for every poke if there are less than 10 pokes in the last 30 seconds
        else:
            self.happiness += 2

        # Optional: print statements to see what's happening (can be removed or replaced with logging)
        print(f"{self.name}'s happiness is now {self.happiness}.")
