class Person:
    def __init__(self,name='kate',age=13):
        print(self,'is generated')
        self.name = name
        self.age = age


bob=Person() #아무것도 안넣을 경우 def 의 값을 그대로 넣어준다.

print(bob.name)#str = java 에서 toString
print(bob.age)

kim =  Person('jang',30)
print(kim.name)
print(kim.age)

qwe = Person(age=45)
print(qwe.name)
print(qwe.age)