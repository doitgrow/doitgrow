# -*- coding: utf-8 -*-

# 원본 리스트
mylist = [5, 3, 7, 1, 9]
print(mylist)

# 리스트의 길이
size = len(mylist)

# 처음부터 뒤에서 두 번째것 까지만 반복
for i in range(0, size-1):
	# i번째 다음부터 끝까지 반복
	for j in range(i+1, size):
		# i번째가 j번째보다 값이 크다면
		if mylist[i] > mylist[j]:
			# 두 원소를 맞바꿈
			mylist[i], mylist[j] = mylist[j], mylist[i]

# 결과 출력
print(mylist)


