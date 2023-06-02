# Homework 8.1
# Author : LeeSeungJun
# Student ID : 22312050
# Dept : Info & Comm. Eng
# Date : May 3, 2023
# -

# txt파일의 데이터를 가져오고 합산과 평균을 구하는 함수를 구현한 ST_Data_Process 모듈을 구현 및 Import
from St_Data_Process import *

# main 함수 생성
def main():
    # st_records.txt안에 있는 데이터를 가져와 L_st_data 에 넣음
    L_st_data = fread_data("st_records.txt")
    # L_st_data를 출력
    for st in L_st_data:
        print(st)
    # calculate_scores 를 사용해서 L_st_data의 평균값을 구하고 리턴시켜 kor_avg,eng_avg,math_avg,sci_avg에 넣음
    kor_avg, eng_avg, math_avg, sci_avg = calculate_scores(L_st_data)
    
    # After calculate_scores 출력
    print("\nAfter calculate_scores(students)")
    print("======================================")
    print("{:5s}|{:^5s}{:^5s}{:^5s}{:^5s}{:^6s}{:^6s}".\
        format("name", "kor", "eng", "math", "sci", "sum", "avg"))
    print("-----+--------------------------------")
    # 합산과 평균이 포함된 L_st_data를 출력
    for data in L_st_data:
        s = ""
        s = "{0:<5s}|".format(data[0])
        s += "{0:>4},".format(data[1])
        s += "{0:>4},".format(data[2])
        s += "{0:>4},".format(data[3])
        s += "{0:>4},".format(data[4])
        s += "{0:4d},".format(data[5])
        s += "{0:6.2f}".format(data[6])
        print(s)
    print("======================================")
    # fwrite_st_recoreds를 이용해 L_st_data를 output.txt에 write
    fwrite_st_records("output.txt", L_st_data)
    
    # Kor,Eng,Math,SCi의 평균값 출력
    print("\nAverage score of each class :")
    print("Kor_avg  = {:5.2f}".format(kor_avg))
    print("Eng_avg  = {:5.2f}".format(eng_avg))
    print("Math_avg = {:5.2f}".format(math_avg))
    print("Sci_avg  = {:5.2f}".format(sci_avg))

# 만약 name이 main이라면 main() 실행
if __name__ == "__main__":
    main()