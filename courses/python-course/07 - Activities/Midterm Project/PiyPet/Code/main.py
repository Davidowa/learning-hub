from legendary_pet_classes import LegendaryPet

# Example usage
pet = LegendaryPet("Fluffy")
while True:
    print("What would you like to do?")
    print("1. Poke")
    print("2. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        pet.poke()
    elif choice == "2":
        break
    else:
        print("Invalid choice")
