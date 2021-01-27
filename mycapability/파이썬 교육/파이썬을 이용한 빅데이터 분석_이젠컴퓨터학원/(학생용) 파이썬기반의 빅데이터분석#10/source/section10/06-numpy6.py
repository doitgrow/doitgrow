# -*- coding: utf-8 -*-
"""
06-numpy6.py > 정형화된 2차 배열 생성하기
"""
# 모듈 가져오기
# -> pip3 install numpy
import numpy

# 1차원 배열을 2차원으로 변환
# -> 칸을 구성하기에 'e'의 원소수가 부족하다면 에러
tmp = numpy.arange(12)
print(tmp)

a = tmp.reshape(3, 4)
print(a)
print("-" * 30)

# `a`배열의 전치행렬 구하기
# -> 행의 수와 열의 수가 바뀐 형태
# -> ex) 3행 5열의 전치는 5행 3열
b = numpy.transpose(a)
print(b)
print("-" * 30)

# 3x3의 단위행렬 생성
# -> (0,0)위치부터 오른쪽 대각선으로 1로 채워지고 그 밖의 값들은 0
# -> dtype은 생략할 경우 int
c = numpy.eye(3, dtype="float")
print(c)
print("-" * 30)


