# -*- coding: utf-8 -*-

# 쓰기 모드로 파일 객체 생성하기
# --> 이전 예제와 동일하지만 f.close()처리는 자동으로 수행함.
with open("hellopython.txt", "w", encoding='utf-8') as f:
    # with 블록 안에서만 파일 객체 f가 유효함
    for i in range(0, 10):
        f.write("%d >> " % i)
        f.write("Life is too short, ")
        f.write("you need python\n")

    print("파일 저장이 완료되었습니다.")

# 읽기 모드로 파일 객체 생성하기
# `w`에서 `r`로 모드가 변경되어야 하므로 파일 객체를 새로 생성해야 한다.
with open("hellopython.txt", "r", encoding='utf-8') as f:
    # 파일의 내용을 변수에 저장함
    data = f.read()
    print(data)


