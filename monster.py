import random


class Monster:
    damage = 0

    def __init__(self, name, hp, minAttack, maxAttack, lootPool, exp, level):
        self.name = name
        self.hp = hp
        self.minAttack = minAttack
        self.maxAttack = maxAttack
        self.lootPool = lootPool
        self.exp = exp
        self.level = level

    def takeDamage(self, damage):
        self.hp = self.hp - damage
    
    # damage is randomized based on the min and max attack
    def attack(self):
        self.damage = random.randrange(self.minAttack, self.maxAttack)
        print('Monster damage: {0}'.format(self.damage))

    # drop random loot when dead        
    def dropLoot(self):
        item = random.choice(self.lootPool)
        self.loot = item
        print('{0} dropped {1}'.format(self.name, self.loot.name))