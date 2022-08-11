#Second class
#A.
#1. Create two variables name X and Y.
#2. Print “BIG” if X is bigger than Y .
#3. Print “small” if X is smaller than Y.

x = 10
y = 15

if x > y:
    print("BIG")
else:
    print("small")

#B.
#1. Run a “for” loop 5 times.
#2. Print iteration number every time.


for x in range(5):
    print(x+1)


#C

season = 1
if season == 1:
    print("summer")
elif season ==2:
    print("winter")
elif season ==3:
    print("fall")
elif season == 4:
    print("spring")

#D
age = 25
letter = "g"
currency = 3.52
flew = True
apartment_number = 20

print(age)
print(letter)
print(currency)
print(flew)
print(apartment_number)
print(currency+age)

#F

phone_number = input("what is your phone number")
print("the phone number is:" + phone_number)

#G
def print_hello():
    print("hello fucker i will win!!!")

print(print_hello())

def calculate():
    print(5+3.2)

#H


def print_name(name):
    print("hello" +name)

print_name("moshe")


def divide(number):
    print(number/2)

divide(1000)

#i

def two_number(x,y):
    return x+y


print(two_number(500,600))

def add_space(word_a, word_b):
    return word_a + " " + word_b