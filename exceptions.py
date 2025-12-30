
class LibraryError(Exception):
    pass

class BookNotFoundError(LibraryError):
    pass

class BookAlreadyBorrowedError(LibraryError):
    pass

class MemberNotFoundError(LibraryError):
    pass
