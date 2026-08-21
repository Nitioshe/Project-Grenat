"""
Docstring for skills.warrior
"""
import random
from skills.base import Skills
from core.audio import jouer_bruit

class LightBarrier(Skills):
    """
    Docstring for LightBarrier
    """
    def __init__(self):
        super().__init__("LightBarrier", cost=1, cooldown=3)
        self.barrier_turns = 0

    def can_use(self, player):
        return player.dexterity >= self.cost and super().can_use(player)

    def use(self, player, target):

        player.dexterity -= self.cost
        self.barrier_turns = 2

        self.start_cooldown()

        print(f"{player.name} uses Light Barrier!")
        print("Light Barrier is active for 2 turns.")

        def reduce_damage(self, damage):
            """
                Reduction degat par barriere
            """
            if self.barrier_turns <= 0:
                return damage
            if self.barrier_turns == 2:
                reduced_damage = 0
                print("LightBarrier blocks all damages!")
            else:
                reduced_damage = int(damage * 0.25)
                print(f"Light Barrier blocks 75% of the damages!")
                print(f"{damage} -> {reduced_damage}")

            self.barrier_turns -=1

            return reduced_damage
