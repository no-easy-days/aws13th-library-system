from dataclasses import dataclass, field
from datetime import datetime
import json
from exception import BookNotFoundException, BookAlreadyBorrowedException, MemberNotFoundException, \
    BookNotBorrowedException, UnauthorizedReturnException


@dataclass
class Book:
    """도서 정보를 담는 클래스"""
    title: str
    author: str
    isbn: str
    is_borrowed: bool = False
    borrowed_by: str | None = None
    borrowed_date: datetime | None = None

    def __str__(self):
        """책 정보를 문자열로 반환"""
        status = "대출중" if self.is_borrowed else "대출가능"
        borrower_info = f" (대출자: {self.borrowed_by})" if self.is_borrowed else ""
        return f"[{self.isbn}] {self.title} - {self.author} [{status}]{borrower_info}"

    def borrowing(self, member_phone):
        """책 빌려간 상태 처리"""
        self.is_borrowed = True
        self.borrowed_by = member_phone
        self.borrowed_date = datetime.now()

    def returning(self, loan_period_days=7):
        """반납 상태 처리"""
        over_day_num = 0
        if self.borrowed_date:
            days_borrowed = (datetime.now() - self.borrowed_date).days
            over_day_num = days_borrowed - loan_period_days
        self.is_borrowed = False
        self.borrowed_by = None
        self.borrowed_date = None
        return over_day_num


@dataclass
class Member:
    name : str
    phone : str
    borrowed_books: list[str] = field(default_factory=list)

    def __str__(self):
        book_count = len(self.borrowed_books)
        return f"{self.name} ({self.phone}) - 대출 중인 책: {book_count}권"

    def borrow_book(self, isbn):
        """회원의 대출 목록에 책 추가"""
        if isbn not in self.borrowed_books:
            self.borrowed_books.append(isbn)

    def return_book(self, isbn):
        """
        회원의 대출 목록에서 책 제거
        """
        if isbn in self.borrowed_books:
            self.borrowed_books.remove(isbn)
            return True
        return False

class Library:
    """전체 도서관 시스템을 관리하는 클래스"""

    def __init__(self, data_file='library_data.json',loan_deadline=7):
        """도서관 초기화"""
        self.books = {}
        self.members = {}
        self.loan_deadline = loan_deadline
        self.data_file = data_file

    def add_book(self, book):
        """
        도서관에 책 추가
        """
        if book.isbn in self.books:
            print(f"비상! ISBN {book.isbn}는 이미 널렸어요")
        else:
            self.books[book.isbn] = book
            print(f"'{book.title}' 책이 등록되었습니다.")

    def add_member(self, member):
        """도서관에 회원 추가"""
        if member.phone in self.members:
            print(f"비상! 전화번호 {member.phone}는 이미 가입되어있어여.")
        else:
            self.members[member.phone] = member
            print(f"{member.name}님이 회원으로 등록되었습니다.🫡🫡🫡")

    def get_book(self, isbn):
        """ISBN으로 책 검색"""
        return self.books.get(isbn)

    def get_member(self, phone):
        """전화번호로 회원 검색"""
        return self.members.get(phone)

    def list_all_books(self):
        """모든 책 목록 출력"""
        if not self.books:
            print("가난하다 우리 도서관. 책이 없어요")
            return

        print("\n=== 전체 도서 목록 ===")
        for book in self.books.values():
            print(book)
        print(f"\n총 {len(self.books)}권의 책이 등록되어 있습니다.\n")

    def search_books(self, keyword):
        """제목으로 책 검색"""
        results = [
            book for book in self.books.values()
            if keyword.lower() in book.title.lower()
        ]
        return results

    def borrow_book(self, member_phone, isbn):
        """책 대출 처리"""
        member = self.get_member(member_phone)
        if not member:
            raise MemberNotFoundException(member_phone)

        book = self.get_book(isbn)
        if not book:
            raise BookNotFoundException(isbn)

        if book.is_borrowed:
            raise BookAlreadyBorrowedException(book.title, book.borrowed_by)

        # 대출 처리
        book.borrowing(member.phone)
        member.borrow_book(isbn)
        print(f"\n>> '{member.name}'님이 '{book.title}' ({isbn})을 대출했습니다.\n")
        return True

    def return_book(self, member_phone, isbn):
        """
        책 반납 처리
        """
        member = self.get_member(member_phone)
        if not member:
            raise MemberNotFoundException(member_phone)

        book = self.get_book(isbn)
        if not book:
            raise BookNotFoundException(isbn)

        if not book.is_borrowed:
            raise BookNotBorrowedException(book.title)

        if book.borrowed_by != member.phone:
            raise UnauthorizedReturnException(book.title, book.borrowed_by, member.phone)

        # 반납 처리
        overdue_days = book.returning(self.loan_deadline)
        if not member.return_book(isbn):
            # 데이터 불일치: Book은 대출중인데 Member 목록에 없음
            raise RuntimeError(
                f"데이터 불일치 감지: '{book.title}' 책이 회원({member.phone})의 대출 목록에 없습니다."
            )

        print(f"\n>> '{member.name}'님이 '{book.title}' ({isbn})을 반납했어요.")

        if overdue_days > 0:
            print(f"!!!!!!연체를 {overdue_days}일 이나;;;;")
        else:
            print(f"  💩정상 반납되었습니다💩")
        print()

        return True

    def save_data(self):
        """도서관 데이터를 JSON 파일로 저장합니다."""
        try:
            data = {
                'books': [],
                'members': []
            }

            # 책 정보 저장
            for isbn, book in self.books.items():
                book_data = {
                    'title': book.title,
                    'author': book.author,
                    'isbn': book.isbn,
                    'is_borrowed': book.is_borrowed,
                    'borrowed_by': book.borrowed_by,
                    'borrowed_date': book.borrowed_date.isoformat() if book.borrowed_date else None
                }
                data['books'].append(book_data)

            # 회원 정보 저장
            for phone, member in self.members.items():
                member_data = {
                    'name': member.name,
                    'phone': member.phone,
                    'borrowed_books': member.borrowed_books
                }
                data['members'].append(member_data)

            # JSON 파일로 저장
            with open(self.data_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)

            return True
        except Exception as e:
            print(f"[오류] 데이터 저장 중 오류 발생: {e}")
            return False

    def load_data(self):
        """JSON 파일에서 도서관 데이터를 불러옵니다"""
        try:
            with open(self.data_file, 'r', encoding='utf-8') as f:
                data = json.load(f)

            # 책 정보 불러오기
            for book_data in data.get('books', []):
                book = Book(
                    title=book_data['title'],
                    author=book_data['author'],
                    isbn=book_data['isbn'],
                    is_borrowed=book_data.get('is_borrowed', False),
                    borrowed_by=book_data.get('borrowed_by'),
                    borrowed_date=datetime.fromisoformat(book_data['borrowed_date']) if book_data.get('borrowed_date') else None
                )
                self.books[book.isbn] = book

            # 회원 정보 불러오기
            for member_data in data.get('members', []):
                member = Member(
                    name=member_data['name'],
                    phone=member_data['phone'],
                    borrowed_books=member_data.get('borrowed_books', [])
                )
                self.members[member.phone] = member

            return True
        except FileNotFoundError:
            return False
        except Exception as e:
            print(f"[오류] 데이터 불러오기 중 오류 발생: {e}")
            return False
