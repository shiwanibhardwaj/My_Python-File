a=int(input("enter: "))
for i in range(a,0,-1):
    for j in range(a-i):
        print(' ',end="")
    for k in range(2*i-1):
        print("*",end="")
    print("\n")
for i in range(1,a+1):
    for j in range(a-i):
        print(' ',end="")
    for k in range(0,2*i-1):
        print("*",end="")
    print("\n")