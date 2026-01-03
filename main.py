# from models import *
# import csv
#
# from process_menu_choice import process_menu_choice
#
#
#
# def read_file(filename):
#     books = []
#     try:
#         with open(filename, newline='', encoding='utf-8') as f:
#             reader = csv.reader(f)
#             next(reader)
#             for title, author, isbn in reader:
#                 books.append(Book(title, author, isbn)) # 고민: 이걸 add_book method로 바꾸면 통일성은 있는데 결합도가 높아짐.
#         print("\n[System] books.csv 에서 도서 데이터를 불러왔습니다.")
#         return books
#     except FileNotFoundError:
#         print('File not found')
#         return []
#
# def get_menu_choice():
#     print (
#         "\n=== 도서관 관리 시스템 ===\n"
#         "1. 도서 등록\n"
#         "2. 도서 목록\n"
#         "3. 회원 등록\n"
#         "4. 대출\n"
#         "5. 반납\n"
#         "6. 검색\n"
#         "7. 종료\n"
#     )
#     while True:
#         choice = input("메뉴를 선택하세요: ")
#         try:
#             choice = int(choice)
#         # 문자 입력시 에러
#         except ValueError:
#             print("[ERROR] 1 ~ 7 사이 숫자를 입력하세요.")
#         # 입력한 숫자의 범위가 맞지 않을 때 에러
#         else:
#             if 1 <= choice <= 7:
#                 return choice
#             print("[ERROR] 1 ~ 7 사이 숫자를 입력하세요.")
#
#
def main():
    print("main")
#     # 파일 읽기
#     books = read_file('books.csv')
#     library = Library(books)
#
#     # 선택지 주기
#     while True:
#         choice = get_menu_choice()
#         if choice == 7:
#             break
#         process_menu_choice(library, choice)
#
#
if __name__ == "__main__":
    main()