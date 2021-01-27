# -*- coding: utf-8 -*-

# 필요한 모듈 참조
import requests
import json
from print_df import print_df

# 간단한 JSON Object URL
simple_json_url = "http://www.itpaper.co.kr/demo/python/phone.json"

# 웹페이지에 접속
r = requests.get(simple_json_url)

# 접속에 실패한 경우
if r.status_code != 200:
    # 에러코드와 에러메시지 출력
    print("[%d Error] %s" % (r.status_code, r.reason))
    # 프로그램 강제 종료
    quit()

# 인코딩 설정 및 결과값 출력
r.encoding = "utf-8"
print_df(r.text)

# 가져온 결과를 딕셔너리로 변환
result = json.loads(r.text)
print_df(result)

print("결과코드: %s" % result['rt'])
print("결과메시지: %s" % result['rtmsg'])
print("제품명: %s" % result['item']['name'])
print("제조사: %s" % result['item']['type'])
print("사진: %s" % result['item']['img'])
print("정가: %d" % result['item']['price']['fixed'])
print("판매가: %d" % result['item']['price']['sale'])


