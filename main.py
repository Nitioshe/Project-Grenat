import json
from ui.intro import start_animation
from classes.player import Player
from classes.inventory import Inventory
from zones.tettno import Tettno_main
from zones.forest import Forest
from zones.bank import Bank
from zones.guild import AdventurersGuild

def create_character():
    name = input("Name: ") or "Numa"
    race = input("Race (Human/Elf/Dwarf): ").capitalize()
    player_class = input("Class (Mage/Rogue/Samuraï): ").capitalize()
    return Player(name, race, player_class)

def main():
    start_animation()

    inventory = Inventory()
    inventory.load()

    player = create_character()

    while True:
        dest = Tettno_main(player, inventory)

        if dest == "1":
            Forest(player, inventory)
        elif dest == "2":
            Bank(player, inventory)
        elif dest == "3":
            AdventurersGuild(player, inventory)

if __name__ == "__main__":
    main()
