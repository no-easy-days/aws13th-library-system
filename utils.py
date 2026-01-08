# utils.py
import csv
from models import Book

books = []

with open("books.csv", encoding="utf-8") as f:
    reader = csv.reader(f)
    next(reader)

    for title, author, isbn in reader:
        books.append(Book(title, author, isbn, False))
