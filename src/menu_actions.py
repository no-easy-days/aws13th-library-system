from src.exception import (
    DuplicateISBNError,
    LibraryError,
    BookNotFoundError,
    BookAlreadyBorrowedError,
    BookNotBorrowedError,
    BookBorrowedByOtherMemberError
)
from src.models import Book, Member
from src.utils import prompt_input_valid, isbn13, phone11, non_empty


def register_book(library) -> None:
    """
    도서 정보를 입력받아 도서 등록한다.

    :param library:
    :raise 이미 등록된 ISBN 등록 시 재입력 요청
    :return:
    """

    print("\n[도서 등록]"
          "\n도서 정보를 입력해주세요.")
    title = prompt_input_valid("책 제목: ", validator=non_empty)
    author = prompt_input_valid("저자: ", validator=non_empty)
    while True:
        isbn = prompt_input_valid("isbn(13자리 숫자만 입력해주세요): ", validator=isbn13)
        try:
            library.add_book(Book(title, author, isbn))
        except DuplicateISBNError as e:
            print(f"[ERROR] {e}")
            continue
        print("\n[INFO] 도서를 등록하였습니다.")
        return

def print_book_table(books: list, header: str) -> None:
    """
    도서 목록/검색 결과를 공통 테이블 포맷으로 출력한다.

    :param books: Book 객체 리스트
    :param header: 출력 헤더 (ex. "[도서 목록]", "[검색 결과]")
    :return:
    """
    TITLE_WIDTH = 32
    AUTHOR_WIDTH = 22
    ISBN_WIDTH = 13
    STATUS_WIDTH = 10

    def format_text(text: str, width: int) -> str:
        if len(text) > width:
            return text[: width - 3] + "..."
        return text.ljust(width)

    print(f"\n{header}")
    print("=" * (TITLE_WIDTH + ISBN_WIDTH + STATUS_WIDTH + AUTHOR_WIDTH + 16))
    print(
        f"{'ISBN'.ljust(ISBN_WIDTH)}  "
        f"{'제목'.ljust(TITLE_WIDTH)}  "
        f"{'저자'.ljust(AUTHOR_WIDTH)}  "
        f"{'상태'.ljust(STATUS_WIDTH)}"
    )
    print("=" * (TITLE_WIDTH + ISBN_WIDTH + STATUS_WIDTH + AUTHOR_WIDTH + 16))
    for book in books:
        print(
            f"{format_text(book.isbn, ISBN_WIDTH)}  "
            f"{format_text(book.title, TITLE_WIDTH)}  "
            f"{format_text(book.author, AUTHOR_WIDTH)}  "
            f"{format_text(book.status, STATUS_WIDTH)}"
        )

    print("=" * (TITLE_WIDTH + ISBN_WIDTH + STATUS_WIDTH + AUTHOR_WIDTH + 16))
    print(f"총 {len(books)}권")


def book_list(books: list) -> None:
    if not books:
        print("[ERROR] 등록된 도서가 없습니다.")
        return
    print_book_table(books, "[도서 목록]")


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
        name = prompt_input_valid("이름: ", validator=non_empty)

        if library.has_member(name):
            print("[ERROR] 이미 등록된 회원 입니다.")
            continue
        break

    # 2. 핸드폰 번호: 숫자 11자리
    # 중복 처리는 따로 하지 않음
    phone = prompt_input_valid("핸드폰 번호 (숫자만 입력해주세요): ", validator=phone11)
    library.add_member(Member(name, phone))
    print("\n[INFO] 회원 정보를 등록하였습니다.")


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
        name = prompt_input_valid("회원명: ", validator=non_empty)
        if not library.has_member(name):
            print("[ERROR] 등록되지 않은 회원 입니다.")
            continue
        break
    # ISBN 입력
    while True:
        isbn = prompt_input_valid("도서 ISBN (13자리 숫자만 입력해주세요): ", validator=isbn13)
        try:
            library.borrow_book(name, isbn)
        except (BookNotFoundError, BookAlreadyBorrowedError) as e:
            print(f"[ERROR] {e}")
            continue
        except LibraryError as e: # 메뉴로 돌아감
            print(f"[ERROR] {e}")
            return
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
        name = prompt_input_valid("회원명: ", validator=non_empty)
        if not library.has_member(name):
            print("[ERROR] 등록되지 않은 회원 입니다.")
            continue
        break
    # ISBN 입력
    while True:
        isbn = prompt_input_valid("도서 ISBN (13자리 숫자만 입력해주세요): ", validator=isbn13)
        try:
            overdue_days = library.return_book(name, isbn)
        except (BookNotFoundError, BookNotBorrowedError, BookBorrowedByOtherMemberError) as e:
            print(f"[ERROR] {e}")
            continue
        except LibraryError as e:  # 메뉴로 돌아감
            print(f"[ERROR] {e}")
            return
        print(f"\n[INFO] {name}님이 도서 {isbn}을 반납하였습니다.")
        if overdue_days > 0:
            print(f"[WARNING] 연체 반납입니다. ({overdue_days}일 초과)")
        return


def handle_search_book(library) -> None:
    keyword = prompt_input_valid("검색어를 입력하세요: ", validator=non_empty)
    result = library.search_book(keyword)
    if not result:
        print("\n[INFO] 검색 결과가 없습니다.")
        return
    print_book_table(result, "[검색 결과]")


def dispatch_menu_actions(library, choice: int) -> None:
    if choice == 1:
        register_book(library)
    elif choice == 2:
        book_list(library.book_list())
    elif choice == 3:
        register_member(library)
    elif choice == 4:
        handle_borrow_book(library)
    elif choice == 5:
        handle_return_book(library)
    elif choice == 6:
        handle_search_book(library)
