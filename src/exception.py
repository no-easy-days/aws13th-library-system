class LibraryError(Exception):
    """ 예외처리 최상위 클래스 """
    pass

class DataLoadError(LibraryError):
    def __init__(self):
        super().__init__("파일을 찾을 수 없습니다.")

# ==== 도서 관련 ====
class DuplicateISBNError(LibraryError):
    def __init__(self, isbn: str):
        super().__init__(f"이미 등록된 도서 입니다: {isbn}")

class BookNotFoundError(LibraryError):
    def __init__(self, isbn: str):
        super().__init__(f"존재 하지 않는 책 입니다: {isbn}")

class BookAlreadyBorrowedError(LibraryError):
    def __init__(self, isbn: str):
        super().__init__(f"이미 대출 중인 도서입니다: {isbn}")

class BookNotBorrowedError(LibraryError):
    def __init__(self, isbn: str):
        super().__init__(f"대출 중인 도서가 아닙니다: {isbn}")

class BookBorrowedByOtherMemberError(LibraryError):
    def __init__(self, isbn: str):
        super().__init__(f"해당 도서는 다른 회원이 대출 중입니다: {isbn}")

# ==== 회원 관련 ====
class DuplicateMemberError(LibraryError):
    def __init__(self, name: str):
        super().__init__(f"이미 등록된 회원 입니다: {name}")

class MemberNotFoundError(LibraryError):
    def __init__(self, name: str):
        super().__init__(f"등록 되지 않은 회원 입니다: {name}")