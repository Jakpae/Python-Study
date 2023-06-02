# calculation of start position of star import math

import math

line_length = float(input("별의 선의 길이 ="))
cx, cy = 0, 0
sx = cx - line_length / 2
theta_rad = math.radians(360 / 5)
sy = cy + line_length / (2 * math.tan(theta_rad))
print("cx ({}), cy ({}), line_length ({}) => sx ({}), sy({})".format(
    cx, cy, line_length, sx, sy))
print("2 * math.tan(theta_rad) = {}".format(2 * math.tan(theta_rad)))
