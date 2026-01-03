
class LibraryError(Exception):
    pass

class DataLoadError(LibraryError):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)




