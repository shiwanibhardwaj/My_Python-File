# question 6).
def power(num, *args):
    if not args:
        print("hey,u did not pass any args")
    else:
        return [i**num for i in args]

l = [2, 3, 4, 5]
print(power(3, *l))
    