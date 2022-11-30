# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 16:35:47 2022

@author: user
"""

import usecsv

# 파일 열기
total = usecsv.opencsv('popSeoul.csv')

# csv형 리스트(2차원배열)로 바꾸기
newPop = usecsv.switch(total)

# 데이터 저장할 리스트 생성 및 필드명 지정
new = [['구','한국인','외국인','외국인 비율(%)']]

# 외국인 비율 3% 초과하는 경우만 리스트에 넣기
for i in newPop:
  foreign = 0
  try:
    # 각 구의 등록 외국인 비율
    foreign = round(i[2] / (i[1] + i[2]) * 100, 1)
    if foreign > 3:
        new.append([i[0], i[1], i[2], foreign])
  except:
    pass

# newPop.csv 파일로 저
usecsv.writecsv('newPop.csv', new)