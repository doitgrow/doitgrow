# -*- coding: utf-8 -*-

# 튜플을 통한 변수 생성
a, b = ("python", "bigdata")
print(a)
print(b)
print("-" * 30)

# 위의 구문과 동일한 기능
(a, b) = "hello", "world"
print(a)
print(b)
print("-" * 30)

# 위의 구문과 동일한 기능
(a, b) = ("안녕", "파이썬")
print(a)
print(b)
print("-" * 30)

# 리스트를 통한 방법도 같은 결과
a, b = ["python", "bigdata"]
print(a)
print(b)
print("-" * 30)

[a, b] = "hello", "world"
print(a)
print(b)
print("-" * 30)

# 리스트를 활용한 변수 생성
[a, b] = ["안녕", "파이썬"]
print(a)
print(b)
print("-" * 30)

# 동일한 값을 갖는 여러 변수 생성
a = b = c = 1234
print(a)
print(b)
print(c)
print("-" * 30)

# 두 변수의 값을 교환
x = 1
y = 2
x, y = y, x
print(x)
print(y)


