# -*- coding:utf-8 -*-
"""
13-sendmail3.py > 대량메일 발송
"""
# 헬퍼에 정의된 함수 참조
from helper import sendmail
import datetime as dt

# 이번년도와 월 얻기
now_time = dt.datetime.now()
now_year = now_time.year
now_month = now_time.month

# 발송자 주소, 메일 제목
from_addr = "직접설정하세요"
subject_tpl = '{name}님의 {yy}년 {mm}월 급여명세서 입니다.'

# 메일 본문은 HTML파일 읽기
with open("mail/content.html", "r", encoding='utf-8') as f:
    content_tpl = f.read()

# 수신자 목록에 대한 CSV파일 읽기
with open("mail/mail_list.csv", "r", encoding='euc-kr') as f:
    csv_data = f.readlines()        # 전체 내용을 리스트로 읽어옴
    count = len(csv_data)           # 전체 행 수

    # 결과 출력을 위한 문자열 템플릿
    result_tpl = "{0}/{1} >> {2}({3})님께 메일을 발송했습니다."

    # 리스트 행 수 만큼 반복 -> i에는 인덱스, line은 한 행의 문자열이 저장됨
    # line = "학생,hello@gmail.com,mail/document.pptx,mail/pay1.xlsx"
    for i, line in  enumerate(csv_data):
        item = line.strip().split(",")
        to_name = item[0].strip()
        to_addr = item[1].strip()
        file1 = item[2].strip()
        file2 = item[3].strip()

        # 제목과 내용에 포함된 {이름} 형식의 치환자에 변수값 적용
        subject = subject_tpl.format(name=to_name, yy=now_year, mm=now_month)
        content = content_tpl.format(name=to_name, yy=now_year, mm=now_month)

        # 메일을 발송한다.
        sendmail(from_addr, to_addr, subject, content, [file1, file2])

        # 결과 출력
        print(result_tpl.format(i+1, count, to_name, to_addr))

# 최종 결과 출력
print("=" * 30)
print("메일 발송이 완료되었습니다.")
