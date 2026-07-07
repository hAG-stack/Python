from member import Member
from staffmember import StaffMember
from book import Book
from library import Library


# Create Library

library = Library()

# Create Staff Member

staff = StaffMember("Ahmed", "M001", "S101")

# Create Books

book1 = Book("Python Basics", "John Smith", "11111")

book2 = Book("Data Structures", "Alice Brown", "22222")

# Staff adds books

staff.add_book(library, book1)

staff.add_book(library, book2)

# Display books

library.display_books()

# Create Member

member = Member("Sara", "M002")

# Borrow a book

member.borrow_book(book1)

# Display books after borrowing

library.display_books()

# Return the book

member.return_book(book1)

# Display books after returning

library.display_books()

# Encapsulation Example

print("Book ISBN:", book1.get_isbn())

book1.set_isbn("99999")

print("Updated ISBN:", book1.get_isbn())

print("Member ID:", member.get_membership_id())

member.set_membership_id("M100")

print("Updated Member ID:", member.get_membership_id())