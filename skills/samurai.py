from skills.base import Skills
import random

class Iaijutsu(Skills):
    def __init__(self):
        super().__init__("Iaijutsu", cost=1, cooldown=3)

    def can_use(self, player):
        return player.dexterity >= self.cost and super().can_use(player)

    def use(self, player, target):
        player.dexterity -= self.cost
        damage = random.randint(20, 30)
        target.health -= damage
        self.start_cooldown()
        print(f"{player.name} exécute Iaijutsu et inflige {damage} dégâts")
