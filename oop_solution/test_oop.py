from library_oop import Book
book = Book(1, "Python Crash Course", "Eric Matthes", 3)

print(book) #Show __str__ method
print("Borrowing 2 books...")
book.borrow()
book.borrow()
print(f"Available books: {book.available_copies}")

print("Returning 1 books...")
book.return_book()
print(f"Available books: {book.available_copies}")
print(book)