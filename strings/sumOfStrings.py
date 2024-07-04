number=input("enter number:")
sum=0
i=0
while i<len(number):
    sum+=int(number[i])
    i+=1
print(f"the sum of given number(string) is: {sum}")