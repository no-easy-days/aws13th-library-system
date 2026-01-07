class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_borrowed = False

    def __str__(self):
        return f"{self.title} {self.author} {self.isbn} {self.is_borrowed}"


class Member:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone
        self.borrowed_books = []


class Library:
    def __init__(self, books, members):
        self.books = books
        self.members = members

    def add_book(self, book):
        self.books.append(book)

    def add_member(self, member):
        self.members.append(member)

    def borrow_book(self, isbn, user_name):
        member = None
        for m in self.members:
            if m.name == user_name:
                member = m
                break

        if member is None:
            print(f"'{user_name}' 회원을 찾을 수 없습니다.")
            return

        for book in self.books:
            if book.isbn == isbn:
                if book.is_borrowed:
                    print("대출이 불가능합니다.")
                else:
                    book.is_borrowed = True
                    print(f">> '{user_name}'님이 '{book.title}' ({book.isbn})을 대출했습니다.")
                    for member in self.members:
                        if member.name == user_name:
                            member.borrowed_books.append(book)
                return

        print(f"ISBN '{isbn}'에 해당하는 책을 찾을 수 없습니다.")
        return

    def return_book(self, isbn, user_name):
        for book in self.books:
            if book.isbn == isbn:
                if book.is_borrowed:
                    print(f" {user_name}님의 {book.title}이 반납 되었습니다")
                    book.is_borrowed = False
                      # 회원의 대출 목록에서 제거

                    for member in self.members:

                        if member.name == user_name:

                            if book in member.borrowed_books:
                                member.borrowed_books.remove(book)

                    return
                else:
                    print("반납할 책이 없습니다.")
                    return

        print(f"ISBN '{isbn}'에 해당하는 책을 찾을 수 없습니다.")