# -*- coding: utf-8 -*-

# 모듈 및 샘플 데이터 참조
from pandas import DataFrame
from sample import grade_list
from sample import grade_dic


# 2차원 리스트를 데이터프레임으로 변환
# -> 학생별 점수 표현 (None은 값이 없다는 뜻.)
df = DataFrame(grade_list)
print(df)
print("-" * 30)

# 각각의 데이터 열의 값과 타입 조회
#-> 각 열의 자료형=Series (DataFrame은 Series의 모음)
print(df[0])
print(type(df[0]))
print("-" * 30)

print(type(df[1]))
print(df[1])
print("-" * 30)


# 컬럼(열)이름을 지정하여 새로 생성
# -> 컬럼의 이름을 갖고 있는 리스트를 지정한다.
c_names = ['국어', '영어', '수학', '과학']
df = DataFrame(grade_list, columns=c_names)
print(df)
print("-" * 30)

# 각각의 데이터 열의 값조회
# -> 컬럼 이름이 지정되면 번호로 접근할 수 없다.
print(df['국어'])
print("-" * 30)

print(df['영어'])
print("-" * 30)



# 인덱스(행)이름을 지정하여 새로 생성
# -> 인덱스의 이름을 갖고 있는 리스트를 지정한다.
i_names = ['철수', '영희', '민철', '수현', '호영']
df = DataFrame(grade_list, index=i_names)
print(df)
print("-" * 30)



# 인덱스와 컬럼이름 모두 지정하기
df = DataFrame(grade_list, index=i_names, columns=c_names)
print(df)
print("-" * 30)




# 딕셔너리를 통한 데이터 프레임 만들기
# -> 딕셔너리의 key는 DataFrame의 컬럼(열)이름이 된다.
df = DataFrame(grade_dic)
print(df)
print("-" * 30)


# 인덱스 이름을 지정한 데이터 프레임 만들기
df = DataFrame(grade_dic, index=['철수', '영희', '민철', '수현', '호영'])
print(df)
print("-" * 30)

