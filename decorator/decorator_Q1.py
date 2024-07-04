from functools import wraps

def print_data(func):
    wraps(func)

    def show(*args, **kwargs):
        print(f"you are calling {func.__name__} function")
        print(func.__doc__)
        return func(*args, **kwargs)
    return show


@print_data
def add(a, b):
    '''this function takes two numbers as arguments and return their sum'''
    return a+b


print(add(5, 5))
    