# -*- coding: utf-8 -*-

# 문자열 안에 따옴표 넣기 -> 이스케이프 문자 사용
case1 = "Life is \"too\" short"
print(case1)

case2 = 'Life is \'too\' short'
print(case2)

# 줄바꿈 => \n
print("Life is too short\nYou need Python")

# 탭키 => \t
print("Life is too short\tYou need Python")

# 순수한 역슬래시 출력 => \\
print("Life is too short\\You need Python")


# 따옴표의 쌍을 조절하여 문자열 안에 따옴표 넣기
a = "You 'need' Python"
print(a)

b = 'You "need" Python'
print(b)

# 줄바꿈이 가능한 문자열 -> 3중 쌍따옴표
msg = """Life is too short
You need Python"""
print(msg)
