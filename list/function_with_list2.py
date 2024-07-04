def reverse(l):
    reverselist=[]
    for i in range(1,len(l)+1):
      a=l.pop()
      reverselist.append(a) 
    return reverselist 
l=list(range(1,11))
print(reverse(l))