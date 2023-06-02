# Homework 3.2
# Author : LeeSeungJun
# Student ID : 22312050
# Dept : Info & Comm. Eng
# Date : March 23, 2023
# Major features :
# - Input Year, Month, Day
# - Make Calendar

# 매 달의 마지막 날 설정
last_day = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# Year Month Day를 문자열(String)으로 입력
data_str = input("연(Year), 월(Month), 일(Day)을 입력해주세요 : ")

# 문자열 리스트 데이터를 .split()을 사용해 나눔
data = data_str.split()

# 입력받은 Year Month Day 데이터를 문자열 형식으로 출력
print("Input Year_Month_Day_String : {}".format(data))

# Map을 사용해서 .split()으로 나눈 데이터를 각각 실수(int)형식으로 year month day에 매핑시킴
year, month, day = map(int, data)

# 공백 출력
print()

# 지정된 달의 영문이름 출력

if month == 1:
    eng_month = "January"

if month == 2:
    eng_month = "February"

if month == 3:
    eng_month = "March"

if month == 4:
    eng_month = "April"

if month == 5:
    eng_month = "May"

if month == 6:
    eng_month = "June"

if month == 7:
    eng_month = "July"

if month == 8:
    eng_month = "August"

if month == 9:
    eng_month = "September"

if month == 10:
    eng_month = "October"

if month == 11:
    eng_month = "November"

if month == 12:
    eng_month = "December"


# 달력 상단의 나올 몇년 몇월 달력인지 출력
print("{} of Year {}".format(eng_month, year))

# 구분을 위한 = 28번 출력
print("="*28)

# 요일를 알기위해 SUN MON TUE WED THR FRI SAT 출력
print(" SUN MON TUE WED THR FRI SAT")

# 구분을 위한 - 28번 출력
print("-"*28)

# 윤년 계산을 위한 leap_year
leap_year = 0

# 윤년계산법 : 년도를 4로 나눴을때 나머지가 0이 나오며 100으로 나눴을때 나머지가 1이 나오지 않으며 400으로 나눴을때 나머지가 0이 나오면 윤년이므로 leap_year = 1 로 설정
if (year % 4 == 0):
    leap_year = 1

    if (year % 100 == 0):
        leap_year = 0

        if (year % 400 == 0):
            leap_year = 1

# 만약 윤년이 맞다면 2월의 마지막 날을 29일로 설정
if (leap_year == 1):
    last_day[1] = 29

# 윤년을 포함해서 서기 1년 1월 1일부터 입력된 전 년도까지의 모든 날을 더하는 공식
total = (year - 1) * 365 + (year - 1) // 4 - \
    (year - 1) // 100 + (year - 1) // 400

# 달력의 1일의 요일을 알기위해 입력된 년도의 입력된 전 달까지의 모든 날을 위에 구한 Total에 더함
for i in range(month-1):
    total += last_day[i]

# 달력의 1일의 요일을 알기 위해 7로 나눠 요일을 알아냄 ( 0:월, 1:화, 2:수, 3:목, 4:금, 5:토, 6:일)
start_month_day = total % 7

# 달력은 일요일부터 시작하기 때문에 ( 0:일 1:월 2:화 3:수 4:목 5:금 6:토) 로 만들어주기위해 1을 더해주고 일요일을 0으로 설정
start_month_day += 1

if start_month_day == 7:
    start_month_day = 0

# for을 사용해 달력의 1일의 요일이 오기 전까지는 공백을 출력
for i in range(start_month_day):
    print('    ', end='')

# for을 사용해 공백이 끝나면 1일부터 last[month-1] 즉 마지막날까지 출력하고 만약 (total + i) % 7 가 6, 즉 토요일이면 줄바꿈 실행
for i in range(1, last_day[month-1]+1):
    print(" {0:2d} ".format(i), end='')

    if (total + i) % 7 == 6:
        print()
