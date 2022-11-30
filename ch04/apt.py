# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 16:35:47 2022

@author: user
"""

import usecsv, re

# 파일 열어서 csv형 리스트(2차원 배열)로 변경
apt = usecsv.switch(usecsv.opencsv('apt_202211.csv'))
print(apt)

# 데이터 저장할 리스트 생성 및 필드명 설정
new = [["시군구","전용면적","거래금액","단지명"]]

# 저장할 내용 선택
for i in apt:
    try:
        if i[5]>84 and i[8]<=25000 and re.search(r'용호동',i[0]):
            new.append([i[0],i[5],i[8],i[4]])
    except:
        pass
    
# csv파일로 저장
usecsv.writecsv("aptover84_lower2500.csv", new)