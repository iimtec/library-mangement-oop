from library_oop import Library
library = Library()

print("=== Testing Library Class ===")
library.add_book(1, "Clean Code", "Robert Martin", 2)
library.add_book(2, "Design Patterns", "Gang of Four", 1)
library.add_member(101, "Bob Jones", "bob@email.com")

library.display_available_books()

library.borrow_book(101, 1)
library.borrow_book(101, 2)
library.display_member_books(101)

library.return_book(101, 1)
library.display_available_books()