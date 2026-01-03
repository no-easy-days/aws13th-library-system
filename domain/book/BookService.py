from exceptions.CustomException import BookAlreadyExists, TargetBookNotFound,TargetBookIsBorrowed,BookIsAlreadyReturned


class BookService:
    """
        도서 관련 비즈니스 로직을 처리하는 서비스 클래스.

        메모리와 CSV 사이에 데이터 처리를 담당하며,
        도서 등록, 조회, 대출 및 반납 상태 관리 로직을 담당
    """
    def __init__(self,book_csv_repository):
        """
            CSV에 책 정보의 의존성을 주입받고, 초기 데이터를 메모리에 로드한다.
            Argument:
                :param book_csv_repository: 도서 데이터를 저장/로드하는 Repository 객체
        """
        #main.py에서 book_csv_repository 의존성 주입
        self.book_csv_repository = book_csv_repository
        #books에 현재 메모리에 저장된 도서 목록 불러오기
        self.books = book_csv_repository.load_all()


    def show_book(self):
        """
            현재 메모리상에 로드된 모든 도서 목록을 출력한다.
        """
        if not self.books:
            print("현재 등록된 책이 없습니다.")
            return

        for book in self.books:
            print(book)

    def add_book(self,new_book):
        """
            새로운 도서를 등록한다.

            ISBN 중복 검사를 수행하며, 성공 시 메모리와 CSV 저장소를 모두 업데이트 한다.
            Argument:
                :param new_book: 등록하고자 하는 Book 클래스의 인스턴스

            Raises:
                :raises:BookAlreadyExists: 이미 존재하는 ISBN일 경우 발생한다.
        """
        #ISBN은 고유해야 함 (Unique Key)
        for existing_book in self.books:
            if existing_book.isbn == new_book.isbn:
                raise BookAlreadyExists(new_book)

        #매우 중요!! 현재 메모리상에 추가된 book을 저장
        self.books.append(new_book)
        #book이 아닌 self.books(현재 메모리상에 저장되어 있는 book list)로
        #save_book 메소드를 호출해야 함 (안 그러면 방금 만든 book 한 객체만 추가됨)
        self.book_csv_repository.save_book(self.books)

    def find_books_by_isbn(self,search_book_isbn):
        """
            ISBN을 사용하여 특정 도서를 검색한다.

            Argument:
                :param search_book_isbn (str): 찾고자 하는 도서의 ISBN

            Returns
                 :return: Book: 검색된 도서 객체

            Raises:
                TargetBookNotFound: 도서를 찾을 수 없는 경우
        """

        find_book = None
        for book in self.books:
            if book.isbn == search_book_isbn:
                find_book = book
                return find_book
        raise TargetBookNotFound(search_book_isbn)

    #isbn을 통해 해당 책이 반납 상태인지 확인하고 해당 책을 사용자에게 대출 전환
    def process_borrowing_by_isbn(self,isbn):
        """
            도서 대출 프로세스를 진행한다.
            도서를 find_books_byIsbn 함수를 이용해서 실제 있는 책인지 확인하고
            도서의 상태를 "대출 중"으로 전환한다.

            Argument:
                 :param isbn: 대출 처리를 진행 할 도서의 고유 번호(Unique)
            Returns:
                :return: 대출 상태가 "True"로 업데이트 된 Book 객체
            Raises:
                :raises: TargetBookIsBorrowed: 이미 대출 중인 도서인 경우
        """
        # target_book이 대출중이라면
        target_book = self.find_books_by_isbn(isbn)
        if target_book.is_borrowed:
            raise TargetBookIsBorrowed(target_book)

        # 해당 책은 대출 상태로 전환
        target_book.is_borrowed = True
        return target_book

    #책 반납 시 해당 책이 대출 상태인지 확인하고 해당 책을 사용자에게 반납
    def process_return_by_isbn(self,isbn):
        """
            도서 반납 프로세스를 진행한다.
            도서를 find_books_byIsbn 함수를 이용해서 실제 있는 책인지 확인하고
            도서의 상태를 "반납"으로 전환한다.

            Argument:
                :param isbn: 대출 처리를 진행 할 도서의 고유 번호(Unique)
            Returns:
                :return: 대출 상태가 "False"로 업데이트 된 Book 객체
            Raises:
                :raises: : BookIsAlreadyReturned 이미 반납 된 도서인 경우
        """
        target_book = self.find_books_by_isbn(isbn)
        if not target_book.is_borrowed:
            raise BookIsAlreadyReturned(target_book)

        target_book.is_borrowed = False
        return target_book

    def search_books_by_keyword(self,keyword):
        """
        제목에 키워드가 포함된 모든 책을 검색한다.
        Argument:
            :param keyword: 검색하고자 하는 도서 제목의 핵심 단어 (str)
        Returns:
            :return: 키워드가 제목에 포함된 Book 객체들의 리스트
                     검색 결과 없을 시 빈 리스트 반환
        """
        #리스트 컴프리헨션
        '''
            for book in self.books:
                if keyword in book.title:
                results.append(book)    
            return results -> 리스트 컴프리헨션으로
        '''
        return [book for book in self.books if keyword in book.title]