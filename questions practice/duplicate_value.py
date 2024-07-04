n = [1, 2, 1, 2, 3, 4, 5, 6, 4, 7, 8, 9, 10]
# Count occurrences of each element
d=[]
count={}
for i in n: 
    if i in count:
        count[i]+=1
    else:
        count[i]=1

# Identify duplicates
for i,j in count.items():
    if j>1:
        d.append(i)
print(d)