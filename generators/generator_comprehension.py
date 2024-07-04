import time
t1 = time.time()
square = (i**2 for i in range(1, 1000000))
t2 = time.time()
print(t2-t1)

# for num in square:
#     print(num)



# for num in square:
#     print(num)


t1 = time.time()
square = [i**2 for i in range(1, 1000000)]
t2 = time.time()
print(t2-t1)

# for num in square:
#     print(num)

