import time
from core.loader import load_zone
from core.state import GameState

def Tettno_main(player, inventory):
    load_zone("Zones/Tettno.json")
    time.sleep(1)

    print("1. Talk\n2. Inventory\n3. Go elsewhere")
    choice = input("> ")

    if choice == "1":
        print("Story not available yet.")
        return Tettno_main(player, inventory)

    if choice == "2":
        try: 
            inventory.display_inventory()
            return Tettno_main(player, inventory)
        except AttributeError:
            print("Une erreur est survenue lors de l'utilisation, module 'classes.inventory' has no attribute 'display_inventory'")
        return Tettno_main(player, inventory)

    if choice == "3":
        print("1. Forest\n2. Bank\n3. Guild\nq. Quit")
        dest = input("> ")
        if dest == "1":
            return GameState.FOREST
        elif dest == "2":
            return GameState.BANK
        elif dest == "3":
            return GameState.GUILD
        elif dest == "q":
            return GameState.EXIT
        return GameState.TOWN
