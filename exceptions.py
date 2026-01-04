class DomainError(Exception):
    """도메인(업무 규칙)"""


class ValidationError(DomainError):
    """입력 값 형식/규칙 위반"""


class DuplicateError(DomainError):
    """중복"""


class AuthenticationError(DomainError):
    """로그인 실패(인증 실패)"""


class NotFoundError(DomainError):
    """리소스를 찾을 수 없음"""


class AlreadyBorrowedError(DomainError):
    """이미 대출중인 도서"""


class UnauthorizedError(DomainError):
    """권한 없음"""
