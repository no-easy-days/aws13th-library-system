
class LibraryError(Exception):
    pass

class DataLoadError(LibraryError):
    def __init__(self):
        super().__init__("파일을 찾을 수 없습니다.")

class DuplicateISBNError(LibraryError):
    def __init__(self, isbn: str):
        super().__init__(f"이미 등록된 도서 입니다: {isbn}")

