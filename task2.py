import csv

CSV_FILE = 'contacts.csv'

def initialize_csv():
    with open(CSV_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        file.seek(0, 2)  # Move to the end of the file
        if file.tell() == 0:
            writer.writerow(['Name', 'Phone', 'Email', 'Address'])

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    
    with open(CSV_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name, phone, email, address])
    print("Contact added successfully!")

def view_contacts():
    with open(CSV_FILE, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(', '.join(row))

def update_contact():
    name_to_update = input("Enter the name of the contact to update: ")
    updated = False

    contacts = []
    with open(CSV_FILE, mode='r') as file:
        reader = csv.reader(file)
        contacts = list(reader)
    
    with open(CSV_FILE, mode='w', newline='') as file:
        writer = csv.writer(file)
        for row in contacts:
            if row[0] == name_to_update:
                name = input("Enter new name: ")
                phone = input("Enter new phone number: ")
                email = input("Enter new email: ")
                address = input("Enter new address: ")
                writer.writerow([name, phone, email, address])
                updated = True
            else:
                writer.writerow(row)
    
    if updated:
        print("Contact updated successfully!")
    else:
        print("Contact not found.")

def delete_contact():
    name_to_delete = input("Enter the name of the contact to delete: ")
    deleted = False

    contacts = []
    with open(CSV_FILE, mode='r') as file:
        reader = csv.reader(file)
        contacts = list(reader)
    
    with open(CSV_FILE, mode='w', newline='') as file:
        writer = csv.writer(file)
        for row in contacts:
            if row[0] == name_to_delete:
                deleted = True
                continue
            writer.writerow(row)
    
    if deleted:
        print("Contact deleted successfully!")
    else:
        print("Contact not found.")

def search_contact():
    search_term = input("Enter name, phone, email, or address to search: ")
    found = False

    with open(CSV_FILE, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            if search_term in row:
                print(', '.join(row))
                found = True
    
    if not found:
        print("No contact found with that information.")

def main():
    initialize_csv()

    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. Search Contact")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            update_contact()
        elif choice == '4':
            delete_contact()
        elif choice == '5':
            search_contact()
        elif choice == '6':
            print("Exiting Contact Book.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
