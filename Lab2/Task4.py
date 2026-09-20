# Python Classes/Objects
# Creating a class

class MyClass: 
    x=5
p1 = MyClass()
print(p1.x)

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age  = age

p1 = Person("John",36)        
print(p1.name)
print(p1.age)

# Object Methods
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age  = age

    def myfunc(self):
        print("Hello my name is "+ self.name)
        print("My age is ",self.age)

p1 = Person("john",36)
p1.myfunc()







