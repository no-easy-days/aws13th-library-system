import csv

# csv 파일을 리스트로 변환하는 함수
def csv_to_list(filename):
    with open(filename, "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        return list(reader)
    
# csv 파일에 리스트를 저장하는 함수
def list_to_csv(data, filename):
    with open(filename, "w", encoding="utf-8", newline='') as file:
        writer = csv.writer(file)

# 임시 클래스 정의 추후 수정 필요
class Book:
    def __init__(self, title, author, isbn,is_borrowed=False):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_borrowed = is_borrowed
        
    def __str__(self):
        return f"{self.title} by {self.author} (ISBN: {self.isbn})"
        
     
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
    title = row[0]
    author = row[1]
    isbn = row[2]
    book = Book(title, author, isbn)
    library.add_book(book)

# # 현재까지 추가된 책 목록 출력
# for book in library.books:
#     print(book)

