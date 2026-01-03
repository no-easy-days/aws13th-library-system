from models import Book, Member, Library

def main():
    library = Library()

    while True:
        print("\n===== 도서관 관리 시스템 =====")
        print("1. 도서 등록")
        print("2. 도서 목록 출력")
        print("3. 회원 등록")
        print("4. 도서 대출")
        print("5. 도서 반납")
        print("6. 도서 검색")
        print("0. 종료")

        choice = input("메뉴 선택: ")

        if choice == "1":
            title = input("제목: ")
            author = input("저자: ")
            isbn = input("ISBN: ")
            library.add_book(Book(title, author, isbn))
            print("도서 등록 완료")

        elif choice == "2":
            for book in library.list_books():
                print(book)

        elif choice == "3":
            name = input("이름: ")
            phone = input("전화번호: ")
            library.add_member(Member(name, phone))
            print("회원 등록 완료")

        elif choice == "4":
            name = input("회원 이름: ")
            isbn = input("ISBN: ")
            if library.borrow_book(name, isbn):
                print("대출 완료")
            else:
                print("대출 실패")

        elif choice == "5":
            name = input("회원 이름: ")
            isbn = input("ISBN: ")
            if library.return_book(name, isbn):
                print("반납 완료")
            else:
                print("반납 실패")

        elif choice == "6":
            keyword = input("검색할 제목 일부: ")
            results = library.search_books(keyword)
            for book in results:
                print(book)

        elif choice == "0":
            print("프로그램 종료")
            break

        else:
            print("잘못된 입력입니다.")

if __name__ == "__main__":
    main()
