# question 4).
def negetive(s):
    f = [i*2 if (i % 2 == 0) else -i for i in s]
    return f

s = list(range(1, 11))
print(negetive(s))