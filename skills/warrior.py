"""
Docstring for skills.mage
"""
import random
from skills.base import Skills
from core.audio import jouer_bruit

class LightBarrier(Skills):
    """
    Docstring for Healing
    """
    def __init__(self):
        super().__init__("LightBarrier", cost=10, cooldown=3)

    def can_use(self, player):
        return player.dexterity >= self.cost and super().can_use(player)

    def use(self, player, target):

        player.dexterity -= self.cost
        lifeheal = player.max_health * 0.15
        player.health += lifeheal

        if player.health > player.max_health :
            player.health = player.max_health

        self.start_cooldown()
        jouer_bruit("Sound Effect/heal-sound.wav")
        print(f"{player.name} cast heal and gain {lifeheal} hp.")
