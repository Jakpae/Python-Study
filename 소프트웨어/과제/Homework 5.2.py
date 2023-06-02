# Homework 5.2
# Author : LeeSeungJun
# Student ID : 22312050
# Dept : Info & Comm. Eng
# Date : March 30, 2023
# Major features :
# - Input year , month , day
# - Calculate this day what Zodiac_sign

# While 무한반복문
while True:
    # 입력받은 3개의 문자열 데이터를 split으로 나눈후 map을 사용해 정수로 변환시켜 각각 yr, mn, dy에 입력시킴
    yr, mn, dy = map(int, input(
        "input data (year month day; 0 0 0 to quit) : ").split())

    if yr+mn+dy == 0:
        break

    # 별자리 찾기를 위한 tuple list 구성
    zodiac = ("", "Capricorn", "Aquarius", "Pisces", "Aries", "Taurus",
              "Gemini", "Cancer", "Leo", "Virgo", "Libra", "Scorpio", "Sagittarius")

    t = mn

    # Zodiac tuple-list를 사용해 별자리 찾기
    if dy > 21:
        t += 1
    if t == 13:
        t = 1

    # 입력받았던 yr, mn , dy 와 구한 별자리를 출력
    print("Your birth date = year({}), month({}), day({}) => Zodica_sign = {}".format(
        yr, mn, dy, zodiac[t]))
