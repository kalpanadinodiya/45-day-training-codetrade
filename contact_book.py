contacts = [
    {"name": "Alex", "phone": "12345", "email": "alex@gmail.com"},
    {"name": "John", "phone": "67890", "email": "john@gmail.com"}
]

def find_contact(name):

    for contact in contacts:

        if contact["name"].lower() == name.lower():
            return contact

    return "Contact not found"

search = input("Enter contact name: ")

print(find_contact(search))