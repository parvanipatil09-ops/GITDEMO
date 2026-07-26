'''Project: Contact Book
Requirements: Add contact; search by name; display all; update; delete '''

d={}
def add():
    while True:
        c_nam=input('Enter name : ')
        c_num=int(input('enter contact number: '))
        d[c_nam]=c_num
        print('Contact Successfully added')
        print()
        ch=input('do you want to continue(y/n): ')
        if ch in 'nN':
            break
        print()
        
def search_by_name(name):
    if name in d:
        print(f"Name:{name}\n Phone number: {d[name]}")
        print()
    else:
        print('no such contact')
        print()
        
def display_all():
    if len(d)==0:
        print('no contacts')
    else:
        for i in d:
            print(i,d[i])
            print()

def update(nam):
    if nam in d:
        d[nam]=int(input('Enter new contact number: '))
        print('Updated successfully')
        print()
    else:
        print('no such contact found')
        print()
    
def delete(nam):
    if nam in d:
        del d[nam]
        print('deleted successfully')
        print()
    else:
        print('no such contact found')
        print()
        
while True:
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Display All")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    ch = int(input("Enter your choice: "))

    if ch == 1:
        add()

    elif ch == 2:
        name = input("Enter name: ")
        search_by_name(name)

    elif ch == 3:
        display_all()

    elif ch == 4:
        name = input("Enter name to update: ")
        update(name)

    elif ch == 5:
        name = input("Enter name to delete: ")
        delete(name)

    elif ch == 6:
        print("Thank you!")
        break

    else:
        print("Invalid choice")