from functools import wraps

def decorate(any_func):
    wraps(any_func)

    def work(*args, **kwargs):
        print(f"this is {any_func.__name__} function: ")
        return any_func(*args, **kwargs)
    return work


@decorate
def power(x):
    def num(n):
        return n**x
    return num

print(power(2)(4))


@decorate
def check(n):
    def even():
        if n % 2 == 0:
            return n
    return even


print(check(6)())


