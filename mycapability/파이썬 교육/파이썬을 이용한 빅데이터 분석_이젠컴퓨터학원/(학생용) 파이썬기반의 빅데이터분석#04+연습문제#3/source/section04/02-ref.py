# -*- coding: utf-8 -*-

# 숫자형,문자열,논리값을 대입할 경우 변수값의 복사
a = 100
b = a
print(a)
print(b)
print("-" * 30)

# -> 복사본을 변경하더라도 원본에는 변화가 없다.
# -> 반대의 경우도 마찬가지
b = 200
print(a)
print(b)
print("-" * 30)

# 객체의 참조 --> 리스트,딕셔너리,집합
foo = [ 1, 2, 3 ]
bar = foo
print(foo)
print(bar)
print("-" * 30)

# -> 참조된 복사본을 변경하면 원본도 함께 변경됨.
# -> 반대의 경우도 마찬가지
# -> 지금까지의 내용들 중에는 리스트, 딕셔너리에 적용됨.
bar[1] = 20
print(foo)
print(bar)
print("-" * 30)

# 리스트 복사 (고전적인 방법)
# -> 같은 길이의 리스트를 만들고 각 원소를 일일이 복사함.
bar = [ 1, 2, 3 ]
cp1 = [ 0, 0, 0 ]
cp1[0] = bar[0]
cp1[1] = bar[1]
cp1[2] = bar[2]
print(bar)
print(cp1)

# -> 복사본을 변경하더라도 원본에 변화 없음.
cp1[2] = 1000
print(bar)
print(cp1)
print("-" * 30)

# 슬라이싱을 활용한 방법
cp2 = bar[:]
print(bar)
print(cp2)
print("-" * 30)

# -> 복사본을 변경하더라도 원본에 영향이 없다.
cp2[1] = 12345
print(bar)
print(cp2)
print("-" * 30)


# 리스트 객체의 함수를 사용하는 방법
cp3 = cp2.copy()

# -> 복사본을 변경하더라도 원본에 영향이 없다.
cp3[0] = 12345
print(cp2)
print(cp3)




