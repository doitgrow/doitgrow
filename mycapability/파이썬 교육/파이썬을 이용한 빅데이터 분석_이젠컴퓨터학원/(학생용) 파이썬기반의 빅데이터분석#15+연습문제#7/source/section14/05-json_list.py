# -*- coding: utf-8 -*-

# 필요한 모듈 참조
import requests
import json
from pandas import DataFrame
from matplotlib import pyplot
from print_df import print_df

# 간단한 JSON List URL
json_list_url = "http://www.itpaper.co.kr/demo/python/student.json"

# 웹페이지에 접속
r = requests.get(json_list_url)

# 접속에 실패한 경우
if r.status_code != 200:
    # 에러코드와 에러메시지 출력
    print("[%d Error] %s" % (r.status_code, r.reason))
    # 프로그램 강제 종료
    quit()

# 가져온 결과 확인
r.encoding = "utf-8"
print_df(r.text)

# 가져온 결과를 딕셔너리로 변환
result = json.loads(r.text)
print_df(result)

# 결과를 데이터프레임으로 변환
df = DataFrame(result['student'])
print_df(df)


# name 열의 값을 인덱스로 사용하기 위해 리스트 형식으로 추출
name_list = list(df['name'])

# 데이터 프레임의 rename 함수에 적용하기 위한 딕셔너리 생성
name_dict = {}
for i, v in enumerate(name_list):
    name_dict[i] = v

# 데이터 프레임의 인덱스 변경 및 name 컬럼 삭제
df.rename(index=name_dict, inplace=True)
df.drop('name', axis=1, inplace=True)
print_df(df)


# 그래프를 만들기 위한 한글 폰트 설정
pyplot.rcParams["font.family"] = 'NanumGothic'
pyplot.rcParams["font.size"] = 14
pyplot.rcParams["figure.figsize"] = (14, 8)

# 전체 컬럼에 대한 시각화
df.plot.bar()
pyplot.grid()
pyplot.title("학생별 시험 점수")
pyplot.legend()
pyplot.ylabel("점수")
#pyplot.savefig('student.png', dpi=200)
pyplot.show()
pyplot.close()
