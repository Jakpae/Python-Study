# St_Data_Process
# Author : LeeSeungJun
# Student ID : 22312050
# Dept : Info & Comm. Eng
# Date : May 3, 2023
# -

# fin에 파일에 있는 데이터를 불러오는 함수 fread_data 생성
def fread_data(fin):
    # fin파일을 read 상태로 엶
    fin = open(fin, 'r')
    # While True 반복문
    while True: # repeat until the end of file
        # fin의 데이터를 read 한후에 read_date로 설정
        read_data = fin.read()
        # 만약 read_data가 비어있다면 break
        # 비어있지 않다면 print()실행
        if read_data == '':
            break
        print()
        
    fin.seek(0)
    
    # 빈 튜플리스트 tep설정
    tep = [[],[],[],[],[],[],[],[],[],[]]
    # i를 0으로 설정
    i = 0
    # readlines를 사용해 fin의 데이터를 받아옴
    for line in fin.readlines():
        # tep 튜플리스트에 line값을 뛰어쓰기 기준으로 나눠서 입력
        tep[i] = line.split()
        # i를 1추가
        i += 1
    # 파일 read 종료
    fin.close()
    
    return tep

# L_st_data의 값을 가져와 합산과 평균을 구한후 리턴시켜주는 함수 calculate_scores 생성
def calculate_scores(L_st_data):
    # 학생별 점수의 합산(sum) 및 평균점수(avg)를 계산 및 추가
    for student in L_st_data:
        # 각 학생의 국어/영어/수학/과학 성적을 정수형으로 변환하여 리스트에 저장
        scores = [int(score) for score in student[1:]]
        # 학생별 점수합산(sum) 계산
        total_score = sum(scores)
        # 학생별 평균점수(avg) 계산
        avg_score = total_score / len(scores)
        # 학생 정보 리스트에 합산점수(sum) 및 평균점수(avg) 추가
        student.append(total_score)
        student.append(avg_score)
    
    # 각 과목별 평균 점수 계산
    num_students = len(L_st_data)
    kor_sum, eng_sum, math_sum, sci_sum = 0, 0, 0, 0
    # L_st_data에 있는 값을 이용해 kor,eng,math,sci의 합산 점수 계산
    for student in L_st_data:
        kor_sum += int(student[1])
        eng_sum += int(student[2])
        math_sum += int(student[3])
        sci_sum += int(student[4])
    # 합산 점수 나누기 학생수를 하여서 평균을 계산
    kor_avg = kor_sum / num_students
    eng_avg = eng_sum / num_students
    math_avg = math_sum / num_students
    sci_avg = sci_sum / num_students
    
    # 각 과목별 평균 점수 반환
    return kor_avg, eng_avg, math_avg, sci_avg


# L_st를 filename에 입력시켜주는 함수 생성
def fwrite_st_records(filename, L_st):
    # file을 write하는 
    with open(filename, "w") as f:
        # 헤더 정보 쓰기
        f.write("======================================\n")
        f.write("name | kor  eng math  sci  sum   avg\n")
        f.write("-----+--------------------------------\n")
        # 데이터 쓰기
        for record in L_st:
            line = f"{record[0]:<5} | {record[1]:>3}, {record[2]:>3}, {record[3]:>3}, {record[4]:>3}, {record[5]:>3}, {record[6]:>5.2f}\n"
            f.write(line)
        # 바닥줄 쓰기
        f.write("======================================\n")