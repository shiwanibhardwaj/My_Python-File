# question 2).

def reverse(l):
    rev = [i[::-1] for i in l]
    return rev

l = ['hello', 'shivi']
print(reverse(l))