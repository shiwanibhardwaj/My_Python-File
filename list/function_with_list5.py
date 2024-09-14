def commonElements(l, n):
    common = list(set(l) & set(n))
    return common


l = []
while (True):
    a = input("enter numbers for first list: ")
    if a == "0":
        break
    l.append(a)

n = []
while (True):
    a = input("enter numbers for second list: ")
    if a == "0":
        break
    n.append(a)
print(commonElements(l, n))


# another way to solve this question.....
def commonElements(l, n):
    common = []
    for i in l:
        if i in n:
            common.append(i)
    return common


l = []
while (True):
    a = input("enter numbers for first list: ")
    if a == "0":
        break
    l.append(a)

n = []
while (True):
    a = input("enter numbers for second list: ")
    if a == "0":
        break
    n.append(a)
print(commonElements(l, n))
