# Homework 4.3
# Author : LeeSeungJun
# Student ID : 22312050
# Dept : Info & Comm. Eng
# Date : March 29, 2023
# Major features :
# - input nation and capital
# - check the country name and capital name
# - output dictionary

while True:

    # 중복일 경우 처음으로 돌아가 리스트가 초기화 되게 만듬
    list_key = []

    list_value = []

    # 국가의 이름과 수도 이름을 입력받아 문자열 형태로 key, value 에 저장 된후 key,value 리스트에 추가
    for i in range(10):
        (key, value) = tuple(
            map(str, input("Input nation and its capital (. to quit)  : ").split()))
        list_key.append(key)
        list_value.append(value)
        i += 1

        # 만약 .이 입력된다면 종료
        if key == ".":
            break

    # set을 활용해서 리스트안에 중복이 있는지 확인후 중복이 있으면 처음으로 없으면 게속 진행
    if len(list_key) == len(set(list_key)):
        print("중복이 없으므로 게속 진행됩니다")
        break
    else:
        print("중복이 있으므로 처음으로 돌아갑니다")
        continue

# 리스트에 있는 값을 딕셔너리에 넣음
dic = dict(zip(list_key, list_value))

# 입력된 딕셔너리 출력
print("dict_nation_capital :  {}".format(dic))

# 무한반복문을 사용해서 .가 입력되지 않으면 게속 국가의 수도 이름을 찾아냄
while True:
    count = input("Input nation to find its capital (. to quit) : ")
    if count == ".":
        break
    print("The capital of {} is {}".format(count, dic[count]))
