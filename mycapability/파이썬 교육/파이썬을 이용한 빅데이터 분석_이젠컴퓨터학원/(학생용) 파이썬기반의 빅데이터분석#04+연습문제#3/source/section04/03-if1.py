# -*- coding: utf-8 -*-

# 일반 구문
print("배고픈데")

# 조건문 --> if 조건식:
have_money = True
#have_money = False

if have_money:
    # 조건문에 속한 명령어는 반드시 들여쓰기 적용해야 함
    # -> tab키 혹은 space x 1개 이상
    # -> tab키와 space를 혼용해서 사용할 수 없다.
    print("식당에서")

# 일반 구문
print("밥을 먹자")

print("-" * 30)


# 숫자형 변수에 대한 조건 처리
money = 10000
# money = 0
if money:
    print("택시를 타고")

print("집에가자")
print("-" * 30)


# 문자열 변수에 대한 조건처리
name = "Python"
#name = ""

if name:
    print(name)

print("프로그래밍")
print("-" * 30)


# 리스트에 대한 조건 처리
grade = [100, 80, 70]
#grade = []

if grade:
    msg = "국어: {0}, 영어: {1}, 수학: {2}"
    print(msg.format(grade[0], grade[1], grade[2]))

print("성적처리")
print("-" * 30)


# 비교식과 논리식은 if문의 조건이 될 수 있다.
money = 12000

# -> money가 0이 아닌 경우
if money:
    print("돈이 있다.")

# -> money가 5000 이상인 경우
if money >= 5000:
    print("선물을 사고 %d원 남는다." % (money-5000))

# -> money가 0이 아니고 15000 보다 작은 경우
# -> and 연산은 두 항이 모두 참인 경우만 전체가 참.
# -> or 연산은 두 항중 하나라도 참이면 전체가 참.
if money and money < 15000:
    print("돈이 있지만 %d원 부족하다." % (15000-money))

print("-" * 30)
