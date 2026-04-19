def display_menu():
    print("\nContact Book Menu")
    print("1. Add Contact")
    print("2. Update Contact")
    print("3. Delete Contact")
    print("4. List All Contacts")
    print("5. Exit")
    choice = input("Enter your choice: ")
    return choice

def add_contact(contact_book):
    name = input("Enter contact name: ")
    if name in contact_book:
        print("Contact already exists.")
    else:
        phone = input("Enter phone number: ")
        email = input("Enter email address: ")
        contact_book[name] = {"phone": phone, "email": email}
        print("Contact added successfully.")

def update_contact(contact_book):
    name = input("Enter the name of the contact to update: ")
    if name not in contact_book:
        print("Contact not found.")
    else:
        phone = input("Enter new phone number: ")
        email = input("Enter new email address: ")
        contact_book[name] = {"phone": phone, "email": email}
        print("Contact updated successfully.")

def delete_contact(contact_book):
    name = input("Enter the name of the contact to delete: ")
    if name in contact_book:
        del contact_book[name]
        print("Contact deleted successfully.")
    else:
        print("Contact not found.")

def list_contacts(contact_book):
    if not contact_book:
        print("The contact book is empty.")
    else:
        for name, details in contact_book.items():
            print(f"\nContact Name: {name}")
            print(f"Phone Number: {details['phone']}")
            print(f"Email: {details['email']}")

contact_book = {}
while True:
    choice = display_menu()
    if choice == "1":
        add_contact(contact_book)
    elif choice == "2":
        update_contact(contact_book)
    elif choice == "3":
        delete_contact(contact_book)
    elif choice == "4":
        list_contacts(contact_book)
    elif choice == "5":
        print("Exiting program.")
        break
    else:
        print("Invalid choice, please try again.")
