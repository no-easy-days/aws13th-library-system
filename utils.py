import csv

from models import Book
from exception import DataLoadError


def load_books(library, filename: str) -> int:
    """
    프로그램 첫 실행 시 csv파일 읽어 library에 도서 등록
    :param library:
    :param filename: 읽을 파일 이름
    :return: 로드된 도서 수
    :raises DataLoadError: 파일 접근 실패 시
    """
    try:
        with open(filename, newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            next(reader)
            count = 0
            for title, author, isbn in reader:
                library.add_book(Book(title, author, isbn))
                count += 1
        return count
    except FileNotFoundError as e:
        raise DataLoadError("파일을 찾을 수 없습니다.") from e