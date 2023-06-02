# 실습 12.1
# Author : LeeSeungJun
# Student ID : 22312050
# Dept : Info & Comm. Eng
# Date : June 1, 2023

# 엑셀파일 read 와 계산을 위한 모듈 pandas Import
import pandas as pd

# pandas의 엑셀파일(csv) Read 기능을 사용해서 엑셀파일의 데이터를 가져와 DaeGu_Temp 변수에 넣음
DaeGu_Temp = pd.read_csv("DaeguTemp_2013_2022_CSV.csv")

# 불러온 DaeGu_Temp 데이터를 출력
print("DaeGu_Temp = \n", DaeGu_Temp)
#Avg_DaeGu_Temp = DaeGu_Temp['Avg']
#print("Avg_DaeGu_Temp =")
#print(Avg_DaeGu_Temp)

# 대구 온도에 대한 Describe를 Print 실행
print("DaeGu_Temp.describe() =")
print(DaeGu_Temp.describe())

# 엑셀파일에 있는 대구의 최대 온도를 Print
DaeGu_Temp_highest = DaeGu_Temp['High'].max()
print("temp_DG_highest = ", DaeGu_Temp_highest)

# 엑셀파일에 있는 대구의 최저 온도를 Print
DaeGu_Temp_lowest = DaeGu_Temp['Low'].min()
print("DaeGu_Temp_lowest = ", DaeGu_Temp_lowest)

# 엑셀파일에 있는 대구의 최대온도가 있었던 날을 출력
DaeGu_Temp_highest_day = DaeGu_Temp[DaeGu_Temp.High >= DaeGu_Temp_highest]
print("DaeGu_Temp_highest_day = "); print(DaeGu_Temp_highest_day)

# 엑셀파일에 있는 대구의 최저온도가 있었던 날을 출력
DaeGu_Temp_lowest_day = DaeGu_Temp[DaeGu_Temp.Low <= DaeGu_Temp_lowest]
print("DaeGu_Temp_lowest_day = "); print(DaeGu_Temp_lowest_day)