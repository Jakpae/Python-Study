# 실습 5.2
# Author : LeeSeungJun
# Student ID : 22312050
# Dept : Info & Comm. Eng
# Date : March 24, 2023
# Major features :
# -

# 학생들의 튜플 리스트 생성
L_students = [
    ("Kim", "CE", 21901234, (2000, 3, 5), 4.17),
    ("Lee", "EE", 22003234, (1998, 10, 7), 3.78),
    ("Park", "ICE", 21801547, (1998, 2, 15), 4.13),
    ("Yoon", "ME", 21902571, (1999, 7, 10), 3.55),
    ("Hong", "ICE", 22003257, (2000, 3, 5), 4.45),
    ("Choi", "CHEM", 22301234, (2001, 7, 20), 3.98),
    ("Hwang", "PH", 22304321, (2001, 10, 25), 4.21),
    ("Ava", "PHY", 21907654, (2000, 8, 10), 4.15),
    ("Bella", "FART", 22007891, (2001, 2, 25), 3.57),
    ("Daniel", "LibArt", 22104321, (2002, 6, 17), 3.89)]


# 별자리를 찾기 위한 printStudent 함수 생성
def printStudent(students):
    for i in range(len(students)):
        (name, major, st_id, date_of_birth, GPA) = students[i]
        print("students[{:1}] : name({:7s}), major({:6s}), st_id({:8d}),dob({:4d}, {:2d}, {:2d}), GPA({:5.2f})".format(
            i, name, major, st_id, date_of_birth[0], date_of_birth[1], date_of_birth[2], GPA))


# 0,1,2,3,4가 입력됨에 따라 각각 이름, 학과명, 학번 ,생년월일 ,성적(역순)으로 정렬해서 출력
print("Original list of students : ")
printStudent(L_students)
while (1):
    input_key_str = input(
        "\ninput key for sorting (0: name, 1: dept name,   2: student_id, 3: date_of_birth, 4: GPA, 9: exit): ")
    if input_key_str == '0':
        sorted_students = sorted(L_students, key=lambda student: student[0])
        print("students sorted by name :")
        printStudent(sorted_students)
    elif input_key_str == '1':
        sorted_students = sorted(L_students, key=lambda student: student[1])
        print("students sorted by department :")
        printStudent(sorted_students)
    elif input_key_str == '2':
        sorted_students = sorted(L_students, key=lambda student: student[2])
        print("students sorted by student id :")
        printStudent(sorted_students)
    elif input_key_str == '3':
        sorted_students = sorted(L_students, key=lambda student: student[3])
        print("students sorted by date of birth :")
        printStudent(sorted_students)
    elif input_key_str == '4':
        sorted_students = sorted(L_students, key=lambda student: student[4],
                                 reverse=True)
        print("students sorted by GPA (decreasing order):")
        printStudent(sorted_students)
    else:
        break
