# -*- coding: utf-8 -*-

from pandas import DataFrame 	# 모듈 참조
from sample import grade_dic	# 데이터 참조

df = DataFrame(grade_dic, index=['철수', '영희', '민철', '수현', '호영'])

# 행과 열의 개수를 튜플로 반환
print( df.shape )
print("-" * 30)

# 전체에 대한 처음 2줄만 추출 -> 파라미터가 없을 경우 5줄이 기본
top = df.head(2)
print(top)
print("-" * 30)

# 특정 열에 대한 처음 2줄
print(df['영어'].head(2))
print("-" * 30)

# 마지막 2줄만 보기 -> 파라미터가 없을 경우 5줄이 기본
button = df.tail(2)
print(button)
print("-" * 30)

# 특정 열에 대한 마지막 2줄
print(df['영어'].tail(2))
print("-" * 30)


# 전체 요약정보 가져오기
des = df.describe()

# -> 요약정보의 타입은 DataFrame
print(type(des))

# -> 요약정보 출력하기
print(des)
print("-" * 30)

# 특정 열에 대한 요약정보 보기
print(df['영어'].describe())
print("-" * 30)



# 요약정보의 개별 조회
# -> 각 열, 혹은 특정 열에 대해 NA를 제외한 값의 수를 반환
print(df.count())
print("-" * 30)
print(df['영어'].count())
print("-" * 30)

# -> 최소값
print(df.min())
print("-" * 30)
print(df['영어'].min())
print("-" * 30)

# -> 최대값
print(df.max())
print("-" * 30)
print(df['영어'].max())
print("-" * 30)

# -> 합계
print(df.sum())
print("-" * 30)
print(df['영어'].sum())
print("-" * 30)

# -> 평균
print(df.mean())
print("-" * 30)
print(df['영어'].mean())
print("-" * 30)

# -> 표준편차
print(df.std())
print("-" * 30)
print(df['영어'].std())
print("-" * 30)

# -> 중앙값 (2사분위수)
print(df.median())
print("-" * 30)
print(df['영어'].median())
print("-" * 30)

# -> 사분위 수 (중앙값 : 50% 위치의 값)
print(df.quantile(q=0.5))
print("-" * 30)
print(df['영어'].quantile(q=0.5))
print("-" * 30)

# -> 1사분위 수 (25% 위치의 값)
print(df.quantile(q=0.25))
print("-" * 30)

# -> 3사분위 수 (75% 위치의 값)
print(df.quantile(q=0.75))
print("-" * 30)

# 사분위 수 이외의 위치 추출
# -> 90% 위치의 값 = 상위 10%
print(df.quantile(q=0.9))
print("-" * 30)
