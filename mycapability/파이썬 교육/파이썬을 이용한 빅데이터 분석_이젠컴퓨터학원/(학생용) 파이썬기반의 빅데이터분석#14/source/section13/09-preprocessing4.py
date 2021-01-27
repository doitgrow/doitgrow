# -*- coding: utf-8 -*-
# 모듈 참조
from print_df import print_df
from pandas import DataFrame
from pandas import Series
from sample import grade_dic

# 샘플 데이터 준비
df = DataFrame(grade_dic,
               index=['철수', '영희', '민철', '수현', '호영'])
print_df(df)


# 행 삭제하기
# -> 추가는 원본 자체가 변하지만
#    삭제는 결과가 반영된 새로운 복사본이 생성된다.
k1 = df.drop("철수")
print_df(k1)



# 한 번에 여러 행 삭제하기
k2 = df.drop(["철수", "영희", "호영"])
print_df(k2)



# -> 인덱싱을 통한 0번째행 삭제하기
k3 = df.drop(df.index[0])
print_df(k3)



# -> 슬라이싱을 통한 3번째 행 부터 7번째 행 전까지 삭제하기
k4 = df.drop(df.index[3:7])
print_df(k4)



# drop 함수에 inplace=True 파라미터를 추가하면 원본 자체에서 삭제된다.
df.drop(['영희','수현'], inplace=True)
print_df(df)

