class ConsoleUI:
    def system(self, msg: str) -> None:
        print(f"[System] {msg}")

    def success(self, msg: str) -> None:
        print(f">> {msg}")

    def error(self, msg: str) -> None:
        print(f"[Error] {msg}")

    def print_start_menu(self) -> None:
        print("\n=== 시작 ===")
        print("1. 로그인")
        print("2. 회원가입")
        print("3. 종료")

    def print_member_menu(self) -> None:
        print("\n=== 회원 도서 관리 ===")
        print("1. 도서 검색")
        print("2. 대출")
        print("3. 내 대출 확인")
        print("4. 반납")
        print("5. 도서 등록 요청")
        print("6. 로그아웃")

    def print_admin_menu(self) -> None:
        print("\n=== 관리자 도서 관리 ===")
        print("1. 등록 요청 승인(도서 등록)")
        print("2. 현재 대출 목록")
        print("3. 로그아웃")

    def ask_int(self, prompt: str, *, min_value: int | None = None, max_value: int | None = None) -> int:
        while True:
            raw = input(prompt).strip()
            try:
                value = int(raw)
            except ValueError:
                self.error("숫자를 입력하세요.")
                continue

            if min_value is not None and value < min_value:
                self.error(f"{min_value} 이상을 입력해 주세요.")
                continue
            if max_value is not None and value > max_value:
                self.error(f"{max_value} 이하를 입력하세요.")
                continue

            return value

    def ask_str(self, prompt: str, *, allow_empty: bool = False) -> str:
        while True:
            text = input(prompt).strip()
            if not allow_empty and text == "":
                self.error("빈 값은 입력할 수 없습니다.")
                continue
            return text
