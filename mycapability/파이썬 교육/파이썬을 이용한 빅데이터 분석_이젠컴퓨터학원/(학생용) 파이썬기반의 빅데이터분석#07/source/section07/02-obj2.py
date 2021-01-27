# -*- coding: utf-8 -*-

# 함수들을 내장하는 클래스의 정의
class Calc:
    # 클래스에 포함되는 함수들은 반드시 첫 번째 파라미터 self를 정의해야 한다.
    def plus(self, x, y):
        return x+y

    def minus(self, x, y):
        return x-y

    def all(self, x, y):
        # 같은 클래스에 소속된 함수들끼리 호출할 경우
        # self.함수이름() 형식으로 접근 가능.
        a = self.plus(x, y)
        b = self.minus(x, y)

        # 튜플로 묶어서 여러개의 값을 한번에 리턴
        return (a, b)

# 생성되는 객체는 클래스에 정의된 모든 함수를 부여받는다.
my = Calc()

# 객체를 통한 함수의 호출.
# -> 함수에 정의된 self는 호출시에 값을 전달하지 않는다.
print( my.plus(10, 20) )
print( my.minus(100, 50) )
print("-" * 30)


# all() 함수는 튜플을 리턴한다.
a = my.all(10, 20)
# -> 튜플의 각 원소 확인
print( a[0] )
print( a[1] )
print("-" * 30)

# 튜플로 묶여서 리턴되는 경우 튜플의 각 원소를
# 콤마로 구분하여 각각 반환받을 수 있다.
p,m = my.all(100, 200)
print(p)
print(m)
