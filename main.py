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
            return f"{self.title} by {self.author} (ISBN: {self.isbn}) - 대출 중"
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

# # 현재까지 추가된 책 목록 출력
# for book in library.books:
#     print(book)

# 구현해야할 기능 : 도서 등록: 제목, 저자, ISBN 입력 받아 저장
# title = input("책 제목을 입력하세요: ")
# author = input("책 저자를 입력하세요: ")
# isbn = input("책 ISBN을 입력하세요: ")
# new_book = Book(title, author, isbn)
# library.add_book(new_book)
# print(f"'{new_book.title}' 책이 등록되었습니다.")

for book in library.books:
   print(book)