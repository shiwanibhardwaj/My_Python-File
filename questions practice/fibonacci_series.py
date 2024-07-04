num1 = int(input("enter the number: "))
i=0
f1=0
f2=1
while i<=num1:
   print(f1,end=" ")
   f1, f2 = f2, f1 + f2 #(f1,f2=f2 means(f1=f2=1),and f1=f1+f2)
   i+=1