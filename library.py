class Book:
    def __init__(self, title):
        self.title = title
        self.available = True


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title):
        self.books.append(Book(title))
        print(title, "added successfully")

    def show_books(self):
        print("\nLibrary Books:")
        for book in self.books:
            status = "Available" if book.available else "Issued"
            print(book.title, "-", status)

    def issue_book(self, title):
        for book in self.books:
            if book.title == title and book.available:
                book.available = False
                print(title, "issued successfully")
                return
        print("Book not available")

    def return_book(self, title):
        for book in self.books:
            if book.title == title:
                book.available = True
                print(title, "returned successfully")
                return


library = Library()

library.add_book("Mathematics")
library.add_book("Statistics")
library.add_book("Computer Science")

library.show_books()

library.issue_book("Mathematics")

library.show_books()

library.return_book("Mathematics")

library.show_books()
