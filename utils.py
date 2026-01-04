"""
여기서 csv를 읽어

"""
import csv
from models import Book


def file_load(filename):
    book_list = []
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            next(reader)  # 헤더 건너뛰기
            for row in reader:
                if len(row) < 3:
                    continue
                title, author, isbn = row
                book = Book(title, author, isbn)
                book_list.append(book)
        print(f"[System] {filename} 에서 도서 데이터를 불러왔습니다.")  # 메시지 약간 수정
    except FileNotFoundError:
        print(f"[오류] {filename} 파일이 없습니다!")
    return book_list




