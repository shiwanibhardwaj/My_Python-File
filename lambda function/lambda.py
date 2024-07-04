#lambda expression (anonymous function)
#generally we use lambda fuction with built in functions like-> map, filter, reduce
a=lambda a,b:a+b
print(a(2,3))

b=lambda a,b:a*b
print(b(2,3))

c=lambda a:a%2==0
print(c(2))

d=lambda s:s[-1]
print(d('shivani'))

#lambda expression with if else..

f=lambda s:True if len(s) > 5 else False
print(f('shivani'))