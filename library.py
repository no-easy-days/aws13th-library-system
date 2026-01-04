from models import Book, Member
from exceptions import (
    BookNotFoundError,
    MemberNotFoundError,
    BookAlreadyBorrowedError
)

class Library:
    def __init__(self):
        self.books = {}    # isbn -> Book
        self.members = {}  # name -> Member

    def add_book(self, book):
        self.books[book.isbn] = book

    def add_member(self, member):
        self.members[member.name] = member

    def list_books(self):
        for book in self.books.values():
            print(book)

    def borrow_book(self, member_name, isbn):
        if member_name not in self.members:
            raise MemberNotFoundError("회원이 존재하지 않습니다.")

        if isbn not in self.books:
            raise BookNotFoundError("책이 존재하지 않습니다.")

        book = self.books[isbn]
        member = self.members[member_name]

        if book.is_borrowed:
            raise BookAlreadyBorrowedError("이미 대출 중인 책입니다.")

        book.is_borrowed = True
        member.borrowed_books.append(isbn)

        print(f">> '{member_name}'님이 '{book.title}'을 대출했습니다.")

    def return_book(self, member_name, isbn):
        book = self.books[isbn]
        member = self.members[member_name]

        book.is_borrowed = False
        member.borrowed_books.remove(isbn)

        print(f">> '{member_name}'님이 '{book.title}'을 반납했습니다.")

    def search_books(self, keyword):
        for book in self.books.values():
            if keyword in book.title:
                print(book)
