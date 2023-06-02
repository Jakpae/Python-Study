# Homework 4.2
# Author : LeeSeungJun
# Student ID : 22312050
# Dept : Info & Comm. Eng
# Date : March 29, 2023
# Major features :
# - Make lists
# - Translation ASCII to digits,alphabets

# 리스트 생성
L_digits = []
L_upper = []
L_lower = []

# 숫자 ,알파벳 대문자, 알파벳 소문자 추출 및 리스트에 추가
for i in range(48, 58):
    digits = chr(i)
    L_digits.append(digits)

for i in range(65, 91):
    upper = chr(i)
    L_upper.append(upper)

for i in range(97, 123):
    lower = chr(i)
    L_lower.append(lower)

# 각 리스트의 길이 산출
le_digits = len(L_digits)
le_upper = len(L_upper)
le_lower = len(L_lower)

# 리스트의 이름과 길이 그리고 결과값 출력
print("L_digits (siez : {}) : {}".format(le_digits, L_digits))
print("L_upper case alphabets (size : {}) : {}".format(le_upper, L_upper))
print("L_lower case alphabets (size : {}) : {}".format(le_lower, L_lower))
