#cubi_finder......

def cube(d):
    dict1={}
    for i in range(1,d+1):
       dict1[i]=i**3
    return dict1
d=int(input("enter the number:"))
print(cube(d))