# -*- coding: utf-8 -*-

class Member:
    # 변수의 값을 비워두기 위해 None을 할당함
    username = None
    email = None

    # 생성자 - 객체가 생성될 때 자동으로 실행되는 특수 함수.
    #          이름이 고정되어 있다. (앞뒤로 언더바 두 개)
    #          주로 클래스에 속한 변수값을 초기화 하는 용도로 사용
    def __init__(self):
        print("------- 생성자가 실행되었습니다. --------")
        self.username = "야옹이"
        self.email = "yaong@gmail.com"

    def view_info(self):
        tpl = "이름: {0} / 이메일: {1}"
        print( tpl.format(self.username, self.email ) )

mem1 = Member()
mem1.view_info()


