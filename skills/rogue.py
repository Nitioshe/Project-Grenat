from skills.base import Skills
import random

class Backstab(Skills):
    def __init__(self):
        super().__init__("Backstab", cost=1, cooldown=2)

    def can_use(self, player):
        return player.agility >= self.cost and super().can_use(player)

    def use(self, player, target):
        player.agility -= self.cost
        damage = random.randint(10, 20) * 2
        target.health -= damage
        self.start_cooldown()
        print(f"{player.name} frappe dans le dos pour {damage} dégâts")
