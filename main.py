import csv

#프로그램 실행 yes 눌르면 진행 아니면 종료 while로
library = []
# user in
while True:

with open('books.csv','r',encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    print("[system] 도서관의 목록을 불러왔습니다.")
    for row in reader:
        library.append(row)

for index, i in enumerate(library, start=1):
    print(str(index) + "- " + i["title"] + "/ " + i["author"] + "/ " + i["isbn"])

print(1.)
print(2.)
print(3.)
print(4.)
print(5.)
print(6.)
#
# #이름 및 전화번호 입력 및 저장 함수 받은 정보는 dict형식으로 저장
# def restration():
#     input()
#     return

#저장된 이름 과 isbn을 input하고 화원이 존재하고, isbn이 대출 가능 상태일시 대출 처리
# 대출 완료시 library에 isbn의 해당 책에 새로운 키밸류 값으로 대출 중이라는 값 집어넣어 처리

#도서검색 title, author, isbn으로 입력할시 str 인덱싱 값을 설정하여 해당 자료 찾기
#'한글자'검색은 차단, 두글자 이상 검색만 허용

#exit 버튼으로 종료 커멘트 생성



# print(library[0].items())
# print(library[1].items())
# print(library[2].items())
# #

# class Book: {
# }
#
# class Member: {
#
# }
#
#
# booklist = {"" :"",
#             "" : ""}
