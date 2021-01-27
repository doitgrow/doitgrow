# -*- coding: utf-8 -*-

# 모듈 참조
from print_df import print_df
from pandas import read_csv
from pandas import DataFrame
from sklearn.preprocessing import Imputer
import numpy
import datetime as dt
from matplotlib import pyplot

#---------------------------------------------------------
# 데이터 수집
#---------------------------------------------------------
# csv 파일은 저장시에 설정한 인코딩 타입을 명시해야 함
df = read_csv('data/grade.csv', encoding='euc-kr')

# 상위 5건 확인
print_df( df.head(5) )

#---------------------------------------------------------
# 데이터 전처리
#---------------------------------------------------------
# 이름에 대한 열을 리스트로 추출
student_list = list(df['이름'])
print_df(student_list)

# 원본의 인덱스 리스트와 이름의 리스트를 결합하여 딕셔너리 구조 생성
index_dict = {}
for i, v in enumerate(student_list):
    index_dict[i] = v

print_df(index_dict)

# 원본에서는 이름에 대한 열을 제거하고 인덱스 이름 변경
df.drop('이름', axis=1, inplace=True)
df.rename(index=index_dict, inplace=True)
print_df( df.head(5) )


#---------------------------------------------------------
# 데이터 정제
#---------------------------------------------------------
# 열별로 결측치의 수를 파악
print_df(df.isnull().sum())

# 결측치를 정제할 규칙 정의 -> nan값을 평균으로 대체
imr = Imputer(missing_values=numpy.nan, strategy='mean')

# dataframe의 값에 대해 규칙이 적용된 2차 배열 생성
df_imr = imr.fit_transform(df.values)

# 2차 배열로 새로운 데이터 프레임 생성
# -> 인덱스 이름과 컬럼 이름은 기존것을 재사용
df = DataFrame(df_imr, index=list(df.index), columns=list(df.columns))

# -> 열별로 결측치의 수를 파악
print_df(df.isnull().sum())

# 평균 점수에 대한 열 추가하기
df['평균'] = df.mean(axis=1)

# 평균에 따른 학점을 부여하기 위한 점수구간을 설정하는 조건들을 리스트로 설정
conditions = [  (df['평균'] >= 90),   # A
                (df['평균'] >= 80),   # B
                (df['평균'] >= 70),   # C
                (df['평균'] < 70) ]   # F

# 조건에 따라 부여될 학점
grade = [ 'A', 'B', 'C', 'F' ]

# 조건에 따른 학점열 추가하기
df['학점'] = numpy.select(conditions, grade)
print_df( df.head(5) )

quit()

#---------------------------------------------------------
# 생성 결과를 CSV로 저장하기
#---------------------------------------------------------
# 현재시각을 기반으로 저장할 파일의 이름 만들기
now_time = dt.datetime.now().strftime("%y%m%d_%H%M%S")
filename = "grade_" + now_time + ".csv"

# 데이터 프레임을 csv로 저장
# encoding -> 파일인코딩(기본값=utf-8)
# na_rep      -> 결측치를 표시할 문자열 (기본값=빈문자열)
# index_label -> 인덱스에 표시될 제목 (기본값=빈문자열)
# index       -> False로 지정할 경우 index는 저장안함 (여기서는 사용하지 않음)
# header      -> 각 컬럼의 제목으로 사용될 문자열 리스트 #(기본값=데이터프레임의 컬럼명)
df.to_csv(filename, encoding='euc-kr', na_rep='NaN',
	     index_label='이름', header=['국','영','수','과','평균','학점'])

#---------------------------------------------------------
# 데이터 시각화
#---------------------------------------------------------
# 학점에 대한 빈도수 계산결과를 새로운 데이터프레임으로 생성
cnt = df['학점'].value_counts()
result_df = DataFrame(cnt)
print_df(result_df)

# 생성된 데이터 프레임의 컬럼이름 수정
result_df.rename(columns={'학점': '학생수'}, inplace=True)
print_df(result_df)

# 그래프 만들기
pyplot.rcParams["font.family"] = 'NanumGothic'
pyplot.rcParams["font.size"] = 14
pyplot.rcParams["figure.figsize"] = (12, 8)

# 데이터프레임을 그래프로 저장하기
result_df.plot.bar()
pyplot.grid()
pyplot.legend()
pyplot.title('학점 분포도')
pyplot.xlabel('학점')
pyplot.savefig('grade.png', dpi=200)
pyplot.show()
pyplot.close()
