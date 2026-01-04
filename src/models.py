from dataclasses import dataclass
from typing import Optional

@dataclass(slots=True)
class Book:
    title: str
    author: str
    isbn: str
    borrowed_by: Optional[str] = None
    is_borrowed: bool = False

    def __str__(self) -> str:
        status = "대출중" if self.is_borrowed else "대출가능"
        return f"{self.title} {self.author} {self.isbn} {status}"

@dataclass(slots=True)
class Member:
    name: str
    phone: str