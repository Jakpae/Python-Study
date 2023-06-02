# 실습 2.1
# Author : LeeSeungJun
# Student ID : 22312050
# Dept : Info & Comm. Eng
# Date : March 9, 2023
# Major features :
# - Print 0 ~ 255 in Decimal, Binary, OCtal, and Hexadecimal

# = 31번 출력
print("=" * 31)

# Decimal , Binary , Octot , Hexadecimal 출력
print("{:^4s} {:^4s} {:^4s} {:^4s}".format(
    "Decimal", "Binary", "Octet", "Hexadecimal"))

"""
For 반복문 i가 반복할때마다 1만큼 커짐, i가 Range 즉 0과 256 사이일때만 반복
Print 3d (10진수 3자리까지)
Print #010b (2진수 10자리를 접두어 0b를 포함하여 출력)
Print #05o (8진수 5자리를 접두어 0o를 포함하여 출력
Print #04X (16진수 접두어 0X를 포함하여 출력 )
"""

for i in range(0, 256):
    print("{0:3d} = {0:#010b} = {0:#05o} = {0:#04X}".format(i))

# = 31번 출력
print("=" * 31)
