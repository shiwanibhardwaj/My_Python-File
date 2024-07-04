class Count_instance():
    count=0
    def __init__(self,name,age):
        Count_instance.count+=1
        self.name=name
        self.age=age

c1=Count_instance('shivani',20)
c2=Count_instance('abhishek',22)
c3=Count_instance('saurabh',25)
print(f"total instance are:- {Count_instance.count}")