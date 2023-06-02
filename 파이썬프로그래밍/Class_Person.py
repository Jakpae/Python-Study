# Module Class_Person.py
# Major features :
# - Implement the creator (initiator) of class person, accessor (accessor) of name and age, and mutator
# - The __init__() function uses the modifier for each data member to set the initial value
# - Implemented as a __str__() function to provide a string used to output as a print() function for classPerson objects


class Person:
    
    # 초기화 메서드 __init__ 을 사용해서 어떤 클래스의 객체가 만들어질 떄 자동으로 호출되어 그 객체가 갖게될 여러가지 성질을 정해 주는 역할
    def __init__(self, name, age):
        self.setName(name) 
        self.setAge(age)
        
    # 이름과 나이를 받는 getName , getAge 메서드 정의 / 구현
    def getName(self): 
        return self.name 
    def getAge(self):
        return self.age 
    
    # setName 메서드
    def setName(self, nm):
        self.name = nm

    # 만약 나이가 0살보다 어리거나 250살보다 많으면 에러발생
    def setAge(self, ag):
        if 0 <= ag < 250: 
            self.age = ag
        else:
            print("*** Error in setting age (name:{}, age:{})".format(self.name, ag)) 
            self.age = 0 
            
    # print()함수로 출력할 때 사용되는 문자열을 제공하기 위한 __str__() 함수
    def __str__(self):
        return "Person({}, {}, {})".format(self.getName(), self.getAge())