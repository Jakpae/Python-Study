# Class_Mtrx
# Author : LeeSeungJun
# Student ID : 22312050
# Dept : Info & Comm. Eng
# Date : May 7, 2023
# - Implement Class custom class module __init__ , setName , __str__ , __add__ , __sub__ , __mul__


class Mtrx:
    # 초기화 메서드 __init__ 을 사용해서 어떤 클래스의 객체가 만들어질 떄 자동으로 호출되어 그 객체가 갖게될 여러가지 성질을 정해 주는 역할
    def __init__(self, n_row, n_col, L_data):
        self.n_row = n_row
        self.n_col = n_col
        tep_row = []
        self.rows = []
        tep = 0
        for r in range(0, self.n_row):
            for c in range(0, self.n_col):
                tep_row.append(L_data[tep])
                tep += 1
            self.rows.append(tep_row)
            tep_row = []
    
    # setName 메서드
    def setName(self, nm):
        self.name = nm
    
    # print() 함수로 출력할 떄 사용되는 문자열을 제공하기 위한 __str__() 함수
    def __str__(self):
        s = '{} =\n'.format(self.name)
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
        return Mtrx(self.n_row, self.n_col, lst_res)
    
    # __sub__ 메서드 (덧셈) 두 개의 객체 self와 other를 인자로 받아서 그 둘의 차을 구한후 Mtrx함수로 리턴해 행렬을 출력
    def __sub__(self, other):
        lst_res = []
        for i in range(0, self.n_row):
            for j in range(0, self.n_col):
                r_ij= self.rows[i][j] - other.rows[i][j]
                lst_res.append(r_ij)
        return Mtrx(self.n_row, self.n_col, lst_res)
    
    # __mul__ 메서드 (덧셈) 두 개의 객체 self와 other를 인자로 받아서 그 둘의 곱을 구한후 Mtrx함수로 리턴해 행렬을 출력                
    def __mul__(self, other):
        lst_res = []
        for i in range(0, self.n_row):
            for j in range(0, other.n_col):
                r_ij= 0
                for k in range(0, self.n_col):
                    r_ij = r_ij + self.rows[i][k] * other.rows[k][j]
                lst_res.append(r_ij)
        return Mtrx(self.n_row, other.n_col, lst_res)
    
# fin 받은후 첫줄에 있는 n_row, n_col을 받고 행렬을 만드는 fgetMtrx 함수
def fgetMtrx(fin):
    n_row, n_col = map(int, fin.readline().split())
    data = []
    for i in range(n_row):
        row_data = list(map(float, fin.readline().split()))
        data.extend(row_data)
    return Mtrx(n_row, n_col, data)