#set is an unordered collection of unique items.
#set help to remove duplicates of items.
#sets doesn't store tuple,list,dictionary.
p={1,2,3,4,4,4,4,5,5,6,6,7,8,8,8,8,8,8}
print(p)

#removing duplicates in list using sets.
l=[1,2,2,2,3,4,3,3,4,3,5,6,7,8,5,6,2]
print(l)
a=list(set(l))
print(a)

#set methods...
v={1,2,3}
v.add(4)
print(v)

v.remove(4) #if we try to remove item which is not inside the set the  it will give error.
print(v)

v.discard(5) #if we try to remove item which is not inside the set the  it will not give error.
print(v)

v1=v.copy()  
print(v1)

v.clear()
print(v)    

#set maths....
s1={1,1,2,3,2,3,4,5,4,6,7}
s2={2,22,4,2,3,2,1,1,1,4,3,33,55}

#union(combine all elements of given sets in one set)...
#for union we use pipe(|).
s=s1|s2
print(s)

#intersection(comman beetwen to or more sets).and we use (&) for intersection.
sh=s1&s2
print(sh)