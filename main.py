
from library import Library
from models import Member
from utils import load_books_from_csv
from exceptions import *
from models import Book

def main():
    library = Library()

    books = load_books_from_csv("books.csv")
    for book in books:
        library.add_book(book)
    print("[System] books.csv 에서 도서 데이터를 불러왔습니다.")

    while True:
        print("""
=== 도서관 관리 시스템 ===
1. 도서 등록
2. 도서 목록
3. 회원 등록
4. 대출
5. 반납
6. 검색
7. 종료
""")
        try:
            choice = int(input("메뉴를 선택하세요: "))

            if choice == 1:
                title = input("제목: ")
                author = input("저자: ")
                isbn = input("ISBN: ")
                library.add_book(Book(title, author, isbn))

            elif choice == 2:
                library.list_books()

            elif choice == 3:
                name = input("이름: ")
                phone = input("전화번호: ")
                library.add_member(Member(name, phone))

            elif choice == 4:
                name = input("회원 이름: ")
                isbn = input("ISBN: ")
                library.borrow_book(name, isbn)
                print("대출 완료")

            elif choice == 5:
                name = input("회원 이름: ")
                isbn = input("ISBN: ")
                library.return_book(name, isbn)
                print("반납 완료")

            elif choice == 6:
                keyword = input("검색어: ")
                library.search_books(keyword)

            elif choice == 7:
                print("프로그램 종료")
                break

            else:
                print("잘못된 선택입니다.")

        except LibraryError as e:
            print(f"[ERROR] {e}")
        except ValueError:
            print("[ERROR] 숫자를 입력하세요.")

if __name__ == "__main__":
    main()
