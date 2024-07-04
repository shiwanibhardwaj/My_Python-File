name, age = input("enter your name and age (seperated by spaces):-").split(" ")
print(name)
print(age)

# we can also write like this:-
address, pin = input("enter your address and pin (seperated by comma):-").split(",")
print(address)
print(pin)

# avarege of three numbers.....
num1, num2, num3 = input( "enter the first number and second number and third number(seperated by space):-").split(" ")
avg = (int(num1)+int(num2)+int(num3))/3
print(f"the avarege will be : {avg}")
