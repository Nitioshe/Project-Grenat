"""
Docstring for classes.player
    Player class module
"""
from classes.inventory import Inventory
from core.audio import jouer_bruit

from skills.factory import create_skill
from combat.status_factory import create_status

from skills.mage import Fireball, Healing
from skills.rogue import Backstab, PoisonStrike
from skills.samurai import Iaijutsu, QuickSlash
from skills.warrior import LightBarrier

SKILL_DICT = {
    "Mage": {
        2: Healing,
        5: Fireball,
    },
    "Rogue": {
        2: Backstab,
        5: PoisonStrike,
    },
    "Samurai": {
        2: Iaijutsu,
        5: QuickSlash,
    },
    "Warrior": {
        2: LightBarrier
    },
}


class Player:
    """
    Docstring for Player
    """
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

        self.skills = []

        self.unlock_skills()

        self.mana = self.maxmana = 20 if player_class == "Mage" else 0
        self.agility = self.maxagility = 2 if player_class == "Rogue" else 0
        self.dexterity = self.maxdexterity = 2 if player_class == "Samurai" else 0
        self.dexterity = self.maxdexterity = 2 if player_class == "Warrior" else 0

        self.status_effect = []
        self.stunned = False

        self.inventory = Inventory()

    def unlock_skills(self):
        """
        Débloque les skills à niveau.
        """
        class_skills = SKILL_DICT.get(self.player_class, {})

        for level, skill_class in class_skills.items():
            if self.level >= level:
                skill = skill_class()

                if not self.has_skill(skill.name):
                    self.skills.append(skill)

    def has_skill(self, skill_name):
        """
        Verif possesion skill
        """
        return any(skill.name ==skill_name for skill in self.skills)

        

    def display_stats(self):
        """
        Docstring for display_stats
        
        :param self: player character
        """
        print("\n╔===---=== Stats Menu ===---===╗")
        print(f"    {self.name} (Lvl {self.level}) - {self.race} {self.player_class}")
        print(f"    HP: {self.health}/{self.max_health} | ATK: {self.attack}")

        if self.player_class == "Mage":
            print(f"    Mana: {self.mana}/{self.maxmana}")

        elif self.player_class == "Rogue":
            print(f"    Agility: {self.agility}/{self.maxagility}")

        elif self.player_class == "Samurai":
            print(f"    Dexterity: {self.dexterity}/{self.maxdexterity}")

        elif self.player_class == "Warrior":
                    print(f"    Dexterity: {self.dexterity}/{self.maxdexterity}")

        print("╚===---=== Stats Menu ===---===╝\n")

    def level_up(self):
        """
        Docstring for level_up
        
        :param self: player character
        """
        while self.exp >= self.exp_needed and self.level < 90:
            self.level += 1
            self.exp -= self.exp_needed
            self.exp_needed *= 2

            self.max_health += 20
            self.health += 20
            self.attack += 5

            self.unlock_skills()

            print(f"\n{self.name} has reached lvl {self.level} !\n")
            jouer_bruit("Sound Effect/levelup-sound.wav")

    # =======================
    # SAVE / LOAD
    # =======================

    def to_dict(self):
        """
        Docstring for to_dict
        
        :param self: player character
        """
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
            "mana": self.mana,
            "maxmana": self.maxmana,
            "agility": self.agility,
            "maxagility": self.maxagility,
            "dexterity": self.dexterity,
            "maxdexterity": self.maxdexterity,
            "skills": [skill.to_dict() for skill in self.skills],
            "status_effects": [s.to_dict() for s in self.status_effect],
        }

    @staticmethod # deco
    
    def from_dict(data):
        """
        Docstring for from_dict
        
        :param data: data of player
        """
        player = Player(
            data["name"],
            data["race"],
            data["player_class"]
        )

        player.level = data["level"]
        player.health = data["health"]
        player.max_health = data["max_health"]
        player.attack = data["attack"]
        player.exp = data["exp"]
        player.exp_needed = data["exp_needed"]

        player.mana = data.get("mana", 0)
        player.maxmana = data.get("maxmana", 0)
        player.agility = data.get("agility", 0)
        player.maxagility = data.get("maxagility", 0)
        player.dexterity = data.get("dexterity", 0)
        player.maxdexterity = data.get("maxdexterity", 0)

        player.load_skills(data.get("skills", []))

        return player

    def load_skills(self, skills_data):
        self.skills = []
        for s in skills_data:
            skill = create_skill(s["name"])
            skill.load_state(s)
            self.skills.append(skill)

    def load_status(self, status_data):
        self.status_effect = []
        for s in status_data:
            status = create_status(s["name"], s["duration"])
            self.status_effect.append(status)