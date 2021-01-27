# -*- coding: utf-8 -*-

# 모듈 참조
import pandas
from pandas import DataFrame
from pandas import Series
from sample import grade_dic
from print_df import print_df

# 샘플 데이터 만들기
df = DataFrame(grade_dic, index=['철수', '영희', '민철', '수현', '호영'])
print_df(df)



# 열 추가하기
# -> 리스트 형식으로 추가할 경우 행의 수에 맞게 추가되어야 한다.
df['한국사'] = [92, 83, 72, None, 80]
print_df(df)



# -> 새로운 열에 하나의 값을 지정하면 모든 행이 동일한 값을 갖는다.
df['세계사'] = 100
print_df(df)



# 시리즈를 통한 열 추가
# -> 각 값이 연결될 행의 이름(index)를 지정해야 한다.
# -> 이 경우는 부분적으로 값을 비워 둘 수 있다.
#   (여기서는 호영의 데이터 생략)
df['사회'] = Series([82, 90, 92, 64],
                  index=['철수', '영희', '민철', '수현'])
print_df(df)




# 열 삭제하기
# -> 컬럼 이름을 통한 열 삭제
# -> inplace=True 파라미터를 추가할 경우
#   원본 자체에서 삭제되고 리턴되는 객체는 없다.
#   (여기서는 사용 안함)
k1 = df.drop('사회', axis=1)
print_df(k1)



# 여러 열을 동시에 삭제하기 -> 열 이름을 리스트로 지정
k2 = df.drop(['영어', '세계사', '사회', '과학'], axis=1)
print_df(k2)



# -> 인덱싱을 통한 4번째(0부터 카운트)열 삭제하기
# -> axis=0 : 행 삭제(기본값), axis=1 : 열 삭제
k3 = df.drop(df.columns[4], axis=1)
print_df(k3)



# -> 슬라이싱을 통한 2번째 열 부터 4번째 열 전까지 삭제하기
k4 = k1.drop(k1.columns[2:4], axis=1)
print_df(k4)





# 특정 열만 필터링해서 새로운 데이터 프레임 만들기
fl = df.filter(items=['국어','수학'])
print_df(fl)
