# Lab07.1 using myturtledrawing.py module
# Author : Cho H-W
# Student ID : 22312081
# Dept: Info&Comm.Eng
# Date: April 13, 2023
# Major feature :
#   -

from MyPyPackage.myModules import MyTurtleDrawings
import sys
import turtle

MyPyPackage_dir = "C:"
sys.path.append(MyPyPackage_dir)


def main():
    turtle.setup(600, 400)
    turtle.title("Drawing polygons with use-defined module")
    t = turtle.Turtle()
    t.shape("classic")
    shapes = [("polygon", 3, -200, 100, 100, "red"), ("polygon", 4, 0, 100, 100, "green"),
              ("circle", 200, 100, 50, "blue"), ("star", -200, -100, 100, "yellow")]
    for i in range(len(shapes)):
        shape_type = shapes[i][0]
        if shape_type == "polygon":
            st, num_vertices, center_x, center_y, line_length, color = shapes[i]
            MyTurtleDrawings.drawPolygon_Turtle(
                t, num_vertices, center_x, center_y, line_length, color)
        elif shape_type == "circle":
            st, center_x, center_y, radius, color = shapes[i]
            MyTurtleDrawings.drawCircle_Turtle(
                t, center_x, center_y, radius, color)
        elif shape_type == "star":
            st, center_x, center_y, length, color = shapes[i]
            MyTurtleDrawings.drawStar_Turtle(
                t, center_x, center_y, length, color)
        else:
            print("Error-the shape({})is not supported yet!".format(shape_type))
    t.up()
    t.home()
    t.down()


if __name__ == "__main__":
    main()
