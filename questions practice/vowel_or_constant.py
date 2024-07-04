# Input alphabet from the user
alphabet = input("Enter an alphabet: ")

# Check if the input is a single alphabet
if len(alphabet) == 1 and alphabet.isalpha():
    # Convert the alphabet to lowercase for easier comparison
    alphabet_lower = alphabet.lower()
    
    # Check if the alphabet is a vowel
    if alphabet_lower in 'aeiou':
        print(f"{alphabet} is a vowel.")
    else:
        print(f"{alphabet} is a consonant.")
else:
    print("Please enter a single alphabet.")
