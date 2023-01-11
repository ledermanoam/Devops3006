import random,time
def mem_game(difficulty):
    digits = int(input('How many digit do you want to guess ?'))

    sequence = []
    for i in range(0,digits):
        sequence.append(random.randint(0,difficulty))
    print(sequence)

    time.sleep(5)
    for i in range(0,50):
        print("")

    for i in range(0,digits):
        print("enter number at index" + str(i))
        num = int(input())
        if num == sequence[i]:
            print("correct")
        else:
            print("wrong")
            return 0
    print(sequence)
    return 1
