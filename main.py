from hero import Hero
from monster import Monster

orc = Monster('orc', 10, 1, 2)
print(orc.damage)


print('Welcome to RPG!')
print('Your hero is eager to go to an adventure.')
heroName = input("What is the hero's name? ")
hero = Hero(heroName)
print("{0}'s stats: {1} hp, {2} def, weapon: {3}, armor: {4}".format(hero.name, hero.hp, hero.defense, hero.weapon.name, hero.armor))
movement =input('Where would you like to go? l = left, r = right, f = forward: ')

if movement == 'l':
    print('The hero turns left')
elif movement == 'r':
    print('The hero turns right')
elif movement == 'f':
    print('The hero goes forward')
else:
    print('Invalid movement')

orc = Monster('orc', 10, 1, 2)
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
elif hero.hp <= 0:
    print('You died.')