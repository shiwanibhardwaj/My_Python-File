#question 1.
def square_list(n):
    num = []
    for i in n:
        num.append(i**2)
    return num

n = []
while(True):
    a = int(input("enter the number: "))
    if a==0:
        break
    n.append(a)

print(square_list(n))


#question 2.
def half_value(n):
    half=[]
    for i in n:
        half.append(i/2)
    return half

n=[]
while(True):
    a = int(input("enter the number: "))
    if a==0:
        break
    n.append(a)
print(half_value(n))

#question 3.
def reversed_list(n):
    rev=[]
    for i in range(len(n)):
        popped_value=n.pop()
        rev.append(popped_value)
    return rev

n=[]
while(True):
    a = int(input("enter the number: "))
    if a==0:
        break
    n.append(a)
print(reversed_list(n))
