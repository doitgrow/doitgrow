# -*- coding: utf-8 -*-

# 연산 결과는 새로운 변수에 할당 하거나 직접 출력 가능
a = 3
b = 4
c = a + b
print(c)

# 연산결과 직접 출력
print( a - b )
print( a * b )
print( a / b )

# 나눗셈의 몫을 구한다
# -> 처리 가능한 단위까지 계산함(마지막 오차발생)
print( 10 / 3 )

# 나눗셈에서 소수점 아래를 버리고 몫만 계산
print ( 10 // 3 )

# 나눗셈의 나머지를 구한다.
# -> 정수 단위에서만 연산후 종료.
print( 10 % 3 )

# 제곱 구하기
print( 3 ** 5 )

# 단항연산자
a = 1
a += 100 # 100 + 1 -> 101
a *= 10  # 101 * 10 -> 1010
a //= 3  # 1010 // 3 -> 336
a %= 5   # 336 % 5 -> 1
print(a)

# 비교연산자
print(100 == 50)
print(100 != 50)
print(100 >= 50)
print(100 > 50)
print(100 < 50)
print(100 <= 50)

# 비교연산도 하나의 수식이므로 결과를 다른 변수에 할당 가능함
result = 100 > 50
print(result)

# 논리연산자
print( True and True )
print( True and False )
print( False and True )
print( False and False )

print( True or True )
print( True or False )
print( False or True )
print( False or False )

# 비교연산의 결과값은 bool형식이므로 논리연산이 가능함
a = 100 > 50
b = 20 > 10
print( a and b )

c = 100 >= 100 and 50 == 10
print(c)

print( 100 != 200 and 100 == 100)


# 두 변수가 동일한지 판별하는 is 연산자
s1 = a is b
print(s1)

s2 = a is c
print(s2)

# "==" 연산과 "is" 연산의 차이
x = 100             # -> 정수형 변수
y = 100.0           # -> 실수형 변수

# 단순히 값만 비교하므로 두 값이 같다고 판단함
print( x == y )

# 값의 종류(데이터타입)까지 비교하므로 정수와 실수는 다르다고 판단함
print( x is y )
