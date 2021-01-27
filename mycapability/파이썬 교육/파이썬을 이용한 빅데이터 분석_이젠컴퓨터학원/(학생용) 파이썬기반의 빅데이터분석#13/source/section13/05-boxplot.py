# -*- coding: utf-8 -*-

from pandas import DataFrame 	# 모듈 참조
from matplotlib import pyplot	# 모듈 참조
from sample import grade_dic	# 데이터 참조

df = DataFrame(grade_dic, index=['철수', '영희', '민철', '수현', '호영'])

# 한글폰트, 그래픽 크기 설정
pyplot.rcParams["font.family"] = 'NanumGothic'
pyplot.rcParams["font.size"] = 14
pyplot.rcParams["figure.figsize"] = (12, 8)



# 국어 점수에 대한 상자그림 보기
pyplot.figure()
df.boxplot("국어")
#pyplot.show()
pyplot.savefig('boxplot1.png', dpi=300)
pyplot.close()


# 전체 점수에 대한 상자그림 보기
pyplot.figure()
df.boxplot()
#pyplot.show()
pyplot.savefig('boxplot2.png', dpi=300)
pyplot.close()
