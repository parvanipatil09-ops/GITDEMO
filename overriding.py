class Vehicle:
    def __init__(self,brand,color):
        self.brand=brand
        self.color=color
    def display(self):
        print(f"Brand: {self.brand}")
        print(f"Color: {self.color}")

class Bike(Vehicle):
    def __init__(self,brand,color,engine_cc):
        super().__init__(brand,color)
        self.engine_cc=engine_cc
    def display(self):
        super().display()
        print(f"Engine CC : {self.engine_cc}")
        
b = Bike("Honda", "Black", 350)
b.display()