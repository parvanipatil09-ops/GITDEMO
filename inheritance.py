class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
class Employee(Person):

    def __init__(self,name,age,employee_id,salary):
        super().__init__(name,age)
        self.employee_id=employee_id
        self.salary=salary
    def annual_salary(self):
        return self.salary*12
    def increment_salary(self,percentage):
        self.salary=self.salary+(self.salary*percentage/100)
    def display(self):

        print(f"Name : {self.name}")

        print(f"Age : {self.age}")

        print(f"Employee ID : {self.employee_id}")

        print(f"Salary : {self.salary}")

        print()


e3=Employee('John',30,101,5000)
print("Annual Salary:", e3.annual_salary())

e3.increment_salary(10)
e3.display()

