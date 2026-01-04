
from utils import load_books
from models import Book, Member, Library

book_list = load_books()
new_lib = Library(book_list, [])

print("[System] books.csv 에서 도서 데이터를 불러왔습니다.")
print("\n\n=== 도서관 관리 시스템 ===")

while True:

    print("1. 도서 등록")
    print("2. 도서 목록")
    print("3. 회원 등록")
    print("4. 대출")
    print("5. 반납")
    print("6. 검색")
    print("7. 종료")

    sel = input("메뉴를 선택하세요:")
    if sel == "1":
        print("도서 등록")
        print(" 제목을 입력")
        input_title = input("")
        print("저자 입력")
        input_author = input("")
        print("ISBN 입력")
        input_ISBN = input("")

        new_book = Book(input_title, input_author, input_ISBN)
        new_lib.add_book(new_book)



    elif sel == "2":
        print("도서 목록")
        for find_book in new_lib.books:
            print(find_book)


    elif sel == "3":
        print("회원 등록")
        print(" 이름을 입력")
        input_name = input("")
        print("핸드폰 번호 입력")
        input_phone = input("")
        new_member = Member(input_name, input_phone)
        new_lib.add_member(new_member)
        print("회원 등록 완료")


    elif sel == "4":
        print("[대출 시스템]")
        print("대출할 책의 ISBN을 입력하세요: ")
        input_ISBN = input("")
        print("사용자 이름을 입력하세요: ")
        input_name = input("")
        new_borrow_book = new_lib.borrow_book(input_ISBN, input_name)



    elif sel == "5":
        print("반납")
        print("반납할 책 ISBN 입력 :")
        input_ISBN = input("")
        print("반납할 사용자 이름 입력:")
        input_name = input("")
        new_return = new_lib.return_book(input_ISBN, input_name)

    elif sel == "6":
        print("검색")
        search = input("")
        for search_title in new_lib.books:
            if search in search_title.title:
                print(search_title)


    elif sel == "7":
        print("종료")
        break









