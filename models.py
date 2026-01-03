import re
from datetime import datetime

class Book:
    def __init__(self, title, author, isbn, is_borrowed = False):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_borrowed = is_borrowed #기본값 False

    def __str__(self):
        if self.is_borrowed == True:
            status = "대출 중"
        else:
            status = "대출 가능"

        return f"[{status}] {self.title} - {self.author} (ISBN: {self.isbn})"

class Member:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone
        self.borrowed_books = []
        self.borrowed_dates = {} # ISBN을 key 값으로, 대출 시각을 value로 저장하는 딕셔너리

class Library:
    def __init__(self):
        self.books = []
        self.members = {}

    def add_book(self, title, author, isbn, is_borrowed = False):
        new_book = Book(title, author, isbn, is_borrowed)
        self.books.append(new_book)
        print(f"[System] - {new_book}")


    def add_member(self, name, phone):
        # ^[a-zA-Z0-9가-힣]+$ : 시작부터 끝까지 영문, 숫자, 한글만 있다는 뜻
        # re 는 글자 패턴 찾기 도구 , "숫자 3자리-숫자 4자리-숫자 4자리로 구성된 글자" 같은 특정한 형식을 찾아내거나 검사할 때 사용
        if not re.match(r'^[a-zA-Z0-9가-힣\s]+$', name):
            raise ValueError(f"회원 이름에 특수문자를 포함할 수 없습니다: {name}")

        phone_pattern = r'^(\d{2,3}-\d{3,4}-\d{4}|\d{9,11})$'
        if not re.match(phone_pattern, phone):
            raise ValueError("전화번호 형식이 올바르지 않습니다. (예: 010-1234-5678 또는 01012345678)")

        if name in self.members:
            #RuntimeError 논리적으로 실행 중 문제가 생겼을 때 범용적으로 사용
            raise RuntimeError(f"이미 등록된 이름입니다: {name}")

        self.members[name] = Member(name, phone)
        print(f"{name} 회원님 등록이 완료되었습니다.")

    def borrow_book(self, name, isbn):
        if name not in self.members:
            raise KeyError(f"{name} 님을 찾을 수 없습니다.")
        member = self.members.get[name]

        for book in self.books:
            if book.isbn == isbn:
                if book.is_borrowed:
                    raise RuntimeError(f"이미 대출 중인 도서입니다: {book.title}")

                book.is_borrowed = True
                member.borrowed_books.append(book)
                member.borroewd_dates[isbn] = datetime.now()
                print(f"{member.name} 님이 {book.title} (ISBN: {book.isbn})을 대출하셨습니다.")
                return
        #LookupError 무언가를 찾지 못했을 때 사용하는 상위 예외
        raise LookupError(f"ISBN {isbn}에 해당하는 도서가 없습니다.")

    def return_book(self, name, isbn):
        member = self.members.get(name)
        if not member:
            raise LookupError(f"죄송합니다. {name} 회원님을 찾을 수 없습니다.")

        for book in self.books:
            if book.isbn == isbn:
                if not book.is_borrowed:
                    raise LookupError(f"{book.title}은 대출된 도서가 아닙니다.")

                borrow_date = member.borrowed_dates.get(isbn)
                if borrow_date:
                    days_passed = (datetime.now() - borrow_date).days
                    if days_passed > 7:
                        print(f"연체되었습니다! (대출 후 {days_passed}일 경과)")

                book.is_borrowed = False
                if book in member.borrowed_books:
                    member.borrowed_books.remove(book)
                if isbn in member.borrowed_dates:
                    del member.borrowed_dates[isbn]
                print(f"{member.name} 님이 {book.title} 을 반납하셨습니다.")
                return

        raise LookupError(f"해당 ISBN의 도서를 찾을 수 없습니다.")

    def search_book(self, book_name):
        found = False
        keyword = book_name.strip().lower()
        for book in self.books:
            if keyword.lower() in book.title.lower():
                print(book)
                found = True

        if not found:    # if found == False: 랑 같은 코드임 / 파이썬 문법
            raise LookupError("해당 단어가 포함된 도서가 없습니다.")