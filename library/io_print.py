def show_menu():
    print("""
=== 도서관 관리 시스템 ===
1. 도서 등록
2. 도서 목록
3. 회원 등록
4. 도서 대출
5. 도서 반납
6. 도서 검색
7. 종료
""")
def add_book():
    title = input("제목: ")
    author = input("저자: ")
    isbn = input("ISBN: ")
    return title, author, isbn

def list_book(books):
    if not books:
        print("도서가 없습니다.")
        return
    for book in books:
        print(book)

def add_member():
    name = input("이름: ")
    phone = input("전화번호: ")
    return name, phone

def input_name():
    return input("회원 이름: ")

def input_isbn():
    return input("ISBN: ")

def print_message(msg):
    print(f">> {msg}")