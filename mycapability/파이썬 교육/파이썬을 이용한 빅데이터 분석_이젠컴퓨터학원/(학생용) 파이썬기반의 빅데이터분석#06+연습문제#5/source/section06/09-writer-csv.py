# -*- coding: utf-8 -*-

# 한 학급의 성적표 데이터 예시
grade = [
    {"name": "철수", "kor": 95, "eng": 88, "math": 72},
    {"name": "영희", "kor": 92, "eng": 90, "math": 95},
    {"name": "철민", "kor": 88, "eng": 76, "math": 64}
]

tpl = "{0},{1},{2},{3}\n"

# csv 파일 저장을 위한 f객체 생성
# -> Excel의 csv는 euc-kr 형식 (sublime은 euc-kr방식의 파일을 읽지 못한다.)
with open("grade.csv", "w", encoding='euc-kr') as f:
    # 첫 줄에 각 항목의 제목 기록
    f.write("이름,국어,영어,수학\n")

    # 각 데이터를 한 줄씩 콤마로 구분하여 기록
    for item in grade:
        tmp = tpl.format(item["name"], item["kor"], item["eng"], item["math"])
        f.write( tmp )



