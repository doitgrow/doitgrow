# -*- coding: utf-8 -*-

# 기본형.
print("Hello World")
print("-" * 30)

# 문장 여러개를 공백으로 구분하여 지정할 경우 "+"연산과 동일하다.
# -> 단순한 문자열 연결
print("Life" + "is" + "short")
print("Life"  "is"  "short")
print("-" * 30)

# 문장을 콤마로 구분하면 띄어쓰기가 수행된다.
# -> 문자열 이외의 다른 타입의 변수도 사용 가능함
a = 100
print("Life", "is", "short", a)
print("-" * 30)


# 출력할 내용을 구성하고 마지막에 `end=""`라고 지정하면 줄바꿈을 수행하지 않는다.
print("Life ", end="")
print("is ", end="")
print("short ", end="")

# end는 출력후 마무리를 어떻게 할지 지정하는 기능.
# -> 기본값은 (줄바꿈문자)"\n"으로 지정되어 있다.
print("You", "need", "Python", end="~~^^)/")
