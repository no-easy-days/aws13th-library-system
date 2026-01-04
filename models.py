import csv

import datetime

from utils import InvalidISBNError

"""
Book 클래스
"""
class Book:
    def __init__(self,title,author,isbn):

        self.title=title
        self.author=author
        if not (isbn.isdigit() and len(isbn) == 13):
            raise InvalidISBNError("[SYSTEM] ISBN은 반드시 13자리 숫자여야 합니다.")
        self.isbn=isbn
        self.is_loaned= False
        self.loan_date = None
        self.due_date = None

    # def loan_book(self):
    def to_dict(self):
        # CSV에 저장할 수 있도록 dict로 변환
        return {
            "title": self.title,
            "author": self.author,
            "isbn": self.isbn,
            "loan": self.is_loaned
        }

    def is_overdue(self):
        if self.is_loaned and self.due_date and datetime.now() > self.due_date:
            return True
        return False


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
        self.loaned_book.remove(book)

    def to_dict(self):
        # CSV에 저장할 수 있도록 dict로 변환
        return {
            "name": self.name,
            "phone": self.phone
        }

"""
Library 클래스
"""
class Library:

    def __init__(self):
        self.library_book=[]
        self.library_members=[]
        self.book_file_path = None
        self.member_file_path = None

    def set_book(self, file_path):
        self.book_file_path = file_path
        with open(file_path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for index, row in enumerate(reader, start=1):
                my_book = Book(row["title"], row["author"], row["isbn"])
                self.library_book.append(my_book)

    def add_book(self,book):
        for b in self.library_book:
            if b.isbn == book.isbn:
                print(f"[SYSTEM] 이미 등록된 책의 ISBN입니다: {b.isbn}")
                return

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
        with open(file_path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for index, row in enumerate(reader, start=1):
                my_member = Member(row["name"], row["phone"])
                self.library_members.append(my_member)

    def add_member(self,member):
        for m in self.library_members:
            if m.name == member.name or m.phone == member.phone:
                print(f"[SYSTEM] 이미 등록된 회원입니다: {m.name}, {m.phone}")
                return False

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
        else: print("도서관에 책이 없음")
