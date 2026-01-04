from datetime import datetime, timedelta
from models import Book, Member, Library, Loan
import utils

# Library 구현 시스템 구현을 위한 library 객체 생성, csv파일 목록 초기화
my_library = Library()

print("[SYSTEM] member.csv에서 도서관의 회원 목록을 구성합니다 ")
member_file_path = "member.csv"
my_library.set_member(member_file_path)

print("[SYSTEM] book.csv에서 도서관의 장서 목록을 구성합니다.")
book_file_path = "books.csv"
my_library.set_book(book_file_path)

print("[SYSTEM] loans.csv에서 도서관의 대출 목록을 구성합니다.")
loan_file_path = "loans.csv"
my_library.set_loan(loan_file_path)

print("[SYSTEM] 도서관의 목록이 갱신되었습니다..")


# 프로그램의 동작 while문 사용하여 매뉴 선택
while True:
    try:
      print('=======================================================')
      print('1. 도서 등록')
      print('2. 도서 목록')
      print('3. 회원 등록')
      print('4. 도서 대출')
      print('5. 도서 반납')
      print('6. 도서 검색')
      print('7. 프로그램 종료')

      userInput = int(input("메뉴를 선택하세요 : "))

      # 도서 등록 매뉴 유저입력값으로, book 객체 생성, library 객체에 저장
      if userInput== 1:
          print("도서등록 매뉴입니다. 도서를 등록하기 위해서는 도서의 이름, 저자, ISBN이 필요합니다.")
          book_title = input("도서의 이름을 입력해 주세요 : ")
          book_author = input("도서의 저자를 입력해 주세요 : ")

          while True:
              book_isbn = input("도서의 ISBN을 입력해 주세요(반드시 13자리 숫자여야 합니다) : ")
              try:
                  my_book = Book(book_title, book_author, book_isbn)
                  print(f"{my_book.title}: 도서의 이름 입니다. {my_book.author}: 도서의 저자입니다. {my_book.isbn} 도서의 isbn 입니다")
                  my_library.add_book(my_book)
                  print("도서가 성공적으로 등록되었습니다.")
                  print("[SYSTEM] 도서관 books.csv 목록이 갱신되었습니다..")
                  break
              except utils.InvalidISBNError as e :
                  print(e)

      # 도서 출력 매뉴, library 객체에 저장되어있는 book객체의 값을 모두 출력
      elif int(userInput)== 2:
          print("도서 출력 메뉴 입니다. 도서관에 소장하고 있는 모든 목록을 불러옵니다.")
          print(f"도서관 file_path - {my_library.book_file_path}")
          my_library.show_library()

     # 회원 등록 매뉴, member 객체생성
      elif userInput== 3:
          print("회원 등록 매뉴입니다. 회원 이름과, 전화 번호를 입력하세요")
          name = input("회원 이름을 입력하세요 : ")
          phone = input("회원 전화번호를 입력하세요 : ")

          my_member = Member(name, phone)
          if my_library.add_member(my_member):
            print("회원 정보가 성공적으로 등록되었습니다.")

      elif userInput== 4:
          print("도서 대출 매뉴입니다, 책을 대출하려면 회원이름과, 대출할 책의 isbn을 입력해 주세요")
          member_name = input("회원의 이름을 입력하세요 : ")
          book_isbn = input("대출할 책의 isbn을 입력하세요 :")

          # 회원 찾기
          member = next((m for m in my_library.library_members if m.name == member_name), None)
          if not member:
              print("[SYSTEM] 해당 회원이 존재하지 않습니다.")
              continue

          # 책 찾기
          book = next((b for b in my_library.library_book if b.isbn == book_isbn), None)
          if not book:
              print("[SYSTEM] 해당 ISBN의 책이 존재하지 않습니다.")
              continue

          # 대출 상태 확인
          if book.is_loaned:
              print("[SYSTEM] 이미 대출 중인 책입니다.")
          else:
              book.is_loaned = True
              book.loan_date = datetime.now()
              book.due_date = book.loan_date + timedelta(days=7)
              member.add_book(book)

              # Loan 객체 생성 후 추가
              loan = Loan(member.name, book.isbn)
              my_library.add_loan(loan)

              print(f"[SYSTEM] {member.name}님이 '{book.title}'을 대출했습니다. 반납 예정일: {loan.due_date.strftime('%Y-%m-%d')}")

      elif userInput== 5:
          print("도서 반납 매뉴입니다, 책을 반납하려면 회원이름과, 반납할 책의 isbn을 입력해 주세요")
          member_name = input("회원의 이름을 입력하세요 : ")
          book_isbn = input("반납할 책의 isbn을 입력하세요 :")

          member = next((m for m in my_library.library_members if m.name == member_name), None)
          if not member:
              print("[SYSTEM] 해당 회원이 존재하지 않습니다.")
              continue

          book = next((b for b in member.loaned_book if b.isbn == book_isbn), None)
          if not book:
              print("[SYSTEM] 해당 회원이 대출한 책이 아닙니다.")
              continue

          book.is_loaned = False
          member.remove_book(book)
          print(f"[SYSTEM] {member.name}님이 '{book.title}'을 반납했습니다.")


      elif userInput== 6:
          print("도서 검색의 매뉴입니다")
          book_name = input("책 이름을 입력하세요 :")
          my_library.search_book(book_name)

      elif userInput== 7:
          print("프로그램을 종료합니다.")
          break
      else:
          print("[SYSTEM] 1~7까지의 숫자만 입력하세요")
    except ValueError:
        print("[SYSTEM] 메뉴의 '숫자'를 입력해 주세요")
        continue
