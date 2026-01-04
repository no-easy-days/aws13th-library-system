import csv
from typing import Callable, Optional

from src.models import Book
from src.exception import DataLoadError

# 에러메세지 or 정상이면 None
Validator = Callable[[str], Optional[str]]

def prompt_input_valid(prompt: str, *, validator: Validator) -> str:
    while True:
        value = input(prompt).strip()
        error = validator(value)
        if error is None:
            return value
        print(f"[ERROR] {error}")

def non_empty(value: str) -> Optional[str]:
    if not value:
        return "값은 비어 있을 수 없습니다."
    return None

def isbn13(isbn: str) -> Optional[str]:
    if not isbn:
        return "ISBN을 입력해주세요."
    if not isbn.isdigit():
        return "ISBN은 숫자만 입력해주세요."
    if len(isbn) != 13:
        return "ISBN은 13자리 숫자여야 합니다."
    return None

def phone11(phone: str) -> Optional[str]:
    if not phone:
        return "핸드폰 번호를 입력해주세요."
    if not phone.isdigit():
        return "숫자만 입력해주세요."
    if len(phone) != 11:
        return "숫자 11자리를 입력해주세요."
    return None


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
    except FileNotFoundError as e:
        raise DataLoadError() from e
    else:
        return count