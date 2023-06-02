# Class_Student_FileIO
# Author : LeeSeungJun
# Student ID : 22312050
# Dept : Info & Comm. Eng
# Date : May 5, 2023
# Major features :

# 학생 정보 처리르 위한 Class_Student 구현
class Student_FileIO(object):

    # 데이터 멤버로 이름,국어,영어,수학,과학,성적합산,평균성적을 설정
    __slots__ = ['name', 'kor', 'eng', 'math', 'sci', 'sumScore', 'avgScore']
    
    # name,kor,eng,math,sci 정의
    def __init__(self, name, kor, eng, math, sci):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math
        self.sci = sci
        
    def __str__(self):
        return "Student({:>8s}, {:3d}, {:3d}, {:3d})".format(self.name, self.kor, self.eng, self.math, self.sci)

# 객체 fin으로 부터 학생정보를 읽어 들이고, class Student 인스탄스를 생성하여 리스트 L_students에 반환하여 준느 함수 fread_st_data
def fread_st_data(fin):
    L_st = []
    for line in fin:
        name, kor, eng, math, sci = line.split()
        st = Student_FileIO(name, int(kor), int(eng), int(math), int(sci))
        L_st.append(st)
    return L_st

# L_st를 한줄한줄 출력시켜주는 printStudents 함수
def printStudents(L_st):
    for st in L_st:
        print(st)
    
# L_st의 합산과 평균을 계산해주는 calculate_st_scores 함수
def calculate_st_scores(L_st):
    for st in L_st:
        st.sumScore = st.kor + st.eng + st.math + st.sci
        st.avgScore = st.sumScore / 4.0

# file_name에 L_st를 write해주는 fwrtie_st_records 함수
def fwrite_st_records(file_name, L_st):
    f = open(file_name, 'w')
    heading = "{:>6s}{:>6s}{:>6s}{:>6s}{:>6s}{:>6s}{:>8s}".format("name", "kor", "eng", "math", "sci", "sum", "avg")
    f.write(heading)
    f.write("\n" + "-" * 44 + "\n")
    for st in L_st:
        s = "{0:>6s}".format(st.name)
        s += "{0:6d}".format(st.kor)
        s += "{0:6d}".format(st.eng)
        s += "{0:6d}".format(st.math)
        s += "{0:6d}".format(st.sci)
        s += "{0:6d}".format(st.sumScore)
        s += "{0:8.2f}".format(st.avgScore)
        s += '\n'
        f.write(s)
    f.close()