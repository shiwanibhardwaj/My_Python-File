# note:-lists are mutable (values can be changed)

student = ["shivani", 23, "bca"]
print(student)
student[1] = 21  # value can be change in list but not in string
print(student)
student[0:]='two'
print(student)
student[1:]=['three','four']
print(student)
# slicing in list
mark = [1, 2, 3, 4, 5]
print(mark)
print(mark[1:4])
print(mark[:4])
print(mark[1:])
print(mark[-4:-2])


# list methods....
list = [11, 22, 33,]
print(min(list))
print(max(list))
print(list)
list.append(4)  # adds one element at the end..
print(list)
list.sort()  # sorts in ascending order..
print(list)
list.sort(reverse=True)  # sort in descending order..
print(list)
list.reverse()  # reverses list  ..
print(list)
list.insert(0, 3)  # insert element at index..
print(list)
list.remove(3)
print(list)
print(list.pop(1)) #it will return popped value
print(list)             
list = ["shivani", "muskan", "priya"]
list.sort() 
print(list)
list.extend(student) #this method will concatenate two lists.
print(list)
del list[3] #del is an oprator.
print(list)
print(','.join(list)) #convert a list to string.
#   1st question:-
movie = []
movie.append(input("enter 1st movie:"))  # we can also append like this
mov2 = input("enter 2nd movie:")
mov3 = input("enter 3rd movie:")
movie.append(mov2)
movie.append(mov3)
print("my favorite movies are:")
print(movie)

# 2nd question:-
list.append(student) 
print(list)