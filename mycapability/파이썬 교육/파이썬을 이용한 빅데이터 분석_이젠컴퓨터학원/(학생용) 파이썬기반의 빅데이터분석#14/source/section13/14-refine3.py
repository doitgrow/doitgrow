# -*- coding: utf-8 -*-

# 모듈 참조
from print_df import print_df
from pandas import DataFrame
from matplotlib import pyplot
from sklearn.impute import SimpleImputer
import numpy

# 데이터를 참조하여 성적표 데이터 프레임 만들기
from sample import grade_dic
df = DataFrame(grade_dic, index=['철수', '영희', '민철', '수현', '호영'])

# 이상치 존재 여부 확인을 위해 상자그림 표시
pyplot.rcParams["font.family"] = 'NanumGothic'
pyplot.rcParams["font.size"] = 14
pyplot.rcParams["figure.figsize"] = (12, 8)
pyplot.figure()
df.boxplot()
pyplot.savefig("refine.png", dpi=300)
pyplot.show()
pyplot.close()




# 국어점수에 대한 이상치 필터링
r = df.query('국어 > 100')
print_df(r)




# 필터링 된 이상치 데이터에 대한 인덱스 추출
r_index = list(r.index)
print_df(r_index)




# 이상치를 갖는 인덱스에 대한 국어 점수를 결측치로 변경
for i in r_index:
    df.loc[i, '국어'] = numpy.nan

print_df(df)




# 결측치를 정제할 규칙 정의 -> 결측치에 대해 평균점수 부여
imr = SimpleImputer(missing_values=numpy.nan, strategy='mean')

# dataframe의 값에 대해 규칙 적용
df_imr = imr.fit_transform(df.values)

# 적용된 규칙으로 새로운 데이터 프레임 생성
re_df2 = DataFrame(df_imr, index=list(df.index), columns=list(df.columns))
print_df(re_df2)
