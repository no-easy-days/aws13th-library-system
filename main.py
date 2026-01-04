from book import Book
from library import Library
import csv

library = Library()

def load_books_from_csv(filename):
    books = []
    try:
        with open(filename, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                book = Book(row["title"].strip(), row["author"].strip(), row["isbn"].strip())
                books.append(book)
    except FileNotFoundError:
        print("books.csv 파일을 찾을 수 없습니다.")
    return books

books = load_books_from_csv("books.csv")
for b in books:
    library.add_book(b.title, b.author, b.isbn)

print("[System] books.csv에서 도서 데이터를 불러왔습니다.")

while True:
    print("\n=== 도서관 관리 시스템 ===")
    print("1. 도서 등록")
    print("2. 도서 목록")
    print("3. 회원 등록")
    print("4. 대출")
    print("5. 반납")
    print("6. 검색")
    print("7. 종료")

    num = input("메뉴를 선택하세요: ")

    if num == "1":
        title = input("책 제목: ")
        author = input("저자: ")
        isbn = input("ISBN: ")
        library.add_book(title, author, isbn)

    elif num == "2":
        library.list_books()
    elif num == "3":
        name = input("회원 이름: ")
        phone = input("전화번호: ")
        library.add_member(name, phone)

    elif num == "4":
        member_name = input("회원 이름: ")
        isbn = input("대출할 책 ISBN: ")
        library.borrow_book(member_name, isbn)
    elif num == "5":
        member_name = input("회원 이름: ")
        isbn = input("반납할 책 ISBN: ")
        library.return_book(member_name, isbn)
    elif num == "6":
        word = input("검색할 책 제목: ")
        library.search_book(word)

    elif num == "7":
        print("프로그램을 종료합니다.")
        break
    else :
        print("잘못된 입력입니다.")


