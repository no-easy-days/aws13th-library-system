# 임시 클래스 정의 추후 수정 필요
class Book:
    def __init__(self, title, author, isbn,is_borrowed=False):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_borrowed = is_borrowed
        
    def __str__(self):
        if self.is_borrowed:
            return f"{self.title} by {self.author} (ISBN: {self.isbn}) - 대출중"
        else:
            return f"{self.title} by {self.author} (ISBN: {self.isbn}) - 대출 가능"
     
class Member:
    def __init__(self, name,phone,borrowed_books):
        self.name = name
        self.phone = phone
        self.borrowed_books = []
        
class Library:
    def __init__(self):
        self.books = []
        self.members = {}
        
    def add_book(self, book):
        self.books.append(book)
        
    def add_member(self, member):
        self.members[member.name] = member
        
    def borrow_book(self, member, book):
        if book in self.books and not book.is_borrowed:
            book.is_borrowed = True
            member.borrowed_books.append(book)
            return True
        return False
    
    def return_book(self, member, book):
        if book in member.borrowed_books:
            book.is_borrowed = False
            member.borrowed_books.remove(book)
            return True
        return False
    
    def has_isvn(self, isbn):
        return any(book.isbn == isbn for book in self.books)