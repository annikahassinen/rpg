from equipment import Armor, Weapon
from hero import Hero
from item import HealingPotion
from monster import Monster
from lists import potions, armors, weapons
from logic import userChoice, encounter, useLoot

""" orc = Monster('orc', 10, 1, 2)
print(orc.damage) """


print('Welcome to RPG!')
print('Your hero is eager to go to an adventure.')
heroName = input("What is the hero's name? ")
hero = Hero(heroName)

while hero.hp > 0:
    userChoice(hero)

""" print("{0}'s stats: {1} hp, {2} def, weapon: {3}, armor: {4}".format(hero.name, hero.hp, hero.defense, hero.weapon.name, hero.armor))
movement =input('Where would you like to go? l = left, r = right, f = forward: ')

if movement == 'l':
    print('The hero turns left')
elif movement == 'r':
    print('The hero turns right')
elif movement == 'f':
    print('The hero goes forward')
else:
    print('Invalid movement')

orc = Monster('orc', 10, 1, 2, potions + armors + weapons)
print('{0} meets an angry {1} that is about to attack.'.format(hero.name, orc.name))
while hero.hp > 0 | orc.hp > 0:
    hero.attack()
    orc.takeDamage(hero.damage)
    print('You attack with {0} damage. {1} has {2} hp.'.format(hero.damage, orc.name, orc.hp))

    orc.attack()
    hero.takeDamage(orc.damage)
    print('{0} attacks back with {1} damage. Your hp is {2}'.format(orc.name, orc.damage, hero.hp))

if orc.hp <= 0:
    print('{0} has died.'.format(orc.name))
    orc.dropLoot()
    hero.addToInventory(orc.loot)
elif hero.hp <= 0:
    print('You died.')

if isinstance(hero.inventory[0], HealingPotion):
    useItem = input('Would you like to use a potion? y/n: ')
    if useItem == 'y':
        print('Hero hp: {0}'.format(hero.hp))
        hero.inventory[0].use(hero)
        print('Hero hp: {0}'.format(hero.hp))
elif isinstance(hero.inventory[0], Armor):
    equipItem = input('Would you like to equip this armor? Your current armor def: {0}, new armor def: {1}. y/n: '.format(hero.armor.defense, hero.inventory[0].defense))
    if equipItem == 'y':
        hero.addArmor(hero.inventory[0])
        print('Hero defense: {0}, armor: {1}'.format(hero.defense, hero.armor.name))
elif isinstance(hero.inventory[0], Weapon):
    equipItem = input('Would you like to equip this weapon? Your current weapon minAttack/maxAttack: {0}/{1}, new weapon min/max: {2}/{3}. y/n: '.format(hero.weapon.minAttack, hero.weapon.maxAttack, hero.inventory[0].minAttack, hero.inventory[0].maxAttack))
    if equipItem == 'y':
        hero.addWeapon(hero.inventory[0])
        print('Hero weapon: {0}'.format(hero.weapon.name)) """
