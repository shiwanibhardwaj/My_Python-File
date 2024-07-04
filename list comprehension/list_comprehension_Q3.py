# question 3).

def change(l):
    num = [str(i) for i in l if type(i) == int or type(i) == float]
    return num

l = ['true', 'false', [1, 2, 3], 1, 1.1, 2]
print(change(l))
