# -*- coding: utf-8 -*-

# 전체 원소의 개수 조회
my_list = [ 1, 2, 3 ]
size = len(my_list)
print(size)
print("-" * 30)

# 맨 뒤에 내용 추가
my_list = [ 1, 2, 3 ]
my_list.append(4)
print(my_list)
print("-" * 30)

# 리스트를 append 할 경우 2차 리스트로 삽입.
my_list = [ 1, 2, 3 ]
my_list.append([5,6])
print(my_list)
print("-" * 30)

# 중간삽입
# -> 1번째 위치에 10을 삽입. 기존의 항목들은 뒤로 밀려난다.
my_list = [ 1, 2, 3 ]
my_list.insert(1, 10)
print(my_list)
print("-" * 30)

# 맨 마지막 요소를 꺼내고 삭제
# -> 마지막 요소를 리턴한다.
my_list = [ 1, 2, 3 ]
k = my_list.pop()
print(k)
print(my_list)
print("-" * 30)

print(my_list.pop())
print(my_list)
print("-" * 30)

# 리스트 확장
my_list = [ 1, 2, 3 ]
addon = [ 10, 9, 8, 7 ]
my_list.extend( addon )
print(my_list)
print("-" * 30)

# 주어진 값과 일치하는 원소의 개수 세기
my_list = [ 1, 2, 3, 2 ]
c = my_list.count(2)
print(c)
print("-" * 30)

# 해당 값이 가장 처음 나타나는 위치(인덱스 반환)
my_list = [ 1, 2, 3, 10, 1, 2, 3, 10 ]
x = my_list.index(10)
print(x)
print("-" * 30)

# 주어진 값과 일치하는 첫 번째 원소를 삭제
my_list = [ 1, 2, 3, 10, 1, 2, 3, 10 ]
my_list.remove(10)
print(my_list)
print(my_list.count(10))
print("-" * 30)

# 순서 뒤집기
my_list = [ 1, 3, 5, 7, 9 ]
my_list.reverse()
print(my_list)
print("-" * 30)

# 순차정렬
my_list = [ 2, 5, 1, 6, 3 ]
my_list.sort()
print(my_list)
print("-" * 30)

# 역순정렬
my_list = [ 2, 5, 1, 6, 3 ]
my_list.sort(reverse=True)
print(my_list)
print("-" * 30)

# 문자열을 주어진 글자를 기준으로 잘라서 리스트로 변환
# -> 문자열 객체에 포함된 함수 사용
text = "Hello,Python,World,Good"
mylist = text.split(",")
print(mylist)
