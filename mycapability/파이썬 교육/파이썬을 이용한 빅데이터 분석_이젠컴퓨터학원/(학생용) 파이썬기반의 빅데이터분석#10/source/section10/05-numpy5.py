# -*- coding: utf-8 -*-
"""
05-numpy5.py > 2차원 배열
    기본적으로 모든 기능은 1차배열인 경우와 동일하게 적용되고
    추가적인 기능이 있다.
"""
# 모듈 가져오기
# -> pip3 install numpy
import numpy

# 철수의 학년-과목별 점수
grade = numpy.array([
    # 열 ->   0   1   2   3
            [98, 72, 80, 64],   # 0행 - kor
            [88, 90, 80, 72],   # 1행 - eng
            [92, 88, 82, 76]    # 2행 - math
        ])
print(grade)
print("-" * 30)


# 배열 정보
# -> 차원 크기
print( "차원크기: %d" % grade.ndim )
# -> 각 차원의 원소수 튜플로 표시한 것.
print( grade.shape )
# -> 각 원소의 타입
print( grade.dtype )


# 각 열끼리 더함 (세로로 덧셈) -> 결과 타입은 numpy의 1차 배열
s1 = numpy.sum(grade, axis=0)
print(type(s1))
print(s1)
print("-" * 30)

# 각 행끼리 더함 (가로로 덧셈)
s2 = numpy.sum(grade, axis=1)
print(type(s2))
print(s2)
print("-" * 30)


# 정수형 인덱싱
# -> 1행 2열의 데이터 접근 = 80
print(grade[1,2])
print("-" * 30)

# bool 형 인덱싱
# -> 추출하고자 하는 원본과 같은 사이즈의 배열
# -> 추출할 값은 True, 그렇지 않으면 False
bool_array = numpy.array([
            [True, False, True, False],
            [True, True, True, False],
            [True, True, True, False]
        ])

# 조건에 맞는 항목만 1차 배열로 추출
result1 = grade[bool_array]
print(result1)
print("-" * 30)

# 80점 이상인지 판별하여 조건에 맞는 데이터만 추려냄
# -> 추출된 결과는 1차 배열
result2 = grade[grade >= 80]
print(result2)
print("-" * 30)

# logical_and 함수를 사용하여 80점 이상이고 90점 이하인 데이터만 추려냄
result3 = grade[numpy.logical_and(grade >= 80, grade <= 90)]
print(result3)
print("-" * 30)

# logical_or 함수를 사용하여 80점 미만이거나 90점 초과인 데이터만 추려냄
result4 = grade[numpy.logical_or(grade < 80, grade > 90)]
print(result4)
print("-" * 30)

# 슬라이싱
# -> 1~3행 전까지,1~4열 전까지 범위를 추출
print(grade[1:3, 1:4])
print("-" * 30)

# -> 0~2행 전까지, 0~3열 전까지 범위를 추출
print(grade[:2, :3])
print("-" * 30)

# -> 1~끝행, 2~끝열 범위를 추출
print(grade[1:, 2:])
print("-" * 30)
