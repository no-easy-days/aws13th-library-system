# main.py
from library import Library
from console import ConsoleUI
import handlers

def bootstrap_library(lib: Library, ui: ConsoleUI) -> None:
    # 1) 관리자 계정 시드
    lib.seed_admin()
    ui.system("관리자 계정을 준비했습니다. (id=admin)")

    # 2) books.csv 로드는(TODO)
    # lib.load_books_from_csv("books.csv")
    # ui.system("books.csv에서 도서 데이터를 불러왔습니다.")

def run_start_loop(lib: Library, ui: ConsoleUI):
    """로그인 전 화면"""
    while True:
        ui.print_start_menu()
        choice = ui.ask_int("선택: ", min_value=1, max_value=3)

        if choice == 1:
            user = handlers.handle_login(lib, ui)
            if user is not None:
                return user  # 로그인 성공 → main으로 돌아가서 role 분기
        elif choice == 2:
            handlers.handle_signup(lib, ui)
        else:
            return None  # 종료

def run_member_loop(lib: Library, ui: ConsoleUI, user):
    """회원 메뉴"""
    while True:
        ui.print_member_menu()
        choice = ui.ask_int("선택: ", min_value=1, max_value=6)

        if choice == 6:
            ui.system("로그아웃")
            return None

        # TODO: 다음 층에서 구현
        ui.error("아직 구현 전입니다. (다음 단계에서 붙일게요)")

def run_admin_loop(lib: Library, ui: ConsoleUI, user):
    """관리자 메뉴"""
    while True:
        ui.print_admin_menu()
        choice = ui.ask_int("선택: ", min_value=1, max_value=3)

        if choice == 3:
            ui.system("로그아웃")
            return None

        # TODO: 다음 층에서 구현
        ui.error("아직 구현 전입니다. (다음 단계에서 붙일게요)")

def main():
    lib = Library()
    ui = ConsoleUI()
    bootstrap_library(lib, ui)

    current_user = None

    while True:
        if current_user is None:
            current_user = run_start_loop(lib, ui)
            if current_user is None:
                ui.system("프로그램 종료")
                break

        # 로그인 된 상태면 role로 분기
        if current_user.role == "admin":
            current_user = run_admin_loop(lib, ui, current_user)
        else:
            current_user = run_member_loop(lib, ui, current_user)

if __name__ == "__main__":
    main()
