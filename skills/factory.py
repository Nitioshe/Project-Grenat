from skills.mage import Fireball, Healing
from skills.rogue import Backstab, PoisonStrike
from skills.samurai import Iaijutsu, QuickSlash
from skills.warrior import LightBarrier

SKILL_REGI = {
    "Fireball": Fireball,
    "Heal": Healing,

    "Backstab": Backstab,
    "PoisonStrike": PoisonStrike,

    "Iaijutsu": Iaijutsu,
    "QuickSlash": QuickSlash,

    "LightBarrier": LightBarrier,

}

def create_skill(name):
    if name not in SKILL_REGI:
        raise ValueError("Unknown skill:{name}")
    return SKILL_REGI[name]()