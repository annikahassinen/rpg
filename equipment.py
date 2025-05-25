class Equipment:
    def __init__(self, defense, name):
        self.defense = defense
        self.name = name

class Weapon:
    def __init__(self, minAttack, maxAttack, name):
        self.minAttack = minAttack
        self.maxAttack = maxAttack
        self.name = name