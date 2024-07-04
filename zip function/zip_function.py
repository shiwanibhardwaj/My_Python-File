# zip_function....
user = [1, 2, 3]
name = ['shivani', 'ganeshu', 'saurabh']
# we can change it any sequencial data type(list,tup0le,dict).
print(dict(zip(user, name)))


user = [1, 2, 3]
name = ['shivani', 'ganeshu', 'saurabh']
age = ['age', 'age', 'age']
age_number = [20, 19, 24]
# we can't change it into dictionary , if we have multiple values.
print(list(zip(user, name, age, age_number)))


# question 1).
num = [(1, 2,), (3, 4), (5, 6), (7, 8)]
l1, l2 = zip(*num)
print(list(l1))
print(list(l2))  # output:-[1, 3, 5, 7]
#                             [2, 4, 6, 8]

# question 2).
s1 = [1, 9, 5, 7]
s2 = [2, 4, 6, 8]
new = []
for i in zip(s1, s2):
    new.append((max(i)))
print(new)


