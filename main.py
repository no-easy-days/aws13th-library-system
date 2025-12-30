"""
일단 여기서 csv를 읽어
 Book 클래스, Member 클래스, Library 클래스 상속 받아서 하는걸로
 csv는 f로
"""
import csv
from models import Library, Member
from utils import file_load


def main():
    # 1. 도서관 생성 및 초기화
    my_library = Library()
    initial_book = file_load('books.csv')
    for book in initial_book:
        my_library.add_book(book)
        # print(book)               # 일단 Library에 들어는 간다.
    while True:
        print("=== 도서관 관리 시스템 ===")
        print("1. 도서 등록")
        print("2. 도서 목록")
        print("3. 회원 등록")
        print("4. 대출")
        print("5. 반납")
        print("6. 검색")
        print("7. 종료")
        a = int(input("메뉴를 선택하세요 : "))
        if a == 1:
            # 도서 등록 메소드
            title = input("책 제목")
            author = input("저자")
            isbn = input("ISBN")
            my_library.register_book(title,author,isbn)
        elif a == 2:
            # 도서 목록 메소드
            for book in my_library.books:
                print(book)
        # 회원 등록
        elif a == 3:
            name = input("이름 : ")
            phone = input("번호 : ")
            my_library.add_member(name,phone)
        elif a == 4:
            # 대출
            name = input("사용자 이름을 입력하세요 : ")
            isbn = input("대출할 책의 ISBN을 입력하세요 : ")
            my_library.borrow_book(name,isbn)
        elif a == 5:
             # 반납
             name = input("회원 이름 : ")
             isbn = input("ISBN : ")
             my_library.return_book(name,isbn)
        elif a == 6:
             # 검색
             ch = input("책 제목의 일부를 입력하세요 : ")
             my_library.search_book(ch)
        else:
            break



main()









