# -*- coding: utf-8 -*-

# 모듈참조
from wordcloud import WordCloud
from matplotlib import pyplot
from collections import Counter

#------------------------------------------------------------
# 데이터 수집
#------------------------------------------------------------
# 텍스트 파일을 열어서 그 안의 내용을 text 변수에 저장
text = ''
with open("res/시경.txt", encoding="utf-8") as f:
    text = f.read();

# 각 글자를 리스트로 변환
tmp = list(text)
print(tmp)
print("-" * 30)

#------------------------------------------------------------
# 데이터 정제 -> 빈 문자열, 줄바꿈 문자, 쉼표 등을 제거
#------------------------------------------------------------
# 걸러낸 글자들이 저장될 리스트
hanja = []

# 금지어 목록 -> 걸러내고자 하는 글자들
ignore = [" ", "\n", ",", ".", "(", ")", "\U000f0703", "\ufeff"]

# 글자 리스트를 반복적으로 처리
for item in tmp:
    # 글자원소가 금지어 목록에 포함된 글자가 아니라면?
    if item not in ignore:
        # 공백을 제거한 상태로 새로운 리스트에 저장
        hanja.append(item.strip())

print(hanja)
print("-" * 30)

#------------------------------------------------------------
# 데이터 전처리 -> 글자별 빈도수 계산
#------------------------------------------------------------
# 1) Counter 객체를 통해 리스트 원소들의 빈도수 계산
count = Counter(hanja)
print(count)
print("-" * 30)

# 2) 가장 많이 등장한 상위 300개 결과를 워드 클라우드로 생성
most = count.most_common(300)
print(most)
print("-" * 30)

# 3) WordCloud 객체가 요구하는 형식으로 딕셔너리를 직접 구성
# -> {"글자": 빈도수, "글자": 빈도수, "글자": 빈도수 ...}
tags = {}
for n, c in most:
    tags[n] = c

print(tags)
print("-" * 30)

#------------------------------------------------------------
# 데이터 시각화
#------------------------------------------------------------
# -> 글꼴=바탕, 최대글자크기=250, 이미지넓이=1200, 높이=800, 확대=2배, 배경색상=흰색
wc = WordCloud(font_path="batang", max_font_size=250,
               width=1200, height=800, scale=2.0, background_color="#ffffff")

# 미리 준비한 딕셔너리를 통해 워드클라우드 생성
gen = wc.generate_from_frequencies(tags)

# 그래픽 결과물 생성하기
pyplot.figure()
pyplot.imshow(gen, interpolation='bilinear')
pyplot.axis("off")
wc.to_file("워드클라우드_시경.png")
pyplot.close()

