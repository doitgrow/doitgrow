# -*- coding: utf-8 -*-

# is는 두 변수의 값이 동일하면 True
a = 123
b = 123
c = 234

if a is b:
    print("a와 b는 같다")

if b is c:
    print("b와 c는 같다")

print("-" * 30)


# == 와 is의 차이
# -> "=="은 값만 비교하므로  실수형 1.0과 정수형 1을 같다고 판별한다.
# -> "is"는 변수의 타입까지 비교하므로 실수형과 정수형은 다르다고 판별한다.
x = 1
y = 1
z = 1.0

if x == z:
    print("x와 z는 같다")

if y is z:
    print("y와 z는 같다")

print("-" * 30)


# 두 값이 서로 다르다면 참인 is not
a = 123.0
b = 123
c = 234

if a is not b:
    print("a와 b는 다르다")

if b is not c:
    print("b와 c는 다르다")

print("-" * 30)



# 포함 여부를 검사하는 in 연산자.
# -> in은 왼쪽의 값이 오른쪽 대상에 포함되어 있다면 참.
user1 = "hello"
user2 = "world"
member_list = ['hello', 'python', 'life']

# -> 왼쪽의 변수가 오른쪽의 리스트에 속한 값이면 참
a = user1 in member_list
print(a)

b = user2 in member_list
print(b)

# -> 조건이 참이므로 결과가 출력됨
if user1 in member_list:
    print( user1 + "(은)는 이미 가입되어 있습니다." )

# -> 조건이 거짓이므로 결과가 출력되지 않음
if user2 in member_list:
    print( user2 + "(은)는 이미 가입되어 있습니다." )

print("-" * 30)


# 포함되지 않았음을 검사하는 not in 연산자
# -> 'not in'은 포함되어 있지 않은 경우 참이 된다.
# -> 조건이 거짓이므로 결과가 출력되지 않음
if user1 not in member_list:
    print( user1 + "(은)는 가입되어 있지 않습니다." )

# -> 조건이 참이므로 결과가 출력됨
if user2 not in member_list:
    print( user2 + "(은)는 가입되어 있지 않습니다." )
