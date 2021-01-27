# -*- coding: utf-8 -*-

# 모듈 가져오기
import datetime as dt

# 현재 시각이 아닌 특정 시각을 저장하는 날짜객체 생성하기
# -> 시간 지정시 24시간제로 지정해야 함
# -> 존재하지 않는 월,날짜,시간 값들을 지정할 경우 에러 발생
someday = dt.datetime(2018, 8, 30, 13, 26, 55)
print(someday.strftime("%y/%m/%d %H:%M:%S"))
print("-" * 30)

# 날짜 형식의 문자열을 날자객체로 변환하기
date_str = "2017년 01월 02일 14시 44분"
oldday = dt.datetime.strptime(date_str, "%Y년 %m월 %d일 %H시 %M분")
print(oldday.strftime("%y/%m/%d %H:%M:%S"))
print("-" * 30)

# 날짜객체에서 특정 값 변경하기
# -> 단위=값 형식으로 원하는 만큼 지정 가능함.
change_date = oldday.replace(year=2018, day=16, hour=15)
print(change_date.strftime("%y/%m/%d %H:%M:%S"))
print("-" * 30)

#날짜객체와 시간객체를 개별적으로 생성
# -> 파라미터가 없을 경우 에러 발생함.
d = dt.date(2015, 4, 15)
t = dt.time(12, 23, 38)
print(d)
print(t)
print("-" * 30)

# 두 객체를 결합하기
result = dt.datetime.combine(d, t)
print(result) # 2015-04-15 12:23:38
print("-" * 30)
