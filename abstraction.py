from abc import ABC, abstractmethod

class Employee(ABC):
    @abstractmethod
    def calculate_salary(self):
        pass
    
class FullTimeEmployee(Employee):

    def __init__(self, name, monthly_salary):
        self.name = name
        self.monthly_salary = monthly_salary

    def calculate_salary(self):
        print()
        print(f"{self.name}'s Salary: ₹{self.monthly_salary}")
        print()

class PartTimeEmployee(Employee):

    def __init__(self, name, hours_worked, hourly_rate):
        self.name = name
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate

    def calculate_salary(self):
        salary = self.hours_worked * self.hourly_rate
        print()
        print(f"{self.name}'s Salary: ₹{salary}")
        print()
        
class Intern(Employee):

    def __init__(self, name, stipend):
        self.name = name
        self.stipend = stipend

    def calculate_salary(self):
        print()
        print(f"{self.name}'s Salary: ₹{self.stipend}")
        print()

a=FullTimeEmployee('Sapna',100000)
a.calculate_salary()

b=PartTimeEmployee('Rakesh',8,100)
b.calculate_salary()

c=Intern('Parvani',200000)
c.calculate_salary()