#from Live import welcome, load_game, game_chosen, game_difficulty,display
import guess_game
from Project.Live import welcome,load_game,game_difficulty,game_chosen,guess_USD_rate
from guess_game import guess_game
from MemoryGame import  mem_game
from CurrencyRouletteGame import call_exchangerates

welcome()

load_game()

game_level = game_difficulty()
game_name = int(input("What game you choose? "))


number_of_games = 3
wins = 0

for i in range(number_of_games):
    winss = wins + game_chosen(game_level,game_name)

print("You won", winss, "games")












 #def load_game(wins=None):
  #difficulty = game_difficulty()
  #wins = wins + game_chosen(difficulty)





