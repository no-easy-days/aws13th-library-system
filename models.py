import csv
from datetime import datetime, timedelta
from utils import InvalidISBNError, DuplicateDataError

ISBN_ERROR_MSG = "[SYSTEM] ISBN은 반드시 13자리 숫자여야 합니다."
DUPLICATE_ISBN_ERROR_MSG= "[SYSTEM] 이미 등록된 책의 ISBN입니다"
DUPLICATE_MEMBER_ERROR_MSG = "[SYSTEM] 이미 등록된 회원입니다"
"""
Book 클래스
"""
class Book:
    def __init__(self,title,author,isbn):

        self.title=title
        self.author=author
        if not (isbn.isdigit() and len(isbn) == 13):
            raise InvalidISBNError(ISBN_ERROR_MSG)
        self.isbn=isbn
        self.is_loaned= False

    # def loan_book(self):
    def to_dict(self):
        # CSV에 저장할 수 있도록 dict로 변환
        return {
            "title": self.title,
            "author": self.author,
            "isbn": self.isbn,
            "is_loaned": self.is_loaned
        }

"""
Member 클래스
"""
class Member:
    def __init__(self,name,phone):
        self.name=name
        self.phone=phone
        self.loaned_book= []

    def add_book(self,book):
        self.loaned_book.append(book)

    def show_book(self):
        for b in self.loaned_book:
            print(f"{b.title}")

    def remove_book(self,book):
        try:
            self.loaned_book.remove(book)
        except ValueError:
            print(f"[SYSTEM] 경고: {book.title}이(가) 대출 목록에 없습니다.")

    def to_dict(self):
        # CSV에 저장할 수 있도록 dict로 변환
        return {
            "name": self.name,
            "phone": self.phone
        }

class Loan:
    def __init__(self, member_name, isbn):
        self.member_name = member_name
        self.isbn = isbn
        self.loan_date = datetime.now()
        self.due_date = self.loan_date + timedelta(days=7)
        self.is_returned = False

    def to_dict(self):
        return {
            "member_name": self.member_name,
            "isbn": self.isbn,
            "loan_date": self.loan_date.strftime("%Y-%m-%d"),
            "due_date": self.due_date.strftime("%Y-%m-%d"),
            "is_returned": self.is_returned
        }

"""
Library 클래스
"""
class Library:

    def __init__(self):
        self.library_book=[]
        self.library_members=[]
        self.loans = []
        self.book_file_path = None
        self.member_file_path = None
        self.loan_file_path = None

    def save_all_books(self):
        """도서 목록 전체를 CSV에 저장 (상태 업데이트용)"""
        if self.book_file_path:
            with open(self.book_file_path, 'w', newline='', encoding='utf-8') as f:
                fieldnames = ["title", "author", "isbn", "is_loaned"]
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                writer.writeheader()
                for b in self.library_book:
                    writer.writerow(b.to_dict())

    def add_loan(self, loan):
        self.loans.append(loan)
        if self.loan_file_path:
            with open(self.loan_file_path, 'w', newline='', encoding='utf-8') as f:
                fieldnames = ["member_name", "isbn", "loan_date", "due_date", "is_returned"]
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                writer.writeheader()
                for ln in self.loans:
                    writer.writerow(ln.to_dict())

    def set_book(self, file_path):
        self.book_file_path = file_path
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    my_book = Book(row["title"], row["author"], row["isbn"])
                    # CSV의 문자열 "True"/"False"를 불리언으로 변환
                    my_book.is_loaned = row["is_loaned"] == "True"
                    self.library_book.append(my_book)
        except FileNotFoundError:
            print(f"[SYSTEM] 파일을 찾을 수 없습니다: {file_path}")
        except (csv.Error, UnicodeDecodeError, KeyError) as e:
            print(f"[SYSTEM] 파일 로드 중 오류 발생: {e}")

    def set_loan(self, file_path):
        self.loan_file_path = file_path
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    loan = Loan(row["member_name"], row["isbn"])
                    loan.loan_date = datetime.strptime(row["loan_date"], "%Y-%m-%d")
                    loan.due_date = datetime.strptime(row["due_date"], "%Y-%m-%d")
                    loan.is_returned = row["is_returned"] == "True"
                    self.loans.append(loan)

                    # [중요] 프로그램 시작 시 대출 중인 책을 회원에게 연결
                    if not loan.is_returned:
                        m = next((m for m in self.library_members if m.name == loan.member_name), None)
                        b = next((b for b in self.library_book if b.isbn == loan.isbn), None)
                        if m and b:
                            m.add_book(b)
        except FileNotFoundError:
            print(f"[SYSTEM] 파일을 찾을 수 없습니다: {file_path}")
        except (csv.Error, UnicodeDecodeError, KeyError) as e:
            print(f"[SYSTEM] 파일 로드 중 오류 발생: {e}")

    def return_loan(self, member_name, isbn):
        """반납 처리 및 파일 갱신"""
        for loan in self.loans:
            if loan.member_name == member_name and loan.isbn == isbn and not loan.is_returned:
                loan.is_returned = True
                self.update_loan_file()
                return True
        return False

    def update_loan_file(self):
        """대출 목록 전체 갱신"""
        if self.loan_file_path:
            with open(self.loan_file_path, 'w', newline='', encoding='utf-8') as f:
                fieldnames = ["member_name", "isbn", "loan_date", "due_date", "is_returned"]
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                writer.writeheader()
                for ln in self.loans:
                    writer.writerow(ln.to_dict())

    def add_book(self,book):
        for b in self.library_book:
            if b.isbn == book.isbn:
                raise DuplicateDataError(DUPLICATE_ISBN_ERROR_MSG)

        self.library_book.append(book)
        if self.book_file_path:
            with open(self.book_file_path, 'w', newline='', encoding='utf-8') as f:
                fieldnames = ["title", "author", "isbn","is_loaned"]
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                writer.writeheader()
                for b in self.library_book:
                    writer.writerow(b.to_dict())

    def set_member(self, file_path):
        self.member_file_path = file_path
        try :
            with open(file_path, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    my_member = Member(row["name"], row["phone"])
                    self.library_members.append(my_member)
        except FileNotFoundError:
            print(f"[SYSTEM] 파일을 찾을 수 없습니다: {file_path}")
        except (csv.Error, UnicodeDecodeError, KeyError) as e:
            print(f"[SYSTEM] 파일 로드 중 오류 발생: {e}")

    def add_member(self,member):
        for m in self.library_members:
            if m.name == member.name or m.phone == member.phone:
                raise DuplicateDataError(DUPLICATE_MEMBER_ERROR_MSG)

        self.library_members.append(member)
        if self.member_file_path:
            with open(self.member_file_path, 'w', newline='', encoding='utf-8') as f:
                fieldnames = ["name", "phone"]
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                writer.writeheader()
                for m in self.library_members:
                    writer.writerow(m.to_dict())
        return True

    def show_library(self):
        for i,b in enumerate(self.library_book, start=1):
            print(f"{i}.이름 : {b.title} / 작가 : {b.author}  / isbn : {b.isbn}  / 도서의 대출상태 : {b.is_loaned}")

    def show_member(self):
        for m in self.library_members:
            print(f"{m.name} / {m.phone}")

    def search_book(self,title):
        for b in self.library_book:
            if title.lower() in b.title.lower():
                print(f"책이 존재 - {b.title} / {b.author} / {b.isbn} / {b.is_loaned}")
                break
        else:
            print("도서관에 책이 없음")
