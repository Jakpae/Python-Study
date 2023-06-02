# Homework 4.2
# Author : LeeSeungJun
# Student ID : 22312050
# Dept : Info & Comm. Eng
# Date : March 23, 2023
# Major features :
# - Input Hour , Mininute , Second
# - How long time to lapse in that day
# - How long time remain in that day
# 하루는 86400초

while True:

    # 시 분 초를 문자열 리스트 형태로 입력받은후 split()을 이용해 hour , mini , sec로 나눈후 map을 사용해 정수로 변환
    hour, mini, sec = map(int, input("Input hour min sec : ").split())

    # 입력받은 시 분 초 문자열을 출력함
    print("Input time : ({:02d}:{:02d}:{:02d})".format(hour, mini, sec))

    # 0시 0분 0초 로부터 몇 초가 경과했는지 계산
    elapsed_time = hour * 3600 + mini * 60 + sec

    # 몇초가 경과했는지 출력
    print("Elapsed seconds from last midnight = {}".format(elapsed_time))

    # 자정까지 몇초가 남았는지 계산
    remain = 86400 - elapsed_time

    # 자정까지 몇초가 남았는지 계산한 값을 출력
    print("Remaining seconds to next-midnight = {}".format(remain))
