# -*- coding: utf-8 -*-

# if문간의 중첩
point = 78

if point > 70:
    print ("패스입니다.")

    if point > 90:
        print("A입니다.")
    elif point > 80:
        print("B입니다.")
    else:
        print("C입니다.")

else:
    print("패스하지 못했습니다.")

print("-" * 30)


# for문과 if문의 중첩 -> 주로 반복되는 index값에 대한 조건 판별.
x = 0
y = 0

# -> 1~10까지 반복 수행
for i in range(1, 11):
    # 어떤 수를 2로 나눈 나머지가 0이면 짝수
    if i % 2 == 0:
        print("%d(은)는 짝수" % i)
        x += i
    # 그렇지 않으면 홀수
    else:
        print("%d(은)는 홀수" % i)
        y += i

print("1~10까지 짝수들의 합: %d" % x)
print("1~10까지 홀수들의 합: %d" % y)

print("-" * 30)



# 2중 반복문 --> 구구단
tpl = "{0} x {1} = {2}"

# i의 변화범위 2~9
for i in range(2, 10):

    # i가 1 증가하는 동안 j의 값이 매번 1~9까지 새로 시작
    for j in range(1, 10):
        k = i * j
        print(tpl.format(i, j, k))

    print("-" * 30)




