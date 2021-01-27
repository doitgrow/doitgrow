# -*- coding: utf-8 -*-

# 모듈 가져오기
import numpy

# 0부터 15전까지 순차적으로 증가하는 값들을 원소로 갖는 배열
# -> 시작값이 무조건 0부터 시작됨
a = numpy.arange(15)
print(a)
print("-" * 30)

# 100~115전까지 순차적으로 증가하는 값들을 원소로 갖는 배열
b = numpy.array(range(100,115))
print(b)
print("-" * 30)

# 모든 원소가 실수형 0인 1행 3열 배열 생성
c = numpy.zeros( [3] )
print(c)
print("-" * 30)

# 모든 원소가 정수형 0인 1행 4열 배열 생성
# -> dtype을 지정하지 않을 경우 기본값은 float(실수)
d = numpy.zeros( [4], dtype='int' )
print(d)
print("-" * 30)

# 모든 원소가 실수형 1인 1행 3열 배열
e = numpy.ones([3])
print(e)
print("-" * 30)

# 모든 원소가 정수형 1인 1행 4열 배열
# -> dtype을 지정하지 않을 경우 기본값은 float(실수)
f = numpy.ones([4], dtype='int')
print(f)
print("-" * 30)

# 모든 원소가 정수형 7인 1행 5열 배열
g = numpy.full( [5], 7)
print(g)
print("-" * 30)

# 모든 원소가 실수형 7인 1행 4열 배열
# -> 주의: dtype은 생략할 경우 "int"
h = numpy.full( [4], 7, dtype='float')
print(h)
print("-" * 30)
