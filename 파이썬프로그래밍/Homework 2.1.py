# Homework 2.1
# Author : LeeSeungJun
# Student ID : 22312050
# Dept : Info & Comm. Eng
# Date : March 9, 2023
# Major features :
# - Print 0 ~ 255 for Decimal , Binary , Octet , Hexadcima

import math

print("=" * 28)
print("{:^4s} {:^4s} {:^4s} {:^4s}".format(
    "Decimal", "Binary", "Octet", "Hexadecimal"))

for i in range(0, 256):
    print("{0:4d} {0:08b} {0:#05o} {0:#04X}".format(i))
print("=" * 28)
