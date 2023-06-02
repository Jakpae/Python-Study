# Class_Country
# Author : LeeSeungJun
# Student ID : 22312050
# Dept : Info & Comm. Eng
# Date : May 7, 2023
# Major features :

class Country(object):
    
    # 데이터 멤버 name,captial,population,area를 포함
    __slots__ = ['name','capital','population','area']
    
    # name,capital,population,area를 정의
    def __init__(self,name,capital,population,area):
        self.name = name
        self.capital = capital
        self.population = population
        self.area = area
    
    # 출력을 위한 __str__ 함수
    def __str__(self, index):
        return "Country[{:>2d}] : Country [{:>10s},{:>13s},{:>11d},{:>10d}]".format(index+1, self.name, self.capital, self.population, self.area)

# 데이터 파일 객체로부터 국가 정보를 읽어 들이고, class_Country의 인스탄스를 생성하여 리스트에 반환하여 주는 함수 fget_CountryData
def fget_CountryData(f_demo):
    L_cu = []
    # 각 국가의 이름과 수도 인구수 면적을 split으로 나눠서 각각 L_cu에 넣음
    for line in f_demo:
        name,capital,populaton,area = line.split()
        st = Country(name,capital,int(populaton),int(area))
        L_cu.append(st)
    return L_cu
2
# L_country , 즉 국가 리스트를 한줄한줄 출력하는 print_countries 함수
def print_countries(L_country):
    for i, cu in enumerate(L_country):
        print(cu.__str__(i))

# st1의 국가와 st2의 국가를 key라는 비교대상으로 오름차순또는 내림차순으로 정렬하는 compare_countries 함수
def compare_countries(st1, st2, key, sorting_order):
    # 만약 비교 기준이 name라면 실행
    if key == "name":
        # 만약 st1의 name와 st2의 name가 같다면 0을 리턴
        if st1.name == st2.name:
            return 0
        # 만약 sorting_order 가 increasing 이라면 실행
        elif sorting_order == "increasing":
            # st1의 name가 st2의 name보다 크다면 -1 리턴 작다면 1 리턴
            return -1 if (st1.name < st2.name) else 1
        # 만약 sorting_order 가 increasing 이 아니라면 실행
        else:
            # st1의 name가 st2의 name보다 작다면 -1 리턴 크다면 1 리턴
            return -1 if (st1.name > st2.name) else 1
        
    # 만약 비교 기준이 population이라면 실행
    if key == "population":
        # 만약 st1의 population과 st2의 population가 같다면 0을 리턴
        if st1.population == st2.population:
            return 0
        # 만약 sorting_order 가 increasing 이라면 실행
        elif sorting_order == "increasing":
            # st1의 population과 st2의 population보다 크다면 -1 리턴 작다면 1 리턴
            return -1 if (st1.population < st2.population) else 1
        # 만약 sorting_order 가 increasing 이 아니라면 실행
        else:
            # st1의 population과 st2의 population보다 작다면 -1 리턴 크다면 1 리턴
            return -1 if (st1.population > st2.population) else 1
        
    # 만약 비교 기준이 area라면 실행
    if key == "area":
        # 만약 st1의 area와 st2의 area가 같다면 0을 리턴
        if st1.area == st2.area:
            return 0
        # 만약 sorting_order 가 increasing 이라면 실행
        elif sorting_order == "increasing":
            # st1의 area가 st2의 area보다 크다면 -1 리턴 작다면 1 리턴
            return -1 if (st1.area < st2.area) else 1
        # 만약 sorting_order 가 increasing 이 아니라면 실행
        else:
            # st1의 area가 st2의 area보다 작다면 -1 리턴 크다면 1 리턴
            return -1 if (st1.area > st2.area) else 1
    

# 비교한 결과를 토대로 학생들을 정렬
def sort_countries(L_st, key, sorting_order):
    for i in range(0, len(L_st)): 
        min_idx = i
        for j in range(i+1, len(L_st)):
            if compare_countries(L_st[j], L_st[min_idx], key, sorting_order) < 0:
                min_idx = j
        if min_idx != i:
                L_st[i], L_st[min_idx] = L_st[min_idx], L_st[i]