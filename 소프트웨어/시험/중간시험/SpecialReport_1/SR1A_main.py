# SR1A_main.py

from MyMath import *

def main():
    st_id = 22312050
    name = "이승준"
    print("2023-1 SW&AI_Exam1A 학번 = {}, 성명 = {}".format(st_id,name))
    
    step_deg = 45
    printTrigonometricTable(step_deg)
    
    step_deg = 30
    printTrigonometricTable(step_deg)    
    
if __name__ == "__main__":
    main()
    
