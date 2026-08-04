class Book:
    def __init__(self,title,author,price):
        self.title=title
        self.author=author
        self.price=price
    def display(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Price: ₹{self.price}")
       
class EBook(Book):
    def __init__(self,title,author,price,file_size):
        super().__init__(title,author,price)
        self.file_size=file_size
    
    def display(self):
        super().display()
        print(f"File size: {self.file_size} MB ")
        

a=Book('400 DAYS','Chetan Bhagat',400)
a.display()
print()

b=EBook('secret 7','Enid Blyton',200,15)
b.display()
print()