# -*- coding: utf-8 -*-

# my_mod1.py 파일의 모든 내용을 참조한다.
# -> import 파일이름
import my_mod1

# 참조한 파일에 정의된 변수,함수는 `파일이름.기능명` 형식으로 사용 가능.
print(my_mod1.NAME)
print(my_mod1.plus(3, 4))
print(my_mod1.minus(3, 4))


