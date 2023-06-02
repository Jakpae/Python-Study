# 실습 4.2
# Author : LeeSeungJun
# Student ID : 22312050
# Dept : Info & Comm. Eng
# Date : March 22, 2023
# Major features :
# - input year , month ,day
# - calculate birthstone

# While 무한반복문, Break로 끝낼수있음
while True:
    input_data_str = input("Input your birth data (year month day) : ")
    yr_mn_dy_strings = input_data_str.split()
    yr, mn, dy = map(int, yr_mn_dy_strings)
    if yr == 0:
        break

    daysFromJan01AD01 = 0

    # 윤년 계산을 위한 식
    for y in range(1, yr):
        if (((y % 4 == 0) and (y % 100 != 0)) or (y % 400) == 0):
            daysFromJan01AD01 += 366
        else:
            daysFromJan01AD01 += 365

    # 각 달의 마지막 날을 지정 , 리스트 제일앞에 0을 넣는 이유는 0월달을 존재하지 않기 때문에
    dayInMonth = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if (((yr % 4 == 0) and (yr % 100 != 0)) or (yr % 400) == 0):
        dayInMonth[2] = 29
    for m in range(1, mn):
        daysFromJan01AD01 += dayInMonth[m]
    daysFromJan01AD01 += dy

    # 탄생석 리스트 생성
    birthStone = ["", "Gernet", "Amethyst", "Aquamarine", "Diamond", "Emerald",
                  "Pearl", "Ruby", "Peridot", "Sapphire", "Opal", "Topaz", "Turquoise"]
    WeekDayNames = ["Sunday", "Monday", "Tuesday",
                    "Wednesday", "Thursday", "Friday", "Saturday"]
    WeekDay = daysFromJan01AD01 % 7

    # 출생일이 무슨 요일인지와 탄생석을 출력
    print("Your birth date = year({}), month({}), day({}) : ".format(yr, mn, dy))
    print(" elapsed {} days from Jan01AD01".format(daysFromJan01AD01))
    print(" week day = {}, birth_stone = {}".format(
        WeekDayNames[WeekDay], birthStone[mn]))
