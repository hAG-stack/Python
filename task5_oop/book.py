class Book:
    def __init__(self, title, author, isbn, available=True):
        self.title = title
        self.author = author
        self.__isbn = isbn
        self.available = available

    def set_isbn(self, isbn):
        self.__isbn = isbn

    def get_isbn(self):
        return self.__isbn
    
    def displayInfo(self):
        status = "Available" if self.available else "Not Available"
        print(f"The Title of the book is {self.title}")
        print(f"The author of the book is {self.author}")
        print(f"The ISBN of the book is {self.__isbn}")
        print(f"Availability of the book {status}")
    
