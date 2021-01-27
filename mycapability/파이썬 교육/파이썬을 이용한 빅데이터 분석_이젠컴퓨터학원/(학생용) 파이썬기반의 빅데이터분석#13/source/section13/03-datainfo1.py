# -*- coding: utf-8 -*-

from pandas import DataFrame 	# 모듈 참조
from sample import grade_dic	# 데이터 참조

# 데이터 구성하기
df = DataFrame(grade_dic, index=['철수', '영희', '민철', '수현', '호영'])
print(df)
print("-" * 30)


# 열 단위의 데이터에 접근하기
# --> 1) 열을 기준으로 데이터 타입 확인
print( df.dtypes )
print("-" * 30)

# --> 2) 열을 기준으로 데이터 값 확인
print(df['국어'])
print("-" * 30)

# --> 3) 열의 값들을 numpy 배열로 추출
arr = df['국어'].values
print( type(arr) )
print( arr )
print("-" * 30)

# --> 4) 열의 값들을 list로 추출
ls = list(df['국어'])
print( type(ls) )
print( ls )
print("-" * 30)


# 행 단위로 접근하기
# --> 1) 하나의 행에 속한 모든 데이터 추출
cs = df.loc['철수']
print(cs)

# Series로 리턴됨. 즉 데이터프레임은 시리즈의 모음
print(type(cs))
print("-" * 30)

# --> 2) 행의 값들을 numpy 배열로 추출
arr = cs.values
print( type(arr) )
print( arr )
print("-" * 30)

# --> 3) 행의 값들을 numpy list로 추출
ls = list(cs)
print( type(ls) )
print( ls )
print("-" * 30)



# 하나의 열에 속한 특정 행의 값 추출하는 다양한 방법
# -> 열 > 행의 순으로 접근
print("철수의 국어 점수: %d" % df['국어']['철수'])

# -> 행 > 열의 순으로 접근하는 방법(권장)
print("영희의 수학 점수: %d" % df.loc['영희','수학'])
print("-" * 30)


# 특정 값 변경하기 -> 행 우선 접근 방법으로만 가능
df.loc['철수','국어'] = 99
print("철수의 국어 점수(변경): %d" % df.loc['철수','국어'])
print("-" * 30)




# dataframe에서 인덱스(=행)이름만 추출하기
print( df.index )			# -> 객체형식
print( list(df.index) ) 	# -> 리스트로 변환
print("-" * 30)

# dataframe에서 컬럼(=열)이름만 추출하기
print( df.columns )			# -> 객체형식
print( list(df.columns) )	# -> 리스트로 변환
print("-" * 30)

# dataframe에서 값만 추출하기
# -> 2차원 배열(numpy객체)로 추출됨
print(type(df.values))
print( df.values )
print("-" * 30)

# 전치 구하기
# -> 가로와 세로가 바뀐 형태
df_t = df.T
print(df_t)
print("-" * 30)

