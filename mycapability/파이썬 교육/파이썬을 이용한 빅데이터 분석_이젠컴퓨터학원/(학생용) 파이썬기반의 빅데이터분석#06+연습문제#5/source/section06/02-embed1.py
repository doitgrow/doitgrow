# -*- coding: utf-8 -*-

# type() --> 변수의 자료형 조회
a = 123
print( type(a) )

b = 123.45
print( type(b) )

# 변수에 저장하지 않고 값을 직접 전달하여 자료형 조회
print( type( "hello" ) )
print( type( True ) )
print( type( [1, 2] ) )
print( type( (1, 2) ) )
print( type( {"name": "python"} ) )

print("-" * 30)


# isinstance() -> i가 dict 형태인지 판별
#   첫 번째 파라미터는 검사하고자 하는 변수
#   두 번째 파라미터는 type()함수에서 표시하는 자료형(클래스) 이름
i = {"name": "python"}
k = isinstance(i, dict)
print(k)

if isinstance(a, int):
    print("a는 정수 타입 입니다.")
else:
    print("a는 정수 타입이 아닙니다.")

print("-" * 30)



# 숫자 형식의 변수를 문자열로 변환하기
a = 3
b = 10
# -> 숫자끼리 계산이므로 합이 출력됨
print(a+b)

# -> 문자열끼리 계산이므로 연결하여 출력됨
c = str(a)  # "3"
d = str(b)  # "10"
print(c+d)

print("-" * 30)


# 문자열을 숫자로 변환하기
x = "123"
y = "45"

# -> 문자열끼리 연결 : 12345
print(x+y)

# -> 문자열을 정수로 변환
x1 = int(x) # 123
y1 = int(y) # 45
print(x1 + y1)
print("-" * 30)

# -> 문자열이나 정수형을 실수형태로 변환
x2 = float(x)   # -> 문자열을 실수로 변환 = 123.0
y2 = float(y1)  # -> 정수형을 실수로 변환 = 45.0
print(x2 + y2)

print("-" * 30)

