class Book:
    # 책 정보를 담는 클래스
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_borrowed = False  # 대출 여부 (기본값을 대출 가능으로 설정함)
        # 대출 여부를 매개 변수로 받지 않고 내부에서 초기화함
    
    def __str__(self):
        # 책 정보를 문자열로 반환
        status = "대출중" if self.is_borrowed else "대출가능"
        return f"[{status}] {self.title} - {self.author} (ISBN: {self.isbn})"


class Member:
    # 도서관 회원 정보를 담는 클래스
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone
        self.borrowed_books = []  # 현재 대출 중인 책 목록
    
    def __str__(self):
        # 회원 정보를 문자열로 반환
        book_count = len(self.borrowed_books) # 해당 회원이 대출한 책의 권수 계산
        return f"{self.name} ({self.phone}) - 대출중인 책: {book_count}권"

# 사용자 정의 예외 클래스
# Exception 클래스 상속받음 
class BookNotFoundError(Exception):
    # 책을 찾을 수 없을 때
    pass

class MemberNotFoundError(Exception):
    # 회원을 찾을 수 없을 때
    pass

class BookAlreadyBorrowedError(Exception):
    # 이미 대출중인 책을 대출하려 할 때
    pass

class BookNotBorrowedError(Exception):
    # 대출중이 아닌 책을 반납하려 할 때
    pass

class Library:
    # 도서관 전체 시스템을 관리하는 클래스
    def __init__(self):
        self.books = []  # Book 객체들을 저장하는 리스트
        self.members = {}  # Member 객체들을 저장하는 딕셔너리 (키 - 이름, 값 - Member 객체)
    
    def add_book(self, book):
        # 도서를 도서관에 추가
        self.books.append(book)
    
    def add_member(self, member):
        # 회원을 도서관에 추가
        self.members[member.name] = member # (키 - 이름, 값 - Member 객체)
    
    def find_book_by_isbn(self, isbn):
        # ISBN으로 책 찾기
        for book in self.books: # 리스트 순회
            if book.isbn == isbn:
                return book 
        return None
    
    def find_member_by_name(self, name):
        # 이름으로 회원 찾기
        return self.members.get(name) # 키에 해당하는 값을 반환 / 키가 없으면 None반환 (에러 발생하지 않음)
    
    def borrow_book(self, member_name, isbn):
        # 도서 대출 처리
        # 1. 회원 확인
        member = self.find_member_by_name(member_name)
        if member is None:
            raise MemberNotFoundError(f"'{member_name}' 회원을 찾을 수 없습니다.")
            # 회원이 없는 경우 raise를 통해 예외(에러)를 발생시킴
        # 2. 책 확인
        book = self.find_book_by_isbn(isbn)
        if book is None:
            raise BookNotFoundError(f"ISBN '{isbn}'인 책을 찾을 수 없습니다.")
        # 3. 대출 가능 여부 확인
        if book.is_borrowed: # True면 이미 대출중
            raise BookAlreadyBorrowedError(f"'{book.title}'는 이미 대출중입니다.")
        
        # 4. 대출 처리
        book.is_borrowed = True # 대출 중으로 상태 변경
        member.borrowed_books.append(book)
        return book
    
    def return_book(self, member_name, isbn):
        # 도서 반납 처리
        # 1. 회원 확인
        member = self.find_member_by_name(member_name)
        if member is None:
            raise MemberNotFoundError(f"'{member_name}' 회원을 찾을 수 없습니다.")
        # 2. 책 확인
        book = self.find_book_by_isbn(isbn)
        if book is None:
            raise BookNotFoundError(f"ISBN '{isbn}'인 책을 찾을 수 없습니다.")
        
        # 3. 대출 중인지 확인 
        if not book.is_borrowed:
            raise BookNotBorrowedError(f"'{book.title}'는 대출중이 아닙니다.")
        # 4. 이 회원이 빌린 책인지 확인
        if book not in member.borrowed_books:
            raise BookNotBorrowedError(f"'{member_name}'님이 대출한 책이 아닙니다.")
        
        # 5. 반납 처리
        book.is_borrowed = False # 대출 가능 상태로 변경
        member.borrowed_books.remove(book) # 회원의 대출목록에서 책 제거
        return book
    
    def search_books(self, keyword):
        # 제목으로 책 검색
        results = [] # 검색 결과를 담을 빈 리스트 생성
        for book in self.books:
            if keyword.lower() in book.title.lower(): # 부분 문자열 검색
                # 검색 성능 향상을 위해 문자열을 소문자로 변환
                results.append(book) # 조건에 맞는 책을 리스트에 추가
        return results
    
    def display_all_books(self):
        # 모든 책 목록 출력
        if not self.books:
            print("도서관에 등록된 책이 없습니다.")
            return
        
        print("\n=== 전체 도서 목록 ===")
        for i, book in enumerate(self.books, 1): # enumerate() : 인덱스와 값 동시 반환
            # 목록 편의를 위해 1부터 시작하도록 함
            print(f"{i}. {book}")
        print()

