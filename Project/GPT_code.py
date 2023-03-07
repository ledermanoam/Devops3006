import random
import datetime

dollars = random.randint(70, 100)

print("Welcome to Guess the Dollar Rate!")
print("You have 5 guesses to get as close as possible to the current dollar rate.")

for i in range(1, 6):
    guess = float(input("Guess #" + str(i) + ": "))
    diff = abs(guess - dollars)

    if guess == dollars:
        print("Congratulations, you guessed it!")
        break
    elif i == 5:
        print("Sorry, you ran out of guesses. The actual rate was", dollars)
    else:
        if diff <= 1:
            score = 10
            print("You're very close! Your score is", score)
        elif diff <= 5:
            score = 5
            print("You're close! Your score is", score)
        else:
            score = 0
            print("Sorry, your guess is not close enough.")

        if i < 5:
            print("You have", 5 - i, "guesses left.")
            print("")

print("Thanks for playing!")

#############

guess = float(input("Guess the dollar rate today: "))


###########################



if guess == dollars:
    print("Congratulations, you guessed it!")
elif guess > dollars:
    print("Sorry, your guess is too high.")
else:
    print("Sorry, your guess is too low.")
