# for calculate run timing
from functools import wraps
import time


def print_data(func):
    wraps(func)
    t1 = time.time()

    def show(*args, **kwargs):
        print(f"you are calling {func.__name__} function")
        print(func.__doc__)
        a = func(*args, **kwargs)
        t2 = time.time()
        total = t2-t1
        print(f"this function took {total} second")
        return a
    return show


@print_data
def add(a, b):
    '''this function takes two numbers as arguments and return their sum'''
    return a+b


print(add(5398493, 50000))

# t2=time.time()
# print(t2-t1)     #calculat the rum timing
