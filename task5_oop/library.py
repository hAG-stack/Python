class Library:
    def __init__(self):
        self.books=[]

    def add_book(self, book):
        self.books.append(book)
        print(f" Book {book.title} added to the library.")

    def display_books(self):
        print("\n Library Books ")
        for book in self.books:
            book.displayInfo()
        
