# -*- coding: utf-8 -*-

str = "Life is too short, You need Python"

# 3번째 문자 추출 -> 0부터 카운트
print( str[3] )

# 뒤에서 3번째 글자 추출 -> -1부터 카운트
# (0과 -0이 같은 값이기 때문)
print( str[-3] )

# 앞에서 0번째 부터 3번째 전 까지의 문자 추출
print( str[0:3] )

# 앞에서 5번째 부터 7번째 전 까지의 문자 추출
print( str[5:7] )

# 앞에서 19번째 부터 끝까지 추출
print( str[19:] )

# 처음부터 앞에서 17번 전 까지의 문자 추출
print( str[:17] )

# 처음부터 끝까지 추출
print( str[:] )

# 앞에서 19번째부터 뒤에서 -7번째 다음까지 추출
print( str[19:-7] )


# [응용] 글자수가 정해져 있는 경우 활용도 높음
# ex) "80년05월27일 남자"의 주민번호 일부
jumin = "8005271"
birth = jumin[:6]   # 생일
gender = jumin[6:]  # 성별
print(birth)
print(gender)

# 태어난 년도
year = "19" + jumin[:2]
print(year)

# 태어난 월
month = jumin[2:4]
print(month)

# 태어난 날
day = jumin[4:6]
print(day)

