# -*- coding: utf-8 -*-

# my_mod2.py 파일의 기능을 import
import my_mod2

# my_mod2에 정의된 Member라는 클래스에 "모듈이름.클래스이름" 형식으로 접근
# -> import된 클래스는 정의된 기능을 다른 변수에 부여해야 사용 가능. = 객체
# -> 클래스에 생성자가 포함되어 있고 생성자가 파라미터를 갖는 경우
#    객체 생성시에 생성자 파라미터를 전달해야 함.
mem = my_mod2.Member('파이썬학생', 'leekh4232@gmail.com')
mem.view_info()


