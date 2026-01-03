class Book:
    def __init__ (self, title, author, isbn, is_borrowed):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_borrowed = False

    def __str__(self):
        if self.is_borrowed:
            status = "대출 중"
        else:
            status = "대충 가능"
        return f'[{self.isbn}] {self.title} / {self.author} ({status})'

class Member:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone
        self.borrowed_books = []

    def __str__(self):
        return f'{self.name}, {self.phone} '

class Library:
    pass