
class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_borrowed = False

    def __str__(self):
        status = "대출 중" if self.is_borrowed else "대출 가능"
        return f"{self.title}  | {self.author} | ISBN:{self.isbn} | {status}"

class Member:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone
        self.borrowed_books = []

    def __str__(self):
        return f"{self.name} ({self.phone})"

