# -*- coding: utf-8 -*-
# 06-shutil2.py

import os
import shutil

#-----------------------------------------------------
# os모듈 내의 path 객체가 갖는 exsits() 함수를 사용.
# -> "hello.txt"라는 파일이 존재하지 않는다면?
if os.path.exists('hello.txt') == False:
    # 테스트용 파일 생성
    with open("hello.txt", "w", encoding="utf-8") as f:
        f.write("Life is too short, you need python")
        print('hello.txt 파일을 생성했습니다.')

    # 생성한 파일을 복사함 -> 이미 존재할 경우 덮어씀
    shutil.copy('hello.txt', 'world.txt')
    print('hello.txt가 world.txt로 복사되었습니다.')
#-----------------------------------------------------
# 그렇지 않다면?
# -> "hello.txt"라는 파일이 존재 한다면?
else:
    os.remove('hello.txt')
    print('hello.txt가 삭제되었습니다.')
    os.remove('world.txt')
    print('world.txt가 삭제되었습니다.')
#-----------------------------------------------------
