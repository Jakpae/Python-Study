# Homework 5.3
# Author : LeeSeungJun
# Student ID : 22312050
# Dept : Info & Comm. Eng
# Date : April 6, 2023
# Major features :
# - Input nation name
# - Separate country names by continent

# 국가 수도 대륙 튜플 리스트 생성
nation_info = [
    ('Korea', 'Seoul', 'Asia'),
    ('Japan', 'Tokyo', 'Asia'),
    ('China', 'Beijing', 'Asia'),
    ('USA', 'WasingtonDC', 'NorthAmerica'),
    ('UK', 'London', 'Europe'),
    ('France', 'Paris', 'Europe'),
    ('Italy', 'Roma', 'Europe'),
    ('Germany', 'Berlin', 'Europe'),
    ('Canada', 'Ottawa', 'NorthAmerica'),
    ('Egypt', 'Cairo', 'Africa')
]


# 국가 수도 대륙 리스트 출력
print("L_nation_info = {}".format(nation_info))


countrys = [[], [], [], []]

continents = [('Asia'), ('NorthAmerica'), ('Europe'), ('Africa')]

dict_country_capital_continent = {}

# 대륙에 따라 국가 이름을 분리 및 dict_country_capital_continent 생성
for i in range(len(nation_info)):
    country, capital, continent = nation_info[i]
    if continent == continents[0]:
        countrys[0].append(country)
    elif continent == continents[1]:
        countrys[1].append(country)
    elif continent == continents[2]:
        countrys[2].append(country)
    elif continent == continents[3]:
        countrys[3].append(country)

    capital_continent = (capital, continent)
    dict_country_capital_continent[country] = capital_continent

print("dict_country_capital_continent = {}".format(
    dict_country_capital_continent))


# dict_continent_nations 딕셔너리 생성
dict_continent_nations = dict(zip(continents, countrys))

# 각 대륙별로 국가를 출력
print("Countries in Asia = {}".format(dict_continent_nations['Asia']))
print("Countries in NorthAmerica = {}".format(
    dict_continent_nations['NorthAmerica']))
print("Countries in Europe = {}".format(
    dict_continent_nations['Europe']))
print("Countries in Africa = {}".format(
    dict_continent_nations['Africa']))

# . 이 입력될때까지 국가 이름을 입력받아 해당 국가의 수도 이름 및 대륙을 찾아내는 While-loop
while True:
    nation_name = input(
        "Input nation_name to find its information (. to quit) : ")
    if nation_name == '.':
        break
    print("The information of {} is {}".format(
        nation_name, dict_country_capital_continent[nation_name]))
