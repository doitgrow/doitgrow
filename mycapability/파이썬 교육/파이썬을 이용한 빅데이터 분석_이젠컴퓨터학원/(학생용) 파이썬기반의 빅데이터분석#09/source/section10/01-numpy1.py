# -*- coding: utf-8 -*-

# 모듈 가져오기
# -> pip install numpy
import numpy

# 리스트를 통한 1차원(=1행으로 구성) 배열 만들기
arr = [1, 2, 3]
print(arr)

a = numpy.array(arr)
print(a)
print("-" * 30)

# 서로 다른 타입의 원소를 갖는 list만들기
# -> 파이썬의 리스트는 서로 다른 타입 허용
arr2 = [1.2, 3, '4']
print(arr2)
print("-" * 30)

# 정수와 실수가 섞인 리스트를 배열로 변환
# -> 배열은 원소의 타입이 서로 다른것을 허용하지 않음
# -> 가장 포괄적인 형태의 자료형으로 통일함
# -> 여기서는 실수가 범위가 더 크므로 모든 원소가 실수형으로 변환됨
b = numpy.array( [1, 2.4, 3, 4.6] )
print(b)
print("-" * 30)

# 정수,실수,문자열이 포함된 리스트를 배열로 변환
# -> 모든 타입이 문자열로 변환되어 있음
c = numpy.array([1.2, 3, '4'])
print(c)
print("-" * 30)

# 모든 원소의 타입을 강제로 int(정수)로 지정
# -> 소수점 아래 값들은 모두 버려진다.
d = numpy.array( [1, 2.4, 3, 4.6], dtype='int' )
print(d)
print("-" * 30)

# 배열의 크기와 각 원소에 접근하기
# -> 내장함수 len()은 모든 연속성 데이터(문자열,리스트,튜플 등)에 사용 가능
arr3 = numpy.array([1,3,5,7,9])
size = len(arr3)
print("배열의 원소는 %d개 입니다." % size)

# 배열의 원소에 접근하기
#-> 리스트와 마찬가지로 각 원소에 인덱스 번호로 접근 가능.
print(arr3[0])
print(arr3[1])
print(arr3[3])
print("-" * 30)

# 인덱스가 있기 때문에 반복문을 통해서 제어할 각 원소에 접근 가능
for i, v in enumerate(arr3):
	print("%d번째 원소 >> %d" % (i, v))




