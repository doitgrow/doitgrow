# -*- coding: utf-8 -*-

# 모듈, 데이터 참조
from pandas import DataFrame
from sample import grade_dic
# -> print_df.py 파일에서 print_df 함수 import
from print_df import print_df


# 데이터프레임 만들기
df = DataFrame(grade_dic, index=['철수', '영희', '민철', '수현', '호영'])
print_df(df)

# 컬럼 순서 변경
# -> 지정된 순서대로 열이 재정렬 된 결과가 반환된다.
# -> 원본은 변화 없음. 결과가 적용된 복사본이 생성된다.
df1 = df.reindex(columns=['국어','수학','과학','영어'])
print_df(df1)


# 인덱스(행) 순서 변경
# -> 지정된 순서대로 행이 재정렬 된 결과가 반환된다.
# -> 원본은 변화 없음. 결과가 적용된 복사본이 생성된다.
df2 = df.reindex(index=['철수','민철','호영','영희','수현'])
print_df(df2)


# 컬럼,인덱스 이름 변경
# -> "기존이름: 새이름" 형식의 딕셔너리로 지정
# -> columns와 index중 변경을 원하는 하나만 설정 가능.
# -> 원본은 변화 없음. 결과가 적용된 복사본이 생성된다.
df3 = df.rename(
        columns={'국어':'kor', '영어':'eng', '수학':'math', '과학': 'sinc'},
        index={'영희': 'yh', '수현':'sh', '호영':'hy', '철수':'cs', '민철': 'mc'} )
print_df(df3)

# 원본을 수정하고자 하는 경우 inplace 파라미터에 True를 지정한다.
df.rename(
    columns={'국어':'kor', '영어':'eng', '수학':'math', '과학': 'sinc'},
    inplace=True)
print_df(df)


