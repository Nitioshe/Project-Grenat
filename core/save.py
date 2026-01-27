"""
Docstring for core.save
    Save & Save Loading module logic
"""
import json
from classes.player import Player
from classes.inventory import Inventory

SAVE_FILE = "Saves/save.json"


def save_game(player, inventory):
    """
    Docstring for save_game
    
    :param player: using player data
    :param inventory: using player inventory data
        Save logic
    """
    data = {
        "player": player.to_dict(),
        "inventory": inventory.items
    }

    with open(SAVE_FILE, "w", encoding="utf8") as f:
        json.dump(data, f, indent=4)


def load_game():
    """
    Docstring for load_game
        Save Loading logic
    """
    try:
        with open(SAVE_FILE, "r", encoding="utf8") as f:
            data = json.load(f)

        player = Player.from_dict(data["player"])

        inventory = Inventory()
        inventory.items = data.get("inventory", {})

        player.inventory = inventory

        return player, inventory

    except FileNotFoundError:
        return None, None
    except KeyError:
        print("Err, BadFile or Method")
        return "new"
