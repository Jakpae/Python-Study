# Homework 11.1
# Author : LeeSeungJun
# Student ID : 22312050
# Dept : Info & Comm. Eng
# Date : May 21, 2023

# 엑셀파일의 정렬과 출력 데이터 입력을 위한 pandas 모듈 import
import pandas as pd

# Excel 파일을 pandas의 read_excel()함수를 사용해 읽고 데이터 프레임을 생성
df = pd.read_excel("students_scores.xlsx")
print("df = \n", df)
df_tmp = df.loc[:, ['Eng', 'Kor', 'Math', 'Sci']]

# 학생들의 성적 평균을 구함
avgs_per_student = df_tmp.mean(1)

# 각 학생의 과목 점수와 평균을 구함
df.loc[:, 'Avg'] = avgs_per_student


# 각 과목의 평균 출력
df_tmp = df.loc[:, ['Eng', 'Kor', 'Math', 'Sci', 'Avg']]
avgs_per_class = df_tmp.mean()
print("\navgs_per_class =")
print(avgs_per_class)

# 평균순으로 정렬해서 출력
df_sorted = df.sort_values(by='Avg', ascending=False)
df_sorted.loc[len(df_sorted), ['Eng', 'Kor', 'Math', 'Sci', 'Avg']]=\
    avgs_per_class
df_sorted.at[len(df_sorted)-1, 'st_name'] = 'Total_Avg'
print("\ndf_sorted_with_avg =")
print(df_sorted)

# 정렬한 데이터를 processed_scores 엑셀 파일에 Write
print("Writing df to excel file")
with pd.ExcelWriter("processed_scores.xlsx") as excel_writer:
    df_sorted.to_excel(excel_writer, sheet_name='Students Records')