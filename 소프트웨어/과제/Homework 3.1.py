# Homewrok 3.1
# Author : LeeSeungJun
# Student ID : 22312050
# Dept : Info & Comm. Eng
# Date : March 17, 2023
# Major features :

# X,Y,Z 각각 Str(문자열)로 입력받기
x_str = input("16진수 X를 입력하세요 : ")
y_str = input("16진수 Y를 입력하세요 : ")
z_str = input("16진수 Z를 입력하세요 : ")

# X,Y,Z 문자열에서 Int(정수)형으로 변경
x = int(x_str, 16)
y = int(y_str, 16)
z = int(z_str, 16)

# X,Y,Z 10진수 16진수 2진수로 각각 출력
print("x = {0:6d} in decimal = {0:#012X} = {0:#032b}".format(x))
print("x = {0:6d} in decimal = {0:#012X} = {0:#032b}".format(y))
print("x = {0:6d} in decimal = {0:#012X} = {0:#032b}".format(z))

# XY에 대한 bit-wise and
bwa = x & y

# XY에 대한 bit-wise or
bwo = x | y

# XY에 대한 bite-wse exclusive or
bwe = x ^ y

# X에 대한 bit-wise not
bwn = ~x

# X에 대한 2-bit bit-wise shift left
bbwsl2 = x << 2

# Y에 대한 2-bit bit-wise shift right
xbbwsr2 = y >> 2

# Z에 대한 2-bit bit-wise shift right
ybbwsr2 = z >> 2

# 데이터 출력
print("x       = {0:#012X} = {0:#032b}".format(x))
print("y       = {0:#012X} = {0:#032b}".format(y))
print("x & y   = {0:#012X} = {0:#032b}".format(bwa))
print("x | y   = {0:#012X} = {0:#032b}".format(bwo))
print("x ^ y   = {0:#012X} = {0:#032b}".format(bwe))
print("~x      = {0:#012X} = {0:#032b}".format(~x))
print("x       = {0:#012X} = {0:#032b}".format(x))
print("x << 2  = {0:#012X} = {0:#032b}".format(bbwsl2))
print("y       = {0:#012X} = {0:#032b}".format(y))
print("y >> 2  = {0:#012X} = {0:#032b}".format(xbbwsr2))
print("z       = {0:#012X} = {0:#032b}".format(z))
print("z >> 2  = {0:#012X} = {0:#032b}".format(ybbwsr2))
