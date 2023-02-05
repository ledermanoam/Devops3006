from Live import welcome, load_game, game_chosen, game_difficulty,display
from random import randint
from Live import display

#difficulty !!!!!!!!

def guess_game(game_level):
    generated_number = randint(1,game_level)
    guess = 0
    guesses = 0

    while(guess != generated_number):


        guess = int(input("Guess a number between 1 and " + str(game_level) + ": "))

        if(guess > generated_number):
            print("too high")
        elif(guess < generated_number):
            print("too low")
        else:
            print("correct, you won by " + str(guesses + 1) + " tries")
            return 1

        guesses = guesses + 1

        if(guesses >= 3):
            print("you lost, more than 3 tries")
            return 0
