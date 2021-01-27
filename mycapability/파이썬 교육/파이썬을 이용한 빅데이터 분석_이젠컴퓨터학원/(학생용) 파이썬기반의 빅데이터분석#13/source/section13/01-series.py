# -*- coding: utf-8 -*-

# pandas모듈에서 Series 클래스 가져오기
from pandas import Series

# 기본 시리즈 만들기
# -> 리스트를 통해 만들 수 있다.
# -> 즉 리스트 자료형을 가공하여 생성된 데이터 구조.
items = [10,30,50,70,90]
column = Series(items)

# 전체 확인
print(column)
print("-" * 30)

# -> 인덱스를 활용한 개별 값 확인
print(column[0])
print(column[2])
print(column[4])
print("-" * 30)

# 시리즈의 값들만 추출
print( column.values )
print("-" * 30)

# 타입을 확인하면 Numpy 배열임을 알 수 있다.
print(type(column.values))
print("-" * 30)

# -> 시리즈의 값들을 저장하고 있는 numpy 배열을 list로 변환
value_list = list(column.values)
print( value_list )
print("-" * 30)

# 시리즈의 색인(index)만 추출
print( column.index )
print("-" * 30)

# 색인들의 타입 확인
print(type(column.index))

# 시리즈의 색인(index)을 list로 변환
print( list(column.index) )
print("-" * 30)



# 특정 조건에 맞는 항목들만 추출
# -> 이름[이름에 대한 조건식]
# -> 30초과인 항목들만 추출
in1 = column[column > 30]
print(type(in1))
print(in1)
print("-" * 30)

# -> 7이하 and 1초과인 항목들만 추출
in2 = column[column <= 70][column > 10]
print(type(in2))
print(in2)
print("-" * 30)

# -> 10이하 or 70이상인 항목들만 추출 -> ()필수
in3 = column[(column <= 10) | (column >= 70)]
print(type(in3))
print(in3)
print("-" * 30)


# 인덱스를 직접 지정하면서 시리즈 만들기
# -> 지난주 주말에 대한 매출액
week1 = Series([290000, 310000], index=['sat', 'sun'])
# -> 이번주 주말에 대한 매출액
week2 = Series([120000, 220000], index=['sun','sat'])

print( week1 )
print("-" * 30)

print( week2 )
print("-" * 30)

# 시리즈 객체의 사칙연산
# -> index가 동일한 항목끼리 연산이 수행된다.
merge = week1 + week2
print(merge)


