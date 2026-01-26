from core.loader import load_zone
from core.state import GameState

def Bank(player):
    load_zone("Zones/bank.json")

    print("1. Deposit (WIP)\n2. Withdraw (WIP)\n3. See Inventory\n4. Back")
    choice = input("> ")

    if choice == "1":
        print("Not available")
        return GameState.BANK
    elif choice == "2":
        print("Not available")
        return GameState.BANK
    elif choice == "3":
        player.inventory.display_inventory()
        input("Press Enter to continue...")
        return GameState.TOWN
    elif choice == "":
        print("Not available")
        return GameState.BANK
    return GameState.BANK
