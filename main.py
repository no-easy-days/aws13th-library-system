import csv
from models import Book, Member, Library

def load_csv(filename, library):
    print("")
    try:
        with open(filename, 'r', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            header = next(reader)
            for row in reader:
                book = Book(
                    title=row[0],
                    author=row[1],
                    isbn=row[2]
                )
                library.add_book(book)
    except FileNotFoundError:
        print(f">> 오류 : {filename} 을 찾을 수 없습니다.")
    except Exception as e:
        print(f">> 파일 로드 중 오류 발생.")
def register_book(library):
    print("")
    print("[도서 등록 시스템]")

    title = input("제목 : ")
    author = input("저자 : ")
    isbn = input("ISBN : ")
    addbook = Book(title, author, isbn)
    library.add_book(addbook)
    print(f"도서 : {title}/ 저자 : {author}/ ISBN : {isbn}이 등록 완료되었습니다.")

def show_book(library):
    print("")
    print("[도서 목록 시스템]")
    print("등록 완료된 도서 목록 입니다")
    for book in library.books:
        print(book)

def register_member(library):
    print("")
    print("[회원 등록 시스템]")
    name = input("회원 이름 : ")
    phone = input("전화번호 : ")

    member = Member(name, phone)
    library.add_member(member)
    print(f">> {name}님이 {phone} 번호로 회원 등록을 완료하였습니다.")


def borrow_book(library):
    print("")
    print("[대출 시스템]")
    name = input("회원 이름 : ")
    isbn = input("도서 번호 : ")

    library.borrow_book(name, isbn)

def return_book(library):
    print("")
    print("[반납 시스템]")
    name = input("회원 이름 : ")
    isbn = input("도서 번호 : ")

    library.return_books(name, isbn)

def search_book(library):
    print("")
    print("[검색 시스템]")
    target = input("책 검색 : ")

    library.search_book(target)

def main():

    library = Library()

    load_csv('books.csv', library)
    print("[System] books.csv 에서 도서 데이터를 불러왔습니다.")
    print("")
    print("=== 도서관 관리 시스템 ===")
    print("1. 도서 등록")
    print("2. 도서 목록")
    print("3. 회원 등록")
    print("4. 대출")
    print("5. 반납")
    print("6. 검색")
    print("7. 종료")

    while True:
        choice = input("메뉴를 선택하세요 : ")
        if choice == "1":
            register_book(library)

        elif choice == "2":
            show_book(library)

        elif choice == "3":
            register_member(library)

        elif choice == "4":
            borrow_book(library)

        elif choice == "5":
            return_book(library)

        elif choice == "6":
            search_book(library)

        elif choice == "7":
            break
        else:
            print("잘못된 메뉴입니다.")


if __name__ == '__main__':
        main()

