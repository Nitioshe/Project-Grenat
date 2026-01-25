from core.loader import load_zone

def AdventurersGuild(player, inventory):
    load_zone("Zones/adventurer_guild.json")

    print("1. Talk\n2. Inventory\n3. Back")
    choice = input("> ")

    if choice == "2":
        inventory.display_inventory()

    return "back"
