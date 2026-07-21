'''OBJECTIVE: 
  Add students
 store marks in a dictionary
 display all
 Highest mark
 average;
search by name.'''


d={}
while True:
    name=input('enter name of student: ')
    marks=int(input('enter marks of student: '))
    d[name]=marks
    ch=input('do you want to continue(y/n): ')
    if ch in 'Nn':
        break

    
def show():
    print(d)

def highest_marks():
    print("Highest marks scored are:", max(d.values()))
    

def avg_marks():
    total_marks=sum(d.values())
    total_stu=len(d)
    avg_marks=total_marks/total_stu
    print('The average marks are: ',avg_marks)
    
def search_byname(name):
    if name in d:
        print(f"The marks scored by {name} are : " , d[name])
    else:
        print('no such record found')
    
while True:
    print("\n1. Show")
    print("2. Highest Marks")
    print("3. Average Marks")
    print("4. Search by Name")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        show()
    elif choice == 2:
        highest_marks()
    elif choice == 3:
        avg_marks()
    elif choice == 4:
        name = input("Enter name: ")
        search_byname(name)
    elif choice == 5:
        break
    else:
        print("Invalid choice!")