# -*- coding: utf-8 -*-

# 반복가능한 자료형(리스트,튜플,문자열,딕셔너리)의 길이 구하기
# -> 문자열인 경우 각 글자를 리스트의 원소로 변환함.
a = [ 1, 2, 3 ]
size = len(a)
print(size)
print("-" * 30)

# 리스트,튜플 중에서
# 최대값, 최소값, 합계 구하기 -> 문자열은 계산 불가.
a = [ 1, 2, 3 ]
print( max(a) )
print( min(a) )
print( sum(a) )

# 평균을 구하는 기능은 없기 때문에 직접 계산해야 함
avg = sum(a) / len(a)
print(avg)
print("-" * 30)

# 반복 가능한 자료형을 리스트로 변환
# -> 문자열의 경우 글자들의 모음으로 변환함.
a = "Python"
b = list(a)
#b = tuple(a)
print(b)

# -> 튜플을 리스트 혹은 튜플로 변환함
c = (1, 2, 3)
d = list(c)
#d = tuple(c)
print(d)

# -> 리스트를 리스트 혹은 튜플로 변환함
e = [10, 20, 30]
f = list(e)
#f = tuple(e)
print(f)

# -> 딕셔너리일 경우 key만 추려서 리스트 혹은 튜플로 변환하기
g = {"a": 100, "b": 200}
h = list(g.keys())
#h = tuple(g.keys())
print(h)

# -> 딕셔너리일 경우 value만 추려서 리스트 혹은 튜플로 변환하기
i = list(g.values())
#i = tuple(g.values())
print(i)

print("-" * 30)




# 1부터 10전까지 1씩 증가하는 range 객체 생성
k = range(1, 10)
print(type(k))
print(k)
print("-" * 30)

# -> list() 함수를 사용하여 리스트로 변환해서 사용 가능함
mylist = list(k)
print(type(mylist))
print(mylist)
print("-" * 30)

# 1부터 10 전까지 3씩 증가하는 range 객체를 list로 변환
k = list(range(1, 10, 3))
print(k)
print("-" * 30)




# 리스트 자체를 정렬하기
data = [1, 4, 2, 3, 5]
data.sort()
print(data) # 원본 리스트 자체가 정렬됨, 리턴값은 없음

print("-" * 30)

data = [1, 4, 2, 3, 5]
k = sorted(data)
print(data) # 원본은 변화 없음
print(k)    # 정렬된 결과가 리턴됨

print("-" * 30)
