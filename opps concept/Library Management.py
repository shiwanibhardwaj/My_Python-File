# Library_Management......

class Book():
    def __init__(self, title, author, ISBN):
        self.title = title
        self.author = author
        self.ISBN = ISBN

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, ISBN: {self.ISBN}"    #this function will print info when library.list_books() will be called.
    
class Library():
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book.title}' added to the library.")

    def remove_book(self, ISBN):
        for book in self.books:
            if book.ISBN == ISBN:
                self.books.remove(book)
                print(f"Book '{book.title}' removed from the library.")
                return
        print("Book is not found.")

    def list_books(self):
        if not self.books:
            print("No books in the library.")
        else:
            for book in self.books:
                print(book)


if __name__ == "__main__":
    book1 = Book("you can win", 'shiv khera', '9780743')
    book2 = Book("To Kill a Mockingbird", "Harper Lee", "9780061")
    book3 = Book("1984", "George Orwell", "97804515")

print(book1.__dict__)
library = Library()

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)
library.list_books()
library.remove_book("9780061")
