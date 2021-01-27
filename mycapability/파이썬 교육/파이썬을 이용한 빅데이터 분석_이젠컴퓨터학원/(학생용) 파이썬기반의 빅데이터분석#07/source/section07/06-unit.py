# -*- coding: utf-8 -*-

class Unit:
    # 객체가 갖는 명사적 특성들을 멤버변수로 정의
    name = None     # 이름
    hp = None       # 체력(health point)
    dps = None      # 초당공격력(damage per Second)

    # 객체의 특성을 초기화 하기 위한 생성자 정의
    def __init__(self, name, hp, dps):
        self.name = name
        self.hp = hp
        self.dps = dps
        print("[%s] 체력: %d, 공격력: %d" % (name, hp, dps))

    # 객체가 수행해야 하는 동작들을 함수 형태로 정의
    def move(self, position):
        print("%s(이)가 %s까지 이동합니다." % (self.name, position))

    def attack(self, target):
        print("%s(이)가 %s(을)를 공격합니다. 데미지: %d" % (self.name, target, self.dps))


# 객체를 생성하면서 생성자를 통해 각 객체의 특성을 정의한다.
u1 = Unit("질럿1호", 100, 10)
u2 = Unit("질럿2호", 100, 12)
u3 = Unit("드라군1호", 120, 20)
u4 = Unit("드라군2호", 150, 35)
print("-" * 30)

# 객체를 동작시킨다.
u1.move('적 본진')
u3.move('적 본진')
u1.attack('적 본진')
u3.attack('적 본진')
print("-" * 30)

u2.move('적 멀티')
u4.move('적 멀티')
u1.attack('적 멀티')
u3.attack('적 멀티')

