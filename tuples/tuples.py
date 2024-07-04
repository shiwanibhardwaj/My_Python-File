# note:-tuples are immutable (values can not be change just like strings).and tuple's performance are faster then lists.
tup = (2, 3, 4, 56) 
# tup[0]=23 (this is not allowed in tuple)
print(tup)
print(type(tup))
# tup=()  (this is a empty tuple)
# for single tuple we need to use a comma like this:-(tup=(2,) or  tup=("shivi",))

# slicing....
print(tup[1:3])
print(tup[:3])
print(tup[1:])
print(tup[-3:-1])

# tuple methods....
print(tup.index(3))  # returns index of given element
print(tup.count(2))  # counts total occurrences

#looping with tuple..
for i in tup:
    print(i)

i=0
while i<len(tup):
    print(tup[i])
    i+=1

#tuple without parenthesis...
t=1,2,3,4,5
print(type(t))

#tuple unpacking..
family=('mine','ours','others')
family1,family2,family3=(family)  #we will take same number of variable as much as elements are.otherwise it will throw error
print(family1)
print(family2)
print(family3)


#list inside tuple ...
l=[1,2,34]
td=(4,43,44,l)
print(td)
td[3].pop()  #it will remove last element  of the list.
print(td)
td[3].append('hello')  #it will add element in the end of the list.
print(td)

#some methods that can we use with tuples...
print(min(tup))
print(max(tup))
print(sum(tup))


#function returning two values(tuple)....

def fun(n1,n2):
    add=n1+n2
    multi=n1*n2
    return add,multi
print(type(fun(2,3)))

#creating tuple using range function....
a=tuple(range(1,11))
print(a,type(a))
a=list(tuple(range(1,11)))        # converting tuple into list..
print(a,type(a))
a=str(tuple(range(1,11)))        # converting tuple into str..
print(a,type(a))
