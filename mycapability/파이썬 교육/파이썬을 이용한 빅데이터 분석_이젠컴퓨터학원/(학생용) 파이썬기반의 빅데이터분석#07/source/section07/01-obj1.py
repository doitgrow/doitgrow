# -*- coding: utf-8 -*-

# 클래스 - 객체를 구성하는 자료구조
# -> 변수를 그룹화 하기 위한 단위를 정의한 것
class Member:
    userid = "python"
    email = "python@gmail.com"
    phone = "01012345678"

# 객체 - 클래스에서 정의한 구조를 부여받은 특수한 변수
# 객체 생성하기 -> 변수이름 = 클래스이름()
# -> 객체 안에는 클래스 단위의 구조를 갖는 변수들이 내장된다.
mem1 = Member()
print(mem1.userid)
print(mem1.email)
print(mem1.phone)
print("-" * 30)

# 객체 안에 내장된 변수는 일반 변수와 동일하게 사용 가능.
# -> 값을 변경하는 것도 가능.
mem1.userid = "life";
mem1.email = "life@naver.com"
mem1.phone = "01098765432"
print(mem1.userid)
print(mem1.email)
print(mem1.phone)
print("-" * 30)

# 정의된 클래스는 몇번이고 재사용 할 수 있다.
# -> 같은 자료구조를 갖는 객체를 여러개 생성할 수 있다.
# -> 클래스 = 붕어빵 틀, 객체 = 붕어빵
mem2 = Member()
mem2.userid = "hello"
mem2.email = "hello@daum.com"
mem2.phone = "01087682342"
print(mem2.userid)
print(mem2.email)
print(mem2.phone)
print("-" * 30)

