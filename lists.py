from equipment import Armor, Weapon
from item import HealingPotion
from monster import Monster

# POTIONS
potions = [HealingPotion(10), HealingPotion(15), HealingPotion(5)]

# ARMORS
armorlvl1 = Armor(name='Wooden armor', defense=1)
armorlvl2 = Armor(name='Silver armor', defense=2)
armorlvl3 = Armor(name='Iron armor', defense=3),
armorlvl4 = Armor(name='Steel armor', defense=4),
armorlvl5 = Armor(name='Molten armor', defense=5),
armorlvl6 = Armor(name='Fire armor', defense=6),
armorlvl7 = Armor(name='Water armor', defense=7),
armorlvl8 = Armor(name='Viking armor', defense=8),
armorlvl9 = Armor(name='Mithril armor', defense=10),

# WEAPONS
weaponlvl1 = Weapon(minAttack=1, maxAttack=3, name='Wooden sword')
weaponlvl2 = Weapon(minAttack=3, maxAttack=5, name='Silver sword')
weaponlvl3 = Weapon(minAttack=3, maxAttack=7, name='Iron sword')
weaponlvl4 = Weapon(minAttack=5, maxAttack=7, name='Steel sword')
weaponlvl5 = Weapon(minAttack=7, maxAttack=10, name='Molten sword')
weaponlvl6 = Weapon(minAttack=7, maxAttack=9, name='Fire sword')
weaponlvl7 = Weapon(minAttack=10, maxAttack=12, name='Water sword')
weaponlvl8 = Weapon(minAttack=12, maxAttack=14, name='Viking sword')
weaponlvl9 = Weapon(minAttack=15, maxAttack=17, name='Mithril sword')

# all available monsters, monsters drop loot appropriate for their level
monsters = [
    Monster('orc', 10, 1, 2, potions + [armorlvl1, weaponlvl1], exp=3, level=1),
    Monster('harpy', 12, 2, 3, potions + [armorlvl2, armorlvl1, weaponlvl1, weaponlvl2], exp=5, level=2),
    Monster('wolf', 15, 3, 4, potions + [armorlvl2, armorlvl3, weaponlvl2, weaponlvl3], exp=10, level=3),
    Monster('bear', 20, 4, 6, potions + [armorlvl3, armorlvl4, weaponlvl3, weaponlvl4], exp=12, level=4),
    Monster('bandit', 20, 5, 8, potions + [armorlvl4, armorlvl5, weaponlvl4, weaponlvl5], exp=15, level=5),
    Monster('wizard', 15, 10, 11, potions + [armorlvl5, armorlvl6, weaponlvl5, weaponlvl6], exp=18, level=6),
    Monster('griffon', 25, 10, 11, potions + [armorlvl6, armorlvl7, weaponlvl6, weaponlvl7], exp=20, level=7),
    Monster('medusa', 25, 12, 14, potions + [armorlvl7, armorlvl8, armorlvl9, weaponlvl7, weaponlvl8, armorlvl9], exp=25, level=8),
    Monster('dragon', 50, 15, 20, [armorlvl9, weaponlvl9], exp=30, level=10),
]