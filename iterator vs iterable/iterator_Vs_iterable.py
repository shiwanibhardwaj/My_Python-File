#iterator Vs iterables....
#iterables:- [list,tuple ,dict,set,range]
my_list = [1, 2, 3]
for item in my_list:  # my_list is an iterable
    print(item)

#iIterator: An object that enables traversal of an iterable's elements.
my_list = [1, 2, 3]
my_iter = iter(my_list)  # my_iter is an iterator
print(next(my_iter))  # Output: 1
print(next(my_iter))  # Output: 2
print(next(my_iter))  # Output: 3
print(next(my_iter))  # Raises StopIteration
