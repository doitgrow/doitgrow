# -*- coding: utf-8 -*-

# 원본 리스트
mylist = [5, 3, 7, 1, 9]
print(mylist)

# 리스트의 길이 --> 5
size = len(mylist)

# 리스트의 길이를 2로 나눈 정수 부분의 몫 --> 2
# 리스트의 길이가 홀수인 경우 가운데 원소는 위치 변경이 필요 없으므로
# 나눗셈의 나머지를 버리고 정수부분의 몫만 취한다.
half = size // 2

# 리스트의 반 만큼만 반복 수행 --> 0부터 2전까지
for i in range(0, half):
	# i번째 항목의 반대쪽에 위치한 원소의 인덱스를 구한다.
	p = size - i - 1

	# i번째 원소와 p번째 원소의 값을 맞바꾼다.
	mylist[i], mylist[p] = mylist[p], mylist[i]

# 결과출력
print(mylist)


