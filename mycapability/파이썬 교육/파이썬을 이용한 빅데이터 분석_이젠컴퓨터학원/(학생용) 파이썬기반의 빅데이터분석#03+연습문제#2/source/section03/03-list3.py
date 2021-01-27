# -*- coding: utf-8 -*-

mylist = [ 10, 20, 30, 40, 50 ]

# 1번째 원소에 접근 -> 0부터 카운트
print(mylist[1])

# 뒤에서 1번째 원소에 접근 -> 1부터 카운트
print(mylist[-1])

# list에서 1번째 부터 3번째 전까지 -> 3번째 원소 포함안됨
print(mylist[1:3])

# 처음부터 3번째 전까지 -> 3번째 원소 포함안됨
print(mylist[:3])

# list[3]부터 끝까지 -> 3번째 원소 포함됨
print(mylist[3:])

# list의 모든 원소
print(mylist[:])

# list에서 1번째부터 뒤에서 부터 2번째 다음까지
# -> 마이너스 값을 사용하여 지정할 경우 "다음까지"의 의미
print(mylist[1:-2])


