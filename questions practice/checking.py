# program to check if a number is positive, negative or zero.
n=int(input("enter the no:"))
if(n>0):
    print("positive")
elif(n<0):
    print("negative")
else:
    print("zero")

#checking that variable is empty or not ...
name=input("enter your name :")
if name:
    print(f"your name is {name}.")
else:
    print("you didn't type anything")