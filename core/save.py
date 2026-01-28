"""
Docstring for core.save
    Save & Load module logic
"""
import json
from classes.player import Player
from classes.inventory import Inventory

SAVE_FILE = "Saves/save.json"


def save_game(player):
    """
    Save game logic
    """
    data = player.to_dict()

    # inventaire
    data["inventory"] = player.inventory.items

    # skills
    data["skills"] = [s.to_dict() for s in player.skills]

    # status effects
    data["status_effect"] = [s.to_dict() for s in player.status_effect]

    with open(SAVE_FILE, "w", encoding="utf8") as f:
        json.dump(data, f, indent=4)


def load_game():
    """
    Load game logic
    """
    try:
        with open(SAVE_FILE, "r", encoding="utf8") as f:
            data = json.load(f)

        player = Player.from_dict(data)

        # inventaire
        inventory = Inventory()
        inventory.items = data.get("inventory", {})
        player.inventory = inventory

        # skills
        player.load_skills(data.get("skills", []))

        # status effects
        player.load_status(data.get("status_effects", []))

        return player

    except FileNotFoundError:
        return None
    except (KeyError, ValueError):
        print("Error: corrupted save file")
        return None
