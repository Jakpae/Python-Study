# Exam1A
# Author : LeeSeungJun
# Student ID : 22312050
# Dept : Info & Comm. Eng
# Date : April 23, 2023

# 실수형 데이터의 입력과 리스트 L 반환 및 통계 분석 결과 출력을 위한 MyList 모듈
# 리스트 L의 병합정렬 결과 출력을 위한 MySortings 모듈 import
from MyList import *
from MySortings import *

def main():
    # 학번출력
    print("2023-1 컴싸파Exam1A 학번:22312050, 성명:이승준")
    # 리스트 L 반환
    L_data = get_float_list()
    ("list of input data : ", L_data)
    # 통계껼과 출력
    L_len, L_min, L_max, L_avg, L_var, L_std = get_statistics(L_data)
    print("L_len = {}, L_min = {}, L_max = {}, L_avg = {:.2f}, L_var = {:.2f}, L_std = {:.2f}"\
    .format(L_len, L_min, L_max, L_avg, L_var, L_std))
    
    # 리스트 L 병합정렬 실행 
    merge_sort(L_data)
    print("sorted list : ", L_data)
    
if __name__ == "__main__":
    main()

