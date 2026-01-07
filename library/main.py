import csv
from models import Book, Member, Library
import io_print as io


def load_books(library):
    try:
        with open("books.csv", newline="", encoding="utf-8") as f:
            reader = csv.reader(f)
            for row in reader:
                if len(row) == 3:
                    title, author, isbn = row
                    library.add_book(Book(title, author, isbn))
    except FileNotFoundError:
        print(">> books.csv 파일을 찾을 수 없습니다.")
    except csv.Error as e:
        print(f">> CSV 오류: {e}")


def main():
    library = Library()
    load_books(library)
    io.print_message("books.csv에서 도서 데이터를 불러왔습니다.")

    while True:
        io.show_menu()
        try:
            choice = int(input("메뉴 선택: "))

            if choice == 1:
                print("[도서 등록]")
                title, author, isbn = io.add_book()
                library.add_book(Book(title, author, isbn))
                io.print_message("도서 등록 완료")

            elif choice == 2:
                print("[도서 목록]")
                io.list_book(library.list_book())

            elif choice == 3:
                print("[회원 등록]")
                name, phone = io.add_member()
                library.add_member(Member(name, phone))
                io.print_message("회원 등록 완료")

            elif choice == 4:
                print("[도서 대출]")
                name = io.input_name()
                if not library.has_member(name):
                    io.print_message("등록된 회원이 아닙니다.")
                    continue
                isbn = io.input_isbn()
                book = library.borrow_book(name, isbn)
                io.print_message(f"'{name}'님이 '{book.title}' ({book.isbn})을 대출했습니다.")

            elif choice == 5:
                print("[도서 반납]")
                name = io.input_name()
                if not library.has_member(name):
                    io.print_message("등록된 회원이 아닙니다.")
                    continue
                isbn = io.input_isbn()
                book = library.return_book(name, isbn)
                io.print_message(f"'{name}'님이 '{book.title}' ({book.isbn})을 반납했습니다.")

            elif choice == 6:
                print("[도서 검색]")
                keyword = input("검색어: ")
                if not keyword.strip():
                    io.print_message("검색어를 입력해주세요.")
                    continue
                io.list_book(library.search_book(keyword))

            elif choice == 7:
                io.print_message("프로그램 종료")
                break

            else:
                io.print_message("잘못된 선택입니다.")

        except ValueError as e:
            io.print_message(e)

if __name__ == "__main__":
    main()