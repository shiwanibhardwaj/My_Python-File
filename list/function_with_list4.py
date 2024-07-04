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
c = True
while (c):
    a = int(input("enter anything: "))
    if a == 0:
        break
    n.append(a)
print(evenOdd(n))
