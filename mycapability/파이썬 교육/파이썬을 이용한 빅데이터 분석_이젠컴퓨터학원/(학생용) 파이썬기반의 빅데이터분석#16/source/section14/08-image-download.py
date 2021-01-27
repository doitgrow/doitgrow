# -*- coding: utf-8 -*-

# 필요한 모듈 참조하기
import os                           # -> os모듈 (파일경로 처리용)
import requests                     # -> 웹 페이지 요청 모듈
from print_df import print_df       # -> 데이터 출력 모듈

# sample.py에서 필요한 데이터 참조
from sample import image_url        # 다운로드 할 이미지의 URL
from sample import user_agent       # 웹 브라우저 버전 정보

#----------------------------------------------------------
# 데이터 수집 - 이미지 URL 가져오기
#----------------------------------------------------------
# 접속 세션을 생성하고 referer 페이지와 브라우저 버전 설정
session = requests.Session()
session.headers.update( {'referer': None, 'User-agent': user_agent} )

# 이미지 URL에 접속 (파일 다운로드의 경우 stream=True 파라미터 추가)
r = session.get(image_url, stream=True)

# -> 결과확인 후 에러 발생시 강제 종료
if r.status_code != 200:
    print("%d 에러가 발생했습니다." % r.status_code)
    quit()


#----------------------------------------------------------
# 데이터 전처리 - 가져온 결과에서 바이너리를 추출하여 저장하기
#----------------------------------------------------------
# 이미지 주소에서 파일이름만 추출하기 -> s_1210_2011112414293493.jpg
fname = os.path.basename(image_url)
print_df(fname)

# 파일명에서 마지막 점(.)의 위치를 찾음
p = fname.rfind(".")

# 찾아진 위치가 0보다 작다면? --> 파일이름에 점이 없다면?
if p < 0:
	# 파일이름 뒤에 강제로 .jpg 라고 확장자 적용
    fname += ".jpg"

print_df(fname)

# 이미지의 바이너리(이진값) 데이터를 추출
img = r.raw.read()

# 추출한 데이터를 저장
# -> 'w': 텍스트 쓰기 모드, 'wb': 바이너리(이진값) 쓰기 모드
with open(fname, 'wb') as f:
    f.write(img)



