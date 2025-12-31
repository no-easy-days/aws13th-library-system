import csv

from exception import InvalidInputBasicException
from models import Book


def get_valid_input(prompt):
    """사용자로부터 비어있지 않은 입력을 받습니다."""
    while True:
        user_input = input(prompt).strip()
        if user_input:
            return user_input
        print("입력값이 비어있습니다. 다시 입력해주세요.")


def load_books_from_csv(filename, library):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            csv_reader = csv.DictReader(file)

            # CSV 헤더 검증
            required_fields = {'title', 'author', 'isbn'}
            if not required_fields.issubset(csv_reader.fieldnames or []):
                raise ValueError(
                    "부적절한 CSV;;"
                )

            for row in csv_reader:
                book = Book(
                    title=row['title'].strip(),
                    author=row['author'].strip(),
                    isbn=row['isbn'].strip()
                )
                library.books[book.isbn] = book

        return

    except FileNotFoundError:
        raise FileNotFoundError(f"'{filename}' 파일을 찾을 수 없습니다.")
    except KeyError as e:
        raise ValueError(f"CSV 파일 형식 오류: {e}")



def print_separator(char="=", length=40):
    """클린코드인척 하기 위한 구분선 함수"""
    print(char * length)



def print_menu():
    """메인 메뉴 출력"""
    print("=== 도서관 관리 시스템 ===")
    print("1. 도서 등록")
    print("2. 도서 목록")
    print("3. 회원 등록")
    print("4. 대출")
    print("5. 반납")
    print("6. 검색")
    print("7. 종료")


def validate_int_format(blah: str) -> str:
    if not blah.isdigit():
        raise InvalidInputBasicException("숫자를 입력해라")
    return blah