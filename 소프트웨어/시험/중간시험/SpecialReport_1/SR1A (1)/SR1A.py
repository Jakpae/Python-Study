# SR1A
# Author : LeeSeungJun
# Student ID : 22312050
# Dept : Info & Comm. Eng
# Date : April 29, 2023
# Major features :
# - Radian units for deg values increasing in units of specified angle (step_deg) in the range of 0 to 360° (degree)
# - Calculate the rad value, calculate the trigonometric sin(rad) and cos(rad) values of this rad value, and output it in tabular form
# - Import custom module myMath Implement main() function using trigonometric table output function
# - Implement the module to run when the name (__name__) is "__main__"

# MyMath 모듈안에 있는 printTrigonmetricTable 함수 불러오기
from MyMath import prinTrigonometricTable

# main 함수 생성
def main():
    # 학번 이름 설정 및 출력
    st_id = 22312050
    name = "이승준"
    print("2023-1 SW&AI_SR1A 학번 : {}, 성명: {}".format(st_id,name))
    print()

    # 45도 각도의 printTrigonometricTable 출력
    step_deg = 45
    prinTrigonometricTable(step_deg)

    # 30도 각도의 printTrigonometricTable 출력
    step_deg = 30
    prinTrigonometricTable(step_deg)

# 만약 name이 main이라면 실행
if __name__ == "__main__":
    main()
