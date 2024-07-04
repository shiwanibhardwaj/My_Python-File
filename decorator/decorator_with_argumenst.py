from functools import wraps


def data_type(s):
    def decorate(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if all([type(agr) == s for agr in args]):
                return func(*args, **kwargs)
            print("invalid arguments")
        return wrapper
    return decorate


@data_type(str)
def string(*args):
    s = ""
    for i in args:
        s += i
    return s


print(string('shivani', 'dubey'))


def data_type(s):
    def decorate(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if all([type(agr) == s for agr in args]):
                return func(*args, **kwargs)
            print("invalid arguments")
        return wrapper
    return decorate


@data_type(str)
def string(*args):
    s = ""
    for i in args:
        s += i
    return s


print(string('shivani', 'dubey', 'a'))
