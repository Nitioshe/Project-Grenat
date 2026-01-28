from skills.base import Skills
from combat.status import Poison
import random

class VenomBite(Skills):
    def __init__(self):
        super().__init__("Venom Bite", cooldown=3)
    
    def use(self, monster, target):
        damage = random.randint(5, 10)
        target.health -= damage
        target.status_effects.append(Poison())
        self.start_cooldown()
        print("{monster.name} poisons {target.name}")