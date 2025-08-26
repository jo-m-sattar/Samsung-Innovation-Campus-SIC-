import random

value = random.randint(1, 100)

print("Welcome to the guessing game!")

print("I have selected a number between 1 and 100, and you should choose the same number.")

guess = int(input("Enter your guess: "))
if guess == value:
    print("Congratulations! You guessed the number correctly.")
while guess != value:
    if guess < value:
        print("Higher! Try again.")
    elif guess > value:
        print("Lower! Try again.")
    guess = int(input("Enter your guess: "))
print("Congratulations! You guessed the number correctly.")