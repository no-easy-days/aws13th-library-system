from src.exception import (
    DuplicateISBNError,
    DuplicateMemberError,
    MemberNotFoundError,
    BookNotFoundError,
    BookAlreadyBorrowedError,
    BookNotBorrowedError,
    BookBorrowedByOtherMemberError,
)

from datetime import datetime, timedelta


class Library:
    def __init__(self) -> None:
        self.books = {} # {"isbn": Book}
        self.members = {} # {"name": Member}

    def add_book(self, new_book) -> None:
        if new_book.isbn in self.books:
            raise DuplicateISBNError(new_book.isbn)
        self.books[new_book.isbn] = new_book

    def add_member(self, new_member) -> None:
        if new_member.name in self.members:
            raise DuplicateMemberError(new_member.name)
        self.members[new_member.name] = new_member

    def has_member(self, name: str) -> bool:
        """
        member에 이미 등록된 멤버인지 검사
        :param name:
        :return: 이미 있는 이름 -> True
                처음 등록되는 이름 -> False
        """
        return name in self.members

    def book_list(self) -> list:
        return list(self.books.values())

    def borrow_book(self, name: str, isbn: str) -> None:
        if name not in self.members:
            raise MemberNotFoundError(name)
        if isbn not in self.books:
            raise BookNotFoundError(isbn)
        book = self.books[isbn]
        if book.is_borrowed:
            raise BookAlreadyBorrowedError(isbn)
        book.is_borrowed = True
        book.borrowed_by = name
        book.borrowed_at = datetime.now()

    def return_book(self, name: str, isbn: str) -> int:
        """
        책 반납 로직

        :param name:
        :param isbn:
        :return: 연체 일수 (7일 이상 대출 시 연체)
        """
        if name not in self.members:
            raise MemberNotFoundError(name)
        if isbn not in self.books:
            raise BookNotFoundError(isbn)
        book = self.books[isbn]
        if not book.is_borrowed:
            raise BookNotBorrowedError(isbn)
        if book.borrowed_by != name:
            raise BookBorrowedByOtherMemberError(isbn)

        overdue_days = 0
        if book.borrowed_at:
            delta = datetime.now() - book.borrowed_at
            if delta > timedelta(days=7):
                overdue_days = delta.days - 7

        book.is_borrowed = False
        book.borrowed_by = None
        book.borrowed_at = None

        return overdue_days

    def search_book(self, keyword: str) -> list:
        def normalize(s: str) -> str:
            return "".join(s.split()).casefold()
        key = normalize(keyword)
        return [
            book for book in self.books.values()
            if key in normalize(book.title)
        ]
