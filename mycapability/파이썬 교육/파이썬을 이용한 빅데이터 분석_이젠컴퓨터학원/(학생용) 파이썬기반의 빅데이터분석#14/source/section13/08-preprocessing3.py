# -*- coding: utf-8 -*-

# 모듈 참조, 샘플 데이터프레임 만들기
from print_df import print_df
from pandas import DataFrame
from pandas import Series
from sample import grade_dic

df = DataFrame(grade_dic, index=['철수', '영희', '민철', '수현', '호영'])
print_df(df)



# 새로운 행 추가하기(원본 자체가 수정됨)
# -> 추가될 행의 인덱스 이름을 지정해 준다.
# -> 리스트로 추가할 경우 dataframe의 컬럼 순서에 맞게 지정한다.
# -> 누락되는 값이 있거나 값의 수가 초과될 경우 에러
df.loc['정호'] = [90, 80, 70, 60]
print_df(df)



# -> 딕셔너리 형태로 추가할 경우 컬럼의 순서는 상관 없다.
# -> 누락되는 값이 있거나 값의 수가 초과될 경우 에러
df.loc['민정'] = {'국어': 81, '영어': 72, '수학': 84, '과학': 90}
print_df(df)



# 기존의 행 복사하기
df.loc['철민'] = df.loc['철수']
print_df(df)



# 다른 데이터 프레임을 추가(병합)
# -> 제외된 열에 대해서는 NaN(결측치)로 설정됨
# -> sort: 열을 이름순으로 정렬함(기본값 true)
tmp = DataFrame({'국어': 81, '수학': 84, '과학': 90}, index=["상호"])
new_df = df.append(tmp, sort=False)
print_df(new_df)







