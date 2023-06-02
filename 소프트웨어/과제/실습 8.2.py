# 실습 8.2
# Author : LeeSeungJun
# Student ID : 22312050
# Dept : Info & Comm. Eng
# Date : April 28, 2023
# Major features :

# 사용자 정의 클래스 Class_InterCityDistTbl import
from Class_InterCityDistTbl import *

# 만약 __main__ 이라면 실행
if __name__ == "__main__":
    ICD_tbl = InterCityDistTbl()
    # 두 도시의 이름과 두 도시 사이의 거리가 있는 튜플 리스트
    L_ICD_data = [("SL", "DJ", 150), ("DJ", "DG", 150), ("SL", "DG", 300), ("DG", "BS", 130),\
        ("SL", "BS", 430), ("DG", "GJ", 180), ("DJ", "GJ", 160), ("SL", "GJ", 310),\
            ("GJ", "BS", 210), ("DJ", "BS", 280), ("SL", "SC", 165), ("DJ", "SC", 193),\
                ("SC", "BS", 235), ("SC", "DG", 202), ("SC", "GJ", 340) ]
    # L_ICD_data 를 setICDTable를 사용해 set 집합자료형으로 만든후 출력 & 딕셔너리 저장
    ICD_tbl. setICDTable(L_ICD_data)
    # Inter_City_Distance_Table 출력
    print("\nInter_City_Distance_Table :\n ", ICD_tbl)
    while True:     
        c1,c2 = input("Two cities names to find distance : ").split(' ') 
        if c1 == '.':
            break
        # getICD를 이용해 딕셔너리에서 두 도시 사이의 거리를 구한후 dist에 저장
        dist = ICD_tbl.getICD(c1, c2)
        print("Distance({}, {}) = {}".format(c1, c2, dist))