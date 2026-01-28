from skills.enemy import VenomBite

class Monster:
    def __init__(self, name, health, attack, exp_reward, drop):
        self.name = name
        self.health = health
        self.attack = attack
        self.exp_reward = exp_reward
        self.drop = drop

        self.skills = []
        if self.name == "Corrupted Wolf":
            self.skills.append(VenomBite())

        self.status_effect = []

    def display_stats(self):
        print(f"{self.name} - Health: {self.health}, Attack: {self.attack}")
