from exceptions import DomainError
from models import Member

def handle_signup(lib, ui) -> None:
    ui.system("[회원가입]")
    member_id = ui.ask_str("아이디(member_id): ")
    name = ui.ask_str("이름: ")
    phone = ui.ask_str("전화번호(010-0000-0000 또는 숫자만): ")
    password = ui.ask_str("비밀번호(4~13자리): ")

    try:
        m = lib.register_member(member_id, name, phone, password)
        ui.success(f"{m.member_id} 가입 완료")
    except DomainError as e:
        ui.error(str(e))


def handle_login(lib, ui) -> Member | None:
    ui.system("[로그인]")
    member_id = ui.ask_str("아이디(member_id): ")
    password = ui.ask_str("비밀번호: ")

    try:
        m = lib.login(member_id, password)
        ui.success(f"{m.name}님 로그인 성공 ({m.role})")
        return m
    except DomainError as e:
        ui.error(str(e))
        return None


def handle_book_list(lib, ui) -> None:
    ui.system("[도서 목록]")
    books = lib.get_all_books()
    
    if not books:
        ui.system("등록된 도서가 없습니다.")
        return
    
    for book in books:
        print(book)


def handle_book_search(lib, ui) -> None:
    ui.system("[도서 검색]")
    query = ui.ask_str("검색할 도서 제목: ")
    
    try:
        books = lib.search_books(query)
        if not books:
            ui.system("검색 결과가 없습니다.")
            return
        
        ui.system(f"검색 결과: {len(books)}권")
        for book in books:
            print(book)
    except DomainError as e:
        ui.error(str(e))


def handle_book_borrow(lib, ui, current_user: Member) -> None:
    ui.system("[도서 대출]")
    isbn = ui.ask_str("대출할 도서 ISBN: ")
    
    try:
        lib.borrow_book(current_user.member_id, isbn)
        book = lib.books.get(isbn)
        ui.success(f"'{book.title}' 대출 완료")
    except DomainError as e:
        ui.error(str(e))


def handle_book_return(lib, ui, current_user: Member) -> None:
    ui.system("[도서 반납]")
    isbn = ui.ask_str("반납할 도서 ISBN: ")
    
    try:
        book = lib.books.get(isbn)
        lib.return_book(current_user.member_id, isbn)
        ui.success(f"'{book.title}' 반납 완료")
    except DomainError as e:
        ui.error(str(e))


def handle_my_loans(lib, ui, current_user: Member) -> None:
    ui.system("[내 대출 목록]")
    loans = lib.get_member_loans(current_user.member_id)
    
    if not loans:
        ui.system("대출중인 도서가 없습니다.")
        return
    
    ui.system(f"대출중인 도서: {len(loans)}권")
    for book in loans:
        print(f"- {book.title} / {book.author} / {book.isbn}")


def handle_book_request(lib, ui, current_user: Member) -> None:
    ui.system("[도서 등록 요청]")
    title = ui.ask_str("도서 제목: ")
    author = ui.ask_str("저자: ")
    isbn = ui.ask_str("ISBN: ")
    
    try:
        request = lib.request_book(current_user.member_id, title, author, isbn)
        ui.success(f"도서 등록 요청이 생성되었습니다. (요청 ID: {request.request_id})")
    except DomainError as e:
        ui.error(str(e))


def handle_register_book(lib, ui) -> None:
    ui.system("[도서 등록]")
    title = ui.ask_str("도서 제목: ")
    author = ui.ask_str("저자: ")
    isbn = ui.ask_str("ISBN: ")
    
    try:
        book = lib.register_book(title, author, isbn)
        ui.success(f"'{book.title}' 등록 완료")
    except DomainError as e:
        ui.error(str(e))


def handle_view_requests(lib, ui) -> None:
    ui.system("[도서 등록 요청 목록]")
    requests = lib.get_pending_requests()
    
    if not requests:
        ui.system("대기중인 요청이 없습니다.")
        return
    
    for request in requests:
        print(f"- {request.request_id}: {request}")


def handle_approve_request(lib, ui) -> None:
    ui.system("[도서 등록 요청 승인]")
    request_id = ui.ask_str("승인할 요청 ID: ")
    
    try:
        book = lib.approve_request(request_id)
        ui.success(f"요청이 승인되어 '{book.title}'이(가) 등록되었습니다.")
    except DomainError as e:
        ui.error(str(e))


def handle_reject_request(lib, ui) -> None:
    ui.system("[도서 등록 요청 거절]")
    request_id = ui.ask_str("거절할 요청 ID: ")
    
    try:
        lib.reject_request(request_id)
        ui.success(f"요청이 거절되었습니다.")
    except DomainError as e:
        ui.error(str(e))


def handle_view_all_loans(lib, ui) -> None:
    ui.system("[전체 대출 현황]")
    loans = lib.get_all_loans()
    
    if not loans:
        ui.system("현재 대출중인 도서가 없습니다.")
        return
    
    ui.system(f"대출중인 도서: {len(loans)}권")
    for book, member_id in loans:
        member = lib.members.get(member_id)
        member_name = member.name if member else "알 수 없음"
        print(f"- {book.title} / {book.isbn} (대출자: {member_name} [{member_id}])")
