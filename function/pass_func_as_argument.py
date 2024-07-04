def soso(l):
    return l*5


print(soso.__name__)  # __name__ it will show the name of the function.


def power(l):
    return l**2


def lc_map(func, l):  # my map by using list comprehension..
    new = [func(i) for i in l]
    return new


# my map function by using normal function.....
def my_map(func, l):
    new_list = []
    for i in l:
        new_list.append(func(i))
    return new_list


l = list(range(1, 11))
print(my_map(lambda a: a**2, l))  # by lambda .
print(my_map(power, l))             # by function.
print(lc_map(power, l))                  # by list comprehension.
