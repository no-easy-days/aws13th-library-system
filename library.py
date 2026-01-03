from exception import DuplicateISBNError


class Library:
    def __init__(self) -> None:
        self.books = {} # {"isbn": Book}
        self.members = {} # {"name": Member}

    def add_book(self, new_book) -> None:
        if new_book.isbn in self.books:
            raise DuplicateISBNError(new_book.isbn)
        self.books[new_book.isbn] = new_book
    #
    # def add_member(self, new_member):
    #     if new_member.phone not in self.members:
    #         self.members[new_member.phone] = new_member
    #     else:
    #         print("[ERROR] 이미 등록된 회원입니다.")
    #         return
    #
    # def book_list(self):
    #     if not self.books:
    #         print("[ERROR] 등록된 도서가 없습니다.")
    #         return
    #     for book in self.books:
    #         print(str(book))
    #
    #
    # # TODO: 여기부터, 기능 4 완성하면 3이랑 같이 커밋
    # def borrow_book(self, phone, isbn):
    #     for book in self.books:
    #         if book.isbn == isbn and not book.is_borrowed:
    #             for member in self.members:
    #                 if member.phone == phone:
    #                     member.



