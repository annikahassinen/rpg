import random
from equipment import Weapon


class Hero:
    hp = 100
    defense = 0
    armor = 'none'
    weapon = Weapon(minAttack=1, maxAttack=5, name='Wooden sword')
    damage = 0

    def __init__(self, name):
        self.name = name

    def addWeapon(self, weapon):
        self.weapon = weapon
    
    def addArmor(self, armor):
        self.armor = armor
        self.defense += armor.defense

    def attack(self):
        self.damage = random.randrange(self.weapon.minAttack, self.weapon.maxAttack)
        print('Hero damage: {0}'.format(self.damage))
    
    def takeDamage(self, damage):
        self.hp -= damage