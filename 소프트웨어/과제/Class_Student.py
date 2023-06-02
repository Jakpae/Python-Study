# Class_Student
# Author : LeeSeungJun
# Student ID : 22312050
# Dept : Info & Comm. Eng
# Date : May 1, 2023
# Major features :
# - Implement a class student that inherits the class person implemented earlier

from Class_Person import *

class Student(Person):
    # 생성자(init)으로 이름, 나이, 학번 , 전공, 학점을 초기화
    def __init__(self, name, age, st_id, major, gpa):
        Person.__init__(self, name, age) 
        self.setMajor(major)
        self.setSTID(st_id)
        self.setGPA(gpa)
    
    # Major(전공) 정의
    def getMajor(self):
        return self.major 
    
    # st_id(학번) 정의
    def getSTID(self):
        return self.st_id 
    
    # GPA(학점) 정의
    def getGPA(self):
        return self.GPA
    
    # Major(전공) 구현 및
    # 만약 전공이 EE,ICE,ME,CE,CS,SE 중에 없다면 오류 코드 발생
    def setMajor(self, major):
        set_majors = {"EE", "ICE", "ME", "CE", "CS", "SE"} 
        if major in set_majors:
            self.major = major
        else:
            print("*** Error in setting major (name:{}, age:{})".format(self.name, major))
            self.major = '---'
            
    def __lt__(self, other):
        if (self.GPA > other.GPA):
            return True 
        else:
            return False 
    
    # st_id(학번) 구현
    def setSTID(self, st_id):
        self.st_id = st_id
        
    # GPA(학점) 구현
    def setGPA(self, gpa):
        self.GPA = gpa
    
    # Name, Age, STID, Major, GPA를 줄맞춤하고 우측정렬하여 출력
    def __str__(self):
        return "Student({:>8s}, {:>3d}, {:>6d}, {:>5s}, {:3.2f})".format(self.getName(), self.getAge(), self.getSTID(), self.getMajor(),self.getGPA())
    
def compareStudent(st1, st2, key, sorting_order):
    
    # 만약 비교 기준이 st_id라면 실행
    if key == "st_id":
        # 만약 st1의 st_id와 st2의 st_id가 같다면 0을 리턴
        if st1.st_id == st2.st_id:
            return 0
        # 만약 sorting_order 가 increasing 이라면 실행
        elif sorting_order == "increasing":
            # st1의 st_id가 st2의 st_id보다 크다면 -1 리턴 작다면 1 리턴
            return -1 if (st1.st_id < st2.st_id) else 1
        # 만약 sorting_order 가 increasing 이 아니라면 실행
        else:
            # st1의 st_id가 st2의 st_id보다 작다면 -1 리턴 크다면 1 리턴
            return -1 if (st1.st_id > st2.st_id) else 1
        
    # 만약 비교 기준이 name이라면 실행
    if key == "name":
        # 만약 st1의 st_id와 st2의 st_id가 같다면 0을 리턴
        if st1.name == st2.name:
            return 0
        # 만약 sorting_order 가 increasing 이라면 실행
        elif sorting_order == "increasing":
            # st1의 st_id가 st2의 st_id보다 크다면 -1 리턴 작다면 1 리턴
            return -1 if (st1.name < st2.name) else 1
        # 만약 sorting_order 가 increasing 이 아니라면 실행
        else:
            # st1의 st_id가 st2의 st_id보다 작다면 -1 리턴 크다면 1 리턴
            return -1 if (st1.name > st2.name) else 1
        
    # 만약 비교 기준이 GPA라면 실행
    if key == "GPA":
        # 만약 st1의 st_id와 st2의 st_id가 같다면 0을 리턴
        if st1.GPA == st2.GPA:
            return 0
        # 만약 sorting_order 가 increasing 이라면 실행
        elif sorting_order == "increasing":
            # st1의 st_id가 st2의 st_id보다 크다면 -1 리턴 작다면 1 리턴
            return -1 if (st1.GPA < st2.GPA) else 1
        # 만약 sorting_order 가 increasing 이 아니라면 실행
        else:
            # st1의 st_id가 st2의 st_id보다 작다면 -1 리턴 크다면 1 리턴
            return -1 if (st1.GPA > st2.GPA) else 1
    

# 비교한 결과를 토대로 학생들을 정렬
def sortStudent(L_st, key, sorting_order):
    for i in range(0, len(L_st)): 
        min_idx = i
        for j in range(i+1, len(L_st)):
            if compareStudent(L_st[j], L_st[min_idx], key, sorting_order) < 0:
                min_idx = j
        if min_idx != i:
                L_st[i], L_st[min_idx] = L_st[min_idx], L_st[i]
 
# L_st에 있는 학생들을 순서대로 출력               
def printStudents(L_st):
        for st in L_st: 
            print(st)
