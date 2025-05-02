class Book:
    def __init__(self, isbn, title, writer):
        self.isbn = isbn
        self.title = title
        self.writer = writer
        self.occupied_by = None
    
class User:
    def __init__(self, name):
        self.name = name
        

class Library:
    def __init__(self):
        self.books = []
        self.users = []
        
    def add_book(self, book):
        print("adding book", book.title, "written by ", book.writer)
        self.books.append(book)
    
    def add_user(self, user):
        print("member created", user.name)
        self.users.append(user)

    def borrow_book(self, user, title):
        if user not in self.users:
            print(f"{user.name} is not a registered user. Cannot borrow books.")
            return None
    
        for book in self.books:
            if book.title == title and book.occupied_by is None:
                print(book.title, "book is getting borrowed by", user.name)
                book.occupied_by = user
                return book
            else:
                print("not borrowed")
        return None


    def return_book(self, book):
        print("returned book", book.title)
        book.occupied_by = None

lib = Library()
book1 = Book("a123", "Harry potter 1", "J K Rowling")
user1 = User("Shivam")
lib.add_book(book1)

lib.borrow_book(user1, book1.title)
lib.return_book(book1)
lib.add_user(user1)
lib.borrow_book(user1, book1.title)

lib.return_book(book1)
print(lib.books[0].title)
