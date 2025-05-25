import random


class Monster:
    damage = 0

    def __init__(self, name, hp, minAttack, maxAttack):
        self.name = name
        self.hp = hp
        self.minAttack = minAttack
        self.maxAttack = maxAttack

    def takeDamage(self, damage):
        self.hp = self.hp - damage
    
    def attack(self):
        self.damage = random.randrange(self.minAttack, self.maxAttack)
        print('Monster damage: {0}'.format(self.damage))
            


