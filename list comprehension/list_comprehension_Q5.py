# question 5).
# without list comprehension...
combination = []
l1 = [1, 2, 3, 4, 5, 6, 7, 8]
l2 = [9, 10, 11, 12, 13, 14, 15, 16]
for i in l1:
    for j in l2:
        if (i+j) % 2 == 0:
            combination.append((i, j))
print(combination)


# without list comprehension...
l1 = [1, 2, 3, 4, 5, 6, 7, 8]
l2 = [9, 10, 11, 12, 13, 14, 15, 16]
c = [(i, j) for i in l1 for j in l2 if (i+j) % 2 == 0]
print(c)
