import random
import time

digits = input("How many digits you want to guess: ")
digits = int(digits)

#sequence = []
#for i in range(0,1):
    #sequence.append((random.randint(0,9)))
    #print(sequence)

list = []
for i in range(0,1):
 numlist = random.sample(range(0,100), digits)
 print(numlist)

time.sleep(5)
for i in range(0,50):
    print("")

for i in range(0,50):
    print('enter number at index' + str(i))
    num = int(input())
    if num == list[i]:
        print("correct")
    else:
        print("Wrong")
        break
print(list)