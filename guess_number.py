secret_guess = 79
guess = 0
playing = True

while playing:
    guess = int(input("Guess the number: "))

    if guess < secret_guess:
        print("too low, try again")

    elif guess > secret_guess:
        print("too high, try again")

    else:
        print("congratulation, you guess the number")
        playing = False

print("Game over._.")