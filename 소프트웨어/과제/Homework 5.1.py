# Homework 5.1
# Author : LeeSeungJun
# Student ID : 22312050
# Dept : Info & Comm. Eng
# Date : March 31, 2023
# Major features :
# - Organize and output an alphabetical list of uppercase, lowercase, and numeric characters in the ASCII character table

# upper,lower,digits 리스트 구성
upper = []
lower = []
digits = []

# Upper list, 즉 영문 대문자 리스트를 아스키코드 변환을 통해 구성
for i in range(65, 91):
    upper.append(chr(i))

# Lower list, 즉 영문 소문자 리스트를 아스키코드 변환을 통해 구성
for i in range(97, 123):
    lower.append(chr(i))

# Digits list, 즉 숫자 리스트를 아스키코드 변환을 통해 구성
for i in range(48, 58):
    digits.append(chr(i))

# 구성한 리스트들을 출력
print("Upper case alphabets")
print(upper)
print()
print("Lower case alphabets")
print(lower)
print()
print("Digits")
print(digits)
