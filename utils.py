import csv

# csv 파일을 리스트로 변환하는 함수
def csv_to_list(filename):
    with open(filename, "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        return list(reader)