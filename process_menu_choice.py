from exception import (
    DuplicateISBNError,
    LibraryError,
    BookNotFoundError,
    BookAlreadyBorrowedError,
    BookNotBorrowedError,
    BookBorrowedByOtherMemberError
)
from models import Book, Member


def register_book(library) -> None:
    """
    도서 정보를 입력받아 도서 등록한다.

    :param library:
    :raise 이미 등록된 ISBN 등록 시 재입력 요청
    :return:
    """

    print("\n[도서 등록]"
          "\n도서 정보를 입력해주세요.")
    # TODO: 공백 입력 처리 여유 있으면 하기

    title = input("책 제목: ").strip()
    author = input("저자: ").strip()
    while True:
        isbn = input("isbn(13자리 숫자만 입력해주세요): ").strip()
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
        return


def register_member(library) -> None:
    """
    회원 정보를 입력받아 회원을 등록한다.

    UX:
    - 이름은 즉시(입력 시점) 공백/중복을 체크한다.
    - 전화번호는 숫자/길이(11자리)를 체크한다.

    :param library:
    :return:
    """
    print("\n[회원 등록]"
          "\n회원 정보를 입력해주세요.")
    # 1. 이름: 공백 + 중복 처리
    while True:
        name = input("이름: ").strip()
        if not name:
            print("[ERROR] 이름은 비어있을 수 없습니다.")
            continue
        if library.has_member(name):
            print("[ERROR] 이미 등록된 회원 이름입니다.")
            continue
        break

    # 2. 핸드폰 번호: 숫자 11자리
    # 중복 처리는 따로 하지 않음
    while True:
        phone = input("핸드폰 번호 (숫자만 입력해주세요): ").strip()
        if not phone.isdigit():
            print("[ERROR] 숫자만 입력해주세요.")
            continue
        if len(phone) != 11:
            print("[ERROR] 숫자 11자리를 입력해주세요.")
            continue
        library.add_member(Member(name, phone))
        print("\n[INFO] 회원 정보를 등록하였습니다.")
        return



def handle_borrow_book(library) -> None:
    """
    도서 대출(UI 컨트롤러).

    - 회원명 입력(공백/미등록 시 재입력)
    - ISBN 입력(형식 오류/미등록/이미 대출중 시 재입력)
    - 최종 대출 처리 로직은 Library.borrow_book()이 담당

    :param library:
    :return:
    """

    print("\n[도서 대출]"
          "\n회원 정보와 대출 하실 도서를 입력해 주세요.")
    # 회원명 입력
    while True:
        name = input("회원명: ").strip()
        if not name:
            print("[ERROR] 회원 이름을 입력해 주세요.")
            continue
        if not library.has_member(name):
            print("[ERROR] 등록되지 않은 회원 입니다.")
            continue
        break
    # TODO: 입력 처리 나중에 함수로 빼기
    # ISBN 입력
    while True:
        isbn = input("도서 ISBN (13자리 숫자만 입력해주세요): ").strip()
        if not isbn.isdigit():
            print("[ERROR] ISBN은 숫자만 입력해주세요.")
            continue
        if len(isbn) != 13:
            print("[ERROR] ISBN은 13자리 숫자 입니다.")
            continue
        try:
            library.borrow_book(name, isbn)
        except (BookNotFoundError, BookAlreadyBorrowedError) as e:
            print(f"[ERROR] {e}")
            continue
        except LibraryError as e: # 메뉴로 돌아감
            print(f"[ERROR] {e}")
            return
        # TODO: isbn대신 책 이름 출력이 보기에는 좋을 듯
        print(f"\n[INFO] {name}님이 도서 {isbn}을 대출하였습니다.")
        return


def handle_return_book(library) -> None:
    """
    도서 반납(UI 컨트롤러)

    - 회원명 입력(공백/미등록 시 재입력)
    - ISBN 입력(형식 오류/미등록/대출 상태 아님/다른 회원 대출 중이면 재입력)
    - 최종 반납 처리 로직은 Library.return_book()이 담당

    :param library:
    :return:
    """
    print("\n[도서 반납]"
          "\n회원 정보와 반납 하실 도서를 입력해 주세요.")
    # 회원명 입력
    while True:
        name = input("회원명: ").strip()
        if not name:
            print("[ERROR] 회원 이름을 입력해 주세요.")
            continue
        if not library.has_member(name):
            print("[ERROR] 등록되지 않은 회원 입니다.")
            continue
        break
    # TODO: 입력 처리 나중에 함수로 빼기
    # ISBN 입력
    while True:
        isbn = input("도서 ISBN (13자리 숫자만 입력해주세요): ").strip()
        if not isbn.isdigit():
            print("[ERROR] ISBN은 숫자만 입력해주세요.")
            continue
        if len(isbn) != 13:
            print("[ERROR] ISBN은 13자리 숫자 입니다.")
            continue
        try:
            library.return_book(name, isbn)
        except (BookNotFoundError, BookNotBorrowedError, BookBorrowedByOtherMemberError) as e:
            print(f"[ERROR] {e}")
            continue
        except LibraryError as e:  # 메뉴로 돌아감
            print(f"[ERROR] {e}")
            return
        # TODO: isbn대신 책 이름 출력이 보기에는 좋을 듯
        print(f"\n[INFO] {name}님이 도서 {isbn}을 반납하였습니다.")
        return



def process_menu_choice(library, choice: int) -> None:
    if choice == 1:
        register_book(library)
    elif choice == 2:
        # TODO: 여유 있으면 출력 서식 지정
        library.book_list()
    elif choice == 3:
        register_member(library)
    elif choice == 4:
        handle_borrow_book(library)
    elif choice == 5:
        handle_return_book(library)
    elif choice == 6:
        pass
