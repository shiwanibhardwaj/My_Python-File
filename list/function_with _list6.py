# counting list inside list...

def listcount(l):
    count = 0
    for i in l:
        if type(i) == type(l):
            count += 1
    return count


number = [1, 2, 3, [1, 3, 4, 6], [9, 4, 8, 7]]
print(listcount(number))
