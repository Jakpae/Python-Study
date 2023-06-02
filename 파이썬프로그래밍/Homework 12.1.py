# Homework 12.1
# Author : LeeSeungJun
# Student ID : 22312050
# Dept : Info & Comm. Eng
# Date : May 23, 2023


def printLPrices(L_p):
    print("length :", end='')
    # 막대기의 길이를 출력
    for i in range(len(L_p)):
        print("{:3d}".format(i+1), end=', ')
    # 각 막대기의 가격을 출력
    print("\nprice :", end='')
    for i in range(len(L_p)):
        print("{:3d}".format(L_p[i]), end=', ')
    # 줄바꿈
    print()


# 막대 자르기의 최대 수익 값과 포함된 막대 자르기의 길이와 가격을 출력
def printLCuttings(L_p, L_cuttings):
    print("selected cuttings : ", end='')
    # L_cuttings의 길이만큼 반복
    for i in range(len(L_cuttings)):
        print("[length({}) : price({})]".format(L_cuttings[i]+1, L_p[L_cuttings[i]]), end='')
    print()


# 막대기의 최대 길이와 각 길이 별 가격이 주어질 때, 막대기를 어떻게 잘라 판매하면 가장 큰 수익을 낼 수 있는지 찾기
def cutRod(price, max_len):
    # values, cut_points 리스트를 초기화하고 두 리스트이 길이를 max_len + 1로 설정하고 모두 0으로 설정
    # values 리스트는 각 길이에 대한 최대 수익을 저장하는데 사용
    values = [0] * (max_len + 1)
    # cut_points 리스트는 최대 수익에 도달하기 위한 각 길이에서의 최적의 자르기 지점을 저장하는데 사용
    cut_points = [0] * (max_len + 1)
    # 막대기의 길이만큼 반복
    for length in range(1, max_len + 1):
        # 최대 가치를 -1로 초기화
        max_value = -1
        # 가능한 모든 자르기 지점에 대해 반복
        for cut in range(length):
            # 현재 자르기 지점에서 얻을 수 있는 값을 계산
            current_val = price[cut] + values[length - cut - 1]
            # 현재 값이 최대 값보다 크면 최대 값을 현재 값으로 업데이트하고 cuut_points 리스트에 현재 자르기 지점을 저장
            if current_val > max_value:
                max_value = current_val
                cut_points[length] = cut
        # 최대 값이 계산되면 values리스트에 해당 길이에서의 값으로 설정
        values[length] = max_value
    # cuttings 리스트를 구성
    cuttings = []
    # max_len이 0이 될 때 까지 반복
    while max_len > 0:
        # 현재 길이에서 최적의 자르기 지점을 찾고 찾은 최적의 자르기 지점을 cuttings 리스트에 추가
        cut = cut_points[max_len]
        cuttings.append(cut)
        max_len -= cut + 1
    # 최대 수익값(values[len(pirce)])과 자른 막대기 조각에 대한 리스트(cuttings)를 반환
    return values[len(price)], cuttings


if __name__ == "__main__":
    # 막대기의 각 길이별 가격 리스트 L_price
    L_pr_a = [1, 5, 8, 9, 10, 17, 18, 20]
    L_pr_b = [2, 5, 8, 11, 14, 17, 20, 23]
    L_pr_c = [3, 5, 8, 11, 14, 17, 20, 23]
    # Case A,B,C 로 나눠서 3번 반복
    for L_name, L_p in [("case A", L_pr_a), ("case_B", L_pr_b), ("case_C", L_pr_c)]:
        print(L_name)
        printLPrices(L_p)
        max_len = len(L_p)
        max_rev, L_cuttings = cutRod(L_p, max_len)
        print("Maximum Obtainable Value with max length ({}) = {}".format(max_len, max_rev))
        printLCuttings(L_p, L_cuttings)