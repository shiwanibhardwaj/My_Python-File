def reverseString(l):
    reverse1 = []
    for i in l:
        reverse1.append(i[::-1])
    return reverse1


n = []
c = True
while (c):
    a = input("enter anything: ")
    if a == "0":
        break
    n.append(a)
print(reverseString(n))
