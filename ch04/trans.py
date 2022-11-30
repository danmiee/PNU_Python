# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 16:35:47 2022

@author: user
"""

import usecsv, re

E = '''Geological Sciences Samples
In the pdf link below, the first two one-page statements written by students in the geological sciences are interesting to compare to each other. Despite their different areas of research specialization within the same field, both writers demonstrate a good deal of scientific fluency and kinship with their target programs.'''

K = '''지질학 샘플
아래 pdf 링크에서 지질학과 학생들이 쓴 첫 두 장의 한 페이지짜리 문장을 서로 비교해 보면 흥미롭다. 같은 분야 내에서 다른 연구 전문 분야에도 불구하고, 두 작가는 그들의 목표 프로그램과 상당한 과학적 유창성과 친족 관계를 보여준다.'''

# 마침표(.)를 기준으로 나누기
E_list = re.split(r'\.', E)
K_list = re.split(r'\.', K)

# 데이터 저장할 리스트 생성
total = [['영문','한글']]

# 리스트에 데이터 넣어주기
for i in range(len(E_list)):
    total.append([E_list[i], K_list[i]])

# csv 파일로 저장
usecsv.writecsv("EKtrans.csv", total)