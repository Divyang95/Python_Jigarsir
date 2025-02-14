import random

num = random.randint(1,20)

while True:
    guess = int(input("Guess Number between 1 to 20 : "))

    if(num == guess):
        print("Guessed Number is same Number")

    elif(num>guess):
        print("guessed number is samller please guess bigger number")

    elif(num<guess):
        print("Guessed number is bigger please guess smaller number")
        
