from utils import books
from models import Library
from exception import MemberNotFoundError,BookNotBorrowedError,BookNotFoundError,LibraryError

def menu():
    print("\n=== 도서관 관리 시스템 ===")
    print("1. 도서 등록")
    print("2. 도서 목록")
    print("3. 회원 등록")
    print("4. 대출")
    print("5. 반납")
    print("6. 검색")
    print("7. 종료")

def main():
    print("[System] books.csv 에서 도서 데이터를 불러왔습니다.")

    library = Library(books)


    while True:
        menu()
        select = input("메뉴를 선택하세요: ")

        if select == "1":
            library.add_book()

        elif select == "2":
            library.show_books()

        elif select == "3":
            library.add_member()

        elif select == "4":
            try:
                library.borrow_book()
            except MemberNotFoundError as e:
                print(e)


        elif select == "5":
            try:
                library.return_book()
            except LibraryError as e:
                print(e)


        elif select == "6":
            library.search_book()

        elif select == "7":
            print("도서관 관리 시스템을 종료합니다.")
            break

        else:
            print("잘못된 메뉴입니다. 다시 선택하세요.")

if __name__ == "__main__":
    main()