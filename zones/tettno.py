import time
from core.loader import load_zone

def Tettno_main(player, inventory):
    load_zone("Zones/Tettno.json")
    time.sleep(1)

    print("1. Talk\n2. Inventory\n3. Go elsewhere")
    choice = input("> ")

    if choice == "1":
        print("Story not available yet.")
        return Tettno_main(player, inventory)

    if choice == "2":
        inventory.display_inventory()
        return Tettno_main(player, inventory)

    if choice == "3":
        print("1. Forest\n2. Bank\n3. Guild")
        dest = input("> ")
        return dest
