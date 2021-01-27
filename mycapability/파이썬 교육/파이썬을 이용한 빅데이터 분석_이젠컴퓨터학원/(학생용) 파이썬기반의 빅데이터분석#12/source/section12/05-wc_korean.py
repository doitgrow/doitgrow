# -*- coding: utf-8 -*-

from wordcloud import WordCloud
from matplotlib import pyplot
from collections import Counter
from konlpy.tag import Okt

#------------------------------------------------------------
# 텍스트 파일을 열어서 그 안의 내용을 text 변수에 저장
#------------------------------------------------------------
text = ''
with open("res/대한민국헌법.txt", encoding="utf-8") as f:
    text = f.read();

#------------------------------------------------------------
# 읽은 내용을 기반으로 형태소 분석
#------------------------------------------------------------
# 형태소 분석 클래스의 객체 생성
nlp = Okt()
# 명사들만 추출 -> 리스트형식으로 반환
nouns = nlp.nouns(text)
print(nouns)
print("-" * 30)

# 한글자로 된 단어는 걸러냄
words = []
for n in nouns:
    if len(n) > 1:
        words.append(n)

print(words)
print("-" * 30)

#------------------------------------------------------------
# 빈도수 계산
#------------------------------------------------------------
# Counter 객체를 통해 리스트 원소들의 빈도수 계산
count = Counter(words)

# 가장 많이 등장한 상위 100개 추출
most = count.most_common(100)
print(most)
print("-" * 30)

# WordCloud 객체가 요구하는 형식으로 딕셔너리를 직접 구성
tags = {}
for n, c in most:
    tags[n] = c

print(tags)
print("-" * 30)

#------------------------------------------------------------
# 수집결과를 활용하여 워드클라우드 생성
#------------------------------------------------------------
wc = WordCloud(font_path="NanumGothic", width=1200, height=800,
                scale=2.0, max_font_size=250)

# 직접 준비한 딕셔너리를 통해 생성
gen = wc.generate_from_frequencies(tags)

pyplot.figure()
pyplot.imshow(gen, interpolation='bilinear')
wc.to_file("korean.png")
pyplot.close()


