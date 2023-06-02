# Homework 7.1
# Author : LeeSeungJun
# Student ID : 22312050
# Dept : Info & Comm. Eng
# Date : April 15, 2023
# Major features :
# - Preparing for the Custom Module Class_Person.py and Class_Studnet.py

# 학생 정보 출력과 정렬을 위한 Class_Student 패키지의 모든 변수, 함수, 클래스를 가져옴
from Class_Student import *

# __main__ 이라면 실행
if __name__ == "__main__":
    # 학생 정보를 class Studnet의 인스턴트로 생성
    students = [
        Student("Kim", 21, 12345, "EE", 4.0), 
        Student("Lee", 22, 11234, "ME", 4.2), 
        Student("Park", 20, 10234, "ICE", 4.3), 
        Student("Hong", 19, 13123, "CE", 4.1), 
        Student("Yoon", 23, 11321, "ICE", 4.2), 
        Student("Wrong", 250, 15321, "??", 3.2), 
        Student("Alpha", 18, 10111, "CS", 4.4), 
        Student("Zedai", 19, 10222, "ICE", 4.4), 
        Student("Beta", 20, 11333, "SE", 3.9), 
        Student("Oliver", 21, 12555, "CE", 3.8)
    ]

    print("students before sorting : ")
    # 학생 정보를 출력
    printStudents(students)
    
    # "name" 즉 학생 이름 기준으로 정렬
    sortStudent(students, "name") 
    print("\nstudents after sorting by name : ") 
    printStudents(students)
    
    # "st_id" 즉 학번 기준으로 정렬
    sortStudent(students, "st_id")
    print("\nstudents after sorting by student_id : ") 
    printStudents(students)
    
    # "GPA" 즉 성적 기준으로 정렬
    sortStudent(students, "GPA")
    print("\nstudents after sorting by GPA in decreasing order : ") 
    printStudents(students)