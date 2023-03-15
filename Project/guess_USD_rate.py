from CurrencyRouletteGame import call_exchangerates
#from main import game_level


def guess_dollar_rate(game_level):
    print("Welcome to Guess the Dollar Rate!")
    print("You have 3 guesses to get as close as possible to the current dollar rate.")
    print("You must to guess the dollar rate in range of " + str(game_level) + " range")

def play(game_level):
    guess_dollar_rate(game_level)
    dollars = call_exchangerates()
    score = 0
    win = False
    for i in range(game_level):
        guess = float(input("Guess #" + str(i) + ": "))
        diff = abs(guess - dollars)

        if diff == 0:
            print("Congratulations, you guessed it!")
            win = True
            break
        else:
            if diff <= 1:
                score += 10
                print("You're very close! Your score is", score)
            elif diff <= 5:
                score += 5
                print("You're close! Your score is", score)
            else:
                print("Sorry, your guess is not close enough.")
            print("You have", game_level - i - 1, "guesses left.")

    if not win:
        print("Sorry, you ran out of guesses. The actual rate was", dollars)
    print("Thanks for playing!")
    if win:
        return (1, score)
    return (0, 0)



