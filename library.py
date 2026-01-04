from exception import DuplicateISBNError, DuplicateMemberError


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
        기존에 등록된 member에 중복되는 이름인지 검사
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


    # # TODO: 여기부터, 기능 4 완성하면 3이랑 같이 커밋
    # def borrow_book(self, phone, isbn):
    #     for book in self.books:
    #         if book.isbn == isbn and not book.is_borrowed:
    #             for member in self.members:
    #                 if member.phone == phone:
    #                     member.



