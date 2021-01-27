# -*- coding: utf-8 -*-

# 쌍따옴표나 홑따옴표로 감싸야 한다. -> 따옴표의 혼용은 불가.
msg1 = "Life is too short"
msg2 = 'You need Python'
print(msg1)
print(msg2)

# 문자열의 덧셈은 문자열을 연결하는 기능
print( msg1 + ", " + msg2 )

# 문자열과 숫자의 곱셈은 동일 내용을 여러번 반복한다.
name = "Python"
print(name * 50)

# 따옴표로 감싸면 무조건 문장.
# -> 숫자가 아니므로 연산 결과도 문자열 연산 규칙을 따른다.
pay = "20000"
bonus = "100"
print( pay + bonus )


# 문자열 안에 따옴표 넣기 -> 이스케이프 문자 사용
case1 = "Life is \"too\" short"
print(case1)

case2 = 'Life is \'too\' short'
print(case2)

# 따옴표의 쌍을 조절하는 방법
case3 = "You 'need' Python"
print(case3)

case4 = 'You "need" Python'
print(case4)

# 줄바꿈 => \n
print("Life is too short\nYou need Python")

# 탭키 => \t
print("Life is too short\tYou need Python")

# 순수한 역슬래시 출력 => \\
print("Life is too short\\You need Python")

# 줄바꿈이 가능한 문자열 변수 -> 3중 쌍따옴표
msg = """Life is too short
You need Python"""
print(msg)
