# -*- coding: utf-8 -*-

# 모듈안에 포함된 특정 기능만 골라서 가져오기
# -> from 모듈이름 import 기능명
from my_mod1 import NAME
from my_mod1 import plus

# 골라서 가져온 기능들은 앞에 모듈이름을 적용하지 않고,
# 직접 접근 가능하다.
print(NAME)

print(plus(3, 4))

# minus 함수는 import 하지 않았으므로 사용 불가
# print(minus(3, 4))


