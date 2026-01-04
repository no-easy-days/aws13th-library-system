# main.py
from library import Library
from console import ConsoleUI
from storage import Storage
import handlers

def bootstrap_library(lib: Library, ui: ConsoleUI, storage: Storage) -> None:
    # 1) 저장된 상태 복원 시도
    if storage.load_state(lib):
        ui.system("저장된 데이터를 복원했습니다.")
    else:
        # 2) 관리자 계정 시드
        lib.seed_admin()
        ui.system("관리자 계정을 준비했습니다. (id=admin)")

        # 3) books.csv 로드
        lib.load_books_from_csv("books.csv")
        ui.system("books.csv에서 도서 데이터를 불러왔습니다.")

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
        choice = ui.ask_int("선택: ", min_value=1, max_value=7)

        if choice == 1:
            handlers.handle_book_list(lib, ui)
        elif choice == 2:
            handlers.handle_book_search(lib, ui)
        elif choice == 3:
            handlers.handle_book_borrow(lib, ui, user)
        elif choice == 4:
            handlers.handle_my_loans(lib, ui, user)
        elif choice == 5:
            handlers.handle_book_return(lib, ui, user)
        elif choice == 6:
            handlers.handle_book_request(lib, ui, user)
        elif choice == 7:
            ui.system("로그아웃")
            return None

def run_admin_loop(lib: Library, ui: ConsoleUI, user):
    """관리자 메뉴"""
    while True:
        ui.print_admin_menu()
        choice = ui.ask_int("선택: ", min_value=1, max_value=8)

        if choice == 1:
            handlers.handle_register_book(lib, ui)
        elif choice == 2:
            handlers.handle_book_list(lib, ui)
        elif choice == 3:
            handlers.handle_book_search(lib, ui)
        elif choice == 4:
            handlers.handle_view_all_loans(lib, ui)
        elif choice == 5:
            handlers.handle_view_requests(lib, ui)
        elif choice == 6:
            handlers.handle_approve_request(lib, ui)
        elif choice == 7:
            handlers.handle_reject_request(lib, ui)
        elif choice == 8:
            ui.system("로그아웃")
            return None

def main():
    lib = Library()
    ui = ConsoleUI()
    storage = Storage()
    bootstrap_library(lib, ui, storage)

    current_user = None

    try:
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
    finally:
        # 프로그램 종료 시 상태 저장
        storage.save_state(lib)
        ui.system("데이터를 저장했습니다.")

if __name__ == "__main__":
    main()
