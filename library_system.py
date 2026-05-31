# Library System using Inheritance

class LibraryItem:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def describe(self):
        return f"{self.title} by {self.author} ({self.year})"


class Book(LibraryItem):
    def __init__(self, title, author, year, pages):
        super().__init__(title, author, year)
        self.pages = pages

    def describe(self):
        return f"Book: {self.title} by {self.author} ({self.year}) - {self.pages} pages"


class EBook(LibraryItem):
    def __init__(self, title, author, year, file_size_mb):
        super().__init__(title, author, year)
        self.file_size_mb = file_size_mb

    def describe(self):
        return f"EBook: {self.title} by {self.author} ({self.year}) - {self.file_size_mb} MB"


book1 = Book("Python Basics", "John Smith", 2020, 250)
book2 = Book("Data Science", "Alice Brown", 2022, 400)

ebook1 = EBook("AI Guide", "David Lee", 2023, 15)
ebook2 = EBook("ML Handbook", "Emma White", 2024, 20)

items = [book1, book2, ebook1, ebook2]

for item in items:
    print(item.describe())

# Explore
print(isinstance(book1, LibraryItem))
# True because Book inherits from LibraryItem