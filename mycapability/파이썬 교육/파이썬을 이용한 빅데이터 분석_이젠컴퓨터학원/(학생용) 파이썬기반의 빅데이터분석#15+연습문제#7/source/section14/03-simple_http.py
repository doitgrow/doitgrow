# -*- coding: utf-8 -*-

# 필요한 모듈 참조
import requests

# 온라인 상의 text 파일 URL
simple_text_url = "http://itpaper.co.kr/demo/python/simple_text.txt"

# 특정 웹 페이지에 접속
r = requests.get(simple_text_url)

# 접속에 실패한 경우
if r.status_code != 200:
    # 에러코드와 에러메시지 출력
    print("[%d Error] %s" % (r.status_code, r.reason))
    # 프로그램 강제 종료
    quit()

# 인코딩 형식 지정
r.encoding = "utf-8"

# 텍스트 출력
print(r.text)


