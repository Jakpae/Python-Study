# Class_InterCityDistTbl
# Author : LeeSeungJun
# Student ID : 22312050
# Dept : Info & Comm. Eng
# Date : April 28, 2023
# Major features :
#  - Create Custom Class InterCityDistTbl
#  - getICD function to find the distance between two cities
#  - sing set() collective data types

# InterCityDistTbl 클래스 생성
class InterCityDistTbl():
    # 생성자 __init__을 사용해 dict_ICD 정의
    def __init__(self): 
        self.dict_ICD = dict()
    def setICD(self, c1, c2, dist):
        self.dict_ICD[(c1, c2)] = dist
        #print("setICD: ({}, {}) : {} Km".format(c1, c2, dist))
    def setICDTable(self, L_ICD_tuples):
        # set()은 집합 자료형이다.
        # 집합 자료형의 특징
        # 중복을 허용하지 않는다.
        # 순서가 없다.
        S_ICD = set()
        # for 반복문을 사용해 S_ICD안에 L_ICE_tuples 즉, I_ICD_data를 대입하고 출력
        for icd_tuple in L_ICD_tuples:
            (c1, c2, dist) = icd_tuple
            S_ICD.add((c1, c2, dist))
        print("S_ICD = ", S_ICD)
        # 후에 두개의 도시의 거리를 찾을수있게 L_ICE_tuples를 setICD를 사용해서 딕셔너리로 만듬
        for icd in S_ICD:
            (c1, c2, dist) = icd
            #print("ICD ({}, {}) : {} km".format(c1, c2, d)) 
            self.setICD(c1, c2, dist)
    
    # 두 도시의 거리를 구하기 위한 getICD 함수
    def getICD(self, c1, c2):
        # 만약 두 도시 사이에 대한 거리에 대한 정보가 존재한다면 거리를 dist를 거리로 설정해서 거리가 출력되게 설정
        if (c1, c2) in self.dict_ICD:
            dist = self.dict_ICD[(c1, c2)]
        elif (c2, c1) in self.dict_ICD:
            dist = self.dict_ICD[(c2, c1)] 
        else:
            # 만약 두 도시 사이의 거리에 대한 정보가 없다면 dist를 None으로 설정해서 None이 출력되게 설정
            dist = None 
        return dist
    
    # 도시사이에 거리 표를 출력하기 위한 __str__ 함수
    def __str__(self):
        keys = self.dict_ICD.keys()
        L_city = []
        for key in keys:
            (city_1, city_2) = key
            if city_1 not in L_city:
                L_city.append(city_1) 
            if city_2 not in L_city:
                L_city.append(city_2) 
        #print("Cities : ", L_city) 
        s="        |"
        for city in L_city:
            s += "{:>10s}".format(city) 
        s += "\n----------+"
        for i in range(len(L_city)):
            s += "----------"
        s += "\n"
        for i in range(len(L_city)):
            s += "{:^10s}|".format(L_city[i]) 
            for j in range(len(L_city)):
                dist = self.getICD(L_city[i], L_city[j])
                if (dist == None) and (L_city[i] == L_city[j]):
                    s += "{:10d}".format(int(0))
                elif (dist == None) and (L_city[i] != L_city[j]):
                    s += "{:>10s}".format("unknown") 
                else:
                    s += "{:10d}".format(dist)
            s += "\n"
        return s