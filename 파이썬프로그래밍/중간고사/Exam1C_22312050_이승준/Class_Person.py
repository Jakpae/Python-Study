# Class_Person
# Author : LeeSeungJun
# Student ID : 22312050
# Dept : Info & Comm. Eng
# Date : April 23, 2023

class Person:
    
    # 초기화 메서드 __init__ 을 사용해서 어떤 클래스의 객체가 만들어질 떄 자동으로 호출되어 그 객체가 갖게될 여러가지 성질을 정해 주는 역할
    def __init__(self, name):
        self.setName(name) 
        
    # 이름과 나이를 받는 getName , getAge 메서드 정의 / 구현
    def getName(self): 
        return self.name 
    
    # setName 메서드
    def setName(self, nm):
        self.name = nm

       
    # print()함수로 출력할 때 사용되는 문자열을 제공하기 위한 __str__() 함수
    def __str__(self):
        return "Person({}, {}, )".format(self.getName())