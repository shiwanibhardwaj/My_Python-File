# Enumerate function()
# we use enumerate function with for loop to track position of our item in iterable.

# without enumerate function.
f = ['shi', 'vani', 'dubey']
pos = 0
for name in f:
    print(f"{pos}----->{name}")
    pos += 1


# with enumerate function.
f = ['shi', 'vani', 'dubey']
for pos, name in enumerate(f):
    print(f"{pos}----->{name}")


# question).
def name(l, name):
    for pos, i in enumerate(l):
        if i == name:
            return pos
        else:
            return -1


l = ['shi', 'vani', 'dubey']
print(name(l, 'shiv'))
