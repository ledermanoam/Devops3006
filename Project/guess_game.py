from random import randint

def guess_game(difficulty):
    generated_number = randint(1,difficulty)
    guess = 0
    guesses = 0

    while(guess != generated_number):

        guesses = guesses + 1

        if(guesses >= 3):
            print("you lost, more than 3 tries")
            return 0

        guess = int(input("Guess a number between 1 and " + str(difficulty)))

        if(guess > generated_number):
            print("too high")
        elif(guess < generated_number):
            print("too low")
        else:
            print("correct, you won by " + str(guesses) + " tries")
            return 1
