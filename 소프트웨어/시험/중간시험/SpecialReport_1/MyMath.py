# MyMath.py

import math

def printTrigonometricTable(step_deg):
    print(">>> Trigonmetric Table (step_deg = {}) <<<".format(step_deg))
    print("     deg|",end='')
    for i in range(0,360+1,step_deg):
        print("{:8d}".format(i),end='')
    print()
    print("-" * 8)
    print("+")
    for i in range(360 / step_deg + 1):
        print("-" * 8,end='')
    print()
    print("     rad|",end='')
    for i in range(0,360+1,step_deg):
        print("{:8.4f}".format(math.radians(i)),end='')
    print()
    print("sin(rad)|",end='')
    for i in range(0,360+1,step_deg):
        print("{:8.4f}".format(math.sin(math.radians(i))),end='')
    print()
    print("cos(rad)|",end='')
    for i in range(0,360+1,step_deg):
        print("{:8.4f}".format(math.cos(math.radians(i))),end='')
    print()
    print()
    