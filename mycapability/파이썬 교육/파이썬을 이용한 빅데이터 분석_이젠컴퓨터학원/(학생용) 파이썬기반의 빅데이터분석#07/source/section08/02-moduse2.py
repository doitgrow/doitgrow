# -*- coding: utf-8 -*-

# 참조한 my_mod1 모듈에 hello라는 별칭 적용하기
# -> import 파일이름 as 별칭
import my_mod1 as hello

# 모듈에 포함된 기능들은 `별칭이름.기능명`형식으로 접근
print(hello.NAME)
print(hello.plus(3, 4))
print(hello.minus(3, 4))


