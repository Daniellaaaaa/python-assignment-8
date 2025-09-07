class Library:
    def __init__(self):
        self.library=[]
        self.borrowed_book={}

    def add_book(self, book_name):
        if book_name not in self.library:
            self.library.append(book_name)
            return f"{book_name} added to the library successfully!"
        else:
            return f"{book_name} already exists"
        
    def borrow_book(self, name, book):
        if book in self.library:
            self.library.remove(book)
            if name not in self.borrowed_book:
                self.borrowed_book[name]=[book]
                return f"{book} borrowed successfully!"
            else:
                self.borrowed_book[name].append(book)
                return f"{book} borrowed successfully!"
        else:
            return f"{book} isn't in the library"  

    def return_book(self, name):
        if name in self.borrowed_book:
            books_borrowed=self.borrowed_book[name]
            for book in books_borrowed:
                self.library.append(book)
            del self.borrowed_book[name]
            return f"Books returned successfully"
        else:
            return f"{name} didn't borrow any book"               

    def show_available_books(self):
        return f"Available books: {self.library}"
    
    def show_borrowed_books(self):
        return f"Borrowed Books: {self.borrowed_book}"

lib = Library()

print(lib.add_book("Python 101"))
print(lib.add_book("Python 101"))
print(lib.add_book("Maths"))
print(lib.add_book("Data Science Handbook"))
print(lib.borrow_book("Alice", "Python 101"))
print(lib.borrow_book("Alice", "Maths"))
print(lib.show_borrowed_books())
print(lib.show_available_books()) 

print(lib.return_book("Alice"))
# print(lib.show_borrowed_books())
print(lib.show_available_books()) 