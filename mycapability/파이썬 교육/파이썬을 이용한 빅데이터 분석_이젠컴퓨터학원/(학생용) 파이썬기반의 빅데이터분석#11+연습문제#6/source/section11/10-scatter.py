#-*- coding: utf-8 -*-

from matplotlib import pyplot
from sample import tmp
from sample import qty

# 한글 폰트 설정, 그래픽 크기 설정
pyplot.rcParams["font.family"] = 'NanumGothic'
pyplot.rcParams["font.size"] = 12
pyplot.rcParams["figure.figsize"] = (10, 10)

pyplot.figure()                                   # 그래프 설정 시작

# marker -> o, v, ^, <, >, 8, s, p, *, h, H, D, d, P, X
pyplot.scatter(tmp, qty, color='#ff6600', marker='o', label='판매수량')
pyplot.legend()                                   # 범주 표시
pyplot.grid()                                     # 격자표시
pyplot.title('기온과 아이스크림 판매수량의 관계') # 그래프 제목
pyplot.ylabel('아이스크림 판매수량')              # y축 라벨
pyplot.xlabel('기온')                             # x축 라벨
pyplot.show()                                     # 그래프 표시하기
pyplot.close()                                    # 그래프 관련 설정 해제

