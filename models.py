class Book:
    def __init__(self, title, author, isbn, is_borrowed = False):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_borrowed = is_borrowed
    def __str__(self):
        if self.is_borrowed:
            status = "대출중"
        else:
            status = "대출가능"
        return f'{self.title} {self.author} {self.isbn} {status}'

class Member:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone
        self.borrowed_books = []

class Library:
    def __init__(self, books=None, members=None):
        self.books = books if books is not None else []
        self.members = members if members is not None else {}

    def add_book(self, book):
        self.books.append(book)

    def add_member(self, member):
        self.members[member.name] = member

    def borrow_book(self, member, isbn):
        if member not in self.members:
            print("")
            print(">>회원이 존재하지 않습니다.")
            return
        for book in self.books:
            if book.isbn == isbn:
                if book.is_borrowed:
                    print("")
                    print(">>대출중입니다")
                    return
                else:
                    book.is_borrowed = True
                    self.members[member].borrowed_books.append(book)
                    print("")
                    print(f">> {member}님이 {isbn}번 도서를 대출하였습니다.")

                    return
        else:
            print("책이 존재하지 않습니다.")
            return


    def return_books(self, member, isbn):
        if member not in self.members:
            print("")
            print(">>회원이 존재하지 않습니다.")
            return
        for book in self.books:
            if book.isbn == isbn:
                if book.is_borrowed:
                    self.members[member].borrowed_books.remove(book)
                    book.is_borrowed = False
                    print("")
                    print(f">> {member}님이 {isbn}번 도서를 반납하였습니다.")
                    return
        else:
            print("")
            print("도서 번호가 올바르지 않습니다.")
            return
    def search_book(self, target_book):
        for book in self.books:
            if target_book.lower() in book.title.lower():
                print("검색 결과 : ", book.title)
                found = True