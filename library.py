from exception import (
    DuplicateISBNError,
    DuplicateMemberError,
    MemberNotFoundError,
    BookNotFoundError,
    BookAlreadyBorrowedError,
    BookNotBorrowedError,
    BookBorrowedByOtherMemberError,
)


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

    def book_list(self) -> None:
        if not self.books:
            print("[ERROR] 등록된 도서가 없습니다.")
            return
        for book in self.books.values():
            print(book)

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

    def return_book(self, name: str, isbn: str) -> None:
        if name not in self.members:
            raise MemberNotFoundError(name)
        if isbn not in self.books:
            raise BookNotFoundError(isbn)

        book = self.books[isbn]
        if not book.is_borrowed:
            raise BookNotBorrowedError(isbn)
        if book.borrowed_by != name:
            raise BookBorrowedByOtherMemberError(isbn)
        book.is_borrowed = False
        book.borrowed_by = None

    def search_book(self, keyword: str) -> list:
        def normalize(s: str) -> str:
            return "".join(s.split()).casefold()
        key = normalize(keyword)
        return [
            book for book in self.books.values()
            if key in normalize(book.title)
        ]
