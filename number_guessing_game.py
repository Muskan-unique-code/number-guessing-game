import random

number = random.randint(1, 10)

guess = int(input("Guess a number from 1 to 10: "))

if guess == number:
    print("Correct! You won!")
else:
    print("Wrong! The number was:", number)