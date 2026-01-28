"""
Docstring for skills.mage
"""
import random
from skills.base import Skills

class Fireball(Skills):
    """
    Docstring for Fireball
    """
    def __init__(self):
        super().__init__("Fireball", cost=5, cooldown=2)

    def can_use(self, player):
        return player.mana >= self.cost and super().can_use(player)

    def use(self, player, target):
        player.mana -= self.cost
        damage = random.randint(15, 25)
        target.health -= damage
        self.start_cooldown()
        print(f"{player.name} cast a fireball and deals {damage} damages !")

class Healing(Skills):
    """
    Docstring for Healing
    """
    def __init__(self):
        super().__init__("Heal", cost=10, cooldown=3)

    def can_use(self, player):
        return player.mana >= self.cost and super().can_use(player)

    def use(self, player, target):

        player.mana -= self.cost
        lifeheal = player.max_health * 0.15
        player.health += lifeheal

        if player.health > player.max_health :
            player.health = player.max_health

        self.start_cooldown()
        print(f"{player.name} cast heal and gain {lifeheal} hp.")
