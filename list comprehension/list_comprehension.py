# list
l = []
for i in range(1, 11):
    l.append(i**2)
print(l)


# list comprehension..
s = [i**2 for i in range(1, 11)]
print(s)



# list comprehension with if statement.......
even = [i for i in range(1, 11) if i % 2 == 0]
print(even)
odd = [i for i in range(1, 11) if i % 2 != 0]
print(odd)



# list comprehension in nested list...
nest = [[i for i in range(1, 11)] for j in range(1, 4)]
print("nested list: ", nest)
