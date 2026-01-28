from skills.mage import Fireball, Healing
from skills.rogue import Backstab
from skills.samurai import Iaijutsu

SKILL_REGI = {
    "Fireball": Fireball,
    "Heal": Healing,

    "Backstab": Backstab,

    "Iaijutsu": Iaijutsu
}

def create_skill(name):
    if name not in SKILL_REGI:
        raise ValueError("Unknown skill:{name}")
    return SKILL_REGI[name]()