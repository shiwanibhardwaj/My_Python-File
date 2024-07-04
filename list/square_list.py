def square_list(n):
    num = []
    for i in n:
        num.append(i**2)
    return num

n = []
a = int(input("enter the number: "))
for i in range(a):
    n.append(i)

print(square_list(n))


def half_value(n):
    half=[]
    for i in n:
        half.append(i//2)
    return half

n=[]
a=int(input("enter the number: "))
for i in range(a):
    n.append(i)
print(half_value(n))