from models import Library, Book, Member
from utils import get_valid_input, load_books_from_csv, print_menu, print_separator, validate_int_format
from exception import BookNotFoundException, BookAlreadyBorrowedException, MemberNotFoundException, \
    InvalidInputBasicException, BookNotBorrowedException, UnauthorizedReturnException
import os


def main():
    """홈화면"""

    # 현재 파일의 디렉토리 겸로
    current_dir = os.path.dirname(os.path.abspath(__file__))
    json_path = os.path.join(current_dir, "library_data.json")

    library = Library(data_file=json_path)

    if library.load_data():
        print(f"[System] 저장된 데이터를 불러왔습니다.")
    else:
        # JSON 파일이 없으면 CSV에서 도서 목록만 불러오기
        print("[System] 새로운 도서관 데이터를 생성합니다.")
        print("[System] books.csv 에서 도서 데이터를 불러옵니다.")
        try:
            csv_path = os.path.join(current_dir, "books.csv")
            load_books_from_csv(csv_path, library)
        except FileNotFoundError as e:
            print(f"[경고] {e}")
        except Exception as e:
            print(f"[오류] 파일 로드 중 오류 발생: {e}\n")
    print()

    while True:
        try:
            print_menu()
            user_input = get_valid_input("메뉴를 선택하세요: ")

            try:
                choice = int(user_input)
            except ValueError:
                raise InvalidInputBasicException(" 숫자를 입력해주세요.")

            # 범위 검증
            if choice < 1 or choice > 7:
                raise InvalidInputBasicException(" 1~7 사이의 숫자를 입력해주세요.")

            # switch도 없네;;
            if choice == 1:
                register_book(library)
            elif choice == 2:
                list_books(library)
            elif choice == 3:
                register_member(library)
            elif choice == 4:
                borrow_book(library)
            elif choice == 5:
                return_book(library)
            elif choice == 6:
                search_books(library)
            elif choice == 7:
                print("\n데이터를 저장하고 시스템을 종료합니다...")
                if library.save_data():
                    print("[System] 데이터가 성공적으로 저장되었습니다.")
                print("\n시스템 종료할게요\n")
                break

        except InvalidInputBasicException as e:
            print(f"\n입력 오류: {e}\n")
        except KeyboardInterrupt:
            print("\n\n데이터를 저장하고 시스템을 종료합니다...")
            if library.save_data():
                print("[System] 데이터가 성공적으로 저장되었습니다.")
            print("시스템을 종료한다\n")
            break
        except Exception as e:
            print(f"\n오류오류오류: {e}\n")



def register_book(library):
    """도서 등록 기능입니다.도서 제목, 저자, ISBN을 입력하면 등록됩니다"""
    print("\n[도서 등록]")
    try:
        title = get_valid_input("도서 제목: ")
        author = get_valid_input("저자: ")
        isbn = validate_int_format(get_valid_input("ISBN: "))


        book = Book(title=title, author=author, isbn=isbn)
        library.add_book(book)
    except Exception as e:
        print(f"오류 발생: {e}")


def list_books(library):
    """도서 목록 출력 기능입니다. 등록되 도서 리스트들을 보여줍니다"""
    library.list_all_books()


def register_member(library):
    """회원 등록 기능입니다. 이름이랑 전화번호와 함께 등록합니다."""
    print("\n[회원 등록]")
    try:
        name = get_valid_input("이름: ")
        phone = validate_int_format(get_valid_input("전화번호: "))

        member = Member(name=name, phone=phone)
        library.add_member(member)
    except Exception as e:
        print(f"오류 발생: {e}")


def borrow_book(library):
    """도서 대출 기능을 합니다 사용자 전화번호와 대출할 책의 ISBN을 통해서 대출합니다."""
    print("\n[대출 시스템]")
    try:
        member_phone = get_valid_input("휴대폰번호 입력하세요: ")
        isbn = get_valid_input("대출할 책의 ISBN을 입력하세요: ")

        library.borrow_book(member_phone, isbn)
    except MemberNotFoundException as e:
        print(f"오류: {e}")
    except BookNotFoundException as e:
        print(f"오류: {e}")
    except BookAlreadyBorrowedException as e:
        print(f"오류: {e}")
    except Exception as e:
        print(f"예상치 못한 오류: {e}")


def return_book(library):
    """도서 반납 기능"""
    print("\n[반납 시스템]")
    try:
        member_phone = get_valid_input("휴대폰번호 입력하세요: ")
        isbn = get_valid_input("반납할 책의 ISBN을 입력하세요: ")

        library.return_book(member_phone, isbn)
    except MemberNotFoundException as e:
        print(f"오류: {e}")
    except BookNotFoundException as e:
        print(f"오류: {e}")
    except BookNotBorrowedException as e:
        print(f"오류: {e}")
    except UnauthorizedReturnException as e:
        print(f"오류: {e}")
    except RuntimeError as e:
        print(f"시스템 오류: {e}")
    except Exception as e:
        print(f"예상치 못한 오류: {e}")



def search_books(library):
    """도서 검색 기능"""
    print("\n[도서 검색]")
    try:
        keyword = get_valid_input("검색할 책 제목 (일부분): ")
        results = library.search_books(keyword)

        if results:
            print(f"\n검색 결과 ({len(results)}건):")
            print_separator("-")
            for book in results:
                print(book)
            print()
        else:
            print(f"'{keyword}'에 해당하는 책을 찾을 수 없습니다.\n")
    except Exception as e:
        print(f"오류 발생: {e}")


if __name__ == "__main__":
    main()