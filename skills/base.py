class Skills:
    def __init__(self, name, cost=0, cooldown=0):
        self.name = name
        self.cost = cost
        self.cooldown = cooldown
        self.current_cd = 0

    def can_use(self, player):
        return self.current_cd == 0

    def start_cooldown(self):
        self.current_cd = self.cooldown

    def reduce_cooldown(self):
        if self.current_cd > 0:
            self.current_cd -= 1

    def use(self, player, target):
        raise NotImplementedError("Skill not implemented")