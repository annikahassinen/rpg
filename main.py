from hero import Hero
from logic import userChoice


print('Welcome to RPG!')
print('Your hero is eager to go to an adventure.')
heroName = input("What is the hero's name? ")
hero = Hero(heroName)

userChoice(hero)
