"""
TASK: Create an Inventory class.

Requirements:
1. Store items in a dictionary (item_name → quantity).
2. Provide a method to add items (with quantity).
3. Provide a method to remove items (only if available).
4. Provide a method to update stock levels.
5. Provide a method to display all inventory items.

Example Usage:
    treasure_store = Inventory()
    favour_store = Inventory()

    treasure_store.add_item("Apples", 50)
    treasure_store.add_item("Bananas", 30)
    treasure_store.remove_item("Apples", 10)
    print(treasure_store.show_inventory())  # {"Apples": 40, "Bananas": 30}

    favour_store.add_item("Milk", 50)
    favour_store.add_item("Garri", 30)
    favour_store.remove_item("Milk", 40)
    print(treasure_store.show_inventory())  # {"Milk": 10, "Garri": 30}
"""

class Inventory:
    def __init__(self):
        self.inventory_dict={}

    def add_item(self, item, quantity):
        if item not in self.inventory_dict:
            self.inventory_dict[item]=quantity
            return f"{item} added successfully"
        else:
            return f"{item} already exist"
        
    def remove_item(self, item, quantity):
        if item in self.inventory_dict:
            if quantity<=self.inventory_dict[item]:
                self.inventory_dict[item]-=quantity
                return f"{quantity} {item} removed successfully" 
            else:
                return f"{item} out of stock"

        else:
            return f"{item} isn't in the dictionary"
        

    def update_item(self, item, quantity):
        if item in self.inventory_dict:
            self.inventory_dict[item]+=quantity
            return f"{quantity} {item} added successfully" 
        else:
            return f"{item} isn't in the dictionary"

        
    def show_inventory(self):
        return self.inventory_dict



treasure_store = Inventory()
favour_store = Inventory()


treasure_store.add_item("Apples", 50)
treasure_store.add_item("Bananas", 30)
treasure_store.remove_item("Apples", 10)
print(treasure_store.show_inventory())

favour_store.add_item("Milk", 50)
favour_store.add_item("Garri", 30)
favour_store.remove_item("Milk", 40)
print(favour_store.show_inventory())

# print(treasure_store.add_item("Apples", 50))
# print(treasure_store.add_item("Apples", 50))
# print(treasure_store.add_item("Bananas", 30))
# print(treasure_store.show_inventory())
# print(treasure_store.remove_item("Apples", 10))
# print(treasure_store.show_inventory())
# print(treasure_store.update_item("Apples", 40))
# print(treasure_store.show_inventory())


