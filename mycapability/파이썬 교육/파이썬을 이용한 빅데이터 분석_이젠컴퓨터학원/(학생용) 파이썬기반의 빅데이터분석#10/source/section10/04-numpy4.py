# -*- coding: utf-8 -*-
"""
04-numpy3.py > 배열의 인덱싱, 슬라이싱
"""
# 모듈 가져오기
import numpy

# 철수의 1학년~4학년까지의 평균 점수
grade = numpy.array([82, 77, 91, 88])
print(grade)
print("-" * 30)

# 인덱싱
# -> 2열(0부터 카운트)의 데이터 접근
print(grade[2])
print("-" * 30)

# bool 형 인덱싱
# -> 추출하고자 하는 원본과 같은 사이즈의 배열을 생성한다.
# -> 추출할 값은 True, 그렇지 않으면 False
bool_array = numpy.array([True, False, True, False])

# -> 조건에 맞는 항목만 1차 배열로 추출
result1 = grade[bool_array]
print(result1)
print("-" * 30)

# 80점 이상인지 판별된 조건에 맞는 데이터만 추려냄
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
# -> 1열부터 3열 전까지 범위를 추출
print(grade[1:3])
print("-" * 30)

# -> 처음부터 2열 전까지 범위를 추출
print(grade[:2])
print("-" * 30)

# -> 1열~끝까지 범위를 추출
print(grade[1:])
print("-" * 30)
