from models import Library, LibraryError


def main():
    lib = Library()

    lib.load_books_from_csv('books.csv')

    while True:
        print("\n=== 도서관 관리 시스템 ===")
        print("1. 도서 등록")
        print("2. 도서 목록")
        print("3. 회원 등록")
        print("4. 대출")
        print("5. 반납")
        print("6. 검색")
        print("7. 종료")

        choice = input("메뉴를 선택하세요: ")

        try:
            if choice == '1':
                title = input("제목: ")
                author = input("저자: ")
                isbn = input("ISBN: ")
                lib.add_book(title, author, isbn)

            elif choice == '2':
                lib.book_list()

            elif choice == '3':
                name = input("이름: ")
                phone = input("전화번호: ")
                lib.add_member(name, phone)

            elif choice == '4':
                name = input("사용자 이름: ")
                isbn = input("대출할 책 ISBN: ")
                lib.borrow_book(name, isbn)

            elif choice == '5':
                name = input("사용자 이름: ")
                isbn = input("반납할 책 ISBN: ")
                lib.return_book(name, isbn)

            elif choice == '6':
                keyword = input("제목 키워드: ")
                lib.search_books(keyword)

            elif choice == '7':
                print("프로그램을 종료합니다.")
                break

            else:
                print("1~7 사이의 숫자를 입력해주세요.^^")

        except LibraryError as e:
            print(f"[경고] {e}")
        except Exception as e:
            print(f"[예상치 못한 에러 발생] {e}")


if __name__ == "__main__":
    main()