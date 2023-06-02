# Homework 3.1
# Author : LeeSeungJun
# Student ID : 22312050
# Dept : Info & Comm. Eng
# Date : March 15, 2023
# Major features :
# - Input 2 Hexadecimal numbers
# - Print A,B to Decimal, Binary, Hexadecimal
# - Calculate A,B for bit-wise AND, bit-wise OR, bit-wise XOR

# Input 2 Hexadeciaml Numbers and save them as A and B using split
a, b = (input("2개의 16진수를 입력하세요 : ").split())

# Convert Hexadeciaml String A,B to number using Int
a = int(a, 16)
b = int(b, 16)

# Calculate A,B for Bit-wise And, Bit-wise OR, Bit-wise XOR
bwa = a & b
bwo = a | b
bwxo = a ^ b

# Print A,B and Calculated Data
print("a = {0:#04X} = {0:4d} = {0:#010b}".format(a))
print("b = {0:#04X} = {0:4d} = {0:#010b}".format(b))
print("a & b = {0:#04X} = {0:4d} = {0:#010b}".format(bwa))
print("a | b = {0:#04X} = {0:4d} = {0:#010b}".format(bwo))
print("a ^ b = {0:#04X} = {0:4d} = {0:#010b}".format(bwxo))
