# -*- coding: utf-8 -*-

dic = { "name": "철수", "phone": "010-1234-5678", "birth": "0115" }

# 특정 key에 대응하는 값 얻기
# -> dic["name"]과 동일
print(dic.get("name"))

# 존재하지 않는 key에 접근하는 경우 --> 에러
# print(dic["gender"])
# 존재하지 않는 key에 접근하는 경우 --> 에러아님(None이 반환됨)
print(dic.get("gender"))

# get함수는 전달하는 key가 존재하지 않을 경우
# 대신 반환될 값을 함께 설정할 수 있다.
print(dic.get("gender", "남자"))

print("-" * 30)




# Key만 모아서 dict_keys라는 객체로 반환
keys = dic.keys()
print(keys)
print("-" * 30)

# dict_keys를 list로 변환
key_list = list(keys)
print(key_list)
print("-" * 30)

# Value만 모아서 dic_values 객체로 반환
values = dic.values()
print(values)
print("-" * 30)

# dic_values를 list로 변환
value_list = list(values)
print(value_list)
print("-" * 30)

# key-value를 쌍으로 묶은 튜플들의 모음인 dict_items 객체 얻기
items = dic.items()
print(items)
print("-" * 30)

lists = list(items)
print(lists)
print("-" * 30)

