# decorators - enhance the functionality of other functions.
# @ use for decorators.
from functools import wraps


def decorat(any_func):
    @wraps(any_func)                              #we are using this decorator for show right name and doc types of a function.
    def wrapper_func(*args, **kwargs):
        '''this is wrapper fucntion'''
        print("this is awesome function. ")
        return any_func(*args, **kwargs)
    return wrapper_func


@decorat  # shortcut
def fun1():
    '''this is 1st fucntion'''
    print("this is 1st function. ")


fun1()


@decorat
def fun2():
    print("this is 2nd function. ")


fun2()


@decorat
def add(a, b):
    return a+b


print(add(2, 3))

print(fun1.__doc__)
print(fun1.__name__)
