def show(n):
    if(n==0):    #base case.
        return
    print(n)
    show(n-1)  #recusrive call
    print("end")

show(10)



#factorial
def fact(n):
    if(n==0 or n==1):
        return 1
    else:
        return n * fact(n-1)

print(fact(10))



#sum of n natural numbers.
def sum_num(s):
    if s==0:
        return 0
    else:
         return s+sum_num(s-1)
    
print(sum_num(10))



#elements in list.
def elements(l,idx):
    if idx==len(l):
        return
    print(l[idx])
    elements(l,idx+1)

l=[1,2,3,4]
elements(l,0)