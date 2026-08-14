class Product:
    def __init__(self,product_id,name,price):
        self.product_id=product_id
        self.name=name
        self.price=price
    def display_details(self):
        print(f"Product ID: {self.product_id}")
        print(f"Name: {self.name}")
        print(f"Price: {self.price}")
        
        
class ElectronicProduct(Product):
    def __init__(self,product_id,name,price,brand,warranty_years):
        super().__init__(product_id,name,price)
        self.brand=brand
        self.warranty_years=warranty_years
    def display_details(self):
        super().display_details()
        print(f"Brand: {self.brand}")
        print(f"Warranty(in years): {self.warranty_years}")
    def apply_discount(self,percent):
        final_price=((100-percent)/100)*self.price
        print(f"Discount applied. Final price: {final_price}")
        
        
class SmartPhone(ElectronicProduct):
    def __init__(self, product_id, name, price, brand, warranty_years, ram, storage, battery):
        super().__init__(product_id, name, price, brand, warranty_years)
        self.ram=ram
        self.storage=storage
        self.battery=battery
    def display_details(self):
        super().display_details()
        print(f"Ram: {self.ram} GB")
        print(f"Storage: {self.storage} GB")
        print(f"Battery: {self.battery} %")
    def make_call(self,number):
        print(f"Calling {number}")
        



p3=SmartPhone(1221,'Mobile',15000,'Samsung',5,128,256,100)
p3.display_details()
p3.make_call(1234567890)