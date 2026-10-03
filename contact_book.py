# MIni Project 5   Contact Book



contacts = []


# Add Contact
def add_contact():
    contact = {
        "name": input("Name: "),
        "phone": input("Phone: "),
        "email": input("Email: ")
    }

    contacts.append(contact)

    print("Contact Added Successfully! ")


# View contacts

def view_contacts():
    print("\n ---Contact Book--- ")


    for contact in contacts:
        print(contact)


# Serch contacts

def search_contact():
    search_name = input("Enter Name To Search: ")


    for contact in contacts:
        if contact["name"].lower() == search_name.lower():
            print("\nContact Found!")
            print(contact)
            return

    print("Contact Not Found!")


# Delete Contact

def delete_contact():
    delete_name = input("Enter name to delete: ")


    for contact in contacts:
        if contact["name"].lower() == delete_name.lower():
            contacts.remove(contact)
            print("Contact Deleted Successfully!")
            return

    print("Contact Not Found!")



while True:
    print("\n--- Contact Book ---")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_contact()

    elif choice == "2":
        view_contacts()

    elif choice == "3":
        search_contact()

    elif choice == "4":
        delete_contact()

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid Choice!")


add_contact()
view_contacts()
delete_contact()
search_contact()