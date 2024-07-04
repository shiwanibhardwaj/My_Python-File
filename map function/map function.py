# map function.
num = [1, 2, 3, 4, 5]


def square(a):
    return a**2


a = list(map(square, num))
print(a)

# by using lambda function..
s = list(map(lambda a: a**2, num))
print(s)

# by using list comprehension..
c = [i**2 for i in num]
print(c)


def sq(num):
    li = []
    for i in num:
        li.append(i**2)
    return li


print(sq(num))


# finding length of string.
s = ['hello', 'shivani', 'dubey']
length = list(map(len, s))
print(length)

# second way..
s = ['hello', 'shivani', 'dubey']
length = map(len, s)
for i in length:
    print(i)
