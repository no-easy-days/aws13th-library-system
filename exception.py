class LibraryBasicException(Exception):
    """도서관 시스템 기본 예외 클래스"""
    pass


class BookNotFoundException(LibraryBasicException):
    """책을 찾을 수 없을 때 발생하는 예외"""
    def __init__(self, isbn):
        self.isbn = isbn
        super().__init__(f"ISBN '{isbn}'에 해당하는 책이 없어요.")

class BookAlreadyBorrowedException(LibraryBasicException):
    """이미 대출 중인 책을 대출하려 할 때 발생하는 예외"""
    def __init__(self, title, borrowed_by):
        self.title = title
        self.borrowed_by = borrowed_by
        super().__init__(
            f"'{title}' 책은 이미 대출 중입니다. (대출자: {borrowed_by})"
        )


class MemberNotFoundException(LibraryBasicException):
    """회원을 찾을 수 없을 때 발생하는 예외"""
    def __init__(self, phone):
        self.phone = phone
        super().__init__(f"전화번호 '{phone}'로 등록된 회원을 찾을 수 없습니다.")


class BookNotBorrowedException(LibraryBasicException):
    """대출 중이 아닌 책을 반납하려 할 때 발생하는 예외"""
    def __init__(self, title):
        self.title = title
        super().__init__(f"'{title}' 책은 대출 중이 아닙니다.")


class UnauthorizedReturnException(LibraryBasicException):
    """다른 사람이 대출한 책을 반납하려 할 때 발생하는 예외"""
    def __init__(self, title, borrower_phone, returner_phone):
        self.title = title
        self.borrower_phone = borrower_phone
        self.returner_phone = returner_phone
        super().__init__(
            f"'{title}' 책은 본인({returner_phone})이 대출한 책이 아닙니다. "
            f"(대출자: {borrower_phone})"
        )


class DataInconsistencyException(LibraryBasicException):
    """Book과 Member 간 데이터 불일치가 발생했을 때의 예외"""
    def __init__(self, book_title, member_phone):
        self.book_title = book_title
        self.member_phone = member_phone
        super().__init__(
            f"데이터 불일치 감지: '{book_title}' 책이 회원({member_phone})의 대출 목록에 없습니다. "
            f"시스템 관리자에게 문의하세요."
        )


class InvalidInputBasicException(LibraryBasicException):
    """잘못된 입력이 들어왔을 때 발생하는 예외"""
    def __init__(self, message="잘못된 입력입니다."):
        super().__init__(message)
