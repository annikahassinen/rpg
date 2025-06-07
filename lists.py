from equipment import Armor, Weapon
from item import HealingPotion
from monster import Monster


potions = [HealingPotion(10), HealingPotion(15), HealingPotion(5)]
armors = [Armor(name='Wooden armor', defense=1),
         Armor(name='Silver armor', defense=2),
         Armor(name='Iron armor', defense=3),
         Armor(name='Steel armor', defense=4),
         Armor(name='Molten armor', defense=5),
         Armor(name='Fire armor', defense=6),
         Armor(name='Water armor', defense=7),
         Armor(name='Viking armor', defense=8),
         Armor(name='Mithril armor', defense=10),
         ]
weapons = [Weapon(minAttack=1, maxAttack=3, name='Wooden sword'), 
           Weapon(minAttack=3, maxAttack=5, name='Silver sword'),
           Weapon(minAttack=3, maxAttack=7, name='Iron sword'),
           Weapon(minAttack=5, maxAttack=7, name='Steel sword'),
           Weapon(minAttack=7, maxAttack=10, name='Molten sword'),
           Weapon(minAttack=7, maxAttack=9, name='Fire sword'),
           Weapon(minAttack=10, maxAttack=12, name='Water sword'),
           Weapon(minAttack=12, maxAttack=14, name='Viking sword'),
           Weapon(minAttack=15, maxAttack=17, name='Mithril sword')
           ]

monsters = [
    Monster('orc', 10, 1, 2, potions + armors + weapons, exp=3, level=1),
    Monster('harpy', 12, 2, 3, potions + armors + weapons, exp=5, level=2),
    Monster('wolf', 15, 3, 4, potions + armors + weapons, exp=10, level=3),
    Monster('bear', 20, 4, 6, potions + armors + weapons, exp=12, level=4),
    Monster('bandit', 20, 5, 8, potions + armors + weapons, exp=15, level=5),
    Monster('wizard', 15, 10, 11, potions + armors + weapons, exp=18, level=6),
    Monster('griffon', 25, 10, 11, potions + armors + weapons, exp=20, level=7),
    Monster('medusa', 25, 12, 14, potions + armors + weapons, exp=25, level=8),
    Monster('dragon', 50, 15, 20, potions + armors + weapons, exp=30, level=10),
]