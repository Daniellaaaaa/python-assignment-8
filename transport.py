class Bus:
    def __init__(self, capacity):
        self.capacity=capacity
        self.passengers=[]

    def add_passenger(self, name):
        if len(self.passengers) < self.capacity:
            self.passengers.append(name)
            return f"{name} added to the bus"
        else:
            return f"Sorry {name} Bus is full"  
        
    def remove_passenger(self, name):
        if name in self.passengers:
            self.passengers.remove(name)
            return f"{name} removed from bus"
        else:
            return f"{name} not in bus"    

    def show_passengers(self):
        return f"Passengers List: {self.passengers}"      
        

metro_bus = Bus(capacity=3)
print(metro_bus.add_passenger("John"))
print(metro_bus.add_passenger("Mary"))
print(metro_bus.add_passenger("Paul"))
# print(metro_bus.remove_passenger("Paul"))
print(metro_bus.add_passenger("Lisa"))  
print(metro_bus.show_passengers())        