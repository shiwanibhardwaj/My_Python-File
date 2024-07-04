class Student:
    pass


c1 = Student()
c2 = Student()
print(type(c1))



class Employee:
    def __init__(self,name,age):  
        print("first init method get called.")   #init method is a constructor,and self works like an object.                                                  
        self.name=name
        #e1.name=name
        self.age=age


e1 = Employee('shivani', 20)
print(e1.__dict__)
e2 = Employee('shiva', 24)
print(e2.__dict__)

