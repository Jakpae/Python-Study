# Class_Mtrx
# Author : LeeSeungJun
# Student ID : 22312050
# Dept : Info & Comm. Eng
# Date : April 23, 2023

class Mtrx:
    # 초기화 메서드 __init__ 을 사용해서 어떤 클래스의 객체가 만들어질 떄 자동으로 호출되어 그 객체가 갖게될 여러가지 성질을 정해 주는 역할
    def __init__(self,name,n_row,n_col,lst_data):
        self.setName(name)
        self.n_row = n_row
        self.n_col = n_col
        tep_row = []
        self.rows = []
        tep = 0
        for r in range(0,self.n_row):
            for c in range(0,self.n_col):
                tep_row.append(lst_data[tep])
                tep += 1
            self.rows.append(tep_row)
            tep_row = []
    
    # setName 메서드
    def setName(self, nm):
        self.name = nm
    
    # print() 함수로 출력할 떄 사용되는 문자열을 제공하기 위한 __str__() 함수
    def __str__(self):
        print('{} ='.format(self.name))
        s = ''
        for i in range(0, self.n_row):
            for j in range(0, self.n_col):
                s += "{:6.2f}".format(self.rows[i][j])
            s += "\n"
        return s
        
    # __add__ 메서드 (덧셈) 두 개의 객체 self와 other를 인자로 받아서 그 둘의 합을 구한후 Mtrx함수로 리턴해 행렬을 출력
    def __add__(self, other):
        lst_res = []
        for i in range(0, self.n_row):
            for j in range(0, self.n_col):
                r_ij= self.rows[i][j] + other.rows[i][j]
                lst_res.append(r_ij)
        return Mtrx("R", self.n_row, self.n_col, lst_res)
    
    # __sub__ 메서드 (덧셈) 두 개의 객체 self와 other를 인자로 받아서 그 둘의 차을 구한후 Mtrx함수로 리턴해 행렬을 출력
    def __sub__(self, other):
        lst_res = []
        for i in range(0, self.n_row):
            for j in range(0, self.n_col):
                r_ij= self.rows[i][j] - other.rows[i][j]
                lst_res.append(r_ij)
        return Mtrx("R", self.n_row, self.n_col, lst_res)
    
    # __mul__ 메서드 (덧셈) 두 개의 객체 self와 other를 인자로 받아서 그 둘의 곱을 구한후 Mtrx함수로 리턴해 행렬을 출력                
    def __mul__(self, other):
        lst_res = []
        for i in range(0, self.n_row):
            for j in range(0, other.n_col):
                r_ij= 0
                for k in range(0, self.n_col):
                    r_ij = r_ij + self.rows[i][k] * other.rows[k][j]
                lst_res.append(r_ij)
        return Mtrx("R", self.n_row, other.n_col, lst_res)
    
    
    def transpose(self):
        lst_res = [] # 빈리스트 생성
        
        # 기존의 열을 행으로, 행을 열로 바꾸어 lst_res에 저장하고 객체를 생성하고 저장
        for i in range(self.n_col):
            for j in range(self.n_row):
                lst_res.append(self.rows[j][i])
        return Mtrx("transpose", self.n_col, self.n_row, lst_res)
 
    
