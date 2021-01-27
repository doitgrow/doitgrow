# -*- coding: utf-8 -*-

with open("helloworld.txt", "r", encoding='utf-8') as f:
    # 파일의 각 행을 원소로 갖는 리스트 생성
    # -> 아래의 구문과 동일한 효과
    #       lines = ["Hello Python!!!\n","안녕하세요. 파이썬!!!\n"]
    lines = f.readlines()
    print(lines)
    print("-" * 30)

    # 전체 리스트의 크기 확인
    size = len(lines)
    print("읽어들인 데이터는 총 %d줄 입니다." % size)
    print("-" * 30)

    for item in lines:
        # 읽어들인 데이터에 줄바꿈 문자가 포함되므로 공백제거 필요
        print( item.strip() )

