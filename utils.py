import csv
from models import Book

def print_menu():
    print("\n===== 도서관 관리 시스템 =====")
    print("1. 도서 등록")
    print("2. 도서 목록 출력")
    print("3. 회원 등록")
    print("4. 도서 대출")
    print("5. 도서 반납")
    print("6. 도서 검색")
    print("0. 종료")

def input_number(message):
    while True:
        try:
            return int(input(message))
        except ValueError:
            print("숫자를 입력하세요.")

def load_books_from_csv(filename):
    books = []
    try:
        with open(filename, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                books.append(Book(row["title"], row["author"], row["isbn"]))
    except FileNotFoundError:
        print(f"{filename} 파일이 없습니다.")
    except Exception as e:
        print(f"{filename} 파일 로드 중 오류 발생 : {e}")
    return books
