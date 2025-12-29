from models import *
import csv


def read_file(filename):
    books = []
    try:
        with open(filename, newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            next(reader)
            for title, author, isbn in reader:
                books.append(Book(title, author, isbn))
        return books
    except FileNotFoundError:
        print('File not found')
        return []


def main():
    # 파일 읽기
    books = read_file('books.csv')
    # for book in books[:3]:
    #     print(book)

    # 선택지 주기
    # 선택지 별 기능 구현



if __name__ == "__main__":
    main()