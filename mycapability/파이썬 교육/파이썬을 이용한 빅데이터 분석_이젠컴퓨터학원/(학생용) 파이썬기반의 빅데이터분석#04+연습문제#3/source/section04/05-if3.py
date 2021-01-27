# -*- coding: utf-8 -*-

# else문
# -> "그렇지 않으면"의 의미
# -> 독립적으로 사용될 수 없고 반드시 if문 뒤에만 위치
age = 19

if age > 19:
    print("성인입니다.")
else:
    print("성인이 아닙니다.")

print("-" * 30)


# 활용예시
user1 = "hello"
user2 = "world"
member_list = ['hello', 'python', 'life']

if user1 in member_list:
    # 조건이 참이므로 if절이 실행된다.
    print("%s는 이미 가입되어 있습니다." % user1)
else:
    # 조건이 거짓이 아니므로 else절은 실행되지 않는다.
    print("%s는 이미 가입되어 있지 않습니다." % user1)

if user2 in member_list:
    # 조건이 거짓이므로 if절은 실행되지 않는다.
    print("%s는 이미 가입되어 있습니다." % user2)
else:
    # 조건이 거짓이므로 else절이 실행된다.
    print("%s는 이미 가입되어 있지 않습니다." % user2)

print("-" * 30)



# 다양한 경우의 수 나열
# -> elif는 if와 else 사이에서 나열된 조건 중
#    처음으로 만나는 참인 조건에 대한 블록을 수행하고
#    나머지 조건은 무시하고 종료한다
point = 72

if point > 90:
    print("A학점")
elif point > 80:
    print("B학점")
elif point > 70:
    print("C학점")
elif point > 60:
    print("D학점")
else:
    print("F학점")
