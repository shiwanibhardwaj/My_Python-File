print("hello world \nhello \nhyy ")     #for next line
print('hello'+'world')                  #concatenation of two or more strings.
print('hello'+" "+'world')              #concatenation with space.
print(5*("hello\"world\""))

name = input("what is your name?")
print('hello'+" " + name + " ," + "how are you?")
length = len(name)
print(length)

name, age = "shivani", 24
length = len(name)
print(name)
print("length of the name is:")
print(length)


var = True
print(type(var))
a = 2
b = 17
c = "shi"
d = 2.5
e = a < d


print(type(e))
print(type(a))
print(a)
print(b)
print(c)
print(d)
print(a+d)
# we use ** operator for a raised to the power b
f = a**b
print(f)
print(a/b)  # floating point devision.
print(a//b)  # integer devision.
print(round(a/b, 4))  # we can reduce floating nubmers by using round function.

print(0o12)     #Octal Literal (base 8) 
print(0b10)     #Binary Literal (base 2)  
print(0x123)    #Hexadecimal Literal (base 16) 
# we can use capital latters too in the place of (o,b,x)..

# type-conversion
age = int(input("age:"))
price = float(input("price"))
print(age)
print(price)

# operators in python

# 1. arithmetic(+,-,*,/,//,%,**)

# 2. relational/comparison(==, !=,>,<,>=,<=)

# 3. assignment(=,-=,*=,/=,%=,//=,**=)

# 4. logical(not,and,or)

# 5. membership(in,not in)

# 6. identity(is, is not)

# 7. bitwise(&,|,^)


#id (built-in function.)
person="hyyy"
print(id(person))
var=23
print(id(var))