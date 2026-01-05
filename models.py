class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_borrowed = False

    # 책 정보 문자열 반환
    def __str__(self):
        status = "[대출중]" if self.is_borrowed else "[대출가능]"
        # 대출상태값 print시 볼 수 있도록 변경 -- 2026.01.05
        # return f"{self.title} | {self.author} | {self.isbn}"
        return f"{self.title} | {self.author} | {self.isbn} | {status} "

class Member:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone
        self.borrowed_books = []

    # 회원 정보 문자열 반환 -- 2026.01.05
    def __str__(self):
        return f"{self.name} | {self.phone}"

class Library:
    def __init__(self):
        # 1. books: Book 클래스 인스턴스들을 담는 리스트
        self.books = []
        self.members = []

    # 도서 등록 (제목, 저자, isbn 등록)
    def add_book(self, title, author, isbn):
        #books 리스트에 대해 for문 돌리고, isbn에 해당하는 밸류값 확인
        for book in self.books:
            if book.isbn == str(isbn):
                print(f"해당 isbn을 가지는 책이 이미 있습니다. 도서 등록이 불가능 합니다.")
                return None
        print(f"해당 책은 등록되어 있지 않습니다. 책 등록을 시작합니다. ")
        self.books.append(Book(title, author, isbn))
        print(f"책 등록에 성공했습니다. 책이름 : {title} | 저자 : {author} | isbn번호 : {isbn}")
        return None

    # 멤버 등록 (이름, 폰번호 등록)
    def add_member(self, name, phone):
        #members 리스트에 이름, 폰번호에서 같은거 있는지 확인
        for member_name in self.members:
            # 부분 문자열이 아닌 정확한 일치로 변경 -- 2026.01.05
            # if member_name.name in name:
            if member_name.name == name:
                print(f"해당 회원명은 이미 등록되어 있습니다. 등록할 수 없습니다.")
                return None
            # 부분 문자열이 아닌 정확한 일치로 변경 -- 2026.01.05
            # elif member_name.phone in phone:
            elif member_name.phone == phone:
                print(f"해당 휴대폰 번호는 이미 등록되어 있습니다. 등록할 수 없습니다.")
                return None
        print(f"해당 이름, 휴대폰 번호는 등록되어 있지 않습니다. 회원 등록을 시작합니다. ")
        self.members.append(Member(name, phone))
        print(f"회원 등록에 성공했습니다. 이름 : {name} | 휴대폰 번호 : {phone}")
        return None

    # 도서 목록 출력 (등록된 도서 목록 출력)
    def print_books(self):
        if not self.books:
            raise ValueError("현재 도서관의 책 정보가 없습니다. 초기화 정상 여부를 확인하세요. ")
        else:
            for book in self.books:
                print(book)
            return None

    # 도서 검색
    def find_books(self, kw_title):
        research_results = False
        for book in self.books:
            if kw_title in book.title:
                print(f"매칭되는 책 제목: {book}")
                research_results = True
        if not research_results:
            print(f"{kw_title} 키워드에 매칭되는 책이 없습니다. ")
            return None
        return None

    #도서 대출
    def borrow_book(self, name, isbn):
        # 회원이름 확인
        target_member = None
        for member in self.members:
            if member.name == name:
                target_member = member
                break
        if not target_member:
            print(f"'{name}'님은 등록된 회원이 아닙니다.")
            return None

        #Books 리스트에 일치하는 isbn 번호 확인
        for book in self.books:
            if book.isbn == str(isbn):
                print(f"일치하는 isbn 번호를 찾았습니다. 책 이름 : {book.title}")
                if book.is_borrowed:
                    print(f"해당 책은 이미 대출중입니다. ")
                    return None
                else:
                    #모든 조건 통과, bool값 바꾸고 borrowed_books에 정보 추가
                    book.is_borrowed = True
                    target_member.borrowed_books.append(book)
                print(f"성공! {target_member.name} 회원님이 '{book.title}'을 대출하였습니다. ")
                return None
        else:
            print("일치하는 isbn 번호가 없습니다. ")
        return None

    # 도서 반납
    def return_book(self, name, isbn):
        #회원 이름 확인
        target_member = None
        for member in self.members:
            if member.name == name:
                target_member = member
                break
        if not target_member:
            print(f"'{name}'님은 등록된 회원이 아닙니다.")
            return None

        # Books 리스트에 일치하는 isbn 번호 확인
        for book in self.books:
            if book.isbn == str(isbn):
                print(f"일치하는 isbn 번호를 찾았습니다. 책 이름 : {book.title}")
                # 다른 회원이 대출한 책의 isbn 입력 / 데이터 불일치 검증 추가 --2026.01.05
                if book not in target_member.borrowed_books:
                    print(f"{name} 님이 대출하신 책이 아닙니다. 다시 시도하세요. ")
                    return None
                # 코드 추가 끝 ---
                book.is_borrowed = False
                target_member.borrowed_books.remove(book)
                print(f"반납 처리가 완료되었습니다. ")
                return None
        else:
            print(f"일치하는 isbn 번호가 없습니다. 번호를 다시 확인해주세요. ")
        return None
