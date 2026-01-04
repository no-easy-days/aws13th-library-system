import csv

# 📘 책 정보 클래스
class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_borrowed = False


# 👤 회원 정보 클래스
class Member:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []


# 🏛 도서관 시스템 클래스
class Library:
    def __init__(self):
        self.book_list = []
        self.member_list = []

    # CSV → 도서 초기 로드
    def initial_book(self):
        with open("books.csv", "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                book = Book(row["title"], row["author"], row["isbn"])
                self.book_list.append(book)

    # 도서 등록
    def add_book(self):
        title = input("제목: ")
        author = input("저자: ")
        isbn = input("ISBN: ")
        self.book_list.append(Book(title, author, isbn))
        print("도서 등록 완료")

    # 도서 목록 출력
    def show_books(self):
        print("\n=== 도서 목록 ===")
        for i, book in enumerate(self.book_list, 1):
            status = "대출중" if book.is_borrowed else "대출가능"
            print(f"{i}. {book.title} / {book.author} / {status}")

    # 회원 등록
    def add_member(self):
        name = input("회원 이름: ")
        self.member_list.append(Member(name))
        print("회원 등록 완료")

    # 도서 대출
    def borrow_book(self):
        isbn = input("대출할 도서 ISBN: ")
        member_name = input("회원 이름: ")

        member = next((m for m in self.member_list if m.name == member_name), None)
        if not member:
            print("회원이 존재하지 않습니다.")
            return

        for book in self.book_list:
            if book.isbn == isbn:
                if book.is_borrowed:
                    print("이미 대출 중인 도서입니다.")
                else:
                    book.is_borrowed = True
                    member.borrowed_books.append(book)
                    print("대출 완료")
                return
        print("도서를 찾을 수 없습니다.")

    # 도서 반납
    def return_book(self):
        isbn = input("반납할 도서 ISBN: ")

        for member in self.member_list:
            for book in member.borrowed_books:
                if book.isbn == isbn:
                    book.is_borrowed = False
                    member.borrowed_books.remove(book)
                    print("반납 완료")
                    return
        print("대출 기록이 없습니다.")

    # 도서 검색
    def search_book(self):
        keyword = input("검색어: ")
        for book in self.book_list:
            if keyword in book.title:
                print(f"{book.title} / {book.author}")