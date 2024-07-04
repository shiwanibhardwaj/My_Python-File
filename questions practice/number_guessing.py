winnig_number = 12  
guessed_number = int(input("guess any number:"))
if guessed_number == winnig_number:
    print("congratulations ,you win")
elif guessed_number < winnig_number:
    print("too low")
elif guessed_number > winnig_number:
    print("too high")


