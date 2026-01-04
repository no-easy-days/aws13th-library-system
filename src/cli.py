# 메뉴 + 실행 흐름 담당

from src.exception import LibraryError
from src.library import Library
from src.utils import load_books
from src.menu_actions import dispatch_menu_actions


def get_menu_choice() -> int:
    """
    사용자에게 기능 목록 제공

    :return: 사용자가 선택한 기능 번호
    """
    print (
        "\n=== 도서관 관리 시스템 ===\n"
        "1. 도서 등록\n"
        "2. 도서 목록\n"
        "3. 회원 등록\n"
        "4. 대출\n"
        "5. 반납\n"
        "6. 검색\n"
        "7. 종료\n"
    )
    while True:
        choice = input("메뉴를 선택하세요: ").strip()
        try:
            choice = int(choice)
        # 문자 입력시 에러
        except ValueError:
            print("[ERROR] 1 ~ 7 사이 숫자를 입력하세요.")
            continue
        # 입력한 숫자의 범위가 맞지 않을 때 에러
        if 1 <= choice <= 7:
            return choice
        print("[ERROR] 1 ~ 7 사이 숫자를 입력하세요.")

def run():
    library = Library()

    # 파일 읽어오기
    try:
        count = load_books(library, "../data/books.csv")
    except LibraryError as e:
        print(f"[ERROR] {e}")
        return
    print(f"\n[System] books.csv 에서 도서 데이터를 불러왔습니다. (총 {count}권)")

    # 기능 선택지 제공
    while True:
        choice = get_menu_choice()
        if choice == 7:
            break
        dispatch_menu_actions(library, choice)
