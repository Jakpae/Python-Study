# Module Class_Student.py
# Major features :
# - Implement printStudents(L_st) that output classStudents object list(L_st)
# - Implement compareStudents (st1, st2, key) that compare class Student objects according to specified criteria (key)
# - Implement sortStudents (L_st, key) that sort object lists (L_st) according to specified criteria (key)


from Class_Person import *

class Student(Person):
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
            self.major = None
    
    # st_id(학번) 구현
    def setSTID(self, st_id):
        self.st_id = st_id
        
    # GPA(학점) 구현
    def setGPA(self, gpa):
        self.GPA = gpa
        
    def __lt__(self, other):
        if (self.GPA > other.GPA):
            return True 
        else:
            return False 
        
    def __str__(self):
        return "Student({}, {}, {}, {}, {})".format(self.getName(), self.getAge(), self.getSTID(), self.getMajor(),self.getGPA())
    
def compareStudent(st1, st2, compare):
        
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
    

# 비교한 결과를 토대로 학생들을 정렬
def sortStudent(L_st, compare):
        for i in range(0, len(L_st)): 
            min_idx = i
            for j in range(i+1, len(L_st)):
                if compareStudent(L_st[j], L_st[min_idx], compare): 
                    min_idx = j
            if min_idx != i:
                L_st[i], L_st[min_idx] = L_st[min_idx], L_st[i]
 
# L_st에 있는 학생들을 순서대로 출력               
def printStudents(L_st):
        for st in L_st: 
            print(st)