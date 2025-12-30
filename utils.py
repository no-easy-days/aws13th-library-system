
import csv
from models import Book

def load_books_from_csv(path):
    books = []
    with open(path,newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        for title, author, isbn in reader:
            books.append(Book(title, author, isbn))
    return books
