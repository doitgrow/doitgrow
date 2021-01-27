# -*- coding: utf-8 -*-

str = "Life is too short, You need Python"

# 전체 글자수 세기 -> 파이썬 내장함수. 한글,영문 구분 없이 1글자씩 카운트
a = len(str)
print( a )
# -> 반환되는 값을 변수에 저장하지 않고 직접 출력도 가능함.
print( len(str) )

# -> 주제마다 출력 결과를 구분하기 위한 직선
print("-" * 30)

# 특정 글자나 단어의 개수 세기
print( str.count("i") )
print( str.count("a") )
print( str.count("short") )
print( str.count("nice") )
print("-" * 30)

# 특정 글자나 단어가 처음 등장하는 위치 조회
# -> 찾지 못할 경우 -1을 리턴함
print( str.find("t") )
print( str.find("short") )
print( str.find("g") )
print( str.find("nice") )
print("-" * 30)

# 특정 글자나 단어가 마지막으로 등장하는 위치 조회
# -> 마지막으로 나타나는 글자의 위치를 왼쪽에서 0부터 카운트 한다.
# -> 찾지 못할 경우 -1을 리턴함
print( str.rfind("t") )
print( str.rfind("short") )
print( str.rfind("g") )
print( str.rfind("nice") )
print("-" * 30)

# 특정 글자나 단어가 처음 등장하는 위치 조회
print( str.index("short") )
# -> 찾지 못할 경우 에러 발생함
# print( str.index("nice") )
print("-" * 30)

# 특정 단어나 글자로 끝나는지 여부 검사 (True, False가 반환된다.)
# -> 대문자 "L"로 시작하는지 검사
print( str.startswith("L") )
# -> 소문자 "l"로 시작하는지 검사
print( str.startswith("l") )
# -> "Life"라는 단어로 시작하는지 검사
print( str.startswith("Life") )
# -> 대문자 "H"로 시작하는지 검사
print( str.startswith("H") )
# -> "Hello"이라는 단어로 시작하는지 검사
print( str.startswith("Hello") )
print("-" * 30)

# 특정 단어나 글자로 끝나는지 여부 검사 (True, False가 반환된다.)
# -> 대문자 "N"으로 끝나는지 검사
print( str.endswith("N") )
# -> 소문자 "n"으로 끝나는지 검사
print( str.endswith("n") )
# -> "Python"이라는 단어로 끝나는지 검사
print( str.endswith("Python") )
# -> "python"이라는 단어로 끝나는지 검사
print( str.endswith("python") )
print("-" * 30)

# 대소문자 변환
# -> 모든 글자를 대문자로 변환한 결과를 반환한다.
# -> 반환 결과를 변수에 저장하고 변수값을 출력하기
upchar = str.upper()
print( upchar )
# -> 모든 글자를 소문자로 변환한 결과를 반환한다.
lowchar = str.lower()
print( lowchar )
# -> 대문자는 소문자로, 소문자는 대문자로 변환한 결과를 반환한다.
# -> 반환 결과를 직접 출력하기
print( str.swapcase() )
# -> 문장의 첫 글자를 대문자로 변환한 결과를 반환한다.
print( str.capitalize() )
# -> 각 단어의 첫 글자를 대문자로 변환한 결과를 반환한다.
print( str.title() )
print("-" * 30)

# 문자열 바꾸기
# -> 변수.replace(A, B), 변수에서 A를 B로 변경
print( str.replace("Life", "Your height") )
print("-" * 30)

# 공백지우기
k = "     python     "
#-> 왼쪽 공백을 지운 결과를 반환한다.
print( k.lstrip() )
#-> 오른쪽 공백을 지운 결과를 반환한다.
print( k.rstrip() )
#-> 좌우 공백을 지운 결과를 반환한다.
print( k.strip() )
print("-" * 30)

# 파라미터로 전달되는 문자열의 각 글자 사이에 변수값을 삽입
a = ","
b = a.join("python")
print(b)
print("-" * 30)
