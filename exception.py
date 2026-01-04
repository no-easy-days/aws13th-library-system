class LibraryError(Exception):
    pass
class MemberNotFoundError(LibraryError):
    pass
class BookNotBorrowedError(LibraryError):
    pass
class BookNotFoundError(LibraryError):
    pass