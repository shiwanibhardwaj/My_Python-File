def average(l1, l2):
    a = []
    for pair in zip(l1, l2):
        a.append(sum(pair)/len(pair))
    return a


l1 = [1, 2, 3, 4]
l2 = [5, 6, 7, 8]
print(average(l1, l2))
