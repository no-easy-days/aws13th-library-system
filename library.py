import re
from os import name

from models import Member, Book
from exceptions import ValidationError, DuplicateError, AuthenticationError

class Library:
    def __init__(self):
        self.members:dict[str,Member] = {}
        self.books:dict[str,Book] = {}
        self.requets:list[object] = [] #나중에 바꿔야함

    def _normalize_phone(self,phone:str) -> str:
        """
            입력 예:
                - 01012345678
                - 010 1234 5678
                - 010 1234 5678
            저장 형식:
                - 010-1234-5678
        """
        digits = re.sub(r'\D','',phone)
        if len(digits) != 11 or not digits.startswith("010"):
            raise ValidationError("전화번호는 010-0000-0000 형식(총 11자리)이어야 합니다.")

        mid = digits[3:7]
        last = digits[7:11]
        return f"010-{mid}-{last}"

    def _validate_password(self,password:str) -> None:
        if not (4 <= len(password) <= 13):
            raise ValidationError("비밀번호는 4자리 이상 13자리 이하로 입력하세요.")

    def seed_admin(self) -> None:#프로그램 시작시 1회 호출해서 관리자 계정 만들기
        admin_id = "admin"
        if admin_id in self.members:
            return
        self.members[admin_id] = Member(
            member_id="admin",
            name = "백시관",
            phone = "010-1234-5678",
            password = "1234567890",
            role = "admin"
        )

    def register_member(self,member_id: str, name: str, phone: str, password: str) -> Member:
        member_id = member_id.strip()
        name = name.strip()

        if member_id == "":
            raise ValidationError("회원 아이디는 비어있을 수 없습니다.")
        if name == "":
            raise ValidationError("이름은 비어있을 수 없습니다.")
        if member_id in self.members:
            raise ValidationError("이미 존재하는 회원 아이디입니다.")

        nomalized_phone = self._normalize_phone(phone)
        self._validate_password(password)

        m = Member(member_id=member_id, name=name, phone=nomalized_phone, password=password,role="member")
        self.members[member_id] = m
        return m

    def login(self,member_id:str,password:str) -> Member:
        member_id = member_id.strip()
        if member_id not in self.members:
            raise AuthenticationError("존재하지 않는 아이디입니다")

        m=self.members[member_id]
        if m.password != password:
            raise AuthenticationError("비밀번호가 일치하지 않습니다.")
        return m