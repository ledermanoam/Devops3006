from random import randint
guesses = 1
number = randint(1,10) #should to be the difficulty_number from the user

guess = int(input("Guess a number between 1 and 10"))

while guess != number:
    if guess < number:
        print("Your guess was too low")
        guess = int(input("guess again"))
        guesses = guesses + 1
    elif guess > number:
        print("Your guess was too high")
        guess = int(input("Guess again"))
        guesses = guesses + 1

print("Mazl tov, you guessed the number!")
print("you tried:", guesses)


if guesses < 3:
    print("you win this game")
else:
    print("you losser, you have been loose your game")