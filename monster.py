import random


class Monster:
    damage = 0

    def __init__(self, name, hp, minAttack, maxAttack, lootPool):
        self.name = name
        self.hp = hp
        self.minAttack = minAttack
        self.maxAttack = maxAttack
        self.lootPool = lootPool

    def takeDamage(self, damage):
        self.hp = self.hp - damage
    
    def attack(self):
        self.damage = random.randrange(self.minAttack, self.maxAttack)
        print('Monster damage: {0}'.format(self.damage))
            
    def dropLoot(self):
        item = random.choice(self.lootPool)
        self.loot = item
        print('{0} dropped {1}'.format(self.name, self.loot.name))

