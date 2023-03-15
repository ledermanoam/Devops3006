#from Live import welcome, load_game, game_chosen, game_difficulty,display
import random,time

score = 0
def mem_game(game_level):
    print("you need to remember number with " +str(game_level) )
    sequence = []
    for i in range(0,game_level):
        sequence.append(random.randint(0,game_level))
    print(sequence)

    time.sleep(5)
    for i in range(0,50):
        print("")

    for i in range(0,game_level):
        print("enter number at index" + str(i))
        num = int(input())
        if num == sequence[i]:
            print("correct")
        else:
            print("wrong")
            return (0, 0)
    print(sequence)
    return (1, score)
