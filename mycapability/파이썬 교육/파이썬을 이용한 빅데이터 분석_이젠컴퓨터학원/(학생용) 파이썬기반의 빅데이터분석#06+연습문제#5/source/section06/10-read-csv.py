# -*- coding: utf-8 -*-

with open("grade.csv", "r", encoding='euc-kr') as f:
    # 파일의 각 행을 원소로 갖는 리스트 생성
    csv_list = f.readlines()
    print(csv_list)
    print("-" * 30)

    for i, line in enumerate(csv_list):
        if i > 0:
            # 현재 행의 내용을 콤마를 기준으로 잘라서 리스트로 변환
            # "철민,88,76,64".split(",") ==> ["철민","88","76","64"]
            item = line.strip().split(",")
            print(item)

            # 이름과 점수로 분리 -> 점수는 정수형으로 변환
            name  = item[0]
            kor   = int(item[1])
            eng   = int(item[2])
            math  = int(item[3])
            total = kor + eng + math    # 총점
            avg   = total / 3           # 평균

            # 결과출력
            tpl = "{0}의 총점은 {1}점이고 평균은 {2:0.2f}점 입니다."
            print(tpl.format(name, total, avg))
