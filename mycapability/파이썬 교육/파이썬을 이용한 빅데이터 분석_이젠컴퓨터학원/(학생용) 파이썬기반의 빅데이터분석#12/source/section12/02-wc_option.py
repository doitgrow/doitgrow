# -*- coding: utf-8 -*-

# 모듈 참조하기
from wordcloud import WordCloud     # 워드클라우드 모듈
from matplotlib import pyplot       # 그래프 모듈
from wordcloud import STOPWORDS     # 금지어 설정 모듈
from PIL import Image               # 이미지 처리 모듈
import numpy                        # 연산모듈

#----------------------------------------------------
# 텍스트 파일을 열어서 그 안의 내용을 text 변수에 저장
#----------------------------------------------------
text = ''
with open("res/이상한나라의앨리스.txt", encoding="utf-8") as f:
    text = f.read()

print(text)
print("-" * 30)

# 금지어 설정 --> 필요한 만큼 add()함수를 호출하여 추가
ignore = set(STOPWORDS)
ignore.add("said")
ignore.add("Alice")


#----------------------------------------------------
# WordCloud 클래스의 객체 생성
#----------------------------------------------------
# 배경이미지 가져오기
img = Image.open("res/앨리스배경.png");
# 배경이미지 데이터를 numpy리스트로 변환
img_array = numpy.array(img)

# 이미지데이터와 금지어를 적용하여 워드클라우드 생성
# -> 이미지 가로크기, 세로크기, 확대비율(1.0=100%, 2.0=200%),
# -> 최대 글자 크기, 최대 표시 단어 수, 금지어, 마스크이미지
wc = WordCloud(width=600, height=1200, max_font_size=150, scale=2.0,
               max_words=100, stopwords=ignore, mask=img_array)

#----------------------------------------------------
# 단어 빈도수 계산
#----------------------------------------------------
# WordCloud 객체를 사용하여 텍스트에 대한 단어 빈도수 추출
# -> {"단어": 빈도수, "단어": 빈도수 ... } 형식.
# -> 딕셔너리를 직접 코딩으로 정의해도 무관함.
gen = wc.generate(text)
print(gen.words_)

#----------------------------------------------------
# 그래픽 생성 시작
#----------------------------------------------------
pyplot.figure()
# 그래픽 표시 데이터를 단어 빈도수에 대한 딕셔너리로 지정
pyplot.imshow(gen, interpolation='bilinear')
wc.to_file("option.png")
pyplot.close()
