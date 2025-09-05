
class ShoppingCart:
    def __init__(self, prices):
        self.prices=prices
        self.cart={}
        self.price=0

    def add_item(self, item, quantity):
        self.cart[item]=quantity
        if item in prices:
            self.price= quantity * self.prices[item]
        return f"{item} added successfully"

    def remove_item(self, item, quantity):
        if item in self.cart:
            if quantity<= self.cart[item]:
                self.cart[item]=self.cart[item]-quantity 
                self.price=self.cart[item]*self.prices[item]
                
                return f"{quantity} of {item} removed successfully"
            else:
                return "Insufficient item"
        else:
            return "Item does not exist in cart"   

    def clear_cart(self):
        return self.cart.clear     

    def calculate_total(self):
        return self.price
        

        


prices = {"Shirt": 5000, "Shoes": 12000}
cart = ShoppingCart(prices)
print(cart.add_item("Shirt", 2))
print(cart.calculate_total())
print(cart.cart)
print(cart.remove_item("Shirt", 1))
print(cart.cart)
print(cart.calculate_total())