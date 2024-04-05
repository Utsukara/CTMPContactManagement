import re
import os


# Function to display the user interface
def user_interface():
    global contact_list, group_list
    while True:
        print("Menu:")
        print("1. Add a new contact")
        print("2. Add contact to group")
        print("3. Edit or add to an existing contact")
        print("4. Delete a contact")
        print("5. Search for a contact")
        print("6. Display all contacts")
        print("7. Display contacts in a group")
        print("8. Export contacts to a text file")
        print("9. Import contacts from a text file")
        print("10. Quit")
        choice = input("Enter your choice: ")
        print()
        if choice == "1":
            add_contact(None)
            print()
        elif choice == "2":
            add_to_group()
            print()
        elif choice == "3":
            edit_contact(None)
            print()
        elif choice == "4":
            delete_contact()
            print()
        elif choice == "5":
            search_contact()
            print()
        elif choice == "6":
            display_contacts()
            print()
        elif choice == "7":
            display_group()
            print()
        elif choice == "8":
            export_contacts()
            print()
        elif choice == "9":
            import_contacts()
            print()
        elif choice == "10":
            export_contacts()
            print("Exiting the Contact Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 9.")
            print()



# Global Variables
group_list = {}
contact_list = {}
email_pattern = r"^\S+@\S+\.\S+$"
phone_pattern = r"^(?:\d{10}|\(\d{3}\)-?\d{3}-?\d{4}|\d{3}-\d{3}-\d{4})$"



def add_contact(contact):
    global contact_list
    if contact == None:
        contact = input("Enter the contact's email or phone number: ")
    if re.match(email_pattern, contact):
        name = input("Enter the contact's name: ")
        email = contact
        phone = input("Enter the contact's phone number: ")
        additional_info = input("Enter additional information: ")
        contact_list[contact] = {"phone": phone, "email": email, "name": name, "additional_info": additional_info}
        print("Contact added successfully.")
    elif re.match(phone_pattern, contact):
        name = input("Enter the contact's name: ")
        phone = contact
        email = input("Enter the contact's email: ")
        additional_info = input("Enter additional information: ")
        contact_list[contact] = {"phone": phone, "email": email, "name": name, "additional_info": additional_info}
        print("Contact added successfully.")
    else:
        print("Invalid contact information. Please enter a valid email or phone number.")



def add_to_group():
    global group_list
    group = input("Enter the group name: ")
    if group not in group_list:
        group_list.update({group: []})
    contact = input("Enter the contact's email or phone number to add to group: ")
    if contact in contact_list:
        group_list[group].append(contact)
        print("Contact added to group successfully.")
    else:
        print("Contact does not exist.")



def edit_contact(contact):
    global contact_list
    if contact == None:
        contact = input("Enter the contact's email or phone number to edit: ")
    if contact in contact_list:
        print("Contact found. Enter the new details:")
        name = input("Enter the contact's name: ")
        email = input("Enter the contact's email: ")
        phone = input("Enter the contact's phone number: ")
        additional_info = input("Enter additional information: ")
        contact_list[contact] = {"phone": phone, "email": email, "name": name, "additional_info": additional_info}
        print("Contact details updated successfully.")
    elif contact not in contact_list:
        print("Contact does not exist. Would you like to add this contact? (Y/N)")
        choice = input()
        if choice.lower() == "y":
            add_contact(contact)
        else:
            print("Contact does not exist and will not be added.")



def delete_contact():
    global contact_list, group_list
    delete = input("Enter the contact's email or phone number to delete: ")
    if re.match(email_pattern, delete) or re.match(phone_pattern, delete):
        if delete in contact_list:
            del contact_list[delete]
            print("Contact deleted successfully.")
        else:
            for key, value in contact_list.items():
                if delete in value["name"].lower():
                    del contact_list[key]
                    print("Contact deleted successfully.")
                    return
                else:
                    print("Contact not found.") 



def search_contact():
    global contact_list
    #search by name, phone number, or email
    search = input("Enter the contact's name, email or phone number to search: ")
    search = search.lower()
     # Check for email pattern
    if re.match(email_pattern, search):
        for key, value in contact_list.items():
            if value["email"].lower() == search:
                print(f"Name: {value['name']}\nEmail: {value['email']}\nPhone: {value['phone']}\nAdditional Info: {value['additional_info']}")
                return  
    # Check for phone number pattern
    elif re.match(phone_pattern, search):
        for key, value in contact_list.items():
            if value["phone"] == search:
                print(f"Name: {value['name']}\nEmail: {value['email']}\nPhone: {value['phone']}\nAdditional Info: {value['additional_info']}")
                return              
    # Assume name search if no pattern match
    else:
        for key, value in contact_list.items():
            if search in value["name"].lower():
                print(f"Name: {value['name']}\nEmail: {value['email']}\nPhone: {value['phone']}\nAdditional Info: {value['additional_info']}")
                return
            else:
                print("Contact not found.")



def display_contacts():
    global contact_list
    #sort by name and display
    sorted_contacts = sorted(contact_list.items(), key=lambda x: x[1]["name"])
    contact_list = dict(sorted_contacts)
    for key, value in sorted_contacts:
        print(f"Name: {value['name']}\nEmail: {value['email']}\nPhone: {value['phone']}\nAdditional Info: {value['additional_info']}\n")



def display_group():
    global group_list
    group = input("Enter the group name to display contacts: ")
    if group in group_list:
        #sort list by contact name
        sorted_contacts = sorted(group_list[group], key=lambda x: contact_list[x]["name"])
        group_list[group] = sorted_contacts
        for contact in sorted_contacts:
            print(f"Name: {contact_list[contact]['name']}\nEmail: {contact_list[contact]['email']}\nPhone: {contact_list[contact]['phone']}\nAdditional Info: {contact_list[contact]['additional_info']}\n")
        


def export_contacts():
    with open("contacts.txt", "w") as file:
        for contact in contact_list.values():
            line = f"{contact['name']}, {contact['phone']}, {contact['email']}, {contact['additional_info']}\n"
            file.write(line)
    print("Contacts exported to contacts.txt successfully.")




def import_contacts():
    global contact_list
    if os.path.exists("contacts.txt"):
        with open("contacts.txt", "r") as file:
            for line in file:
                parts = line.strip().split(", ")
                if len(parts) >= 4:  # Ensure there are at least 4 parts
                    name, phone, email, additional_info = parts[0], parts[1], parts[2], parts[3]
                    contact_key = email  # Using email as the key; adjust as needed
                    contact_list[contact_key] = {"phone": phone, "email": email, "name": name, "additional_info": additional_info}
                else:
                    print(f"Skipping incomplete contact: {line.strip()}")
        print("Contacts imported from contacts.txt successfully.")
    else:
        print("No contacts to import.")




if __name__ == "__main__":
    print("Welcome to the Contact Management System.")
    import_contacts()
    user_interface()