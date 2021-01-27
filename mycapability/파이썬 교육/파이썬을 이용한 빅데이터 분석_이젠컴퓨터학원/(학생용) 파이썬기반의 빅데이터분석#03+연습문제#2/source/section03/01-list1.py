# -*- coding: utf-8 -*-

# 5명의 학생에 대한 성적 나열.
grade = [ 98, 82, 73, 64, 100 ]
print( grade )

# 각 학생의 이름에 대한 나열
names = [ "철수", "영희", "나영", "민식", "호영" ]
print( names )

# 파이썬은 서로 다른 자료형들을 함께 사용 가능
stud1 = [ "철수", 98 ]
stud2 = [ "영희", 82 ]
stud3 = [ "나영", 73 ]
print(stud1)
print(stud2)
print(stud3)

# 리스트의 각 원소는 0부터 시작되는 일련번호를 부여받는다. --> 인덱스 번호
# 인덱스 번호를 통해 각 원소에 접근할 수 있다.
name = stud1[0]
point = stud1[1]
print(name)
print(point)

# 값의 변경
stud1[0] = "철호"
stud1[1] = 100

# 리스트의 원소를 직접 출력하는 활용 예시
msg = "{0}(이)의 점수는 {1}점 입니다."
print( msg.format(stud1[0], stud1[1]) )
print( msg.format(stud2[0], stud2[1]) )
print( msg.format(stud3[0], stud3[1]) )


