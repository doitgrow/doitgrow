# -*- coding: utf-8 -*-

# 딕셔너리는 리스트나 다른 딕셔너리를 포함할 수 있다.
# -> 정보를 계층화해서 표현 가능함
addr = ["서울", "서초구", "강남대로"]
grade = {"korean": 98, "math": 77, "english": 82}

member = {
    "userid": "python",     # 문자열 데이터
    "age": 20,              # 정수형 데이터
    "addr": addr,           # 리스트 데이터
    "grade": grade          # 딕셔너리 데이터
}

print( member )
print("-" * 30)

# 계층화된 값에 접근하기
print( member["addr"][0] )
print( member["grade"]["korean"] )
print("-" * 30)


# 딕셔너리의 계층화 직접 표현
mydic = {
    'total' : 1962,
    'city' : ["서울", "대전", "광주"],
    'population' : [987, 654, 321],
    'date' : { 'yy': 2018, 'mm': 9, 'dd': 10 }
}

print(mydic)
print(mydic["city"][0])
print(mydic["population"][0])
print(mydic["date"]["yy"])
print("-" * 30)

# 리스트의 원소가 딕셔너리가 되는 경우 --> 표 자료형
grade = [
    {"name": "철수", "kor": 95, "eng": 88},
    {"name": "영희", "kor": 92, "eng": 90},
    {"name": "철민", "kor": 88, "eng": 76}
]

tpl = "{0}의 국어점수:{1}, 영어점수: {2}"
print( tpl.format(grade[0]["name"], grade[0]["kor"], grade[0]["eng"]) )
print( tpl.format(grade[1]["name"], grade[1]["kor"], grade[1]["eng"]) )
print( tpl.format(grade[2]["name"], grade[2]["kor"], grade[2]["eng"]) )
print("-" * 30)

