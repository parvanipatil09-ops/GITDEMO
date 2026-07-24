class Student:
    def __init__(self,name,roll_no,marks):
        self.name=name
        self.roll_no=roll_no
        self.marks=marks
        
        
    def display(self):
        print(f"Name: {self.name}")
        print(f"Roll number: {self.roll_no}")
        print(f"Marks: {self.marks}")
        print()
        
        
    def grade(self):
        if 90<=self.marks<=100:
            print('Grade: A')
        elif 75<=self.marks<=89:
            print('Grade: B')
        elif 60<=self.marks<=74:
            print('Grade: C')
        elif 40<=self.marks<=59:
            print('Grade: D')
        else:
            print("Grade: Fail")
        print()
        
        
    def is_pass(self):
        if self.marks>=40:
            print('Result: Pass')
        else:
            print('Result: Fail')
        print()
    def update_marks(self,new_marks):
        self.marks=new_marks
        print(f"Updated marks for {self.name}: {self.marks}")
        print()
    


student1=Student('Parvani',11,100)
student2=Student('Susan',12,99)
student3=Student('Catherine',13,98)
student4=Student('XYZ',19,38)
l=[student1,student2,student3,student4]
for i in l:
    i.display()
    i.grade()
    i.is_pass()