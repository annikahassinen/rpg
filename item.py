# in case other kinds of items are added later, for now only healing potions
class Item:

    def __init__(self, name, increase):
        self.name = name
        self.increase = increase

    def use(self):
        print('Used item')


class HealingPotion(Item):
    name = "Healing potion"
    def __init__(self, increase):
        self.increase = increase

    def use(self, hero):
        hero.hp += self.increase
    