"""
도서관의 기능을 하는 로직을 담당하는 클래스 생성
기능 - 도서 등록, 도서 목록, 회원 추가, 대출, 반납 ,검색
각각의 함수 만들고 기능 구현
"""
from member import Member
from book import Book



class Library:
    def __init__(self):
        self.books = []
        self.members = {}


    def add_book(self,title,author,isbn):    #도서 등록
        book = Book(title,author,isbn)
        self.books.append(book)
        print("도서가 등록되었습니다")

    def list_books(self):      #도서 목록
        for book in self.books:
            print(book)

    def add_member(self,name,phone):     #회원등록
        member = Member(name,phone)
        self.members[name] = member
        print("회원이 등록되었습니다.")

    def borrow_book(self,member_name,isbn):    #대출
        if member_name not in self.members:      #회원 존재 확인
            print("존재하지 않는 회원입니다")
            return
        book  = None
        for b in self.books:
            if b.isbn.strip()== isbn.strip():
                book = b
                break
        if book is None:
            print("해당 책이 없습니다.")
            return
        if book.is_borrowed:      #대출 가능 여부 확인
            print("이미 대출 중인 책입니다")
            return
        book.is_borrowed = True
        self.members[member_name].borrowed_books.append(book)
        print(f">> '{member_name}'님이 '{book.title}' ({book.isbn})을 대출했습니다.")

    def return_book(self,member_name,isbn):
        if member_name not in self.members:
            print("존재하지 않는 회원입니다")
            return
        member = self.members[member_name]

        book = None
        for b in member.borrowed_books:
            if b.isbn.strip() == isbn.strip():
                book = b
                break
        if book is None:
            print("회원님이 대출한 책이 아닙니다.")
            return

        book.is_borrowed = False
        member.borrowed_books.remove(book)
        print("대출한 책이 반납되었습니다.")

    def search_book(self,word):
        search = False

        for book in self.books:
            if word in book.title:
                print(book)
                search = True
        if not search:
            print("책을 못찾았습니다")




