def evenOdd(l):
    even = []
    odd  = []
    both = []
    for i in l:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
    both.append(even)
    both.append(odd)
    return both


n = []
while (True):
    a = int(input("enter numbers: "))
    if a == 0:
        break
    n.append(a)
print(evenOdd(n))
