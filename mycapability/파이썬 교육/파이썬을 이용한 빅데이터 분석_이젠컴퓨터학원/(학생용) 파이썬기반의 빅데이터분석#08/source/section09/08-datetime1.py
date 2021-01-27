# -*- coding: utf-8 -*-

# 날짜 처리 모듈(datetime)에 dt라는 별칭 적용
import datetime as dt

# 현재시각을 갖는 객체 가져오기
now_time = dt.datetime.now()
print(now_time)
print("-" * 30)

# 현재시각 객체에서 원하는 값만 추출하기
print(now_time.year)
print(now_time.month)
print(now_time.day)
print(now_time.hour)
print(now_time.minute)
print(now_time.second)
print(now_time.microsecond)
print("-" * 30)


# 현재시각 객체에서 요일 반환 (0:월, 1:화, 2:수, 3:목, 4:금, 5:토, 6:일)
d = now_time.weekday()
print(d)

# -> 리턴된 요일 값을 튜플의 인덱스로 활용하여 요일이름 출력
days = ("월", "화", "수", "목", "금", "토", "일")
print(days[d])
print("-" * 30)

# 출력형식 만들기
"""
%Y  앞의 빈자리를 0으로 채우는 4자리 연도 숫자
%y  앞의 빈자리를 0으로 채우는 2자리 연도 숫자
%m  앞의 빈자리를 0으로 채우는 2자리 월 숫자
%d  앞의 빈자리를 0으로 채우는 2자리 일 숫자
%H  앞의 빈자리를 0으로 채우는 24시간 형식 2자리 시간 숫자
%M  앞의 빈자리를 0으로 채우는 2자리 분 숫자
%S  앞의 빈자리를 0으로 채우는 2자리 초 숫자
"""
print(now_time.strftime("%y/%m/%d %H:%M:%S"))
print("-" * 30)
