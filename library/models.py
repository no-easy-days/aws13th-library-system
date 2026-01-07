class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_borrowed = False

    def __str__(self):
        self.status = "대출중" if self.is_borrowed else "대출 가능"
        return (f"책 이름: {self.title}, 저자: {self.author}, "
                f"ISBN: {self.isbn}, 상태: {self.status}")

class Member:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone
        self.borrowed_books = []

class Library:
    def __init__(self):
        self.books = []
        self.members = {}

    # 공통 유틸
    def has_member(self, name):
        return name in self.members
    # 1. 도서 등록
    def add_book(self, book):
        for b in self.books:
            if b.isbn == book.isbn:
                raise ValueError("이미 등록된 ISBN입니다.")
        self.books.append(book)

    # 2. 도서 목록
    def list_book(self):
        return list(self.books)


    # 3. 회원 등록
    def add_member(self, member):
        self.members[member.name] = member

    # 4. 대출
    def borrow_book(self, name, isbn):
        if not self.has_member(name):
            raise ValueError("등록된 회원이 아닙니다.")

        book = None
        for b in self.books:
            if b.isbn == isbn:
                book = b
                break
        if book is None:
            raise ValueError("존재하지 않는 책입니다.")

        if book.is_borrowed:
            raise ValueError("이미 대출 중인 책입니다.")

        book.is_borrowed = True
        self.members[name].borrowed_books.append(book)
        return book

    # 5. 반납
    def return_book(self, name, isbn):
        if name not in self.members:
            raise ValueError("등록된 회원이 아닙니다.")
        member = self.members[name]

        book = None
        for b in self.books:
            if b.isbn == isbn:
                book = b
                break
        if book is None or not book.is_borrowed:
            raise ValueError("반납할 수 없는 책입니다.")

        if book not in member.borrowed_books:
            raise ValueError("이 회원이 대출한 책이 아닙니다.")

        book.is_borrowed = False
        member.borrowed_books.remove(book)
        return book

    # 6. 검색
    def search_book(self, keyword):
        return [book for book in self.books
                if keyword in book.title
                or keyword in book.author]




