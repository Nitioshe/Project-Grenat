from classes.inventory import Inventory
from core.audio import jouer_bruit

class Player:
    def __init__(self, name, race, player_class):
        self.name = name
        self.race = race
        self.player_class = player_class
        self.level = 1
        self.max_health = 100
        self.health = 100
        self.attack = 10
        self.exp = 0
        self.exp_needed = 100

        self.mana = self.maxmana = 20 if player_class == "Mage" else 0
        self.agility = self.maxagility = 2 if player_class == "Rogue" else 0
        self.dexterity = self.maxdexterity = 2 if player_class == "Samuraï" else 0

        self.inventory = Inventory()

    def display_stats(self):
        print(f"{self.name} (Lvl {self.level}) - {self.race} {self.player_class}")
        print(f"HP: {self.health}/{self.max_health} | ATK: {self.attack}")

    def level_up(self):
        while self.exp >= self.exp_needed and self.level < 90:
            self.level += 1
            self.exp -= self.exp_needed
            self.exp_needed *= 2
            self.max_health += 20
            self.health += 20
            self.attack += 5
            jouer_bruit("Sound Effect/levelup-sound.mp3")

    def to_dict(self):
        return {
            "name": self.name,
            "race": self.race,
            "player_class": self.player_class,
            "level": self.level,
            "health": self.health,
            "max_health": self.max_health,
            "attack": self.attack,
            "exp": self.exp,
            "exp_needed": self.exp_needed,
        }

