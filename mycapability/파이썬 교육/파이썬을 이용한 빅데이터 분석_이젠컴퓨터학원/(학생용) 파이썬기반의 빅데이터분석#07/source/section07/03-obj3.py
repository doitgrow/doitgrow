# -*- coding: utf-8 -*-
# 변수와 함수를 모두 내장하는 클래스 정의
class Member:
    # 클래스 레벨에서 정의된 변수는 내장되어 있는 함수들끼리 공유한다.
    # -> `전역변수` 혹은 `멤버변수` 라고 부름
    username = ""
    email = ""

    def join(self, username, email):
        # 파라미터로 전달된 값들을 멤버변수에 복사 --> 데이터 입력
        # 파라미터나 메서드 안에서 정의된 변수들은
        # 그 함수 밖에서는 식별할 수 없으므로 `지역변수`라고 부름
        self.username = username
        self.email = email

    def view_info(self):
        # join()에 의해서 설정된 값들을 활용 --> 데이터 출력
        print( self.username )
        print( self.email )

# 클래스의 기능을 객체에 부여하기
mem1 = Member()
mem1.join("Python", "python@gmail.com")
mem1.view_info()


