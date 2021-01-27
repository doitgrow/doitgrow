# -*- coding: utf-8 -*-

# 모듈 참조
from print_df import print_df
from pandas import DataFrame
from matplotlib import pyplot
import numpy

#---------------------------------------------------
# 데이터 수집 -> 데이터를 참조하여 데이터 프레임 만들기
#---------------------------------------------------
from sample import traffic
df = DataFrame(traffic)
print_df(df)

#---------------------------------------------------
# 데이터 전처리
#---------------------------------------------------
# `월`에 대한 컬럼만 리스트로 추출
month = list(df['month'])

# 빈 딕셔너리 생성
new_name = {}

# `월`리스트에 대해 반복
for i, v in enumerate(month):
    # 딕셔너리에 {인덱스번호: 값} 형식으로 채워넣음
    new_name[i] = v

# 데이터프레임의 인덱스 변경
df.rename(index=new_name, inplace=True)

# 기존의 `월`컬럼은 삭제
df.drop('month', axis=1, inplace=True)

# 결과확인
print_df(df)


#---------------------------------------------------
# 상자그림
#---------------------------------------------------
# 한글폰트, 그래픽 크기 설정
pyplot.rcParams["font.family"] = 'NanumGothic'
pyplot.rcParams["font.size"] = 15
pyplot.rcParams["figure.figsize"] = (15, 10)

pyplot.grid()
# 컬럼 이름을 파라미터로 전달하여 특정 컬럼에 대해서만 생성
df.boxplot('seoul')
pyplot.title("2017년 교통사고 변화")
pyplot.ylabel("교통사고 수")
#pyplot.savefig('boxplot1.png', dpi=200)
pyplot.show()
pyplot.close()


pyplot.grid()
# 컬럼 이름의 리스트를 파라미터로 전달하여 복수 컬럼에 대해서만 생성
df.boxplot(['inchun', 'busan'])
pyplot.title("2017년 교통사고 변화")
pyplot.ylabel("교통사고 수")
#pyplot.savefig('boxplot2.png', dpi=200)
pyplot.show()
pyplot.close()


pyplot.grid()
# 파라미터가 없을 경우 전체 컬럼에 대한 생성
df.boxplot()
pyplot.title("2017년 교통사고 변화")
pyplot.ylabel("교통사고 수")
#pyplot.savefig('boxplot3.png', dpi=200)
pyplot.show()
pyplot.close()


#---------------------------------------------------
# 데이터 시각화(1) - 선 그래프
#---------------------------------------------------
# 그래프의 x좌표를 위해 미리 준비해 둔 `월`리스트의 길이만큼 배열생성
x = numpy.arange(len(month))

# 특정 컬럼에 대해서만 시각화 하기
df['seoul'].plot()
pyplot.grid()
pyplot.legend()
pyplot.title("2017년 월별 교통사고 변화")
pyplot.ylabel("교통사고 수")
pyplot.xticks(x, month)
pyplot.xlim(0, 11)
#pyplot.savefig('plot1.png', dpi=200)
pyplot.show()
pyplot.close()

# 전체 컬럼 시각화 하기
df.plot()
pyplot.grid()
pyplot.legend()
pyplot.title("2017년 월별 교통사고 변화")
pyplot.ylabel("교통사고 수")
pyplot.xticks(x, month)
pyplot.xlim(0, 11)
#pyplot.savefig('plot2.png', dpi=200)
pyplot.show()
pyplot.close()


#---------------------------------------------------
# 데이터 시각화(2) - 막대 그래프
#---------------------------------------------------
# 특정 컬럼에 대한 시각화
df['seoul'].plot.bar()
pyplot.grid()
pyplot.title("2017년 서울의 월별 교통사고 변화")
pyplot.ylabel("교통사고 수")
# -> x축의 라벨은 선 그래프와 동일하게 처리
pyplot.xticks(x, month)
#pyplot.savefig('bar1.png', dpi=200)
pyplot.show()
pyplot.close()


# 전체 컬럼에 대한 시각화
df.plot.bar()
pyplot.grid()
pyplot.title("2017년 주요도시의 월별 교통사고 변화")
pyplot.legend()
pyplot.ylabel("교통사고 수")
# -> x축의 라벨은 선 그래프와 동일하게 처리
pyplot.xticks(x, month)
#pyplot.savefig('bar2.png', dpi=200)
pyplot.show()
pyplot.close()

#---------------------------------------------------
# 데이터 시각화(3) - 산점도 그래프
#---------------------------------------------------
# 산점도 그래프는 두 컬럼(변수)간의 관계를 분석하기 위해 사용된다.
df.plot.scatter(x='seoul', y='busan')
pyplot.grid()
pyplot.title("서울과 부산의 교통사고량 관계")
pyplot.savefig('scatter.png', dpi=200)
pyplot.show()
pyplot.close()


#---------------------------------------------------
# 데이터 시각화(4) - 파이 그래프
#---------------------------------------------------
# 각 컬럼별로 합계 구하기 --> 도시별 1년간의 교통사고량
total = df.sum()
print_df(total)

# 구해진 합계를 사용해서 데이터프레임 생성
total_df = DataFrame(total, columns=['교통사고'])
print_df(total_df)

# 데이터프레임의 특정 컬럼에 대한 파이그래프 표시
total_df['교통사고'].plot.pie(autopct='%0.1f%%')
pyplot.title("2017년 주요도시의 교통사고 비율")
#pyplot.savefig('pie.png', dpi=200)
pyplot.show()
pyplot.close()






