import csv
from models import Book


def load_books(file_path):
    books = []
    with open(file_path, mode='r', encoding='utf-8') as f:
        # DictReader를 사용하여 헤더 기반으로 안전하게 읽기
        reader = csv.DictReader(f)
        for row in reader:
            try:
                # 데이터 양끝 공백 제거(strip)로 입력 오류 방지
                books.append(Book(
                    row['title'].strip(),
                    row['author'].strip(),
                    row['isbn'].strip()
                ))
            except FileNotFoundError:
                #헤더명 틀렸을 발생하는 내장 에러
                raise KeyError("CSV 헤더 형식이 올바르지 않습니.")
    return books


def get_input(prompt):
    value = input(prompt).strip()
    if not value:
        raise ValueError("입력 값이 비어있습니다. 내용을 입력해주세요.")
    return value