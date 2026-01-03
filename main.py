from models import Library
from utils import load_books, get_input

def main():
    # 시스템 초기화 (Library 인스턴스 생성 및 데이터 로드)
    lib = Library()

    # 초기화 프로그램 시작 시 books.csv 로드
    init_data = load_books('books.csv')
    for b in init_data:
        lib.add_book(b.title, b.author, b.isbn, b.is_borrowed)

    print("[System] books.csv 에서 도서 데이터를 불러왔습니다.")

    while True:
        print("\n=== 도서관 관리 시스템 ===")
        print("1. 도서 등록 \n2. 도서 목록 \n3. 회원 등록 \n4. 대출 \n5. 반납 \n6. 검색 \n7. 종료")

        try:
            number = get_input("메뉴를 선택하세요: ")

            if number == '1':
                # TODO: 제목, 저자, ISBN 입력받아 lib.add_book() 호출
                title = get_input("등록할 도서: ")
                author = get_input("저자: ")
                isbn = get_input("ISBN: ")
                lib.add_book(title, author, isbn, False)
                pass
            elif number == '2':
                # TODO: 전체 도서 목록 출력 로직 구현
                print("\n[전체 도서 목록]")
                for book in lib.books:
                    print(book)
                pass
            elif number == '3':
                # TODO: 이름, 전화번호 입력받아 lib.add_member() 호출
                name = get_input("사용자 이름: ")
                phone = get_input("사용자 전화번호: ")
                lib.add_member(name, phone)
                pass
            elif number == '4':
                # TODO: 회원 이름과 ISBN 입력받아 lib.borrow_book() 호출
                name = get_input("사용자 이름: ")
                isbn = get_input("대출할 도서의 ISBN: ")
                lib.borrow_book(name, isbn)
                pass
            elif number == '5':
                # TODO: 회원 이름과 ISBN 입력받아 lib.return_book() 호출
                name = get_input("사용자 이름: ")
                isbn = get_input("대출할 도서의 ISBN: ")
                lib.return_book(name, isbn)
                pass
            elif number == '6':
                # TODO: 검색 키워드 입력받아 lib.search_book() 호출
                keyword = get_input("도서 제목을 입력하세요: ")
                lib.search_book(keyword)
                pass
            elif number == '7':
                print("프로그램을 종료합니다.")
                break
            else:
                print("1~7 사이의 숫자를 입력해주세요.")

        except ValueError as e:
            print(f"입력 오류: \n {e}")
        except KeyError as e:
            print(f"데이터 참조 오류: \n {e}")
        except FileNotFoundError as e:
            print(f"파일을 탐색 오류: \n {e}")
        except LookupError as e:
            print(f"검색어 탐색 오류: \n {e}")
        except RuntimeError as e:
            print(f"실행 오류: \n {e}")
        except Exception as e:
            print(f"예상치 못한 오류 발생! \n {e}")




if __name__ == "__main__":
    main()