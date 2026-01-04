import csv

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