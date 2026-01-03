from exception import DuplicateISBNError
from models import Book, Member

def register_book(library) -> Book:
    print("\n[도서 등록]"
          "\n도서 정보를 입력해주세요.")
    title = input("책 제목: ")
    author = input("저자: ")
    while True:
        isbn = input("isbn(13자리 숫자만 입력해주세요): ")
        if not isbn.isdigit():
            print("[ERROR] ISBN은 숫자만 입력해주세요.")
            continue
        if len(isbn) != 13:
            print("[ERROR] ISBN은 13자리 숫자 입니다.")
            continue
        try:
            library.add_book(Book(title, author, isbn))
        except DuplicateISBNError as e:
            print(f"[ERROR] {e}")
            continue
        print("\n[INFO] 도서를 등록하였습니다.")
        break


# def register_member(library):
#     print("\n[회원 등록]"
#           "\n회원 정보를 입력해주세요.")
#     name = input("이름: ")
#     while True:
#         phone = input("핸드폰 번호 (숫자만 입력해주세요): ")
#         if not phone.isdigit():
#             print("[ERROR] 숫자만 입력해주세요.")
#             continue
#         if len(phone) != 11:
#             print("[ERROR] 숫자 11자리를 입력해주세요.")
#             continue
#         library.add_member(Member(name, phone))
#         print("\n회원정보를 등록하였습니다.")
#         break
#
#
# # def borrow_book(library):
# #     print("\n[도서 대출]"
# #           "\n회원 정보와 대출하실 도서를 입력해주세요.")
# #     # TODO: isbn 입력 에러 처리 코드 중복 어떻게 처리할지 고민
# #     name = input("회원명: ")
# #     book_isbn = input("도서 isbn: ")
#
#
def process_menu_choice(library, choice: int) -> None:
    if choice == 1:
        register_book(library)
    elif choice == 2:
        # TODO: 여유 있으면 출력 서식 지정
        library.book_list()
        pass
    elif choice == 3:
        # register_member(library)
        pass
    elif choice == 4:
        # borrow_book(library)
        pass
    elif choice == 5:
        pass
    elif choice == 6:
        pass