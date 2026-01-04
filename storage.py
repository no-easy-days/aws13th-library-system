import json
from models import Member, Book, BookRequest
from library import Library

class Storage:
    def save_state(self, lib: Library, filename: str = "library_state.json") -> None:
        """라이브러리 상태를 JSON 파일로 저장"""
        state = {
            "members": {},
            "books": {},
            "requests": [],
            "next_request_id": lib.next_request_id
        }
        
        # 회원 정보 저장
        for member_id, member in lib.members.items():
            state["members"][member_id] = {
                "member_id": member.member_id,
                "name": member.name,
                "phone": member.phone,
                "password": member.password,
                "role": member.role
            }
        
        # 도서 정보 저장
        for isbn, book in lib.books.items():
            state["books"][isbn] = {
                "title": book.title,
                "author": book.author,
                "isbn": book.isbn,
                "borrowed_by": book.borrowed_by
            }
        
        # 요청 정보 저장
        for request in lib.requests:
            state["requests"].append({
                "request_id": request.request_id,
                "member_id": request.member_id,
                "title": request.title,
                "author": request.author,
                "isbn": request.isbn,
                "status": request.status
            })
        
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(state, f, ensure_ascii=False, indent=2)
    
    def load_state(self, lib: Library, filename: str = "library_state.json") -> bool:
        """JSON 파일에서 라이브러리 상태 복원"""
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                state = json.load(f)
            
            # 회원 정보 복원
            for member_data in state["members"].values():
                member = Member(
                    member_id=member_data["member_id"],
                    name=member_data["name"],
                    phone=member_data["phone"],
                    password=member_data["password"],
                    role=member_data["role"]
                )
                lib.members[member.member_id] = member
            
            # 도서 정보 복원
            for book_data in state["books"].values():
                book = Book(
                    title=book_data["title"],
                    author=book_data["author"],
                    isbn=book_data["isbn"]
                )
                book.borrowed_by = book_data["borrowed_by"]
                lib.books[book.isbn] = book
            
            # 요청 정보 복원
            for request_data in state["requests"]:
                request = BookRequest(
                    request_id=request_data["request_id"],
                    member_id=request_data["member_id"],
                    title=request_data["title"],
                    author=request_data["author"],
                    isbn=request_data["isbn"]
                )
                request.status = request_data["status"]
                lib.requests.append(request)
            
            lib.next_request_id = state.get("next_request_id", 1)
            
            return True
        except FileNotFoundError:
            return False