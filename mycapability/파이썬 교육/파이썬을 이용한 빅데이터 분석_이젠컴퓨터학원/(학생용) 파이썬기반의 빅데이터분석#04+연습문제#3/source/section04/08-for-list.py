# -*- coding: utf-8 -*-

# 문자열에 대한 반복
test_str = "Python"

# -> 문자열의 각 글자를 순차적으로 i에 대입하면서 반복
for i in test_str:
    print(i)

print("-" * 30)


# 리스트에 대한 반복
test_list = ['python', 'is', 'good']

# -> 리스트의 각 원소를 순차적으로 i에 대입하면서 반복
# -> 단점: 몇 번째 원소인지는 알 수 없다.
for i in test_list:
    print(i)

print("-" * 30)


# 몇 번째 원소인지를 카운트하기 위한 별도의 변수 사용
# -> 단점: 별도의 변수를 관리해야 하므로 처리가 복잡해진다.
count = 0
for i in test_list:
    print( "%d번째 원소: %s" % (count, i) )
    count += 1

print("-" * 30)


# 원소의 수를 조회한 다음 직접 반복범위 지정하기
# -> 단점: 각 원소가 저장되는 변수가 없기 때문에
#          원소에 대한 접근을 리스트를 통해 직접 수행해야 한다.
size = len(test_list)
for i in range(0, size):
    print( "%d번째 원소: %s" % (i, test_list[i]) )

print("-" * 30)


# 내장함수를 사용하여 인덱스와 값 한번에 얻기
# -> i에는 리스트의 인덱스가 저장된다.
# -> value에는 리스트의 값(원소)가 저장된다.
# -> i, value는 단순 변수이므로 개발자 편의에 따라 이름지을 수 있다.
for i, value in enumerate(test_list):
    print("%d번째 값 >> %s" % (i, value))

print("-" * 30)



# 성적에 대한 총점과 평균 구하기
point_list = [ 100, 82, 98, 76, 51 ]

# -> 총점을 저장할 변수
total = 0

for point in point_list:
    # 총점은 각 원소를 누적해서 더한다.
    total += point

# 평균은 총 합에서 원소의 수를 나눈다.
# -> "//"는 나눗셈에서 정수부분의 몫만 구한다.
avg = total // len(point_list)

tpl = "총점: {0}, 평균: {1}"
print(tpl.format(total, avg))
