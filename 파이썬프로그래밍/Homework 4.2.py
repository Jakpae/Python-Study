# Homework 4.2
# Author : LeeSeungJun
# Student ID : 22312050
# Dept : Info & Comm. Eng
# Date : March 24, 2023
# Major features :
# - Make list of student-tuples
# = Sort by name print list of student-tuples
# = re-Sort by GPA print list of student-tuples

# 튜플 리스트 생성
L_students = [
    ("Kim, S.C.", 12001234, "CE", 4.10),
    ("Choi, Y.B.", 19003234, "EE", 3.78),
    ("Hong, C.H.", 21001547, "ICE", 4.13),
    ("Yoon, J.H.", 17002571, "ME", 3.55),
    ("Lee, S.H.", 20003257, "ICE", 4.45),
    ("Kim, H.Y", 19001234, "CE", 4.17),
    ("Lee, J.K", 18003234, "EE", 3.78),
    ("Park, S.Y.", 21001643, "ICE", 4.13),
    ("Jang, S.H.", 19002567, "ME", 3.35),
    ("Yeo, C.S", 20005243, "CE", 4.45)]

# 튜플 리스트를 출력하기 위한 printStudent 함수 생성


def printStudent(students):
    for i in range(len(students)):
        (name, st_id, major, GPA) = students[i]
        print("students[{:2}] : name({:10s}), st_id({:8d}), major({:3s}, GPA({:5.2f}))".format(
            i, name, st_id, major, GPA))


# 튜플 자료 출력
printStudent(L_students)

# L_student 튜플을 이름 오름차순으로 정렬해서 출력
L_students.sort(key=lambda x: x[0])
print("After sorting in increasing order")
printStudent(L_students)

# L_student 튜플을 학점을 기준으로 역순으로 정렬하여 출력
L_students.sort(key=lambda x: x[3], reverse=True)
print("After sorting according to GPA in decreasing order")
printStudent(L_students)
