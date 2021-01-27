# -*- coding: utf-8 -*-
"""
07-glob.py > 파일이나 폴더 목록 검색하기 위한 모듈
"""
import glob as gl

# 현재 폴더의 모든 하위 요소들 조회
ls = gl.glob('*')
print(ls)
print('-' * 30)

# 현재 폴더에서 ".txt" 로 끝나는 모든 요소들 조회
ls = gl.glob('*.txt')
print(ls)
print('-' * 30)

# 현재 폴더에서 "0"으로 시작하는 모든 요소들 조회
ls = gl.glob('0*')
print(ls)
