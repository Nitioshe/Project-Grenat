from skills.base import Skills
import random

class Fireball(Skills):
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