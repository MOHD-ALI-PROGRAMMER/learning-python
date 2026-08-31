secret_guess = 37
attempts = 0
playing = True

while playing:
    guess = int(input("Guess the number: "))
    attempts = attempts + 1

    if guess < secret_guess:
        print("too low, try again")

    elif guess > secret_guess:
        print("too high, try again")

    else:
        print("congratulation, you guess the number")
        playing = False

print("You won in",attempts,"tries")

print("Game over._.")