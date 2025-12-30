import csv

# csv 파일을 리스트로 변환하는 함수
def csv_to_list(filename):
    with open(filename, "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        return list(reader)

# 임시 클래스 정의 추후 수정 필요
class Book:
    def __init__(self, title, author, isbn,is_borrowed=False):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_borrowed = is_borrowed
        
    def __str__(self):
        if self.is_borrowed:
            return f"{self.title} by {self.author} (ISBN: {self.isbn}) - 대출중"
        else:
            return f"{self.title} by {self.author} (ISBN: {self.isbn}) - 대출 가능"
     
class Member:
    def __init__(self, name,phone,borrowed_books):
        self.name = name
        self.phone = phone
        self.borrowed_books = []
        
class Library:
    def __init__(self):
        self.books = []
        self.members = {}
        
    def add_book(self, book):
        self.books.append(book)
        
    def add_member(self, member):
        self.members.append(member)
        
    def borrow_book(self, member, book):
        if book in self.books and not book.is_borrowed:
            book.is_borrowed = True
            member.borrowed_books.append(book)
            return True
        return False
    
    def return_book(self, member, book):
        if book in member.borrowed_books:
            book.is_borrowed = False
            member.borrowed_books.remove(book)
            return True
        return False
    
    
    
    
# Library 인스턴스 생성 및 예제 사용
library = Library()
# csv 파일에서 책 데이터 불러오기
init_data = csv_to_list("books.csv")
for row in init_data:
    book = Book(row[0], row[1], row[2])
    library.add_book(book)

# 구현해야할 기능 : 도서 등록: 제목, 저자, ISBN 입력 받아 저장
title = input("책 제목을 입력하세요: ")
author = input("책 저자를 입력하세요: ")
isbn = input("책 ISBN을 입력하세요: ")
new_book = Book(title, author, isbn)
library.add_book(new_book)
print(f"'{new_book.title}' 책이 등록되었습니다.")

# 구현해야할 기능 : 현재 등록된 도서 목록 출력
print("현재 등록된 도서 목록:")
for book in library.books:
    print(book)

# 구현해야할 기능 : 회원 등록: 이름, 전화번호 입력 받아 저장
name = input("회원 이름을 입력하세요: ")
phone = input("회원 전화번호를 입력하세요: ")
new_member = Member(name, phone, [])
library.add_member(new_member)

# 구현해야할 기능 : 도서 대출 : 회원 이름과 isbn 입력 받아 해당 회원 존재하고, 도서가 대출 가능하면 대출 처리
member_name = input("사용자 이름을 입력하세요: ")
isbn_to_borrow = input("대출할 책의 ISBN을 입력하세요: ")
# 우선 회원 존재 여부 확인 및 도서 존재 여부 확인 및 대출 가능산 상태 확인
# 회원 존재 여부
if member_name in library.members:
    member = library.members[member_name]
    # 도서 존재 여부
    book_to_borrow = None
    for book in library.books:
        if book.isbn == isbn_to_borrow:
            book_to_borrow = book
            break
    if book_to_borrow:
        # 도서 대출 상태 확인
        if not book_to_borrow.is_borrowed:
            library.borrow_book(member, book_to_borrow)
            print(f">> '{member_name}'님이 '{book_to_borrow.title}' ({isbn_to_borrow})을 대출했습니다.")
        else:
            print("해당 도서는 이미 대출 중입니다.")
    else:
        print("해당 ISBN의 도서를 찾을 수 없습니다.")
else:
    print("해당 이름의 회원을 찾을 수 없습니다.")
    
