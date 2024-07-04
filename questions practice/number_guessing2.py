import random
win = random.randint(1,100)
guess = 1
num = int(input("guess a number: "))
game_over = False
while not game_over:
    if num == win:
        print(f"you win,and you guessed this number in {guess} times")
        game_over = True
    else:
        if num < win:
            print("too low")
            guess += 1
            num = int(input("guess again :"))
        else:
            print("too high")
            guess += 1
            num = int(input("guess again :"))
