char = input("Enter a character: ")
# Check if the input character is uppercase or lowercase...
if char>='A' and char <='Z' :
    print(f"{char} is uppercase.")
elif char>='a' and char <='z':
    print(f"{char} is lowercase.")