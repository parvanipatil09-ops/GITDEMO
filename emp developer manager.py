class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def display(self):
        print(f"Name: {self.name}")
        print(f"Salary: {self.salary}")
        

class Developer(Employee):
    def __init__(self,name,salary,programming_language):
        super().__init__(name,salary)
        self.programming_language=programming_language
    def display(self):
        super().display()
        print(f"Programming Language: {self.programming_language}")
class Manager(Employee):
    def __init__(self,name,salary,team_size):
        super().__init__(name,salary)
        self.team_size=team_size
    def display(self):
        super().display()
        print(f"Team Size: {self.team_size}")

d1=Developer('Cathy',100000,'JAVA')
m1=Manager('Jennifer',150000,8)
employees=[d1,m1]
for employee in employees:
    employee.display()
    print()
        