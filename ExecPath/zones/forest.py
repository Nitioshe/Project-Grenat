import random
import time
from core.loader import load_zone
from classes.monster import Monster
from combat.battle import battle
from core.state import GameState

def Forest(player):
    zone = load_zone("Zones/Forest.json")
    monsters_data = zone.get("monsters", [])

    monsters = [
        Monster(m["name"], m["health"], m["attack"], m["exp_reward"], m["drop"])
        for m in monsters_data
    ]

    monster = random.choice(monsters)
    monster.display_stats()

    print("1. Explore\n2. Back to city")

    choice = input("> ")

    if choice == "1":
        return GameState.COMBAT, monster
    elif choice == "2":
        return GameState.TOWN
    
    return GameState.FOREST
