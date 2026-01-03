
class LibraryError(Exception):
    pass

class DataLoadError(LibraryError):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class DuplicateISBNError(LibraryError):
    def __init__(self, isbn):
        super().__init__(f"이미 등록된 도서 입니다: {isbn}")

