import os
import models
import csv

def main():
    #Book, Member, Library 클래스 가져오기
    library = models.Library()

    """
    1. 초기화(자동수행)
    프로그램 시작 시 books.csv 파일을 읽어 Library에 도서들을 저장
    혹시나 books.csv 파일이 없거나 불러오지 못하면 예외 처리 발생
    """
    source_path = os.getcwd()
    csv_file = os.path.join(source_path, "books.csv")
    if not os.path.isfile(csv_file):
        raise FileNotFoundError("books.csv 파일이 없습니다.")
    else:
        with open(csv_file, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                library.add_book(row['title'], row['author'], row['isbn'])
    print(f"[System] books.csv 에서 도서 데이터를 불러왔습니다.")

    """
    while 반복문을 활용하여 메뉴가 반복되어 출력되어야 함
    """
    while True:
        print(f"=== 도서관 관리 시스템 ===")
        print(f"1. 도서 등록")
        print(f"2. 도서 목록")
        print(f"3. 회원 등록")
        print(f"4. 대출")
        print(f"5. 반납")
        print(f"6. 검색")
        print(f"7. 종료")

        number_input = input("메뉴를 선택하세요 : ")
        try:
            menu = int(number_input)
            if 1 <= menu <= 7:
                if menu == 1:
        #           도서 등록 모듈 불러오기
                    print(f"1. 도서 등록")
                    title = input("책 제목을 입력하세요 : ")
                    author = input("책 저자명을 입력하세요 : ")
                    isbn = input("책의 isbn번호를 입력하세요 : ")
                    library.add_book(title, author, isbn)
                elif menu == 2:
                    print(f"2. 도서 목록")
        #           도서 목록 모듈 불러오기
                    print(f"---등록된 책 정보 리스트---")
                    library.print_books()
                elif menu == 3:
                    print(f"3. 회원 등록")
                    name = input("등록할 회원명을 입력하세요 : ")
                    phone = input("등록할 휴대폰번호를 입력하세요 : ")
        #           회원 등록 모듈 불러오기
                    library.add_member(name, phone)
                elif menu == 4:
                    print(f"4. 대출")
                    borrow_name = input("회원 이름을 입력하세요 : ")
                    borrow_isbn = input("대출할 도서의 isbn번호를 입력하세요 : ")
        #           대출 모듈 불러오기
                    library.borrow_book(borrow_name, borrow_isbn)
                elif menu == 5:
                    print(f"5. 반납")
                    return_name = input("회원 이름을 입력하세요 : ")
                    return_isbn = input("반납할 도서의 isbn번호를 입력하세요 : ")
        #           반납 모듈 불러오기
                    library.return_book(return_name, return_isbn)
                elif menu == 6:
                    print(f"6. 검색")
                    kw_title = input("검색할 키워드를 입력하세요 : ")
        #           검색 모듈 불러오기
                    library.find_books(kw_title)
                elif menu == 7:
                    print(f"7. 종료")
        #           반복문 종료
                    break
            else:
                raise ValueError
        except ValueError:
            print(f"잘못 입력했습니다. 1~7까지의 정수를 입력하세요.")

if __name__ == '__main__':
    try:
        main()
    finally:
        print(f"프로그램이 종료 처리 됩니다.")