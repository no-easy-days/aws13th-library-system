import csv
from utils import LibraryError


class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_borrowed = False

    def __str__(self):
        # 대출 여부에 따라 출력 문자열 변경
        if self.is_borrowed:
            status = "[대출중]"
        else:
            status = "[대출가능]"
        return f"{status} {self.title} / {self.author} / {self.isbn}"


class Member:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone
        self.borrowed_books = []  # 회원이 빌린 Book 객체들을 저장하는 리스트

    def __str__(self):
        return f"{self.name} ({self.phone}) - 대출 권수: {len(self.borrowed_books)}권"


class Library:
    def __init__(self):
        self.books = []  # Book 객체 리스트
        self.members = {}  # 이름으로 회원을 찾기 위한 딕셔너리 {이름: Member객체}

    # --- 1. 초기화: CSV 파일 읽기 ---
    def load_books_from_csv(self, filename):
        with open(filename, 'r', encoding='utf-8') as f:
                # [변경] reader 대신 DictReader 사용
            reader = csv.DictReader(f)

                # next(reader) 필요 없음! (알아서 첫 줄을 키로 씀)

            for row in reader:
                    # [변경] 숫자가 아니라 '이름'으로 명확하게 가져옴
                    # 데이터 공백 제거(.strip())는 여전히 필수!
                title = row['title'].strip()
                author = row['author'].strip()
                isbn = row['isbn'].strip()

                new_book = Book(title, author, isbn)
                self.books.append(new_book)


    # --- 2. 도서 등록 ---
    def add_book(self, title, author, isbn):
        new_book = Book(title, author, isbn)
        self.books.append(new_book)
        print(f"도서 등록 완료 - {title}")

    # --- 3. 회원 등록 ---
    def add_member(self, name, phone):
        new_member = Member(name, phone)
        self.members[name] = new_member
        print(f"{name} 회원 등록이 완료되었습니다.")

    # --- 4. 대출 (핵심 로직) ---
    def borrow_book(self, member_name, isbn):
        # 1) 회원 존재 여부 확인
        if member_name not in self.members:
            raise LibraryError("등록되지 않은 회원입니다.")
        member = self.members[member_name]

        # 2) 책 존재 여부 확인
        target_book = None
        for book in self.books:
            if book.isbn == isbn:
                target_book = book
                break

        if target_book is None:
            raise LibraryError("존재하지 않는 ISBN입니다.")

        # 3) 대출 가능 여부 확인 (is_borrowed 속성 체크) ✅
        if target_book.is_borrowed:
            raise LibraryError(f"이미 다른 사람이 대출 중입니다.")

        # 4) 대출 처리 (상태 변경) ✅
        target_book.is_borrowed = True  # 책 상태를 대출중(True)으로 변경
        member.borrowed_books.append(target_book)  # 회원 목록에 추가
        print(f">> '{target_book.title}' 대출이 완료됐습니다.")

    # --- 5. 반납 ---
    def return_book(self, member_name, isbn):
        if member_name not in self.members:
            raise LibraryError("등록되지 않은 회원입니다.")
        member = self.members[member_name]

        # 회원이 빌린 책 목록에서 찾기
        target_book = None
        for book in member.borrowed_books:
            if book.isbn == isbn:
                target_book = book
                break

        if target_book is None:
            raise LibraryError("해당 책을 빌린 기록이 존재하지 않습니다.")

        # 반납 처리 (상태 변경) ✅
        target_book.is_borrowed = False  # 책 상태를 대출가능(False)으로 복구
        member.borrowed_books.remove(target_book)  # 회원 목록에서 제거
        print(f">> '{target_book.title}' 반납이 완료되었습니다.")

    # --- 6. 도서 목록 출력 ---
    def book_list(self):
        print("\n=== 도서 목록 ===")
        if not self.books:
            print("등록된 도서가 없습니다.")
        for book in self.books:
            print(book)  # Book 클래스의 __str__ 호출

    # --- 7. 도서 검색 ---
    def search_books(self, keyword):
        found = False
        for book in self.books:
            if keyword in book.title:
                print(book)
                found = True
        if not found:
            print("검색 결과가 없습니다.")
