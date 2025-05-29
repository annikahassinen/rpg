class Armor:
    def __init__(self, defense, name):
        self.name = name
        self.defense = defense       

class Weapon:
    def __init__(self, minAttack, maxAttack, name):
        self.name = name
        self.minAttack = minAttack
        self.maxAttack = maxAttack