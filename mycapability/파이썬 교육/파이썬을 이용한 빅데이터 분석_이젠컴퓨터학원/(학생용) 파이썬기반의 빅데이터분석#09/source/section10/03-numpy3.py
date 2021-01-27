# -*- coding: utf-8 -*-

# 모듈 가져오기
import numpy

# 예제를 위한 배열 구성
grade = numpy.array([82, 77, 91, 88])
print(grade)
print("-" * 30)

# 모든 원소에 대한 사칙연산 수행
#-> 모든 원소에 대하여 2씩 더함
new1 = grade + 2
print(new1)
print("-" * 30)

#-> 모든 원소에 대하여 5씩 뺌
new2 = grade - 5
print(new2)
print("-" * 30)

# 연산자를 사용한 배열간의 연산 => 위치가 동일한 각 원소끼리 수행된다.
arr1 = numpy.array([10,15,20,25,30])
arr2 = numpy.array([2,3,4,5,6])
print(arr1)
print(arr2)
print("-" * 30)

a = arr1 + arr2
print(a)
print("-" * 30)

b = arr1 - arr2
print(b)
print("-" * 30)

c = arr1 * arr2
print(c)
print("-" * 30)

d = arr1 / arr2
print(d)
print("-" * 30)


# numpy모듈의 함수를 사용한 배열간의 연산 => 연산자와 동일한 결과
arr1 = numpy.array([10,15,20,25,30])
arr2 = numpy.array([2,3,4,5,6])
print(arr1)
print(arr2)
print("-" * 30)

a = numpy.add(arr1, arr2)
print(a)
print("-" * 30)

b = numpy.subtract(arr1, arr2)
print(b)
print("-" * 30)

c = numpy.multiply(arr1, arr2)
print(c)
print("-" * 30)

d = numpy.divide(arr1, arr2)
print(d)
print("-" * 30)



grade = numpy.array([82, 77, 91, 88])

# 모든 원소의 합
s1 = numpy.sum(grade)
print("총점: %d" % s1)

# 모든 원소의 평균
s2 = numpy.average(grade)
print("평균 : %d" % s2)

# 최대, 최소값
s3 = numpy.max(grade)
s4 = numpy.min(grade)
print("최대값 : %d, 최소값: %d" % (s3, s4) )
