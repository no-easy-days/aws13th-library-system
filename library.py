import re
import csv

from models import Member, Book, BookRequest
from exceptions import ValidationError, DuplicateError, AuthenticationError, NotFoundError, AlreadyBorrowedError, UnauthorizedError

class Library:
    def __init__(self):
        self.members:dict[str,Member] = {}
        self.books:dict[str,Book] = {}
        self.requests:list[BookRequest] = []
        self.next_request_id = 1

    def _normalize_phone(self,phone:str) -> str:
        """
            입력 예:
                - 01012345678
                - 010 1234 5678
                - 010 1234 5678
            저장 형식:
                - 010-1234-5678
        """
        digits = re.sub(r'\D','',phone)
        if len(digits) != 11 or not digits.startswith("010"):
            raise ValidationError("전화번호는 010-0000-0000 형식(총 11자리)이어야 합니다.")

        mid = digits[3:7]
        last = digits[7:11]
        return f"010-{mid}-{last}"

    def _validate_password(self,password:str) -> None:
        if not (4 <= len(password) <= 13):
            raise ValidationError("비밀번호는 4자리 이상 13자리 이하로 입력하세요.")

    def seed_admin(self) -> None:#프로그램 시작시 1회 호출해서 관리자 계정 만들기
        admin_id = "admin"
        if admin_id in self.members:
            return
        self.members[admin_id] = Member(
            member_id="admin",
            name = "백시관",
            phone = "010-1234-5678",
            password = "1234567890",
            role = "admin"
        )

    def register_member(self,member_id: str, name: str, phone: str, password: str) -> Member:
        member_id = member_id.strip()
        name = name.strip()

        if member_id == "":
            raise ValidationError("회원 아이디는 비어있을 수 없습니다.")
        if name == "":
            raise ValidationError("이름은 비어있을 수 없습니다.")
        if member_id in self.members:
            raise ValidationError("이미 존재하는 회원 아이디입니다.")

        nomalized_phone = self._normalize_phone(phone)
        self._validate_password(password)

        m = Member(member_id=member_id, name=name, phone=nomalized_phone, password=password,role="member")
        self.members[member_id] = m
        return m

    def login(self,member_id:str,password:str) -> Member:
        member_id = member_id.strip()
        if member_id not in self.members:
            raise AuthenticationError("존재하지 않는 아이디입니다")

        m=self.members[member_id]
        if m.password != password:
            raise AuthenticationError("비밀번호가 일치하지 않습니다.")
        return m
    
    def load_books_from_csv(self, filename: str) -> None:
        """CSV 파일에서 도서 정보 로드"""
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    title = row.get('title', '').strip()
                    author = row.get('author', '').strip()
                    isbn = row.get('isbn', '').strip()
                    
                    if title and author and isbn:
                        self.books[isbn] = Book(title=title, author=author, isbn=isbn)
        except FileNotFoundError:
            pass
    
    def register_book(self, title: str, author: str, isbn: str) -> Book:
        """도서 등록"""
        title = title.strip()
        author = author.strip()
        isbn = isbn.strip()
        
        if not title or not author or not isbn:
            raise ValidationError("도서 제목, 저자, ISBN은 모두 필수 입력 항목입니다.")
        
        if isbn in self.books:
            raise DuplicateError("이미 등록된 ISBN입니다.")
        
        book = Book(title=title, author=author, isbn=isbn)
        self.books[isbn] = book
        return book
    
    def get_all_books(self) -> list[Book]:
        """모든 도서 목록 반환 (제목순 정렬)"""
        books = list(self.books.values())
        return sorted(books, key=lambda b: b.title.lower())
    
    def search_books(self, query: str) -> list[Book]:
        """제목으로 도서 검색 (부분 매칭)"""
        query = query.strip().lower()
        if not query:
            return []
        
        results = []
        for book in self.books.values():
            if query in book.title.lower():
                results.append(book)
        
        return sorted(results, key=lambda b: b.title.lower())
    
    def borrow_book(self, member_id: str, isbn: str) -> None:
        """도서 대출"""
        if member_id not in self.members:
            raise NotFoundError("존재하지 않는 회원입니다.")
        
        if isbn not in self.books:
            raise NotFoundError("존재하지 않는 도서입니다.")
        
        book = self.books[isbn]
        if book.borrowed_by is not None:
            raise AlreadyBorrowedError(f"이미 대출중인 도서입니다. (대출자: {book.borrowed_by})")
        
        book.borrowed_by = member_id
    
    def return_book(self, member_id: str, isbn: str) -> None:
        """도서 반납"""
        if isbn not in self.books:
            raise NotFoundError("존재하지 않는 도서입니다.")
        
        book = self.books[isbn]
        if book.borrowed_by is None:
            raise ValidationError("대출중이 아닌 도서입니다.")
        
        if book.borrowed_by != member_id:
            raise UnauthorizedError("본인이 대출한 도서만 반납할 수 있습니다.")
        
        book.borrowed_by = None
    
    def get_member_loans(self, member_id: str) -> list[Book]:
        """회원이 대출한 도서 목록"""
        loans = []
        for book in self.books.values():
            if book.borrowed_by == member_id:
                loans.append(book)
        
        return sorted(loans, key=lambda b: b.title.lower())
    
    def get_all_loans(self) -> list[tuple[Book, str]]:
        """현재 대출중인 모든 도서 목록 (도서, 대출자)"""
        loans = []
        for book in self.books.values():
            if book.borrowed_by is not None:
                loans.append((book, book.borrowed_by))
        
        return sorted(loans, key=lambda x: x[0].title.lower())
    
    def request_book(self, member_id: str, title: str, author: str, isbn: str) -> BookRequest:
        """회원의 도서 등록 요청"""
        if member_id not in self.members:
            raise NotFoundError("존재하지 않는 회원입니다.")
        
        title = title.strip()
        author = author.strip()
        isbn = isbn.strip()
        
        if not title or not author or not isbn:
            raise ValidationError("도서 제목, 저자, ISBN은 모두 필수 입력 항목입니다.")
        
        # 이미 동일한 ISBN 요청이 있는지 확인
        for req in self.requests:
            if req.isbn == isbn and req.status == "pending":
                raise DuplicateError("이미 동일한 ISBN으로 요청이 진행중입니다.")
        
        request_id = f"REQ{self.next_request_id:04d}"
        self.next_request_id += 1
        
        request = BookRequest(
            request_id=request_id,
            member_id=member_id,
            title=title,
            author=author,
            isbn=isbn
        )
        self.requests.append(request)
        
        return request
    
    def get_pending_requests(self) -> list[BookRequest]:
        """대기중인 요청 목록"""
        return [req for req in self.requests if req.status == "pending"]
    
    def approve_request(self, request_id: str) -> Book:
        """요청 승인하고 도서 등록"""
        request = None
        for req in self.requests:
            if req.request_id == request_id:
                request = req
                break
        
        if request is None:
            raise NotFoundError("존재하지 않는 요청입니다.")
        
        if request.status != "pending":
            raise ValidationError("이미 처리된 요청입니다.")
        
        # ISBN 중복 확인
        if request.isbn in self.books:
            request.status = "rejected"
            raise DuplicateError("이미 등록된 ISBN입니다.")
        
        # 도서 등록
        book = Book(title=request.title, author=request.author, isbn=request.isbn)
        self.books[request.isbn] = book
        request.status = "approved"
        
        return book
    
    def reject_request(self, request_id: str) -> None:
        """요청 거절"""
        request = None
        for req in self.requests:
            if req.request_id == request_id:
                request = req
                break
        
        if request is None:
            raise NotFoundError("존재하지 않는 요청입니다.")
        
        if request.status != "pending":
            raise ValidationError("이미 처리된 요청입니다.")
        
        request.status = "rejected"