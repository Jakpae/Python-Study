# Class_Student
# Author : LeeSeungJun
# Student ID : 22312050
# Dept : Info & Comm. Eng
# Date : April 23, 2023

from Class_Person import *

class Student(Person):
    def __init__(self,name,st_id,major,gpa):
        Person.__init__(self, name) 
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
    
    def setMajor(self, major):
        self.major = major
    
    # st_id(학번) 구현
    def setSTID(self, st_id):
        self.st_id = st_id
        
    # GPA(학점) 구현
    def setGPA(self, gpa):
        self.GPA = gpa
    
    def __str__(self):
        return "Student({:>8s}, {:>7d}, {:>3s}, {})".format(self.getName(), self.getSTID(), self.getMajor(),self.getGPA())

def compareStudent(st1, st2, compare, sort_order):
        
        # 만약 비교 기준이 학번이라면 학생들을 학번 기준 오름차순으로 비교
        if compare == "st_id":
            if st1.st_id < st2.st_id:
                return True
            else:
                return False
        
        # 만약 비교 기준이 이름이라면 학생들을 학번 기준 오름차순으로 비교
        elif compare == "name":
            if st1.name < st2.name: 
                return True
            else:
                return False
            
        # 만약 비교 기준이 학점이라면 학생들을 학번 기준 내림차순으로 비교
        elif compare == "GPA": 
            if st1.GPA > st2.GPA:
                return True 
            else:
                return False 
            
        # 비교 기준이 학번,이름,학점이 아니라면 아무것도 리턴하지 않음
        else:
            return None
        
def sortStudents(L_st, compare, sort_order):
        for i in range(0, len(L_st)): 
            min_idx = i
            for j in range(i+1, len(L_st)):
                if compareStudent(L_st[j], L_st[min_idx], compare, sort_order): 
                    min_idx = j
            if min_idx != i:
                L_st[i], L_st[min_idx] = L_st[min_idx], L_st[i]

def printStudents(L_st):
        for st in L_st: 
            print(st)
            
            