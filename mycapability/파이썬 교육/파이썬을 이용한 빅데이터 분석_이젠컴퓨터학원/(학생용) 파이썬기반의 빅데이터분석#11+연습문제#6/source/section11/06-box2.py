#-*- coding: utf-8 -*-

# 모듈 및 데이터 참조
import numpy
from matplotlib import pyplot
from sample import seoul
from sample import busan
from sample import label

# 한글폰트 설정
pyplot.rcParams["font.family"] = 'NanumGothic'
pyplot.rcParams["font.size"] = 12

# 생성될 결과물의 가로,세로 크기 (inch단위)
pyplot.rcParams["figure.figsize"] = (12, 8)

pyplot.figure()                                # 그래프 설정 시작


# 막대그래프 기준축에 대한 좌표를 표현한 배열 생성 (0~11)
x = numpy.arange(len(label))
print(x)

# 기준축(x축)의 좌표와 굵기를 설정한 막대그래프
# -> numpy 배열 자체에 숫자 연산을 수행하면 배열의 모든 원소에
pyplot.bar(x-0.2, seoul, label='서울', width=0.4, color='#ff6600')
pyplot.bar(x+0.2, busan, label='부산', width=0.4, color='#0066ff')

pyplot.xticks(x, label)    # 기준축(x축)의 라벨은 별도로 지정함

pyplot.legend()                                # 범주 표시하기
pyplot.xlabel('월')                            # 기준축(x축) 라벨
pyplot.ylabel('교통사고 수')                   # 데이터(y축) 라벨
pyplot.ylim(0,4000)                            # 데이터(y축) 범위
pyplot.title('2017년 서울,부산 교통사고 현황') # 그래프 제목

pyplot.show()                                  # 그래프 표시하기
pyplot.close()                                 # 그래프 관련 설정 해제

