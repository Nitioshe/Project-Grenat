import random
import time
from core.loader import load_zone
from classes.monster import Monster
from combat.battle import battle

def Forest(player, inventory):
    zone = load_zone("Zones/Forest.json")
    monsters_data = zone.get("monsters", [])

    monsters = [
        Monster(m["name"], m["health"], m["attack"], m["exp_reward"], m["drop"])
        for m in monsters_data
    ]

    monster = random.choice(monsters)
    monster.display_stats()

    result = battle(player, monster)

    if result:
        print("You survived the forest.")
    else:
        print("Game Over.")
