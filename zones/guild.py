from core.loader import load_zone
from core.game import GameState

def AdventurersGuild(player, inventory):
    load_zone("Zones/adventurer_guild.json")

    print("1. Talk\n2. Inventory\n3. Back")
    choice = input("> ")

    if choice == "1":
        print("Story not available")
    elif choice == "2":
        try:
            inventory.display_inventory()
        except AttributeError :
            print("Err, Attribut Err")
    elif choice == "3":
        return GameState.TOWN

    return "back"
