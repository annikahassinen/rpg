from hero import Hero
from logic import userChoice

# welcome the user and let them name the hero
print('Welcome to RPG!')
print('Your hero is eager to go to an adventure.')
heroName = input("What is the hero's name? ")
hero = Hero(heroName)

# start the game loop
userChoice(hero)
