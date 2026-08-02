class Shape:
    def area(self):
        print("Area depends on the shape.")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        print(f"Area of Circle: {3.14 * self.radius ** 2}")
        
class Square(Shape):
    def __init__(self,side):
        self.side=side
    
    def area(self):
        print(f"Area of Square: {self.side ** 2}")
        
        
shapes=[Circle(7),Square(9)]
for shape in shapes:
    shape.area()