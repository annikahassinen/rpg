import random
from equipment import Armor, Weapon


class Hero:
    hp = 100
    defense = 0
    armor = Armor(name='Base', defense=0)
    weapon = Weapon(minAttack=1, maxAttack=5, name='Wooden sword')
    damage = 0
    inventory = []

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

    def addToInventory(self, item):
        self.inventory.append(item)
        print('Inventory: {0}'.format(self.inventory))