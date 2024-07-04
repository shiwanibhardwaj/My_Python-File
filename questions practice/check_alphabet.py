# Take input from the user
char = input("Enter a character: ")

# Check if the input character is an alphabet
if (char>='a' or 'A' )and (char<='z' or 'Z'):
    print(f"{char} is an alphabet.")
else:
    print(f"{char} is not an alphabet.")



#another way to check if the character is an alphabet or not ...

char = input("Enter a character: ")

# Check if the input character is an alphabet
if char.isalpha ():
    print(f"{char} is an alphabet.")
else:
    print(f"{char} is not an alphabet.")
