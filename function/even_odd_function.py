def even_odd(num):
    if num%2==0:
        return "even"
    else:
        return "odd"
num=int(input("enter a number: "))
print(even_odd(num))

#another way...
def is_even(num):
    return  num%2==0 
n=int(input("enter a number: "))
print(is_even(n))


