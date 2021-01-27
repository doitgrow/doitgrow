# -*- coding: utf-8 -*-

def plus(x, y):
    z = x + y
    # 자신이 호출된 위치로 값을 되돌려준다.
    return z

a = plus(10, 20)
print(a)

# 리턴값을 갖는 함수는 그 결과를 직접 출력하거나
# 다른 연산에 활용할 수 있다.
print( plus(100, 200) )

b = plus(5, 7) + 100
print(b)
print("-" * 30)



# return문을 중간에 만나는 경우 그 즉시 수행을 종료한다.
def foo(x, y):
    if x < 10 or y < 10:
        return 0

    z = x + y
    return z

# -> 26라인의 조건이 거짓이 되므로 27라인은 수행되지 않는다.
print( foo(100, 200) )

# -> 26라인이 참이 되므로 27라인이 수행된다.
# -> 27라인의 return문에 의해 함수가 종료되므로
#    29,30라인은 수행되지 않는다.
print( foo(1, 2) )

print("-" * 30)





# 단순히 실행을 종료할 목적이라면 return키워드만 사용 가능
def id_check(user_id):
    # 기존에 가입되어 있는 회원들의 아이디.
    member_list = ['user1', 'user2', 'user3']

    # 만약 user_id가 값이 없다면 처리중단.
    if not user_id:
        return

    # 만약 user_id의 값이 member_list에 속해 있다면?
    if user_id in member_list:
        print("사용할 수 없는 아이디 입니다.")
    else:
        print("사용 가능한 아이디 입니다.")

id_check("")        # 아무것도 출력안됨
id_check("user1")
id_check("python")
print("-" * 30)


# 두 개의 값을 튜플이나 리스트로 묶어서 한번에 리턴
def bar():
    x = 1
    y = 2
    return (x, y)


# 함수의 리턴값이 튜플이므로 인덱스 번호를 활용하여 원소에 접근한다.
a = bar()
print(a)
print(a[0])
print(a[1])


# `a, b = (1, 2)`의 변수 일괄 생성 규칙을 활용하면
# 아래와 같이 튜플이나 리스트 형식의 파라미터를 개별변수로 저장 가능함
m, n = bar()
print(m)
print(n)






