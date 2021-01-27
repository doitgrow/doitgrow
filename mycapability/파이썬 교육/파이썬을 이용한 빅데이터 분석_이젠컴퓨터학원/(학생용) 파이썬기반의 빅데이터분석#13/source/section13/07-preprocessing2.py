# -*- coding: utf-8 -*-

# 모듈, 데이터 참조
from pandas import DataFrame
from sample import grade_dic
# -> print_df.py 파일에서 print_df 함수 import
from print_df import print_df

# 데이터프레임 생성
df = DataFrame(grade_dic, index=['철수', '영희', '민철', '수현', '호영'])
print_df(df)


# 특정 열로 오름차순(순차정렬) 정렬
# -> inplace=True 인 경우 원본 자체를 정렬함
# -> inplace=False 인 경우 정렬된 결과를 리턴하고 원본은 변화 없음(기본값)
df.sort_values('국어', inplace=True)
print_df(df)


# 특정 열로 내림차순 정렬
# ascending=False 내림차순
# ascending=True 오름차순 (기본값)
df.sort_values('국어', inplace=True, ascending=False)
print_df(df)


# 두 개 이상의 열로 정렬할 경우 리스트로 설정
# -> 국어 점수가 동일할 경우 수학점수 순으로 정렬된다.
df.sort_values(['국어', '수학'], inplace=True)
print_df(df)


# 특정 조건이 맞는 행 조회
r1 = df.query('국어 > 80')
print_df(r1)


# 다중조건에 맞는 행 조회(1) -> And
r2 = df.query('국어 > 80 and 수학 > 80')
print_df(r2)


# 다중조건에 맞는 행 조회(2) -> Or
r3 = df.query('국어 < 70 or 수학 < 70')
print_df(r3)
