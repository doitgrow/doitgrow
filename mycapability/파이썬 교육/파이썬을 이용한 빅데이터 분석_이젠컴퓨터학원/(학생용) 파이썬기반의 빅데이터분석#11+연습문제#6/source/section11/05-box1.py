#-*- coding: utf-8 -*-

# 모듈 및 데이터 참조
from matplotlib import pyplot
from sample import newborn
from sample import year

# 한글폰트 설정
pyplot.rcParams["font.family"] = 'NanumGothic'
pyplot.rcParams["font.size"] = 12

# 생성될 결과물의 가로,세로 크기 (inch단위)
pyplot.rcParams["figure.figsize"] = (12, 8)

pyplot.figure()                               # 그래프 설정 시작

# 세로 막대 그래프
# -> 기준축(x축)의 좌표를 저장하는 리스트와 데이터를 저장하는 리스트, 옵션들...
# -> bar() 함수의 기준축은 x방향임
pyplot.bar(year, newborn, label='신생아 수')  # 막대 그래프 표현
pyplot.legend()                               # 범주 표시하기
pyplot.xlabel('년도')                         # 기준축(x축) 라벨
pyplot.ylabel('신생아 수')                    # 데이터(y축) 라벨
pyplot.ylim(350000, 450000)                   # 데이터(y축) 범위
pyplot.title('년도별 신생아 수')              # 그래프 제목
pyplot.grid()                                 # 격자 선 표시

# 그래프의 데이터 수 만큼 반복하면서 텍스트 표시하기
for i, v in enumerate(year):
    # -> 표시할 텍스트
    str_val = "%d명" % newborn[i]

    # -> x축 좌표, y축 좌표, 표시문구, 글자크기, 색상, 가로/세로 정렬
    pyplot.text(v, newborn[i], str_val, fontsize=9, color='#ff6600',
                horizontalalignment='center', verticalalignment='bottom')

pyplot.show()                                 # 그래프 표시하기
pyplot.close()                                # 그래프 관련 설정 해제
