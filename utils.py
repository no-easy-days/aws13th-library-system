import csv
from models import Book

def load_books_from_csv(filename):
    # CSV 파일에서 도서 데이터를 읽어오는 함수
    books = []
    try:
        with open(filename, 'r', encoding='utf-8') as file: # 인코딩 지정, 
            csv_reader = csv.reader(file) # CSV 파일을 읽는 리더 객체 생성
            next(csv_reader, None)  # 다음 줄 읽기 - 첫 줄(헤더) 건너뛰기
            
            for row in csv_reader:
                if len(row) >= 3:  # 데이터가 3개 이상인 경우만 처리
                    title = row[0].strip()
                    author = row[1].strip()
                    isbn = row[2].strip()
                    book = Book(title, author, isbn)
                    books.append(book)
        
        return books
    
    except FileNotFoundError:
        print(f"[오류] '{filename}' 파일을 찾을 수 없습니다.")
        return []
    
    except Exception as e:
        print(f"[오류] 파일을 읽는 중 문제가 발생했습니다: {e}")
        return []


def get_valid_input(prompt, input_type=str):
    # 사용자로부터 올바른 입력을 받을 때까지 반복
    while True:
        try: # 사용자 입력 받기
            user_input = input(prompt)
            if input_type is int: # 숫자 변환이 필요할 경우 변환해서 반환
                # 타입 비교 시 is 사용
                return int(user_input)
            return user_input # 문자열 그대로 반환
        except ValueError: # 숫자로 변환 실패시 에러 메시지
            print("[오류] 숫자를 입력해주세요.") 