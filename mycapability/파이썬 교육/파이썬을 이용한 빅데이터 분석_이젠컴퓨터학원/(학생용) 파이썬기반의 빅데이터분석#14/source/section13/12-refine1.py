# -*- coding: utf-8 -*-

# 모듈 및 샘플 데이터 참조
from print_df import print_df
from pandas import DataFrame
from sample import grade_dic

df = DataFrame(grade_dic, index=['철수', '영희', '민철', '수현', '호영'])
print_df(df)



# 결측치 여부 확인
# -> 각 열에 대해 결측치가 아닐 경우 False, 결측치는 True로 표시됨
# -> isna() 함수도 같은 기능
empty = df.isnull()
print_df(empty)



# 결측치의 수를 파악하기 위해 각 열별로 합계 도출
# -> True에 대해서만 카운팅
empty_sum = empty.sum()
print_df(empty_sum)



# 결측치가 있는 모든 행 삭제 (원본은 변화 없음, 삭제결과 리턴됨)
na1 = df.dropna()

# -> 결측치가 삭제된 데이터 프레임 확인
print_df(na1)

# -> 결측치 값 갯수 확인
print_df(na1.isnull().sum())





# 결측치가 있는 모든 열 삭제
na2 = df.dropna(axis=1)

# -> 결측치가 삭제된 데이터 프레임 확인
print_df(na2)

# -> 결측치 값 갯수 확인
print_df(na2.isnull().sum())





# 행의 모든 값이 결측치면 행을 삭제
na3 = df.dropna(how='all')
print_df(na3)




# 열의 모든 값이 결측치면 열을 삭제
na4 = df.dropna(how='all', axis=1)
print_df(na4)




