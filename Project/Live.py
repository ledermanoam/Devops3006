def welcome(name):
    print("Hello" + " " + name + " " + "and welcome to the world game...")


def load_game():
    print("Please choose a game to play:"
          "1. Memory Game - a sequence of numbers will appear for 1 second and you have to" + " " + " "+
          "guess it back"
          "2. Guess Game - guess a number and see if you chose like the computer"
          "3. Currency Roulette - try and guess the value of a random amount of USD in ILS")



def game_chosen(): # add int(input) to change to int

    game_name = int(input("What game you choose ?"))
    if game_name == 1:
        game_name = "Memory game"
        print("you choose to play in" + " " + game_name)
        print("Error...")
    elif game_name == 2:
        game_name = "Guess Game"
        print("you choose to play in" + " " + game_name)
    elif game_name == 3:
        game_name = "Currency Roulette"
        print("you choose to play in" + " " + game_name)



def game_difficulty():

    game_level = int(input("Please choose difficulty level between 1-5"))
    try:
     print("you choose to play im level " + " " + str(game_level))
    except Exception as e:
     print(e)






