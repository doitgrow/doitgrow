# -*- coding: utf-8 -*-

import os
import sys

# 현재 작업중인 폴더(Current Wording Directory) 위치 확인
# -> 소스파일이 위치한 폴더.
print(os.getcwd())
print("-" * 30)

# 현재 폴더 내의 하위 항목들의 이름을 리스트로 리턴받음
# -> "./" 혹은 "." 은 현재 폴더라는 의미
# -> "../ 는 상위 폴더라는 의미"
ls = os.listdir('./')
print(ls)
print('-' * 30)

# 특정 폴더내의 항목들 조회하기
if sys.platform == 'win32':
    target = 'C:\\'     # C드라이브의 최상위 폴더
else:
    target = "/"       # mac,linux의 최상위 폴더

ls = os.listdir(target)
print(ls)

