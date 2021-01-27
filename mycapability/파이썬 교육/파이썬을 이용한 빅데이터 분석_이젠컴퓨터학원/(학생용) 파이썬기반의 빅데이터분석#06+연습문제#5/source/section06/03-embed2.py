# -*- coding: utf-8 -*-

# 제곱근 구하기 --> 2**8 연산과 동일한 결과.
a = pow(2, 8)
print(a)

# 절대값 구하기
a = abs(100)
print(a)

b = abs(-100)
print(b)

c = abs(-12.345)
print(c)

print("-" * 30)


# 나눗셈의 연산 결과를 정수 부분의 몫과 나머지로 계산하여 튜플로 리턴
c = divmod(7, 3)
print(c)

# ex)
hours = 800
k = divmod(800, 24)
tpl = "{0}일 {1}시간"
print( tpl.format(k[0], k[1]) )

print("-" * 30)


# 결과가 튜플로 리턴되므로 값을 서로 다른 변수에 나누어 저장할 수 있다.
days, hours = divmod(960, 24)
tpl = "{0}일 {1}시간"
print( tpl.format(days, hours) )







