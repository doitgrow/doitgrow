# -*- coding: utf-8 -*-

# 딕셔너리 정의하기
# -> 이름(key)과 값(value)가 쌍을 이루는 자료구조
dic = { "name": "철수", "phone": "010-1234-5678", "birth": "0115" }
print( dic )
print("-" * 30)

# 특정 원소에 접근하기 -> 직접 출력
print( dic["name"] )
print("-" * 30)

# 특정 원소에 접근하기 -> 다른 변수에 복사
phone = dic["phone"]
print(phone)
print("-" * 30)




# 특정 원소의 값을 변경
dic["name"] = "호영"
print( dic["name"] )
print("-" * 30)

# 존재하지 않는 키의 값을 사용하면 에러
#print( dic["weight"] )

# 존재하지 않는 키에 값을 할당하면 확장
dic["height"] = 175
print( dic )
print("-" * 30)

# -> key가 birth인 데이터 삭제
del(dic["birth"])
print(dic)
print("-" * 30)


# 키가 중복될 경우 하나를 제외한 나머지는 무시됨.
# -> 일반적으로 나중에 정의된 항목이 이전에 정의된 항목을 덮어 씀
data = {"msg": "hello", "msg": "world", "msg": "python"}
print(data['msg'])
print("-" * 30)

# 딕셔너리는 리스트와 다르게 자료의 순서가 중요하지 않다.
# key는 정수형으로도 지정 가능
rank = {0: "Python", 30: "R", 10: "Java"}
print(rank[0])
print(rank[30])
print(rank[10])
print("-" * 30)



