class Person:
    def __init__(self,name='kate',age=13):
        print(self,'is generated')
        self.name = name
        self.age = age

bob = Person()
print(bob.name)
print(bob.age)

kim = Person('kim',20)
print(kim.name)
print(kim.age)

kim1 = Person(age=20)
print(kim1.name)
print(kim1.age)