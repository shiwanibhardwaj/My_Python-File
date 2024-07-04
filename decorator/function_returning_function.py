# function returning function (closure)....

def outer_func():
    def inner_func():
        print("hello")
    return inner_func  # outer function returning inner function.


var = outer_func()
var()


def outer1_func(mag):
    def inner1_func():
        print(f"massage is :{mag}")
    return inner1_func


var1 = outer1_func("hii there !")
var1()


def power(x):
    def cal_power(n):
        return n**x
    return cal_power


cube = power(3)
print(f"cube of 2 is : {cube(2)}")


square = power(2)
print(f"square of 4 is: {square(4)}")


def fun(l):
    def inner():
        a = [i**2 for i in l if i % 2 == 0]
        return a
    return inner


l = [2, 3, 4, 5, 6, 7]
s = fun(l)
print(s())
 


