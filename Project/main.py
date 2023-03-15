#from Live import welcome, load_game, game_chosen, game_difficulty,display
#import guess_game
from Live import welcome,load_game,game_difficulty,game_chosen
#from guess_game import guess_game
#from MemoryGame import  mem_game
#from CurrencyRouletteGame import call_exchangerates

welcome()

load_game()

game_level = game_difficulty()
game_name = int(input("What game you choose? "))


number_of_games = 3
wins = 0
score = 0

for i in range(number_of_games):
    win = game_chosen(game_level,game_name)
    wins = wins + win[0]
    score = score + win[1]
    wins = wins + game_chosen(game_level,game_name)

print("You won", wins, "games")












 #def load_game(wins=None):
  #difficulty = game_difficulty()
  #wins = wins + game_chosen(difficulty)





