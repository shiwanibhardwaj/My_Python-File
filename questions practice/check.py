l = []
p = []
n = []
pr =[]
e = []
o = []
count = 0
c = True
while (c):
    a = int(input("enter no.: "))
    if a == 0:
        break
    l.append(a)

for a in l:
    if a >= 0:
        p.append(a)
        count += 1
    else:
        n.append(a)
        count += 1
    if a % 2 == 0:
        e.append(a)
        count += 1
    else:
        o.append(a)
        count += 1
print(p,n, e, o)
