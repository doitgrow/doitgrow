# -*- coding: utf-8 -*-

class Member:
    username = None
    email = None

    # 생성자도 함수의 일종이므로 필요한만큼 파라미터를 정의할 수 있다.
    # 주로 외부에서 전달되는 값을 클래스변수에 할당하는 용도로 사용한다.
    def __init__(self, username, email):
        print("------- 생성자가 실행되었습니다. --------")
        self.username = username
        self.email = email

    def view_info(self):
        tpl = "이름: {0} / 이메일: {1}"
        print( tpl.format(self.username, self.email) )


# 생성자가 파라미터를 갖는 클래스에 대한 객체를 생성할 경우
# 생성자가 정의하는 파라미터를 전달해야 한다.
mem1 = Member("야옹이", "yaong@gmail.com")
mem1.view_info()


