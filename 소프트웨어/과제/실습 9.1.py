# 실습 9.1
# Author : LeeSeungJun
# Student ID : 22312050
# Dept : Info & Comm. Eng
# Date : May 5, 2023
# Major features :

#  
from Class_Student_FileIO import *

def main():
    # open 을 사용해 student_records.txt 안에 파일을 Read해서 fin에 넣음
    # 파일 객체 = open(파일 이름, 파일 열기 모드)
    fin = open("student_records.txt", "r")
    # fread_st_data 함수를 사용해 Read해서 받은 데이터를 구분해서 L_student로 설정
    L_students = fread_st_data(fin)
    # open 종료
    fin.close()
    
    # L_student 출력
    print("L_students =")
    printStudents(L_students)
    
    # L_student의 성적 합산과 평균을 구한후 다시 L_Students로 리턴하는 Calculate_st_scores 함수
    calculate_st_scores(L_students)
    
    # 성적과 평균을 구한 L_Students를 result_st_records.txt파일에 write
    print("\nfwrite_st_data after calculate_st_score(L_studnets) .....")
    f_result_st_records = "result_st_records.txt"
    fwrite_st_records(f_result_st_records, L_students)
    
    # result_st_recodrs.txt 파일에 write 된걸 다시 read해서 출력
    print("\nContents of processed result file {}:".format(f_result_st_records))
    f_st = open(f_result_st_records,'r')
    while True:
        line = f_st.readline()
        if line == '':
            break
        print(line,end='')
    f_st.close()

# 만약 name이 main이라면 main()실행
if __name__ == "__main__":
    main()