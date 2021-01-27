# -*- coding: utf-8 -*-

# my_mod2 모듈에서 Member라는 이름의 기능만 지정해서 참조
from my_mod2 import Member

# from절로 특정 기능만 골라서 참조한 경우 파일이름이나 별칭 없이 적접 접근.
# 참조된 기능이 클래스므로, 객체로 생성해야만 사용가능.
mem = Member('파이썬학생', 19)
mem.view_info()


