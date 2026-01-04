from models import Book, Member, Library
from utils import csv_to_list, input_non_empty, validate_phone, validate_name
    
# Library 인스턴스 생성 및 예제 사용
library = Library()
# csv 파일에서 책 데이터 불러오기
try:
    init_data = csv_to_list("books.csv")
except FileNotFoundError as e:
    print(f"\n[ERROR] {e}")
    print("프로그램을 종료합니다.")
    exit()
except ValueError as e:
    print(f"\n[ERROR] {e}")
    print("프로그램을 종료합니다.")
    exit()


for row in init_data[1:]:  # 첫 번째 행은 헤더이므로 제외
    book = Book(row[0], row[1], row[2])
    library.add_book(book)
print("\n[System] books.csv 에서 도서 데이터를 불러왔습니다.")

arr = ["도서 등록", "도서 목록", "회원 등록", "대출", "반납", "검색", "종료"]

while True:
    print("\n=== 도서관 관리 시스템 ===")
    for (i, item) in enumerate(arr, start=1):
        print(f"{i}. {item}")
    choice = input("메뉴를 선택하세요: ").strip()
    
    if not choice.isdigit():
        print("\n[ERROR] 숫자를 입력해주세요.")
        input("\n엔터를 누르면 메뉴로 돌아갑니다...")
        continue
    
    if not (1 <= int(choice) <= 7):
        print("\n[ERROR] 1부터 7 사이의 번호를 입력해주세요.")
        input("\n엔터를 누르면 메뉴로 돌아갑니다...")
        continue
        
    if choice == "1":
        # 도서 등록 기능 구현
        title = input_non_empty("\n책 제목을 입력하세요: ", "책 제목은 필수 입력값입니다.")
        author = input_non_empty("책 저자를 입력하세요: ", "책 저자는 필수 입력값입니다.")
        isbn = input_non_empty("책 ISBN을 입력하세요: ", "ISBN은 필수 입력값입니다.")

        new_book = Book(title, author, isbn)
        library.add_book(new_book)
        print("\n[완료] 도서 등록이 완료되었습니다.")
        input("\n엔터를 누르면 메뉴로 돌아갑니다...")
    elif choice == "2":
        # 도서 목록 출력 기능 구현
        print("\n현재 등록된 도서 목록:")
        for book in library.books:
            print(book)
        input("\n엔터를 누르면 메뉴로 돌아갑니다...")
    elif choice == "3":
        # 회원 등록 기능 구현
        name = input_non_empty("\n회원 이름을 입력하세요: ", "회원 이름은 필수 입력값입니다.")
        phone = input_non_empty("회원 전화번호를 입력하세요: ", "회원 전화번호는 필수 입력값입니다.")
        
        try:
            validate_name(name)
            validate_phone(phone)
        except ValueError as e:
            print(f"\n[ERROR] {e}")
            input("\n엔터를 누르면 메뉴로 돌아갑니다...")
            continue
        
        if name in library.members:
            print("\n[ERROR] 이미 등록된 회원입니다.")
            input("\n엔터를 누르면 메뉴로 돌아갑니다...")
            continue
        # TODO:
        """현재 회원 식별자는 name 기준으로 구현됨.
        동명이인 문제를 고려하면 phone을 PK로 사용하는 구조가 더 적절함.
        추후 구조 리팩토링 시 members dict의 key를 phone으로 변경 예정. """
        
        new_member = Member(name, phone, [])
        library.add_member(new_member)
        print("\n[완료] 회원 등록이 완료되었습니다.")
        input("\n엔터를 누르면 메뉴로 돌아갑니다...")
    elif choice == "4":
        # 도서 대출 기능 구현
        member_name = input_non_empty("\n회원 이름을 입력하세요: ", "회원 이름은 필수 입력값입니다.")
        isbn_to_borrow = input_non_empty("대출할 책의 ISBN을 입력하세요: ", "ISBN은 필수 입력값입니다.")

        # 우선 회원 존재 여부 확인 및 도서 존재 여부 확인 및 대출 가능산 상태 확인
        # 회원 존재 여부
        if member_name in library.members:
            member = library.members[member_name]
            # 도서 존재 여부
            book_to_borrow = None
            for book in library.books:
                if book.isbn == isbn_to_borrow:
                    book_to_borrow = book
                    break
            if book_to_borrow:
                # 도서 대출 상태 확인
                if not book_to_borrow.is_borrowed:
                    library.borrow_book(member, book_to_borrow)
                    print(f"\n>> '{member_name}'님이 '{book_to_borrow.title}' ({isbn_to_borrow})을 대출했습니다.")
                else:
                    print("해당 도서는 이미 대출 중입니다.")
            else:
                print("해당 ISBN의 도서를 찾을 수 없습니다.")
        else:
            print("해당 이름의 회원을 찾을 수 없습니다.")
        input("\n엔터를 누르면 메뉴로 돌아갑니다...")
    elif choice == "5":
        # 도서 반납 기능 구현
        member_name = input_non_empty("\n회원 이름을 입력하세요: ", "회원 이름은 필수 입력값입니다.")
        isbn_to_return = input_non_empty("반납할 책의 ISBN을 입력하세요: ", "ISBN은 필수 입력값입니다.")   
        # 우선 회원 존재 여부 확인 및 도서 존재 여부 확인 및 대출 중인지 상태 확인
        if member_name in library.members:
            member = library.members[member_name]
            # 도서 존재 여부
            book_to_return = None
            for book in library.books:
                if book.isbn == isbn_to_return:
                    book_to_return = book
                    break
            if book_to_return:
                # 도서 대출 상태 확인
                if book_to_return.is_borrowed:
                    library.return_book(member, book_to_return)
                    print(f"\n>> '{member_name}'님이 '{book_to_return.title}' ({isbn_to_return})을 반납했습니다.")
                else:
                    print("해당 도서는 대출 중이 아닙니다.")
            else:
                print("해당 ISBN의 도서를 찾을 수 없습니다.")
        else:
            print("해당 이름의 회원을 찾을 수 없습니다.")
        input("\n엔터를 누르면 메뉴로 돌아갑니다...")
    elif choice == "6":
        # 도서 검색 기능 구현
        book_title_section = input_non_empty("\n검색할 책 제목의 일부를 입력하세요: ", "검색어를 입력해주세요.")

        print(f"\n'{book_title_section}'이(가) 포함된 도서 목록:")
        found = False
        for book in library.books:
            if book_title_section in book.title:
                print(book)
                found = True
        if not found:
            print("검색 결과가 없습니다.")
        input("\n엔터를 누르면 메뉴로 돌아갑니다...")
    elif choice == "7":
        print("프로그램을 종료합니다.")
        break
    else:
        print("잘못된 선택입니다. 다시 시도하세요.")