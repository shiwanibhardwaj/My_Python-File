from functools import wraps


def int_allow(func):
    @wraps(func)

    def wrapper(*args, **kwargs):
        int_data = []
        for i in args:
            int_data.append(type(i) == int or type(i) == float)
        if all(int_data):
            return func(*args, **kwargs)
        else:
            print("invalid function")
    return wrapper


@int_allow
def sum_all(*args):
    sum = 0
    for i in args:
        sum += i
    return sum


l = [2, 3, 4]
print(sum_all(1, 2, 3, 4, 5, l))
