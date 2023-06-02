#Exam1A
#Name : LeeSeungJun
#St_id : 22312050

from MyMath import prinTrigonometricTable

def main():
    # 학번 이름 설정 및 출력
    st_id = 22312050
    name = "이승준"
    print("2023-1 SW&AI_Exam1A 학번 : {}, 성명: {}".format(st_id,name))
    print()

    # 45도 각도의 printTrigonometricTable 출력
    step_deg = 45
    prinTrigonometricTable(step_deg)

    # 30도 각도의 printTrigonometricTable 출력
    step_deg = 30
    prinTrigonometricTable(step_deg)

if __name__ == "__main__":
    main()
