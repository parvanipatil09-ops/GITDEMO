class Food:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def display(self):
        print(f"Name: {self.name}")
        print(f"Price: ₹{self.price}")

class Pizza(Food):
    def __init__(self, name, price, size):
        super().__init__(name, price)
        self.size = size

    def display(self):
        print("Pizza")
        super().display()
        print(f"Size: {self.size}")
        print()
    
class Burger(Food):
    def __init__(self,name,price,cheese):
        super().__init__(name,price)
        self.cheese=cheese
    
    def display(self):
        print('Burger')
        super().display()
        print(f"Cheese: {self.cheese}")
        print()
        
class Drink(Food):
    def __init__(self,name,price,volume):
        super().__init__(name,price)
        self.volume=volume
        
    def display(self):
        print('Drink')
        super().display()
        print(f"Volume: {self.volume} ml")
        print()
        
pizza=Pizza("Margherita", 299, "Medium")

burger=Burger("Veg Burger", 149, "Yes")

drink=Drink("Cold Coffee", 120, 350)

l=[pizza,burger,drink]
for food in l:
    food.display()