
from exceptions import *

class Library:
    def __init__(self):
        self.books = {}
        self.members = {}

    def add_book(self, book):
        self.books[book.isbn] = book

    def list_books(self):
        for book in self.books.values():
            print(book)

    def find_book(self, isbn):
        if isbn not in self.books:
            raise BookNotFoundError("존재하지 않는 도서입니다.")
        return self.books[isbn]

    def add_member(self, member):
        self.members[member.name] = member

    def find_member(self, name):
        if name not in self.members:
            raise MemberNotFoundError("존재하지 않는 회원입니다.")
        return self.members[name]

    def borrow_book(self, member_name, isbn):
        member = self.find_member(member_name)
        book = self.find_book(isbn)

        if book.is_borrowed:
            raise BookAlreadyBorrowedError("이미 대출 중인 책입니다.")

        book.is_borrowed = True
        member.borrowed_books.append(book)

    def return_book(self, member_name, isbn):
        member = self.find_member(member_name)
        book = self.find_book(isbn)

        if not book.is_borrowed:
            raise Exception("이미 반납된 도서입니다.")

        book.is_borrowed = False
        member.borrowed_books.remove(book)

    def search_books(self, keyword):
        for book in self.books.values():
            if keyword.lower() in book.title.lower():
                print(book)
