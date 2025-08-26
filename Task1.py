# this is a simple game that asks the user for their name, favorite color, favorite food, and current city
import time
#Used for adding delays beween print statements
print("Welcome to the game!")
time.sleep(1)
Username = input("Hi, what is your name?  ")
time.sleep(1)
print("Hello " + Username + ", let's ask you some questions")
time.sleep(1)
fav_color = input("What is your favorite color? ")
time.sleep(1)
fav_food = input("What is your favorite food? ")
time.sleep(1)
current_city = input("What is your current city? ")
time.sleep(1)
print("Ok " + Username + ", " + "your favourite color is " + fav_color + ", your favourite food is " + fav_food + ", and you are currently in " + current_city + ".")