"""
도서관을 이용하는 회원 한명 한명에 대한 정보 처리하는 클래스 생성

회원의 이름,전화번호 받아서 저장
그리고 그 회원이 대출한 책에 대한 목록
"""



class Member:
    def __init__(self,name,phone):
        self.name = name
        self.phone = phone
        self.borrowed_books = []

