from library_oop import Member
member = Member(101, "Alice Smith", "alice@email.com")

print(member) #Show __str__ method
print("Borrowing 2 books...")
member.borrow_book(1)
member.borrow_book(2)
member.borrow_book(3)
print(f"Borrowed books lists: {member.borrowed_books}")

# Overlimit borrowing
member.borrow_book(4)

print("Returning book...")
member.return_book(2)
print(f"Borrowed books lists: {member.borrowed_books}")