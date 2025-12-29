from models import Book, Library

def register_book(library):
    print("\n[도서 등록]"
          "\n도서 정보를 입력해주세요.")
    title = input("책 제목: ")
    author = input("저자: ")
    while True:
        isbn = input("isbn(숫자만 입력해주세요): ")
        if not isbn.isdigit():
            print("[ERROR] ISBN은 숫자만 입력해주세요.")
            continue
        if len(isbn) != 13:
            print("[ERROR] ISBN은 13자리 입니다.")
            continue
        if library.check_same_isbn(isbn):
            print("[ERROR] 이미 등록된 ISBN입니다.")
            continue
        library.add_book(Book(title, author, isbn))
        print("\n도서를 등록하였습니다.")
        break


# def book_list(library):



def process_menu_choice(library, choice):
    if choice == 1:
        register_book(library)
    elif choice == 2:
        # TODO: 여유 있으면 출력 서식 지정
        library.book_list()
    elif choice == 3:
        return library
    elif choice == 4:
        return library
    elif choice == 5:
        return library
    elif choice == 6:
        return library