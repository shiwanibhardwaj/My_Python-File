for i in range(10):
    print(f"hello world : {i}")
print("\n")
for i in range(1, 11):
    print(f"hello world : {i}")


#sum of numbers ....
num=int(input("enter the number:"))
sum=0
for i in range(num):
    sum+=i
print(f"the sum is:{sum}")


#sum of string ..
num=input("enter the number:")
sum=0
for i in range(len(num)):
   sum+=int(num[i])
print(f"the sum is:{sum}")


# count charactre...

name = input("enter your name:")
temp = ""
for i in range(len(name)):
    if name[i] not in temp:
        temp += name[i]
        print(f"{name[i]}:{name.count(name[i])}")


#step argument ....
for i in range(1,10,2): #(2 is a step argumnet)
 print(i)
print("\n")
#for reverse order ....
for i in range(10,0,-1): #(-1 is a step argumnet)
  print(i)
