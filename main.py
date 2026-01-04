from models import Library, Book, Member
from models import BookNotFoundError, MemberNotFoundError
from models import BookAlreadyBorrowedError, BookNotBorrowedError
from utils import load_books_from_csv, get_valid_input


def display_menu():
    # 메뉴 출력
    print("\n=== 도서관 관리 시스템 ===")
    print("1. 도서 등록")
    print("2. 도서 목록")
    print("3. 회원 등록")
    print("4. 대출")
    print("5. 반납")
    print("6. 검색")
    print("7. 종료")


def register_book(library):
    # 도서 등록 기능
    print("\n[도서 등록]")
    title = input("책 제목을 입력하세요: ")
    author = input("저자를 입력하세요: ")
    isbn = input("ISBN을 입력하세요: ")
    
    book = Book(title, author, isbn)
    library.add_book(book)
    print(f">> '{title}' 책이 등록되었습니다.")


def show_all_books(library):
    # 도서 목록 출력 기능
    library.display_all_books()


def register_member(library):
    # 회원 등록 기능
    print("\n[회원 등록]")
    name = input("회원 이름을 입력하세요: ")
    
    # 이미 등록된 회원인지 확인
    if library.find_member_by_name(name):
        print(f">> '{name}'님은 이미 등록된 회원입니다.")
        return
    
    phone = input("전화번호를 입력하세요: ")
    
    member = Member(name, phone)
    library.add_member(member)
    print(f">> '{name}'님이 회원으로 등록되었습니다.")


def borrow_book(library):
    # 도서 대출 기능
    print("\n[대출 시스템]")
    member_name = input("사용자 이름을 입력하세요: ")
    isbn = input("대출할 책의 ISBN을 입력하세요: ")
    
    try:
        book = library.borrow_book(member_name, isbn)
        print(f">> '{member_name}'님이 '{book.title}' ({isbn})을 대출했습니다.")
    
    except MemberNotFoundError as e:
        print(f"[오류] {e}")
    
    except BookNotFoundError as e:
        print(f"[오류] {e}")
    
    except BookAlreadyBorrowedError as e:
        print(f"[오류] {e}")


def return_book(library):
    # 도서 반납 기능
    print("\n[반납 시스템]")
    member_name = input("사용자 이름을 입력하세요: ")
    isbn = input("반납할 책의 ISBN을 입력하세요: ")
    
    try:
        book = library.return_book(member_name, isbn)
        print(f">> '{member_name}'님이 '{book.title}' ({isbn})을 반납했습니다.")
    
    except MemberNotFoundError as e:
        print(f"[오류] {e}")
    
    except BookNotFoundError as e:
        print(f"[오류] {e}")
    
    except BookNotBorrowedError as e:
        print(f"[오류] {e}")


def search_books(library):
    # 도서 검색 기능
    print("\n[도서 검색]")
    keyword = input("검색할 책 제목을 입력하세요: ")
    
    results = library.search_books(keyword)
    
    if not results:
        print(f"'{keyword}'에 해당하는 책을 찾을 수 없습니다.")
        return
    
    print(f"\n검색 결과 ({len(results)}권):")
    for i, book in enumerate(results, 1):
        print(f"{i}. {book}")

# 메인 함수
def main():
    # 1. 도서관 객체 생성
    library = Library()
    
    # 2. books.csv 파일에서 초기 도서 데이터 로드
    print("[System] books.csv 에서 도서 데이터를 불러오는 중입니다.")
    books = load_books_from_csv('books.csv')
    
    for book in books:
        library.add_book(book)
    
    if books:
        print(f"[System] {len(books)}권의 도서 데이터를 불러왔습니다.")
    else:
        print("[System] 불러온 도서 데이터가 없습니다.")
    
    # 3. 반복
    while True:
        display_menu()
        
        # 메뉴 선택
        # 잘못된 메뉴 처리 
        choice = get_valid_input("메뉴를 선택하세요: ", int)
        
        if choice == 1:
            register_book(library)
        
        elif choice == 2:
            show_all_books(library)
        
        elif choice == 3:
            register_member(library)
        
        elif choice == 4:
            borrow_book(library)
        
        elif choice == 5:
            return_book(library)
        
        elif choice == 6:
            search_books(library)
        
        elif choice == 7:
            print("\n프로그램을 종료합니다. 감사합니다!")
            break
        
        else:
            print("[오류] 1~7 사이의 숫자를 입력해주세요.")


if __name__ == "__main__":
    main()