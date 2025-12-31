"""
여기서 Book 클래스, Member 클래스, Library 클래스 여기서 작성하고
"""

class Book:
    """
    - 속성 : title,author,isbn,is_borrowed
    - 메서드 : __str__(책 정보 문자열 반환)
    """
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_borrowed = False
    def __str__(self):
        return f"{self.title} {self.author} {self.isbn}"

class Member:
    """
    - 속성 : name, phone, borrowed_books(현재 대출 중인 책 목록)
    """
    def __init__(self ,name ,phone):
        self.name = name
        self.phone = phone
        self.borrowed_books = []
    # ▼ 이 메서드가 "출력 모양"을 결정합니다!
    def __str__(self):
        return f"{self.name} {self.phone}"

class Library:
    """
    -속성: books(Book 객체 리스트) , members(Member 객체 딕셔너리)
    -메서드 : add_book,add_member,borrow_book,return_book
    이러면 상속?
    """
    def __init__(self):
        self.books = []
        self.members = {}
    def add_book(self ,book):
        self.books.append(book)
    def register_book(self, title, author, isbn):
        # 책을 등록하는 메소드
        book = Book(title, author, isbn)
        self.add_book(book)
    def add_member(self, name, phone):
        new_member = Member(name, phone)
        self.members[name] = new_member
        print(f"{name}님이 회원으로 등록되셨습니다.")


    def borrow_book(self, name, isbn):
        # 대출 메소드
        if name not in self.members:
            print("회원이 없습니다")
            return
        # 내가 입력한 회원이 있으니깐 대출 가능한지도 일단 책이있는지 보고
        # 그 isbn에 대한 is_borrowed를 봐야하네
        target_book = None
        for book in self.books:     # 일단 책을 다 넣어
            if book.isbn == isbn:  #그렇다가 내가 입력한 isbn에 맞는 isbn이있으면
                target_book = book  # 이제 내가 찾은 책이여
                break
        if target_book is None:
            print("찾으 시는 책이 없습니다.")
            return
        if target_book.is_borrowed:  # 이건 Ture이면 빌려졌다는거니깐
            print("대출이 어렵습니다.")
        else:
            target_book.is_borrowed = True
            print("대출 처리 하였습니다.")
            print(f"{name}님이 {target_book.title} ({isbn})을 대출했습니다.")
    def return_book(self,_name, isbn):
        target_book = None
        for book in self.books:  # 일단 책을 다 넣어
            if book.isbn == isbn:  # 그렇다가 내가 입력한 isbn에 맞는 isbn이있으면
                target_book = book  # 이제 내가 찾은 책이여
                break
        if target_book is None:
            print("해당 ISBN책을 찾을 수 없습니다.") # 해당 ISBN에 맞는 책을 못찾으면
            return
        if target_book.is_borrowed:  # 이건 Ture이면 빌려졌다는거니깐
            target_book.is_borrowed = False
            print("반납 완료 했습니다.")
        else:
            print("대출안하셨습니다.")
    def search_book(self,ch):
        # if '점프'을 입력 받았다고 생각
        for book in self.books:
            if book.title.find(ch) >= 0:
                print(book.title)
                found = True
        if not found:
            print("찾으시는 책이 없는듯 합니다.")

    def __str__(self):
        return f"Library(books={len(self.books)}, members={len(self.members)})"



