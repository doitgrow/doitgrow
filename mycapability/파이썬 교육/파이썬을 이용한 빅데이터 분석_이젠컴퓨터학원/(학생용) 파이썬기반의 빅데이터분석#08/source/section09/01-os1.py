# -*- coding: utf-8 -*-

import sys      # 현재 시스템의 정보를 제공하는 모듈
import os       # 운영체제의 기능에 접근할 수 있는 모듈

# 현재 운영체제 이름 얻기
# -> 윈도우=win32, Mac=darwin, Linux=linux1 혹은 linux2
print(sys.platform)
print('-' * 30)

# 윈도우인 경우와 그 밖의 경우를 분기하여 command 변수 생성
if sys.platform == 'win32':
    command = 'dir'
else:
    command = 'ls -l'

# 시스템 명령어를 수행하여 결과를 즉시 출력
#   -> 서브라임에서 출력할 경우 윈도우에서는 한글 깨질 수 있음
os.system(command)
print('-' * 30)


# 시스템 명령어를 수행하여 출력결과를 리턴받음
ls = os.popen(command)
# -> 출력결과는 객체형식
print(ls)
print('-' * 30)

# -> 출력결과를 문자열로 변환함.
# -> 출력결과를 리턴한 후 ls객체가 담고 있던 내용은 소멸됨
r1 = ls.read()
print(r1)
print('-' * 30)

# 시스템 명령어의 수행 결과를 리스트로 변환하여 출력하기
ls = os.popen(command)
r2 = list(ls)
for item in r2:
    print(" >> ", item.strip())
