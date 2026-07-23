class Student:
    def __init__(self,name,roll_no):
        self.name=name
        self.roll_no=roll_no
        print(f"Student name: {name}")
        print(f"Roll number: {roll_no}\n")
        

class Dog:
    def __init__(self,breed,colour):
        self.breed=breed
        self.colour=colour
        print(f"Dog breed: {breed}")
        print(f"Dog colour: {colour}\n")
        
class Car:
    def __init__(self,c_name,company):
        self.c_name=c_name
        self.company=company
        print(f"Car name: {c_name}")
        print(f"Company name: {company}\n")
        
a=Car('G-Wagon','Mercedez')
b=Dog('Golden retriever','Ochre')
c=Student('Parvani',9)