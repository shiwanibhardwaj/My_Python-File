#filter function...
number=[1,2,3,4,5,6,7,8,9,10]
is_even=list(filter(lambda a:a%2==0,number))
print(is_even)


l=['shivani','kumari','dubey']
char=list(filter(lambda s:'a' in s,l))
print(char)


word=['shi','kumari','dubey']
length=list(filter(lambda s:len(s)>3,word))
print(length)


