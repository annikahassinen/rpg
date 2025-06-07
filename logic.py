import copy
import random
import sys
from equipment import Armor, Weapon
from item import HealingPotion
from lists import potions, armors, weapons, monsters

def userChoice(hero):
    print("{0}'s stats: {1} hp, {2} def, weapon: {3}, armor: {4}".format(hero.name, hero.hp, hero.defense, hero.weapon.name, hero.armor.name))
    userInput =input('Where would you like to go? l = left, r = right, f = forward: '
    'Or would you like to use a potion? u : ')

    if userInput == 'l':
        print('The hero turns left')
        encounter(hero)
    elif userInput == 'r':
        print('The hero turns right')
        encounter(hero)
    elif userInput == 'f':
        print('The hero goes forward')
        encounter(hero)
    elif userInput == 'u':
        for val in hero.inventory:
            if isinstance(val, HealingPotion):
                val.use(hero)
                print('used potion')
                break
    elif userInput == 'q':
        sys.exit()
    else:
        print('Invalid movement')

def encounter(hero):
    available_monsters = []
    allMonsters = copy.deepcopy(monsters)
    for i in allMonsters:
        if i.level <= hero.level:
            available_monsters.append(i)
            print('Added {0}'.format(i.name))
    monster = random.choice(available_monsters)
    print('{0} meets an angry {1} that is about to attack. Monster hp: {2}'.format(hero.name, monster.name, monster.hp))
    while hero.hp > 0 and monster.hp > 0:
        hero.attack()
        monster.takeDamage(hero.damage)
        print('You attack with {0} damage. {1} has {2} hp.'.format(hero.damage, monster.name, monster.hp))

        monster.attack()
        hero.takeDamage(monster.damage)
        print('{0} attacks back with {1} damage. Your hp is {2}'.format(monster.name, monster.damage, hero.hp))

    if monster.hp <= 0:
        print('{0} has died.'.format(monster.name))
        monster.dropLoot()
        hero.addToInventory(monster.loot)
        hero.addExp(monster.exp)
        useLoot(hero)
    elif hero.hp <= 0:
        print('You died.')

def useLoot(hero):
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
            print('Hero weapon: {0}'.format(hero.weapon.name))
    
    userChoice(hero)