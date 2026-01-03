class Library:
    def __init__(self, books):
        self.books = books # {"isbn": Book}
        self.members = {} # {"이름": Member}

    # def add_book(self, new_book):
    #     self.books.append(new_book)
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
    # def check_same_isbn(self, isbn):
    #     for book in self.books:
    #         if book.isbn == isbn:
    #             return True
    #     return False
    #
    # # TODO: 여기부터, 기능 4 완성하면 3이랑 같이 커밋
    # def borrow_book(self, phone, isbn):
    #     for book in self.books:
    #         if book.isbn == isbn and not book.is_borrowed:
    #             for member in self.members:
    #                 if member.phone == phone:
    #                     member.



