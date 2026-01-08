#isbn이 잘못되었을 때 발생하는 사용자 정의 예외
class LibraryError(Exception):
    """도서관 시스템 기본 예외 클래스"""
    pass

class InvalidISBNError(LibraryError):
    """ISBN 형식이 잘못되었을 때 발생"""
    pass

class DuplicateDataError(LibraryError):
    """이미 존재하는 책이나 회원일 때 발생"""
    pass

class LoanError(LibraryError):
    """대출/반납이 불가능한 상황일 때 발생"""
    pass

