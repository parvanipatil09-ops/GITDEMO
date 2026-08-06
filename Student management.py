class Student:
    def __init__(self,name,roll_no):
        self.name=name
        self.roll_no=roll_no
        
    def __str__(self):
        return f"Name: {self.name}| Roll No: {self.roll_no}"
 
class University:
    def __init__(self,university_name):
        self.university_name=university_name
        self.students=[]
        
    def add_student(self,student): #add students
        self.students.append(student)
    
    def display_students(self):  #display records of students
        print(self.university_name)
        for s in self.students:
            print(s)
            
    def search_student(self,roll_no): #search student by roll number
        for student in self.students:
            if student.roll_no==roll_no:
                print(student)
                break
        else:
            print('No such record')
            
    def remove_student(self,roll_no): #remove student record 
        for student in self.students:
            if student.roll_no==roll_no:
                self.students.remove(student)
                print('Record deleted')
                break
        else:
            print('no such record')
        
    def count_students(self): #number of student records
        print(f"Number of students: {len(self.students)}")
    
    def update_student_name(self,roll_no,new_name): #keeping roll num intact updating student name
        for student in self.students:
            if student.roll_no==roll_no:
                student.name=new_name
                print(f"Updated to {new_name}")
                break
        else:
            print('No such record')

s1=Student('Parvani',11)
s2=Student('Karry',12)
s3=Student('Kanins',13)
s4=Student('Prerna',14)
u=University('TSS')
u.add_student(s1)
u.add_student(s2)
u.add_student(s3)
u.add_student(s4)

u.display_students()

u.search_student(12)

u.remove_student(14)

u.count_students()

u.update_student_name(11,'Pari')

