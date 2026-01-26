import time
from core.loader import load_zone
from core.state import GameState


def Tettno_main(player):
    load_zone("Zones/Tettno.json")
    time.sleep(1)

    print("1. Talk\n2. Inventory\n3. Go elsewhere\nq. Quit")

    choice = input("> ")

    if choice == "1":
        print("Story not available yet.")
        return GameState.TOWN

    elif choice == "2":
        player.inventory.display_inventory()
        input("Press Enter to continue...")
        return GameState.TOWN

    elif choice == "3":
        print("1. Forest\n2. Bank\n3. Guild\n0. Back")

        dest = input("> ")

        if dest == "1":
            return GameState.FOREST
        elif dest == "2":
            return GameState.BANK
        elif dest == "3":
            return GameState.GUILD
        else:
            return GameState.TOWN

    elif choice == "q":
        return GameState.EXIT

    return GameState.TOWN
