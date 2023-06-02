# Exam1C
# Author : LeeSeungJun
# Student ID : 22312050
# Dept : Info & Comm. Eng
# Date : April 23, 2023

# Class_Student 모듈 import
from Class_Student import *

def main():
    print("2023-1 컴사파Exam1C_22312050_이승준")
    # 학생들 리스트 설정
    L_students = [
        Student("Kim_YD", 33333, "EE", 4.0),
        Student("Lee_CS", 88888, "ME", 4.2),
        Student("Park_KW", 11111, "ICE", 4.3),
        Student("Hong_CH", 22222, "CE", 4.1),
        Student("Yoon_DS", 77777, "ICE", 4.2),
        Student("Choi_HS", 12345, "CS", 3.9),
        Student("Adams", 13579, "AA", 4.4),
        Student("Zulu", 98765, "WW", 3.8),
        Student("Indian", 66554, "KK", 3.7),
        Student("Delta", 55443, "MM", 4.5)
    
    # 정렬되지않은 리스트와 정렬된 리스트 출력
    ]
    print("students before sorting : ")
    printStudents(L_students)
    sortStudents(L_students, "name", "increasing")
    
    print("\nstudents after sorting by name (increasing order) :")
    printStudents(L_students)
    sortStudents(L_students, "st_id", "increasing")
    
    print("\nstudents after sorting by student_id (increasing order) :")
    printStudents(L_students)
    sortStudents(L_students, "GPA", "decreasing")
    
    print("\nstudents after sorting by GPA (decreasing order) :")
    printStudents(L_students)
    
if __name__ == "__main__":
    main()