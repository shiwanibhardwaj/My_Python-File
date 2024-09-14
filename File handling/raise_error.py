def add(a, b):
    if (type(a) is int or type(a) is float) and (type(b) is int or type(b) is float):
        return a+b
    raise TypeError("opps you passed wrong data type")


print(add(3.5,5))


def value(a):
    if type(a) is int:
        print(a)
    raise ValueError("opps you passed wrong value!")

value("str")






