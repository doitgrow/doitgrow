# -*- coding: utf-8 -*-

# 모듈 참조
from print_df import print_df
from pandas import DataFrame
from matplotlib import pyplot
import numpy


# 데이터를 참조하여 데이터 프레임 만들기
from sample import city_people
df = DataFrame(city_people)
print_df(df)

# 각 도시별 연도에 따른 인구수
pv1 = df.pivot('도시', '연도', '인구')
print_df(pv1)

# 행이나 열에 대한 값들 중 중복된 값들이 있는 경우 에러 발생
# -> 그러므로 아래의 코드는 에러가 발생함
#pv2 = df.pivot('지역', '연도', '인구')
#print_df(pv2)




지역별인구수 = df.groupby(df['지역']).sum()
print_df(지역별인구수)




연도별인구수 = df.groupby(df['연도']).sum()
print_df(연도별인구수)




지역_연도별_평균인구 = df.groupby( [ df['지역'], df['연도'] ] ).mean()
print_df(지역_연도별_평균인구)


