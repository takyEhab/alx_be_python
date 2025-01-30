class Book:
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author
    def __str__(self):
        return f"Book: {self.title} by {self.author}"

class EBook(Book):
    def __init__(self, title: str, author: str, file_size: int):
        super().__init__(title, author)
        self.file_size = file_size
class PrintBook(Book):
    def __init__(self, title: str, author: str, page_count: int):
        super().__init__(title, author)
        self.page_count = page_count

class Library:
    def __init__(self):
        self.books = []
    def add_book(self, book):
        self.books.append(book)
    def list_books(self):
        for book in self.books:
            if book.__class__.__name__ == 'Book':
                print(f"Book: {book.title} by {book.author}")
            elif book.__class__.__name__ == 'EBook':
                print(f"E-Book: {book.title} by {book.author}, File Size: {book.file_size}")
            elif book.__class__.__name__ == 'PrintBook':
                print(f"Print Book: {book.title} by {book.author}, Page Count: {book.page_count}")
            