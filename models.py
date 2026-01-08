from exception import MemberNotFoundError, BookNotBorrowedError, BookNotFoundError


class Book:
    def __init__(self, title, author, isbn, is_borrowed):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_borrowed = is_borrowed


    def __str__(self):
        return f"{self.title} {self.author} {self.isbn} {self.is_borrowed}"

class Member:
    def __init__(self, name, phone, borrowed_books):
        self.name = name
        self.phone = phone
        self.borrowed_books = borrowed_books

class Library:
    def __init__(self, books):
        self.books = books
        self.members = {}

    def add_book(self):
        title = input("책 제목을 입력하세요:")
        author = input("저자를 입력하세요:")
        isbn = input("책 고유 번호를 입력하세요:")

        self.books.append(Book(title, author, isbn, False))

    def add_member(self):
        name = input("이름을 입력하세요:")
        phone = input("-를 제외한 번호를 입력하세요:")
        borrowed_books = False
        print("회원등록이 완료되었습니다.")
        self.members[name] = Member(name, phone, borrowed_books)

    def show_books(self):
        for book in self.books:
            print(book)

    def borrow_book(self):
        name = input("회원 이름을 입력하세요:")
        isbn = input("책 고유 번호를 입력하세요:")
        if name not in self.members:
            raise MemberNotFoundError("회원을 찾을 수 없습니다.")
        ## 모든 오류 상황을 예외 처리 하는 것은 가능하지만
        ## if문 실습도 해보기위해서 밑부분은 조건문 처리로 구현했습니다.
        for book in self.books:
            if book.isbn == isbn:
                if book.is_borrowed:
                    print("이미 대출중인 책입니다.")
                    return
                else:
                    book.is_borrowed = True
                print("대출이 완료되었습니다.")
                return

        print("존재하지 않는 고유 번호 입니다.")


    def return_book(self):
        name = input("회원 이름을 입력하세요:")
        isbn = input("대출하신 책 고유 번호를 입력하세요:")

        if name not in self.members:
            raise MemberNotFoundError("회원을 찾을 수 없습니다.")

        for book in self.books:
            if book.isbn == isbn:
                if not book.is_borrowed:
                    raise BookNotBorrowedError("현재 대출 중인 책이 아닙니다.")

                book.is_borrowed = False
                print("반납이 완료되었습니다.")
                return

        raise BookNotFoundError("존재하지 않는 고유 번호입니다.")

    def search_book(self):
        keyword = input("검색할 책 제목을 입력하세요: ")

        found = False

        for book in self.books:
            if keyword.lower() in book.title.lower():
                print(book)
                found = True

        if not found:
            print("검색 결과가 없습니다.")

