# Homwork 9.2
# Author : LeeSeungJun
# Student ID : 22312050
# Dept : Info & Comm. Eng
# Date : May 7, 2023

from Class_Country import *

def main():
    # demography.txt에 있는 값을 read하는 f_demo 실행
    f_demo = open("demography.txt", 'r')
    # fget_countrydata를 이용해 f_demo의 값을 L_country에 넣음
    L_country = fget_CountryData(f_demo)
    # f_demo 종료
    f_demo.close()
    
    print("List of countries (input data):")
    # print_countries 함수를 사용해 L_country 출력
    print_countries(L_country)
    
    print("\nList of countries sorted by name:")
    # L_country를 name을 기준으로 오름차순 정렬
    sort_countries(L_country,"name","increasing")
    print_countries(L_country)
    
    print("\nList of countries sorted by demography(number of people):")
    # L_country를 population을 기준으로 내림차순 정렬
    sort_countries(L_country,"population","decreasing")
    print_countries(L_country)
    
    print("\nList of countries sorted by area:")
    # L_country를 area를 기준으로 내림차순 정렬
    sort_countries(L_country,"area","decreasing")
    print_countries(L_country)

# 만약 name이 main이라면 main()실행
if __name__ == "__main__":
    main()