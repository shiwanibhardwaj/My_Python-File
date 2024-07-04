l=['shivani','ganeshu','saurabh']
for i in l:
    print(i)

i=0
while i<len(l):
    print(l[i])
    i+=1

matrix=[[1,2,3],[4,5,6],[7,8,9]]
for i in matrix:
    for j in i:
        print(j)


print(matrix[0][0])
print(matrix[0][1])
print(matrix[0][2])
print(matrix[1][0])
print(matrix[1][1])
print(matrix[1][2]) 
print(matrix[2][0])
print(matrix[2][1])
print(matrix[2][2])
print(type(matrix))

# generating list with range function...
num=list(range(1,21))
print(num)