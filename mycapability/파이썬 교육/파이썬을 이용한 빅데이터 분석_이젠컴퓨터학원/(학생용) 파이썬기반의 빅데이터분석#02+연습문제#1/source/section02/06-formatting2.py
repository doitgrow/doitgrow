# -*- coding: utf-8 -*-

# 0번째 위치에 format()함수에 전달된 0번째 값을 대입
msg1 = "I eat {0} apples"
print( msg1.format(3) )

# 여러 개의 값을 혼용하기
msg2 = "{0}은 {1}년 {2}월 {3}일 입니다."
print( msg2.format("개강일", 2018, 8, 12) )

# 이름으로 넣기
msg3 = "{name}은 {yy}년 {mm}월 {dd}일 입니다."
print( msg3.format(name="종강일", yy=2018, mm=10, dd=20) )

# 혼합사용 -> 숫자형식의 치환자가 먼저 위치해야 한다.
msg4 = "{0}은 {yy}년 {mm}월 {dd}일 입니다."
print( msg4.format("생일", yy=1990, mm=1, dd=31) )

# 5글자 오른쪽 정렬 -> "%5s"와 동일
msg5 = "{0:>5}!!Python, {1:>9}~Python"
print( msg5.format("Hi", "Welcome") )

# 5글자 왼쪽 정렬 -> "%-5s"와 동일
msg6 = "{0:<5}!!Python, {1:<9}~Python"
print( msg6.format("Hi", "Welcome") )

# 가운데 정렬
msg7 = "{0:^10}!!Python, {1:^9}~Python"
print( msg7.format("Hi", "Hello") )

# 공백을 지정한 문자로 채우기
msg8 = "{0:~<5}!!Python!! {1:*^9}!!Python"
print( msg8.format("Hi", "Hello") )

# 소수점 4째자리까지 표현하기 -> 5째자리에서 반올림
msg9 = "{0:0.4f}"
print( msg9.format(123.456789) )

# 전체 10글자,소수점 4째자리까지 표현하기 -> 5째자리에서 반올림
msg10 = "{0:10.4f}"
print( msg10.format(123.456789) )

# 전체 10글자,공백은 0, 소수점 4째자리까지 표현하기 -> 5째자리에서 반올림
msg11 = "{0:010.4f}"
print( msg11.format(123.456789) )

# 문자열에 "{"나 "}" 포함시키기 --> 두겹으로 사용
msg12 = "{{python}}은 {0}다"
print( msg12.format("쉽") )
print( msg12.format("좋") )


