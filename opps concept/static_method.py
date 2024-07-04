class static:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    @staticmethod
    def add():
        a=2
        b=3
        c=a+b
        return c

print(static.add())