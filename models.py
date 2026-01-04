class Book:
    def __init__(self,title:str,author:str,isbn:str):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.borrowed_by : str | None = None

    @property
    def is_available(self) -> bool:
        return self.borrowed_by is None

    def __str__(self) -> str:
        status = "[대출가능]" if self.is_available else "[대출중]"
        return f"{status} {self.title} / {self.author} / {self.isbn}"


class Member:
    def __init__(self, member_id: str, name: str, phone: str, password: str, role: str = "member"):
        self.member_id = member_id
        self.name = name
        self.phone = phone
        self.password = password
        self.role = role          # 관리자 / 회원

    def __str__(self) -> str:
        return f"{self.member_id} / {self.name} / {self.phone} / {self.role}"

