"""
도서관의 각각의 책 1권에 대한 정보를 저장하게 클래스 생성

책정보 title,author,isbn을 받아서 저장하고
책을 대출했는지에 대한 상태까지 확인
"""

class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_borrowed = False



    def __str__(self):
        status = "대출중" if self.is_borrowed else "대출가능"
        return f"{self.title} / {self.author} / {self.isbn} / {status}"
