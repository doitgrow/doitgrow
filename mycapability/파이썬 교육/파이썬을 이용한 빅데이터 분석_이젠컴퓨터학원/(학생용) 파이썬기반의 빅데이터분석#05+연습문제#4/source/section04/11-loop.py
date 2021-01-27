# -*- coding: utf-8 -*-

# 무한루프 -> 조건설정이 잘못되어 종료되지 않는 반복
x = 1

# 실행시에 종료되지 않기 때문에 주석으로 막아둠.
# while x < 10:
#    print(x)
#    x -= 1


# 의도적으로 무한루프를 설정하는 경우
# -> 반복의 횟수를 가늠할 수 없을 때 사용.
# -> 반복문 내에서의 흐름제어 : continue, break
y = 0
while True:
    y += 1

    if y % 2 == 0:
        continue    # 조건식으로 강제 이동

    if y > 100:
        break       # 반복문을 강제로 종료

    print("Hello Python (%d)" % y)


