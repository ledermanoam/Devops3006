import random
#from Live import game_difficulty

######## This is master , don't change !!!!!!!!

def generate_number(x):
 print("Welcome to the guess game !")
 random_number = random.randint(1,x)
 guess = 0
 while guess !=  random_number:
    guess = int(input(f'Guess a number between 1 and {x}: '))
    if guess < random_number:
        print("Too Low")
    elif guess > random_number:
        print("Too high")
    elif guess == random_number:
        print("your guess is correct" + " " + str(guess))


generate_number(5)




