# -*- coding: utf-8 -*-

# 각 학생별 이름,점수 정의
stud1 = [ "철수", 98 ]
stud2 = [ "영희", 82 ]
stud3 = [ "나영", 73 ]

# 2차원 리스트 -> 새로운 리스트 stud_group의 각 원소가 리스트가 되는 형태
stud_group = [ stud1, stud2, stud3 ]
print(stud_group)
print("-" * 30)

# 1차원 원소에 접근하기
print(stud_group[0])     # stud_group의 0번째 원소
print(stud_group[1])     # stud_group의 1번째 원소
print("-" * 30)

# 2차원 원소에 접근하기
print(stud_group[0][0])  # 0번째 원소의 0번째 항목
print(stud_group[0][1])  # 0번째 원소의 1번째 항목
print(stud_group[1][0])  # 1번째 원소의 0번째 항목
print(stud_group[1][1])  # 1번째 원소의 1번째 항목
print("-" * 30)

# 2차원 리스트의 일괄 생성
# -> 바깥의 리스트에 속한 원소들는 행을 구성하고,
#    안쪽의 리스트에 속한 원소들은 열을 구성한다.
grade = [
            [ "민식", 64 ] ,	# 0번째 행 -> 0번째 열=민식, 1번째 열=64
            [ "호영", 100 ]		# 1번째 행 -> 0번째 열=호영, 1번째 열=100
        ]
print(grade)
print("-" * 30)

# 존재하지 않는 인덱스에 접근할 경우 "list index out of range" 에러 발생
# -> 아래 구문은 에러가 발생하므로 주석으로 막아둠.
# print(grade[3][1])


