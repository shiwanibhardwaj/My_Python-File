num = int(input("enter the number: "))
for i in range(2, num):
    if num % i == 0:
        print(num, "num is not prime number.")
        break
    else:
        print(num, "num is prime number.")
        break
