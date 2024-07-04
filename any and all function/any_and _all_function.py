# all and any function
l1 = [9, 2, 3, 4, 5, 6, 7]
l2 = [2, 4, 6, 8, 10, 12]
print(all([num % 2 == 0 for num in l1]))
print(all([num % 2 == 0 for num in l2]))
print(any([num % 2 == 0 for num in l2]))


def sum(*args):
    if all([(type(arg) == int or type(arg) == float) for arg in args]):
        total = 0
        for num in args:
            total += num
        return total
    else:
        return "wrong input"


num = [2, 3, 4, 5, 'shivani', 'dubey', 4, 5, 6]
print(sum(num))
