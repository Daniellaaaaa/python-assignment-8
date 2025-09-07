class RestaurantOrder:
    def __init__(self, prices):
        self.prices=prices
        self.orders={}

    def add_item(self, item, quantity): 
        if item not in self.orders:
            self.orders[item]=quantity
            return f"{item} added to order"
        else:
            self.orders[item]+=quantity
            return f"{quantity} more {item} added to order"  
        
    def remove_items(self, item):
        if item in self.orders:
            del self.orders[item] 
            return f"{item} removed successfully!"
        else:
            return f"{item} is not in order"   
        
    def calculate_total(self):
        total=0
        for key, value in self.orders.items():
            if key in self.prices:
                add=value*self.prices[key]
                total+=add
            else:
                return f"{key} not in price list"
        return f"Total Bill: {total}"        


    def show_orders(self):
        return f"Orders: {self.orders}"    
        



prices = {"Pizza": 2000, "Burger": 1500, "Drink": 500}
order = RestaurantOrder(prices)

print(order.add_item("Pizza", 2))
print(order.add_item("Drink", 3))
# print(order.remove_items("Drink"))
print(order.show_orders())

print(order.calculate_total())  
