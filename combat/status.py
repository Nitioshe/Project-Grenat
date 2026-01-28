class StatusEffect:
    def __init__(self, name, duration):
        self.name = name
        self.duration = duration

        def apply(self, target):
            pass

        def on_turn_start(self, target):
            pass

        def tick(self):
            self.duration -= 1
            return self.duration <= 0
        
class Poison(StatusEffect):
    def __init__(self, duration=3, damage=2):
        super().__init__("Poison", duration)
        self.damage = damage

    def on_turn_start(self, target):
        target.health -= self.damage
        print(f"{target.name} take {self.damage} poison damage")

class Stun(StatusEffect):
    def __init__(self, duration=1):
        super().__init__("Stun", duration)

    def apply(self, target):
        target.stunned = True
