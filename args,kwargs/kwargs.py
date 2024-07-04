#kwargs (keyword arguments)..
#**kwargs (double star operator)..

#kwargs as a parameter..

def func(**kwargs):    #we can write anything in the place of kwargs,like:->(**num).it works like dictionary.
    print(type(kwargs))
    for i,j in kwargs.items():
        print(f"{i}:{j}")

func(name='shivani',age=20)


def func1(name1,**kwargs):   
    print(type(kwargs))
    print(type(name1))
    for i,j in kwargs.items():
        print(f"{i}:{j}")

func1('shivani',name='shivani',age=20)    #we can not write like this->(name1=shivi,name='shivani',age=20) ,
                                          #it will consider in dictionary,and give type error.


#kwargs with dictionary.(dictionary unpacking)

def f(**v):
    print(v)
v={'name':'shivani','age':20}
f(**v)