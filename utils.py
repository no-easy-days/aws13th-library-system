import csv
from models import Book


def load_books():
    books = []

    try:
        with open('books.csv', 'r', encoding='utf-8') as f:
            reader = csv.reader(f)

            for row in reader:
                if len(row) < 3:
                    continue

                new_book = Book(row[0], row[1], row[2])
                books.append(new_book)

    except FileNotFoundError:
        print("파일이 없습니다.")

    return books