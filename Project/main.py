from Live import welcome, load_game,game_chosen,game_difficulty

def welcome_to_game():
# try:
 name = input("Please insert your name: ")
 welcome(name)
 wins = 0


 load_game()
 difficulty = game_difficulty()
 wins = wins + game_chosen(difficulty)

#except:
#print("Error call functions")

 welcome_to_game()

