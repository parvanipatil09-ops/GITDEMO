class FoodItem:
    def __init__(self,item_id,name,price,quantity):
        self.item_id=item_id
        self.name=name
        self.price=price
        self.quantity=quantity
        
    def display(self):
        print(f"Item Id: {self.item_id}")
        print(f"Name: {self.name}")
        print(f"Price: {self.price}")
        print(f"Quantity: {self.quantity}")
        print()

class Restaurant:
    def __init__(self):
        self.menu=[]
        
    def add_food(self,food_item):
        self.menu.append(food_item)
        print(f"{food_item.name} Added successfully")
        print()
        
    def display_menu(self):
        if not self.menu:
            print("Menu is empty")
            print()
            return

        for food in self.menu:
            food.display()
            
            
    def search_food(self,item_id):
        for food in self.menu:
            if food.item_id==item_id:
                food.display()
                break
        else:
            print('No such record')
            print()
            
    def update_price(self,item_id,new_price):
        for food in self.menu:
            if food.item_id==item_id:
                food.price=new_price
                print('Price Updated')
                print()
                break
        else:
            print('No such record')
            print()
    
    def update_quantity(self,item_id,new_quantity):
        for food in self.menu:
            if food.item_id==item_id:
                food.quantity=new_quantity
                print('Quantity Updated')
                print()
                break
            
        else:
            print('No such record')
            print()
    
    def delete_food(self,item_id):
        for food in self.menu:
            if food.item_id==item_id:
                self.menu.remove(food)
                print(f"{food.name} Deleted")
                print()
                break
        else:
            print('No such record')
            print()
    
    def count_items(self):
        print(f"Number of items: {len(self.menu)}")
        print()
        
f1=FoodItem(1,'Veg crispy',230,19)
f2=FoodItem(2,'Paneer chilly',370,11)
f3=FoodItem(3,'Honey chilly potato',249,4)
r=Restaurant()
r.add_food(f1)
r.add_food(f2)
r.add_food(f3)
r.display_menu()
r.search_food(2)
r.update_price(1,299)
r.update_quantity(3,2)
r.delete_food(2)
r.count_items()