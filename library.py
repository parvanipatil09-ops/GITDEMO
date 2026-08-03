from abc import ABC , abstractmethod

#Objective: Build a Library Management System using OOP.
class LibraryItem:
    def __init__(self,title,author):
        self.title=title
        self.author=author
        self.__available=True
    
    def display_info(self):
        print(f"Title: {self.title}")
        print()
        print(f"Author name:{self.author}")
        print()
        
    def borrow(self):
        if self.__available:
            self.__available=False
            print('Book borrowed successfully')
            print()
        else:
            print('Book already borrowed')
            print()
    
    def return_item(self):
        if self.__available:
            print("Item is already available.")
            print()
        else:
            self.__available = True
            print("Item returned successfully.")
            print()
        
        
class Book(LibraryItem):
    def __init__(self, title, author, pages):
        super().__init__(title, author)
        self.pages = pages
    def display_info(self):
        super().display_info()
        print(f"Pages: {self.pages}")
        print()

class Magazine(LibraryItem):
    def __init__(self, title, author, issue_number):
        super().__init__(title, author)
        self.issue_number = issue_number
    
    def display_info(self):
        super().display_info()
        print(f"Issue number: {self.issue_number}")
        print()

class Newspaper(LibraryItem):
    def __init__(self, title, author, date):
        super().__init__(title, author)
        self.date = date
    
    def display_info(self):
        super().display_info()
        print(f"Date: {self.date}")
        print()

class LibraryMember(ABC):
    @abstractmethod
    def member_type(self):
        pass
    
class StudentMember(LibraryMember):
    def member_type(self):
        print("Student Member")
        print()

class FacultyMember(LibraryMember):
    def member_type(self):
        print("Faculty Member")
        print()
        
b1=Book('Secret Seven','Enid blyton',220)
b1.display_info()

b2=Book('400 DAYS','chetan bhagat',290)
b2.display_info()

m1=Magazine('Dubai Bling','Farhana',134)
m1.display_info()

n1=Newspaper('toi','angad bedi','17-09-26')
n1.display_info()

b1.borrow()
b1.borrow()

b1.return_item()
b1.return_item()


class Fine:
    def __init__(self,days):
        self.fine=days*5
    
    def display_fine(self):
        print(f"Fine: ₹{self.fine}")
        print()

f=Fine(6)
f.display_fine()
        
    
        

student = StudentMember()
faculty = FacultyMember()

student.member_type()
faculty.member_type()