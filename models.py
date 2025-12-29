class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_borrowed = False

    def __str__(self):
        return self.title + ' ' + self.author + ' ' + self.isbn

class Member:
    def __init__(self, name, phone, borrowed_books):
        self.name = name
        self.phone = phone
        self.borrowed_books = borrowed_books

class Library:
    def __init__(self):
        self.books = []
        self.members = {} # {"책 이름": "빌린 사람"}
