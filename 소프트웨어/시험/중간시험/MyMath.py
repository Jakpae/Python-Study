import math # 계산을 위한 math 함수 import

# printinTrigonometricTable 함수 생성
def prinTrigonometricTable(step_deg):
    print(">>> Trigonmetric Table (step_deg = {}) <<<".format(step_deg))
    print("     deg|",end='')
    for i in range(0,361,step_deg):
        print("{:8d}".format(i),end='')
    print()
    
    # - 8번 출력 및 + 한번 출력
    print("-" * 8,end='')
    print("+",end='')

    # - 출력을 위한 tep 생성과 for 반복문 사용
    tep = int(360 / step_deg + 1)

    for i in range(tep):
        print("-" * 8,end='')
    print()

    # sin(rad) 줄 출력
    print("     rad|",end='')
    for i in range(0,361,step_deg):
        print("{:8.4f}".format(math.radians(i)),end='')
    print()

    # sin(rad) 줄 출력
    print("sin(rad)|",end='')
    for i in range(0,361,step_deg):
        print("{:8.4f}".format(math.sin(math.radians(i))),end='')
    print()

    # cos(rad) 줄 출력
    print("cos(rad)|",end='')
    for i in range(0,361,step_deg):
        print("{:8.4f}".format(math.cos(math.radians(i))),end='')
    print()
    print()
