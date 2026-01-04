from library import Library
from models import Book, Member
from utils import load_books_from_csv
from exceptions import LibraryError

def main():
    library = Library()

    # CSV 로드
    books = load_books_from_csv("books.csv")
    for book in books:
        library.add_book(book)

    print("[System] books.csv 에서 도서 데이터를 불러왔습니다.\n")

    while True:
        print("=== 도서관 관리 시스템 ===")
        print("1. 도서 등록")
        print("2. 도서 목록")
        print("3. 회원 등록")
        print("4. 대출")
        print("5. 반납")
        print("6. 검색")
        print("7. 종료")

        try:
            menu = int(input("메뉴 선택: "))
        except ValueError:
            print("숫자를 입력하세요.\n")
            continue

        try:
            if menu == 1:
                title = input("제목: ")
                author = input("저자: ")
                isbn = input("ISBN: ")
                library.add_book(Book(title, author, isbn))

            elif menu == 2:
                library.list_books()

            elif menu == 3:
                name = input("이름: ")
                phone = input("전화번호: ")
                library.add_member(Member(name, phone))

            elif menu == 4:
                name = input("회원 이름: ")
                isbn = input("ISBN: ")
                library.borrow_book(name, isbn)

            elif menu == 5:
                name = input("회원 이름: ")
                isbn = input("ISBN: ")
                library.return_book(name, isbn)

            elif menu == 6:
                keyword = input("검색어: ")
                library.search_books(keyword)

            elif menu == 7:
                print("종료합니다.")
                break

        except LibraryError as e:
            print("[Error]", e)

        print()

if __name__ == "__main__":
    main()
