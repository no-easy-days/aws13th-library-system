import csv
import re

# csv 파일을 리스트로 변환하는 함수
def csv_to_list(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            reader = csv.reader(file)
            data = list(reader)
    except FileNotFoundError:
        raise FileNotFoundError(f"{filename} 파일을 찾을 수 없습니다.")
    
    if len(data) <= 1:
        raise ValueError(f"{filename} 파일에 도서 데이터가 없습니다.")
    
    return data

def input_non_empty(prompt, error_message):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        else:
            print(f"\n[ERROR] {error_message}")
            
def validate_phone(phone):
    pattern = r"^010(-?\d{4}){2}$"
    if not re.match(pattern, phone):
        raise ValueError("전화번호 형식이 올바르지 않습니다. 예: 01012345678 또는 010-1234-5678")
    
def validate_name(name):
    if not name.replace(" ", "").isalpha():
        raise ValueError("이름은 한글 또는 영문자만 포함해야 합니다.")
    
def validate_isbn(isbn):
    if not isbn.isdigit():
        raise ValueError("ISBN은 숫자만 입력해야 합니다.")
    if len(isbn) != 13:
        raise ValueError("ISBN은 13자리 숫자여야 합니다.")