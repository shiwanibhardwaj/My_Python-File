#  *args  operator....
# we can also write anything in the place of args this:(*number).
def operator_checking(*args):
    print(type(args))
    sum = 0
    for i in args:
        sum += i
    return sum


a = operator_checking(1, 2, 3, 4, 5, 6)
print(a)


def fun(num, *args):  # we can not write like this:-> (*args,num).it will throw error.
    print(num)
    print(args)
    sum = 0
    for i in args:
        sum += i
    return sum

print(fun(2, 3, 4, 5))


#*args with list or tuple....
def list_checking(*args):
    sum=0
    for i in args:
        sum+=i
    return sum

l=[2,3,4]
print(list_checking(*l))   #we can not write like this:-> print(list_checking(l)).it will throw error.
 