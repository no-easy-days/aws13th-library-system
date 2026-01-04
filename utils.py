import csv
from models import Book

def load_books_from_csv(path):
    books = []
    with open(path, encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            books.append(
                Book(row["title"], row["author"], row["isbn"])
            )
    return books
