import random
from equipment import Armor, Weapon


class Hero:
    hp = 100
    defense = 0
    armor = Armor(name='Base', defense=0)
    weapon = Weapon(minAttack=1, maxAttack=5, name='Wooden sword')
    damage = 0
    inventory = []
    level = 1
    exp = 0
    maxHp = 100

    def __init__(self, name):
        self.name = name

    def addWeapon(self, weapon):
        self.weapon = weapon
    
    def addArmor(self, armor):
        self.armor = armor

    def attack(self):
        self.damage = random.randrange(self.weapon.minAttack, self.weapon.maxAttack)
        print('Hero damage: {0}'.format(self.damage))
    
    def takeDamage(self, damage):
        totalDefense = self.defense + self.armor.defense
        if totalDefense > damage:
            self.hp -= 1
        else:
            self.hp -= (damage - totalDefense)

    def addToInventory(self, item):
        self.inventory.insert(0, item)

    def addExp(self, exp):
        self.exp += exp
        if self.exp >= self.level * 10:
            self.levelUp()

    def levelUp(self):
        self.level += 1
        self.defense += 1
        self.maxHp = 100 + self.level * 10
        self.hp = self.maxHp
        self.exp = 0
        print("LEVEL UP! You are now level {0}!".format(self.level))