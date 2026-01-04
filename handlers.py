from exceptions import DomainError
from models import Member

def handle_signup(lib, ui) -> None:
    ui.system("[회원가입]")
    member_id = ui.ask_str("아이디(member_id): ")
    name = ui.ask_str("이름: ")
    phone = ui.ask_str("전화번호(010-0000-0000 또는 숫자만): ")
    password = ui.ask_str("비밀번호(4~13자리): ")

    try:
        m = lib.register_member(member_id, name, phone, password)
        ui.success(f"{m.member_id} 가입 완료")
    except DomainError as e:
        ui.error(str(e))


def handle_login(lib, ui) -> Member | None:
    ui.system("[로그인]")
    member_id = ui.ask_str("아이디(member_id): ")
    password = ui.ask_str("비밀번호: ")

    try:
        m = lib.login(member_id, password)
        ui.success(f"{m.name}님 로그인 성공 ({m.role})")
        return m
    except DomainError as e:
        ui.error(str(e))
        return None
