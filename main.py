from models import *
import csv


def read_file(filename):
    # TODO: 같은 책 들어왔을 때 처리 필요
    books = []
    try:
        with open(filename, newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            next(reader)
            for title, author, isbn in reader:
                books.append(Book(title, author, isbn))
        print("\n[System] books.csv 에서 도서 데이터를 불러왔습니다.")
        return books
    except FileNotFoundError:
        print('File not found')
        return []

def start_program():
    print (
        "\n=== 도서관 관리 시스템 ===\n"
        "1. 도서 등록\n"
        "2. 도서 목록\n"
        "3. 회원 등록\n"
        "4. 대출\n"
        "5. 반납\n"
        "6. 검색\n"
        "7. 종료\n"
    )
    while True:
        choice = input("메뉴를 선택하세요: ")
        try:
            choice = int(choice)
        except ValueError:
            print("1 ~ 7 사이 숫자를 입력하세요.")
        else:
            if 1 <= choice <= 7:
                return choice
            print("1 ~ 7 사이 숫자를 입력하세요.")



def main():
    # 파일 읽기
    books = read_file('books.csv')
    # for book in books[:3]:
    #     print(book)

    # 선택지 주기
    start_program()
    # print(f"선택지: {start_program()}")


    # 선택지 별 기능 구현



if __name__ == "__main__":
    main()