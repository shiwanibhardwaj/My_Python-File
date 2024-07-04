ch = True
while (ch):
    print("patterns:")
    c = int(input("enter cordinate number: "))
    if (c == 1):
        n = int(input("enter no.: "))
        for i in range(1, n+1):
            print("*"*i)
    elif (c == 2):
        n = int(input("enter no.: "))
        for i in range(1, n+1):
            print(" "*(n-i)+"*"*i)
    elif (c == 3):
        n = int(input("enter no.: "))
        for i in range(n, 0, -1):
            print("*"*i)
    elif (c == 4):
        n = int(input("enter no.: "))
        for i in range(n, 0, -1):
            print(" "*(n-i)+"*"*i)
    elif (c == 5):
        n = int(input("enter no.: "))
        for i in range(1, n+1):
            print(" "*(n-i)+"*"*(2*i))
        for i in range(n, 0, -1):
            print(" "*(n-i)+"*"*(2*i))
    elif (c == 0):
        exit()
    else:
        c = input("invalid input ...press enter to exit")
        exit()

    ch = input("do you want to print any other pattern?(y/n)")
    if (ch == 'Y' or ch == 'y'):
        ch = True
    else:
        ch = False
