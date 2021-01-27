# -*- coding: utf-8 -*-

# 날짜 처리 모듈을 로드함
import datetime as dt

# 두 날짜 만들기
# -> 오늘날짜
dt1 = dt.datetime.now()
# -> 내년 1월1일 자정
dt2 = dt.datetime(dt1.year+1, 1, 1, 0, 0, 0)

# 두 날짜의 차를 구한 결과는 timedelta 객체형식이 된다.
# -> datetime 모듈에 정의되어 있는 객체형식임.
td = dt2 - dt1
# -> ex) 25 days, 21:04:12.386733
print(td)

# timedelta 객체에 내장된 변수(=속성)
# -> 날짜만 추출
print(td.days)      # ex) 25일
# -> 날짜를 제외하고 시간,분,초 단위를 모두 초로 합산한 값.
print(td.seconds)   # ex) 75852초
print("올해는 %d일 남았습니다." % td.days)
print("-" * 30)

# 모든 속성을 초단위로 모아서 반환
# -> ex) 25일에 해당하는 초를 구한 후 75852를 더한 결과를 반환
result = td.total_seconds()
print(result)
print("-" * 30)

# 특정시각(혹은 현재시각)에 timedelta 객체를 더해 연산결과를 얻을 수 있다.
now_time = dt.datetime.now()

# timedelta 객체 만들기(더할 값) --> 100일+3600초
d = dt.timedelta(days=100, seconds=3600)

# 연산 결과는 datetime 객체가 된다.
after_time = now_time + d
print(after_time.strftime("%Y-%m-%d %H:%M:%S"))
