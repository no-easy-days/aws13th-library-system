from models import Book, Member, Library
from utils import print_menu, input_number, load_books_from_csv

def main():
    library = Library()

    # CSV 로드
    books = load_books_from_csv("books.csv")
    for book in books:
        library.add_book(book)

    print(f"초기 도서 {len(books)}권 로드 완료")

    while True:
        print_menu()
        choice = input_number("메뉴 선택: ")

        if choice == 1:
            title = input("제목: ")
            author = input("저자: ")
            isbn = input("ISBN: ")
            library.add_book(Book(title, author, isbn))
            print("도서 등록 완료")

        elif choice == 2:
            for book in library.list_books():
                print(book)

        elif choice == 3:
            name = input("이름: ")
            phone = input("전화번호: ")
            library.add_member(Member(name, phone))
            print("회원 등록 완료")

        elif choice == 4:
            name = input("회원 이름: ")
            isbn = input("ISBN: ")
            if library.borrow_book(name, isbn):
                print("대출 완료")
            else:
                print("대출 실패")

        elif choice == 5:
            name = input("회원 이름: ")
            isbn = input("ISBN: ")
            if library.return_book(name, isbn):
                print("반납 완료")
            else:
                print("반납 실패")

        elif choice == 6:
            keyword = input("검색할 제목 일부: ")
            results = library.search_books(keyword)
            for book in results:
                print(book)

        elif choice == 0:
            print("프로그램 종료")
            break

        else:
            print("잘못된 메뉴입니다.")

if __name__ == "__main__":
    main()
