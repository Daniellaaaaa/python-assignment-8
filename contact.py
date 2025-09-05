

# Requirements:
# 1. Store contacts in a dictionary (name → phone number).
# 2. Provide a method to add new contacts.
# 3. Provide a method to delete contacts.
# 4. Provide a method to search for a contact by name.
# 5. Provide a method to show all contacts.

# Example Usage:
#     book = ContactBook()
#     book.add_contact("Alice", "08012345678")
#     print(book.search_contact("Alice"))  # "08012345678"
# """\

class ContactBook:
    def __init__(self):
        self.contacts={}

    def add_contact(self, name, number):
        self.contacts[name]=number
        return f"{name} added succesfully"
    
    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            return f"{name} deleted succesfully"
        else:
            return f"{name} doesn't exist in contact"
        
    def search_contact(self, name):
        if name in self.contacts:
            return f"Found {name} with number: {self.contacts[name]}" 
        else:
            return f"{name} not found in contact" 
        
    def show_contacts(self):
        return self.contacts    

book = ContactBook()
print(book.add_contact("Alice", "08012345678"))
#print(book.delete_contact("Alice"))
print(book.search_contact("Alice"))
print(book.show_contacts())