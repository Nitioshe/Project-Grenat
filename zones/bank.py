from core.loader import load_zone

def Bank(player, inventory):
    load_zone("Zones/bank.json")

    print("1. Deposit (WIP)\n2. Withdraw (WIP)\n3. Back")
    choice = input("> ")

    if choice == "3":
        return "back"
