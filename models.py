class Book:
    def __init__ (self, title, author, isbn):
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
    def __init__(self):
        self.books = []   # list 사용
        self.members = {} # dict 사용

    # 도서
    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        return self.books

    # 화원
    def add_member(self, member):
        self.members[member.name] = member

    def get_member(self, name):
        return self.members.get(name)

    # 대출
    def borrow_book(self, member_name, isbn):
        member = self.get_member(member_name)
        if not member:
            return False

        for book in self.books:
            if book.isbn == isbn and not book.is_borrowed:
                book.is_borrowed = True
                member.borrowed_books.append(book)
                return True
        return False

    # 반납
    def return_book(self, member_name, isbn):
        member = self.get_member(member_name)
        if not member:
            return False

        for book in member.borrowed_books:
            if book.isbn == isbn:
                book.is_borrowed = False
                member.borrowed_books.remove(book)
                return True
        return False

    # 검색
    def search_books(self, keyword):
        result = []
        for book in self.books:
            if keyword in book.title:
                result.append(book)
        return result