# -*- coding: utf-8 -*-

# 모듈 참조하기
from wordcloud import WordCloud     # 워드클라우드 모듈
from matplotlib import pyplot       # 그래프 모듈

#----------------------------------------------------
# 색상값을 리턴하기 위한 함수 정의
#----------------------------------------------------
# -> 이 함수는 wordcloud 모듈에 의해 호출된다.
#    함수 이름은 임의로 설정가능하지만
#    파라미터는 wordcloud모듈에 의해 정해진대로 사용해야 한다.
def make_colors(word, font_size, position, orientation, random_state, **kwargs):
    # case1) 단일 색상 지정
    # color = "#ff6600"

    # case2) rgb(255,255,255) 형식의 색상값 생성
    # -> 파라미터로 전달되는 random_state 객체를 사용하여
    #    주어진 범위 안에서 랜덤값 생성 가능함.
    # r = random_state.randint(0, 255)
    # g = random_state.randint(0, 255)
    # b = random_state.randint(0, 255)

    # rgb(128, 245, 21) 형식으로 색상문자열 생성
    # color = "rgb(%d, %d, %d)" % (r, g, b)

    # case3) hsl 형식 색상 지정
    # -> 색상, 포화, 밝기
    # - 색상(H) : 0 ~ 360, 원형의 색상 띠 (`빨주노초파남보`는 대략 51˚씩 차이)
    # - 채도(S) : 0 ~ 100% , 색상의 순도 (빨갛다 ~ 새빨갛다 등)
    # - 명도(L) : 0(어둠,검게 보임) ~ 100(밝음,하얗게 보임)%, 색의 밝기
    a = random_state.randint(30, 90)
    b = random_state.randint(30, 90)

    # hsl(270, 54% 32%) 형식으로 색상문자열 생성
    color = "hsl(270, %d%%, %d%%)" % (a, b)

    return color

#----------------------------------------------------
# 텍스트 파일을 열기 +  WordCloud 객체 생성 + 단어빈도수 계산
#----------------------------------------------------
text = ''
with open("res/이상한나라의앨리스.txt", encoding="utf-8") as f:
    text = f.read()

# background_color 파라미터를 통해 배경색상을 설정할 수 있다.
wc = WordCloud(width=1200, height=800, scale=2.0, max_font_size=150,
               background_color="#ffffff")
gen = wc.generate(text)

#----------------------------------------------------
# 그래픽 생성 시작
#----------------------------------------------------
# 계산된 빈도수에 색상값들을 정의.
# -> 색상값을 리턴해 줄 함수의 이름과 random_state 기능 사용 여부 설정
#    여기서 설정한 random_state에 따라 make_colors 함수 안에서 랜덤값을
#    사용할 수 있을지가 결정된다.
recolor = gen.recolor(color_func=make_colors, random_state=True)

pyplot.figure()
pyplot.imshow(recolor, interpolation='bilinear')
wc.to_file("color.png")
pyplot.close()
