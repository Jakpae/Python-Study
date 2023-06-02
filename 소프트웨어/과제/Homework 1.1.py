# Lab01.3 PythonProgram_BasicComments.py
# Author : LeeSeungJun
# Student ID : 22312050
# Dept : Info & Comm. Eng
# Date : March 3, 2023
# Major featur :
# - Integer width and length of a rectangle
# - calculate area, perimeter and diagonal
# - print results

import math

#width, height = 300, 200
width_str = input("input width of rectagle = ")
length_str = input("input length of rectangle = ")
width = int(width_str)
length = int(length_str)
area = width * length
perimeter = 2 * (width + length)
diagonal = math.sqrt(width**2 + length**2)
print("rectangle of width ({}) and length ({})".format(width, length))
print(" => area ({}), perimeter ({}), diagonal ({})".format(area, perimeter, diagonal))
